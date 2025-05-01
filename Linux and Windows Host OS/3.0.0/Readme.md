This pack s designed to do inventory collection for both Linux and Windows hosts using the following bots:  
  
- **System-info**  
- **Disks**  
- **Disk-usages**  
- **Processes**  
- **Netstat**  
- **Services**  
- **Software-packages**  
- **Network-config**  
- **Bios-details** (Windows)  

### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack. |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 3   | Use `Configure and Manage` ->  `Host Credentials` to create credentials of type `linux-inventory` and  `windows-inventory` with the correct values.  |   
| 4    | Use `Configure and Manage` -> `Host Discovery Targets` to either add host ips and credential names individually or upload them using CSV file. Note: You need to provide the `ip_address`, `type`, `port`, `credential`, and `discovery_scope` values in cvs file. For example: 10.97.200.201,linux,22,linux_credential_name,yes |  
| 5    | Under `Configure and Manage` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for hosts. The verification results can be seen in `Access Verification Status` dashboard page. |  
| 6    | Use `Configure and Manage` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Linux Discovery` and/or `Run Windows Discovery` option. |  
| 7    | After the discovery completes successfully, use the pages under `Host OS Inventory` to view the inventory details. |   
   

