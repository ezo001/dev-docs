---
sidebar_position: 2
title: IAI Twin Viewer Builder API Reference
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">Twin Viewer and Builder</p>
<p class="doc-type">API REFERENCE</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / Twin Builder and Viewer |
| **Domain / Area** | Digital Twin / Visual monitoring and alerts |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya, Rane, Chetankumar |
| **Status** | Draft / In Progress |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [[Summary - Overview]](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) **Related Assets / Alternatives** |

## 


</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools, including data integration extractors that can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The Twin Builder application is implemented as a Micro-Frontend (MFE) based on React. Twin Builder allows an admin user to create a dynamic floor layout using a Drag and Drop mechanism through a web-based user interface. The 3D visuals created in Twin Builder are viewable in Twin Viewer.

The Twin Viewer application is also implemented as an MFE based on React. Twin Viewer fetches and displays 3D content from the Twin Builder application. The visualization is augmented with information that resides in CDF (Cognite Data Fusion).

### Purpose

This document serves as a reference for the APIs used in IAI\'s Twin Builder and Twin Viewer applications.

### Target Audience

-   Business Analysts

-   Client IT Admins

-   Accenture teams deploying IAI

### Contact

-   [rishabh.b.joshi@accenture.com](mailto:rishabh.b.joshi@accenture.com)

-   [chetankumar.rane@accenture.com](mailto:chetankumar.rane@accenture.com)

### Related Links

