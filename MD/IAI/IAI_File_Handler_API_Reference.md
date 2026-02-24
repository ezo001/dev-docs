---
sidebar_position: 2
title: IAI File Handler API Reference
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">File Handler</p>
<p class="doc-type">API REFERENCE</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / File Handler |
| **Domain / Area** | Digital Twin / API |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Gali, Hanuman |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [[Summary - Overview]](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | IAI Getting Started |

## 


</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools that can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

IAI\'s File Handler component facilitates the uploading and downloading of files using Azure blob storage. It is a standalone component that is utilized by other IAI components such as Operation Hierarchy\'s Entity Viewer and Smart KPIs to upload and download template files. This component also provides download functionality for the latest templates used for KPI configuration and Entity Viewer configuration based on Plant and Asset Type details.

### Purpose

The parameters and examples found in this document should be used by the target audience when developing or customizing applications that require the uploading and downloading of files from the Azure blob account via the middleware APIs.

### Target Audience

Developers with the following skills:

-   Azure blob storage account

-   API-related DLL

-   API Management Service

### Prerequisites

An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64) may be useful.

### Contacts

-   [[rishabh.b.joshi@accenture.com]](mailto:rishabh.b.joshi@accenture.com)

-   [b.h.ranganathan@accenture.com](mailto:b.h.ranganathan@accenture.com)

### Related Links

-   [IAI Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [IAI Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

### Glossary


| &gt; Term | &gt; Definition |
| --- | --- |
| &gt; API | &gt; Application Programming Interface; a set of protocols and tools for building and interacting with software applications. |
| &gt; API Management | &gt; Services that enable the creation, publication, and management of APIs in a secure and scalable manner. |
| &gt; Azure Services | &gt; Cloud computing services provided by Microsoft Azure, used for hosting, storing, and managing data and applications. |
| &gt; Blob Storage | &gt; A cloud storage solution for storing large amounts of unstructured data, such as files and media. |
| &gt; Flask | &gt; A lightweight Python web framework used for building APIs and web applications. |
| &gt; Kubernetes | &gt; An open-source platform for automating deployment, scaling, and management of containerized applications. |
| &gt; Authentication Token | &gt; A digital credential used to verify a user\'s identity and authorize access to APIs or services. |
| &gt; Epoch Time | &gt; The number of seconds that have elapsed since January 1, 1970 (UTC), commonly used in computing for time representation. |


## 

# API Architecture

The Python-based File handler APIs covered in this document are built and hosted on a cloud-agnostic Kubernetes environment. End Users are provided access to these APIs via API Management (Azure Services), which also assists in User Authentication. File handler APIs are developed using Flask, which is a microweb framework. It uses an Azure blob storage account to upload and download files. An authentication token is required to use the APIs. All the time zones are in [Epoch time (UTC](https://www.epochconverter.com/)) format.

## File Handler APIs

The middleware APIs to upload and download files from Azure blob storage are listed in the below table.

### Operations Hierarchy Configuration APIs


| API | Description |
| --- | --- |
| POST-Upload File | This API is used for uploading files into the Azure blob account. |
| POST-Download File | This API is used for downloading files from the storage blob. These APIs are described further in the subsequent sections. |

## 

# POST-Upload File

The POST-Upload File API is used for uploading files into the Azure blob account.

To fetch the response from the APIs, the authorization token must exist.

### Specification


| Protocol | HTTPS |
| --- | --- |
| PATH IAI (Cognite)(Public Exposure) | [[https://apim-mw-aot-dev.azure-api.net/api/filehandler/files/upload]](https://apim-mw-aot-dev.azure-api.net/api/filehandler/files/upload) |
| PATH IAI (Azure)(Public Exposure) | [[https://apim-aot-azure-dev.azure-api.net/api/filehandler/files/upload]](https://apim-aot-azure-dev.azure-api.net/api/filehandler/files/upload) |
| METHOD | POST |
| CONTENT TYPE | application / json |


### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |
| Content-Type | Type of content. E.g.- application/json M String |


### Input Body


| Parameter | Description M/O Type |
| --- | --- |
| Path | Provides the file/folder path to upload the file to the Azure blob storage M String |
| File | Provide the file that needs to be uploaded M File \* Mandatory/Optional |


### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles the request \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Type of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes String |


### Output Body


| Parameter | Description Type |
| --- | --- |
| Path | Display path of the uploaded file String |


### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | The file is uploaded successfully to the blob storage. |


### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 401 Unauthorized User or Header Token missing |
| 400 | 400 Bad request - Please select the proper file extension - Storage account not configured for a given base - Please select the file for uploading |


### Sample JSON Response

\{

\"path\": blob_path,

\"message\": \"File uploaded successfully to blob storage.\"

\}

### 

# 

## POST-Download File

The POST-Download File API is used for downloading files from the storage blob.

To fetch the response from the APIs, the authorization token must exist.

### Specification


| PROTOCOL | HTTPS |
| --- | --- |
| PATH IAI (Cognite)(Public Exposure) |  |
| PATH IAI (Azure)(Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |


### Input Header


| Parameter | Description M/O\* Type |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |
| Content-Type | Type of content. E.g.- application/json M String \* Mandatory/Optional |


### Input Body


| Parameter | Description M/O Type |
| --- | --- |
| Path | Provides the path value for downloading files from the Azure blob storage. e.g., \"Path\":\[\"\{basename\}/folder1/filename\"\] where basename represents the folder name and storage account of the respective module like OHEntityViewer and SmartKPI. M String |


### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles the request \[e.g., Werkzeug/2.1.2 Python/3.9.7\] String |
| Content-Type | Type of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes. String |


### Output Body


| Parameter | Description Type |
| --- | --- |
| Content | Downloading the file into the local system String |


### Result


| HTTP Code | Result Description |
| --- | --- |
| 200 | file downloader (Sample success response) |


### Error Management


| HTTP Code | Error Code Error Description |
| --- | --- |
| 500 | 500 Generic Error |
| 400 | 401 Unauthorized User or Header Token missing |
| 400 | 400 Bad request - Invalid file path. Please reach out to Admin for a resolution - Storage account not configured for the given base: \'\{base_name\}\'. Please reach out to Admin for resolution. |


### Sample JSON Request

\{\
\"DownloadFileName\":\"\",\
\"Path\": \[\"\{basename\}/foldername/filename\",\"\{basename\}/foldername/filename\"\]\
\}
