# Fabrix AIOPs SNMP

## Overview

Fabrix AIOPs SNMP Pack collects SNMP alerts.

### Feature Summary  
  
Following are the key features covered by Fabrix AIOPs SNMP solution package:  
  
- SNMP Event Visualization: Provides detailed visibility into SNMP Trap event data for enhanced monitoring and analysis.
- Fabrix AIOPs SNMP Pack Visualize the SNMP alerts


## Prerequisites
- Fabrix AIOps Fault Management Base pack should be Activated 
- Alert endpoints , mappings, Correlation and Supression policies configuration. <a href="https://bot-docs.cloudfabrix.io/installation_guides/oia_management" target="_blank">Click here for configuation guide.</a><br>Use SNMP mapping script . <a href="https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOPs%20snmp/8.0.3/resources" target="_blank">Click here for Snmp mapping script</a><br>NOTE: Refer<br>Alert Endpoints - 4.1.3 [ Note - The alert endpoint name should be `SNMP_Traps` ]<br>Alert Mappings - 4.1.6<br>Correlation Policies - 7.3.2<br>
- Add `snmp_trap_event_stream` pstream for single tenant and `<customer_tag>_snmp_trap_event_stream` for multi tenant.<br>1.vi default_values.json<br>```{
	"device_status": "UNMANAGED"
} ```<br>2.vi enrich.json<br>```{   
    "dict": "chassis_inventory",
    "dict_source": "dataset",
    "src_key_cols": "rda_gw_client_ip",
    "dict_key_cols": "device_ip",
    "enrich_cols": "device_status,device_hostname,device_hostname_short,device_vendor,device_fw_type,device_model,device_fw_version,parent_sn,device_serial_number",
    "replace_values": "yes",
    "dict_update_check_seconds": 60
} ```<br>3.Add pstream using below cmd<br> for single tenant:<br>```rdac pstream add --name snmp_trap_event_stream --default_values default_values.json --enrich enrich.json --retention_days 31 --index <tenant_id>-snmp_trap_event_stream_single ```<br>for multi tenant:<br>```rdac pstream add --name <customer_tag>_snmp_trap_event_stream --default_values default_values.json --enrich enrich.json --retention_days 31 --index <tenant_id>-snmp_trap_event_stream_<customer_tag> ```<br>NOTE: for multi tenant, dict name in enrich.json  should be `<customer_tag>_chassis_inventory`.

- install event_gatway on your environment:<a href="https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/#12-rda-event-gateway-installation" target="_blank">Click here for the Event Gateway installation steps.</a><br>Note:<br>-  Use latest image of Event Gateway <br>-  Install event_gatway with latest daily tags `rdaf event_gateway install --tag <tag>`<br>Endpoints Configuration<a href="https://bot-docs.cloudfabrix.io/installation_guides/rda_edge_services/#124-endpoints-configuration" target="_blank">Click here for the Endpoints Configuration steps.</a><br>Note:Pstream name should be given as:<br>- Single tenant - `direct_to_stream: snmp_trap_event_stream`<br>- Multi tenant - `direct_to_stream: customer1_snmp_trap_event_stream`



### Quick Start Guide 
  
  
| Step | Description |  
|------|-------------| 
| 1    | Complete the above Prerequisites. |  
| 2    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |  
| 3    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 4    |  Add `alert_endpoint_details` dataset.<br> Use `Main Menu --> Configuartion --> RDA Administraion --> Datasets --> Add Dataset`. csv file should have columns: alertEndpointName,customer_id,customer_tag,project_id,webhookURL.<br>For example:<br> ```SNMP_Traps,41bc5cf743844136b5651529eb255921,DemoCustomer-1,6f870d54-0cc8-11ef-88c3-0242ac120006,https://10.95.107.118:443/webhooks/hookid/c8e281ea-22c6-453f-abcf-6857c23b0df9```<br>NOTE: for Multi tenant the dataset name should be `<customer_tag>_alert_endpoint_details` <br>alertEndpointName should be `SNMP_Traps` for both single and multi tenant. |    
| 5    | Pipeline for raising SNMP alerts is scheduled.|
| 6    | After the completion of the pipeline , the SNMP alerts is visualized in Alerts dashboard. |   
   

