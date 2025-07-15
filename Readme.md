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

| RDA Pack Name | RDA Pack Version | Supported Fabrix Services | Description |
|---------------|------------------|----------------------------|-------------|
| [Cisco Meraki](https://github.com/cloudfabrix/rda_packs/tree/main/Cisco%20Meraki/9.0.2) | 9.0.2 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | Cisco Meraki pack is designed for inventory collection for Meraki using **Meraki-Networks** . |
| [Cisco vManage](https://github.com/cloudfabrix/rda_packs/tree/main/Cisco%20vManage/9.0.1) | 9.0.1 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | Cisco vManage pack is designed for inventory collection for vManage using **query-api** bot. |
| [Fabrix AIOPs snmp](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOPs%20snmp/9.0.0) | 9.0.0 | worker >=8.1.0, <br>api-server >=8.1.0, <br>alert-processor >=8.1.0, <br>alert-ingester >=8.1.0, <br>alert-correlator >=8.1.0, <br>cfxdimensions-app-irm_service >=8.1.0, <br>cfxdimensions-app-collaboration >=8.1.0 | Fabrix AIOPs SNMP Pack collects SNMP alerts. |
| [Fabrix AIOPs syslogs](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOPs%20syslogs/9.0.0) | 9.0.0 | worker >=8.1.0, <br>api-server >=8.1.0, <br>alert-processor >=8.1.0, <br>alert-ingester >=8.1.0, <br>alert-correlator >=8.1.0, <br>cfxdimensions-app-irm_service >=8.1.0, <br>cfxdimensions-app-collaboration >=8.1.0 | Fabrix AIOPs syslogs Pack collects Syslog alerts. |
| [Fabrix AIOps Asset Correlation Regression](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Asset%20Correlation%20Regression/9.0.1) | 9.0.1 | api-server >=8.1.0 | This pack is designed to automate the systematic monitoring and analysis of asset-related metrics using the following bots: |
| [Fabrix AIOps BulkStats](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20BulkStats/9.0.0) | 9.0.0 | api-server >=8.1.0 | This pack is designed to automate the systematic monitoring and analysis of asset-related metrics using the following bots: |
| [Fabrix AIOps Fault Management Base](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Fault%20Management%20Base/9.0.13) | 9.0.13 | worker >=8.1.0, <br>api-server >=8.1.0, <br>alert-processor >=8.1.0, <br>alert-ingester >=8.1.0, <br>alert-correlator >=8.1.0, <br>cfxdimensions-app-irm_service >=8.1.0, <br>cfxdimensions-app-collaboration >=8.1.0 | Fabrix AIOps Fault Management Base solution package creates Alerts and Incidents |
| [Fabrix AIOps ML](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20ML/9.0.0) | 9.0.0 | api-server >=8.1.0 | This pack is designed for experimenting for Users: |
| [Fabrix AIOps ML Metrics Regression](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20ML%20Metrics%20Regression/9.0.0) | 9.0.0 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | This pack is designed to automate the systematic monitoring and analysis of asset-related metrics for regression using the following bots: |
| [Fabrix AIOps Network Performance Management SNMP](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Network%20Performance%20Management%20SNMP/8.0.3) | 8.0.3 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | **Fabrix AIOps Network Performance Management SNMP Pack** |
| [Fabrix AIOps Network Performance Management Telemetry](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Network%20Performance%20Management%20Telemetry/8.0.3) | 8.0.3 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | **Fabrix AIOps Network Performance Management Telemetry Pack** |
| [Fabrix Inventory Collection Base Pack](https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20Inventory%20Collection%20Base%20Pack/7.2.0) | 7.2.0 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | This pack contains the following artifacts that are common to the inventory collection packs that depend on them: |
| [Linux and Windows Host OS](https://github.com/cloudfabrix/rda_packs/tree/main/Linux%20and%20Windows%20Host%20OS/3.0.0) | 3.0.0 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | This pack is designed for single-tenant deployments and inventory collection for both Linux and Windows hosts using the following bots: |
| [Multi Network Device Discovery](https://github.com/cloudfabrix/rda_packs/tree/main/Multi%20Network%20Device%20Discovery/1.0.1) | 1.0.1 | worker >=8.1.0, <br>api-server >=8.1.0 | Multi Network Device Discovery solution package supports mutli networks and collects inventory data for network devices. |
| [Network Device Discovery](https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Device%20Discovery/9.0.0) | 9.0.0 | worker >=8.1.0, <br>api-server >=8.1.0 | Network Device Discovery solution package collects inventory data for network devices. |
| [RDA Dashboard Training](https://github.com/cloudfabrix/rda_packs/tree/main/RDA%20Dashboard%20Training/2.0.0) | 2.0.0 | api-server >=8.1.0, <br>collector >=8.1.0 | The RDA Dashboard Training Pack provides a comprehensive, hands-on learning experience for building dynamic dashboards and understanding key RDA concepts. |
| [VMWare VeloCloud](https://github.com/cloudfabrix/rda_packs/tree/main/VMWare%20VeloCloud/8.0.0) | 8.0.0 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | This pack is designed to collect inventory for VeloCloud by calling the following APIs: |
| [VMWare vCenter](https://github.com/cloudfabrix/rda_packs/tree/main/VMWare%20vCenter/9.0.2) | 9.0.2 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | This pack is designed for inventory collection for vCenter using the following bots: |
| [VMware vROps](https://github.com/cloudfabrix/rda_packs/tree/main/VMware%20vROps/9.0.1) | 9.0.1 | api-server >=8.0.0, <br>rda_worker >=8.0.0 | VMware vROps pack is designed for metric collection for VMware vROps using the following bots: |

