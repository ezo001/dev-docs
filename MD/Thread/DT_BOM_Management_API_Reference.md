---
sidebar_position: 2
title: DT BOM Management API Reference
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Digital Thread Foundations</p>
<p class="doc-topic">BOM Management</p>
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

The EBOM to MBOM Conversion feature in IX Digital Thread Foundations\' BOM Management application enables users to efficiently transform an Engineering Bill of Materials (EBOM) into a Manufacturing Bill of Materials (MBOM) within a structured workflow. This process ensures that engineering data is accurately translated into a manufacturable format while maintaining traceability and version control.

### Purpose

This document serves as an API reference for the IX Digital Thread BOM Management application.

### Target Audience

Developers, Business Analysts, and Accenture teams deploying the IX Digital Thread BOM Management application.

### Prerequisites

-   The BOM Management application must be deployed and accessible.

-   BOM management API and its dependencies must be deployed.

-   Users must have valid login credentials with role-based permissions.

-   A supported browser (Google Chrome or Microsoft Edge) should be used.

### Contacts

-   [karthik.ramachandra@accenture.com](mailto:karthik.ramachandra@accenture.com)

-   [vamsi.konambhotla@accenture.com](https://encoded-592c9deb-987b-4562-aa3c-9fa3d37d83e9.uri/mailto%3avamsi.konambhotla%40accenture.com%2520)

-   [riju.dhar@accenture.com](mailto:riju.dhar@accenture.com)

-   [aishah.yusra.np@accenture.com](mailto:aishah.yusra.np@accenture.com)

-   [dhana.chevveti@accenture.com](mailto:dhana.chevveti@accenture.com)

-   [sathish.kumar.sanga@accenture.com](mailto:sathish.kumar.sanga@accenture.com)

### Related Links

-   [IX Digital Thread Foundations Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=IX%20Digital%20Thread)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/84)

### Glossary


| **Term** | **Definition** |
| --- | --- |
| BOM (Bill of Materials) | A structured list of components, assemblies, and materials required to build a product. Includes EBOM and MBOM. |
| EBOM (Engineering Bill of Materials) | The BOM created during the product design phase, detailing all parts and assemblies from an engineering perspective. |
| MBOM (Manufacturing Bill of Materials) | The BOM used in manufacturing, specifying how a product is built, including production processes and assembly instructions. |
| API (Application Programming Interface) | Protocols and tools that allow different software applications to communicate and perform operations such as fetching BOM details, managing conversions, and reviewing statuses. |
| MSAL Authentication | Microsoft Authentication Library integration used for secure user login and access control within the BOM Management application. |
| M/O | Mandatory/Optional. This indicates whether a parameter value is mandatory or optional to be specified for a particular API. |

## 

## Technology Stack

#### Tools

-   angular - 17.3.0

-   bootstrap - 5.3.3

-   primeng - 17.18.15

-   ng2-charts - 5.0.4

-   swimlane/ngx-graph - 8.0.2

-   azure/msal-angular - 3.0.9

-   rxjs - 7.8.0

-   sonar-scanner: 3.1.0

-   RxJS - 7.8.0

-   Zone.js - 0.14.3

-   TSLib - 2.3.0

-   azure/msal-angular - 3.0.9

-   azure/msal-browser - 3.6.0

-   File-Saver - 2.0.5

-   ExcelJS - 4.4.0

-   JSZip - 3.10.1

-   html2canvas - 1.4.1

#### Repository

-   Git branch name: dev

-   Git folder path: Git -\&gt; Repos -\&gt; ixassets -\&gt; mbom -\&gt; ix-mbom-ui

