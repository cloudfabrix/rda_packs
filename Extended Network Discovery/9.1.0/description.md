
### Overview  
  
Fabrix.ai Extended Network Device Discovery supports SNMP- and SSH-based discovery of multi-vendor enterprise and service-provider IP network infrastructure, including campus and branch switches, routers, SD-WAN edges, wireless infrastructure, security gateways, ADC/load-balancing platforms, and IP/MPLS service-edge devices across leading network vendors. In addition to protocol-based discovery and inventory collection, the pack can use SSH login to gather device CLI output and internally leverages TextFSM templates to parse commands and extract device features, configurations, and operational parameters. Discovery depth can vary by platform based on enabled protocols, exposed MIBs, device credentials, CLI access, and available parsing coverage. 
  
| Network Vendor | Platforms / Hardware | OS |
|---|---|---|
| Cisco | Catalyst switches, Nexus switches, ISR / ASR / NCS routers, Catalyst 8000 SD-WAN edge platforms, Catalyst 9800 wireless controllers, Meraki MR / MS / MX, Secure Firewall / Firepower | IOS, IOS XE, IOS XR, NX-OS, Meraki cloud platform, Secure Firewall Threat Defense, FXOS |
| Juniper Networks | EX, QFX, MX, ACX, PTX, SRX, Mist-managed wireless | JUNOS |
| HPE Aruba Networking | CX campus/data-center switches, wireless APs, gateways, controllers | AOS-CX, ArubaOS, AOS 10 |
| Extreme Networks | ExtremeSwitching campus/data-center switches, fabric deployments, wireless infrastructure | ExtremeXOS |
| Ubiquiti | UniFi switches, UniFi cloud gateways, UniFi access points, UISP routers | UniFi OS, UISP platform |
| Fortinet | FortiGate, FortiSwitch, FortiAP | FortiOS, FortiSwitchOS |
| Palo Alto Networks | PA-Series next-generation firewalls, Panorama-managed security environments | PAN-OS |
| Arista | Campus switches, data-center/cloud switches | EOS |
| Dell | PowerSwitch N-Series, S-Series, Z-Series | SmartFabric OS10, OS6, OS9 |
| RUCKUS / CommScope | ICX switches, RUCKUS APs, SmartZone / RUCKUS One-managed WLAN | ICX switch software, SmartZone, RUCKUS One |
| Nokia | 7XXX Family SR, XRS, IXR, SIR etc.  | SR OS, SR Linux |
| Ciena | 3900 family service-delivery / packet platforms | SAOS |
| Check Point | Quantum Security Gateways | Gaia |
| F5 | BIG-IP appliances, virtual editions, application delivery platforms | TMOS |
| A10 Networks | Thunder ADC, application delivery / security platforms | ACOS |
| SonicWall | TZ, NSa, NSsp firewall families | SonicOS |
| Versa Networks | Secure SD-WAN, branch/WAN edge, CSG appliances | VOS |
| Alcatel-Lucent Enterprise | OmniSwitch campus switches, OmniAccess wireless, OmniVista-managed environments | |
| H3C Technologies | S12500X-AF series Switches, S98XX, S68XX, S10500X | |


This pack is designed for inventory collection for Extended Network Devices using standard SNMP mibs.

  
### Feature Summary  
  
Following are the key features covered by Extended Network Device Discovery solution package:  
  
- Network device discovery using SNMP and SSH for a given list of seed devices. The device IPs can be provided as single IPs, command-separated, and/or ranges.
- Access verification checks for devices on a set schedule or on demand for selected devices.
- Run discovery on a set schedule for devices that have passed access verification checks or run discovery on demand for selected devices.
- Dashboards to see the statuses of access verification checks and discovery runs.
- Dashboards to visualize the inventory data collected for devices along with the drill downs to view assets and asset hierarchy.
- CDP/LLDP, OSPF, BGP, and ISIS topologies. 

NOTE: 
- KPI Workbench related functionality will be available upon activation on Network Performance Management pack. 
- Alerts and Events functionality will be available upon activation Fabrix AIOPs SNMP and Fabrix AIOPs syslogs packs.

### Pre-requisite Steps 
- Add arango template from the resources folder to path: `Main Menu -> Configuration -> RDA Administration -> Object store -> Upload`. Give Name as `rda_arango_templates`and Folder name as `arango_templates`<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Network%20Device%20Discovery/9.1.0/resources/arango_templates" target="_blank">Click here for Arango template</a><br>


### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 3   | Use `Configure and Manage` ->  `Network Credentials` to create credentials of type `snmp-cred`,`device-snmp-v1v2`,`device-snmp-v3`,`device-host-ssh`,`ssh-cred`,`network_device`  with the correct values.  |   
| 4    | Use `Configure and Manage` -> `Network Discovery Targets` to on board Network Devices. Use `Add Devices` or `Import Devices`. `Import Devices` needs a csv file. For Example:<br><table><tr><th>device_ip</th><th>discovery_scope</th><th>cdp</th><th>lldp</th><th>ospf</th><th>bgp</th><th>isis</th></tr><tr><td>10.95.158.10</td><td>yes</td><td>yes</td><td>no</td><td>no</td><td>yes</td><td>yes</td></tr></table><br>**Note:** Set cdp, lldp, ospf, bgp, or isis to 'yes' for devices for which the respective topology needs to be collected. **Note:** The discovery_scope field (Yes/No) controls which devices are included in the blueprint's automated scheduled discovery runs. Only devices with discovery_scope set to 'yes' will be automatically discovered according to the blueprint's schedule.| 
| 5    | Update `geo_location` dataset. Use `Configure and Manage`-->`Network Management`-->`Configure Artifacts`-->`Row Level Actions`-->`import` action. Upload the csv file. **Note:** `geo_location` dataset should have columns - device_hostname,latitude,longitude|  
| 6    | Under `Configure and Manage` ->  `Run Discovery`  -> `Run Access Verification` -> select the protocols ICMP , SSH as per requirement to perform the credential check for Network Devices. <br>The verification results can be seen in `Status` -> `Network Access Status` dashboard page. <br>**Note:** For scheduled pipeline , the option to control ICMP/SSH during access check is available in `Configure and Manage`-->`Network Management`-->`Configure Artifacts`-->`Row Level Actions`-->`Manage Data` --> `Row Level Actions` --> `Edit Row` --> `Save` --> `Commit Changes`.|  
| 7    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Discovery` option . Use `Status` -> `Network Discovery Status` to view the device discovery status. |  
| 8    | After the collection completes successfully, use the pages under `Inventory` to view the inventory details. |   
| 9    | Use `Topology` and `Asset Navigator` to view topology. |
   
