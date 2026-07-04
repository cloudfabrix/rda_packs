**Fabrix AIOps Network Performance Management SNMP Pack**

**Overview**

Fabrix AIOps Network Performance Management SNMP Pack collects SNMP Metrics and displays in the KPI Workbench.

**NOTE:** This pack is intended only for **SNMP plugin** based network performance metrics collection.

### Feature Summary  
  
Following are the key features covered by Fabrix AIOps Network Performance Management SNMP Pack solution package:  
  
- Fabrix AIOps Network Performance Management SNMP Pack collects SNMP metrics
- SNMP metrics collection includes CPU,Memory,Interface,Environmental metrics
- Pack contains Metrics Workbench and Metrics Navigator dashboards to visualize the collected SNMP metrics data.
- Threshold-based alert rules are preconfigured and enabled to automatically generate alerts when SNMP metrics exceed defined limits, facilitating real-time monitoring and incident response.
 


**Prerequisites**
- To collect SNMP metrics using the SNMP Plugin, devices must have the `snmp-cred` credential configured. If network discovery was previously performed using a different credential type, configure the `snmp-cred` credential and rerun Access Verification before deploying this pack.

- **Migration Note**
>
> If the devices are currently configured for metrics collection using a different plugin or collection method, remove or disable the existing metrics collection configuration before deploying the SNMP Pack. This prevents duplicate metric collection, redundant alert generation, and inaccurate KPI reporting.
>
> **Configuration files to delete:** from path `/opt/rdaf/event_gateway/telegraf/config/conf.d`
>
> * kafka_output.conf
> * ping_metrics.conf
> * snmp_metrics_cisco.conf
>
> **Alert rules to delete:** from UI `Main Menu-> Configuration->RDA Administration -> Alert Rules -> row level action -> delete`
>
> * memory_snmp_metric
> * cpu_snmp_metric
> * out_octets_snmp_metric
> * out_errors_snmp_metric
> * out_discards_snmp_metric
> * in_octets_snmp_metric
> * in_errors_snmp_metric
> * in_discards_snmp_metric
> * device_availability_snmp
> * oper_status_snmp

- Install Event-Gateway. Use `rdaf event_gateway install --tag 8.1.1`.<br>
- Add the following three fields in telegraf.conf in the path `/opt/rdaf/event_gateway/telegraf/config`<br>
  - In `[global_tags]`: `host_ip` and `projectid`<br>
  - In `[agent]`: `hostname`<br>
  Example: `host_ip = "10.95.109.130"`, `projectid = "a511a92b-1b74-11f1-97fc-0242ac120006"`, `hostname = "svc129.qa.engr.cloudfabrix.com"`
- Copy Telegarf config files from the resources folder  to path:<br> telegraf.conf - `/opt/rdaf/event_gateway/telegraf/config`<br>cisco_snmp_metrics.conf - `/opt/rdaf/event_gateway/telegraf/config/conf.d` <br><a href="https://github.com/cloudfabrix/rda_packs/tree/main/Fabrix%20AIOps%20Network%20Performance%20Management%20SNMP/10.0.2/resources" target="_blank">Click here for Telegarf Config Files</a><br>
 

### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    |  Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |   
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|  
| 3    | use the pages  `Metrics Workbench` and `SNMP Metric Navigator` to view the Metrics details. |  
| 4    | Go to `Main Menu` -> `Configuration` -> `RDA Administration` -> `Alert Rules` -> `Alert Rules`.Click on `Edit Json` action and set threshold as per requirement in the alert rules and Alert rules are scheduled. |
| 5    | SNMP metrics alerts and incidents are visualized under Alerts and Incidents page. |


