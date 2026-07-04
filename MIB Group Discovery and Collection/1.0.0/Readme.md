### Overview

This pack enables users to upload SNMP MIBs, identify which MIBs are supported by network devices, and define collection rules for gathering device data.

The **collector** bot from the **asset-discovery** extension is used to perform data collection.

---

### Feature Summary

The following are the key features of the **MIB Group Discovery and Collection** solution pack:

- Upload MIBs and extract collection groups  
- Identify which MIBs are supported by network devices  
- Define collection rules for network devices  
- Perform scheduled data collection or run discovery on demand for selected devices  
- Dashboards to monitor the status of collection runs  
- User-friendly dashboards for configuration and visibility  


---

### Quick Start Guide

| Step | Description |
|------|-------------|
| 1 | Activate the solution pack. |
| 2 | Use the `Launch Dashboard` menu option to navigate to the pack’s dashboard. |
| 3 | Go to `MIB Management` → `MIBs` and upload one or more MIB files or a zip file. |
| 4 | After successful upload, view collection group details under `MIB Management` → `Collection Groups`. |
| 5 | Navigate to `Configure and Manage` → `Collection Management` → `Network Credentials` and create credentials of type `snmp-cred`, `device-snmp-v1v2`, `device-snmp-v3`, `ssh-cred` with appropriate values. |
| 6 | Go to `Configure and Manage` → `Collection Management` → `Device Discovery Targets` to onboard network devices. Use `Add Device` to add individual devices or upload using a csv file with `device_ip,discovery_scope` columns. |
| 7 | Go to `Configure and Manage` → `Collection Management` → `Run Collection` and use  `Run Access Verification` to run the access verification on the target devices.|
| 8 |After access verification completes, go to `Configure and Manage` → `Collection Management` → `Discover MIBs for Devices` and perform MIBs discovery for the target devices using `Discover MIBs for Devices` option. Its important to complete step 7.  |
| 9 | After MIBs has been discovered, define collection rules for the devices using the `Create Collection Group Rules` menu of devices on `Configure and Manage` → `Collection Management` → `Discover MIBs for Devices` page. |
| 10| The collection group rules you created in step 9 are stored in the `mibs_discovery` file. You can view them under `Configure and Manage` → `Collection Management` → `Collection Group Rules`. |
| 11 | Use `Configure and Manage` → `Run Discovery` to schedule collections or run them on demand. Note: `mibs_collection` pipeline will not collect data if steps 8 and 9 are not completed.  | 
| 12| Monitor execution using the `Configure and Manage` → `Collection Status`. |
| 9 | After successful collection, the data can be viewed using `Collection Data`. |

