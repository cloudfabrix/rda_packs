**Fabrix AIOps Network Performance Management SNMP Pack**

**Overview**

Fabrix AIOps Network Performance Management SNMP Pack collects SNMP Metrics and displays in the KPI Workbench.


### Feature Summary  
  
Following are the key features covered by Fabrix AIOps Network Performance Management SNMP Pack solution package:  
  
- Fabrix AIOps Network Performance Management SNMP Pack collects SNMP metrics
- SNMP metrics collection includes CPU,Memory,Interface,Environmental metrics
- Pack contains Metrics Workbench and Metrics Navigator dashboards to visualize the collected SNMP metrics data.
- Threshold-based alert rules are preconfigured and enabled to automatically generate alerts when SNMP metrics exceed defined limits, facilitating real-time monitoring and incident response.
 


**Prerequisites**

- Install Event-Gateway. Use `rdaf event_gateway install --tag 8.1.1`.<br>
- Add the projectId in telegraf.conf in the path `/opt/rdaf/event_gateway/telegraf/config`<br>
Example:`projectId = "ab7085a8-6dda-11f0-b23b-0242ac150006"`
- Copy all Telegarf config files from the resources folder to path: `/opt/rdaf/event_gateway/telegraf/config/conf.d`<br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Network%20Performance%20Management%20SNMP/10.0.0/resources" target="_blank">Click here for Telegarf Config Files</a><br>
- Add agents in snmp_metrics_cisco.conf<br>
Example:
`agents = ["udp://10.95.158.1:161","udp://10.95.158.9:161"]`

- Add agents in ping_metrics.conf<br>
Example:
`urls = [ "10.95.140.24","10.95.140.20","10.95.140.21"]`


### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    |  Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |   
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|  
| 3    | use the pages  `Metrics Workbench` and `SNMP Metric Navigator` to view the Metrics details. |  
| 4    | Go to `Main Menu` -> `Configuration` -> `RDA Administration` -> `Alert Rules` -> `Alert Rules`.Click on `Edit Json` action and set threshold as per requirement in the alert rules and Alert rules are scheduled. |
| 5    | SNMP metrics alerts and incidents are visualized under Alerts and Incidents page. |


