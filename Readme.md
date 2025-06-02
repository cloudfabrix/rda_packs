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

## Latest Versions of RDA Packs


| RDA Pack Name | RDA Pack Version | Description |
|---------------|------------------|-------------|
| [Base Pack](https://github.com/cloudfabrix/rda_packs/tree/main/Base%20Pack/5.0.0) | 5.0.0 | This pack contains the artifacts that are common to the inventory collection packs that depend on them: |
| [Cisco Catalyst Center](https://github.com/cloudfabrix/rda_packs/tree/main/Cisco%20Catalyst%20Center/9.0.1) | 9.0.1 | This pack is designed for inventory collection for Cisco Catalyst Center.   |
| [Cisco Meraki](https://github.com/cloudfabrix/rda_packs/tree/main/Cisco%20Meraki/9.0.2) | 9.0.2 | Cisco Meraki pack is designed for inventory collection for Meraki using **Meraki-Networks** . |
| [Cisco Prime Infrastructure](https://github.com/cloudfabrix/rda_packs/tree/main/Cisco%20Prime%20Infrastructure/9.0.0) | 9.0.0 | This pack is designed for inventory collection for prime clients report using the following bots:   |
| [Cisco vManage](https://github.com/cloudfabrix/rda_packs/tree/main/Cisco%20vManage/9.0.1) | 9.0.1 | Cisco vManage pack is designed for inventory collection for vManage using **query-api** bot. |
| [Fabrix AIOPs snmp](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOPs%20snmp/8.0.3) | 8.0.3 | Fabrix AIOPs SNMP Pack collects SNMP alerts. |
| [Fabrix AIOPs syslogs](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOPs%20syslogs/8.0.3) | 8.0.3 | Fabrix AIOPs syslogs Pack collects Syslog alerts. |
| [Fabrix AIOps Asset Correlation Regression](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Asset%20Correlation%20Regression/9.0.0) | 9.0.0 | This pack is designed to automate the systematic monitoring and analysis of asset-related metrics using the following bots: |
| [Fabrix AIOps Fault Management Base](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Fault%20Management%20Base/8.0.3) | 8.0.3 | Fabrix AIOps Fault Management Base solution package creates Alerts and Incidents |  
| [Fabrix AIOps ML Metrics Regression](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20ML%20Metrics%20Regression/9.0.0) | 9.0.0 | This pack is designed to automate the systematic monitoring and analysis of asset-related metrics for regression using the following bots: |
| [Fabrix AIOps Network Performance Management SNMP](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Network%20Performance%20Management%20SNMP/8.0.3) | 8.0.3 | Fabrix AIOps Network Performance Management SNMP Pack collects SNMP Metrics and displays in the KPI Workbench. |
| [Fabrix AIOps Network Performance Management Telemetry](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Network%20Performance%20Management%20Telemetry/8.0.3) | 8.0.3 | Fabrix AIOps Network Performance Management Telemetry Pack collects Telemetry Metrics and displays in the KPI Workbench. |
| [Fabrix Inventory Collection Base Pack](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20Inventory%20Collection%20Base%20Pack/7.0.0) | 7.0.0 | This pack contains the artifacts that are common to the inventory collection packs that depend on them. |
| [Linux and Windows Host OS](https://github.com/cloudfabrix/rda_packs/tree/main/Linux%20and%20Windows%20Host%20OS/3.0.0) | 3.0.0 | This pack is designed to do inventory collection for both Linux and Windows hosts using the following bots:   |
| [Multi Network Device Discovery](https://github.com/cloudfabrix/rda_packs/tree/main/Multi%20Network%20Device%20Discovery/1.0.0) | 1.0.0 | Multi Network Device Discovery solution package supports mutli networks and collects inventory data for network devices. |
| [Network Device Discovery](https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Device%20Discovery/8.0.3) | 8.0.3 | Network Device Discovery solution package collects inventory data for network devices. |
| [RDA Dashboard Training](https://github.com/cloudfabrix/rda_packs/tree/main/RDA%20Dashboard%20Training/1.0.0) | 1.0.0 | The RDA Dashboard Training Pack provides a comprehensive, hands-on learning experience for building dynamic dashboards using RDA’s powerful widget library. |
| [VMWare VeloCloud](https://github.com/cloudfabrix/rda_packs/tree/main/VMWare%20VeloCloud/8.0.0) | 8.0.0 | This pack is designed to collect inventory for VeloCloud. |
| [VMWare vCenter](https://github.com/cloudfabrix/rda_packs/tree/main/VMWare%20vCenter/9.0.2) | 9.0.2 | This pack is designed for inventory collection for vCenter. |
| [VMware vROps](https://github.com/cloudfabrix/rda_packs/tree/main/VMware%20vROps/9.0.1) | 9.0.1 | VMware vROps pack is designed for metric collection for VMware vROps.|

