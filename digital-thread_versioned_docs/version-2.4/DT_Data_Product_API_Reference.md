---
sidebar_position: 2
title: DT Data Product API Reference
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Digital Thread Foundations</p>
<p class="doc-topic">Data Products</p>
<p class="doc-type">API REFERENCE</p>
</div>

<p class="doc-version">Release Version: 1.2</p>

<div class="metadata-for-agents" aria-hidden="true">
Metadata Table


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Digital Thread |
| **Domain / Area** | Engineering |
| **Owner (Team/Person)** | Karthik Ramachandra |
| **Reviewers** | Karthik Ramachandra |
| **Status** | Approved / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [link](https://dev.azure.com/IXAssets/IXAssetsProject/\_git/ixassets) |
| **Related Assets / Alternatives** | AOT / Engineering Orchestration / Engineering Agents |
</div>

## Introduction

Data products are data structures that would need to be created based on end-user reports and dashboard requirements. Types of data products may vary from simply one dataset from a single source system to a streamlined version of a huge dataset with only some attributes picked out of the \'n\' total present in it. It may also be a combination of attributes fetched from multiple source systems, viz., PLM, ERP, MES, etc.

Data products need to be created and refreshed with real-time data for the client to view a real-time dashboard of the same, and carry out their tracking, monitoring, analyzing, and similar other activities. The data products are to be exposed to the client application\'s UI via APIM URLs, and the attribute values need to be refreshed at an interval as stipulated by the client basis their need.

### Target Audience

This document is valuable to Client Delivery Teams planning to deliver Accenture IX Digital Thread.

### Purpose

This reference document includes information about paths, inputs, outputs, and error management for APIs related to Data Products. The document includes descriptions of APIs used for configuration as well as descriptions of APIs that provide middleware functionality.

### Prerequisites

An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64).

### Contacts

-   [karthik.ramachandra@accenture.com](mailto:karthik.ramachandra@accenture.com)

-   [l.bramhanapalli@accenture.com](mailto:l.bramhanapalli@accenture.com)

-   [d.choukse@accenture.com](mailto:d.choukse@accenture.com)

### Related Links

-   [IX Digital Thread Foundations Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=ix%20digital%20thread)