-   [IAI Twin Viewer and Builder Resources](https://industryxdevhub.accenture.com/assetdetails/47)

-   [IAI IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [IAI Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

### Glossary


| Term | Definition |
| --- | --- |
| Business Analysts | Professionals who analyze and evaluate business processes, systems, and requirements to help organizations improve efficiency and achieve objectives. |
| Client IT Admins | Information technology administrators on the client side who are responsible for managing, maintaining, and supporting IT infrastructure and applications. |
| IAI Twin Viewer and Builder | Applications used for visualizing and constructing digital twins, which are virtual representations of physical assets or systems. |
| IAI IX Developer Hub | A resource hub for developers working on IAI IX, providing documentation, tools, and support. |
| Twin Viewer and Builder APIs | Application Programming Interfaces that facilitate integration and interaction with the Twin Viewer and Builder applications. |
| Plantlayout (GET) | An API endpoint used to retrieve saved layouts within the 3D Twin Viewer and Builder applications. |
| Plantlayout (POST) | An API endpoint used to create or update layouts within the 3D Twin Viewer and Builder applications. |
| M/O (Mandatory/Optional) | Indicates whether a parameter is mandatory (M) or optional (O). |

## 

# Twin Viewer and Builder APIs

The following are the APIs that are part of the Twin Viewer and Builder applications:


| **API** | **Purpose** |
| --- | --- |
| Plantlayout (GET) | loads the saved layouts in the 3D Twin Viewer and Builder applications. |
| Plantlayout (POST) | save plant layouts created on the Builder app. |
| Plantlayout (DELETE) | used to delete plant layouts created on the Builder app. |
| AssetMapping (GET) | generates a builder toolbar and the assets to be consumed by the Builder app. |
| AssetMapping (POST) | for mapping of 3D Models from EliXR and Cognite Asset Hierarchy ID. |
| AssetMapping Update (PATCH) | update the mapping of 3D Models from EliXR and Cognite Asset Hierarchy ID. |
| AssetMapping (DELETE) | delete the mapped Asset via the Twin Builder application. |
| Asset (GET) | list 3D Models in Viewer and Builder applications. |
| Asset (POST) | create 3D Models in Builder applications. |
| Asset (PATCH) | update the 3D Models in the Builder application. |
| Asset (DELETE) | delete 3D Models in Builder applications. |
| Continuum Engine Login (GET) | list 3D Models in the Viewer and Builder applications. |
| ModelMW (GET) | list 3D Models in Viewer and Builder applications. |
| ModelMW (POST) | create 3D Models in the Builder application. |
| ModelMW (PATCH) | update 3D Models in the Builder application. |
| ModelMW (DELETE) | delete 3D Models in the Builder application |
| GRID (GET) | list the Grid/Plant in Viewer and Builder applications. |
| GRID by ID (GET) | get the details of the specific Grid/Plant in the Viewer and Builder applications. |
| GRID (POST) | create the Grid/Plant in Builder applications. |
| GRID (PATCH) | update the Grid in Builder applications. |
| GRID (DELETE) | delete Grid in the Builder application. |
| POI (GET) | list 3D Models in the Viewer and Builder applications. |
| POI (POST) | create and update POIs in the Builder application. |
| POI Mapping (POST) | create and update the POI Mapping in Builder applications. |
| POI (DELETE) | delete POIs in the Builder applications. |
| svgfiles (GET) | load the saved layouts in the 2D Twin Viewer and Builder applications. |
| svgfiles (POST) | save 2D Models created on the Builder app. |
| svgfiles by ID (GET) | update plant layouts created on the 2D Builder app. |
| svgfiles (DELETE) | delete plant layouts created on the 2D Builder app. |
| linklayout (POST) | link or connect 2D and 3D plant layouts. These APIs are detailed in the subsequent sections. |

### 

## Plantlayout (GET) 

The Plantlayout API is invoked by the Viewer/Builder app to create plant layouts that are consumed by the Viewer/Builder app. It is used to load the saved layouts in the Twin Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/plants) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Plantlayout%20(GET)/Plantlayout_GET_JSON_Response.txt) **Input Header Parameter** |
| Parameter | Description M/O\* Type |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String *\*Mandatory/Optional* |


#### Output Header


| Parameter | Description Type |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body

  ------------------------------------------------------------------------

| Parameter | Description Type |
| --- | --- |
| gridBasedGrids | The array of grid details Array |


#### Error Management

+:--------------+:--------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |



#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result. |

### 

## Plantlayout (POST)

The Plantlayout API is invoked by the Builder app to save plant layouts created on the Builder app.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/plants) |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Plantlayout%20(POST)/Plantlayout_POST_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Plantlayout%20(POST)/Plantlayout_POST_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type** |
| --- | --- |
| name | Name of the Plant M String |
| factoryLocation | Location-based Plant M String |
| plantId | Factory location id M String |
| tileParentData | Grid Details of Plant M Array |
| connections | Connections of Plant O Array |
| dimensions | Dimension of Grid M Object |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| name | Name of the Plant String |
| factoryLocation | Location-based Plant Name String |
| createdAt | Plant Created At Date |
| tileParentData | Grid Details of Plant Array |
| plantId | Plant id of the factory location String |
| linkLayout | 2D linked layout ID String |
| connection | Connections of Plant Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:------------------+:------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Plantlayout (PATCH)

The Plantlayout PATCH API is invoked by the Builder app to update plant layouts created on the Builder app.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/plants/\{id\}) |
| METHOD | PATCH |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Plantlayout%20(PATCH)/Plantlayout_PATCH_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Plantlayout%20(PATCH)/Plantlayout_PATCH_JSON_Response.txt) |


#### Input Header Parameters


| **Parameter ** | **Description ** **M/O** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body Parameters


| **Parameter ** | **Description ** **M/O** **Type** |
| --- | --- |
| name | Name of the Plant M String |
| factoryLocation | Location-based Plant M String |
| plantId | Factory location id M String |
| tileParentData | Grid Details of Plant M Array |
| connections | Connections of Plant O Array |
| dimensions | Dimension of Grid M Object |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| name | Name of the Plant String |
| factoryLocation | Location-based Plant Name String |
| createdAt | Plant Created At Date |
| tileParentData | Grid Details of Plant Array |
| plantId | Plant id of the factory Location String |
| linkLayout | 2D Link layout ID String |
| connections | Connections of Plant Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 401 | CRSM_02.005.000 | Unauthorized |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Plantlayout by ID (GET)

The Plantlayout API is invoked by the Builder app to update plant layouts created on the Builder app.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/plants/\{id\}) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Plantlayout%20by%20ID%20(GET)/Plantlayout_by_ID_GET_JSON_Response.txt) |


