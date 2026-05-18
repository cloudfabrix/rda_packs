
### Overview  
  
Network Suite is a comprehensive network management package that provides end-to-end network device discovery, inventory collection, performance monitoring, topology visualization, and log management. Following network device vendors are supported out of the box for inventory discovery. If needed, additional ones can be added.  
  
- Cisco (IOS, IOS-XR, NX-OS, SD-WAN/Viptela)  
- Juniper  
- Fortinet  

For SNMP-based performance metrics, the following vendors are additionally supported via Telegraf plugins:

- Arista
- Cisco (IOS, NX-OS)
- H3C
- HPE
- Juniper
- Viptela

This pack is designed for inventory collection for Network Devices using **asset-discovery** extension. Following bots are being called by this pack:

- **collector**
- **get-collection-files**

  
### Feature Summary  
  
Following are the key features covered by Network Suite solution package:  
  
- Network device discovery using SNMP and SSH for a given list of seed devices. The device IPs can be provided as single IPs, comma-separated, and/or ranges.
- Access verification checks for devices on a set schedule or on demand for selected devices.
- Run discovery on a set schedule for devices that have passed access verification checks or run discovery on demand for selected devices.
- Dashboards to see the statuses of access verification checks and discovery runs.
- Dashboards to visualize the inventory data collected for devices along with the drill downs to view assets and asset hierarchy.
- CDP/LLDP, OSPF, BGP, and ISIS topologies with interactive topology map, path visualization, and geomap views.
- SNMP performance metrics monitoring — CPU, memory, interface throughput, utilization, errors, discards, CRC/alignment/symbol errors, and PoE metrics.
- ICMP ping monitoring for reachability, latency, and packet loss.
- SSL certificate monitoring for expiry tracking.
- Net response metrics for port connectivity monitoring.
- Sensor metrics (temperature, voltage, fan status) and NTP status monitoring.
- Routing protocol metrics — OSPF neighbor/interface state and events, BGP peer state, messages, and updates.
- Syslog collection (UDP) with device enrichment.
- SNMP trap collection with device enrichment.
- SNMP entity physical inventory collection for hardware component details.
- Pre-configured alert rules for critical network metrics with automated notifications.
- Network topology relationship mapping and visualization capabilities.

NOTE: 
- Alert rules are included in this pack for CPU, memory, interface metrics, and device availability monitoring with configurable thresholds and notification channels.
- Additional SNMP trap-based alert rules include `interface_down` and `ospf_neighbor_state` for interface/link and OSPF neighbor-state monitoring.


### Pre-requisite Steps 
- Add arango template from the resources folder to path: `Main Menu -> Configuration -> RDA Administration -> Object store -> Upload`. Give Name as `rda_arango_templates` and Folder name as `arango_templates`<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Suite/1.0.0/resources" target="_blank">Click here for resources</a><br>
  - File: `resources/arango_templates/rda_arango_templates.yml`

### Manual Steps (Post Activation)

#### 1. Add Collection Rule

After the pack is activated, add the collection rule from the file `resources/collection_group/network.json`.<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Suite/1.0.0/resources/collection_group" target="_blank">Click here for collection group files</a><br>

Navigate to: `Main Menu` -> `Configuration` -> `RDA Administration` -> `Asset Discovery` -> `Collection Group Rules` -> Upload the `network.json` file.
  - File: `resources/collection_group/network.json`

This collection group defines the default inventory collection rules for all devices including vendor-specific SNMP group mappings for Cisco, Juniper, Fortinet, and other vendors.


#### 2. Add Data Models to Minio

Copy the following data model files from `resources/data_models/` to the Minio path `<tenant-id>/declarative-dataset-definitions/`:<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Suite/1.0.0/resources/data_models" target="_blank">Click here for data model files</a><br>

- `resources/data_models/interface_model.json`
- `resources/data_models/cdp_model.json`
- `resources/data_models/network_assets_model.json`

These data models define the declarative dataset definitions required for network device inventory and topology processing.


#### 3. Configure Plugins (Telegraf)

- Install Event-Gateway. Use `rdaf event_gateway install --tag <tag_name>`.<br>
  **Note**: Contact customer support to obtain the appropriate tag details for your environment.
- Add the following three fields in telegraf.conf in the path `/opt/rdaf/event_gateway/telegraf/config`<br>
  - In `[global_tags]`: `host_ip` and `projectid`<br>
  - In `[agent]`: `hostname`<br>
  Example: `host_ip = "10.95.109.130"`, `projectid = "a511a92b-1b74-11f1-97fc-0242ac120006"`, `hostname = "svc129.qa.engr.cloudfabrix.com"`
- Copy the required Telegraf config files from `resources/telegraf_config_files/` to path: `/opt/rdaf/event_gateway/telegraf/config/conf.d`<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Suite/1.0.0/resources/telegraf_config_files" target="_blank">Click here for Telegraf config files</a><br>

  **SNMP Metrics**:
  - `cisco_network_ios_snmp_metrics.conf`
  - `cisco_network_nxos_snmp_metrics.conf`
  - `arista_network_snmp_metrics.conf`
  - `h3c_network_snmp_metrics.conf`
  - `hpe_network_snmp_metrics.conf`
  - `juniper_network_snmp_metrics.conf`
  - `viptela_network_snmp_metrics.conf`

  **ICMP / SSL / Net Response Metrics:**
  - `icmp_ping_metrics.conf`
  - `ssl_certificate_metrics.conf`
  - `rda_net_response_metrics.conf`

  **Syslog / SNMP Trap Receivers:**
  - `rda_syslog_udp_events.conf`
  - `rda_snmp_trap_events.conf`

