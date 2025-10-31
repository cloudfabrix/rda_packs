#!/usr/bin/env python3

import os
import json
import yaml
import urllib.parse
from packaging.version import Version

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PACKS_METADATA = []

for pack_name in os.listdir(REPO_ROOT):
    pack_path = os.path.join(REPO_ROOT, pack_name)
    if not os.path.isdir(pack_path) or pack_name == "metadata":
        continue

    for version in os.listdir(pack_path):
        version_path = os.path.join(pack_path, version)
        if not os.path.isdir(version_path):
            continue

        manifest_path = os.path.join(version_path, "manifest.yaml")
        description_path = os.path.join(version_path, "description.md")
        tar_file = next((f for f in os.listdir(version_path) if f.endswith(".tar.gz")), None)

        if not os.path.exists(manifest_path) or not os.path.exists(description_path) or not tar_file:
            continue

        with open(manifest_path) as mf:
            manifest = yaml.safe_load(mf)

        # Extract required_base_packs from manifest
        # If requires is commented out or doesn't exist, yaml.safe_load will return None
        required_base_packs = manifest.get("requires")
        
        # Format required_base_packs if it's a list
        if isinstance(required_base_packs, list):
            # Format as list of dictionaries with name and version
            formatted_requires = []
            for req in required_base_packs:
                if isinstance(req, dict):
                    formatted_requires.append({
                        "name": req.get("name", ""),
                        "version": req.get("version", "")
                    })
            required_base_packs = formatted_requires if formatted_requires else "None"
        else:
            # If requires is None, commented out, or doesn't exist, set to "None"
            required_base_packs = "None"

        description_text = manifest.get("name", "")  # fallback default
        # Initialize description path and fallback
        desc_file_path = None
        desc_cfg = manifest.get("description", {})

        if isinstance(desc_cfg, dict):
            md_path = desc_cfg.get("md")
            if md_path:
                if md_path.startswith("./"):
                    desc_file_path = os.path.join(version_path, md_path[2:])
                else:
                    desc_file_path = os.path.abspath(os.path.join(REPO_ROOT, md_path))
            elif "value" in desc_cfg:
                # If no md but value is provided
                description_text = str(desc_cfg["value"])

        # Fallback to default description.md only if text wasn't set from value
        if not desc_file_path and description_text == manifest.get("name", ""):
            desc_file_path = os.path.join(version_path, "description.md")

        if desc_file_path and os.path.exists(desc_file_path):
            with open(desc_file_path) as df:
                lines = [line.strip() for line in df if line.strip()]

            def extract_line(lines_iter):
                for line in lines_iter:
                    if line:
                        period_index = line.find(".")
                        return line[:period_index + 1] if period_index >= 0 else line
                return ""

            for i, line in enumerate(lines):
                if line.lower().startswith("#") and "overview" in line.lower():
                    description_text = extract_line(lines[i + 1:])
                    break
            else:
                description_text = extract_line(lines)

        # Escape double quotes
        description_text = description_text.replace('"', '\\"')
        metadata = {
            "pack_name": manifest.get("name"),
            "pack_version": manifest.get("version"),
            "tar_file_name": tar_file,
            "tar_file_url": f"https://raw.githubusercontent.com/cloudfabrix/rda_packs/main/{pack_name}/{version}/{tar_file}",
            "description": description_text,
            "required_fabric_services": manifest.get("fabric_services", [{"name":"api-server","version":">=8.0.0"},{"name":"worker","version":">=8.0.0"}]),
            "required_base_packs": required_base_packs,
        }

        PACKS_METADATA.append(metadata)
# Sort the metadata
PACKS_METADATA.sort(key=lambda x: (x["pack_name"].lower(), Version(x["pack_version"])), reverse=False)

# Ensure metadata directory exists
METADATA_DIR = os.path.join(REPO_ROOT, "metadata")
os.makedirs(METADATA_DIR, exist_ok=True)
# Write metadata
packs_metadata_path = os.path.join(METADATA_DIR, "packs_metadata.json")
with open(packs_metadata_path, "w") as outfile:
    json.dump(PACKS_METADATA, outfile, indent=2)

# Extract latest version of each pack
latest_packs = {}
for entry in PACKS_METADATA:
    name = entry["pack_name"]
    version = Version(entry["pack_version"])
    if name not in latest_packs or version > Version(latest_packs[name]["pack_version"]):
        latest_packs[name] = entry

# Write latest packs metadata
latest_packs_path = os.path.join(REPO_ROOT, "metadata", "latest_packs_meta.json")
with open(latest_packs_path, "w") as latest_file:
    json.dump(list(latest_packs.values()), latest_file, indent=2)

# ------------------------------
# Generate latest_packs.md
# ------------------------------

# Load latest_packs.json
with open(latest_packs_path) as f:
    latest_packs_list = json.load(f)

# Prepare Markdown table
md_lines = [
    "| RDA Pack Name | RDA Pack Version | Supported Fabrix Services | Required Base Packs | Description |",
    "|---------------|------------------|----------------------------|---------------------|-------------|"
]

for pack in latest_packs_list:
    pack_name = pack.get("pack_name", "")
    pack_version = pack.get("pack_version", "")
    description = pack.get("description", "").replace("|", "\\|")

    # Encode for GitHub URL
    encoded_pack_name = urllib.parse.quote(pack_name, safe='')
    encoded_version = urllib.parse.quote(pack_version, safe='')
    github_url = f"https://github.com/cloudfabrix/rda_packs/tree/main/{encoded_pack_name}/{encoded_version}"
    pack_name_md = f"[{pack_name}]({github_url})"

    services = pack.get("required_fabric_services", [])
    if isinstance(services, list):
        services_str = "<br>".join(f"{srv.get('name', '')} ({srv.get('version', '')})" for srv in services)
    else:
        services_str = str(services)

    services_str = services_str.replace("|", "\\|")

    # Format required_base_packs for markdown
    required_packs = pack.get("required_base_packs", "None")
    if isinstance(required_packs, list):
        required_packs_str = "<br>".join(f"{req.get('name', '')} ({req.get('version', '')})" for req in required_packs)
    elif required_packs == "None" or required_packs is None:
        required_packs_str = "None"
    else:
        required_packs_str = str(required_packs)
    
    required_packs_str = required_packs_str.replace("|", "\\|")

    md_lines.append(f"| {pack_name_md} | {pack_version} | {services_str} | {required_packs_str} | {description} |")

# Write the markdown file
latest_packs_md_path = os.path.join(METADATA_DIR, "latest_packs.md")
with open(latest_packs_md_path, "w") as md_file:
    md_file.write("\n".join(md_lines))