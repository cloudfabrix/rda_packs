### Overview  

VMware vROps pack is designed for metric collection for VMware vROps using the following bots:     

- **vm-summary**  
- **metric-list**  
- **metrics**

### Feature Summary

Following are the key features covered by VMware vROps solution package:
- Access verification checks for bots on a set scheduled or on demand.
- Run vROps Metric Collection on a set schedule for bots that have passed access verification checks or run on demand.
- Dashboards to see the statuses of access verification and collection status checks.
- Dashboards to visualize the metrics data collected for bots.

### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                                  |  
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                           |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.                                         |     
| 3   | Use `Configure and Manage` ->  `vROps Credentials` to create credentials of type `vROps`  with the correct values.                                                                                                                |   
| 4    | Use `Configure and Manage` -> `vROps Discovery Targets` to on board all the credentials specified for vROps.                                                                                                                 |  
| 5    | Under `Configure and Manage` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for vROps. The verification results can be seen in `Access Verification Status` dashboard page.       |  
| 6    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run vROps Metric Collection Rule` and after that run `Run vROps Metric Collection` option. |  
| 7    | After the collection completes successfully, use the pages under `vROps Metrics` to view the Metric data.                                                                                                                    |