-   [REST API](https://restfulapi.net/)

## 

# Authentication and Authorization

API requires authorization using a Bearer Token (JWT) to secure access to its resources.

**Obtaining a Bearer Token (JWT)**

-   Users or applications authenticate and obtain a token from the Azure cloud.

-   Kindly send an email to BA [\ to provide B2B App access for Data Product API.

-   Use the below Curl and replace the client_secret with the actual value.

> curl \--location \--request GET \'https://ixthreaddev.b2clogin.com/ixthreaddev.onmicrosoft.com/B2C_1_IXDEV_ixthread_signin/oauth2/v2.0/token\' \\
>
> \--header \'Ocp-Apim-Subscription-Key: 0fc5e126b1384b9898ee186fe412d6a0\' \\
>
> \--header \'Cookie: x-ms-cpim-geo=NA\' \\
>
> \--form \'client_id=\"300ffe0a-18fa-44d3-adfc-4a672bb90084 \"\' \\
>
> \--form \'client_secret=\"\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \"\' \\
>
> \--form \'grant_type=\"client_credentials\"\' \\
>
> \--form \'scope=\"https://ixthreaddev.onmicrosoft.com/300ffe0a-18fa-44d3-adfc-4a672bb90084/.default\"\'

### Including the Bearer Token in API Requests

-   To access protected endpoints of the Data Product API, include the JWT token in the Authorization header of your HTTP requests.

-   Format the header as Bearer \.

-   Replace \ with the actual access_token obtained from the above curl command.

### Handling Authorization Errors

If an invalid or expired JWT token is provided, then the API will respond with an HTTP 401 Unauthorized error.

### Subscription key

When accessing APIs managed by API Management (APIM), it is mandatory to include the Ocp-Apim-Subscription-Key header in your HTTP requests.

**Including the Subscription Key in API Requests**

-   To authenticate and authorize your requests, include the Ocp-Apim-Subscription-Key header in the HTTP request.

-   Format the header as Ocp-Apim-Subscription-Key: \

**Error Handling**

If you omit or provide an incorrect Ocp-Apim-Subscription-Key then API will respond with an HTTP 401, Access Denied Error Access denied due to invalid subscription key. Make sure to provide a valid key for an active subscription.

## Data Product APIs

The method for all the Data Product APIs is GET. These APIs are described in detail in the subsequent sections.

### LIMS APIs

-   labtests

-   labsamples

-   labtestresults

-   labtestanalyses

### MES APIs

-   manufacturingBatch

-   productionSchedule

-   productionPerformance

-   manufacturingPerformanceMetrics

-   manufacturingScrap

-   productionDowntime

-   productionShift

-   productionResource

-   resource

-   electronicBatchRecord

-   maintenance

### Other APIs


| System | API |
| --- | --- |
| Siemens Simcenter | simulationData |
| BMS / Battery Data | fielddata |
| SCM Platform | logisticData |
| External Market Data | priceData |
| Compliance Management | regulatory Each of the APIs listed above is described on the pages that follow. |
### LIMS

#### Lab tests

This API is used to get Laboratory test-related data such as testID, test Name, testequipment, test Date, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [LINK](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/LIMS/DT_Data_Product_Lab_Test_Response.txt) |
##### Input Header


| Parameter | Description M/O MaxLength Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| Authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Request


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| limit | pagination. default max limit of record is100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| order_by | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. |
| 404 | Not Found Resource not found |
#### 

### Lab samples

This API is used to collect sample data for laboratory such as sampletype, samplequantity, samplelocation, samplingdate, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [LINK](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/LIMS/DT_Data_Product_Lab_Sample_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Request


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| limit | pagination. default max limit of record is100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| order_by | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description M/O Type |
| --- | --- |
| createdby | User that created the record M String |
| createdtimestamp | Time of creation M String |
| modifiedby | User that modified the record M String |
| modifiedtimestamp | Time of modification M String |
| lastQueryRun | Time the query was last run M String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Lab test results

The labtestresults API is used to get detailed outcomes from laboratory tests such as testId, resultid, resultvalue, sampleId, resultflag, analysistechnician, analysis date, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [[https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=lab_test_result]](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=lab_test_result) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/LIMS/DT_Data_Product_Lab_Test_Result_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Request


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| limit | pagination. default max limit of record is100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| order_by | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| createdby | User that created the record | M | String |
| createdtimestamp | Time of creation | M | String |
| modifiedby | User that modified the record | M | String |
| modifiedtimestamp | Time of modification | M | String |
| lastQueryRun | Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Lab test analyses

The labtestanalyses API is used for evaluation and interpretation of laboratory test results to ensure quality control and compliance such as analysisname, analysisparameters, cost, method, equipment, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [[https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=lab_test_analyses]](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=lab_test_analyses) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/LIMS/DT_Data_Product_Lab_Test_Analysis_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Request


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| limit | pagination. default max limit of record is100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| order_by | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
### 

## MES

#### Manufacturing Batch

The manufacturingBatch API is used to produce a unique identifier (Batch ID) to track and manage the production process, ensuring quality control, traceability, and compliance with manufacturing standards. The batch encompasses various attributes such as product type, production line, start and end dates, status, and estimated quantities.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?offset=1&amp;modified_after=2023-02-03) 15:45:03.000&amp;limit=10&amp;name=manufacturing_batch |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Manufacturing_Batch_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### Production Schedule

The productionSchedule API is used to plan timing and sequence of production activities in a manufacturing or production environment. It helps ensure that resources such as raw materials, labor, and equipment are used efficiently and that products are produced on time.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000&amp;name=production_schedule |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Production_Schedule_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Production Performance

The productionPerformance API is used to refer to effectiveness and efficiency of a production process. It measures how well the production system is meeting its goals and can encompass various metrics and factors, including volume, quantity, Cycle Time, Downtime, Cost, Efficiency, Yield.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=production_performance&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Production_Performance_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Manufacturing Performance Metrics

The manufacturingPerformanceMetrics API is used to evaluate the efficiency, effectiveness, and quality of manufacturing processes. These metrics help organizations assess how well their manufacturing operations are performing and identify areas for improvement. Common manufacturing performance metrics include type, name, and description.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=manufacturing_performance_metrics&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Manufacturing_Performance_Metrics_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Manufacturing Scrap Wastage

The manufacturingScrap API is used to refer to materials or products that are discarded or deemed unusable during the manufacturing process. Scrap can arise from various issues, such as defects, errors, or inefficiencies, and represents a loss in the production process.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=manufacturing_scrap_wastage&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Manufacturing_Scrap_Wastage.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Production Downtime

The productionDowntime API is used to refer to periods when manufacturing equipment or production lines are not operational, leading to a halt in production activities. Downtime can be caused by a variety of factors and can significantly impact manufacturing efficiency, productivity, and overall costs. Key aspects of production downtime include start time, end time, duration, and category.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=production_downtime&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Production_Downtime_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Production Shift

The productionShift API is used to refer to a scheduled period of work during which employees are assigned to operate or oversee the production process. It\'s a way to organize work hours and ensure continuous operations, especially in industries like manufacturing, healthcare, and IT.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=production_shift&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Production_Shift_Response.txt) |
##### Input Header

  -----------------------------------------------------------------------------------------------------------------------------------------
  --------------------------- ----------------------------------------------------- ----------- ---------------------------------- --------

  Parameter                   Description                                           M/O         Possible values                    Type

  Ocp-Apim-Subscription-Key   Value of the subscription key                         M-Private   2547a337c5c048afa719197ba4ac4ffe   String

  authorization               Value of the Access Token \[e.g. Bearer \\]   M-Public    \-                                 String

  BODY PARAM                                                                                                                       
  -----------------------------------------------------------------------------------------------------------------------------------------


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Production Resource

The production Resources API is used to refer to the various assets, tools, and materials required to carry out the production process effectively.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=production_resource&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Production_Resource_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Resource

The Resource API is used to refer to any asset, tool, or support used to achieve a specific goal or complete a task.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=resource&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Mes_Resource_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Electronic Batch Record

An Electronic Batch Record (EBR) API is used in manufacturing, particularly in industries. It provides a detailed, electronic account of the production process, including all steps, materials, equipment, and conditions involved in producing a batch of products.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=electronic_batch_record&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Electronic_Batch_Record.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
#### 

### Maintenance

The Maintenance API is used to refer to the actions taken to keep equipment, systems, or facilities in good working condition and to prevent or address issues that might affect their performance.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=mes_maintenance&amp;offset=1&amp;limit=10&amp;modified_after=2023-02-03) 15:45:03.000 |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/MES/DT_Data_Product_Mes_Maintenance_Response.txt) |
##### Input Header


