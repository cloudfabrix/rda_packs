# Fabrix AIOPs SNMP

## Overview

Fabrix AIOPs SNMP Pack collects SNMP alerts.

### Feature Summary  
  
Following are the key features covered by Fabrix AIOPs SNMP solution package:  
  
- SNMP Event Visualization: Provides detailed visibility into SNMP Trap event data for enhanced monitoring and analysis.
- Fabrix AIOPs SNMP Pack Visualize the SNMP alerts


## Prerequisites


- install event_gatway on your environment:<a href="https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/#12-rda-event-gateway-installation" target="_blank">Click here for the Event Gateway installation steps.</a><br>Note:<br>-  Use latest image of Event Gateway <br>-  Install event_gatway with latest daily tags `rdaf event_gateway install --tag <tag>`<br>Endpoints Configuration<a href="https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/#124-endpoints-configuration" target="_blank">Click here for the Endpoints Configuration steps.</a><br>Note:Pstream,tenant details and kafka should be added as below example:<br>Single tenant:
  ```
  direct_to_stream: snmp_trap_event_stream
  attrs:
   projectId: 9896d3a1-92b1-11f0-ae9b-0242ac140006
   customerId: 882cf154ab42477fb5785040e8f42766"
   customerTag: customer1
   site_code: acme_site01
  kafka:
    - stream_name: snmp_trap_event_stream
      context: datanetwork
      retention.ms: "3600000"
    ```
  
     Multi Tenant:
    ```
  direct_to_stream: <customer_tag>_snmp_trap_event_stream
  attrs:
   projectId: 9896d3a1-92b1-11f0-ae9b-0242ac140006
   customerId: 882cf154ab42477fb5785040e8f42766"
   customerTag: customer1
   site_code: acme_site01
  kafka:
    - stream_name: <customer_tag>_snmp_trap_event_stream
      context: datanetwork
      retention.ms: "3600000"
  ```
- Ensure that the Network Device Discovery Pack is activated, network devices are successfully discovered by executing ondemand_discovery_main pipeline, and `cisco_device_chassis_dict` and `cisco_device_interface_data` datasets are created.<br>NOTE: The tenant mode must be the same for both the `Network Device Discovery` Pack and the `Fabrix AIOps SNMP` Pack. 
- Fabrix AIOps Fault Management Base pack should be Activated. Enable single or multi tenant in the `Fabrix AIOps Fault Management Base` pack to match the tenant mode configured in the `Fabrix AIOPs SNMP` pack.<br>
For example: if the `Fabrix AIOPs SNMP` pack is to be enabled for single tenant, the `Fabrix AIOps Fault Management Base` pack must  be enabled for single tenant.
### Quick Start Guide 
  
  
| Step | Description |  
|------|-------------| 
| 1    | Complete the above Prerequisites. |  
| 2    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |  
| 3    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 4    | Update `snmp_trap_alert_rules_dict` dataset. Use `Management`-->`SNMP Management`-->`Configure Artifacts`-->`Row Level Actions`-->`import` action. Upload the csv file |    
| 5    | Review the blueprint for the scheduled pipeline that raises alerts|
| 6    | SNMP Traps data is visualized under `Events` -> `SNMP Traps`. | 
| 7    | SNMP alerts and incidents are visualized under Alerts and Incidents page. |   