- The SNMP and ICMP plugins automatically read device targets from the `network_access_verification` pstream after access verification completes. No manual agent list configuration is required.
- The SSL and Port metrics plugins read targets from the `discovery` pstream based on the onboarded device entries.

#### 4. Configure Notification Profile

Navigate to: `Main Menu` -> `Configuration` -> `RDA Administration` -> `Alert Rules` -> `Notification Profiles` -> `Add`

- **Name**: `snmp_metrics_notification_profile`
- **Notification Channel**: Select `telegraf_snmp_metrics`
- Save the profile.

This notification profile is used by all alert rules in this pack to route alerts through the `asm_syslog_webhook` notification channel.

#### 4. Enable Alert Rules

Alert rules shipped with this pack are disabled by default. After activation, enable them as follows:

Navigate to: `Main Menu` -> `Configuration` -> `RDA Administration` -> `Alert Rules`

- Locate each alert rule from this pack in the list.
- Click the **three-dot** (⋮) on the row to open the row-level actions.
- Select **Enable** to activate the alert rule.

Repeat for each alert rule you want to enable.


### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    | Complete all steps listed in the Pre-requisite section above. |  
| 2    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack. |  
| 3    | Complete the Manual Steps (Post Activation) listed above — add the collection rule, copy data model files to Minio, configure the Telegraf plugins (SNMP, ICMP, SSL, Net Response, Syslog UDP, SNMP Trap), and configure the `snmp_metrics_notification_profile` notification profile. |  
| 4    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multitenant environment, the pack specific dashboards will be available in Customer Ops page. |     
| 5    | Use `Configure and Manage` -> `Network Credentials` to create credentials of type `snmp-cred`, `device-snmp-v1v2`, `device-snmp-v3`, `device-host-ssh`, `ssh-cred`, `network_device` with the correct values. |   
| 6    | Use `Configure and Manage` -> `Network Discovery Targets` to onboard Network Devices. Use `Add Devices` or `Import Devices`. **Add Devices** provides a form with toggles for: **Discovery** (IP Address, discovery_scope, CDP, LLDP, OSPF, BGP, ISIS), **ICMP Metrics** (IP Address), **SNMP Metrics** (IP Address), **SSL Metrics** (URL, e.g. `https://192.168.1.10:80`), and **Port Metrics** (URL and Protocol, e.g. `192.168.1.10:22`). **Import Devices** accepts a CSV file with a `type` column. Allowed values for `type`: `discovery`, `icmp_metrics`, `snmp_metrics`, `ssl_metrics`, `port_metrics`. Mandatory and optional fields per type: (1) **discovery** — Mandatory: `device_ip`, `discovery_scope`; Optional: `cdp_field`, `lldp_field`, `ospf_field`, `bgp_field`, `isis_field`. (2) **icmp_metrics** — Mandatory: `device_ip`. (3) **snmp_metrics** — Mandatory: `device_ip`. (4) **port_metrics** — Mandatory: `url_field`, `protocol`. (5) **ssl_metrics** — Mandatory: `url_field`. **Note:** Set cdp_field, lldp_field, ospf_field, bgp_field, or isis_field to 'yes' for devices for which the respective topology needs to be collected. **Note:** The `discovery_scope` field (Yes/No) controls which devices are included in the blueprint's automated scheduled discovery runs. Only devices with `discovery_scope` set to 'yes' will be automatically discovered according to the blueprint's schedule. | 
| 7    | Update `geo_location` dataset. Use `Configure and Manage` --> `Network Management` --> `Configure Artifacts` --> `Row Level Actions` --> `import` action. Upload the csv file. **Note:** `geo_location` dataset should have columns - device_hostname, latitude, longitude |  
| 8    | Under `Configure and Manage` -> `Run Discovery` -> `Run Access Verification` -> select the protocols ICMP, SSH as per requirement to perform the credential check for Network Devices. The verification results can be seen in `Status` -> `Network Access Status` dashboard page. **Note:** For scheduled pipeline, the option to control ICMP/SSH during access check is available in `Configure and Manage` --> `Network Management` --> `Configure Artifacts` --> `Row Level Actions` --> `Manage Data` --> `Row Level Actions` --> `Edit Row` --> `Save` --> `Commit Changes`. |  
| 9    | Use `Configure and Manage` -> `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Discovery` option. Use `Status` -> `Network Discovery Status` to view the device discovery status. |  
| 10   | After the collection completes successfully, use the pages under `Inventory` (`Network Assets`, `Network Hardware`, `Network Software`) to view the inventory details. Use `Metrics` (`Network Device Metrics`, `Network Overview`) to view device performance metrics. Use `Logs` (`Syslogs`, `SNMP Traps`) to view device logs and traps. |   
| 11   | Use `Topology` (`Network Topology`, `Path Visualization`, `Topology Geomap`) to view topology. |
   
