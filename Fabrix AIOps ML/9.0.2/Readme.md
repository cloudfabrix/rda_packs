This pack is designed for experimenting for Users:
 


### Quick Start Guide  
   
| Step | Description                                                                                                                                                                            |  
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1  | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.                                                          |  
| 2  | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant tenant environment, the pack specific dashboards will be available in Customer Ops page.  |
| 3  | Use `Credentials` ->  To add credentials used by experimental pipelines.                                                                                                                 |
| 4  | Use `Pipelines` -> To view published experimental pipelines.                                                                                                                             |
| 5  | Use `Experiments` ->  To create experiments for `Regression`, `Clustering` and `Classification`.                                                                                         |   

### ML DB Migration Guide

**Important:** Before upgrading the ml-config service, follow these steps to migrate data from MySQL to p-streams:

| Step | Description                                                                                                                                                                            |  
|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|  
| 1  | **Disable all schedules**: Disable all enabled schedules for all ML experiments (Clustering, Regression). This ensures no active jobs are running during migration.                   |  
| 2  | **Upgrade ml-config service**: Upgrade the ml-config service to the latest version that supports p-stream migration.                                                                  |  
| 3  | **Upload latest pack**: Upload the latest oia_ml_pack (version 9.0.0 or later) that includes the migration pipeline.                                                                 |  
| 4  | **Run migration pipeline**: Execute the migration pipeline (`ml-db-data-migration`) to migrate all data from MySQL database to p-streams. This will migrate experiments, jobs, clusters, model metadata, and versions data. Before executing the pipeline, verify and update the database name |   
