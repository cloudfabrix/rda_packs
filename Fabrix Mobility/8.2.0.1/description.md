##  Overview

This document describes the end-to-end setup and onboarding process for the **Fabrix Mobility Pack**, including deployment prerequisites, discovery configuration, and Bulkstats file ingestion.

---

##  Summary

The FabrixAI Mobility Pack is designed to ingest bulk statistics data from StarOS devices (ASR 5500) and provide comprehensive visibility into network performance and operational metrics.
The pack enables users to view, analyze, and monitor Key Performance Indicators (KPIs) derived from bulkstats data. It includes a set of predefined KPIs and also provides the flexibility for users to create and customize additional KPIs based on operational requirements. Users can further extend the solution by defining and adding new schemas.

In addition, the Mobility Pack supports StarOS device discovery and proactive alert generation based on configurable threshold conditions. Generated alerts are processed through the AIOps module, where they can be intelligently correlated to help identify patterns, reduce noise, and improve operational insights.

---

## Prerequisites

Required solution packs should be deployed in the following order:

1. **Fabrix Inventory Collection Base Pack**  
2. **Network Device Discovery**  
3. **Fabrix AIOps Fault Management Base**  
4. **Fabrix AIOps Syslogs**  
5. **Fabrix AIOps SNMP**  
6. **Fabrix Mobility Pack**


---

##  Quick Start Guide

| **Step** | **Section**                         | **Description**                        | **Navigation / Path** | **Actions** |
|----------|-------------------------------------|----------------------------------------|------------------------|-------------|
| **1**    | Configure Credentials               | Configure credentials for discovery    | `Home → EPC Mobility → Onboarding → Configure Discovery → Credentials` | Add required credentials |
| **2**    | Add Data Models                     | Add required data model files to MinIO | `<minio-alias-name>/<tenant-id>/declarative-dataset-definitions/` | Copy model ZIP to VM and extract files:<br><br>- `cdp_model.json`<br>- `interface_model.json`<br>- `network_assets_model.json`<br><br>Example Command:<br>`mc cp cdp_model.json <minio-alias-name>/<tenant-id>/declarative-dataset-definitions/` |
| **3**    | Add Devices                         | Onboard devices for discovery          | `Home → EPC Mobility → Onboarding → Configure → Discovery Targets` | Use **Add Devices** / **Import Devices** |
| **4**    | Run Discovery Pipelines             | Execute discovery workflows            | `Home → EPC Mobility → Onboarding → Configure → Run Discovery` | Run:<br>1. **Run Access Verification**<br>2. **Run Discovery** |
| **5**    | Verification                        | Validate discovered data               | `Home → EPC Mobility → Inventory → Network Devices` | Verify **network device inventory** |
| **6**    | Add Schema                          | Upload Bulkstats schema                | `Home → EPC Mobility → Onboarding → Schemas` | Click **Add Schema** and upload file |
| **7**    | Bulkstats Ingestion Process         | Configure file ingestion path          | `/opt/public/` | Configure devices to send Bulkstats files to **/opt/public/** where file_object service is deployed |

---