-   Git folder links: [ix-mbom-ui - Repos](https://dev.azure.com/IXAssets/IXAssetsProject/_git/ixassets?path=/mbom/ix-mbom-ui)

## Background

To enhance security and compliance, the application integrates MSAL authentication for user login. Upon successful authentication, users are redirected to the dashboard, where they can access converted MBOMs, initiate a new conversion, or manage their profile details.

The application provides a centralized repository displaying all converted MBOMs in a tabular format, allowing users to track the status of each conversion. Each MBOM entry includes an Action button that navigates users to the Review Details Page, where authorized users can take necessary actions based on the MBOM\'s status, such as Approve, Reject, Delete, or Push to Target.

The conversion workflow involves selecting an EBOM, choosing an MBOM template, applying transformation rules, and finalizing the conversion. Once the process is complete, MBOMs appear in the dashboard, where users can review them and take appropriate actions based on their status. This structured approach ensures a seamless and traceable EBOM-to-MBOM transformation while providing users with a clear and efficient review and approval process.

In addition to BOM Conversion, the application offers several functionalities, the major ones being:

-   BOM Comparison, where users can perform comprehensive comparisons between BOM files from different systems or sources (e.g., TC and S4).

-   Rule Management, where admin users can define, view, and manage business rules and configurations within the application.

-   MBOM Template Management, where admin users can create and manage MBOM templates within the system.

-   Data Quality Check, where automated validation processes ensure the BOM data is accurate and compliant with required/configured standard.

All these functionalities are achieved through API integrations, with real-time feedback, form validations, and responsive design to ensure a seamless user experience across devices.

## 

# APIs

The following APIs are used in the system:

-   GET - Get Converted MBOM Details

-   GET - Fetch EBOM Details

-   POST - Create New EBOM Entry

-   PUT - Update EBOM Data

-   DELETE - Remove EBOM Entry

-   POST - Initiate BOM Conversion

-   GET - Retrieve Conversion Status

-   DELETE - Cancel Conversion Process

-   GET - Fetch MBOM Review Details

-   POST - Submit Review Action (Approve/Reject)

-   GET - Retrieve Review Status for MBOM

-   POST - Push MBOM to Target System

-   GET - Check Push Status

-   POST - Submit BOM Comparison Request

-   GET - Get Comparison Results

-   GET - List Business Rules

-   POST - Create or Update Rule

-   DELETE - Delete Rule

-   GET - Fetch MBOM Templates

-   POST - Create New Template

-   PUT - Update Template

-   DELETE - Delete Template

-   POST - Run Data Quality Validation

-   GET - Retrieve Validation Results

-   POST - Upload BOM File

-   GET - List Uploaded Files

-   DELETE - Remove Uploaded File

-   GET - Retrieve Digital Thread Data

-   GET - Application Health Status

### 

## GET- Get Converted MBOM Details

This API retrieves BOM conversion details from Postgres DB using the \`created_by\` request parameter. It returns relevant BOM data, including template details, status, and timestamps, ordered by descending date.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameters | created_by, offset, limits |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 25 Mar 2025 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Successful Operations |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 400 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad Request **Sample JSON Response** \{ \"bomConversionData\": \[\{ \"conversionId\": \"CV357\", \"templateId\": \"T014\", \"templateName\": \"SAP MBOM Template\", \"ruleId\": \"R033\", \"eBOMId\": \"006010-Laptop Battery\", \"revisionId\": \"A\", \"mBOMId\": null, \"status\": \"In-Progress\", \"description\": \"Conversion initiated for BOM ID: 006010\", \"eBOMStoragePath\": null, \"mBOMStoragePath\": null, \"createdDate\": \"2025-03-20T04:35:20.872825\", \"createdBy\": \"Chevveti, Dhana\", \"updatedDate\": \"2025-03-20T04:35:20.872825\", \"updatedBy\": \"Chevveti, Dhana\" \} \] |

### 

## GET- EBOM Search Results

This API enables searching and retrieving BOM data from an external system, selected via the source system input.

Once determined, the API sends other search parameters such as keywords, attributes, offset, and limits to the appropriate external system, which then returns the corresponding BOM details. This ensures accurate and efficient BOM retrieval based on user-defined criteria.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameters | Keywords, offset, limits, source_system, attributes |
| Sample Json Response | [[Link]](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_EBOM_Search_Results_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | Successful Operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |

### 

## GET- EBOM Details

This API retrieves EBOM data, allowing for keyword filtering and pagination to search and fetch detailed information.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | ? |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameters | bom_id, bom_rev_id, offset, limits, source_system, fetch_children |
| Sample Json Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_EBOM_Details_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | &gt; Unauthorized User or Header Token could be missing |
| 400 | 400 | &gt; Bad request |


### 

## GET - MBOM Templates 

This API retrieves MBOM (Manufacturing Bill of Materials) templates from a PostgreSQL database based on user-defined criteria. Users can filter searches by template name, ID, or description using an optional keyword. The API supports pagination with offset and limit parameters to control the number of results. It queries the database for matching templates and returns details in paginated format for efficient retrieval.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/mbom/templates?offset=\{offset\}&amp;limits=\{limits\}) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameters | Offset, limits |
| Sample JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_MBOM_Template_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server manages requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | &gt; Unauthorized User or Header Token could be missing |
| 400 | 400 | &gt; Bad request |


### 

## GET- MBOM Template Details API

This API facilitates the retrieval of detailed information regarding the MBOM (Manufacturing Bill of Materials) from the database. It allows users to query specific details and access content based on the keywords provided


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/mbom/templates?keyword=\{keyword\}&amp;offset=\{offset\}&amp;limits=\{limits\}) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameters | Keyword, offset, limits |
| Sample JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_MBOM_Template_Details_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application. M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |


### 

## GET - Transformation Rules Details

This API enables the retrieval of Business Rules stored in a PostgreSQL database based on user-defined search criteria. The search functionality can be enhanced by utilizing an optional keyword to filter results based on rule ID or rule type. The API supports pagination with offset and limit parameters to control the number of results returned. Upon processing the request, the system queries the database for corresponding business rules and returns the pertinent details in a paginated format, thereby ensuring efficient and focused retrieval of business rules.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | ? |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameter | offset, limits |
| Sample JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_Transformation_Rules_Details_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## POST - CONVERSION API

This API allows users to submit EBOM to MBOM conversion requests between systems. It processes and stores BOM details in the database, forwards the request to the target system (e.g., Teamcenter), manages related rule data, and uploads it to Azure Blob Storage. Each request is tracked with a unique conversion_id for efficient handling.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | ? |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameter | source_system, target_system |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\[

\{

\"srcEbomId\": \"006010\",

\"srcRevId\": \"A\",

\"conversionReqId\": \"CV370\",

\"message\": \"Conversion initiated for the requested BOM ID: 006010\"

\}

\]

### GET - Converted MBOM Review Details 

This API retrieves the EBOM and MBOM file details from blob storage based on the provided conversion ID.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | ? |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameter | conversion_id |
| Sample JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_Converted_MBOM_Review_Details_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## POST - APPROVE API

This API will update the BOM review status as \`approved\`.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameters | conversion_id, source_system, status, type, entity_set_name |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

Status updated successfully for conversion ID: CV320 with status APPROVED

### 

## POST - Reject API

This API will update the BOM review status as \`REJECTED\`


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameter | conversion_id, source_system, status, bom_id, rev_id, type, entity_set_name |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server manages requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |



#### Sample Response

\{

\"statusMessage\": \"Conversation ID CV320 is Rejected\",

\"statusCode\": \"201\"

\}

### 

## POST - DELETE API

This API deletes an existing Converted MBOM using the Conversion ID.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameter | conversion_id, source_system, status, type, entity_set_name |
| Sample JSON Request | Query Parameter: Subscription-key of the application (example, query engine) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response

Conversion ID Deleted successfully from the database: CV369

### 

## POST - Push to Target

This API facilitates the creation of MBOM in the target system.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameter | target_system, entity_set_name, type, conversion_id |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\{

\"statusMessage\": \"Mbom is created in SAP ERP\",

\"statusCode\": \"201\"

### 

## GET - Fetch Folders

This API will fetch the list of comparison input and output folders.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application / json |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\[

\"BomComparison/SAP_BOM\",

\"BomComparison/TC_BOM\",

\]

### 

## POST - Trigger Comparison

This API triggers the comparison operation.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Query Parameter | source_folder, target_folder |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\{

\"jobId\":\"0495ed4d-dbd4-49da-8738-330798d3d29f\"

\}

### 

## GET - Comparison Status API

This API is responsible for monitoring the progress of file comparisons, including memory usage and job status. The job ID, which is obtained from the comparison trigger API, serves as the path parameter. Polling functionality is used to fetch the latest progress at specific intervals.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/files/comparison/status/\ |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Query Parameter | Job Id |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\{

\"currentBomId\": \"1237-448-01\",

\"memoryUsage\": \"16.64%\",

\"processedFiles\": 2,

\"progress\": \"20.00%\",

\"totalFiles\": 10,

\"status\": \"IN_PROGRESS\"

\}

### 

## 

### GET - Consolidated Summary Data API

The Consolidated Summary Data API provides a comprehensive comparison of BOM files, highlighting mismatches and matches across various categories. It offers detailed insights into the occurrence and percentage of different mismatch reasons, ensuring accurate and efficient data analysis.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | text/csv |
| Sample Response | [Comparison_Summary_Data_API.csv](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/Comparison_Summary_Data_API.csv?d=w69033428064344e5a86eabb215251b48&amp;csf=1&amp;web=1&amp;e=na1aOE) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## GET - Consolidated Table Details API

The comparison consolidated table details API provides a detailed analysis of Compared BOM files, highlighting their match and mismatch percentages, counts, and specific reasons for mismatches. It also includes paths to the comparison and summary reports for each BOM file, ensuring comprehensive data tracking and error identification.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | text/csv |
| Query Parameter | offset, limits |
| Sample Response | [Comparison_Consolidated_Table_Details_API.csv](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/Comparison_Consolidated_Table_Details_API.csv?d=w1b2044fb5fdf41d9a1077055a92162a7&amp;csf=1&amp;web=1&amp;e=deQjwj) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |


### 

## GET - Item Level Summary Data API

The API provides a detailed comparison of BOM files, highlighting match and mismatch counts and percentages for various reasons. It also includes the total valid line items and rows in both TC and S4 BOMs, ensuring comprehensive data analysis.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/\/summary](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/%3cbom-id%3e/summary) |
| METHOD | GET |
| CONTENT TYPE | text/csv |
| Query Parameter | bom-id |
| Sample Response | [Item_Level_Comparison_Summary_Details_API.csv](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/Item_Level_Comparison_Summary_Details_API.csv?d=w54b4af88d569441182f72d834f9b4969&amp;csf=1&amp;web=1&amp;e=3UBbpl) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## GET - Item Level Table Details API

The Item Level Comparison Table Details API provides a detailed comparison of individual BOM items, highlighting their match status and reasons for any mismatches. It includes hierarchical item IDs for better traceability and ensures accurate data analysis.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/\/comparison](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/%3cbom-id%3e/comparison) |
| METHOD | GET |
| CONTENT TYPE | text/csv |
| Query Parameter | Bom-id, offset, limits |
| Sample JSON Response | [Item_Level_Comparison_Table_Details_API.csv](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/Item_Level_Comparison_Table_Details_API.csv?d=wa976da7eb26f4f7d975bc2040c4a5c6f&amp;csf=1&amp;web=1&amp;e=awKOEq) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## POST - Upload Rule API

By utilizing the upload rule API, users can submit a JSON file containing rule details. Upon uploading, a new rule will be created.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | multipart/form-data |
| Sample input json file | [rule-template.json](https://ts.accenture.com/sites/GlobalDocTemplates/_layouts/15/download.aspx?UniqueId=bed7cab6eaaa42c382dc7d91c0554ce0&amp;e=AxRFVh) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response 

\{

\"statusCode\": \"200\",

\"statusMessage\": \"Validation passed. Rule \'Upload test SAP classification Rule\' saved successfully.\"\}

### 

## POST - ADD Rule API

By utilizing the add rule API, users can submit a JSON payload containing rule details. Upon updating the rule details from the JSON payload and triggering the API, a new rule will be created.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/rules/create) |
| METHOD | POST |
| CONTENT TYPE | application/json |
| Sample Payload | \[ \{ \"ruleType\": \"Re-structuring\", \"ruleName\": \"SAP RULE\", \"ruleDescription\": \"SAP RULE\", \"ruleVersion\": \"V0.1\", \"active\": true \} \] |



#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |



#### Sample Response 

Rule saved successfully with ID: R232

### 

## GET - Fetch Rules

The Fetch Rules API can be used to retrieve a list of rules with limit and offset parameters. Users can search for specific rule information using the keywords parameter to fetch details for a particular rule ID.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json |
| Query Parameter | offset, limits, keywords(optional) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |



#### Sample JSON Response

\{

\"businessRules\": \[

\{

\"ruleId\": \"R232\",

\"ruleType\": \"SAP Rule \",

\"ruleName\": \"Upload test SAP classification Rule 2027\",

\"subRuleName\": null,

\"ruleDescription\": \"Testing SAP Rule for Packages\",

\"ruleJson\": null,

\"ruleVersion\": \"V0.1\",

\"ruleSequence\": null,

\"createdBy\": null,

\"updatedBy\": null,

\"createdDate\": \"2025-05-27 14:57:58\",

\"updatedDate\": \"2025-05-27 14:57:58\",

\"active\": true

\}

\]

\}

### PUT - Update Rule API

Update Rule API allows users to utilize a JSON payload containing rule details. Users can update the details and trigger the API, resulting in the rule details being updated accordingly.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | PUT |
| CONTENT TYPE | application/json |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Payload

\{

\"ruleType\": \"Re-structuring test update test\",

\"ruleName\": \"test add rule api\",

\"subRuleName\": \" \",

\"ruleVersion\": \"V0.1\",

\"ruleSequence\": 0,

\"active\": true,

\"ruleDescription\": \"test add rule api\",

\"ruleId\": \"R190\"

\}

#### Sample Response

Rule ID R190 updated successfully

### DELETE - Delete Rule API

Delete Rule API allows users to delete the rule by specifying the rule id.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | DELETE |
| CONTENT TYPE | application/json |
| Query Parameter | rule_id |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response

Rule deleted successfully with ID: R232

### POST - Upload MBOM Template API

This API is used to upload a new MBOM template file. The request body typically contains the file data and any associated metadata required for the upload.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Request Body | [mbom_template_input.json](https://ts.accenture.com/sites/GlobalDocTemplates/_layouts/15/download.aspx?UniqueId=c7d7da867030410b9407a28e0531eb28&amp;e=9uH63h) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server manages requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |



#### Sample Response

\{

\"statusCode\": \"200\",

\"statusMessage\": \"Validation passed. Template \'Upload file functionaity testing Template\' saved successfully.\"

\}

### POST - ADD Template API

By utilizing this API, users can submit a JSON payload containing MBOM Template details. Upon updating the MBOM Template details from the JSON payload and triggering the API, a new MBOM Template will be created.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application/json |
| Sample Payload | [ADD_Template_API_Payload.txt](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/ADD_Template_API_Payload.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response

Template saved successfully with ID: T232

### 

## GET - Fetch MBOM-Templates API

This API fetches MBOM (Manufacturing Bill of Materials) templates from a PostgreSQL database based on user-specified filters. Users can optionally search by template name, ID, or description using a keyword. The API supports pagination through offset and limit parameters, enabling efficient retrieval of results in a paginated format. It returns matching template details based on the provided criteria.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/templates?offset=\{offset\}&amp;limits=\{limits\}) |
| METHOD | GET |
| CONTENT TYPE | application/json |
| Query Parameter | offset, limits, keywords(optional) |
| Sample JSON Response | [Link](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_MBOM_Template_Response.txt?CID=4377af3d-700e-42d9-ad16-bbb244dcc849) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## PUT - Update Template API

Update Template API allows users to utilize a JSON payload containing template details. Users can update the details and trigger the API, resulting in the template details being updated accordingly.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | PUT |
| CONTENT TYPE | application/json |
| Sample Payload | [Update_Template_API_Input_Payload.txt](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/Update_Template_API_Input_Payload.txt?csf=1&amp;web=1&amp;e=jRNnNS) **Input Header** |
| Parameter | Description M/O\* Type |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response

Template updated successfully: T103

### 

## DELETE - Delete Template API

Delete Template API allows users to delete the template by specifying the template id.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | DELETE |
| CONTENT TYPE | application/json |
| Query Parameter | template_id |


#### Input Header 


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response

Template deleted successfully with ID: T013

### 

## GET - List of Folder Names for Data Quality Batch Process

This API retrieves the list of available folder names used in the Data Quality Batch Process. It helps in identifying and organizing batch files for processing and validation purposes within the BOM management system.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\[\"BomBatchDataQuality/Input/Prod_BB_Bom_S2\", \"BomBatchDataQuality/Input/Prod_BB_Bom_S3\", \"BomBatchDataQuality/Input/BQ_QA_Sample_V2_test\", \"BomBatchDataQuality/Input/BQ_Test_Sample_50\", \"BomBatchDataQuality/Input/Prod_BB_Bom_S1\", \"BomBatchDataQuality/Input/BQ_Sample_New10\", \"BomBatchDataQuality/Input/All_BB_PROD_4K\", \"BomBatchDataQuality/Input/Batch_DQ_Engine_Demo\", \"BomBatchDataQuality/Input/BQ_Test_Sample_100\", \"BomBatchDataQuality/Input/BQ_Sample_10\", \"BomBatchDataQuality/Input/BQ_QA_Sample_299\", \"BomBatchDataQuality/Input/BQ_Test_Sample_300\", \"BomBatchDataQuality/Input/BB_PROD_4K_Aug15\", \"BomBatchDataQuality/Input/testfolder_forlimitcheck\", \"BomBatchDataQuality/Input/All_BB_PROD_Big_B3\", \"BomBatchDataQuality/Input/BQ_Test_Sample_5500\", \"BomBatchDataQuality/Input/All_BB_PROD_4K_B2\"\]

### 

## POST - Trigger TC BOM Batch Data Quality in a Folder

This API triggers the BOM Batch Data Quality process for a specified folder within the BOM Management system. It initiates automated data quality checks on BOM files to ensure data consistency, accuracy, and standard compliance.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application/json |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\{

\"jobId\": \"f3f81697-7d9e-4606-a0e5-25758a2b8b1e\"

\}

### 

## GET - BOM Batch Data Quality Job Status

This API retrieves the current status of a BOM Batch Data Quality job. It provides details such as job ID, execution status, and completion state, helping users monitor and track the progress of batch validations.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/data/quality/batch-process/\{job-id\}) |
| METHOD | GET |
| CONTENT TYPE | application/json |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\{

\"currentBomId\": \"1283-368-01\",

\"memoryUsage\": \"71.03%\",

\"processedFiles\": \"10\",

\"sourceFolder\": \"BomBatchDataQuality/Input/BQ_Sample_10\",

\"progress\": \"100.00%\",

\"totalFiles\": \"10\",

\"timestamp\": \"1757575973382\",

\"status\": \"COMPLETED\"

\}

### 

## GET - Consolidated BOM Summary Details

This API fetches consolidated BOM summary details related to the Data Quality Batch Process. It returns the summarized data as CSV content in the response body, useful for reporting, analysis, and audit purposes.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/data/quality/batch-process/summary/consolidated/\{date\}/\{job-id\}) |
| METHOD | GET |
| CONTENT TYPE | application/json **Input Header** |
| Parameter | Description M/O\* Type |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional **Output Header** |
| Parameter | Description Type |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\"Consolidated TC BOM BatchQuality Summary Report\"

\"\"

\" \",\"File Count\",\"Percentage\"

\"Number of TC BOM Files Checked\",\"10\"

\"Number of TC BOM Files with Invalid Status\",\"9\",\"90.00%\"

\"Number of TC BOM Files with Warning Status\",\"0\",\"0.00%\"

\"Number of TC BOM Files with Valid Status\",\"1\",\"10.00%\"

\"Number of TC BOM Files in Error Status\",\"0\",\"0.00%\"

\"\"

\"Consolidated Counts for All Files\"

\"\",\"Count\",\"Percentage\"

\"Overall Valid Count\",\"61679\",\"86.64%\"

\"Overall Invalid Count\",\"9478\",\"13.31%\"

\"Overall Warning Count\",\"29\",\"0.04%\"

\"Overall TC BoM Record Count\",\"71186\"

\"\"

\"Reasons\",\"Occurrences\",\"Percentage\"

\"Item Name contains Generic\",\"3\",\"0.03%\"

\"Child Status not allowed for Top Level Parent\",\"7847\",\"82.51%\"

\"Item is Obsolete\",\"1617\",\"17.00%\"

\"ASM Generic is not TC Released\",\"12\",\"0.13%\"

\"No Bom Structure\",\"2\",\"0.02%\"

\"Top Level Parent can be Revised but cannot be Promoted\",\"29\",\"0.30%\"

### GET - Consolidated Data Quality Batch Process Details

This API retrieves detailed records of the Data Quality Batch Process in a consolidated CSV format. It supports pagination for large datasets and can return the data as a ZIP file upon request for easier download and storage.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/data/quality/batch-process/consolidated/\{date\}/\{job-id\}) |
| METHOD | GET |
| CONTENT TYPE | application/json |
| Sample JSON Response | [LINK](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/BOM%20Management%20UI%20API%20Reference/GET_Fetch_Consolidated_Data_Quality_Batch_Process_Details_Sample_Response.txt) |


#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |

### 

## GET - BOM Data Quality Batch Process Summary for Particular BOM ID

This API retrieves summary details of the Data Quality Batch Process for a specific BOM ID. It helps users review validation results, quality metrics, and status related to an individual BOM entry.


| PROTOCOL | &gt; HTTPS |
| --- | --- |
| PATH (Public Exposure) | &gt; [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/data/quality/batch-process/\{bom-id\}/summary/\{date\}/\{job-id\}) |
| METHOD | &gt; GET |
| CONTENT TYPE | &gt; application/json |


**Input Header**


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional **Output Header** |
| Parameter | Description Type |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** | HTTP Code | Error Code | Error Description |  | --- | --- | --- |  | 500 | 500 | Internal Server Error |  | 400 | 401 | Unauthorized User |  |
|  |  |  |  | Header Token could be missing |  | 400 | 400 | Bad request |  |


#### Sample JSON Response

\[\"Summary Report of BOM ID:\", \"1219-948-01\"\],

\[\"Metric\", \"Count\", \"Percentage\"\],

\[\"Valid Count\", \"1137\", \"97.01%\"\],

\[\"Invalid Count\", \"25\", \"2.13%\"\],

\[\"Warning Count\", \"10\", \"0.85%\"\],

\[\"TC File Count\", \"1172\"\],

\[\],

\[\"Reasons\", \"Occurrences\", \"Percentage\"\],

\[\"Child Status not allowed for Immediate Parent\", \"18\", \"29.51%\"\],

\[\"Check Previous Revision Status for Immediate Parent\", \"10\", \"16.39%\"\],

\[\"Child Status not allowed for Top Level Parent\", \"16\", \"26.23%\"\],

\[\"Check Previous Revision Status for Top Level Parent\", \"10\", \"16.39%\"\],

\[\"Item is Obsolete\", \"3\", \"4.92%\"\],

\[\"ASM Generic is not TC Released\", \"4\", \"6.56%\"\]

### 

## GET - BOM Data Quality Batch Process Details by BOM ID

This API retrieves both summary and detailed reports of the Data Quality Batch Process for a specific BOM ID. It supports paginated CSV output or ZIP file download, enabling efficient access to detailed validation results.


| PROTOCOL | &gt; HTTPS |
| --- | --- |
| PATH (Public Exposure) | &gt; [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/bom/\{bom-id\}/data/quality/batch-process/\{date\}/\{job-id\}) |
| METHOD | &gt; GET |
| CONTENT TYPE | &gt; application/json |



#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional **Output Header** |
| Parameter | Description Type |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample JSON Response

\[\"S.No\", \"Root Parent ID\", \"Root Parent Release Status\", \"Immediate Parent ID\", \"Immediate Parent Status\", \"Child ID\", \"Child Release Status\", \"Child Revision\", \"Child Item Type\", \"Is Allowed Status?\", \"Allowed Child Statuses\", \"Remarks\", \"Item Hierarchy\"\],

\[\"1\", \"\", \"\", \"\", \"\", \"1219-948-01\", \"Production\", \"A\", \"ASM MechDesign\", \"Allowed\", \"\", \"\", \"1219-948-01\"\],

\[\"2\", \"1219-948-01\", \"Production\", \"1219-948-01\", \"Production\", \"1045-711-01\", \"Production\", \"E\", \"ASM MechDesign\", \"Allowed\", \"\", \"\", \"1045-711-01\ HTTPS |
| --- | --- |
| PATH (Public Exposure) | &gt; |
| METHOD | &gt; GET |
| CONTENT TYPE | &gt; application/json |



#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional **Output Header** |
| Parameter | Description Type |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response:

\[

\"BomBatchDataQuality/Input/BQ_Test_Sample_50\",

\"BomBatchDataQuality/Input/BB_PROD_4K_Aug15\",

\"BomBatchDataQuality/Input/BQ_Test_Demo_Sample_500\",

\"BomBatchDataQuality/Input/BQ_Sample_New10\",

\"BomBatchDataQuality/Input/BQ_Sample_100\",

\"BomBatchDataQuality/Input/testfolder_forlimitcheck\",

\"BomBatchDataQuality/Input/All_BB_PROD_4K\",

\"BomBatchDataQuality/Input/Batch_DQ_Engine_Demo\"

\]

### POST - Add a New Folder for the Data Quality Batch Process

This API allows users to create a new folder for the Data Quality Batch Process and upload files into it. If the folder already exists, users can add new files to the existing folder for further processing and validation within the BOM management system.


| PROTOCOL | &gt; HTTPS |
| --- | --- |
| PATH (Public Exposure) | &gt; |
| METHOD | &gt; POST |
| CONTENT TYPE | &gt; application/json |



#### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String \*Mandatory / Optional **Output Header** |
| Parameter | Description Type |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response:

\{

\"uploadedFiles\": \[

\"data-quality-format.xlsm\"

\],

\"folder\": \"TestUpload\",

\"status\": \"success\"

\}

### 

## GET - List of Existing Folder Names for BOM Comparison Process

This API provides a list of folder names currently available for use in the BOM Comparison Process. By retrieving these folder names, users can efficiently locate, organize, and manage batch files required for comparison and validation tasks in the BOM management system. This functionality supports streamlined comparison operations and ensures accurate tracking of BOM comparison activities.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json |


#### Input Header


| **Parameter** | **Description** **M/O\*** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response:

\[

\"BomComparison/Input/TC_BOM_EXPORTED\",

\"BomComparison/Input/TC_BOM_GL_LW_10\",

\"BomComparison/Input/TC_BOM_TEST\",

\"BomComparison/Input/S4_BOM_BC_DEMO\",

\"BomComparison/Input/TC_BOM_BC_DEMO\",

\"BomComparison/Input/TC_BOM_GL_T4STSV_10\",

\"BomComparison/Input/S4_BOM_EXPORTED\",

\"BomComparison/Input/TC_BOM_GLS_LW_FULL\",

\"BomComparison/Input/S4_BOM_TEST\",

\]

### 

## POST - Add a New Folder for the BOM Comparison Process

This API allows users to create a new folder for the BOM Comparison Process and upload files into it. If the folder already exists, users can add new files to the existing folder for further comparison within the BOM management system.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application/json |


#### Input Header


| **Parameter** | **Description** **M/O\*** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample response:

\{

\"uploadedFiles\": \[

\"comparison-format.xlsm\"

\],

\"folder\": \"TestUpload1\",

\"status\": \"success\"

\}

### 

## GET - Retrieve List of Projects for BOM Comparison Dashboard

This API retrieves the list of available projects displayed on the Digital Thread Dashboard. It helps users view and select projects for managing, monitoring, and analyzing Digital Thread activities within the BOM management system.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json |


#### Input Header


| **Parameter** | **Description** **M/O\*** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample response:

\[

\{

\"projectId\": 122, \"projectTitle\": \"Space Test Project\", \"description\": \"Space Test Project\",

\"industry\": \"Space &amp; Defense\", \"status\": \"Active\", \"systemIntegration\": \"Teamcenter,Polarion\",

\"createdBy\": \"dhana.chevveti\", \"createdDate\": \"2025-10-29T07:09:00.051312\",

\"updatedDate\": \"2025-10-29T07:10:15.559206\", \"isActive\": true,

\"integrationCombinations\": \[

\{\"combinationId\": 3, \"fromSystem\": \"Teamcenter\", \"toSystem\": \"Polarion\", \"integrationStatus\": \"integrated\"\}

\]

\}

\]

### 

## POST - API to Create a new Project

This API allows users to create a new project within the BOM Management system by providing details such as project title, description, industry, integration systems, and status. Once successfully created, the project becomes available in the dashboard.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** | HTTP Code | Error Code | Error Description |  | --- | --- | --- |  | 500 | 500 | Internal Server Error |  | 400 | 401 | Unauthorized User |  |
|  |  |  |  | Header Token could be missing |  | 400 | 400 | Bad request |  |


#### Sample response:

\{

\"projectId\": 123,

\"projectTitle\": \"Test Space Project\",

\"description\": \"\",

\"industry\": \"Space &amp; Defense\",

\"status\": \"Active\",

\"systemIntegration\": \"Teamcenter,Polarion\",

\"createdBy\": \"sathish.kumar.sanga\",

\"createdDate\": \"2025-10-29T13:28:08.225718747\",

\"updatedDate\": \"2025-10-29T13:28:08.225720347\",

\"isActive\": true,

\"integrationCombinations\": \[\{

\"combinationId\": 3,

\"fromSystem\": \"Teamcenter\",

\"toSystem\": \"Polarion\",

\"integrationStatus\": \"not integrated\"\}\]\}

### 

## PUT - API to Edit an Existing Project

This API allows users to update the details of an existing project in the Digital Thread system. Users can modify fields such as project title, description, industry, integration systems, and status.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/dt/dashboard/projects/\{Project) Id\} |
| METHOD | PUT |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| **HTTP Code** | **Error Code** **Error Description** |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample Response:

\{

\"projectId\": 122,

\"projectTitle\": \"Space Test Project\",

\"description\": \"Space Test Project Desc\",

\"industry\": \"Space &amp; Defense\",

\"status\": \"Active\",

\"systemIntegration\": \"Teamcenter,Polarion\",

\"createdBy\": \"sathish.kumar.sanga\",

\"createdDate\": \"2025-10-29T07:09:00.051312\",

\"updatedDate\": \"2025-10-29T13:25:16.7076476\",

\"isActive\": true

\}

### 

## DELETE - API to Delete an Existing Project

This API allows users to delete an existing project from the Digital Thread system using its unique project ID. It helps maintain a clean and organized project repository by removing inactive or obsolete projects from the dashboard.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/dt/dashboard/project/\{Project) id\} |
| METHOD | DELETE |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |


#### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | successful operation |


#### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Internal Server Error |
| 400 | 401 | Unauthorized User Header Token could be missing |
| 400 | 400 | Bad request |



#### Sample response

\{\"success\":true,\"message\":\"Id has been successfully deleted\",\"projectId\":123\}

### 

## GET - API to Retrieve List of Integrated Systems

This API retrieves the list of all available systems integrated within the Digital Thread platform. It enables users to view and select source and destination systems for project configurations, supporting seamless system-to-system integration management.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json **Input Header** |
| Parameter | Description M/O\* Type |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample response

\[

\{

\"systemId\": 1,

\"systemName\": \"Teamcenter\",

\"version\": \"2356\",

\"integrationType\": \"API\",

\"systemCategoryId\": 1,

\"systemCategoryName\": \"PLM\",

\"description\": \"Product Lifecycle Management systems\"

\}

\]

#### 

## GET - Teamcenter Health Status API

The Teamcenter Health API is designed to monitor and validate the operational status of the Teamcenter system within the Digital Thread ecosystem. It ensures that the integration between Teamcenter and other connected systems (such as Polarion, SAP, or MES) is functioning correctly and data exchanges occur seamlessly.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### *Sample response*

\{

\"TcServerID\": \"tcserver00038@PoolA_nonsso@9856@DT-TC2312VM\",

\"Locale\": \"en_US\",

\"LogFile\": \"tcserver.exe34207cb6.syslog\",

\"Version\": \"23120.0005.0000.2024062000\",

\"UserID\": \"infodba\",

\"SiteLocale\": \"en_US\",

\"DisplayVersion\": \"2312.0005:2024062000\",

\"HostName\": \"dt-tc2312vm\",

\"status\": \"UP\"

\}

### 

## GET - SAP Health Status API

The SAP Health Status API monitors and validates the connectivity, responsiveness, and overall health of the SAP system within the Digital Thread ecosystem. It ensures seamless integration and uninterrupted data exchange between SAP and other connected systems such as Teamcenter, Polarion, and MES.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample response

\{

\"status\": \"UP\",

\"groups\": \[\"liveness\", \"readiness\"\],

\"components\": \{

\"diskSpace\": \{ \"status\": \"UP\", \"details\": \{ \"total\": 133003395072, \"free\": 98851127296, \"threshold\": 10485760, \"path\": \"/deployments/.\", \"exists\": true \} \},

\"livenessState\": \{ \"status\": \"UP\" \},

\"ping\": \{ \"status\": \"UP\" \},

\"readinessState\": \{ \"status\": \"UP\" \},

\"sap\": \{ \"status\": \"UP\", \"details\": \{ \"status\": \"UP\", \"responseTimeMs\": 4762, \"timestamp\": \"2025-10-29T14:30:01.308410420\", \"message\": \"SAP ECC responded with HTTP 200\" \} \},

\"ssl\": \{ \"status\": \"UP\", \"details\": \{ \"validChains\": \[\], \"invalidChains\": \[\] \} \}

\}

### 

## GET - SAP S/4 Hana Health Status API

The SAP S/4 Hana Health Status API monitors and validates the connectivity, responsiveness, and overall health of the SAP S/4 Hana system within the Digital Thread ecosystem. It ensures seamless integration and uninterrupted data exchange between SAP S/4 Hana and other connected systems such as Teamcenter, Polarion, and MES.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/s4hana-api/health) |
| METHOD | GET |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| HTTP Code | Error Code Error Description |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample response:

\{

\"status\": \"DOWN\",

\"groups\": \[\"liveness\", \"readiness\"\],

\"components\": \{

\"diskSpace\": \{ \"status\": \"UP\", \"details\": \{ \"total\": 133003395072, \"free\": 97176326144, \"threshold\": 10485760, \"path\": \"/deployments/.\", \"exists\": true \} \},

\"livenessState\": \{ \"status\": \"UP\" \},

\"ping\": \{ \"status\": \"UP\" \},

\"readinessState\": \{ \"status\": \"UP\" \},

\"sap\": \{ \"status\": \"DOWN\", \"details\": \{ \"sapStatus\": \"DOWN\", \"timestamp\": \"2025-10-30T06:50:22.643181831Z\", \"message\": \"SAP connection failed: 400 Bad Request on GET request for \'https://yoejhh1oo8.execute-api.us-east-1.amazonaws.com/Dq4/sap/opu/odata/sap/zixts_s4mbom_if_srv/bom_headSet\': Bill of Material is Required. See SAP Note 1797736 for error analysis.\" \} \},

\"ssl\": \{ \"status\": \"UP\", \"details\": \{ \"validChains\": \[\], \"invalidChains\": \[\] \} \}

\}

### 

## PATCH - Update Project Integration Status

This API allows users to update the integration status of a specific project within the Digital Thread dashboard. It enables toggling the integration state between \"Integrated\" and \"Not Integrated\", helping maintain accurate synchronization and tracking of system connectivity across the digital ecosystem.


| PROTOCOL | HTTPS |
| --- | --- |
| PATH (Public Exposure) | [link](https://ixts-dev-apim.azure-api.net/bom-management-api/v1/dt/dashboard/project/\{projectid\}/integration-status) |
| METHOD | PATCH |
| CONTENT TYPE | application/json **Input Header** |
| **Parameter** | **Description** **M/O** **Type** |
| Authorization | Token acquired from Azure B2C based on the user credentials for further API calls. M String |
| Content-Type | Length of content. M String |
| Ocp-Apim-Subscription-Key | Subscription-key of the application M String **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime **Result** |
| HTTP Code | Result Description |
| 200 | successful operation **Error Management** |
| **HTTP Code** | **Error Code** **Error Description** |
| 500 | 500 Internal Server Error |
| 400 | 401 Unauthorized User or Header Token could be missing |
| 400 | 400 Bad request |


#### Sample response

\[\
\{\
\"combinationId\": 1,\
\"fromSystem\": \"Teamcenter\",\
\"toSystem\": \"SAP S/4HANA\",\
\"integrationStatus\": \"integrated\"\
\}\
\]
