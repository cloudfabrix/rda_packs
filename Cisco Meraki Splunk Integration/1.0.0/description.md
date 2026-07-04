### Overview  
Cisco Meraki Integration Pack is designed to ingest **event and metrics data** from Cisco Meraki into a **Splunk system** using the **splunkv2** – **add-to-index** and **add-to-index-metric** bot



### Feature Summary

Following are the key features covered by Cisco Meraki solution package:
- Automated Splunk index creation for ITSI and Meraki data  
- ITSI service and KPI setup for monitoring key metrics  
- Entity type management for structured ITSI modeling  
- Import job automation to ingest entities from saved searches  
- Correlation search creation to detect complex event patterns  
- Notable event aggregation policies to streamline ITSI alerts  
- Parameterized workflow execution with input validation and UI schemas
- Ingestion of events and metrics data into splunk 

### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                             |  
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                         |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.                                    |     
| 3    | Use `Meraki Integration Management` ->  `Meraki Integration Credentials` to create credentials of type `splunk_v2`  with the correct values. |   
| 5    | Use `Meraki Integration Management`-->`Configure Artifacts`-->`Row Level Actions`-->`Manage Data` --> `Row Level Actions` --> `Edit Row` --> `Save` --> `Commit Changes`. To view and edit datasets | 
| 6    | Use `Continuous Integration` to view the jobs scheduled for Meraki events and metrics data ingestion into Splunk.|
| 7    | Use `Meraki ITSI Workflow`-->`Workflows`-->`Row Level Actions`-->`Run` --> `Select credentials` --> `Click Run` To run the workflow.
| 8    | Use `Meraki ITSI Workflow`-->`Workflow Jobs`-->`View Details`-->`Logs` to trace the workflow execution. | 

