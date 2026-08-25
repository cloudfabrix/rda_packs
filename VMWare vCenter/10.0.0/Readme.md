This pack is designed for inventory collection for vCenter using the following bots:

* **vcenter-summary**
* **vms**
* **hosts**
* **clusters**
* **datastores**
* **vswitches**
* **host-storage-adapters**
* **host-networks**

### Quick Start Guide
| Step | Description |
| ---- | ----------- |
| 1 | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack. |
| 2 | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multi-tenant environment, the pack specific dashboards will be available in Customer Ops page. |
| 3 | Use `vCenter Configuration And Status` -> `vCenter Credentials` to create credentials of type `vmware-vcenter-v2` with the correct values. |
| 4 | Use `vCenter Configuration And Status` -> `vCenter Discovery Targets` and click on `Sync Targets with Defined Credential Names` to on board all the credentials specified for vCenter. Note: Select a site in the Sites field. Ensure correct worker site is selected. |
| 5 | Under `vCenter Configuration And Status` -> `Run Discovery` use `Run Access Verification` option to perform the credential check for vCenter. Note: Select a site in the Sites field. Ensure correct worker site is selected for on-demand pipeline runs. The verification results can be seen in `vCenter Configuration And Status` -> `vCenter Credentials` -> `Access Verification Status` dashboard page.  |
| 6 | Use `vCenter Configuration And Status` -> `Run Discovery` to view and/or edit the schedule of the vCenter Inventory Collection pipeline or run the discovery on demand using `Run vCenter Inventory Collection` option. Note: Select a site in the Sites field. Ensure correct worker site is selected for on-demand pipeline runs. |
| 7 | Use `vCenter Configuration And Status` -> `Run Discovery` to view and/or edit the schedule of the vCenter Topology pipeline or run the discovery on demand using `Run vCenter Topology` option. Note: Select a site in the Sites field. Ensure correct worker site is selected for on-demand pipeline runs. Run the vCenter Topology pipeline only after the vCenter Inventory Collection pipeline has completed successfully. |
| 8 | After collections complete successfully, use the following dashboards to view the collected data: `vCenter Manager`, `Virtual Machines`, `ESXi Hosts`, `ESXi Datastores`, and `ESXi vSwitches`. For Discovery details refer to `Discovery Status` |