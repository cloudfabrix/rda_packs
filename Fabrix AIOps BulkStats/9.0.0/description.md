This pack is designed to automate the systematic monitoring and analysis of asset-related metrics using the following bots:  
  
- **cfxml**
- **restclient**  


### Prerequisites
- All the below streams should be present with the corresponding fields:
- mobility_new_kpi_list - KPI_Name,schema
- mobility_device_mappings - device
- mobility_kpi_metrics_data - device, instance_key, schema and KPI columns

### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                                          |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                                      |
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant tenant environment, the pack specific dashboards will be available in Customer Ops page.                                              |
| 3    | Use `Configure and Manage` ->  `ML Credential` to view the credentials of type `cfxai_regression` and `restclient` with name `cfxml` and `restclient` which is added by default from the pack.                                       |   
| 4    | Use `Configure and Manage` ->  `Run Discovery`  ->  `BulkStats Metrics Correlation and Regression / Multi Tenant` Run the action pipelines in the same order one after another as shown in the blueprint                                 |  
| 5    | Once all the action pipelines are completed, check dashboard `Insights` and `Configuration`                                                                                                                                          |
| 6    | Use `Configuration` dashboard scroll down to `Metrics` tabular to `Select a metric` and set `Static Upper Threshold`, `Static Lowe Threshold` and Ignore/Select `Upper Anomalies Alerts`,  `Lower Anomalies Alerts` for a particular `Device IP` and manually run/let the `Scheduled` pipelines to run.                              |
| 7    | To enable live anomaly detection, once all action pipelines are completed, Go to `Services` pipeline and change the `Configure` instance from `0` to `1`                                                                             |
   