#### Input Header Parameter


| **Parameter ** | **Description ** **M/O** **Type** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path Parameter


| **Parameter ** | **Description ** **M/O** **Type** |
| --- | --- |
| id | id of the Plant M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| Parameter | Description Type |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| name | Name of the Plant String |
| factoryLocation | Location based Plant Name String |
| plantId | Plant id of the factory location String |
| createdAt | Plant Created At Date |
| tileParentData | Grid Details of Plant Array |
| connections | Connections of Plant Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 401 | CRSM_02.005.000 | Unauthorized |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Plantlayout (DELETE)

The Plantlayout API is invoked by the Builder app to delete plant layouts created on the Builder app.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/plants/\{id\}) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |


#### Input Header Param


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path Param


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Id of the Plant M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| name | Name of the Plant String |
| factoryLocation | Location of the Plant name String |
| createdAt | Plant Created At Date |
| grid | Grid Details of Plant Array |
| connection | Connections of Plant Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:----------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## AssetMapping (GET) 

The Asset Mapping API generates a builder toolbar and the assets to be consumed by the Builder app.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/mappings) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/AssetMapping%20(GET)/AssetMapping_GET_JSON_Response.txt) |


#### Input Header Parameter


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant collection String |
| name | Name of the asset mapping String |
| type | Type of the mapping String |
| asset_used_in_layout | The mapping used in Layout Boolean |
| tile_size | Tile size of Grid String |
| elixr_model_id | Model ID of the 3D asset String |
| version | Model version Number |
| gltfAsset | GLTF Asset details Object |
| thumbnail | Thumbnail details Object |
| cognite_model_id | Cognite model ID value String |
| component_name | Component name 3D Asset String |
| context_id | Cognite AH data String |
| component_hierarchy | The mapped array of 3D components and Cognite AH data String |
| env | Environment value String |
| mappedLayout | Plant collection array of string id Array |
| createdAt | Created date and time Date |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-----------------+:------------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## AssetMapping (POST)

This Asset Mapping API is used for the mapping of 3D Models from EliXR and Cognite Asset Hierarchy ID. This is used in the Unity app to download and load 3D models and show contextualized data.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/mappings) |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/AssetMapping%20(POST)/AssetMapping_POST_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/AssetMapping%20(POST)/AssetMapping_POST_JSON_Response.txt) |


#### Input Header Parameter


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body Parameters


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| name | Name of the asset Mapping M String |
| type | Type of the mapping M String |
| tile_size | Tile size of Grid M String |
| elixr_model_id | Model ID of the 3D asset M String |
| version | Model version M Number |
| gltfAsset | GLTF Asset details M Object |
| thumbnail | Thumbnail details M Object |
| cognite_model_id | Cognite model ID value O String |
| component_name | Component name 3D Asset M String |
| context_id | Cognite AH data M String |
| component_hierarchy | The mapped array of 3D components and Cognite AH data M Array |
| plantId | PlantId of the plant level data M String |
| env | Environment value O String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| name | Name of the asset Mapping String |
| type | Type of the mapping String |
| asset_used_in_layout | The mapping used in Layout Boolean |
| tile_size | Tile size of Grid String |
| elixr_model_id | Model ID of the 3D asset String |
| version | Model version Number |
| gltfAsset | GLTF Asset details Object |
| thumbnail | Thumbnail details Object |
| cognite_model_id | Cognite model ID value String |
| component_name | Component name 3D Asset String |
| context_id | Cognite AH data String |
| component_hierarchy | The mapped array of 3D components and Cognite AH data String |
| plantId | Plant level ID String |
| env | Environment value String |
| mappedLayout | Plant collection array of string id Array |
| createdAt | Created date and time Date |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 401 | CRSM_02.005.000 | Unauthorized |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## AssetMapping Update (PATCH)

