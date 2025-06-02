This pack is designed for inventory collection for prime clients report using the following bots:  
  
- **get-report**  


### Feature Summary

Following are the key features covered by Prime Infrstructure package:

- All Pipelines are scheduled to run.
- Dashboards to see the statuses of collection status check for the bot.
- Dashboards show trends for client count, data usage, and throughput over time.
- Pipeline collects inventory, reachability, and other network reports from Prime.
- collects client data every hour. 


### Quick Start Guide  
   
| Step | Description                                                                                                                                                                          |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                      |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page. |     
| 3    | Use `Configure and Manage` ->  `Prime Credentials` to create credentials of type `cisco-prime` and `cfxaia` and with the correct values .                                            |   
| 4    | Use `Configure and Manage` -> `Prime Discovery Targets` to on board all the credentials specified for Prime.                                                                         |
| 5    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery                                                                                     |  
| 6    | After the collection completes successfully, use the pages under `Prime Inventory` to view the inventory details.                                                                    |   
   