This pack is designed to automate the systematic monitoring and analysis of asset-related metrics using the following bots:  
  
- **cfxml**
- **restclient**  


### Feature Summary
- ML Usecase Guide. <a href="https://bot-docs.cloudfabrix.io/installation_guides/ml_usecase_guide" target="_blank">Click here for Usecase guide.</a>
- Use Formatting template and Mapping Script. <a href="https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix AIOps Asset Correlation Regression/9.0.0/resources" target="_blank">Click here for Formatting Template and Mapping Script</a>


### Prerequisites
- Fabrix AIOps Fault Management Base pack should be Activated 
- Go to `Main Menu` -> `Configuration` -> `RDA Integrations` -> Add credentials of type `vrops`  with the correct values. 
- Go to `Main Menu` -> `Configuration` -> `RDA Administration` -> `Service Blueprints` Enable the blueprint `Metric Data Collection for IRM`. 
- Within the Blueprint `Metric Data Collection for IRM` -> Run `Actions` pipelines in order first with `metric_collection_rules` and `metric-list-dataset`.
- After the `metric-list-dataset` completes successfully, Run `Scheduled` pipeline `metric_data_collection` to populate `oia-metrics-data`.

#### Steps to create Webhook URL
- Go to `Main Menu` -> `Configuration` -> `RDA Integrations` -> check whether the credentials of type `vrops` is added.
- Go to `Main Menu` -> `Administration` -> `Organizations` -> add the organization with name and customer tag / if an organization is previously added click on `configure`.
- Within the Alerts `Alerts Endpoints` -> Add -> Give `Name` as `vrops` -> Select `Event Type` as `OIA Alert`, `Endpoint Type` as `Webhook HTTP Service` and add `Hostname or IP Address`,`Port` now `Save` and Enable.
- Within the Alerts `Alert Mappings` -> Add -> Select `Source Endpoint` as `vrops`, `Tagret Endpoint` as `OIA Alert` click on Next `Source Mapper` as `default.mapper-vrop-json` , `Source Pipeline` as `default.pipeline-default` click on Next add the `Mapping Script` click on next and finish.
- Within the Alerts `Alerts Endpoints` -> Click on more options menu -> `Webhook URL` and copy the URL and save it for Step 3.

### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                                                          |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                                                      |  
| 2    | Go to `Main Menu` -> `Administration` -> `Organizations` -> click on more options menu to one of the organizations to which the `Webhook URL` was configured -> `View JSON` and copy value of `customerTag , customerId , projectId` |
| 3    | Go to `RDA Administration` -> `Datasets` -> `customer_details` -> `Manage Data` -> `Add Row` and specify value to columns `customer_id,  customer_tag, project_id, webhook_url`                                                      |
| 4    | Go to `RDA Administration` -> `Formatting Template` to add template with name `raise_alerts_from_anomalies`.                                                                                                                         |
| 5    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant tenant environment, the pack specific dashboards will be available in Customer Ops page.                                              |
| 6    | Use `Configure and Manage` ->  `ML Credential` to view the credentials of type `cfxai_regression` and `restclient` with name `cfxml` and `restclient` which is added by default from the pack.                                       |   
| 7    | Use `Configure and Manage` ->  `Run Discovery`  ->  `Asset Metrics Correlation and Regression / Multi Tenant` Run the action pipelines in the same order one after another as shown in the blueprint                                 |  
| 8    | Once all the action pipelines are completed, check dashboard `Insights` and `Configuration`                                                                                                                                          |
| 9    | Use `configuration` dashboard scroll down to `Metric` tabular to `Select a metric` and set `Static Upper Threshold` for a particular `Device IP` and manually run/let the `Scheduled` pipelines to run.                              |
| 10   | To enable live anomaly detection, once all action pipelines are completed, Go to `Services` pipeline and change the `Configure` instance from `0` to `1`                                                                             |
   
