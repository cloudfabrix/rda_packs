
### Overview  
  
Network Device Discovery solution package collects inventory data for network devices. Following network device vendors are supported out of the box. If needed, additional ones can be added.  
  
- Cisco  
- Juniper  
- Fortinet  


This pack is designed for inventory collection for Network Devices using **asset-discovery** extension. Following bots are being called by this pack:

- **collector**
- **get-collection-files**

  
### Feature Summary  
  
Following are the key features covered by Network Device Discovery solution package:  
  
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
| 4    | Use `Configure and Manage` -> `Network Discovery Targets` to on board Network Devices. Use `Add Devices` or `Import Devices`. `Import Devices` needs a csv file with columns device_ip, discovery_scope, cdp, lldp, ospf, bgp, isis. For Example: 10.95.158.10,yes,yes,no,no,yes,yes,no. **Note:** Set cdp, lldp, ospf, bgp, or isis to 'yes' for devices for which the respective topology needs to be collected. **Note:** The discovery_scope field (Yes/No) controls which devices are included in the blueprint's automated scheduled discovery runs. Only devices with discovery_scope set to 'yes' will be automatically discovered according to the blueprint's schedule.| 
| 5    | Update `geo_location` dataset. Use `Configure and Manage`-->`Network Management`-->`Configure Artifacts`-->`Row Level Actions`-->`import` action. Upload the csv file. **Note:** `geo_location` dataset should have columns - device_hostname,latitude,longitude|  
| 6    | Under `Configure and Manage` ->  `Run Discovery`  -> `Run Access Verification` -> select the protocols ICMP , SSH as per requirement to perform the credential check for Network Devices. <br>The verification results can be seen in `Status` -> `Network Access Status` dashboard page. <br>**Note:** For scheduled pipeline , the option to control ICMP/SSH during access check is available in `Configure and Manage`-->`Network Management`-->`Configure Artifacts`-->`Row Level Actions`-->`Manage Data` --> `Row Level Actions` --> `Edit Row` --> `Save` --> `Commit Changes`.|  
| 7    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Discovery` option . Use `Status` -> `Network Discovery Status` to view the device discovery status. |  
| 8    | After the collection completes successfully, use the pages under `Inventory` to view the inventory details. |   
| 9    | Use `Topology` and `Asset Navigator` to view topology. |
   