| Parameter | Description M/O Possible values Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 2547a337c5c048afa719197ba4ac4ffe String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public String |
##### Input Body


| Parameter | Description M/O values Type |
| --- | --- |
| limit | Number of records per page M 10 Integer |
| offset | pagination M 1 Integer |
| modified_after | Date of aveva mes system M 2023-02-03 15:45:03.000 String \*M/O: Mandatory/Optional |
##### Output


| &gt; Parameter | &gt; Description | M/O | &gt; Type |
| --- | --- | --- | --- |
| &gt; createdby | &gt; User that created the record | M | String |
| &gt; createdtimestamp | &gt; Time of creation | M | String |
| &gt; modifiedby | &gt; User that modified the record | M | String |
| &gt; modifiedtimestamp | &gt; Time of modification | M | String |
| &gt; lastQueryRun | &gt; Time the query was last run | M | String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
### 

## Siemens Simcenter Battery Design Studio

#### Simulation Data

The simulationData API is used to get data from Siemens Simcenter Battery Design Studio system for Simulated properties like Cell Voltage, Capacity Fade, Thermal Behavior, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [[https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=simulation_data]](https://ix-dev-apimgmt.azure-api.net/data-product-api/product?name=simulation) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/DT_Data_Product_Simulation_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| limit | pagination. default max limit of record is 100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| orderBy | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description M/O Type |
| --- | --- |
| Simulated Cell Voltage | Predicted voltage profile of the battery during discharge/charge cycles under various conditions M String |
| Simulated Capacity Fade | Predicted loss of battery capacity over time or charge cycles M String |
| Simulated Thermal Behavior | Predicted temperature distribution within the battery during operation M String |
| Simulated Material Interactions | Predicted chemical and physical interactions between different materials within the battery M String |
| createdby | User that created the record M String |
| createdtimestamp | Time of creation M String |
| modifiedby | User that modified the record M String |
| modifiedtimestamp | Time of modification M String |
| lastQueryRun | Time the query was last run M String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
### 

## BMS / Battery Data

#### Field Data

The Field Data API is used to refer to information collected from real-world operations from Battery Management Systems (BMS) and battery data for properties such as Real-time Cell Voltage, Temperature, Current, State of Health (SOH), State of Charge (SOC), etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=field_data) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/DT_Data_Product_Field_Data_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| limit | pagination. default max limit of record is 100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| orderBy | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description M/O Type |
| --- | --- |
| Real-time Cell Voltage | Actual voltage of the battery during operation M String |
| Real-time Cell Temperature | Actual temperature of the battery during operation M String |
| Real-time Cell Current | Actual current flowing into or out of the battery M String |
| State of Health (SOH) | Battery\'s health compared to new, reflecting its capacity to store charge M String |
| State of Charge (SOC) | Remaining battery capacity as a percentage M String |
| createdby | User that created the record M String |
| createdtimestamp | Time of creation M String |
| modifiedby | User that modified the record M String |
| modifiedtimestamp | Time of modification M String |
| lastQueryRun | Time the query was last run M String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
### 

