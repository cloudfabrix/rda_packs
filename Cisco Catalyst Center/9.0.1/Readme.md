This pack is designed for inventory collection for Cisco Catalyst Center using the following bots:  

- **system-performance**  
- **wireless-profile**  
- **get-network-device**  
- **device-health**  
- **compliance**  
- **pnp-device**  
- **images**
- **dnac-info**
- **system-health**
- **system-perf-history**
- **compliance-detail**
- **nodes-config**
- **audit-logs**
- **health-analysis**
- **client-health**
- **device-interface**
- **list-report**
- **download-report**



### Feature Summary

Following are the key features covered by Catalyst Center solution package:

- All Pipelines are scheduled to run.
- Dashboards to see the statuses of collection status checks for each bots.
- Dashboards to visualize the inventory data collected by dnac bots.
- Pipeline collects inventory data , device health and  device compliance from the Catalyst center.
- collects client data once a day and their health 
- More information on wired and wireless connections are also displayed in Dashboards 
- Summary Dashboard gives the breif summary of full data for catalyst center   
- Also support DNA Center




   
### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                            |  
| 2    | Upload the dataset `device_family_alias` with value specified in csv file with columns `device_family_short` and `device_model_ext`                                                                              |
| 3    | Upload the dataset `dnac_building` with value specified in csv file with columns `building_input` , `building_rule` , `city` , `region` , `rto_priority` , `state` and `clli_code`                               |
| 4    | Upload the dataset `dnac_executive_device_list` with value specified in csv file with columns `CLLI` , `Street` , `floors`                                                                                       |
| 5    | Upload the dataset `dnac_host_info` with value specified in csv file with columns `dnac_category` ,  `dnac_cred` , `dnac_hostname` and `dnac_name`                                                                |
| 6    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant tenant environment, the pack specific dashboards will be available in Customer Ops page.    |     
| 7    | Use `Configure and Manage` ->  `DNAC Credentials` to create credentials of type `cisco-dnac` with the name DNAC_Alpharetta and other correct values and the `cfxaia` with the name cfxaia. |   
| 8    | Use `Configure and Manage` -> `DNAC Discovery Targets` to on board all the credentials specified for DNAC.                                                                                 |
| 9    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery.                                                                                          |  
| 10   | After the pipelines completes successfully, use the pages under `DNAC Inventory` to view the inventory details.                                                                            |   