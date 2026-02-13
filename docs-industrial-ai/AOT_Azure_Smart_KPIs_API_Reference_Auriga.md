---
sidebar_position: 2
title: AOT Azure Smart KPIs API Reference Auriga
---

**Accenture Operations Twin**

Smart KPIs

API REFERENCE

(Azure)

Release Version: 2.5

#  \{#section .TOC-Heading\}

# Contents

[Introduction [3](#introduction)](#introduction)

[Target Audience [3](#target-audience)](#target-audience)

[Purpose [3](#purpose)](#purpose)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Smart KPIs APIs [4](#smart-kpis-apis)](#smart-kpis-apis)

[OT (Operation Twin) KPIs [4](#ot-operation-twin-kpis)](#ot-operation-twin-kpis)

[Non-OT KPIs [4](#non-ot-kpis)](#non-ot-kpis)

[Authentication [4](#authentication)](#authentication)

[API Data Flow Mapping [5](#api-data-flow-mapping)](#api-data-flow-mapping)

[Smart KPIs Configuration Microservice APIs [6](#smart-kpis-configuration-microservice-apis)](#smart-kpis-configuration-microservice-apis)

[POST- CREATE CONFIG FILE [6](#post--create-config-file)](#post--create-config-file)

[POST- KPI CREATION [8](#post--kpi-creation)](#post--kpi-creation)

[POST- DOWNLOAD EXCEL [10](#post--download-excel)](#post--download-excel)

[GET- KPISPERPLANT [12](#get--kpisperplant)](#get--kpisperplant)

[Smart KPIs Microservice APIs [14](#smart-kpis-microservice-apis)](#smart-kpis-microservice-apis)

[GET- KPI DASHBOARD [14](#get--kpi-dashboard)](#get--kpi-dashboard)

[POST - KPI DRILLDOWN [16](#post---kpi-drilldown)](#post---kpi-drilldown)

[POST- SMART KPI TILE [18](#post--smart-kpi-tile)](#post--smart-kpi-tile)

[POST- TRENDLINE [22](#post--trendline)](#post--trendline)

[GET- LIST [24](#get--list)](#get--list)

[POST- DEVIATION [26](#post--deviation)](#post--deviation)

[POST- DRILLDOWN DEVIATION [28](#post--drilldown-deviation)](#post--drilldown-deviation)

[POST- RAG [30](#post--rag)](#post--rag)

[POST- INSIGHT API [32](#post--insight-api)](#post--insight-api)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including Smart KPIs, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Smart KPIs is a Micro Front-end Application that is mounted on the AOT application and is the landing page of the AOT application. It provides contextualized views of Key Performance Indicators (KPIs) to AOT users in both the boardroom and on the shop floor. The Smart KPIs application is invaluable for tracking performance issues as well as the actions taken to improve performance. On the backend, Smart KPIs are powered by several separate microservices that are described in this document.

## Target Audience

Client Delivery Teams planning to deliver Accenture Operations Twin.

## Purpose

This reference document includes information about paths, inputs, outputs, and error management for APIs related to AOT Smart KPIs on Azure. The document includes descriptions of APIs used for configuration as well as descriptions of APIs that provide middleware functionality.

##  Prerequisites

An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64).

## Contacts

-   

-   

-   

-   

## Related Links

-   

-   [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)[AOT General Architecture](https://industryxdevhub.accenture.com/assetdetails/53)

-   [AOT Smart KPIs Resources](https://industryxdevhub.accenture.com/assetdetails/42)

-   [AOT People Management Resources](https://industryxdevhub.accenture.com/assetdetails/64)



-   [API Management Documentation](https://docs.microsoft.com/en-us/azure/api-management/)

-   [REST API](https://restfulapi.net/) 

# 

# Smart KPIs APIs

The Python-based Smart KPIs microservices listed below are built and hosted in a cloud-agnostic Kubernetes environment that provides the APIs access to AOT functionalities and data through an API management service gateway---[Azure API Management REST API \| Microsoft Learn](https://learn.microsoft.com/en-us/rest/api/apimanagement/). It authenticates and authorizes registered APIs. See the related links section for more information on APIs.

The microservices act as middleware and provide a unified interface between the various backends of AOT and the consumers of the data. The APIs support both OT and Non-OT KPIs. For both types, the Computation Trigger time is mandatory and must be specified in 24 hours format (hh:mm:ss) UTC.

## 

## OT (Operation Twin) KPIs 

These APIs rely on time-series data points sourced from specific parameters. These parameters represent continuous data streams that capture asset performance over time. In this case the KPI Configuration template must have the Input_Resource_Type_Actual set to Timeseries.

## Non-OT KPIs

These APIs are driven by event-based data, typically linked to significant operational events, providing flexibility for event-driven monitoring. Non-OT KPIs support shift-based calculations. In this case, the Template Mapping Column is mandatory and the KPI Configuration template must have the Input_Resource_Type_Actual set to Events.

**Configuration Microservice KPIs**

The Smart KPIs Configuration Microservice is a flask-based microservice that is positioned between AOT\'s Smart KPI Config UI and Azure. The request received from the processed configuration tool UI is processed and the output is stored in the Azure portal. The API for the microservice can be called using Postman or the Smart KPIs Config UI tool with the necessary inputs. It is a clean canvas that stitches together other modularized AOT components. User login/authentication is part of the component

-   POST- CREATE CONFIG FILE

-   POST- KPI CREATION

-   POST- EXCELDOWNLOAD API

-   GET- KPISPERPLANT API

**Microservice APIs**

The middleware microservice provides a unified interface between the different backends of AOT and the consumers of the data (AOT Applications). These services are accessed from the AOT application and are used in end-user visualization. Using Smart KPIs, users can have a contextualized view of operational performance through KPIs and can critically analyze business performance and drive decisions.

-   GET- KPI DASHBOARD

-   GET- KPI DRILLDOWN

-   POST- SMART-KPITILE

-   POST- TRENDLINE API

-   GET- LIST API

-   POST- DEVIATION API

-   POST- DRILLDOWN DEVIATION

-   POST-RAG API

-   POST-INSIGHT API

## Authentication

The APIs use an authentication token, which can be retrieved either from the AOT UI interface or using a tool like Postman, Requirements other than the authentication token, if any, are mentioned under the corresponding KPI. All the time zones are in [Epoch time UTC](https://www.epochconverter.com/) format.

# 

# API Data Flow Mapping

**Configuration Microservice KPIs**: APIs that manage the creation and configuration of KPIs, primarily interacting with the Azure SQL Server.

**Microservice KPIs**: APIs that are used for the front end of Smart KPIs, and interact with Azure SQL Server, Azure Data Explorer, and Azure Digital Twins.


| Type | Data Flow | API |
| --- | --- | --- |
| Configuration Microservice KPIs | Azure SQL Server | POST- CREATE CONFIG FILE |
|  |  | POST- KPI CREATION |
|  |  | POST- EXCELDOWNLOAD API |
|  |  | GET- KPISPERPLANT API |
| Microservice KPIs | Azure Digital Twins | GET- KPI DASHBOARD |
|  | Azure SQL Server | GET- KPI DRILLDOWN |
|  |  | POST- SMART-KPITILE |
|  |  | POST- TRENDLINE API |
|  |  | GET- LIST API |
|  |  | POST- DEVIATION API |
|  |  | POST-DRILLDOWN DEVIATION |
|  |  | POST-RAG API |
|  |  | POST-INSIGHT API |


# 

# Smart KPIs Configuration Microservice APIs

## POST- CREATE CONFIG FILE

The create config file Azure API is a part of the AOT-SmartKPI-Configuration Microservice that is invoked by the UI to be consumed by the UI. The create config file API is used to validate the KPI Template Excel file.\
Once all these validations are done and there is no error found, the user can access the KPI Hierarchy creation part. To upload the KPI Template and validate, the Azure blob File Path and Authorization token must exist.

### 

### Specification

  -----------------------------------------------------------------------------------------------------------
  PROTOCOL        HTTPS
  --------------- -------------------------------------------------------------------------------------------
  REQUEST URL     https://apim-aot-azure-dev.azure-api.net/api/smartkpi/configuration/file/assets/\{assetid\}

  METHOD          POST

  CONTENT TYPE    application / json

  JSON Response   \{\"message\": \"Request accepted\"\}
  -----------------------------------------------------------------------------------------------------------

### Input Header

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                            **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------ ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"Bearer \{token\}\" \}   M-Public   \*\*             String

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ---------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                  **M/O**   **Max Length**   **Type**
  --------------- -------------------------------------------------------------------------------- --------- ---------------- -----------------------
  File path       \{\"Path\":\"\{smartkpibase\}/initialtemplate/\/\.xlsm\"\}   M         \*\*             Multipart / Form-data

  ---------------------------------------------------------------------------------------------------------------------------------------------------

### Output Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**             **Description**                                                                                                                                                                                                                                                      **M/O**    **Type**
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------
  Content-Type              Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data.                                                                                                                     M-Public   255

  Content-Length            Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It is used to let the receiving entity know how much data to expect.                                                                                                O-Public   255

  date                      Date of operation execution                                                                                                                                                                                                                                          O-Public   255

  ocp-apim-apiid            This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs.                                                                                            O-Public   255

  ocp-apim-operationid      This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked.                                                                                                 O-Public   255

  ocp-apim-productid        This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to.                                                               O-Public   255

  ocp-apim-subscriptionid   This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization.                                                    O-Public   255

  ocp-apim-trace-location   This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues.   O-Public   255
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Output Body

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                                                                                                                                                                                                                                                                                                                                                       **M/O**   **Type**
  ------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- ----------
  errorManagement    This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue.                                                                                                                                         O         Object

  errorCode          This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors.                                                                                                                                                                              M         String

  errorDescription   This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error.   M         String
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

\*M/O: Mandatory/Optional

### Result

  -------------------------------------------------------------------------------
   **HTTP Code**  **Result Description**
  --------------- ---------------------------------------------------------------
        202       \{\"message\": \"Request accepted\"\}

  -------------------------------------------------------------------------------

### Error Management

  -------------------------------------------------------------------------------------------
   **HTTP Code**   **Error Code**  **Error Description**
  --------------- ---------------- ----------------------------------------------------------
        500             500        Generic Error

        401             401        Unauthorized, 401 / \"Bearer \{token\}\" could be missing,
  -------------------------------------------------------------------------------------------

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

\"Invalid: Error occurred during File uploading to blob- \{exception_message\} \"

\"Invalid : Archiving restricted. This KPI \ is a contributing kpi for: \.\"

\"Invalid : Department - \ has not been created in the People Management tool.\
Please ensure that the departments added in the template are created in the People Management tool.\"

\"Invalid : Role - \ has not been created in the People Management tool.\
Please ensure that the roles added in the template are created in the People Management tool.\"

\"Invalid : \ - \ association does not match the role configuration in the People Management tool. Please ensure that the roles mapped to the departments in the template is as per the role configuration in the People Management tool.\" 

## 

## POST- KPI CREATION

KPI creation is a POST call to the Smart KPI AOT server hosted at the backend. This API picks the Template uploaded by the user from Azure Blob Storage, processes the data, generates UID/Config_ID details, fetches JSON files uploaded in Azure, and creates the KPI hierarchy by adding KPI twins with Update_flag as update, relationships, and metadata information. It also identifies low level KPIs and Events and create schedulers in Generic scheduler for sending data to event hub for further computation. To fetch the response from the KPI creation operation, the authorization token must exist.

### Specification

  ---------------------------------------------------------------------------------------------------------------
  **PROTOCOL**        HTTPS
  ------------------- -------------------------------------------------------------------------------------------
  **REQUEST URL**     https://apim-aot-azure-dev.azure-api.net/api/smartkpi/kpi/creation

  **METHOD**          POST

  **CONTENT TYPE**    application / json

  **JSON Request**    \[\
                        \{\
                          \"plantId\":\"C-B1-G1-R1-F1\",\
                          \"templatePath\":\"\{smartkpibase\}/initialtemplate/C-B1-G1-R1-F1/Oil&GasField1.xlsm\"\
                        \}\
                      \]

  **JSON Response**   \{\"message\": \"Process started\...\...\"\}
  ---------------------------------------------------------------------------------------------------------------

### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                             **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-               String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ------------------------------------------------------------------------------------------
  **Parameter**   **Description**                      **M/O**   **Max Length**   **Type**
  --------------- ------------------------------------ --------- ---------------- ----------
  plantid         ExternalID of Uploading Plant        M         255              String

  templatepath    File path                            M         255              String
  ------------------------------------------------------------------------------------------

### Output Header

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**             **Description**                                                                                                                                                                                                                                                      **M/O**    **Type**
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- -----------
  Content-Type              Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data.                                                                                                                     M-Public   255

  Content-Length            Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It is used to let the receiving entity know how much data to expect.                                                                                                O-Public   255

  date                      Date of operation execution                                                                                                                                                                                                                                          O-Public   255

  ocp-apim-apiid            This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs.                                                                                            O-Public   255

  ocp-apim-operationid      This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked.                                                                                                 O-Public   255

  ocp-apim-productid        This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to.                                                               O-Public   255

  ocp-apim-subscriptionid   This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization.                                                    O-Public   255

  ocp-apim-trace-location   This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues.   O-Public   255
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Output Body

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                                                                                                                                                                                                                                                                                                                                                       **M/O**   **Type**
  ------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- -----------
  errorManagement    This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue.                                                                                                                                         O         Object

  errorCode          This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors.                                                                                                                                                                              M         String

  errorDescription   This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error.   M         String

  services           This refers to the array or list of Service objects that have been created because of the operation.                                                                                                                                                                                                                                                                                                  O         List

  Status             Displays the KPI creation status                                                                                                                                                                                                                                                                                                                                                                      M         String
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  ---------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- -----------------------------------------------------------
  202             \{\"message\": \"Process started\...\...\"\}

  ---------------------------------------------------------------------------

### Error Management

  -------------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**   **Error Description**
  --------------- ---------------- ----------------------------------------------------------
  500             500              Generic Error

  400             400              Bad request

  401             401              Unauthorized (authorization token is missing or expired)
  -------------------------------------------------------------------------------------------

## 

## POST- DOWNLOAD EXCEL 

The download excel-template API is a part of the AOT-SmartKPI- Configuration Microservice that is invoked by the UI and consumed by the UI. The Download template API is a POST call to the Smart KPI AOT server hosted at the backend. It triggers the download functionality for the updated template that has been stored in an Azure blob storage with proper UUID, Status, and Version generated. To fetch the response from the download template operation, the authorization token must exist.

### 

### Specification


| **PROTOCOL** | HTTPS |
| --- | --- |
| **REQUEST URL** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **JSON Response** | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_EXCELDOWNLOAD_JSON_Response.txt) |
| **JSON Request Body** | \{ |
|  | \"asset-files\": \[ |
|  | \{ |
|  | \"key\": \"Multi-Plant\", |
|  | \"external_id\": \"Multi-Plant\" |
|  | \} |
|  | \] |
|  | \} |


### Input Header

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                            **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------ ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"Bearer \{token\}\" \}   M-Public   \-               String

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  -------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                             **M/O**   **Max Length**   **Type**
  --------------- ------------------------------------------- --------- ---------------- ----------
  Asset-files     It contains Key and ExternalId parameters   M         \-               List

  -------------------------------------------------------------------------------------------------

### Output Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**             **Description**                                                                                                                                                                                                                                                      **M/O**    **Type**
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------
  Content-Type              Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data.                                                                                                                     M-Public   255

  Content-Length            Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It\'s used to let the receiving entity know how much data to expect.                                                                                                O-Public   255

  date                      Date of operation execution                                                                                                                                                                                                                                          O-Public   255

  ocp-apim-apiid            This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs.                                                                                            O-Public   255

  ocp-apim-operationid      This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked.                                                                                                 O-Public   255

  ocp-apim-productid        This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to.                                                               O-Public   255

  ocp-apim-subscriptionid   This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization.                                                    O-Public   255

  ocp-apim-trace-location   This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues.   O-Public   255
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Output Body

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                                                                                                                                                                                                                                                                                                                                                       **M/O**   **Type**
  ------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- ----------
  errorManagement    This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue.                                                                                                                                         O         Object

  errorCode          This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors.                                                                                                                                                                              M         String

  errorDescription   This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error.   M         String

  services           This refers to the array or list of Service objects that have been created because of the operation.                                                                                                                                                                                                                                                                                                  O         List

  errorManagement    The object identifying the error. Provided only if there is an error.                                                                                                                                                                                                                                                                                                                                 O         Object

  Asset-files        external_id, key, path(path of this plant e.g., Multi-Plant.xlsm)                                                                                                                                                                                                                                                                                                                                     M         String
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- -------------------------------------------------------------
  200             Operation executed successfully

  -----------------------------------------------------------------------------

### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 401 | 401 | Unauthorized / \{Header Token\} Access token is missing or invalid |
| 400 | 400 | Bad request |
|  |  | **Example**: |
|  |  | \"Invalid File or File name\" |
|  |  | \"Unable to connect file storage\" |


## 

## GET- KPISPERPLANT

The KPISPERPLANT API is a part of the AOT-SmartKPI-Configuration Microservice that is invoked by the UI and consumed by the UI. KPISPERPLANT is a GET call and it is used to fetch details of the selected plant from the dropdown menu in the SmartkpiConfig page. To fetch the response from the smart-kpititle, the authorization token must exist.

### Specification

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PROTOCOL        HTTPS
  --------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  REQUEST URL     https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{plantexternalid\}/kpisperplant

  METHOD          GET

  CONTENT TYPE    application / json

  JSON Response   [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/GET_KPISPERPLANT_JSON_Response.txt)

  Request URL     https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1/kpisperplant
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Header

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                                                                                M/O        Max Length   Type
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------ ---------- ------------ --------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"Bearer \{token\}\" \}   M-Public   \-           String

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Path

  ----------------------------------------------------------------------------------------------------------------------------
  Parameter         Description                                                                   M/O    Max Length   Type
  ----------------- ----------------------------------------------------------------------------- ------ ------------ --------
  plantExternalId   External id of the KPI the asset is linked to \[e.g., path value\\]   M      255          String

  ----------------------------------------------------------------------------------------------------------------------------

### Output Header


| Parameter | Description | M/O | Type |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |


### 

### Output Body

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter                    Description                                                                                                                M/O     Type
  ---------------------------- -------------------------------------------------------------------------------------------------------------------------- ------- --------
  errorManagement              The object identifying the error. Provided only if there is an error.                                                      O       Object

  errorCode                    The numeric identifier of the error                                                                                        M       String

  errorDescription             Alphanumeric explanation of the error                                                                                      M       String

  Services                     List of the created Services                                                                                               O       List

  Asset Hierarchy Mapping      Returns the Level (plant, unit, system, sub-system) of the timeseries of KPI and parameter                                 M       String

  Calculation Frequency        Frequency of KPI calculation. Selected from dropdown list, e.g. (5min,30min,1h,12h)                                        M       String

  Config_Id                    Unique ID of the external ID                                                                                               M       String

  KPI Calculation_Actual       The formula used to calculate the actual value of KPI, which depends on the configuration.                                 M       String

  KPI Name                     Name of the KPI to be computed and displayed in UI. The KPI name should be unique and cannot have duplicates for a plant   M       String

  KPI_TimeAggregation_Actual   The formula used to aggregate the actual values of KPI based on the time frame that has been selected by the user          M       String

  Product Hierarchy Mapping    External id of the product                                                                                                 M       String

  Responsible Role             The role which is responsible for the KPI                                                                                  M       String

  Status                       The status of the KPI whether it is already published or ready to be published is generated by the system                  M       String
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  **HTTP Code**    **Result Description**
  ---------------- ------------------------------------------------------
  200              Operation executed successfully

  -----------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**   **Error Description**
  --------------- ---------------- -----------------------------------------------------------
  500             500              Generic Error

  401             401              Unauthorized / \{Header Token\} could be missing or expired

  400             400              Bad request
  --------------------------------------------------------------------------------------------

# 

# Smart KPIs Microservice APIs

## GET- KPI DASHBOARD

The KPI dashboard API, part of the AOT-SmartKPI-Middleware Microservice, is a GET request to retrieve parent KPI details from the backend Smart KPI AOT server. It displays all KPIs owned by the signed-in user, as identified by the GET UsersToken API. Owners have read and write permissions for Asset Hierarchy and Timeseries. The API checks Timeseries and asset access, roles sensitivity, and KPI sensitivity. Dashboard drilldown depends on the user\'s asset access, determined by shared roles. The API\'s disableFurtherDashboardDrilldown attribute indicates whether further drilldown is allowed. Archived KPIs can be fetched by setting the ArchivedKPI parameter to True. To fetch the response from the download template operation, the authorization token must exist. The necessary attributes and metadata are correctly mapped in the asset hierarchy. See example.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}](https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Request URL |  |
|  | [https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}?includeArchivedKPI=True](https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d?includeArchivedKPI=True) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/Azure%20Smart%20KPIs%20API%20Reference/2.2/Azure_KPI_Dashboard_Response.txt) |


### Input Header

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                                                                                M/O\*      Max Length   Type
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------ ---------- ------------ --------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g.- msal.accesstoken : \{token: \"\\" \}   M-Public   \-           String

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Path

  -------------------------------------------------------------------------------------------------------------------------------------
  Parameter            Description                                                                        M/O    Max Length   Type
  -------------------- ---------------------------------------------------------------------------------- ------ ------------ ---------
  assetid              External id of the KPI the asset is linked to \[e.g., path value\\]        M      255          String

  kpiname              UID of the KPI \[e.g., path value\\]                                       M      255          String

  includeArchivedKPI   Boolean value to include archived KPIs. If nothing is given, considered as false   0      \-           Boolean
  -------------------------------------------------------------------------------------------------------------------------------------

### Output Header


| Parameter | Description | M/O | Type |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |
| disableFurtherDashboardDrilldown | The disableFurtherDashboardDrilldown attribute returns a boolean value, either true or false, which dictates whether additional drilldown from the dashboard is permitted or not. | M | 255 |


### 

### Output Body


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. | O | Object |
| errorManagement | This is an object that is included in the response only if an error has occurred during the processing of the request. It serves to identify the nature of the error and provides relevant information for understanding and potentially resolving the issue. | O | Object |
| errorCode | This is a numeric identifier associated with the specific type of error that occurred. Each type of error has a unique code. These codes can be used for categorizing, prioritizing, and systematically handling errors. | M | String |
| errorDescription | This is an alphanumeric string that provides a human-readable explanation of the error. It is designed to give developers a clear understanding of what went wrong during the processing of the request. This could involve issues like invalid input data, problems with the server, or other unexpected conditions. The description often includes suggestions for how to avoid or fix the error. | M | String |
| services | This refers to the array or list of Service objects that have been created because of the operation. | O | List |
| errorCode | The numeric identifier of the error | M | String |
| errorDescription | Alphanumeric explanation of the error. | M | String |
| services | List of the created Services | O | List |
| assetid | The external ID of the asset the KPI is linked to, | M | String |
| productid | The external ID of the product | M | String |
| uid | The uid of the KPI | M | String |
| kpiname | Name of the KPI configured in the KPI config template. Example: \[Thesis differentfreq, Thesis samefreq diffrole\]. Please note that the name of the KPI cannot be duplicated for parameters and the KPI name should match exactly with the timeseries name. | M | String |
| kpititle | Timeseries id or name of Timeseries Example: (C-B1-G1-R1-F1-P: Thesis differentfreq, C-B1-G1-R1-F1-P: Thesis differentfreq, C-B1-G1-R1-F1: OEE, C-B1-G1-R1-F1-P-PP-U1-EGCA: RunHours, C-B1-G1-R1-F1:OEE) | M | String |
| Department | Each KPI is assigned a department based on its relevancy to the department | M | String |
| ResponsibleRole | The responsible Role represents the owner role for the KPI in the KPI Hierarchy | M | String |
|  | Example: (Production Engineer, Admin_PeopleManagement, Maintenance Manager) |  |  |
| CalculationLogic | Aggregationlogic with UoM represents the formula used to aggregate the KPIs at various levels of the asset hierarchy or aggregate based on the time frame that has been selected by the user. | M | String |
| details | Contains the config_id, name, parent_external_id, description, UoM, KPI_Name, source id, created_time, last_updated_time, root_id, ConfigurationUoM, Input_Resource_Type_Actual | M | List |
| assetName | Asset name from asset hierarchy |  |  |
| TimeseriesRole | Identify the timeseries access, being an \'owner\' implies that both read and write permissions are granted, whereas being a \'viewer\' means only read permission is provided |  |  |
| TemplateMapping | This represents the template to which NoN OT KPI belongs to. |  | String |


### Result

  -----------------------------------------------------------------------
  **HTTP Code**         **Result Description**
  --------------------- -------------------------------------------------
  200                   Operation executed successfully

  -----------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**   **Error Description**
  --------------- ---------------- -----------------------------------------------------------
  500             500              Generic Error

  401             401              Unauthorized / \{Header Token\} could be missing or expired

  400             400              Bad request
  --------------------------------------------------------------------------------------------

## 

## POST - KPI DRILLDOWN

The KPI drilldown API is part of the AOT-SmartKPI-Middleware Microservice that is invoked and consumed by the UI. It is a POST call to the Smart KPI AOT server hosted at the backend to get the contributing and influencing KPI details (external IDs) which are displayed to the user on clicking on the KPI tile. The drilldown details displayed to a user are based on the user\'s role authorizations, which the Drilldown API fetches from a People Management API. For more information on how this API communicates with the People Management component, refer to the [People Management Integration with Smart KPIs document](https://industryxdevhub.accenture.com/assetdetails/64). To fetch the KPI drilldown, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/drilldown](https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/drilldown) |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Request URL |  |
| JSON Request Body | \{ |
|  | \"startdate\":\"2023-12-01T09:00:39.308Z\", |
|  | \"enddate\":\"2023-12-01T09:00:39.308Z\", |
|  | \"calendarOption\":\"noselection\" |
|  | \} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/Azure%20Smart%20KPIs%20API%20Reference/2.2/Azure_KPI_Drilldown_Response.txt) |


### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                             **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-               String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Path

  ---------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                   **M/O**   **Max Length**   **Type**
  --------------- --------------------------------------------------------------------------------- --------- ---------------- ----------
  assetid         The external ID of the KPI the asset is linked to \[e.g., path value\\]   M         255              String

  assetName       The Name of the KPI the asset is linked to                                        M         255              String

  kpiname         UID of the KPI \[e.g., path value\\]                                      M         255              String
  ---------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**    **Description**                                                                                                **M/O**   **Max Length**   **Type**
  ---------------- -------------------------------------------------------------------------------------------------------------- --------- ---------------- ----------
  startdate        Start date to perform the calculation                                                                          M         255              String

  enddate          End date to perform the calculation                                                                            M         255              String

  calendarOption   Available calendar Options (noselection, hours, day, weeks, monthly, quarterly, half-yearly, yearly, custom)   M         255              String
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Output Header

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**             **Description**                                                                                                                                                             **M/O**    **Type**
  ------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------
  Content-Type              Type of the content It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data.                             M-Public   255

  Content-Length            Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It\'s used to let the receiving entity know how much data to expect.       O-Public   255

  date                      Date of operation execution                                                                                                                                                 O-Public   255

  ocp-apim-apiid            This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs.   O-Public   255

  ocp-apim-operationid      This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked.        O-Public   255

  ocp-apim-productid        Contains the product ID of the API it is tagged                                                                                                                             O-Public   255

  ocp-apim-subscriptionid   Contains the subscription ID of the APIM instance                                                                                                                           O-Public   255

  ocp-apim-trace-location   Contains the URL to trace the output                                                                                                                                        O-Public   255
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Output Body

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                                                                                                                                                                                                                                  **M/O**   **Type**
  ------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- ----------
  errorManagement    The object identifying the error. Provided only if there is an error.                                                                                                                                                                                                            O         Object

  errorCode          Numeric identifier of the error.                                                                                                                                                                                                                                                 M         String

  errorDescription   Alphanumeric explanation of the error.                                                                                                                                                                                                                                           M         String

  services           List of the created Service\                                                                                                                                                                                                                                                 O         List

  Contributing       Contributing KPIs represent all the KPIs of a selected KPI which directly influence the value/ performance of the selected KPI. For example: for OEE at the plant level, the contributing KPIs can be availability, performance, and OEE at the system level among other KPIs.   M         String

  Influencing        Influencing KPIs represent all the KPIs of a selected KPI that indirectly influence the value/ performance of the selected KPI. For example: for OEE at the plant level - the influencing KPIs can be no. of safety incidents among other KPIs.                                  M         String
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  **HTTP Code**    **Result Description**
  ---------------- ------------------------------------------------------
  200              operation executed successfully

  -----------------------------------------------------------------------

### Error Management

  ------------------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**   **Error Description**
  --------------- ---------------- ---------------------------------------------------------------
  500             500              Generic Error

  401             401              Unauthorized / \"Bearer \{token\}\" could be missing or expired

  400             400              Bad request
  ------------------------------------------------------------------------------------------------

## 

## POST- SMART KPI TILE

The smart kpitile API is a part of the AOT-SmartKPI-Middleware Microservice. It is invoked by the UI and consumed by the UI. This API is a POST call to the Smart KPI AOT DEV server hosted at the backend to get the details of actual, forecast, historical, target, RAGStatus, and CompareActual calculations for KPI. In the case of a parameter, the details fetched are actual, forecast, and target calculations. To fetch the response from the smart-kpitile, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/detail](https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/%7bkpiname%7d/detail) |
| METHOD | POST |
| CONTENT TYPE | application / json |
| REQUEST URL |  |
| REQUEST URL(PARAMETER) | [https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/detail?productid=l1](https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/detail?productid=l1) |
| JSON Request Body | \{ |
|  | \"startdate\":\"2023-11-29T15:47:39.061Z\", |
|  | \"enddate\":\"2023-11-29T15:47:39.061Z\", |
|  | \"calendarOption\":\"noselection\" |
|  | \} |


### Input Header

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                               **M/O**    **Max Length**   **Type**
  --------------- --------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. Example: msal.accesstoken : \{ token: \"Bearer \{token\}\" \}   M-Public   \-               String

  productid       Unique Id of a product from product hierarchy(ex:l1)                                                                                          O          \-               String
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**            **Description**                                                                                                                                                                                                                                                                                               **M/O**   **Max Length**   **Type**
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------- ---------------- ----------
  startdate                Start date to perform the calculation (ISO 8601 date format (i.e., YYYY-MM-DDTHH:mm:ss.sssZ))                                                                                                                                                                                                                 M         255              String

  enddate                  End date to perform the calculation (ISO 8601 date format (i.e., YYYY-MM-DDTHH:mm:ss.sssZ))                                                                                                                                                                                                                   M         255              String

  calendarOption           This parameter specifies whether a specific calendar option has been selected for the data range. In this case, \"noselection\" indicates that no specific calendar option has been selected. Available calendar Options (noselection, hours, day, weeks, monthly, quarterly, half-yearly, yearly, custom).   M         255              String

  drilldowndetails         This is an object that contains details for the drilldown operation.                                                                                                                                                                                                                                          M         255              String

  isSameCalcfreq           This is a Boolean parameter that signifies whether the calculation frequency of the parent KPI and the contributing or influencing KPI are the same. \'True\' means they have the same calculation frequency. \'False\' means they have different calculation frequencies.                                    M         255              String

  kpiRelationship          This indicates the relationship of the KPI being drilled down. \"AOT_ContributingKPI\" means the KPI being considered is a contributing KPI. \"AOT_InfluencingKPI\" means the KPI being considered is an InfluencingKPI.                                                                                      M         255              String

  isdrilldown              This is a Boolean parameter that indicates if a detail call is for contributing or influencing KPI.                                                                                                                                                                                                           M         255              String

  KPI_calculation_Actual   This parameter holds the calculation method for the KPI. Here, \"SK.average(\'Performance\')\" means the average of performance is calculated.                                                                                                                                                                M         255              String

  startdate_aggregate      This parameter represents the start date and time for the data range used for aggregation, given in the ISO 8601 format.                                                                                                                                                                                      M         255              String

  enddate_aggregate        This parameter represents the end date and time for the data range used for aggregation, given in the ISO 8601 format.                                                                                                                                                                                        M         255              String
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Path

  -----------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                               **M/O**   **Max Length**   **Type**
  --------------- ----------------------------------------------------------------------------- --------- ---------------- ----------
  assetid         External id of the KPI the asset is linked to \[e.g., path value\\]   M         255              String

  kpiname         UID of the KPI \[e.g., path value\\]                                  M         255              String
  -----------------------------------------------------------------------------------------------------------------------------------

### 

### Output Header


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |


### Output Body


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. | O | Object |
| errorCode | The numeric identifier of the error | M | String |
| errorDescription | Alphanumeric explanation of the error | M | String |
| services | List of the created Service\ | O | List |
| Actual | The Actual calculation of the KPI depends on its configuration. For example: If a KPI is configured to be calculated at 12 AM every day, the actual value would depend on the past 24hrs data i.e., 12 AM the previous day to 12 AM the current day. ex:( C-B1-G1-R1-F1:OEE) | M | String |
| Forecast | Forecast refers to the average of the actual KPI values calculated over the past seven days. These calculated values are stored in its dedicated timeseries ID in Azure. ex:( C-B1-G1-R1-F1:OEE_Forecast) | M | String |
| Historical | Historical refers to the peak performance of a specific KPI recorded on any given day during the preceding 12 months. These calculated values are stored in its dedicated timeseries ID in Azure like C-B1-G1-R1-F1-P-PP-U1:OEE_Historical | M | String |
| RAGStatus | This visually represents the performance of the KPI. For example, if the actual value of the KPI is being compared with its target value, then it represents how the performance compares. | M | String |
|  | The visualization incorporates a color-coded system based on the RAG (Red, Amber, Green) status configuration designated for the KPI. This means that the actual KPI values will be represented within red, amber, or green zones on the KPI tiles, providing an understanding of performance status. |  |  |
| Target | Target represents the target value of the KPI. This can be a static value or can also be a dynamic target such that the target might be updated every shift or at a specific time interval. ex:(C-B1-G1-R1-F1-P-PP-U1:OEE_target)) | M | String |
| CompareActual | The percentage comparison calculates the relative change between the two most recent values of a KPI. The formula for this calculation is ((current value - previous value) / previous value) \* 100. If the result of the calculation is positive, indicating an increase in the KPI, an upward-pointing arrow should be displayed. Conversely, if the result is negative, signifying a decrease in the KPI, a downward-pointing arrow should be displayed. The color of the arrow is determined based on the settings specified in the KPI Config template or the KPI configuration tool. | M | String |
| assetid | Level in the asset hierarchy against which the KPI must be computed. | M | String |
| iskpi | Returns a Boolean response (True or False) and checks whether the response is for KPI or Parameter. | M | String |
| uid | UID is the Unique ID that automatically generates a unique identity for each KPI created by the user. | M | String |
| kpiDirection | Returns response(Up or Down) arrow and checks whether it\'s best performing or worst performing. | M | String |
| UoM | Returns the response of the respective unit of measurement(e.g., kg). It retrieves the value from the Azure KPI hierarchy in timeseries metadata. | M | String |
| CalculationFrequency | Frequency ( 5nin,1Hr,1day, etc.) for the calculation of KPI | M | String |
| ConfiguredUoM | Configured \"Unit of Measurement\" on the KPI configuration template updated by the end-user | M | String |
| StandardUoM | The standard unit of measurement as per asset system ID. It retrieves the value from the Timeseries metadata | M | String |
| UoM_SystemID | Returns the response of the respective unit of measurement system ID(e.g., kg). It retrieves the value Asset metadata | M | String |


### Result

  ------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- --------------------------------------------------------
  200             Service executed successfully

  ------------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**   **Error Description**
  --------------- ---------------- -----------------------------------------------------------------
  500             500              Internal server error

  401             401              Unauthorized / \{HeaderToken\} Access token is missing or invalid

  400             400              Bad request
  --------------------------------------------------------------------------------------------------

### Requests and Response

Refer to [POST_smart_kpitile.zip](https://ts.accenture.com/:u:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.1/POST_smart_kpitile.zip?csf=1&web=1&e=yZ1q9o) for the JSON Requests and Responses. Right click a line in the selection list to view the request URL.

#### Selection

[No Calendar Selection for KPI\*](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U3-SWLPC/kpis/d6b9f38e-28db-4eb7-806e-da9969e39ffb/detail)

[No Calendar Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U3-SWLPC/kpis/d6b9f38e-28db-4eb7-806e-da9969e39ffb/detail)

[Hours Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Hours Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Days Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U3-SWLPC/kpis/d6b9f38e-28db-4eb7-806e-da9969e39ffb/detail)

[Days Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U3-SWLPC/kpis/d6b9f38e-28db-4eb7-806e-da9969e39ffb/detail)

[Weeks Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Weeks Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Monthly Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Monthly Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Quarterly Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Quarterly Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Half-yearly Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Half-yearly Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Yearly Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Yearly Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Custom Selection for KPI](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

[Custom Selection for Parameter](https://apim-mw-aot-dev.azure-api.net/api/smartkpi/assets/C-B1-G1-R1-F1-P-PP-U1-EGCA/kpis/Available%20Hours/detail)

\*The No Calendar Selection for KPI also performs the aggregation of all data points into one data point. This means that the data retrieved based on the user\'s specified start and end times is consolidated into a singular data point, presenting a unified view of the data over the selected time.

## 

## POST- TRENDLINE

The Trendline API is part of the AOT-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. A Trendline API is a POST call to the Smart KPI AOT DEV server hosted to execute Multiple APIs concurrently and return the consolidated result of all four APIs in JSON format. Trendline displays the trend charts for the selected KPIs for the selected timeframe in the calendar.

Data points used to display trend charts are currently aggregated on hourly basis for the sake of performance but can be customized according to client requirement. Viewing Insights and Actions are still applicable in the KPI comparison scenario. To fetch the response from the trendline API, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | https://apim-aot-azure-dev.azure-api.net/api/smartkpi/trendline |
| METHOD | POST |
| CONTENT TYPE | application / json |
| REQUEST URL | https://apim-aot-azure-dev.azure-api.net/api/smartkpi/trendline |
| JSON Request | \{ |
|  | \"startedate\":1700764200000, |
|  | \"enddate\":1701368999000, |
|  | \"kpilist\":\"C-B1-G1-R1-F1-P-PP-U1-EGCA:d6b9f38e-28db-4eb7-806e-da9969e39ffb\" |
|  | \} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/Azure%20Smart%20KPIs%20API%20Reference/2.2/Azure_Trendline_Response.txt) |


### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                             **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-               String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                              **M/O**   **Max Length**   **Type**
  --------------- -------------------------------------------------------------------------------------------------------------------------------------------- --------- ---------------- ----------
  startdate       Start date to perform the calculation(Unix Timestamp) [Timestamp Converter (timestamp-converter.com)](http://www.timestamp-converter.com/)   M         255              String

  enddate         End date to perform the calculation(Unix Timestamp) [Timestamp Converter (timestamp-converter.com)](http://www.timestamp-converter.com/)     M         255              String

  kpilist         ExternalId of the KPI (e.g., C-B1-G1-R1-F1-P-PP-U1-EGCA:d6b9f38e-28db-4eb7-806e-da9969e39ffb)                                                M         255              String
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Output Header


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |


### 

### Output Body

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                                                                                                                                                                                                                                **M/O**   **Type**
  ------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------- ----------
  errorManagement    The object identifying the error. Provided only if there is an error.                                                                                                                                                                                                          O         Object

  errorCode          The numeric identifier of the error                                                                                                                                                                                                                                            M         String

  errorDescription   Alphanumeric explanation of the error                                                                                                                                                                                                                                          M         String

  Services           List of the created Service\                                                                                                                                                                                                                                               O         List

  Actual             The Actual calculation of the KPI depends on its configuration. For example: If a KPI is configured to be calculated at 12 AM every day, the actual value would depend on the past 24hrs data i.e., 12 AM the previous day to 12 AM the current day. ex:( C-B1-G1-R1-F1:OEE)   M         String

  Forecast           Forecast refers to the average of the actual KPI values calculated over the past seven days. These calculated values are stored in its dedicated timeseries ID in Azure. ex:( C-B1-G1-R1-F1:OEE_Forecast)                                                                      M         String

  Historical         Historical refers to the peak performance of a specific KPI recorded on any given day during the preceding 12 months. These calculated values are stored in its dedicated timeseries ID in Azure ex:( C-B1-G1-R1-F1-P-PP-U1:OEE_Historical)                                    M         String

  Target             Target represents the target value of the KPI. This can be a static value or can also be a dynamic target such that the target might be updated every shift or at a specific time interval. ex:(C-B1-G1-R1-F1-P-PP-U1:OEE_target))                                             M         String

  kpititle           Timeseries external_id                                                                                                                                                                                                                                                         M         String

  kpiname            Name of that KPI                                                                                                                                                                                                                                                               M         String

  uid                UID is the Unique ID that automatically generates a unique identity for each KPI created by the user.                                                                                                                                                                          M         String

  assetid            Level in the asset hierarchy against which the KPI must be computed.                                                                                                                                                                                                           M         String

  assetName          The Name of the KPI the asset is linked to,                                                                                                                                                                                                                                    M         String

  UoM                Returns the response of the respective unit of measurement (e.g.: \"kg\"). It retrieves the value from the Azure KPI hierarchy in timeseries metadata.                                                                                                                         M         String
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  **HTTP Code**     **Result Description**
  ----------------- -----------------------------------------------------
  200               Service executed successfully

  -----------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------
  HTTP Code    Error Code    Error Description
  ------------ ------------- -----------------------------------------------------
  500          500           Generic Error

  400          401           Unauthorized user or HeaderToken missing or expired

  400          400           Bad request
  --------------------------------------------------------------------------------

## 

## GET- LIST

The List API is part of the AOT-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. A List API is a GET call to the Smart KPI AOT DEV server that is hosted to retrieve all timeseries available and to return it in JSON format. This API is also integrated with the People Management API and the GET Roles API. The API is designed to accept a path parameter that specifies the external ID of a plant. This endpoint can retrieve timeseries linked for both single and as well as multi-plant. When accessing this API, the \'asset\' query parameter should be replaced with the external ID of the plant. For multi-plant queries ensure that the format of the external ID is correctly updated as \"Multi-Plant\". To fetch the response from the smart-kpitile, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| JSON Response | [Plant](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.1/GET_List_Plant_JSON_Response.txt) \ | [Multi-plant](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.1/GET_List_Multiplant_JSON_Response.txt) |


### Input Header


| Parameter | Description | M/O | Max Length | Type |
| --- | --- | --- | --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M-Public | \- | String |
|  | e.g., msal.accesstoken : \{ token: \"\\" \} |  |  |  |


### Output Header


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |


### 

### Output Body

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**         **Description**                                                                                                                **M/O**   **Type**
  --------------------- ------------------------------------------------------------------------------------------------------------------------------ --------- ----------
  errorManagement       The object identifying the error. Provided only if there is an error.                                                          O         Object

  errorCode             The numeric identifier of the error                                                                                            M         String

  errorDescription      Alphanumeric explanation of the error                                                                                          M         String

  Services              List of the created Service\                                                                                               O         List

  assetHierarchyLevel   Returns the Level (plant, unit, system, sub-system) of the timeseries of KPI and parameter                                     M         String

  computationtrigger    Returns whenever any computation is getting triggered. For example, Time-based.                                                M         String

  department            Contains \"departmentId\" and \"departmentName\". Each KPI is assigned a department based on its relevancy to the department   M         String

  frequency             Frequency of KPI calculation e.g., 5min,10min,15min,30min                                                                      M         String

  name                  Timeseries external ID                                                                                                         M         String

  plantname             Name of the parent plantname (e.g., C-B1-G1-R1-F1)                                                                             M         String

  role                  Contains \"roleId\" and \"roleName\". Represent the Owner role assigned to the KPI in the KPI hierarchy                        M         String

  type                  Displays the type whether it is of type KPI or parameter                                                                       M         String

  uid                   unique identity only for KPI that is created by the user                                                                       M         String
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- -------------------------------------------------------------
  200             Service executed successfully

  -----------------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**    **Error Description**
  --------------- ----------------- ----------------------------------------------------------
  500             500               Generic Error

  400             401               Unauthorized / \{HeaderToken\} could be missing or expired

  400             400               Bad request
  --------------------------------------------------------------------------------------------

## 

## POST- DEVIATION

The Deviation API is part of the AOT-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. This API is a POST call that is used to calculate the deviated value for each KPI and to send the consolidated output (all KPI deviation values) according to which KPIs are sorted by performance and displayed on the UI. To fetch the response from the Deviation API the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/all/deviation](https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/%7bassetid%7d/kpis/all/deviation) |
| METHOD | POST |
| CONTENT TYPE | application / json |
| REQUEST URL |  |
| JSON Request | \{ |
|  | \"startdate\":\"2023-11-29T16:09:05.594Z\", |
|  | \"enddate\":\"2023-11-29T16:09:05.594Z\", |
|  | \"calendarOption\":\"noselection\" |
|  | \} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_DEVIATION_API_JSON_Response.txt) |


### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                                                                                 M/O        Max Length   Type
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ------------ --------
  authorization   Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-           String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                                                    M/O    Max Length   Type
  ---------------- -------------------------------------------------------------------------------------------------------------- ------ ------------ --------
  startdate        Start date to perform the calculation                                                                          M      255          String

  enddate          End date to perform the calculation                                                                            M      255          String

  calendarOption   Available calendar Options (noselection, hours, day, weeks, monthly, quarterly, half-yearly, yearly, custom)   M      255          String
  ------------------------------------------------------------------------------------------------------------------------------------------------------------

### Output Header


| Parameter | Description | M/O | Type |
| --- | --- | --- | --- |
| content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to. | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |


### 

### Output Body

  -----------------------------------------------------------------------------------------------------------
  Parameter          Description                                                             M/O     Type
  ------------------ ----------------------------------------------------------------------- ------- --------
  errorManagement    The object identifying the error. Provided only if there is an error.   O       Object

  errorCode          The numeric identifier of the error                                     M       String

  errorDescription   Alphanumeric explanation of the error                                   M       String

  Services           List of the created Service\                                        O       List

  kpitile            Timeseries id                                                           M       String

  id                 Timeseries External Id                                                  M       String

  deviation          Deviation value                                                         M       String

  error              Error object if any                                                     M       String
  -----------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  HTTP Code    Result Description
  ------------ ----------------------------------------------------------
  200          Service executed successfully

  -----------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------------
  HTTP Code    Error Code     Error Description
  ------------ -------------- ----------------------------------------------------------
  500          500            Generic Error

  400          401            Unauthorized / \{HeaderToken\} could be missing or expired

  400          400            Bad request
  --------------------------------------------------------------------------------------

## 

## POST- DRILLDOWN DEVIATION

The drilldown deviation API is part of the AOT-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. This API is a POST call that is used to calculate the deviated value for each contributor and influencer. After calculating all deviated values, the drilldown details are shown on the UI. To fetch the response from the drilldown deviation API, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | https://apim-aot-azure-dev.azure-api.net/api/smartkpi/deviation |
| METHOD |  |
| CONTENT TYPE | application / json |
| JSON Request | \{ |
|  | \"startdate\": \"2023-10-10T08:57:07.209Z\", |
|  | \"enddate\": \"2023-10-10T08:57:07.209Z\", |
|  | \"calendarOption\": \"noselection\", |
|  | \"kpiList\": \[ |
|  | \"C-B1-G1-R1-F1-P-PP-U2:ea737d1b-97f6-41cb-b6fa-159b47abb884\", |
|  | \"C-B1-G1-R1-F1-P-PP-U1:ea737d1b-97f6-41cb-b6fa-159b47abb884\", |
|  | \"C-B1-G1-R1-F1-P-PP-U3:ea737d1b-97f6-41cb-b6fa-159b47abb884\" |
|  | \] |
|  | \} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_DRILLDOWN_DEVIATION_JSON_Response.txt) |


### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                             **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. E.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-               String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  -------------------------------------------------------------------------------------------------
  **Parameter**    **Description**                            **M/O**   **Max Length**   **Type**
  ---------------- ------------------------------------------ --------- ---------------- ----------
  startdate        Start date to perform the calculation      M         255              String

  enddate          End date to perform the calculation        M         255              String

  calendarOption   Available calendar Options (noselection)   M         255              String

  kpiList          List of kpiList ex.\[\"C-B1-G1-R1-F1\"\]   M         255              List
  -------------------------------------------------------------------------------------------------

### Output Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**             **Description**                                                                                                                                                                                                                                                      **M/O**    **Type**
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------
  Content-Type              Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data.                                                                                                                     M-Public   255

  Content-Length            Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It is used to let the receiving entity know how much data to expect.                                                                                                O-Public   255

  date                      Date of operation execution                                                                                                                                                                                                                                          O-Public   255

  ocp-apim-apiid            This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs.                                                                                            O-Public   255

  ocp-apim-operationid      This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked.                                                                                                 O-Public   255

  ocp-apim-productid        This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs to.                                                               O-Public   255

  ocp-apim-subscriptionid   This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization.                                                    O-Public   255

  ocp-apim-trace-location   This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues.   O-Public   255
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Output Body

  ---------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                         **M/O**   **Type**
  ------------------ ----------------------------------------------------------------------- --------- ----------
  errorManagement    The object identifying the error. Provided only if there is an error.   O         Object

  errorCode          The numeric identifier of the error                                     M         String

  errorDescription   Alphanumeric explanation of the error                                   M         String

  Services           List of the created Service\                                        O         List

  kpitile            Timeseries id                                                           M         String

  id                 Timeseries External Id                                                  M         String

  deviation          Deviation value                                                         M         String

  error              Error object if any                                                     M         String
  ---------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  **HTTP Code**                      **Result Description**
  ---------------------------------- ------------------------------------
  200                                Service executed successfully

  -----------------------------------------------------------------------

### Error Management

  -----------------------------------------------------------------------------------
  HTTP Code   Error Code        Error Description
  ----------- ----------------- -----------------------------------------------------
  500         500               Generic Error

  400         401               Unauthorized user or HeaderToken missing or expired

  400         400               Bad request
  -----------------------------------------------------------------------------------

## 

## POST- RAG

The RAG API is a component of the AOT-SmartKPI-Middleware API. This API is integrated into the Operation Hierarchy, specifically with the asset list. The RAG API generates a response that includes a color code (Red, Amber, or Green) for a specific requested asset, based on asset calculations. Within the Operation Hierarchy, the color code for each asset is displayed using the RAG API. Additionally, it checks the role-based permissions of each KPI that are mapped for requested assets. The RAG status of an Asset is based on the user\'s role permissions and sensitivities, which the RAG API fetches from a People Management API. For more information on how this API communicates with the People Management component, refer to the document [AOT Azure People Management Integration with SmartKPIs](https://industryxdevhub.accenture.com/assetdetails/42). To fetch the response from the smart-kpitile, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| JSON Request | \{ |
|  | \"startdate\": \"2023-11-30T06:06:01.855Z \", |
|  | \"enddate\": \"2023-11-30T06:06:01.855Z\", |
|  | \"calendarOption\": \"noselection\", |
|  | \"Asset_ExternalIds\": \[ |
|  | \"C-B1-G2-R1-F1-P-PP-U2-MOLP1\", |
|  | \"C-B1-G2-R1-F1\", |
|  | \"C\", |
|  | \"C-B1-G1-R1-F1-P-PP-U2-MOLP2\" |
|  | \] |
|  | \} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/2.0/POST_RAG_API_JSON_Response.txt) |


### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                             **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls. E.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-               String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ---------------------------------------------------------------------------------------------------------------
  **Parameter**       **Description**                                       **M/O**   **Max Length**   **Type**
  ------------------- ----------------------------------------------------- --------- ---------------- ----------
  startdate           Start date to perform the calculation                 M         255              String

  enddate             End date to perform the calculation                   M         255              String

  calendarOption      Available calendar Options (noselection)              M         255              String

  Asset_ExternalIds   List of asset external IDs ex.\[\"C-B1-G1-R1-F1\"\]   M         255              List
  ---------------------------------------------------------------------------------------------------------------

### Output Header


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| Content-Type | Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data. | M-Public | 255 |
| Content-Length | Length of the content. This is an HTTP header that indicates the size of the body data in bytes. | O-Public | 255 |
|  | It is used to let the receiving entity know how much data to expect. |  |  |
| date | Date of operation execution | O-Public | 255 |
| ocp-apim-apiid | This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs. | O-Public | 255 |
| ocp-apim-operationid | This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked. | O-Public | 255 |
| ocp-apim-productid | This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs | O-Public | 255 |
| ocp-apim-subscriptionid | This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization. | O-Public | 255 |
| ocp-apim-trace-location | This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues. | O-Public | 255 |


### 

### Output Body

  --------------------------------------------------------------------------------------------------------------------
  **Parameter**      **Description**                                                              **M/O**   **Type**
  ------------------ ---------------------------------------------------------------------------- --------- ----------
  errorManagement    The object identifying the error. Provided only if there is an error.        O         Object

  errorCode          The numeric identifier of the error                                          M         String

  errorDescription   Alphanumeric explanation of the error                                        M         String

  Services           List of the created Service\                                             O         List

  AssetExternalId    External id of the asset                                                     M         String

  AssetName          Name of asset                                                                M         String

  Asset_ExternalId   The external ID of the asset                                                 M         String

  RAGStatus          RAG (Red, Amber, and Green) status of color that is updated in the RAG API   M         String
  --------------------------------------------------------------------------------------------------------------------

### Result

  ----------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- ------------------------------------------------------------
  200             Service executed successfully

  ----------------------------------------------------------------------------

### Error Management

  ---------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**    **Error Description**
  --------------- ----------------- -----------------------------------------------------
  500             500               Generic Error

  400             401               Unauthorized user or HeaderToken missing or expired

  400             400               Bad request
  ---------------------------------------------------------------------------------------

## 

## POST- INSIGHT API

The INSIGHT API is part of the AOT-SmartKPI-Middleware Microservice that is invoked by the UI and consumed by the UI. Insight API is a POST call to the Smart KPI AOT DEV server hosted at the backend to get the details of actual, forecast, historical, target, RAGStatus, and CompareActual calculations for a KPI. To fetch the response from the response from the Insight API, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| REQUEST URL | https://apim-aot-azure-dev.azure-api.net/api/smartkpi/assets/\{assetid\}/kpis/\{kpiname\}/insightkpi |
| METHOD | POST |
| CONTENT TYPE | application / json |
| JSON Request | \{ |
|  | \"startdate\":\"2022-07-13T06:30:00Z\", |
|  | \"enddate\":\"2022-07-13T08:30:59Z\", |
|  | \"calendarOption\":\"custom\" |
|  | \} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Smart%20KPIs%20API%20Reference/Azure%20Smart%20KPIs%20API%20Reference/2.2/Azure_Insight_API_Response.txt) |


### Input Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**   **Description**                                                                                                                             **M/O**    **Max Length**   **Type**
  --------------- ------------------------------------------------------------------------------------------------------------------------------------------- ---------- ---------------- ----------
  authorization   Token acquired from Azure AD based on the user credentials for further API calls. E.g., msal.accesstoken : \{ token: \"\\" \}   M-Public   \-               String

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Body

  ----------------------------------------------------------------------------------------------
  **Parameter**    **Description**                         **M/O**   **Max Length**   **Type**
  ---------------- --------------------------------------- --------- ---------------- ----------
  startdate        Start date to perform the calculation   M         255              String

  enddate          End date to perform the calculation     M         255              String

  calendarOption   Available calendar Options (custom)     M         255              String
  ----------------------------------------------------------------------------------------------

### Output Header

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**             **Description**                                                                                                                                                                                                                                                      **M/O**    **Type**
  ------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------- ----------
  Content-Type              Type of the content. It could be application/json, text/html, application/xml, etc. It lets the receiving entity know how to interpret the data.                                                                                                                     M-Public   255

  Content-Length            Length of the content. This is an HTTP header that indicates the size of the body data in bytes. It is used to let the receiving entity know how much data to expect.                                                                                                O-Public   255

  date                      Date of operation execution                                                                                                                                                                                                                                          O-Public   255

  ocp-apim-apiid            This field holds the unique identifier of the API in Azure API Management (APIM). This identifier is used within the APIM instance to distinguish between different APIs.                                                                                            O-Public   255

  ocp-apim-operationid      This field contains the unique identifier for a particular operation within an API in APIM. This helps in tracing the specific operation or method that was invoked.                                                                                                 O-Public   255

  ocp-apim-productid        This field contains the unique identifier of the product with which the API is associated. In APIM, APIs can be grouped into products, and this field helps identify which product the API belongs                                                                   O-Public   255

  ocp-apim-subscriptionid   This field contains the unique identifier of the subscription associated with the APIM instance. In APIM, a subscription relates to the agreement to use an API and provides the primary means for authorization.                                                    O-Public   255

  ocp-apim-trace-location   This field contains the URL where the trace output can be found. This is typically used for debugging purposes. When APIM tracing is enabled, detailed information about the request and response is written to this location, which can help troubleshoot issues.   O-Public   255
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Output Body


| **Parameter** | **Description** | **M/O** | **Type** |
| --- | --- | --- | --- |
| errorManagement | The object identifying the error. Provided only if there is an error. | O | Object |
| errorCode | The numeric identifier of the error | M | String |
| errorDescription | Alphanumeric explanation of the error | M | String |
| Services | List of the created Service\ | O | List |
| Actual | The Actual calculation of the KPI depends on its configuration. For example: If a KPI is configured to be calculated at 12 AM every day, the actual value would depend on the past 24hrs data i.e., 12 AM the previous day to 12 AM the current day. ex:( C-B1-G1-R1-F1:OEE) | M | String |
| Calculation Frequency | Frequency of KPI calculation. Ex:5min,10min,30min,1h,12h | M | String |
| Forecast | Forecast refers to the average of the actual KPI values calculated over the past seven days. These calculated values are stored in its dedicated timeseries ID in Azure. ex:( C-B1-G1-R1-F1:OEE_Forecast) | M | String |
| Historical | Historical refers to the peak performance of a specific KPI recorded on any given day during the preceding 12 months. These calculated values are stored in its dedicated timeseries ID in Azure ex:( C-B1-G1-R1-F1-P-PP-U1:OEE_Historical) | M | String |
| RAGStatus | This visually represents the performance of the KPI. For example, if the actual value of the KPI is being compared with its target value, then it represents how the performance compares. | M | String |
|  | The visualization incorporates a color-coded system based on the RAG (Red, Amber, Green) status configuration designated for the KPI. This means that the actual KPI values will be represented within red, amber, or green zones on the KPI tiles, providing an understanding of performance status. |  |  |
| Target | Target represents the target value of the KPI. This can be a static value or can also be a dynamic target such that the target might be updated every shift or at a specific time interval. ex:(C-B1-G1-R1-F1-P-PP-U1:OEE_target) | M | String |
| assetid | Level in the asset hierarchy against which the KPI must be computed. | M | String |
| isKpi | Returns a Boolean response (True or False) and checks whether the response is for KPI or Parameter. | M | String |
| KPI direction | Returns response (Up or Down) arrow and checks whether it\'s best performing or worst performing. | M | String |
| uid | Unique ID - The system automatically generates a unique identity for each KPI that is created by the user | M | String |


### Result

  ---------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- -----------------------------------------------------------
  200             Service executed successfully

  ---------------------------------------------------------------------------

### Error Management

  --------------------------------------------------------------------------------------
  **HTTP Code**   **Error Code**   **Error Description**
  --------------- ---------------- -----------------------------------------------------
  500             500              Generic Error

  400             401              Unauthorized user or HeaderToken missing or expired

  400             400              Bad request
  --------------------------------------------------------------------------------------
