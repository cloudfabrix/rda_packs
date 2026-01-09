This pack is designed for inventory collection for Cisco Crosswork using the following bots:  

- **devices**  
- **device-nodes**  
- **chassis-instances**  
- **physical-connectors**  
- **alarms**  
- **alarm-severity-config**  
- **network-nodes**  
- **network-link**  
- **l2-vpn-services**  
- **l2-vpn-service-underlay-transport**  
- **network-description**


### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                                          |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                                      |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant environment, the pack specific dashboards will be available in Customer Ops page.                                                     |    
| 3    | Use `CrossWork Configure and Manage` ->  `CrossWork Credential` to create credentials of type `cisco-crosswork`  with the correct values.                                                                                         |   
| 4    | Use `CrossWork Configure and Manage` -> `CrossWork Discovery Targets` and click on `Add IP Address` to manually add IP addresses for discovery. Select the credential name and set the discovery scope (yes/no) for each IP address.                                               |  
| 5    | Use `CrossWork Configure and Manage` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for CrossWork. The verification results can be seen in `Access Verification Status` of `CrossWork Asset Discovery Collection Status` dashboard page. |  
| 6    | Use `CrossWork Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run CrossWork Inventory Collection` option.                                         |  
| 7    | After the collection completes successfully, use the `CrossWork Inventory` dashboard to view the inventory details . |   