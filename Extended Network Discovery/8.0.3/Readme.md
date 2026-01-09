
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
- CDP/LLDP topology. 

NOTE: 
- KPI Workbench related functionality will be available upon activation on Network Performance Management pack. 
- Alerts and Events functionality will be available upon activation Fabrix AIOPs SNMP and Fabrix AIOPs syslogs packs.


### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 3   | Use `Configure and Manage` ->  `Network Credentials` to create credentials of type `snmp-cred`,`device-snmp-v1v2`,`device-snmp-v3`,`device-host-ssh`,`ssh-cred`  with the correct values.  |   
| 4    | Use `Configure and Manage` -> `Network Discovery Targets` to on board Network Devices. Use `Add Devices` or `Import Devices` by Uploading csv file with columns device_ip and discovery_scope. For Example: 10.95.158.10,yes. |  
| 5    | Under `Configure and Manage` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for Network Devices. The verification results can be seen in `Status` -> `Access Verification Status` dashboard page. |  
| 6    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Discovery` option . Use `Status` -> `Discovery Status` to view the device discovery status. |  
| 7    | After the collection completes successfully, use the pages under `Inventory` to view the inventory details. |   
| 8    | Use `Topology` and `Asset Navigator` to view topology. |
   