This Asset Mapping API is used to update the mapping of 3D Models from EliXR and Cognite Asset Hierarchy ID.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/mappings/\{id\}) |
| METHOD | PATCH |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [JSON Request](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/AssetMapping%20(PATCH)/AssetMapping_Update_JSON_Request.txt) |
| JSON Response | [JSON Response](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/AssetMapping%20(PATCH)/AssetMapping_Update_JSON_Response.txt) |


#### Input Header Parameter


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path Parameter


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Unique ID of the mapping collection M String |


#### Input Body Parameters


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| name | Name of the asset Mapping M String |
| type | Type of the mapping M String |
| tile_size | Tile size of Grid M String |
| elixr_model_id | Model ID of the 3D asset M String |
| version | Model version M Number |
| gltfAsset | GLTF Asset details M Object |
| thumbnail | Thumbnail details M Object |
| cognite_model_id | Cognite model ID value O String |
| component_name | Component name 3D Asset M String |
| context_id | Cognite AH data M String |
| component_hierarchy | The mapped array of 3D components and Cognite AH data M Array |
| plantId | Plant level ID M String |
| env | Environment value O String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| name | Name of the asset Mapping String |
| type | Type of the mapping String |
| asset_used_in_layout | The mapping used in Layout Boolean |
| tile_size | Tile size of Grid String |
| elixr_model_id | Model ID of the 3D asset String |
| version | Model version Number |
| gltfAsset | GLTF Asset details Object |
| thumbnail | Thumbnail details Object |
| cognite_model_id | Cognite model ID value String |
| component_name | Component name 3D Asset String |
| context_id | Cognite AH data String |
| component_hierarchy | The mapped array of 3D components and Cognite AH data String |
| env | Environment value String |
| plantId | Plant level id String |
| mappedLayout | Plant collection array of string id Array |
| createdAt | Created date and time Date |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:------------------+:-----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |



### AssetMapping (DELETE)

This AssetMapping API is used for deleting the mapped Asset via the Twin Builder application.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/mappings/\{id\}) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/AssetMapping%20(DELETE)/AssetMapping_Delete_JSON_Response.txt) |


#### Input Header Parameter


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path Parameter


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Id of the Mapping M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Output Body** |
| **Parameter ** | **Description ** **Type ** |
| \_id | Unique ID of plant Collection String |
| name | Name of the asset Mapping String |
| type | Type of the mapping String |
| asset_used_in_layout | The mapping used in Layout Boolean |
| tile_size | Tile size of Grid String |
| elixr_model_id | Model ID of the 3D asset String |
| version | Model version Number |
| gltfAsset | GLTF Asset details Object |
| thumbnail | Thumbnail details Object |
| cognite_model_id | Cognite model ID value String |
| component_name | Component name 3D Asset String |
| context_id | Cognite AH data String |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:---------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Asset (GET)

This Asset API is consumed by the Viewer/Builder app. It is used to list 3D Models in Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/assets) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Asset%20(GET)/Asset_Get_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| body | This refers to the array or list of models. It has title, env, gltfAsset, thumbnail, ismapped, and mapped model data. Array |
| sasToken | Name of the asset Mapping String |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-------------------+:----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Asset (POST)

This Asset post API is consumed by the Builder app. It is used to create 3D Models in Builder applications.

#### Specification


| **PROTOCOL** | HTTP |
| --- | --- |
| **PATH (Public Exposure)** | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/assets) |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **Authorization** | Bearer \{Token\} |
| **JSON Request** | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Asset%20(POST)/Asset_POST_JSON_Request.txt) |
| **JSON Response** | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Asset%20(POST)/Asset_POST_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| title | Title of the asset M String |
| icon | Thumbnail object M Object |
| asset | GLTF asset object M Object |
| env | Environment value O String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of assets Collection String |
| model | The array of a model object. It has title, version, thumbnail, gltfAsset, env, isMapped, and mappedModel fields Array |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:----------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Asset (PATCH)

This Asset API is consumed by the Builder app. It is used to update the 3D Models in the Builder application.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/assets/\{id\}) |
| METHOD | PATCH |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Asset%20(PATCH)/Asset_Patch_Json_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Asset%20(PATCH)/Asset_Patch_Json_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Unique ID of the assets collection M String |


