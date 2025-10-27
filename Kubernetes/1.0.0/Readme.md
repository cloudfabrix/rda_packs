This pack is designed for inventory collection for kubernetes and Linux using the following bots:  

### Kubernetes 
- **nodes**  
- **nodes-images**  
- **pods**  
- **pod-containers**  
- **deployment**  
- **deployment-containers**  
- **services**  
- **service-ports**
- **endpoints**
- **endpoint-addresses**

### Linux 
- **system-info**  
- **disks**  
- **disk-usage**  
- **network-config**
- **processes**  
- **netstat**  
- **services**  
- **software-packages**  


### Quick Start Guide  
   
| Step | Description |  
|------|-------------|  
| 1    | Activate the solution pack. After the Pack is in `ACTIVATED` status, use `Enable Single Tenant` menu option to enable the pack. |  
| 2    | Use `Launch Dashboard` menu option to navigate to the pack's dashboard. Note: For multinent tenant environment, the pack specific dashboards will be available in Customer Ops page.|     
| 3   | Use `Kubernetes Management` ->  `Kubernetes Credentials` to create credentials of type `kubernetes-inventory` and  `linux-inventory` with the correct values.  |   
| 4    | Use `Kubernetes Management` -> `Kubernetes Discovery Targets` to Add kubernetes master node IP using `Add K8s Master Node IP` and/or add Host IP using `Add Linux Host`|  
| 5    | Under `Kubernetes Management` ->  `Run Discovery`  use `Run Access Verification` option to perform the credential check for kubernetes master node IP and hosts. The verification results can be seen in `Kubernetes Status` -> `Access Verification Status` dashboard page. |  
| 6    | Use `Kubernetes Management` ->  `Run Discovery` to view and/or edit the schedule of the discovery or run the discovery on demand using `Run Kubernetes Inventory Collection` and/or `Run Server Inventory` option. |  
| 7    | After the discovery completes successfully, use the pages under `Kubernetes Inventory` to view the inventory details. | 
| 8    | Use `Kubernetes Management` ->  `Run Discovery` -> `Run Kubernetes Topology` to run topology. Use `Kubernetes Topology` dashboard page to view the topology.|   
   


