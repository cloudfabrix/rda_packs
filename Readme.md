# RDA Packs Repository

This repository contains various **packs**, each organized by name and version. The structure is designed to make it easy to find and download specific versions of a pack.

## Repository Structure
```text
<pack-name>/
└── <version>/
    ├── README.md                # Description and details about this specific pack version
    └── <filename>.tar.gz        # Compressed pack archive
```
- **`<pack-name>`**: The name of the pack.
- **`<version>`**: The version of the pack (e.g., `1.0.0`, `2.3.1`, etc.).  
Each version directory includes:
-- `README.md` file with version-specific information.
-- `.tar.gz` file containing the pack contents.
### Example:
```text
<Cisco Meraki>/
└── <9.0.0>/
    ├── README.md                # Description and details about this specific pack version
    └── meraki_pack.tar.gz       # Compressed pack archive
```
## Downloading and Deploying a Pack

To use a specific pack:
1. Navigate to the desired pack and version directory.
2. Download the corresponding `.tar.gz` file.
3. Follow the instructions in the [RDA Packs Deployment Guide](https://bot-docs.cloudfabrix.io/beginners_guide/rda_packs/#6-rda-packs-deployment-steps) to upload and deploy the pack.

