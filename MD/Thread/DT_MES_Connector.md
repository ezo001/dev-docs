---
sidebar_position: 2
title: DT MES Connector
---

<div class="doc-title-block">
<p class="doc-asset-name">Digital Thread Foundations</p>
<p class="doc-topic">MES Connector</p>
<p class="doc-type">INTEGRATION GUIDE</p>
</div>

<p class="doc-version">Release Version: 1.2</p>

##  \{#section .TOC-Heading\}


## Introduction

A digital thread refers to the continuous and consistent flow of information throughout the entire lifecycle of a product or system -- from design and development to operation and maintenance. It enables the integration of data from different stages and sources, allowing effective traceability, seamless collaboration, and efficient decision-making by unleashing the power of sleeping data. The digital thread is considered a key aspect of Industry 4.0 and the digital transformation of the manufacturing industry. It is the core of what we call the Enterprise Operating System (EOS). Digital Thread is a communication framework that helps integrate various enterprise systems involved in the engineering and manufacturing product life cycle.

The MES Connector is a set of Rest APIs, designed specifically to facilitate data retrieval from IX Digital Thread's MES database (IX MES DB). It has APIs that connect with stored procedures and Views for data and metadata retrieval.

### Purpose

This document describes the API and database details needed to integrate the IX Digital Thread Foundations MES Connector.

### Target Audience

Software architects, developers, and integrators with IT backgrounds.

### Prerequisites

-   MES Connector must be deployed on the target environment

-   Access to the ADO instance -- can be requested from the Technical Contacts.

### 

## Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [laura.mosconi@accenture.com](mailto:laura.mosconi@accenture.com)

-   [karthik.ramachandra@accenture.com](mailto:karthik.ramachandra@accenture.com)

-   [stefano.giacco@accenture.com](mailto:stefano.giacco@accenture.com)

### 

## Related Links

