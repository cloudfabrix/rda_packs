This pack is designed to automate the systematic monitoring and analysis of asset-related metrics for regression using the following bots:  
 
- **cfxml**  


### Feature Summary
- ML Usecase Guide. <a href="https://bot-docs.cloudfabrix.io/installation_guides/ml_usecase_guide" target="_blank">Click here for Usecase guide.</a>


### Prerequisites
- Fabrix AIOps Fault Management Base pack should be Activated 
- Go to `Main Menu` -> `Configuration` -> `RDA Integrations` -> Add credentials of type `vrops`  with the correct values. 
- Go to `Main Menu` -> `Configuration` -> `RDA Administration` -> `Service Blueprints` Enable the blueprint `Metric Data Collection for IRM`. 
- Within the Blueprint `Metric Data Collection for IRM` -> Run `Actions` pipelines in order first with `metric_collection_rules` and `metric-list-dataset`.
- After the `metric-list-dataset` completes successfully, Run `Scheduled` pipeline `metric_data_collection` to populate `oia-metrics-data`.


### Quick Start Guide  
   
| Step | Description                                                                                                                                                                                      |  
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                                  |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant tenant environment, the pack specific dashboards will be available in Customer Ops page.          |     
| 3    | Need to have metrics data in a stream `oia-metrics-data`.                                                                                                                                        |
| 4    | Use `Configure and Manage` ->  `ML Credential` to view the credentials of type `cfxai_regression` with name `cfxml` which is added by default from the pack.                                     |   
| 5    | Use `Configure and Manage` ->  `Run Discovery`  ->  `ML Metrics Regression Single Tenant / Multi Tenant` Run the action pipelines in the same order one after another as shown in the blueprint. |  
| 6    | Within the Blueprint `ML Metrics Regression Single Tenant / Multi Tenant` Go to `Services` and change the `Configure` instance from `0` to `1`.                                                  |   
| 7    | After the regression completes successfully, use the pages under `Metrics ML Insights` to view the regression details.                                                                           |