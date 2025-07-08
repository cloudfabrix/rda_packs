# Fabrix AIOPs syslogs

## Overview

Fabrix AIOPs syslogs Pack collects Syslog alerts.

### Feature Summary  
  
Following are the key features covered by Fabrix AIOPs syslogs solution package:  
  
- Syslog Event Visualization: Provides detailed visibility into Syslog event data for enhanced monitoring and analysis.
- Fabrix AIOPs syslogs Pack Visualize the syslogs alerts

## Prerequisites
- Ensure that the Network Device Discovery Pack is activated, network devices are successfully discovered, the network topology pipeline is executed, and `chassis_inventory` dataset is created.<br>NOTE: The tenant mode must be the same for both the `Network Device Discovery` Pack and the `Fabrix AIOps syslogs` Pack.
- Fabrix AIOps `Fabrix AIOps Fault Management Base` pack should be Activated. Enable single or multi tenant in the `Fabrix AIOps Fault Management Base` pack to match the tenant mode configured in the `Fabrix AIOPs syslogs` pack.<br>
For example: if the `Fabrix AIOPs syslogs` pack is to be enabled for single tenant, the `Fabrix AIOps Fault Management Base` pack must  be enabled for single tenant.



- install event_gatway on your environment. <a href="https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/#12-rda-event-gateway-installation" target="_blank">Click here for the Event Gateway installation steps.</a><br>Note:<br>-  Use latest image of Event Gateway <br>-  Install event_gatway with latest daily tags `rdaf event_gateway install --tag <tag>`<br>Endpoints Configuration <a href="https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/#124-endpoints-configuration" target="_blank">Click here for the Endpoints Configuration steps.</a><br>Note:Pstream name should be given as:<br>- Single tenant - `direct_to_stream: syslog_udp_event_stream`<br>- Multi tenant - `direct_to_stream: customer1_syslog_udp_event_stream`







### Quick Start Guide 
  
  
| Step | Description |  
|------|-------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 3    | Add `syslog_alert_rules_dict` and `syslog-severities` datasets. Use `Configure and Manage`-->`Syslog Management`-->`Configure Artifacts`-->`Row Level Actions`-->`import`action. Upload the csv file. |    
| 4    | Pipeline for raising syslog alerts is scheduled.|
| 5    | Syslog alerts and incidents are visualized under Alerts and Incidents page. |   
   