#### Input Body


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| title | Title of the asset M String |
| icon | Thumbnail object M Object |
| asset | GLTF asset object M Object |
| env | Environment value O String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of assets Collection String |
| model | The array of a model object. It has title, version, thumbnail, gltfAsset, env, isMapped, and mappedModel fields. Array |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:----------------------+:---------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Asset (DELETE)

This Asset API is consumed by the Builder app. It is used to delete 3D Models in Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/assets/\{id\}) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Asset%20(DELETE)/Asset_Delete_Json_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Id of the Assets Collection M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of assets Collection String |
| model | The array of a model object. It has title, version, thumbnail, gltfAsset, env, isMapped, and mappedModel fields. Array |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-----------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## Continuum Engine Login (GET)

This Continuum Engine Login API is used to list 3D Models in the Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/Continuum%20Engine%20Login%20(GET)/Continuum_Engine_Login_GET_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| data | This refers to the array or list of models. It has a title, assetId, tag, thumbnailUrl, ismapped, and mapped model data. Array |
| count | Count of the Content Number |
| totalAssetsCount | Total Asset count Number |
| lastRead | The last read has assetId and updatedat field for pagination Object |
| sasToken | Sas token for fetching blob from Azure blob storage String |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-------------------+:----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## ModelMW (GET)

This API is used to list 3D Models in Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/modelmw) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/ModelMW%20(GET)/ModelMW_GET_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| data | This refers to the array or list of models. It has a title, assetId, tag, thumbnailUrl, ismapped, and mapped model data. Array |
| count | Count of the Content Number |
| totalAssetsCount | Total Asset count Number |
| lastRead | Last read has assetId and updatedat field for pagination Object |
| sasToken | Sas token for fetching blob from Azure blob storage String |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:---------------------+:----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## ModelMW(POST)

This API is used to create 3D Models in the Builder application.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/modelmw) |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/ModelMW%20(POST)/ModelMW_POST_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/ModelMW%20(POST)/ModelMW_POST_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| title | Title of the asset M String |
| icon | Thumbnail object M Object |
| asset | GLTF asset object M Object |
| tag | Environment value M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Unique ID of assets Collection String |
| title | Title of the asset String |
| tag | Tag of the asset String |
| versions | The array of a model object. It has title, version, thumbnail, gltfAsset, isMapped, isPOIMapped, isPlantMapped fields Array |
| plantId | Plant level id String |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:------------------+:------------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## ModelMW (PATCH)

The ModelMW API is used to update 3D Models in the Builder application.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/modelmw) /\{id\} |
| METHOD | PATCH |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/ModelMW%20(PATCH)/ModelMW_PATCH_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/ModelMW%20(PATCH)/ModelMW_PATCH_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Unique ID of the assets collection M String |


#### Input Body


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| title | Title of the asset M String |
| icon | Thumbnail object M Object |
| asset | GLTF asset object M Object |
| tag | Environment value M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Unique ID of assets Collection String |
| title | Title of the asset String |
| tag | Tag of the asset String |
| plantId | Plant level id String |
| versions | The array of a model object. It has title, version, thumbnail, gltfAsset, isMapped, isPOIMapped, isPlantMapped fields Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-----------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## ModelMW (DELETE)

