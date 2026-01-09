This pack is designed for inventory collection for Cisco using **Cisco Intersight APIs**. Following bots are being called by this pack:

- **ucs-server-summary**
- **ucs-server-cpu-inventory**
- **ucs-server-memory-inventory**
- **ucs-server-network-inventory**
- **ucs-server-storage-inventory**
- **ucs-server-hba-inventory**
- **ucs-fw-inventory**
- **ucs-fi-summary**
- **ucs-fi-eth-port-inventory**
- **ucs-hx-clusters**
- **ucs-hx-nodes**


### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 3   | Use `Intersight Management` ->  `Intersight Credentials` to create credentials of type `cisco-intersight`  with the correct values.  |   
| 4    | Use `Intersight Management` -> `Intersight Discovery Targets` and click on `Sync Targets with Defined Credential Names` to on board all the credentials specified for cisco-intersight. |  
| 5    | Under `Intersight Management` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for cisco-intersight. The verification results can be seen in `Access Verification Status` of `Intersight Status` dashboard page. |  
| 6    | Use `Intersight Management` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Intersight Inventory Collection` option. |  
| 7    | After the collection completes successfully, use the `Intersight Inventory` dashboard page to view the inventory details. |   