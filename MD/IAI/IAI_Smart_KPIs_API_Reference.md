---
sidebar_position: 2
title: IAI Smart KPIs API Reference
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">Smart KPIs</p>
<p class="doc-type">API REFERENCE</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

![](./media/IAI_Smart_KPIs_API_Reference/image1.png)

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value (Example)** |
| --- | --- |
| **Asset / Solution Name** | Smart KPIs API Reference |
| **Domain / Area** | Analytics / KPI Management |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Smart KPIs UI Guide, Smart KPIs Admin Guide |

</div>

## Introduction

Industrial AI Foundation (IAI) is a suite of software accelerators, including Smart KPIs, designed to deliver integrated client solutions. IAI streamlines the integration of products, processes, and real-time data from various IT and OT systems, providing a unified operational view for improved decision-making. Smart KPIs serve as the main dashboard within IAI, offering contextualized KPI insights for both management and operational teams. This application helps track performance issues and corrective actions, supported by dedicated backend microservices.

### Purpose

This reference document includes information about paths, inputs, outputs, and error management for APIs related to IAI Smart KPIs. The document includes descriptions of APIs used for configuration as well as descriptions of APIs that provide middleware functionality.

### Target Audience

Client Delivery Teams planning to deliver Industrial AI Foundation.

### Prerequisites

An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64).

### Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [thejash.s.suresh@accenture.com](mailto:thejash.s.suresh@accenture.com)

-   [nithya.arumugham@accenture.com](mailto:nithya.arumugham@accenture.com)

-   [hanuman.prasad.gali@accenture.com](mailto:hanuman.prasad.gali@accenture.com)

### Related Links