This API is used to delete 3D Models in Builder. It is only available in the decoupled version of the Builder application.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [link](https://apim-mw-aot-test.azure-api.net/api/3d-cms/modelmw) /\{id\} |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/ModelMW%20(DELETE)/ModelMW_DELETE_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Id of the Assets Collection M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Unique ID of assets Collection String |
| title | Title of the asset String |
| tag | Tag of the asset String |
| plantId | Plant level id String |
| versions | The array of a model object. ( version, thumbnail, gltfAsset, isMapped, isPOIMapped, isPlantMapped fields) Array |


#### Result


| ### HTTP Code | ### Result Description |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |



#### Error Management

+:--------------+:------------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## GRID (GET)

This API is used to list the Grid/Plant in Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20(GET)/GRID_GET_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| data | This refers to the array or list of plants. It has a title and assetId. Array |
| count | Count of the Grid Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:--------------------+:----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## GRID by ID (GET)

This API is used to get the details of the specific Grid/Plant in the Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-dev.azure-api.net/api/3d-cms/grid/\{id\}](https://apim-mw-aot-dev.azure-api.net/api/3d-cms/grid/%7bid%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20by%20ID%20(GET)/GRID_BY_ID_GET_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| data | This refers to the array or list of plants. It has title, assetId Array |
| count | Count of the Grid Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-------------------+:----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## GRID (POST)

This API is used to create the Grid/Plant in Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20(POST)/GRID_POST_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20(POST)/GRID_POST_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| title | Title of the Grid/Plant M String |
| versions | Array of Grid Details M Array |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| versions | Array of Grid Details Array |
| title | Title of the asset String |
| Is_aot | Boolean value for couple and decouple Boolean |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:--------------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## GRID (PATCH)

This API is used to update the Grid in Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-dev.azure-api.net/api/3d-cms/grid/\{ID\}](https://apim-mw-aot-dev.azure-api.net/api/3d-cms/grid/%7bID%7d) |
| METHOD | PATCH |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20(PATCH)/GRID_PATCH_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20(PATCH)/GRID_PATCH_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| title | Title of the Grid/Plant M String |
| versions | Array of Grid Details M Array |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| versions | Array of Grid Details Array |
| title | Title of the asset String |
| Is_aot | Boolean value for couple and decouple Boolean |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| ### HTTP Code | ### Result Description |
| --- | --- |
| ### 200 | ### The request is accepted, and the response contains the result |



#### Error Management

+:--------------+:--------------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## GRID (DELETE)

This API is used to delete Grid in the Builder application.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-dev.azure-api.net/api/3d-cms/grid/\{ID\}](https://apim-mw-aot-dev.azure-api.net/api/3d-cms/grid/%7bID%7d) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/GRID%20(DELETE)/GRID_DELETE_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Id of the Assets Collection M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| title | Title of the Grid String |
| Is_aot | Boolean value for couple and decouple Boolean |
| versions | The array of grid details Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-----------------------+:--------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## POI (GET)

This API is used to list 3D Models in the Viewer and Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/POI%20(GET)/POI_GET_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Query


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| assetId | Id of the asset M String |
| v | The version number of the asset M Object |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Id of the asset String |
| applicationMetadata | This refers to the array of mapped Data Array |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:--------------------+:----------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## POI (POST)

This API is used to create and update POIs in the Builder application.

#### Specification


| **PROTOCOL** | HTTP |
| --- | --- |
| **PATH (Public Exposure)** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **Authorization** | Bearer \{Token\} |
| **JSON Request** | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/POI%20(POST)/POI_POST_JSON_Request.txt) |
| **JSON Response** | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/POI%20(POST)/POI_POST_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| assetId | id of the asset M String |
| metadataType | Metadata type M Object |
| data | Added poi data M Object |
| version | The version of the asset M String |


#### Output Header


| ### Parameter | ### Description | ### Type |
| --- | --- | --- |
| ### Server | ### Contains information about how the server handles requests \[e.g., Express\] | ### String |
| ### Content-Type | ### Length of the content | ### String |
| ### Date | ### Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | ### Datetime |
| ### Content-Length | ### Length of the content | ### Bytes |



#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Unique ID of assets Collection String |
| metadataType | poi String |
| poi | Poi added data Array |
| dataMaps | Poi mapped with cdf id Array |
| version | The version of the asset Number |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:--------------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## POI Mapping (POST)

This API is used to create and update the POI Mapping in Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/POI%20Mapping%20(POST)/POI_Mapping_POST_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/POI%20Mapping%20(POST)/POI_Mapping_POST_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Body


