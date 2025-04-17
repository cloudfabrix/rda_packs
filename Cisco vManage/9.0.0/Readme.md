### Overview  

Cisco vManage pack is designed for inventory collection for vManage using **query-api** bot. Following apis are being called by this pack:

- **system/device/controllers**
- **system/device/vedges**
- **device**
- **/device/bfd/synced/sessions**

### Feature Summary

Following are the key features covered by Cisco vManage solution package:

- Access verification checks for apis on a set scheduled or on demand.
- Run vManage Inventory Collection on a set schedule for apis that have passed access verification checks or run on demand.
- Dashboards to see the statuses of access verification and collection status checks.
- Dashboards to visualize the inventory data collected for apis along with the topology.

### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                              |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                          |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.                                     |     
| 3   | Use `Configure and Manage` ->  `vManage Credentials` to create credentials of type `cisco_vmanage`  with the correct values.                                                                                             |   
| 4    | Use `Configure and Manage` -> `vManage Discovery Targets` to on board all the credentials specified for vManage.                                                                                                         |  
| 5    | Under `Configure and Manage` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for vManage. The verification results can be seen in `Access Verification Status` dashboard page. |  
| 6    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run vManage Inventory Collection`.                                                |  
| 7    | After the collection completes successfully, use the pages under `vManage Inventory`to view the Inventory and Topology data.                                                                                             |