-   [IAI Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)[IAI General Architecture](https://industryxdevhub.accenture.com/assetdetails/53)

-   [IAI Smart KPIs Resources](https://industryxdevhub.accenture.com/assetdetails/42)

-   [IAI People Management Resources](https://industryxdevhub.accenture.com/assetdetails/64)

-   [Cognite API Docs](https://docs.cognite.com/api/v1/)



-   [API Management Documentation](https://docs.microsoft.com/en-us/azure/api-management/)

-   [REST API](https://restfulapi.net/) 

###  Glossary


| **Term / Acronym** | **Definition** |
| --- | --- |
| IAI (Industrial AI Foundation) | A suite of software accelerators and tools that integrate product, process, and live data from IT and OT systems to provide a contextualized view of operations for better decision-making and process optimization. |
| Smart KPIs | Micro Front-end applications within IAI that provide contextualized views of Key Performance Indicators (KPIs) for users, enabling performance tracking and improvement actions. |
| KPI (Key Performance Indicator) | Quantitative metric used to evaluate the success of an organization, employee, or process in meeting objectives for performance. |
| Microservice | A small, independent service that performs a specific function within a larger application architecture. In IAI, microservices provide middleware functionality and API endpoints. |
| Configuration Microservice | Flask-based microservice that manages KPI configuration, acting as middleware between the Smart KPI Config UI and Cognite CDF. |
| Cognite Data Fusion (CDF) | DataOps platform used for storing and processing operational data, including KPI templates and configuration files. |
| API (Application Programming Interface) | A set of protocols and tools for building and interacting with software applications. In IAI, APIs provide access to Smart KPIs functionalities and data. |
| Amazon API Gateway | AWS service that manages, secures, and publishes APIs to internal and external consumers. |
| Authorization Token | Security credential (usually from Azure AD) required to authenticate and authorize API requests. |
| Epoch Time UTC | Time representation as the number of seconds elapsed since January 1, 1970 (UTC). Used for timestamps in API requests and responses. |
| RAG Status (Red, Amber, Green) | Visual indicator of KPI performance, where Red = poor, Amber = warning, Green = good. |
| Asset Hierarchy Mapping | Structure that defines the relationship between assets (plant, unit, system, sub-system) and KPIs. |
| Config File | Excel template validated and uploaded to configure KPIs for a plant or asset. |
| UID (Unique Identifier) | Automatically generated unique ID for each KPI or configuration item. |
| KPI Hierarchy | Organizational structure of KPIs, showing relationships and dependencies among them. |
| Timeseries | Sequential data points collected over time, used for KPI calculations and analysis. |
| Drilldown | The process of exploring detailed data underlying a KPI, such as contributing or influencing KPIs. |
| Deviation API | API endpoint that calculates the deviation value for each KPI, used to sort and display KPIs by performance. |
| RAG API | API endpoint that returns the RAG status for assets based on KPI calculations. |
| Insight API | API endpoint that provides detailed calculations (actual, forecast, historical, target, RAG status) for a KPI. |
| Trendline API | API endpoint that returns trend charts for selected KPIs over a specified timeframe. |
| Responsible Role | The role assigned as the owner or manager of a KPI in the KPI hierarchy (e.g., Production Engineer, Maintenance Manager). |
| Department | Organizational unit to which a KPI is assigned based on its relevance. |
| Calculation Frequency | The interval at which a KPI is calculated (e.g., 5 min, 1 hour, daily). |
| UoM (Unit of Measurement) | The unit in which KPI values are expressed (e.g., kg, hours). |
| Error Management | Object in API responses that provides details about errors encountered during processing, including error codes and descriptions. |
| M/O (Mandatory/Optional) | M designates that a value is Mandatory, while O designates it as Optional. |
| UI | User interface |


## Smart KPIs APIs

The Python-based Smart KPIs microservices listed below are built and hosted in a cloud-agnostic Kubernetes environment that provides the APIs access to IAI functionalities and data through an API management service gateway---[AWS API Gateway REST API \| Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/apimanagement/). It authenticates and authorizes registered APIs. See the related links section for more information on APIs.

The microservices act as middleware and provide a unified interface between the various backends of IAI and the consumers of the data. For example, the middleware could be between the Cognite Data Fusion DataOps platform and IAI Applications, or between the IAI configuration backends and third-party data consumers.

###  Configuration Microservice KPIs

The Smart KPIs Configuration Microservice is a flask-based microservice that is positioned between IAI's Smart KPI Config UI and Cognite CDF. The request received from the processed configuration tool UI is processed and the output is stored in the CDF portal. The API for the microservice can be called using Postman or the Smart KPIs Config UI tool with the necessary inputs. It is a clean canvas that stitches together other modularized IAI components. User login/authentication is part of the component

-   POST- CREATE CONFIG FILE

-   POST- KPI CREATION

-   POST- EXCELDOWNLOAD API

-   GET- KPISPERPLANT API

###  Microservice APIs

The middleware microservice provides a unified interface between the different backends of IAI (Cognite Data Fusion DataOps platform) and the consumers of the data (IAI Applications). These services are accessed from the IAI application and are used in end-user visualization. Using Smart KPIs, users can have a contextualized view of operational performance through KPIs and can critically analyze business performance and drive decisions.

-   GET- KPI DASHBOARD

-   GET- KPI DRILLDOWN

-   POST- SMART-KPITILE

-   POST- TRENDLINE API

-   GET- LIST API

-   POST- DEVIATION API

-   POST- DRILLDOWN DEVIATION

-   POST-RAG API

-   POST-INSIGHT API

The APIs described in this document use an authentication token that can be retrieved either from the IAI UI or using a tool like Postman.

Requirements other than the authentication token, if any, are mentioned under the corresponding KPI. All the time zones are in [Epoch time UTC](https://www.epochconverter.com/) format.

## Smart KPIs Configuration Microservice APIs

### 

## POST- CREATE CONFIG FILE

The create config file CDF API is a part of the IAI-SmartKPI-Configuration Microservice that is invoked by the UI to be consumed by the UI. The create config file API is used to validate the KPI Template Excel file. Once all these validations are done and there is no error found, the user can access the KPI Hierarchy creation part.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"Bearer \{token\}\" \} M-Public \*\* String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| File path | \{\"Path\":\"\{smartkpibase\}/initialtemplate/\/\.xlsm\"\} M \*\* Multipart / Form-data |


#### Output Header


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. M-Public 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It is used to let the receiving entity know how much data to expect. O-Public 255 |
| date | Date of operation execution O-Public 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. O-Public 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. O-Public 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. O-Public 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. O-Public 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. O-Public 255 |


#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue. O Object |
| errorCode | This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors. M String |
| errorDescription | This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error. M String \*M/O: Mandatory/Optional |


#### API Precondition

To upload the KPI Template and to validate, the following entities must exist. For convenience, they are listed in the order of creation.

-   Azure blob File Path

-   Authorization token

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/configuration/file/assets/\](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/configuration/file/assets/%3cstring:plantExternalId%3e) |
| **PATH IAI (AWS) \** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/configuration/file/assets/\{assetid\}](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/configuration/file/assets/%7bassetid%7d) |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Response** | \{\"message\": \"Request accepted\"\} |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 202 | \{\"message\": \"Request accepted\"\} |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 401 | 401 | Unauthorized, 401 \"Bearer \{token\}\" could be missing, |


**Error message list which can be shown on the portal after validation**

\"Invalid: Duplicated row with same KPI name and same Asset Hierarchy Mapping is present.\"

\"Invalid or missing KPI Name value\"

\"Invalid or Asset Hierarchy Mapping value is same as that of Dependent Asset Hierarchy Level value\"

\"Invalid KPI Calculation Target value\"

\"Invalid or KPI Calculation Target has non-numeric value\"

\"Invalid UID or update flag or status or version\"

\"Invalid : Existing KPI should have UID and valid status\"

\"Invalid : Update Flag should not be any other than \'Add\', \'Update\', \'Archive\'\"

\"Invalid : New KPIs should have update flag value as \'Add\'\"

\"Invalid : sensitive field value should be either Yes or No\"

\"Invalid: UID should not be different for same KPI \"

\"Invalid: Archiving restricted. This KPI is a contributing kpi:\{kpis\[\'target_external_id\'\]\}.\"

\"Invalid: User should not update existing UID: error in \{Kpi_name\}\"

\"Invalid: Error occurred during File uploading to S3- \{exception_message\} \"

\"Invalid : Archiving restricted. This KPI \ is a contributing kpi for: \.\"

\"Invalid : Department - \ has not been created in the People Management tool.\
Please ensure that the departments added in the template are created in the People Management tool.\"\
\"invalid : Role - \ has not been created in the People Management tool.\
Please ensure that the roles added in the template are created in the People Management tool.\"\
\"invalid : \ - \ association does not match the role configuration in the People Management tool.\
Please ensure that the roles mapped to the departments in the template are as per the role configuration in the People Management tool."

##### 

## 

### POST- KPI CREATION

KPI creation is a POST call to the Smart KPI IAI server hosted at the back end. This API picks the Template uploaded by the user from Azure Blob Storage, processes the data, generates UID/Config_ID details, fetches JSON files uploaded in CDF, and creates the KPI hierarchy by adding assets, relationships, and metadata information.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| plantId | ExternalID of Uploading Plant M 255 String |
| templatePath | File path M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue. O Object |
| errorCode | This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors. M String |
| errorDescription | This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error. M String |
| services | This refers to the array or list of Service objects that have been created because of the operation. O List |
| Status | Displays the KPI creation status M String |
| ### | API Precondition To fetch the response from the KPI creation operation, the authorization token must exist. |


#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/kpi/creation](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/kpi/creation) |
| **PATH IAI (AWS) \** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Request Body** | \[ \{ \"plantId\": \"C-B1-G1-R1-F1\", \"templatePath\": \"\{smartkpibase\}/initialtemplate/C-B1-G1-R1-F1/Oil &amp; Gas Field 1.xlsm\" \} \] |
| **JSON Response** | message: \"Successfully Uploaded &amp; defined KPI\" |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Operation executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 400 Bad request |
| 401 | 401 Unauthorized (authorization token is missing or expired) |

### 

## POST- DOWNLOAD EXCEL 

The download excel-template API is a part of the IAI-SmartKPI- Configuration Microservice that is invoked by the UI and consumed by the UI.

The Download template API is a POST call to the Smart KPI IAI server hosted at the back end. It triggers the download functionality for the updated template that has been stored in an Azure blob storage with proper UUID, Status, and Version generated.

####  Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"Bearer \{token\}\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Asset-files | It contains Key and ExternalId parameters M \- List |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue. O Object |
| errorCode | This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors. M String |
| errorDescription | This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error. M String |
| services | This refers to the array or list of Service objects that have been created because of the operation. O List |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| Asset-files | external_id, key, path (path of this plant e.g., Multi-Plant.xlsm) M String |
| ### | API Precondition To fetch the response from the download template operation, the authorization token must exist. |


#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/kpi/downloadexcel](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/kpi/downloadexcel) |
| **PATH IAI (AWS) \** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_EXCELDOWNLOAD_JSON_Response.txt) |
| **JSON Request Body** | \{ \"asset-files\": \[ \{\"key\":\" plant1 \",\"external_id\":\" b037e3dd-02f4-4e19-9020-6ab0006e7ce9 \"\} \] \} |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Operation executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 401 | 401 | Unauthorized \{Header Token\} Access token is missing or invalid |
| 400 | 400 | Bad request **Example**: \"Invalid File or File name\" \"Unable to connect file storage\" |


### 

## 

### GET- KPISPERPLANT

The KPISPERPLANT API is a part of the IAI-SmartKPI-Configuration Microservice that is invoked by the UI and consumed by the UI. KPISPERPLANT is a GET call and it is used to fetch details of the selected plant from the dropdown menu in the SmartkpiConfig page.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"Bearer \{token\}\" \} M-Public \- String |


#### Input Path Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| plantExternalId | External id of the KPI the asset is linked to \[e.g., path value\\] M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | The numeric identifier of the error M String |
| errorDescription | Alphanumeric explanation of the error M String |
| Services | List of the created Service\ O List |
| Asset Hierarchy Mapping | Returns the Level (plant, unit, system, sub-system) of the timeseries of KPI and parameter M String |
| Calculation Frequency | Frequency of KPI calculation. Selected from dropdown list Ex:(5min,30min,1h,12h) M String |
| Config_Id | Unique ID of the external ID M String |
| KPI Calculation_Actual | The formula used to calculate the actual value of KPI where it depends on the configuration M String |
| KPI Name | Name of the KPI to be computed and displayed in UI. The KPI name should be unique and cannot have duplicates for a plant M String |
| KPI_TimeAggregation_Actual | The formula used to aggregate the actual values of KPI based on the time frame that has been selected by the user M String |
| Product Hierarchy Mapping | External id of the product M String |
| Responsible Role | The role which is responsible for the KPI M String |
| Status | The status of the KPI whether it is already published or ready to be published is generated by the system M String |
| ### | API Precondition To fetch the response from the smart-kpititle, the authorization token must exist. |


#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [link](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/) \{plantExternalId\}/kpisperplant |
| **PATH IAI (AWS) \** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/kpisperplant/\{plantExternalId\}](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/kpisperplant/%7bplantExternalId%7d) |
| **METHOD** | GET |
| **CONTENT TYPE** | application / json |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/GET_KPISPERPLANT_JSON_Response.txt) |
| **Request URL** | [link](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1/kpisperplant) |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Operation executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 401 | 401 Unauthorized / \{Header Token\} could be missing or expired |
| 400 | 400 Bad request |


## Smart KPIs Microservice APIs

### GET- KPI DASHBOARD

The KPI dashboard API, part of the IAI-SmartKPI-Middleware Microservice, is a GET request that retrieves parent KPI details for the signed-in user who is identified as an owner via the UsersToken API. Owners have read and write permissions for Asset Hierarchy and Timeseries. The API checks access to Timeseries, assets, roles sensitivity, and KPI sensitivity. Drilldown from the dashboard depends on asset access; if permitted, further drilldown is enabled. The API's disableFurtherDashboardDrilldown attribute controls whether the UI allows additional drilldown (true or false).

#### Input Header Parameters


| **Parameter** | **Description** **M/O\*** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g.- msal.accesstoken : \{token: \"\\" \} M-Public \- String |


#### Input Path Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| assetid | External id of the KPI the asset is linked to \[e.g., path value\\] M 255 String |
| kpiname | UID of the KPI \[e.g., path value\\] M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| **errorManagement** | The object identifying the error. Provided only if there is an error. | O | Object |
| errorManagement | This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue. | O | Object |
| errorCode | This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors. | M | String |
| errorDescription | This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error. | M | String |
| services | This refers to the array or list of Service objects that have been created because of the operation. | O | List |
| errorCode | The numeric identifier of the error | M | String |
| errorDescription | Alphanumeric explanation of the error. | M | String |
| services | List of the created Service\ | O | List |
| assetid | The external ID of the asset the KPI is linked to, | M | String |
| productid | The external ID of the product | M | String |
| uid | The uid of the KPI | M | String |
| kpiname | Name of the KPI configured in the KPI config template. Example: \[Thesis differentfreq, Thesis samefreq diffrole\]. Please note that the name of the KPI cannot be duplicated for parameters and the KPI name should match exactly with the timeseries name. | M | String |
| kpititle | Timeseries id or name of Timeseries Example: (C-B1-G1-R1-F1-P: Thesis differentfreq, C-B1-G1-R1-F1-P: Thesis differentfreq, C-B1-G1-R1-F1: OEE, C-B1-G1-R1-F1-P-PP-U1-EGCA: RunHours, C-B1-G1-R1-F1:OEE) | M | String |
| Department | Each KPI is assigned a department based on its relevancy to the department | M | String |
| ResponsibleRole | The responsible Role represents the owner role for the KPI in the KPI Hierarchy | M | String |
| CalculationLogic | Aggregationlogic with UoM represents the formula used to aggregate the KPIs at various levels of the asset hierarchy or aggregate based on the time frame that has been selected by the user. | M | String |
| details | Contains the config_id, name, parent_external_id, description, UoM, KPI_Name, source id, created_time, last_updated_time, root_id, ConfigurationUoM | M | List |
| assetName | Asset name from asset hierarchy |  |  |
| TimeseriesRole | Identify the timeseries access, being an \'owner\' implies that both read and write permissions are granted, whereas being a \'viewer\' means only read permission is provided |  |  |
| disableFurtherDashboardDrilldown | The disableFurtherDashboardDrilldown attribute returns a boolean value, either true or false, which dictates whether additional drilldown from the dashboard is permitted or not. | M | Boolean |


*\*M/O: Mandatory/Optional\
***API Preconditions**

-   To fetch the response from the download template operation, the authorization token must exist.

-   The necessary attributes and metadata are correctly mapped in the asset hierarchy. [See example](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/Attribute_Mapping_for_Dashboard_API.txt).

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **PATH \** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d) |
| **PATH \(AWS)** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d) |
| **METHOD** | GET |
| **CONTENT TYPE** | application / json |
| **Request URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/all/kpis/all](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/all/kpis/all) |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/GET_DASHBOARD_API_JSON_Response.txt) |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Operation executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 401 | 401 Unauthorized / \{Header Token\} could be missing or expired |
| 400 | 400 Bad request |


### POST - KPI DRILLDOWN

The KPI drilldown API is part of the IAI-SmartKPI-Middleware Microservice that is invoked and consumed by the UI. It is a POST call to the Smart KPI IAI server hosted at the backend to get the contributing and influencing KPI details (external IDs) which are displayed to the user on clicking on the KPI tile.

The drilldown details displayed to a user are based on the user's role authorizations, which the Drilldown API fetches from a People Management API. For more information on how this API communicates with the People Management component, refer to the [People Management Integration with Smart KPIs document](https://industryxdevhub.accenture.com/assetdetails/64).

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Path Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| assetid | The external ID of the KPI the asset is linked to \[e.g., path value\\] M 255 String |
| kpiname | UID of the KPI \[e.g., path value\\] M 255 String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| startdate | Start date to perform the calculation M 255 String |
| enddate | End date to perform the calculation M 255 String |
| calendarOption | Available calendar Options (noselection, hours, day, weeks, monthly, quarterly, half-yearly, yearly, custom) M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| Content-Type | Type of the content It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. M-Public 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It\'s used to let the receiving entity know how much data to expect. O-Public 255 |
| date | Date of operation execution O-Public 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. O-Public 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. O-Public 255 |
| ocp-apim-productid | Contains the product ID of the API it is tagged O-Public 255 |
| ocp-apim-subscriptionid | Contains the subscription ID of the API Gateway instance O-Public 255 |
| ocp-apim-trace-location | Contains the URL to trace the output O-Public 255 |


#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | Numeric identifier of the error. M String |
| errorDescription | Alphanumeric explanation of the error. M String |
| services | List of the created Service\ O List |
| Contributing | Contributing KPIs represent all the KPIs of a selected KPI which directly influence the value/ performance of the selected KPI. For example: for OEE at the plant level, the contributing KPIs can be availability, performance, and OEE at the system level among other KPIs. M String |
| Influencing | Influencing KPIs represent all the KPIs of a selected KPI that indirectly influence the value/ performance of the selected KPI. For example: for OEE at the plant level - the influencing KPIs can be no. of safety incidents among other KPIs. M String |


#### API Precondition

To fetch the KPI drilldown, the authorization token must exist.

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **PATH \** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/drilldown](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/drilldown) |
| **PATH IAI (AWS) \** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/drilldown](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/drilldown) |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **Request URL** |  |
| **JSON Request Body** | \{ \"startdate\":\"2023-12-01T09:00:39.308Z\", \"enddate\":\"2023-12-01T09:00:39.308Z\", \"calendarOption\":\"noselection\" \} |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_DRILLDOWN_API_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | operation executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 401 | 401 | Unauthorized \"Bearer \{token\}\" could be missing or expired |
| 400 | 400 | Bad request |


#### 

## 

### 

## POST- SMART KPI TILE

The smart kpitile API is a part of the IAI-SmartKPI-Middleware Microservice. It is invoked by the UI and consumed by the UI. This API is a POST call to the Smart KPI IAI DEV server is hosted at the backend to get the details of actual, forecast, historical, target, RAGStatus, and CompareActual calculations for KPI. In the case of a parameter, the details fetched are actual, forecast, and target calculations.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. Example: msal.accesstoken : \{ token: \"Bearer \{token\}\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** | **M/O** | **Max Length** | **Type** |
| --- | --- | --- | --- | --- |
| startdate | Start date to perform the calculation (ISO 8601 date format (i.e., YYYY-MM-DDTHH:mm:ss.sssZ)) | M | 255 | String |
| enddate | End date to perform the calculation (ISO 8601 date format (i.e., YYYY-MM-DDTHH:mm:ss.sssZ)) | M | 255 | String |
| calendarOption | This parameter specifies whether a specific calendar option has been selected for the data range. In this case, \"noselection\" indicates that no specific calendar option has been selected. | M | 255 | String |
| drilldowndetails | This is an object that contains details for the drilldown operation. | M | 255 | String |
| isSameCalcfreq | This is a Boolean parameter that signifies whether the calculation frequency of the parent KPI and the contributing or influencing KPI is the same. \'True\' means they have the same calculation frequency. \'False\' means they have different calculation frequencies. | M | 255 | String |
| kpiRelationship | This indicates the relationship of the KPI being drilled down. \"IAI_ContributingKPI\" means the KPI being considered is a contributing KPI. \"IAI_InfluencingKPI\" means the KPI being considered is an InfluencingKPI. | M | 255 | String |
| isdrilldown | This is a Boolean parameter that indicates if a detail call is for contributing or influencing KPI. | M | 255 | String |
| KPI_calculation_Actual | This parameter holds the calculation method for the KPI. Here, \"SK.average(\'Performance\')\" means the average of performance is calculated. | M | 255 | String |
| startdate_aggregate | This parameter represents the start date and time for the data range used for aggregation, given in the ISO 8601 format. | M | 255 | String |
| enddate_aggregate | This parameter represents the end date and time for the data range used for aggregation, given in the ISO 8601 format. | M | 255 | String |



#### Input Path Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| assetid | External id of the KPI the asset is linked to \[e.g., path value\\] M 255 String |
| kpiname | UID of the KPI \[e.g., path value\\] M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



####  Output Body Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. | O | Object |
| errorCode | The numeric identifier of the error | M | String |
| errorDescription | Alphanumeric explanation of the error | M | String |
| services | List of the created Service\ | O | List |
| Actual | The Actual calculation of the KPI depends on its configuration. For example: If a KPI is configured to be calculated at 12 AM every day, the actual value would depend on the past 24hrs data i.e., 12 AM the previous day to 12 AM the current day. ex:( C-B1-G1-R1-F1:OEE) | M | String |
| Forecast | Forecast refers to the average of the actual KPI values calculated over the past seven days. These calculated values are stored in its dedicated timeseries ID in CDF. ex:( C-B1-G1-R1-F1:OEE_Forecast) | M | String |
| Historical | Historical refers to the peak performance of a specific KPI recorded on any given day during the preceding 12 months. These calculated values are stored in its dedicated timeseries ID in CDF ex:( C-B1-G1-R1-F1-P-PP-U1:OEE_Historical) | M | String |
| RAGStatus | This visually represents the performance of the KPI. For example, if the actual value of the KPI is being compared with its target value, then it represents how the performance compares. | M | String |
| Target | Target represents the target value of the KPI. This can be a static value or can also be a dynamic target such that the target might be updated every shift or at a specific time interval. ex:(C-B1-G1-R1-F1-P-PP-U1:OEE_target)) | M | String |
| CompareActual | The percentage comparison calculates the relative change between the two most recent values of a KPI. The formula for this calculation is ((current value - previous value) / previous value) \* 100. If the result of the calculation is positive, indicating an increase in the KPI, an upward-pointing arrow should be displayed. Conversely, if the result is negative, signifying a decrease in the KPI, a downward-pointing arrow should be displayed. The color of the arrow is determined based on the settings specified in the KPI Config template or the KPI configuration tool. | M | String |
| assetid | Level in the asset hierarchy against which the KPI must be computed. | M | String |
| iskpi | Returns a Boolean response (**True** or **False**) and checks whether the response is for KPI or Parameter. | M | String |
| uid | UID is the Unique ID that automatically generates a unique identity for each KPI created by the user. | M | String |
| kpiDirection | Returns response(Up or Down) arrow and checks whether it's best performing or worst performing. | M | String |
| UoM | Returns the response of the respective unit of measurement (e.g., kg). It retrieves the value from the CDF KPI hierarchy in timeseries metadata. | M | String |
| CalculationFrequency | Frequency (5nin,1Hr,1day, etc.) for the calculation of KPI | M | String |
| ConfiguredUoM | Configured "Unit of Measurement" on the KPI configuration template updated by the end-user | M | String |
| StandardUoM | The standard unit of measurement as per asset system id. It retrieves the value from the Timeseries metadata | M | String |
| UoM_SystemID | Returns the response of the respective unit of measurement system ID (e.g., kg). It retrieves the value Asset metadata | M | String |



#### API Precondition

To fetch the response from the smart-kpitile, the authorization token must exist.

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **PATH \** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/detail](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/detail) |
| **PATH IAI (AWS) \** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/detail](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/detail) |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **REQUEST URL** | [link](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U3-SWLPC/kpis/d6b9f38e-28db-4eb7-806e-da9969e39ffb/detail) |
| **REQUEST URL(PARAMETER)** |  |
| **JSON Request Body** | \{ \"startdate\":\"2023-11-29T15:47:39.061Z\", \"enddate\":\"2023-11-29T15:47:39.061Z\", \"calendarOption\":\"noselection\" \} |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management

+:-------------:+:--------------:+:-------------------------------------------------:+
| **HTTP Code** | **Error Code** | **Error Description** |

| 500 | 500 | Internal server error |
| --- | --- | --- |
| 401 | 401 | Unauthorized \{HeaderToken\} Access token is missing or invalid |
| 400 | 400 | Bad request |



#### Requests and Response

##### 

#### Selection Options

-   No Calendar Selection for KPIs\*

-   No Calendar Selection for Parameter

-   Hours Selection for KPI

-   Hours Selection for Parameter

-   Days Selection for KPI

-   Days Selection for Parameter

-   Weeks Selection for KPI

-   Weeks Selection for Parameter

-   Monthly Selection for KPI

-   Monthly Selection for Parameter

-   Quarterly Selection for KPI

-   Quarterly Selection for Parameter

-   Half-yearly Selection for KPI

-   Half-yearly Selection for Parameter

-   Yearly Selection for KPI

-   Yearly Selection for Parameter

-   Custom Selection for KPI

-   Custom Selection for Parameter

#####  Request URLs

-   No Calendar: 

-   Hours Selections: 

-   Days Selections: 

-   Week, Monthly, Quarterly, Half-yearly, Yearly, and Custom Selections: 

##### JSON Request and Responses

Refer to [POST_smart_kpitile.zip](https://ts.accenture.com/:u:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.1/POST_smart_kpitile.zip?csf=1&amp;web=1&amp;e=yZ1q9o) for the JSON Requests and Responses.

\* The No Calendar Selection for KPI selection also performs the aggregation of all data points into one data point. This means that the data retrieved based on the user\'s specified start and end times is consolidated into a singular data point, presenting a unified view of the data over the selected time.

### 

## Detail API Backend Aggregation Logic 

#### Actual 

The backend applies KPI calculation frequency as the granularity within the Detail API. For frequencies equal to or greater than one hour, a \'60min\' granularity is implemented. Aggregate calculations exclude data at the start timestamp and include data at the end timestamp.

Data points are retrieved according to the selected KPI calculation frequency and calendar option (e.g., No Calendar, Hour, Day, Week, Month, Quarter, Half-Yearly, Yearly). Aggregations---including Average, Maximum, Minimum, or Sum---are computed and the actual value response is delivered to the front end.

#### Historical Benchmark 

Similarly, KPI calculation frequency serves as the granularity in the Detail API. When the frequency meets or exceeds one hour, a \'60min\' granularity is applied. The aggregation process omits data at the starting timestamp and includes data at the ending timestamp.

Based on the selected calendar and frequency, relevant data points are gathered for aggregations (Average, Maximum, Minimum, Sum), followed by historical benchmark computations (Maximum, Minimum). The resulting historical value response is then transmitted to the front end

### POST- TRENDLINE

The Trendline API is part of the IAI-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. A Trendline API is a POST call to the Smart KPI IAI DEV server hosted to execute Multiple APIs concurrently and return the consolidated result of all four APIs in JSON format. Trendline displays the trend charts for the selected KPIs for the selected timeframe in the calendar. Viewing Insights and Actions are still applicable in the KPI comparison scenario.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| startdate | Start date to perform the calculation(Unix Timestamp) [Timestamp Converter (timestamp-converter.com)](http://www.timestamp-converter.com/) M 255 String |
| enddate | End date to perform the calculation(Unix Timestamp) [Timestamp Converter (timestamp-converter.com)](http://www.timestamp-converter.com/) M 255 String |
| kpilist | ExternalId of the KPI (e.g., C-B1-G1-R1-F1-P-PP-U1-EGCA:d6b9f38e-28db-4eb7-806e-da9969e39ffb) M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | The numeric identifier of the error M String |
| errorDescription | Alphanumeric explanation of the error M String |
| Services | List of the created Service\ O List |
| Actual | The Actual calculation of the KPI depends on its configuration. For example: If a KPI is configured to be calculated at 12 AM every day, the actual value would depend on the past 24hrs data i.e., 12 AM the previous day to 12 AM the current day. ex:( C-B1-G1-R1-F1:OEE) M String |
| Forecast | Forecast refers to the average of the actual KPI values calculated over the past seven days. These calculated values are stored in its dedicated timeseries ID in CDF. ex:( C-B1-G1-R1-F1:OEE_Forecast) M String |
| Historical | Historical refers to the peak performance of a specific KPI recorded on any given day during the preceding 12 months. These calculated values are stored in its dedicated timeseries ID in CDF ex:( C-B1-G1-R1-F1-P-PP-U1:OEE_Historical) M String |
| Target | Target represents the target value of the KPI. This can be a static value or can also be a dynamic target such that the target might be updated every shift or at a specific time interval. ex:(C-B1-G1-R1-F1-P-PP-U1:OEE_target)) M String |
| kpititle | Timeseries external_id M String |
| kpiname | Name of that KPI M String |
| uid | UID is the Unique ID that automatically generates a unique identity for each KPI created by the user. M String |
| assetid | Level in the asset hierarchy against which the KPI must be computed. M String |
| UoM | Returns the response of the respective unit of measurement (e.g.: "kg"). It retrieves the value from the CDF KPI hierarchy in timeseries metadata. M String |


#### API Precondition

To fetch the response from the smart-kpitile, the authorization token must exist.

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **PATH \** | [link](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/trendline) |
| **PATH IAI (AWS) \** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **REQUEST URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/trendline](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/trendline) |
| **JSON Request** | \{ \"startedate\":1700764200000, \"enddate\":1701368999000, \"kpilist\":\"C-B1-G1-R1-F1-P-PP-U1-EGCA:d6b9f38e-28db-4eb7-806e-da9969e39ffb\" \} |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_TRENDLINE_API_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 401 Unauthorized / \{HeaderToken\} could be missing or expired |
| 400 | 400 Bad request |


### GET- LIST

The List API, part of the IAI-SmartKPI-Middleware Microservice, is a GET endpoint used by the UI to retrieve all available timeseries from the Smart KPI IAI DEV server in JSON format. It integrates with the People Management and GET Roles APIs, and requires a path parameter specifying a plant\'s external ID. For multi-plant queries, the external ID should be formatted as "Multi-Plant."

#### Input Header Parameters


| **Parameter** | **Description** | **M/O** | **Max Length** | **Type** |
| --- | --- | --- | --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M-Public | \- | String |



#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | The numeric identifier of the error M String |
| errorDescription | Alphanumeric explanation of the error M String |
| Services | List of the created Service\ O List |
| assetHierarchyLevel | Returns the Level (plant, unit, system, sub-system) of the timeseries of KPI and parameter M String |
| computationtrigger | Returns whenever any computation is getting triggered. For example, Time-based. M String |
| department | Contains "departmentId" and "departmentName". Each KPI is assigned a department based on its relevancy to the department M String |
| frequency | Frequency of KPI calculation e.g., 5min,10min,15min,30min M String |
| name | Contains Assetname and KPI name (e.g. Field 2_MOL P-0191:OEE) M String |
| plantname | Name of the parent plantname (e.g., Oil &amp; Gas Field 2) M String |
| role | Contains "roleId" and "roleName". Represent the Owner role assigned to the KPI in the KPI hierarchy M String |
| type | Displays the type whether it is of type KPI or parameter M String |
| uid | unique identity only for KPI that is created by the user M String |


#### API Precondition

To fetch the response from the smart-kpitile, the authorization token must exist.

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [link](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/listkpi?asset=C-B1-G2-R1-F1) [link](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/listkpi?asset=Multi-Plant) |
| **PATH IAI (AWS) \** |  |
| **METHOD** | GET |
| **CONTENT TYPE** | application / json |
| **JSON Response** | Plant- [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.1/GET_List_Plant_JSON_Response.txt)\ Multi-plant - [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.1/GET_List_Multiplant_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | Unauthorized \{HeaderToken\} could be missing or expired |
| 400 | 400 | Bad request |


### 

## POST- DEVIATION

The Deviation API is part of the IAI-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. This API is a POST call that is used to calculate the deviated value for each KPI and to send the consolidated output (all KPI deviation values) according to which KPIs are sorted by performance and displayed on the UI.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| authorization | Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| startdate | Start date to perform the calculation M 255 String |
| enddate | End date to perform the calculation M 255 String |
| calendarOption | Available calendar Options (noselection, hours, day, weeks, monthly, quarterly, half-yearly, yearly, custom) M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | The numeric identifier of the error M String |
| errorDescription | Alphanumeric explanation of the error M String |
| Services | List of the created Service\ O List |
| kpitile | Timeseries id M String |
| id | Timeseries External Id M String |
| deviation | Deviation value M String |
| error | Error object if any M String |
| ### | API Precondition To fetch the response from the Deviation API the authorization token must exist. |


#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **PATH \** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/deviation](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/deviation) |
| **PATH IAI (AWS) \** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/\{assetid\}/kpis/all/deviation](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/%7bassetid%7d/kpis/all/deviation) |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **REQUEST URL** |  |
| **JSON Request** | \{ \"startdate\":\"2023-11-29T16:09:05.594Z\", \"enddate\":\"2023-11-29T16:09:05.594Z\", \"calendarOption\":\"noselection\" \} |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_DEVIATION_API_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | Unauthorized \{HeaderToken\} could be missing or expired |
| 400 | 400 | Bad request |


### 

## POST- DRILLDOWN DEVIATION

The drilldown deviation API is part of the IAI-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. This API is a POST call that is used to calculate the deviated value for each contributor and influencer. After calculating all deviated values, the drilldown details are shown on the UI.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. E.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| startdate | Start date to perform the calculation M 255 String |
| enddate | End date to perform the calculation M 255 String |
| calendarOption | Available calendar Options (noselection\} M 255 String |
| kpiList | List of kpiList ex.\["C-B1-G1-R1-F1"\] M 255 List |


#### Output Header Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. M-Public 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It is used to let the receiving entity know how much data to expect. O-Public 255 |
| date | Date of operation execution O-Public 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. O-Public 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. O-Public 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs to. O-Public 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. O-Public 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. O-Public 255 |


#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | The numeric identifier of the error M String |
| errorDescription | Alphanumeric explanation of the error M String |
| Services | List of the created Service\ O List |
| kpitile | Timeseries id M String |
| id | Timeseries External Id M String |
| deviation | Deviation value M String |
| error | Error object if any M String |
| ### | API Precondition To fetch the response from the drilldown deviation API, the authorization token must exist. |


#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** |  |
| **PATH IAI (AWS) \** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Request** | \{ \"startdate\": \"2023-10-10T08:57:07.209Z\", \"enddate\": \"2023-10-10T08:57:07.209Z\", \"calendarOption\": \"noselection\", \"kpiList\": \[ \"C-B1-G1-R1-F1-P-PP-U2:ea737d1b-97f6-41cb-b6fa-159b47abb884\", \"C-B1-G1-R1-F1-P-PP-U1:ea737d1b-97f6-41cb-b6fa-159b47abb884\", \"C-B1-G1-R1-F1-P-PP-U3:ea737d1b-97f6-41cb-b6fa-159b47abb884\" \] \} |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_DRILLDOWN_DEVIATION_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 401 Unauthorized / \{HeaderToken\} could be missing or expired |
| 400 | 400 Bad request |

### 

## 

### POST- RAG

The RAG API, a component of the IAI-SmartKPI-Middleware API, is both invoked and utilized by the UI. This API is integrated into the Operation Hierarchy, specifically with the asset list. The RAG API generates a response that includes a color code (Red, Amber, or Green) for a specific requested asset, based on asset calculations. Within the Operation Hierarchy, the color code for each asset is displayed using the RAG API. Additionally, it checks the role-based permissions of each KPI that are mapped for requested assets.

#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. E.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| startdate | Start date to perform the calculation M 255 String |
| enddate | End date to perform the calculation M 255 String |
| calendarOption | Available calendar Options (noselection\} M 255 String |
| Asset_ExternalIds | List of asset external IDs ex.\["C-B1-G1-R1-F1"\] M 255 List |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** **M/O** **Type** |
| --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. O Object |
| errorCode | The numeric identifier of the error M String |
| errorDescription | Alphanumeric explanation of the error M String |
| Services | List of the created Service\ O List |
| AssetExternalId | External id of the asset M String |
| AssetName | Name of asset M String |
| Asset_ExternalId | The external ID of the asset M String |
| RAGStatus | RAG (Red, Amber, and Green) status of color that is updated in the RAG API M String |
| ### | API Precondition To fetch the response from the smart-kpitile, the authorization token must exist. |


#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/ragkpi](https://apim-aot-mw-dev.azure-api.net/api/smartkpi/ragkpi) |
| **PATH IAI (AWS) \** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Request** | \{ \"startdate\": \"2023-11-30T06:06:01.855Z \", \"enddate\": \"2023-11-30T06:06:01.855Z\", \"calendarOption\": \"noselection\", \"Asset_ExternalIds\": \[ \"C-B1-G2-R1-F1-P-PP-U2-MOLP1\", \"C-B1-G2-R1-F1\", \"C\", \"C-B1-G1-R1-F1-P-PP-U2-MOLP2\" \] \} |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_RAG_API_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 401 Unauthorized / \{HeaderToken\} could be missing or expired |
| 400 | 400 Bad request |
| ## | POST- INSIGHT API The INSIGHT API is part of the IAI-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. Insight API is a POST call to the Smart KPI IAI DEV server is hosted at the backend to get the details of actual, forecast, historical, target, RAGStatus, and CompareActual calculations for a KPI. |


#### Input Header Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| authorization | Token acquired from Azure AD based on the user credentials for further API calls. E.g., msal.accesstoken : \{ token: \"\\" \} M-Public \- String |


#### Input Body Parameters


| **Parameter** | **Description** **M/O** **Max Length** **Type** |
| --- | --- |
| startdate | Start date to perform the calculation M 255 String |
| enddate | End date to perform the calculation M 255 String |
| calendarOption | Available calendar Options (custom) M 255 String |


#### Output Header Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in AWS API Gateway. This identifier is used within the API Gateway instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in API Gateway. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In API Gateway, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the API Gateway instance. In API Gateway, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When API Gateway tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |



#### Output Body Parameters


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. | O | Object |
| errorCode | The numeric identifier of the error | M | String |
| errorDescription | Alphanumeric explanation of the error | M | String |
| Services | List of the created Service\ | O | List |
| Actual | The Actual calculation of the KPI depends on its configuration. For example: If a KPI is configured to be calculated at 12 AM every day, the actual value would depend on the past 24hrs data i.e., 12 AM the previous day to 12 AM the current day. ex:( C-B1-G1-R1-F1:OEE) | M | String |
| CalculationFrequency | Frequency of KPI calculation. Ex:5min,10min,30min,1h,12h | M | String |
| Forecast | Forecast refers to the average of the actual KPI values calculated over the past seven days. These calculated values are stored in its dedicated timeseries ID in CDF. ex:( C-B1-G1-R1-F1:OEE_Forecast) | M | String |
| Historical | Historical refers to the peak performance of a specific KPI recorded on any given day during the preceding 12 months. These calculated values are stored in its dedicated timeseries ID in CDF ex:( C-B1-G1-R1-F1-P-PP-U1:OEE_Historical) | M | String |
| RAGStatus | This visually represents the performance of the KPI. For example, if the actual value of the KPI is being compared with its target value, then it represents how the performance compares. | M | String |
| Target | Target represents the target value of the KPI. This can be a static value or can also be a dynamic target such that the target might be updated every shift or at a specific time interval. ex:(C-B1-G1-R1-F1-P-PP-U1:OEE_target) | M | String |
| assetid | Level in the asset hierarchy against which the KPI must be computed. | M | String |
| isKpi | Returns a Boolean response (True or False) and checks whether the response is for KPI or Parameter. | M | String |
| KPI direction | Returns response (Up or Down) arrow and checks whether it's best performing or worst performing. | M | String |
| uid | Unique ID - The system automatically generates a unique identity for each KPI that is created by the user | M | String |



####  API Precondition

To fetch the response from the response from the Insight API, the authorization token must exist.

#### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** | [https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/insightkpi](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/insightkpi) |
| **PATH IAI (AWS) \** | [https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/insightkpi](https://cn13sbr3r6.execute-api.us-west-2.amazonaws.com/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/insightkpi) |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Request** | \{ \"startdate\":\"2022-07-13T06:30:00Z\", \"enddate\":\"2022-07-13T08:30:59Z\", \"calendarOption\":\"custom\" \} |
| **JSON Response** | [Link](../../../../../:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_INSIGHT_API_JSON_Response.txt) |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | Service executed successfully |


#### Error Management


| **HTTP Code** | **Error Code** **Error Description** |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 401 Unauthorized / \{HeaderToken\} could be missing or expired |
| 400 | 400 Bad request |
