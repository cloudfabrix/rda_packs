### Overview

This pack is designed to collect inventory for VeloCloud by calling the following APIs:
- **/monitoring/getEnterpriseEdgeLinkStatus**
- **/enterprise/getEnterpriseEdges**
- **/enterpriseProxy/getEnterpriseProxy**
- **/enterpriseProxy/getEnterpriseProxyGateways**
- **/gateway/getGatewayEdgeAssignments**

### Feature Summary

Key features of the Cisco VeloCloud solution package include:
- Access verification checks for APIs on a scheduled or on-demand basis
- VeloCloud Inventory Collection:
  - Run on a set schedule for APIs that have passed access verification
  - On-demand collection option available
- Comprehensive dashboards:
  - Access verification status checks
  - Collection status monitoring
  - Inventory data visualization
  - Topology representation


### Quick Start Guide

| Step | Description |
|------|-------------|
| 1 | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack. |
| 2 | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. **Note:** For multi-tenant environments, pack-specific dashboards will be available in the Customer Ops page. |
| 3 | Use `Configure and Manage` -> `VeloCloud Credentials` to create credentials of type `velocloud_orchestrator` with the correct values. |
| 4 | Upload a dataset with `vco_cred` and `enterprise_id` as column names:<br>- `vco_cred`: Rows for the defined credentials<br>- `enterprise_id`: Contains the enterprise ID for subsequent credentials |
| 5 | Use `Configure and Manage` -> `VeloCloud Discovery Targets` to onboard all specified VeloCloud credentials. |
| 6 | Under `Configure and Manage` -> `Run Discovery`, use `Run Access Verification` to perform credential checks for VeloCloud. View verification results in the `Access Verification Status` dashboard. |
| 7 | Use `Configure and Manage` -> `Run Discovery` to:<br>- View or edit discovery schedule<br>- Run VeloCloud Inventory Collection on demand |
| 8 | After successful collection, use pages under `VeloCloud Inventory` to view:<br>- Inventory data<br>- Topology information |
