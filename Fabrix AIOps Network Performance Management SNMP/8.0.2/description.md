**Fabrix AIOps Network Performance Management SNMP Pack**

**Overview**

Fabrix AIOps Network Performance Management SNMP Pack collects SNMP Metrics and displays in the KPI Workbench.


### Feature Summary  
  
Following are the key features covered by Fabrix AIOps Network Performance Management SNMP Pack solution package:  
  
- Fabrix AIOps Network Performance Management SNMP Pack collects SNMP metrics
- SNMP metrics collection includes CPU,Memory,Interface,Environmental metrics
- Pack contains KPI Workbench dashboard to visualize the collected SNMP metrics data.
 


**Prerequisites**
To install Telegraf, please follow the steps outlined in the detailed installation guide.
Access it by clicking the link below:



<a href="https://bot-docs.cloudfabrix.io/beginners_guide/telegraf/?h=telegra" target="_blank">Click here for the detailed installation steps.</a>

Important Note:
For the installation process, please follow steps 1.1 and 1.2 from the guide


Below is the example to add agents(devices) in snmp_metrics.conf


agents = ["udp://10.95.158.1:161",
          "udp://10.95.158.9:161"]

          



### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    |  Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack.  |   
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|  
| 3    | use the pages  `Metrics Workbench` to view the Metrics details. |  

