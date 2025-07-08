**Fabrix AIOps Network Performance Management Telemetry Pack**

**Overview**

Fabrix AIOps Network Performance Management Telemetry Pack collects Telemetry Metrics and displays in the KPI Workbench.
Following devices are supported. If needed, additional ones needs to be added.  
  
- IOS-XR  
- N9k  
- TG 1100  

### Feature Summary  
  
Following are the key features covered by Fabrix AIOps Network Performance Management Telemetry Pack solution package:  
  
- Fabrix AIOps Network Performance Management Telemetry Pack collects Telemetry metrics
- Telemetry metrics collection includes CPU,Memory,Interface metrics
 


**Prerequisites**
- Install Telegraf, please follow the steps outlined in the detailed installation guide.<a href="https://bot-docs.cloudfabrix.io/beginners_guide/telegraf/?h=telegra" target="_blank">Click here for the detailed installation steps.</a><br>Important Note:<br>For the installation process, please follow steps 1.1 and 1.2 from the guide

- Telemetry configuration : <a href="https://bot-docs.cloudfabrix.io/installation_guides/nginx_lb_configuration_telemetrics/?h=telemetry#4-telemetry-re-configuration" target="_blank">Click here for Telemetry configuration guide.</a><br>After the configuration , In `/opt/rdaf-telegraf/config/conf.d/kafka-output.conf` , change the topic name to telemetry_metrics and restart the telegraf container.



## Pre-configuration Steps  
   
| Step | Description |  
|------|-------------|  
| 1    |  Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |   
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|  
| 3    | use the pages under  `Metrics Workbench` --> `Telemetry Workbench` to view the Telemetry Metrics. |  

