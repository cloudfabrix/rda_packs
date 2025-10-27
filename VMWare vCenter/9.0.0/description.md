This pack is designed for inventory collection for vCenter using the following bots:  
  
- **vcenter-summary**  
- **vms**  
- **hosts**  
- **clusters**  
- **datastores**  
- **vswitches**  
- **host-storage-adapters**  
- **host-networks**


### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                              |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                          |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.                                     |     
| 3    | Use `Configure and Manage` ->  `vCenter Credentials` to create credentials of type `vmware-vcenter-v2`  with the correct values.                                                                                         |   
| 4    | Use `Configure and Manage` -> `vCenter Discovery Targets` to on board all the credentials specified for vCenter.                                                                                                         |  
| 5    | Under `Configure and Manage` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for vCenter. The verification results can be seen in `Access Verification Status` dashboard page. |  
| 6    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run vCenter Inventory Collection` option.                                         |  
| 7    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run vCenter Topology Calculation` option.                                         |  
| 8    | After the collection completes successfully, use the pages under `Inventory` to view the inventory details.                                                                                                              |   
| 9    | After the topology calculation completes successfully, use the pages under `Topology` to view the topology details.                                                                                                      |   