-   [IX Digital Thread - Connectors](https://industryxdevhub.accenture.com/assetdetails/97)

-   [GitHub -- Kafka Connector](https://github.com/castorm/kafka-connect-http)

### 

# Technology Stack

### Repository

-   Git branch name: dev

-   Git folder link: [ix-aveva-mes-api - Repos (azure.com)](https://dev.azure.com/IXDigitalThread/IXThreadComponents/_git/ix-thread-components?path=/connector/ix-aveva-mes-api)

### Tools

-   Springboot

-   Java

-   SQL Server

-   Azure APIM

-   Kubernetes

-   JWT

-   Postman

## 

# APIs

Since Kafka Connect is intended to be run as a service, it supports a set of REST APIs for managing connectors:

-   GET Product Data

-   GET Product Data with Common Format

-   GET Product Metadata

-   GET SendNotificationToEI

-   GET triggerStoredEquipment

### Preconditions

#### Authentication and Authorization

The MES Connector requires authorization using a Bearer Token (JWT) to secure access to its resources.

-   Users or applications authenticate and obtain a JWT token from the authentication server. Kindly send an email to Infra Team [IX_DT_DEVOPS_INFRA@accenture.com](mailto:IX_DT_DEVOPS_INFRA@accenture.com) to provide x-functions-key details to generate the JWT token.

-   The below curl is used to generate the JWT token.

> curl \--location \--request POST \'https://ix-dev-user-auth-ropc.azurewebsites.net/api/UserAuthRopc\' \\
>
> \--header \'Content-Type: application/json\' \\
>
> \--header \'x-functions-key: \\'

-   To access protected endpoints of the MES Connector, include the JWT token in the Authorization header of your HTTP requests.

-   Format the header as follows: Authorization :Bearer \

-   Replace \ with the actual JWT token obtained from the authentication server.

#### Subscription Key

-   When accessing APIs managed by API Management (APIM), it is mandatory to include the Ocp-Apim-Subscription-Key header in your HTTP requests.

-   To authenticate and authorize your requests, include the Ocp-Apim-Subscription-Key header in the HTTP request.

-   Format the header as follows:

> Ocp-Apim-Subscription-Key: \
>
> Contact the Infra team for the subscription key values.

### GET Product Data

This API fetches data from MES DB based on source parameters, used in ADF and Query engine APIs.


| PROTOCOL | HTTP |
| --- | --- |
| DEV ENDPOINT | [link](https://ix-dev-apimgmt.azure-api.net/avevames-api/mes/batteryData) |
| QA ENDPOINT |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Sample Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/MES%20Connector/GET_Product_Data_Sample_Request.txt) |
| Sample Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/MES%20Connector/GET_Product_Data_Sample_Response.txt) |


#### Input


| Parameter | Description |
| --- | --- |
| offset | Page number of the dataset to retrieve (greater than 0) |
| limits | Page size, maximum value is 500 (greater than 0) |
| modified_after | Sample date: 2023-01-01 15:45:03.012 |
| source | Data source name from the given list: - manufacturing_batch - production_schedule - production_performance - manufacturing_performance_metrics - manufacturing_scrap_wastage - production_downtime - production_shift - production_resource - resource - electronic_batch_record - Maintenance |



#### Result


| HTTP Code | Result Description |
| --- | --- |
| 201 | Service executed successfully |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 401 | HTTP 401 Unauthorized error An invalid or expired JWT token is provided to the MES Connector. |
| 401 | HTTP 401 Access Denied Error If the Ocp-Apim-Subscription-Key is omitted or incorrect, then APIM will respond with an Access denied error due to an invalid subscription key. Make sure to provide a valid key for an active subscription. |


### Get Product Data With Common Format

This API fetches battery data with a common response format, used in Purview.


| PROTOCOL | HTTP |
| --- | --- |
| DEV ENDPOINT |  |
| QA ENDPOINT | [link](https://ix-qa-apimgmt.azure-api.net/avevames-api/mes/) batteryDataV1 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Sample Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/MES%20Connector/GET_Product_Common_Format_Sample_Request.txt) |
| Sample Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/MES%20Connector/GET_Product_Common_Format_Sample_Response.txt) |


#### Input


| Parameter | Description |
| --- | --- |
| offset | Page number of the dataset to retrieve (greater than 0) |
| limits | Page size, maximum value is 500 (greater than 0) |
| modified_after | Sample date: 2023-01-01 15:45:03.012 |
| source | Data source name from the given list: - manufacturing_batch - production_schedule - production_performance - manufacturing_performance_metrics - manufacturing_scrap_wastage - production_downtime - production_shift - production_resource - resource - electronic_batch_record - Maintenance |



#### Result


| HTTP Code | Result Description |
| --- | --- |
| 201 | Service executed successfully |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 401 | HTTP 401 Unauthorized error An invalid or expired JWT token is provided to the MES Connector. |
| 401 | HTTP 401 Access Denied Error If the Ocp-Apim-Subscription-Key is omitted or incorrect, then APIM will respond with an Access denied error due to an invalid subscription key. Make sure to provide a valid key for an active subscription. |


### Get Product Metadata

This API fetches metadata for battery-related data attributes which are mapped to MES DB.


| PROTOCOL | HTTP |
| --- | --- |
| DEV ENDPOINT |  |
| QA ENDPOINT | [link](https://ix-qa-apimgmt.azure-api.net/avevames-api/mes/) batteryMetadata |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Sample Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/MES%20Connector/GET_Product_Metadata_Sample_Request.txt) |
| Sample Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/MES%20Connector/GET_Product_Metadata_Sample_Response.txt) |


#### Input


| Parameter | Description |
| --- | --- |
| offset | Page number of the dataset to retrieve (greater than 0) |
| limits | Page size, maximum value is 500 (greater than 0) |
| modified_after | Sample date: 2023-01-01 15:45:03.012 |
| source | Data source name from the given list: - manufacturing_batch - production_schedule - production_performance - manufacturing_performance_metrics - manufacturing_scrap_wastage - production_downtime - production_shift - production_resource - resource - electronic_batch_record - Maintenance |



#### Result


| HTTP Code | Result Description |
| --- | --- |
| 201 | Service executed successfully |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 401 | HTTP 401 Unauthorized error An invalid or expired JWT token is provided to the MES Connector. |
| 401 | HTTP 401 Access Denied Error If the Ocp-Apim-Subscription-Key is omitted or incorrect, then APIM will respond with an Access denied error due to an invalid subscription key. Make sure to provide a valid key for an active subscription. |


## Database Setup

The below tables from the MES DB are used in Battery data APIs.


| Table | Description |
| --- | --- |
| job_exec | Stores execution details of manufacturing jobs |
| job | Contains information about production jobs |
| item_prod | Records data related to produced items |
| item | Lists all items used in production |
| lot | Tracks batches of produced items |
| BOM_ver | Details versions of the bill of materials |
| wo | Manages work orders for production |
| shift | Defines production shifts and schedules |
| item_inv | Manages inventory details of items |
| util_history | Logs utility events, including downtimes |
| util_reas | Contains reasons for utility events |
| util_reas_grp | Groups utility reasons for better categorization |
| shift_history | Records historical shift data |
| user_name | Stores user identification and details |
| ent | Represents entities involved in manufacturing |
| job_event | Logs events related to jobs |
| item_cons | Details consumed items during production. |
| shift_sched | Manages shift scheduling information |


### Script Details

-   [View Creation](https://dev.azure.com/IXDigitalThread/IXThreadComponents/_git/ix-thread-components?path=/connector/ix-aveva-mes-api/db/sql/BatteryManagementScript.sql) defines multiple views that aggregate and summarize manufacturing and production data for efficient reporting and analysis.

-   [Procedure Creation](https://dev.azure.com/IXDigitalThread/IXThreadComponents/_git/ix-thread-components?path=/connector/ix-aveva-mes-api/db/sql/BatteryManagementScript.sql) defines two stored procedures for data retrieval:

    -   GetMesBatteryData: This procedure takes ViewName, ModifiedAfter, Offset, and Limit parameters and fetches data for the requested source.

    -   GetMesMetaData: This procedure takes the ViewName parameter and fetches metadata for the requested source.

-   [Sample Data Update](https://dev.azure.com/IXDigitalThread/IXThreadComponents/_git/ix-thread-components?path=/connector/ix-aveva-mes-api/db/sql/sample_data_update.sql) SQL script updates various tables within the MES database with sample data, specifically for testing and development of battery-related processes.
