---
id: aot-operations-hierarchy-api-reference-auriga
title: AOT Operations Hierarchy API Reference Auriga
---

**Accenture Operations Twin**

**Operations Hierarchy**

**API REFERENCE**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin / Operations Hierarchy |
| **Domain / Area** | Digital Twin / Asset Management |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Ranganathan, Balamurugan |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Operations Hierarchy Deployment Guide, Operations Hierarchy UI Guide |

**Contents**

[Introduction [3](#introduction)](#introduction)

[Target Audience [3](#target-audience)](#target-audience)

[Purpose [3](#purpose)](#purpose)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[OH Module APIs [4](#oh-module-apis)](#oh-module-apis)

[GET- GetOperationsHierarchy [5](#get--getoperationshierarchy)](#get--getoperationshierarchy)

[GET- GetParentOperationsHierarchy [6](#get--getparentoperationshierarchy)](#get--getparentoperationshierarchy)

[GET- GetChildOperationsHierarchy [7](#get--getchildoperationshierarchy)](#get--getchildoperationshierarchy)

[POST- CreatePinAsset [8](#post--createpinasset)](#post--createpinasset)

[DELETE- UnpinAsset [9](#delete--unpinasset)](#delete--unpinasset)

[GET- GetPinAsset [10](#get--getpinasset)](#get--getpinasset)

[POST- SearchAssets [11](#post--searchassets)](#post--searchassets)

[POST- GetAssetRagInsightPriority [12](#post--getassetraginsightpriority)](#post--getassetraginsightpriority)

[POST- SearchStringToDB [13](#post--searchstringtodb)](#post--searchstringtodb)

[GET- GetEVStatusDetails [14](#get--getevstatusdetails)](#get--getevstatusdetails)

[GET- GetOHAssetPath [15](#get--getohassetpath)](#get--getohassetpath)

[GET- GetAssetDetails [16](#get--getassetdetails)](#get--getassetdetails)

[POST- SearchAssetsPath [17](#post--searchassetspath)](#post--searchassetspath)

[GET- GetPlantAssets [18](#get--getplantassets)](#get--getplantassets)

[GET- GetAssetTypes [19](#get--getassettypes)](#get--getassettypes)

[GET- GetUnitSystemandTimezoneByUser [20](#get--getunitsystemandtimezonebyuser)](#get--getunitsystemandtimezonebyuser)

[GET- GetAssetTypesByPlant [21](#get--getassettypesbyplant)](#get--getassettypesbyplant)

[GET- GetPlantsByUser [22](#get--getplantsbyuser)](#get--getplantsbyuser)

[POST- ManageAssetRolePermissions [23](#post--manageassetrolepermissions)](#post--manageassetrolepermissions)

[OH Config APIs [24](#oh-config-apis)](#oh-config-apis)

[POST- CreateOrUpdateOrReviveOrDeleteRoleAssetMappings [25](#post--createorupdateorreviveordeleteroleassetmappings)](#post--createorupdateorreviveordeleteroleassetmappings)

[GET- GetAssetsByRole [26](#get--getassetsbyrole)](#get--getassetsbyrole)

[GET- GetRolesByPlant [27](#get--getrolesbyplant)](#get--getrolesbyplant)

[GET- GetPlantsByRoleIds [28](#get--getplantsbyroleids)](#get--getplantsbyroleids)

[GET- GetHighestLevelAssetsbyRoles [29](#get--gethighestlevelassetsbyroles)](#get--gethighestlevelassetsbyroles)

[GET- BatchDetails API [30](#get--batchdetails-api)](#get--batchdetails-api)

[GET - BatchAnalysis API [31](#get---batchanalysis-api)](#get---batchanalysis-api)

[Entity Viewer Config APIs [32](#entity-viewer-config-apis)](#entity-viewer-config-apis)

[POST- AddEntityViewerConfiguration [32](#post--addentityviewerconfiguration)](#post--addentityviewerconfiguration)

[GET- GetEntityViewerConfig [33](#get--getentityviewerconfig)](#get--getentityviewerconfig)

[GET- GetEntityViewerConfigByAssetTypeAndPlantName [34](#get--getentityviewerconfigbyassettypeandplantname)](#get--getentityviewerconfigbyassettypeandplantname)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes. 

Operations Hierarchy is an AOT component that helps the user navigate through the plant's hierarchy and view the 360-degree information associated with each node. A node, also known as an entity, could be a Line, Unit, System, Sub-system, Equipment, or something similar. The Entity Viewer provides a unified view that helps the business user to explore the contextualized data that in turn would help to speed up the problem investigation and analysis.

The Python-based Operations Hierarchy APIs are built and hosted on a cloud-agnostic Kubernetes environment. End users are provided with access to these APIs via API Management (Azure Services) that facilitates the required authentication. These APIs are developed using the Flask microweb framework. It uses an Object Relational Mapper (ORM) approach to communicate with the database. SQL Alchemy is the SQL toolkit that has been used to achieve the ORM approach. All the time zones are in Epoch time (UTC) format.

## Target Audience

This guide is designed for use by developers with the following skills:

- SQL Server Management studio.

- Configure SQL database to Azure server.

- API-related DLL.

- API Management Service.

## Purpose

This reference document describes the APIs used for Operation Hierarchy Configuration and Entity Viewer Configuration along with those that provide middleware functionality.

## Prerequisites

An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64) may be useful.

## Contacts

- ``

- ``

- [`rishabh.b.joshi@accenture.com`](mailto:`rishabh.b.joshi@accenture.com`)

##  Related Links

- [AOT [Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- AOT OH [Documentation](https://industryxdevhub.accenture.com/assetdetails/76)

- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| Term | Definition |
|:---|:---|
| Accenture Operations Twin (AOT) | A suite of software accelerators and tools that integrate product, process, and live data from IT and OT systems, providing a comprehensive view of operations for better decision-making and process optimization. |
| Operations Hierarchy | An AOT component that lets users navigate a plant’s hierarchy and view detailed, contextualized information for each node (entity), such as Line, Unit, System, Sub-system, or Equipment. |
| Entity Viewer | The unified interface within Operations Hierarchy for exploring contextualized data for each node, supporting problem investigation and analysis. |
| API Management (Azure Services) | Service that provides secure access to APIs, handling authentication and authorization for users. |
| Asset / Solution Name | The specific solution or asset managed, here "Accenture Operations Twin / Operations Hierarchy." |
| Digital Twin | A digital representation of physical assets, systems, or processes, used for asset management and operational insights. |
| M/O | Mandatory/Optional |
| Asset | Any entity in the operations hierarchy (Line, Unit, System, Sub-system, Equipment), each with metadata, external IDs, and hierarchical relationships. |
| AssetExternalId | Unique identifier for an asset, used in API requests to fetch or manipulate asset data. |
| ParentAssetId / ParentExternalId | Unique identifier for the parent asset in the hierarchy, establishing relationships between assets. |
| Authorization Token | Security token from Azure Active Directory, required for authenticating API requests. |
| RAG Status | Color-coded status (Red, Amber, Green) indicating the health or priority of an asset, used in dashboards and visualizations. |
| Cursor | Value used for pagination in API responses, allowing users to fetch additional data in subsequent requests. |
| Metadata | Additional data describing an asset, such as type, source, creation time, and other attributes. |
| PlantId / PlantName | Identifiers and names for plant-level assets within the hierarchy. |
| RoleAssetMappings | Mappings between user roles and assets, used for managing permissions and access within the hierarchy. |
| Entity Viewer Configuration | APIs and templates for configuring the Entity Viewer component, specifying how asset data is displayed and organized. |
| ORM (Object Relational Mapper) | Programming technique for interacting with databases by mapping objects to tables, here using SQL Alchemy. |
| Epoch Time (UTC) | Time format representing seconds since January 1, 1970 (UTC), used for timestamps in the system. |

# OH Module APIs

Operations Hierarchy Module APIs help in fetching the Operations Hierarchy information for the End Users to visualize and perform actions on the Operations Hierarchy data such as root assets, child assets, and asset details.

The OH Module APIs are listed below and described in detail in the subsequent sections.

- GET-GetOperationsHierarchy

- GET-GetParentOperationsHierarchy

- GET-GetChildOperationsHierarchy

- POST-CreatePinAsset

- DELETE-UnpinAsset

- GET-GetpinAsset

- POST-SearchAssets

- GET-GetAssetRagInsightPriority

- POST-SearchStringToDB

- GET- GetEVStatusDetails

- GET - GetOHAssetPath

- GET – GetAssetDetails

- POST-SearchAssetsPath

- GET-GetPlantAssets

- GET-GetAssetTypes

- GET- GetUnitSystemandTimezoneByUser

- GET- GetAssetTypesByPlant

- GET- GetPlantsByUser

- POST - ManageAssetRolePermissions

## GET- GetOperationsHierarchy

This API is used to get all the assets that are at a lower level than the given asset ID. This will return a success message or validation message based on the assetId provided.

### API Preconditions

To fetch the response from the APIs, the following entities must exist:

- Authorization token

- Assetid

### Input Header Parameters

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | string |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Assetid | Provide the Asset External ID of an existing asset. If the Asset is present, it will return the assets that are level(s) below. | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter          | Description                                  | Type   |
|--------------------|----------------------------------------------|--------|
| external_id        | The external ID of the asset                 | String |
| name               | Name of asset                                | String |
| description        | Description of the asset’s data              | String |
| parent_external_id | The external ID of the parent asset          | String |
| metadata           | Metadata of asset                            | String |
| source             | Source of asset                              | String |
| created_time       | The time when the asset is created           | String |
| last_updated_time  | The time when the asset is updated last time | String |

###  API Specifications

| Protocol | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/assets/`\{assetId](https://apim-mw-aot-dev.azure-api.net/api/oh-module/assets/%7bassetId) \}` |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/`\{assetId\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/%7bassetId%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

"Assets" : \[

`\{`

"external_id": "",

"name": "",

"description": "",

"parent_external_id": "",

"source": "",

"created_time": "",

"last_updated_time": "",

"metadata": `\{`\}

`\}`

\]

### Result

| HTTP Code | Result Description              |
|-----------|---------------------------------|
| 200       | Operation hierarchy is fetched. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Please enter a valid asset ID
``
``
``
``

## GET- GetParentOperationsHierarchy

This API is used to get all the parent/root assets. This will return a success message or validation message. If the asset only has metadata associated with it, then the API will fetch that asset.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Query Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Cursor | Cursor value generated to point next set of information which needs to fetch on load more request from UI. | O | String |
| Limit | The limit is a number to fetch assets. | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes. | String |

### Output Body Parameters






``

``
Parameter
Description
Type
``
``

``
AssetName
Name of asset
String
``
``
AssetExternalId
The external ID of the asset
String
``
``
AssetChildrenCount
Count of direct children present in the asset
String
``
``
AssetType
This information is fetched from metadata which indicates the Type of asset.
String
``
``
PlantId
The external ID of the Plant asset
String
``
``
nextCursor
`Cursor for paging through results.`
Example: nextCursor =4zj0Vy2fo0NtNMb229mI9r1V3YG5NBL752kQz1cKtwo
String
``
``
``

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | https://apim-mw-aot-dev.azure-api.net/api/oh-module/parentassets |
| PATH AOT (Azure) \<Public Exposure\> | https://apim-aot-azure-dev.azure-api.net/api/oh-module/parentassets |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

\> `\{`
\>
\> "Parent Details": \[
\>
\> `\{`
\>
\> "AssetName": "",
\>
\> "AssetExternalId": "",
\>
\> "AssetChildrenCount": "",
\>
\> "AssetType": "",
\>
\> "PlantId": ""
\>
\> `\}`
\>
\> \],
\>
\> "nextCursor": ""
\>
\> `\}`

### Result

| HTTP Code | Result Description                              |
|-----------|-------------------------------------------------|
| 200       | All parent/root assets fetched using pagination |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Error while fetching Root assets
``
``
``
``

## GET- GetChildOperationsHierarchy

This API is used to get children assets for a particular parent asset. This returns a success message or validation message. If AssetType is not present in the asset metadata, the default value for AssetType is "NA".

### API Preconditions

To fetch the response from the APIs, the authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Query Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Asset_ExternalIds | Provide asset external IDs of assets. | M | String |
| Cursor | Cursor value generated to point next set of information which needs to fetch on load more request from UI. | O | String |
| Limit | The limit is a number to fetch assets. | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters






``

``
Parameter
Description
Type
``
``

``
AssetName
Name of asset
String
``
``
AssetExternalId
The external ID of the asset
String
``
``
AssetChildrenCount
Count of direct children
String
``
``
AssetType
This information is fetched from metadata which indicates the Type of asset.
String
``
``
PlantId
The external ID of the Plant asset
String
``
``
nextCursor
`Cursor for paging through results.`
Example: nextCursor =4zj0Vy2fo0NtNMb229mI9r1V3YG5NBL752kQz1cKtwo
String
``
``
``

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

\> `\{`
\>
\> "Child Details": \[
\>
\> `\{`
\>
\> "AssetName": "",
\>
\> "AssetExternalId": "",
\>
\> "AssetId": "",
\>
\> "AssetChildrenCount": "",
\>
\> "AssetType": "",
\>
\> "PlantId": ""
\>
\> `\}`
\>
\> \],
\>
\> "nextCursor": ""
\>
\> `\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | All child assets for a particular asset get fetched using pagination. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Error while fetching child Assets
``
``
``
``

## POST- CreatePinAsset 

This API is used to pin the given asset in the asset hierarchy using the AssetId and ParentAssetId.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

- AssetExternalId

- ParentExternalId

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| AssetId | Provide assetid of the existing asset hierarchy to pin it. | M | String |
| ParentAssetId | Provide RootAssetId of an asset, which the given assetid needs to follow to be pinned in the asset hierarchy. | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | https://apim-mw-aot-dev.azure-api.net/api/oh-module/assets/pin |
| PATH AOT (Azure) \<Public Exposure\> | https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/pin |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Sample JSON Request and Response





``

``
Request
``\{
" AssetExternalId": "",
" ParentExternalId": ""
`\}`
``
``

``
Response Type 1
`Whenever the asset is pinned successfully, then the following response will be returned.`
`\{"message":"Asset successfully pinned in the asset hierarchy"\}`
``
``
Response Type 2
`Whenever the given AssetExternalId / ParentExternalId already has a preexisting asset, which is pinned, the following response will be returned.`
`\{"message":"Pinned asset already exists with the given AssetExternalId / ParentExternalId "\}`
``
``
Response Type 3
`Whenever the given AssetExternalId / ParentExternalId is not valid or not present, then the following response will be returned.`
`\{"message":"The given AssetExternalId / ParentExternalId is not valid or does not exist"\}`
``
``
``

### Result

| HTTP Code | Result Description                                  |
|-----------|-----------------------------------------------------|
| 200       | "Asset successfully pinned in the asset hierarchy." |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
The given AssetId/ParentAssetId is not valid or does not exist.
``
``
``
``

## DELETE- UnpinAsset

This API is used to unpin the asset from the pinned assets list.

### API Preconditions

To fetch the response from the APIs, the following entities exist.

- Authorization token

- Content-Type

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Path Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| AssetId | Provide AssetId of a pinned asset which needs to be unpinned from the list of pinned assets and to be deleted from the database as well | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/assets/`\{assetid\}`/unpin](https://apim-mw-aot-dev.azure-api.net/api/oh-module/assets/%7bassetid%7d/unpin) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/`\{assetid\}`/unpin](https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/%7bassetid%7d/unpin) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Sample Response





``

``
Response Type 1
`Whenever the given AssetId is valid and exists in the pinned asset list, it will be unpinned and deleted, and the following response will be returned.`
`\{"message":"Asset successfully unpinned in the asset hierarchy"\}`
``
``

``
Response Type 2
`Whenever the given AssetId is not valid and does not exist in the pinned asset list, the following response will be returned.`
`\{"message":"Cannot Delete: This Assetid is not valid or not pinned"\}`
``
``
``

### Result

| HTTP Code | Result Description                                     |
|-----------|--------------------------------------------------------|
| 200       | " Asset successfully unpinned in the asset hierarchy." |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
This Assetid is not valid or not pinned, so you cannot delete it.
``
``
``
``

## GET- GetPinAsset

This API is used to retrieve the assets pinned by the user.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| **BODY** |  |  |
|----|----|----|
| Parameter | Description | Type |
| AssetName | Name of asset | String |
| AssetExternalId | The external ID of the asset | String |
| AssetId | ID of asset | String |
| ParentExternalId | Id of parent asset. | String |
| AssetType | This information is fetched from metadata which indicates the Type of asset. | String |

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/getpinasse t](https://apim-aot-azure-dev.azure-api.net/api/oh-module/assets/getpinasse%20t) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

\> `\{`
\>
\> "Assets": \[
\>
\> `\{`
\>
\> "AssetName": "",
\>
\> "AssetExternalId": "",
\>
\> "AssetId": "",
\>
\> "ParentExternalId": "",
\>
\> "AssetType": ""
\>
\> `\}`
\>
\> \]
\>
\> `\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | AssetId and UserId mapping is present then returns the aforementioned response. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
The pinned asset is not present for this user
``
``
``
``

## POST- SearchAssets

This API is used to search the given assets in the asset hierarchy using the AssetName. It will show the first 10 search results.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Assetname

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description                   | M/O | Type   |
|-----------|-------------------------------|-----|--------|
| AssetName | Provide asset name for search | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| AssetName | Name of asset | String |
| AssetExternalId | The external ID of the asset | String |
| AssetType | This information is fetched from metadata which indicates the Type of asset. | String |
| AssetPath | Path of asset | String |

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/searchassetspath/`\{assetname\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/searchassetspath/%7bassetname%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/searchassetspath/`\{assetname\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/searchassetspath/%7bassetname%7d) |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Sample JSON Request and Response





``

``
Request
Response
``
``

``
``\{
"Filter": [""]
`\}`
``\{
"Assets": [
`\{`
"AssetName": "",
"AssetExternalId": "",
"AssetType": "",
"AssetPath": ""
`\}`
`\}`
``
``
``

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | The result is a list of all searched assets whose names consist of the searched asset name |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Error while searching Assets in Asset Hierarchy
``
``
``
``

## POST- GetAssetRagInsightPriority

GetAssetRagInsightPriority API provides the color of the dot that is displayed on the OH UI. Internally, this API integrates RAG Status API and Insights list API. The color of the dot is assigned as per the conditions mentioned in the table on the side.

For any other scenario or condition, the API returns ‘NA’ for that particular asset.

| Red   | RAG Status is Red or Insight Priority is High     |
|-------|---------------------------------------------------|
| Amber | RAG Status is Amber or Insight Priority is Medium |
| Green | RAG Status is Green or Insight Priority is Low.   |

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Asset_ExternalIds

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter         | Description                           | M/O | Type   |
|-------------------|---------------------------------------|-----|--------|
| Asset_ExternalIds | Provide asset external IDs of assets. | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter        | Description               | Type   |
|------------------|---------------------------|--------|
| Asset_ExternalId | External id of the asset. | String |

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Sample JSON Request and Response





``

``
Request
Response
``
``

``
``\{
" Asset_ExternalIds": ""
`\}`
``\{
"AssetsDotColor":
[
`\{`
"Asset_ExternalId": "Dot Colour"
`\}`
]
`\}`
``
``
``

### Result

| HTTP Code | Result Description                                           |
|-----------|--------------------------------------------------------------|
| 200       | The result is the asset external ID and the color of the dot |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Error while fetching RAG Status and Insight priority of Assets
``
``
``
``

## POST- SearchStringToDB

This API is used to store the searched asset’s ExternalId, AssetName, AssetType, AssetPath in the OH Database.

### API Preconditions

To fetch the response from the APIs, the following entities must exist:

- Authorization token

- AssetExternalId

- AssetName

- AssetType

- AssetPath

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Query Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| AssetExternalId | Provide the Asset External ID of an existing asset. | M | String |
| AssetName | Provide asset name of existing asset | M | String |
| AssetType | Provide asset type of existing asset | O | String |
| AssetPath | Provide asset path of existing asset | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  API Specifications

| Protocol | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | POST |
| CONTENT TYPE | application / json |

###  Sample JSON Response





``

``
Response Type1
`Whenever the details get stored in the database, then the following response will be returned.`
`\{`
"message": "Recent Search saved into Database."
`\}`
``
``

``
Response Type2
`Whenever any issue occurs in storing the search asset details in the database, the following response will be returned.`
`\{`
"message": "Error Message",
"error": "Exception"
`\}`
``
``
``

### Result

| HTTP Code | Result Description                 |
|-----------|------------------------------------|
| 200       | Recent Search saved into Database. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Missing request body
``
``
``
``

## GET- GetEVStatusDetails

This API is used to get all the asset-specific information. This will return asset details from the general and metadata fields or a validation message for the provided asset external ID.

### API Preconditions

To fetch the response from the APIs, the following entities must exist:

- Authorization token

- AssetExternalId

- SubSectionName

- Dimension

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | string |

### Input Query Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| AssetExternalId | Provide the Asset External ID of an existing asset. | M | String |
| SubSectionName | Provide the subsection name of the entity viewer tab | O | String |
| Dimension | It will consist of the parameter list which needs to be fetched. | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| Header | Get the header details according to the specified dimension. | String |
| Details | Details of Asset | String |

###  API Specifications

| Protocol | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/getevstatusdetails?AssetExternalId=`\{AssetExternalId\}`&SubSectionName=`\{SubSectionName\}`&Dimension=`\{Dimension\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/getevstatusdetails?AssetExternalId=%7bAssetExternalId%7d&SubSectionName=%7bSubSectionName%7d&Dimension=%7bDimension%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/getevstatusdetails?AssetExternalId=`\{AssetExternalId\}`&SubSectionName=`\{SubSectionName\}`&Dimension=`\{Dimension\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/getevstatusdetails?AssetExternalId=%7bAssetExternalId%7d&SubSectionName=%7bSubSectionName%7d&Dimension=%7bDimension%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

\> `\{`
\>
\> "header": \[
\>
\> "key1",
\>
\> "key2"
\>
\> \],
\>
\> "details": \[
\>
\> `\{`
\>
\> "key1": "value1",
\>
\> "key2": "value2"
\>
\> `\}`
\>
\> \]
\>
\> `\}`

### Result

| HTTP Code | Result Description |
|-----------|--------------------|
| 200       | Get asset details  |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
Please provide a valid asset
Please pass the required query string parameters
``
``
``
``

## GET- GetOHAssetPath

This API is used to get the Operations Hierarchy asset's name and path.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- AssetExternalId

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| AssetExternalId | Provide the Asset External ID of an existing asset. | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter   | Description        | Type   |
|-------------|--------------------|--------|
| name        | Name of the asset. | String |
| description | Details of Asset.  | String |
| AssetType   | Type of the asset. | String |
| asset_path  | Path of the asset. | String |

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/getohassetpath/`\{asset_external_id\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/getohassetpath/%7basset_external_id%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/getohassetpath/`\{asset_external_id\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/getohassetpath/%7basset_external_id%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample Response

\> `\{`
\>
\> "AssetDetails": `\{`
\>
\> "name": " ",
\>
\> "description": " ",
\>
\> "metadata": `\{`
\>
\> "AssetType": " "
\>
\> `\}`,
\>
\> "asset_path": ""
\>
\> `\}`
\>
\> `\}`

### Result

| HTTP Code | Result Description                  |
|-----------|-------------------------------------|
| 200       | Fetched Asset details successfully. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
The given AssetId / ParenetAssetId is not valid or does not exist.
``
``
``
``

## GET- GetAssetDetails

This API is used to get one or more specific asset details based on the asset external ID.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Assets

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description                                         | M/O | Type   |
|-----------|-----------------------------------------------------|-----|--------|
| Assets    | Provide the Asset External ID of an existing asset. | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Result

| HTTP Code | Result Description                                    |
|-----------|-------------------------------------------------------|
| 200       | If all the external IDs in the assets list are found. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/assetdetails?Assets=`\{Assets\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/assetdetails?Assets=%7bAssets%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/assetdetails?Assets=`\{Assets\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/assetdetails?Assets=%7bAssets%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample Response

\> `\{`
\>
\> "Assets":
\>
\> \[
\>
\> `\{`
\>
\> "AssetExternalId": "",
\>
\> "Name": "",
\>
\> "Metadata": `\{`\},
\>
\> "Source": "",
\>
\> "CreatedTime": "",
\>
\> "LastUpdatedTime": ""
\>
\> `\}`
\>
\> \]
\>
\> `\}`

### Response Types





``

``
1
`If some of the external IDs in the list do not have any assets, then the following response will be returned.`
`\{`
"message": "No assets found for the following external IDs: asset1, asset2. "
`\}`
``
``

``
2
`If all the external IDs are not found, then the following response will be returned.`
`\{`
"message": "No assets found for the provided external IDs."
`\}`
``
``
3
`If the assets list is empty, then the following response will be returned.`
`\{`
'message’:” Assets list is empty. Please provide a list of external IDs to retrieve asset details."
`\}`
``
``
``

## POST- SearchAssetsPath

This API is used to get the path of the searched assets in the asset hierarchy.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- AssetName

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description                                        | M/O | Type   |
|-----------|----------------------------------------------------|-----|--------|
| AssetName | Please provide the asset name of an existing asset | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/searchassetspath/`\{assetname\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/searchassetspath/%7bassetname%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/searchassetspath/`\{assetname\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/searchassetspath/%7bassetname%7d) |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Sample JSON Request and Response





``

``
Request
Response
``
``

``
``\{
"Filter": [""]
`\}`
``
 `\{`
"Assets": [
                                        `\{`
                                            "AssetName": "",
                                            "AssetExternalId": "",
                                            "AssetType": "",
                                            "Assetrootid": "",
                                            "RootAssetName": "",
                                            "Path": ""
                                        `\}`
                                    ]
`\}`
``
``
``
``

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The result is a list of all searched assets along with their paths whose names consist of the searched asset name |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetPlantAssets

This API is used to get the list of all the plant-level assets from the asset hierarchy.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter | Description                   | Type   |
|-----------|-------------------------------|--------|
| PlantId   | The plant’s asset external ID | String |
| PlantName | The plant’s asset name        | String |

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample Response

`\{`

"plantlist": \[

`\{`

"PlantId": "",

"PlantName": ""

`\}`,

`\{`

"PlantId": "",

"PlantName": ""

`\}`

\]

`\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The list of all the plant level assets fetched along with their Plant IDs and Plant Names. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetAssetTypes

This API is used to get the asset types of assets in the asset hierarchy.

### API Preconditions

To fetch the response from the APIs, the ·Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample Response

\> `\{`
\>
\>    "filters": \[
\>
\>                  `\{`
\>
\>                      "assetType": ""
\>
\>                  `\}`,
\>
\>                  `\{`
\>
\>                      "assetType": ""
\>
\>                  `\}`
\>
\>               \]
\>
\> `\}`

### Result

| HTTP Code | Result Description                          |
|-----------|---------------------------------------------|
| 200       | The list of all the asset types is fetched. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetUnitSystemandTimezoneByUser

This API is used to fetch user-specific Unit System and Time Zone.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample Response

`\{`

"Unit System":"",

"TimeZone":""

`\}`

### Result

| HTTP Code | Result Description                               |
|-----------|--------------------------------------------------|
| 200       | The user-specific UoM and Time Zone are fetched. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetAssetTypesByPlant 

This API is used to get all asset types present for a specific plant in the asset hierarchy.

**API Precondition**

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- AssetExternalID

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| **BODY PARAM** |  |  |  |
|----|----|----|----|
| Parameter | Description | M/O | Type |
| AssetExternalID | Please provide the asset external ID of an existing plant asset | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/assettypes/byplant?asset_id=`\{asset_id\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/assettypes/byplant?asset_id=%7basset_id%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/assettypes/byplant?asset_id=`\{asset_id\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/assettypes/byplant?asset_id=%7basset_id%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample Response

`\{`

"AssetTypes": \[\]

 `\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The list of all the asset types is fetched for the given plant asset external ID. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetPlantsByUser

This API is used to get the list of asset details of plants and assets above the plant level based on the User Roles.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Sample Response

\> `\{`
\>
\> "Assets": \[
\>
\> `\{`
\>
\> "external_id": "",
\>
\> "name": "",
\>
\> "description":"",
\>
\> "parent_external_id": "",
\>
\> "source": "",
\>
\> "metadata": `\{`\}
\>
\> `\}`
\>
\> \]
\>
\> `\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The user-specific plant assets and assets above plant level are fetched. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## POST- ManageAssetRolePermissions

This API is used to create, update or delete role permissions for assets.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### API Specifications

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Sample JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/OH%20API%20Reference/POST_ManageAssetRolePermissions_Request.txt) |
| Sample JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/OH%20API%20Reference/POST_ManageAssetRolePermissions_Response.txt) |

###  Result

| HTTP Code | Result Description |
|----|----|
| 200 | The result is the details of the assets and their associated role permissions. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
`Unauthorized User`
`\{Header Token\}` could be missing
``
``
400
400
Bad request
``
``
``

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

###  Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

# 

# OH Config APIs

Operations Hierarchy Configuration APIs help in configuring various components of the Operations Hierarchy for People Management Roles in a multi-plant architecture.

The OH Config APIs are listed below and are described further in the subsequent sections.

- POST-CreateOrUpdateOrReviveOrDeleteRoleAssetMappings

- GET-GetAssetsByRole

- GET- GetRolesByPlant

- GET- GetPlantsByRoleIds

- GET- GetHighestLevelAssetsbyRoles

## POST- CreateOrUpdateOrReviveOrDeleteRoleAssetMappings

This API is used to create, update, revive, or delete Role to Asset mappings in the OH config database.

**API Preconditions**

To fetch the response from the APIs, the Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | Role-to-asset mappings are successfully Created/Updated/Revived/Deleted. |

Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Sample Request Body | [**Link**](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/OH%20API%20Reference/POST_CreateOrUpdateOrReviveOrDeleteRoleAssetMappings_Request_Body.txt) |

### Sample Response





``

``
1
`If any of the RoleID, PlantID & RoleOperation is not provided in the request body, then the following response will be returned.`
`\{`
"message": " "Please provide a valid request body to process the request."
`\}`
``
``

``
2
`If the RoleOperation is invalid, then the following response will be returned.`
`\{`
"message": " Please provide a valid Role Operation to process the request."
`\}`
``
``
3
`If the RoleOperation is ‘Create’, the API will create the role belonging to Plant mapping and the role to asset mappings based on the request body. The following response will be returned.`
`\{`
"details": "",
“message”:” Assets list is empty. Please provide a list of external IDs to retrieve asset details."
`\}`
``
``
4
`If the RoleOperation is ‘Update’, the API will create or remove Role to Asset mappings based on the request body and the following response will be returned.`
`\{`
"details": "",
“message”:” Role to Assets mappings successfully updated."
`\}`
``
``
5
`If the RoleOperation is ‘Revive’, the API will revive the role that belongs to the plant mapping and the role to asset mappings, as well as create or remove the role to asset mappings based on the request body. The following response will be returned.`
`\{`
"details": "",
“message”:” Role to Assets mappings successfully revived."
`\}`
``
``
6
`If the RoleOperation is ‘Delete’, the API will delete the role belonging to the plant mapping and the role to asset mappings. The following response will be returned.`
`\{`
"details": "",
“message”:” Role to Assets mappings successfully deleted."
`\}`
``
``
7
`If any unknown exception occurs in the API, the following response will be returned.`
`\{`
"error": "",
"message": "Error occurred while creating or updating or reviving or deleting Role to Assets mappings in OH config database."
`\}`
``
``
``

## GET- GetAssetsByRole

This API is used to retrieve all assets by role.

### API Preconditions

To fetch the response from the APIs, the · Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Source (optional) | Please specify to fetch specific Role to Asset mappings from the OH config database. | M | String |
| IsDeletedRole (optional) | Please specify as **true** to fetch inactive Role to Asset mappings from the OH config database. | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Result

| HTTP Code | Result Description                                 |
|-----------|----------------------------------------------------|
| 200       | A list of assets is retrieved based on the RoleID. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
The pinned asset is not present for this user
``
``
``
``

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/roles/`\{roleId\}`/Assets](https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/roles/%7broleId%7d/Assets) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/roles/`\{roleId\}`/Assets](https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/roles/%7broleId%7d/Assets) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

`\{`

"Assets": \[

`\{`

"AssetExternalId": "",

"AssetName": "",

"AssetType": "",

"MultiPlantAsset":""

`\}`,

`\{`

"AssetExternalId": "",

"AssetName": "",

"AssetType": "",

"MultiPlantAsset":""

`\}`

\]

## GET- GetRolesByPlant

This API is used to retrieve all the roles based on AssetExternalId of the Plant given in the URL.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| **BODY PARAM** |  |  |  |
|----|----|----|----|
| Parameter | Description | M/O | Type |
| IncludeDeletedRoles (optional) | Please specify as true to fetch both active & inactive Roles based on Plant. | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  API Specifications

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/plant/`\{plant_id\}`/Roles](https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/plant/%7bplant_id%7d/Roles) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plant/`\{plant_id\}`/Roles](https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plant/%7bplant_id%7d/Roles) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

`\{`

"Roles": \[

" ",

" "

\]

`\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | A list of roles is retrieved based on the AssetExternalID of the Plant. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
The pinned asset is not present for this user
``
``
``
``

## GET- GetPlantsByRoleIds

This API is used to retrieve the Plant details based on Role IDs.

### API Preconditions

To fetch the response from the APIs, the Authorization token and the list of Role IDs must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description                         | M/O | Type   |
|-----------|-------------------------------------|-----|--------|
| RoleIds   | Please provide the list of RoleIDs. | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter         | Description                    | Type   |
|-------------------|--------------------------------|--------|
| Plant External ID | External ID of the plant asset | String |
| PlantName         | The plant’s asset name         | String |

### API Specifications

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/plants/byRoleIds?RoleIds=`\{RoleIds\}`](https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/plants/byRoleIds?RoleIds=%7bRoleIds%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plants/byRoleIds?RoleIds=`\{RoleIds\}`](https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plants/byRoleIds?RoleIds=%7bRoleIds%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

**  
**

###  Sample JSON Response

`\{`

"\<RoleID\>": `\{`

"PlantExternalId": "",

"PlantName": ""

`\}`,

"\<RoleID\>": `\{`

"PlantExternalId": "",

"PlantName": ""

`\}`

`\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | A list of Plants with associated Plant IDs and Plant Names is retrieved based on the Role IDs. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetHighestLevelAssetsbyRoles

This API is used to retrieve the highest-level assets for provided list of role ids in the query parameter from OH config database.

### API Preconditions

To fetch the response from the APIs, the Authorization token and the list of Role IDs must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| BODY PARAM |                                     |     |        |
|------------|-------------------------------------|-----|--------|
| Parameter  | Description                         | M/O | Type   |
| RoleIds    | Please provide the list of RoleIDs. | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Output Body Parameters

| Parameter | Description              | Type   |
|-----------|--------------------------|--------|
| Asset ID  | External ID of the asset | String |

###  API Specifications

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/assets/highest-level/byRoleIds?ids=`\{ids\}`](https://apim-mw-aot-dev.azure-api.net/api/operation-heirarchy/assets/highest-level/byRoleIds?ids=%7bids%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/assets/highest-level/byRoleIds?ids=`\{ids\}`](https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/assets/highest-level/byRoleIds?ids=%7bids%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Sample JSON Response

`\{`

"Assets": \[

`\{`

"AssetId": ""

`\}`,

`\{`

"AssetId": ""

`\}`

\]

`\}`

`\}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | A list of assets with associated Asset External IDs is retrieved based on the Role IDs. |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
`Unauthorized User`
`\{Header Token\}` could be missing
``
``
400
400
Bad request
``
``
``

## 

## GET- BatchDetails API

This API is used to get batch details based on the batch number.

### 

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. . e.g., msal, accesstoken : `\{ token: "Bearer \{token\}`" \} | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Result

| HTTP Code | Result Description              |
|-----------|---------------------------------|
| 200       | Operation executed successfully |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
`Unauthorized User`
`\{Header Token\}` could be missing
``
``
400
400
`Bad request`
The pinned asset is not present for this user
``
``
``

###  API Specifications

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/productionmanager/batches/`\{batchid\}`](https://apim-aot-azure-dev.azure-api.net/api/productionmanager/batches/%7bbatchid%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Output Body Parameters

| Parameter           | Description               | Type   |
|---------------------|---------------------------|--------|
| Batch_ID            | Name of the Batch         | String |
| Start_Time          | Start Time of the Batch   | String |
| End_Time            | End Time of the Batch     | String |
| Product             | Name of the Product       | String |
| Process_Area        | Name of the Process Area  | String |
| Product_Order       | Name of the Product Order | String |
| Recipe_ID           | ID of the Recipe          | String |
| Recipe_Name         | Name of the Recipe        | String |
| Consumed_Batch_ID   | ID of consumed batch      | String |
| Batch_Status        | Status of the Batch       | String |
| Order_Status        | Status of the Order       | String |
| Batch_Critical_Time | Critical time of Batch    | String |
| UOM_Material        | Name of the UOM Material  | String |
| Expected_Start_Time | Batch Expected_Start_Time | String |
| Expected_End_Time   | Batch Expected_End_Time   | String |
| Status              | Status of the Batch       | String |

### Sample JSON Response

[Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/OH%20API%20Reference/GET_BatchDetails_Response.txt)

## 

## GET - BatchAnalysis API

Batch Analysis API is a GET operation, but functions as POST due to the limitation of query parameters that can be sent in the header. It expects process area, forward_Ref,Backward_Ref,start date, end date, and attributes list.

### 

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

### API Specifications

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT  |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. . e.g., msal, accesstoken : `\{ token: "Bearer \{token\}`" \} | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Sample Request

`\{`starttime=2025-06-29T10:10:43.911Z,  
endtime=2025-07-29T10:10:43.890Z,  
processid="PROC_003",  
attributes="C-PC-G1-R1-CT1-PM-PMP-DS-L1-WS:raw_material_weighing_station_batch_min",  
forward_ref="PROC_005",  
backward_ref="PROC_001"`\}`

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

###  Output Body Parameters

| Parameter           | Description                      | Type   |
|---------------------|----------------------------------|--------|
| AggregationFunction | Name of the aggregation function | String |
| AttributeName       | Name of the Attribute            | String |
| AttributeId         | Id of the attribute              | String |
| AttributeType       | Type of the attribut             | String |
| EPQAId              | ID of the EPQAId                 | String |
| HistoricalStdDev    | Name of the EPQAId               | String |
| LowerControlLimit   | Value of LowerControlLimit       | String |
| Process             | Name of the Process              | String |
| Product             | Name of the Product              | String |
| UOM                 | Unit of Measure                  | String |
| UpperControlLimit   | Value of Upper Control Limit     | String |

### Sample JSON Response

`\{`  
"BatchAttributeList": \[  
`\{`  
"AggregationFunction": "MINIMUM",  
"AttributeId": "C-PC-G1-R1-CT1-PM-PMP-DS-L1-WS:raw_material_weighing_station_batch_min",  
"AttributeName": "raw_material_weighing_station",  
"AttributeType": "Batch Attribute",  
"Criticality": "No",  
"Data": \[\],  
"EPQAId": 1887,  
"HistoricalStdDev": "228.25",  
"LowerControlLimit": 1.0,  
"Process": "PROCESS 9",  
"Product": "Product DP2",  
"UOM": "-",  
"UpperControlLimit": 10.0  
`\}`,

### Result

| HTTP Code | Result Description              |
|-----------|---------------------------------|
| 200       | Operation executed successfully |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
`Unauthorized User`
`\{Header Token\}` could be missing
``
``
400
400
`Bad request`
The pinned asset is not present for this user
``
``
``

# Entity Viewer Config APIs

Operations Hierarchy Entity Viewer Configuration APIs help in configuring the Entity Viewer component of Operations Hierarchy which is used to show 360-degree information of an asset in the Asset Hierarchy.

The EV Configuration APIs are listed below and are described further in the subsequent sections.

- POST - AddEntityViewerConfiguration

- GET - GetEntityViewerConfig

- GET - GetEntityViewerConfigByAssetTypeAndPlantName

## POST- AddEntityViewerConfiguration

This API is used to add Entity Viewer template data to the OH Config database.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| foldername/filename | Please provide a valid path for the entity viewer template | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### API Specficiations

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)  |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Sample Response

\>  `\{`
\>
\> "example": "Successfully added entity viewer template to OH config database."
\>
\> `\}`

### Result

| HTTP Code | Result Description                                              |
|-----------|-----------------------------------------------------------------|
| 200       | Successfully added entity viewer template to OH config database |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## GET- GetEntityViewerConfig

This API is used to get Entity Viewer config details.

### API Preconditions

To fetch the response from the APIs, the authorization token and PlantName query parameter must exist. AssetType is an optional query parameter.

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/entity-viewer-config/configuration/entityviewer/getconfig?plant_name=`\{plant_name\}`](https://apim-mw-aot-dev.azure-api.net/api/entity-viewer-config/configuration/entityviewer/getconfig?plant_name=%7bplant_name%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/entity-viewer-config/configuration/entityviewer/getconfig?plant_name=`\{plant_name\}`](https://apim-aot-azure-dev.azure-api.net/api/entity-viewer-config/configuration/entityviewer/getconfig?plant_name=%7bplant_name%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter            | Description                           | M/O | Type   |
|----------------------|---------------------------------------|-----|--------|
| PlantName            | Please provide the name of the Plant. | M   | String |
| AssetType (optional) | Please provide the Type of the asset. |     |        |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Sample Response

 `\{`

"EntityViewerConfig": \[

`\{`

"CreatedOn": "",

"CreatedById": "",

"CreatedByUserName": "",

"Version": "",

"AssetType": "",

"PlantId": "",

"UpdatedOn": "",

"UpdatedById": "",

"UpdatedByUserName": ""

"FilePath": ""

`\}`

\]

`\}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | Get entity viewer config details according to the asset type and plant name |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

## 

## GET- GetEntityViewerConfigByAssetTypeAndPlantName

This API is used to get Entity Viewer configuration details based on the Asset Type and Plant Name.

### API Preconditions

To fetch the response from the APIs, the Authorization token, AssetType, and PlantName must already exist.

### API Specifications

| PROTOCOL | HTTPS |
|:---|:---|
| PATH AOT (Cognite) \<Public Exposure\> | [https://apim-mw-aot-dev.azure-api.net/api/oh-module/configuration/entityviewer/getconfig/`\{assettype\}`/`\{plantname\}`](https://apim-mw-aot-dev.azure-api.net/api/oh-module/configuration/entityviewer/getconfig/%7bassettype%7d/%7bplantname%7d) |
| PATH AOT (Azure) \<Public Exposure\> | [https://apim-aot-azure-dev.azure-api.net/api/oh-module/configuration/entityviewer/getconfig/`\{assettype\}`/`\{plantname\}`](https://apim-aot-azure-dev.azure-api.net/api/oh-module/configuration/entityviewer/getconfig/%7bassettype%7d/%7bplantname%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| SAMPLE RESPONSE | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT_GetEntityViewerConfigByAssetTypeAndPlantName_Sample_Response.txt) |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Type of content. E.g.- application/json | M | String |

### Input Path Parameters

| Parameter | Description            | M/O | Type   |
|-----------|------------------------|-----|--------|
| Assettype | Provide the asset type | M   | String |
| Plantname | Provide the plant name | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Type of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |
| Connection | A general header specifying whether the current network connection stays open once the current transaction finishes | String |

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | Get entity viewer config details according to the asset type and plant name |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
500
500
Generic Error
``
``
400
401
``
Unauthorized User
`\{Header Token\}` could be missing
``
``
``
400
400
``
Bad request
``
``
``
``

### Sample Response

[LINK](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/OH%20API%20Reference/GET_GetEntityViewerConfigByAssetTypeAndPlantName_Sample_Response.txt)