| **Parameter ** | **Description ** **M/O** **Type ** |
| --- | --- |
| assetId | id of the asset M String |
| dataMaps | Map poi with cognite id M Array |
| data | Added poi data M Object |
| version | The version of the asset M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Unique ID of assets Collection String |
| metadataType | poi String |
| poi | Poi added data with id, name, isMapped, parent, position fields Array |
| dataMaps | Poi mapped with cdf id Array |
| version | The version of the asset Number |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:--------------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## POI (DELETE)

This API is used to delete POIs in the Builder applications.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-dev.azure-api.net/api/3d-cms/poi/\{ID\}](https://apim-mw-aot-dev.azure-api.net/api/3d-cms/poi/%7bID%7d) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/POI%20(DELETE)/POI_DELETE_JSON_Response.txt) |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | The ID of the Assets Collection M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| assetId | Unique ID of assets Collection String |
| metadataType | poi String |
| poi | Poi added data Array |
| dataMaps | Poi mapped with cdf id Array |
| version | The version of the asset Number |
| createdAt | Created date and time String |
| updatedAt | Updated date and time Number |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management

+:--------------+:-----------------------+:-------------------------------+
| **HTTP Code** | **Error Code** | **Error Description** |

| 401 | CRSM_02.005.000 | Unauthorized |
| --- | --- | --- |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## svgfiles (GET) 

The svgfiles API is invoked by the Viewer/Builder app to create 2D plant layouts that are consumed by the 2D Viewer/Builder app. It is used to load the saved layouts in the 2D Twin Viewer and Builder applications.

**Specification**


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-test.azure-api.net/api/3d-cms/svgfiles?plantId=\{id\}](https://apim-mw-aot-test.azure-api.net/api/3d-cms/svgfiles?plantId=%7bid%7d) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/svgfiles%20(GET)/svgfiles_GET_JSON_Response.txt) **Input Header** |
| **Parameter** | **Description** **M/O\*** **Type** |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String *\*Mandatory/Optional* **Output Header** |
| **Parameter** | **Description** **Type** |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Output Body** |
| **Parameter** | **Description** **Type** |
| svgData | The array of SVG details Array |
| sasToken | Sas token String **Result** |
| **HTTP Code** | **Result Description** |
| 200 | The request is accepted, and the response contains the result. **Error Management** | **HTTP Code** | **Error Code** | **Error Description** |  | --- | --- | --- |  | 401 | CRSM_02.005.000 | Unauthorized |  | 400 | CRSM_01.005.001 | \{field\} is missing bad request |  |
|  |  |  |  | \{field\} could be: |  |

### 

## svgfiles (POST)

The svgfiles API is invoked by the 2D Builder app to save 2D Models created on the Builder app.

**Specification**


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) |  |
| METHOD | POST |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Request | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/svgfiles%20(POST)/svgfiles_POST_JSON_Request.txt) |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/svgfiles%20(POST)/svgfiles_POST_JSON_Response.txt) **Input Header** |
| **Parameter ** | **Description ** **M/O** **Type** |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String **Input Body** |
| **Parameter ** | **Description ** **M/O** **Type** |
| title | Name of the 2D Model M String |
| svgAsset | Svg asset details M Object |
| thumbnail | Thumbnail Details M Object |
| plantId | Plant id of the factory location M String **Output Header** |
| **Parameter ** | **Description ** **Type ** |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Output Body** |
| **Parameter ** | **Description ** **Type ** |
| \_id | Unique ID of 2D Model String |
| title | Name of the 2D Model String |
| svgAsset | Svg asset details Object |
| createdAt | Svg Created At Date |
| thumbnail | Thumbnail Details Object |
| plantId | Plant id of the factory location String **Result** |
| **HTTP Code** | **Result Description** |
| 200 | The request is accepted, and the response contains the result **Error Management** | **HTTP Code** | **Error Code** | **Error Description** |  | --- | --- | --- |  | 401 | CRSM_02.005.000 | Unauthorized |  | 400 | CRSM_01.005.001 | \{field\} is missing bad request |  |
|  |  |  |  | \{field\} could be: |  |

### 

## svgfiles by ID (GET)

The svgfiles API is invoked by the 2D Builder app to update plant layouts created on the 2D Builder app.

