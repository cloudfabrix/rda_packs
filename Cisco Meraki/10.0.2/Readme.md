Cisco Meraki pack is designed for inventory and metrics collection for Meraki using **Meraki-Networks** . Following bots are being called by this pack:

**Inventory Collection**
- **networks**
- **network-devices**
- **network-clients**

 **Metrics & Performance Data Collection**
- **clients**  
- **client-application-usage**  
- **client-bandwidth-usage-history**  
- **device-status**  
- **device-system-memory-usage**  
- **device-uplink-loss-latency**  
- **vpn-status**
- **client-count**  
- **ap-radio-status**  
- **appliance-uplink-usage-history**  
- **utilization**  
- **events**   

### Feature Summary

Following are the key features covered by Cisco Meraki solution package:
- Access verification checks for bots on a set scheduled or on demand.
- Run Meraki data Collection on a set schedule for bots that have passed access verification checks or run on demand.
- Dashboards to see the statuses of access verification and collection status checks.
- Dashboards to visualize the inventory data collected for bots along with the topology.

### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                             |  
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                         |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.                                    |     
| 3    | Use `Meraki Management` ->  `Meraki Credential` to create credentials of type `cisco-meraki`  with the correct values.                                                                                              |   
| 4    | Use `Meraki Management` -> `Meraki Discovery Targets` to on board all the credentials specified for Meraki.                                                                                                          |  
| 5    | Under `Meraki Management` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for Meraki. The verification results can be seen in `Meraki Status` -> `Access Verification Status` dashboard page. |  
| 6    | Use `Meraki Management` ->  `Run Discovery` to view and/or edit the schedule of the Meraki Inventory Collection pipeline or run the discovery on demand using `Run Meraki Inventory Collection` option.                                         |
| 7    | Use `Meraki Management` ->  `Run Discovery` to view and/or edit the schedule of the Meraki Metrics Collection pipeline or run the discovery on demand using `Run Meraki Metrics Collection` option.       |
| 7    | Use `Meraki Management` ->  `Run Discovery` to view and/or edit the schedule of the Meraki Topology pipeline or run the discovery on demand using `Run Meraki Topology Calculation` option.                                         |
| 8    | After the collection completes successfully, use the pages under `Meraki Device Inventory` to view the inventory and `Meraki Device Insights` for metrics collection details.                                                                                                      |   
| 9    | After the topology calculation completes successfully, use the pages under `Meraki Topology` to view the topology details.                                                                                              |   
   

