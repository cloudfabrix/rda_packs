This pack is designed for inventory collection and performance monitoring for vManage using the following API paths:

- **alarms**
- **alarms/count**
- **auditlog**
- **device**
- **device/bfd/sessions**
- **/device/bfd/synced/sessions**
- **device/control/connections**
- **device/hardwarehealth/summary**
- **device/interface**
- **device/omp/peers**
- **device/orchestrator/statistics**
- **device/reachable**
- **device/software**
- **device/system/statistics**
- **device/system/status**
- **device/tlocutil**
- **device/tlocutil/detail**
- **device/tunnel/statistics**
- **event**
- **network/connectionssummary**
- **network/status**
- **statistics/approute**
- **statistics/devicehealth/history**
- **statistics/devicehealth/overview/vbond**
- **statistics/devicehealth/overview/vedge**
- **statistics/devicehealth/overview/vmanage**
- **statistics/devicehealth/overview/vsmart**
- **statistics/dpi/aggregation**
- **statistics/interface**
- **statistics/qos**
- **statistics/sitehealth/common**
- **statistics/system**
- **statistics/system/aggregation**
- **system/device/controllers**
- **system/device/vedges**


### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                                          |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                                      |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant environment, the pack specific dashboards will be available in Customer Ops page.                                                     |    
| 3    | Use `Configure and Manage` ->  `vManage Credentials` to create credentials of type `cisco_vmanage`  with the correct values.                                                                                         |   
| 4    | Use `Configure and Manage` -> `vManage Discovery Targets` and click on `Sync Targets with Defined Credential Names` to on board all the credentials specified for vManage.                                               |  
| 5    | Under `Configure and Manage` -> `Run Discovery`, use `Run Access Verification` to perform credential checks for the selected vManage credentials.                                                                 |  
| 6    | View access verification results on the `Collection and Access Status` page under `Access Verification Status`.                                                                                                      |  
| 7    | Under `Configure and Manage` -> `Run Discovery`, select the Service Blueprint and use `Edit` to view or modify collection schedules.                                                                               |  
| 8    | To run collections on demand from `Configure and Manage` -> `Run Discovery`, use `Run Inventory`, `Run Performance`, `Run Alerts`, or `Run Advanced Visibility` for the selected vManage credentials.              |  
| 9    | Monitor pipeline job progress under `Configure and Manage` -> `Run Discovery` -> `All Jobs`. Collection run status is also available on `Collection and Access Status`.                                             |  
| 10   | After collections complete successfully, use the operational dashboards (`Network Overview`, `Device Inventory`, `Performance and SLA`, `Alerts and Events`, and `Topology`) to view collected data. |   