**Specification**


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-test.azure-api.net/api/3d-cms/svgfiles /\{id\}](https://apim-mw-aot-test.azure-api.net/api/3d-cms/svgfiles%20/%7bid%7d%20) |
| METHOD | GET |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |
| JSON Response | [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Twin%20Viewer%20and%20Builder%20API%20Reference/svgfiles%20by%20ID%20(GET)/svgfiles_by_ID_GET_JSON_Response.txt) **Input Header** |
| **Parameter ** | **Description ** **M/O** **Type** |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String **Input Path** |
| **Parameter ** | **Description ** **M/O** **Type** |
| id | id of the Plant M String **Output Header** |
| **Parameter ** | **Description ** **Type ** |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes **Output Body** |
| **Parameter ** | **Description ** **Type ** |
| \_id | Unique ID of plant Collection String |
| title | Name of the Plant String |
| svgAsset | Svg asset details Object |
| plantId | Plant id of the factory location String |
| createdAt | Plant Created At Date |
| thumbnail | Thumbnail details Object |
| linkLayout | Linked to 3D layout Object **Result** |
| **HTTP Code** | **Result Description** |
| 200 | The request is accepted, and the response contains the result **Error Management** | **HTTP Code** | **Error Code** | **Error Description** |  | --- | --- | --- |  | 401 | CRSM_02.005.000 | Unauthorized |  | 400 | CRSM_01.005.001 | \{field\} is missing bad request |  |
|  |  |  |  | \{field\} could be: |  |

### 

## svgfiles (DELETE)

The svgfiles API is invoked by the 2D Builder app to delete plant layouts created on the Builder app.

#### Specification


| PROTOCOL | HTTP |
| --- | --- |
| PATH (Public Exposure) | [https://apim-mw-aot-test.azure-api.net/api/3d-cms/svgfiles/\{id\}](https://apim-mw-aot-test.azure-api.net/api/3d-cms/svgfiles/%7bid%7d) |
| METHOD | DELETE |
| CONTENT TYPE | application / json |
| Authorization | Bearer \{Token\} |


#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| id | Id of the Plant M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] Datetime |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| \_id | Unique ID of plant Collection String |
| title | Name of the Plant String |
| svgAsset | Svg asset details Object |
| createdAt | Plant Created At Date |
| thumbnail | Svg thumbnail details Object |
| linkLayout | Linked to 3D plant layout Object |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 401 | CRSM_02.005.000 | Unauthorized |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |


### 

## linklayout (POST)

The linklayout API is invoked by the 2D Builder app to link or connect 2D and 3D plant layouts.

#### Specification


| **PROTOCOL** | HTTP |
| --- | --- |
| **PATH (Public Exposure)** |  |
| **METHOD** | POST |
| **CONTENT TYPE** | application / json |
| **Authorization** | Bearer \{Token\} |
| **JSON Request** | \{ \"plantId3D\": \"66b08a0dd031eb78923f4056\", \"plantId2D\": \"675151351e3c2b547e7af5b9\" \} |



#### Input Header


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. M String |


#### Input Path


| **Parameter ** | **Description ** **M/O ** **Type ** |
| --- | --- |
| plantId3D | Id of the 3D Plant M String |
| plantId2D | Id of the 2D Plant M String |


#### Output Header


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| Server | Contains information about how the server handles requests \[e.g., Express\] String |
| Content-Type | Length of the content String |
| Content-Length | Length of the content Bytes |


#### Output Body


| **Parameter ** | **Description ** **Type ** |
| --- | --- |
| message | message String |


#### Result


| **HTTP Code** | **Result Description** |
| --- | --- |
| 200 | The request is accepted, and the response contains the result |


#### Error Management


| **HTTP Code** | **Error Code** | **Error Description** |
| --- | --- | --- |
| 401 | CRSM_02.005.000 | Unauthorized |
| 400 | CRSM_01.005.001 | \{field\} is missing bad request \{field\} could be: &gt; Query params &gt; &gt; Layout name &gt; &gt; Tenant-id &gt; &gt; Client-id |