## SCM Platform

#### Logistic data

This API is used to refer to information related to the management and movement of goods and services of a Logistics vendor/partner with properties Vendor Name, route, mode, shipping time, shipping cost, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=logistic_data) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/DT_Data_Product_Logistic_Data_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| limit | pagination. default max limit of record is 100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| orderBy | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description M/O Type |
| --- | --- |
| Vendor Name | Logistics vendor/partner responsible for transportation M String |
| Route | Route of transportation M String |
| Mode | Mode of transportation M String |
| Shipping time | Schedules for shipping and delivery of raw materials M String |
| Shipping cost | Cost for shipping and delivery of raw materials M String |
| createdby | User that created the record M String |
| createdtimestamp | Time of creation M String |
| modifiedby | User that modified the record M String |
| modifiedtimestamp | Time of modification M String |
| lastQueryRun | Time the query was last run M String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
### 

## External Market Data

#### Price data

The priceData API is used to refer to information about the cost or price of goods, services, or financial assets in the market with properties such as Commodity Name, Current Price, Futures Price Data, Historical Price Data, etc.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=price_data) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/DT_Data_Product_Price_Data_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| limit | pagination. default max limit of record is 100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| orderBy | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description M/O Type |
| --- | --- |
| Commodity Name | Specific material used in battery production (e.g., Lithium, Cobalt, Nickel) M String |
| Current Price | Current market price for immediate delivery of the commodity M String |
| Futures Price Data | Predicted prices for the commodity at different future delivery dates (e.g., monthly, quarterly contracts) M String |
| Historical Price Data | Past price movements of the commodity over a chosen period M String |
| createdby | User that created the record M String |
| createdtimestamp | Time of creation M String |
| modifiedby | User that modified the record M String |
| modifiedtimestamp | Time of modification M String |
| lastQueryRun | Time the query was last run M String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |
### Compliance Management

#### Regulatory

The Regulatory API is used to refer to the rules, laws, and standards established by governmental or regulatory bodies that organizations must adhere to. These regulations are designed to ensure compliance with legal, safety, environmental, and industry-specific requirements.


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | [link](https://ix-dev-apimgmt.azure-api.net/dataproduct-api/product?name=regulatory_data) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [[LINK]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Data_Product/DT_Data_Product_Regulatory_Data_Response.txt) |
##### Input Header


| Parameter | Description M/O Max Length Type |
| --- | --- |
| Ocp-Apim-Subscription-Key | Value of the subscription key M-Private 255 String |
| authorization | Value of the Access Token \[e.g. Bearer \\] M-Public \- String |
##### Input Body


| Parameter | Description M/O Max Length Type |
| --- | --- |
| name | data product name M 255 String |
| filter | filtering condition for example \{name:\"seema\",id:100\} O 255 String |
| limit | pagination. default max limit of record is 100 O 2 Integer |
| offset | pagination. offset start at 1 O 2 Integer |
| orderBy | order by asc and desc order for example orderBy:\{natural\} O 255 String \*M/O: Mandatory/Optional |
##### Output


| Parameter | Description M/O Type |
| --- | --- |
| Environmental | Environmental regulations requirement M String |
| Safety | Safety standards requirement M String |
| Conflict Materials | Data on the presence and sourcing of conflict minerals such as cobalt, nickel, etc M String |
| createdby | User that created the record M String |
| createdtimestamp | Time of creation M String |
| modifiedby | User that modified the record M String |
| modifiedtimestamp | Time of modification M String |
| lastQueryRun | Time the query was last run M String |
##### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Service executed successfully |
##### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 400 | Bad Request no matching data products are available |
| 401 | Unauthorized Unauthorized. Invalid access token or claim |
| 401 | Access denied Access denied due to missing subscription key. Make sure to include subscription key when making requests to an API |
| 404 | Not Found Resource not found |