---
sidebar_position: 2
title: AOT People Management Integration with SmartKPIs Azure Auriga
---

Accenture Operations Twin

People Management with Smart KPIs

INTEGRATION GUIDE (AZURE)

Release Version: 2.5

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / Smart KPIs

  **Domain / Area**                   Performance Metrics

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Susarla, Aditya

  **Status**                          Draft / In Progress

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   Smart KPIs UI Guide, Smart KPIs API Reference
  -----------------------------------------------------------------------------------------------------------------

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Target Audience [3](#target-audience)](#target-audience)

[Related Links [3](#related-links)](#related-links)

[Contacts [3](#contacts)](#contacts)

[Glossary [3](#glossary)](#glossary)

[Permissions [4](#permissions)](#permissions)

[Functional Permissions [4](#functional-permissions)](#functional-permissions)

[Data Permissions [5](#data-permissions)](#data-permissions)

[Main Layers [6](#main-layers)](#main-layers)

[Authentication and Authorization [6](#authentication-and-authorization)](#authentication-and-authorization)

[Authentication Token [7](#authentication-token)](#authentication-token)

[Caching [7](#caching)](#caching)

[Data Permission Microservice [8](#data-permission-microservice)](#data-permission-microservice)

[API Precondition [8](#api-precondition)](#api-precondition)

[People Management Role Retrieval API [8](#people-management-role-retrieval-api)](#people-management-role-retrieval-api)

[People Management Role Detail API [8](#people-management-role-detail-api)](#people-management-role-detail-api)

[Workflow Diagram [9](#workflow-diagram)](#workflow-diagram)

[Workflow Description [10](#workflow-description)](#workflow-description)

[Azure Portal View [11](#azure-portal-view)](#azure-portal-view)

[Smart KPI Integration [14](#smart-kpi-integration)](#smart-kpi-integration)

[Metadata of People Management [14](#_Toc215666513)](#_Toc215666513)

[Tenants of People Management [14](#tenants-of-people-management)](#tenants-of-people-management)

[Roles [14](#roles)](#roles)

[Admin [14](#admin)](#admin)

[Non-Admin [14](#non-admin)](#non-admin)

[Use Cases [15](#use-cases)](#use-cases)

[Use Case 1: GET- KPI dashboard [15](#use-case-1-get--kpi-dashboard)](#use-case-1-get--kpi-dashboard)

[Use Case 2: GET -- List API [15](#use-case-2-get-list-api)](#use-case-2-get-list-api)

[Use Case 3: POST- KPI Drilldown [16](#use-case-3-post--kpi-drilldown)](#use-case-3-post--kpi-drilldown)

[Use Case 4: POST- RAG API [17](#section-13)](#section-13)

[Result [18](#result)](#result)

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Smart KPIs is a micro-frontend application that is mounted on the AOT application and is the landing page of the AOT application. It provides contextualized views of Key Performance Indicators to AOT users in both the boardroom and on the shop floor. The Smart KPIs application is invaluable for tracking performance issues as well as the actions taken to improve performance. On the backend, Smart KPIs are powered by several separate microservices that are described in this document.

AOT\'s People Management (PM) component may be integrated with other AOT components -- including Smart KPIs -- to allow filtering by specific user roles. The role of the PM module is to enable administrators to manage access to data and functionality in the platform.

## Purpose

-   This guide explains how to integrate the people management component with AOT Smart KPIs by adding roles to the metadata for assets and time series.

-   This guide should be used along with the API reference document that includes information about paths, inputs, outputs, and error management for APIs related to AOT Smart KPIs.

## Prerequisites

-   An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64) is needed to manually update Roles in Time series and Assets.

-   An Authentication Token is needed to call the APIs.

## Target Audience

-   Client Delivery Teams planning to deliver AOT with People Management integration.

## Related Links

-   [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)



-   [API Management Documentation](https://docs.microsoft.com/en-us/azure/api-management/)

-   [REST API](https://apim-aot-mw-dev.azure-api.net/api/people-management/roles/%7broleId)

## Contacts

-   

-   

-   

##  Glossary 

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**                          **Definition**
  --------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  AOT (Accenture Operations Twin)   A collection of software accelerators and tools designed to integrate product, process, and live data from various IT and OT systems, providing a comprehensive view of operations for better decision-making.

  Smart KPIs                        A micro-frontend application within AOT that displays contextualized Key Performance Indicators (KPIs) to users, helping track performance issues and improvement actions.

  People Management (PM)            A component of AOT that manages user roles and permissions, enabling administrators to control access to data and functionality.

  Functional Permissions            Permissions that allow access to configuration pages and screens, typically restricted to admin users.

  Data Permissions                  Permissions that control access to business objects (assets, KPIs, insights) based on user roles and responsibilities.

  Active Directory (AD) Groups      Groups in Azure Active Directory used to manage user access and roles within AOT.

  Authentication Token              A security token required to access APIs, typically obtained via Azure AD.

  Role (Admin/Non-Admin)            Defines the level of access and permissions a user has within the system; Admins have broader access, while Non-Admins have restricted access based on hierarchy and sensitivity tags.

  KPI Dashboard                     The main interface displaying KPIs to which the user has owner access, determined by their roles and permissions.

  RAG Status                        A color-coded indicator (Red, Amber, Green) representing the status or priority of an asset or KPI.

  Azure Digital Twin (ADT)          A platform used to model and manage digital representations of physical assets, including KPIs and their relationships.

  Message Broker                    A system component that handles event-driven communication between microservices, especially for updating permissions and roles.

  Microservice                      A small, independent service that performs a specific function within the larger AOT architecture, such as managing roles or permissions.

  M/O                               Mandatory/Optional
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Permissions

As shown in the table below, two different types of permissions are managed.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Permission Type**      **Description**
  ------------------------ -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Functional Permissions   Permission to access configuration pages of various components. Access to configuration screens will be restricted to admin role users.

  Data Permissions         Permission defined to AOT business objects (asset hierarchy, KPIs, Insights, etc.) based on roles and responsibilities. The users have access only to the data their roles are mapped to.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following sections describe the two different permission types in detail.

## Functional Permissions

The direction of the flow of the functional permissions for People Management is shown below.

![functional permissions for PM with AOT components](media/image2.png)\{width="8.947916666666666in" height="4.986627296587926in"\}

Note that Functional permissions should be per user. There will be a one-time Backend configuration where specific users are added to each of the component config modules and they in turn will manage permissions for other users.

## 

## Data Permissions

Data permissions are managed using custom metadata entries on each ADT asset (e.g., Asset, Timeseries, Events, etc.) inside the Knowledge Graph. All the Roles that have owner or viewer access to that object will have access rights represented on the metadata of the object. Managing these metadata entries on the objects is the responsibility of the module the data belongs to. An example is: KPIs that are represented as Timeseries in the Knowledge Graph will be managed by the SmartKPIs module.

The access rights of an object might be influenced by the access rights of objects from another module (e.g., Insights linked to KPIs will influence the access rights of the KPI objects). AOT\'s event-driven change feed architecture allows each AOT module to publish its changes related to data permissions (e.g., owner changed, etc.) of objects. Any dependent module can subscribe to these changes and update the data permissions of its objects accordingly. The change feed consists of:

-   The Event Broker, which stores published events and notifies the subscribers of any new events.

-   The Event Publisher microservices, which publish module-related configuration or object create/update events to the Message Broker.

-   The Event Subscriber microservices, which process the events from the feed and update the objects with the necessary data permissions.

The diagram on the right illustrates the integration of AOT components and data permission.

![data permissions for PM with AOT components](media/image3.png)\{width="8.982331583552057in" height="4.908293963254593in"\}

## 

# Main Layers


| **Layer** | **Definition** |
| --- | --- |
| People Management Configuration UI | > An interface that is provided to admin users where AOT Roles can be created and managed, different Active directory groups can be linked to AOT Roles, user permissions can be changed, etc. |
| People Management APIs and Backend services | > These services enable querying and updating User and Role information, mapping the Roles to Active Directory Groups, checking user authorizations, etc. All AOT backend services will use People Management services/APIs to determine the exact data access the AOT user has and limit the returned datasets only to the data accessible by the user based on their role. |


## 

# Authentication and Authorization

Azure Active Directory is used for user Authentication.

> ![Diagram showing authentication and authorization process ](media/image4.png)\{width="8.953937007874016in" height="0.9900984251968504in"\}

For user Authorization, each AOT micro-frontend will need to determine the user\'s access privileges to the functionality and data based on the user\'s AOT roles. There are two ways a user can be linked to AOT roles to gain access to AOT applications and data:

-   The user is a member of at least one AD Group, which is assigned to at least one AOT role.

-   The user is directly assigned to a Role in AOT.

## 

## Authentication Token

To fetch the People Management APIs, an authentication token must already exist.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PROTOCOL                 HTTPS
  ------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------
  PATH (Public Exposure0   [https://apim-mw-aot-dev.azure-api.net/api/people-management/users/bytoken](https://apim-aot-mw-dev.azure-api.net/api/people-management/users/bytoken)

  METHOD                   GET

  CONTENT TYPE             application / json
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Caching

To enable fast authorization of the user to AOT, each microservice must locally cache mappings between both users and roles as well as between AD groups and roles.

An AOT User will have AOT Roles mapped to them in two different ways:

-   Direct User - Role mapping

-   Indirect mapping through AD Groups

A user can be a member of multiple AD Groups which are mapped to multiple AOT Roles. The cache should be implemented as a reusable component (library) in the programming language (Python) used by the microservices. The cache will store the cached data as two lists of key/value pairs in memory -- one list where the key is the UserID and a second list where the key is the AD Group ID. In both lists, the values are represented as a list of AOT Roles mapped to the key.\
![Diagram depicting the cache mappings](media/image5.png)\{width="7.989583333333333in" height="3.5390102799650043in"\}

**Initialization**

-   When the cache is initialized inside the microservice, the base URL of the People Management API and the connection information of the Message Broker should be provided by the microservice.

-   The cache will automatically connect to the People Management API and load all the mappings between AD Groups and AOT Roles.

**\
Updating Cache**

-   The cache module itself will be responsible for keeping the data up to date.

-   If the data for a user is not present in the cache, then it will be loaded the first time it is required using the People Management API.

-   The People Management microservice will push change events whenever a role is updated to the Message Broker. The cache will subscribe to these events and will update the cached data accordingly.

**\
Cache Interface**

The Cache will provide three interface methods:

-   An Initialization method / constructor will be used to pass both the URL of the People Management API and the connection information of the Message Broker.

-   A Get method will return the user\'s AOT Roles based on UserID and AD Groups for which the user is a member.

-   A Get method will return the user\'s AOT Roles based on the AD token the user possesses.

# 

# Data Permission Microservice

-   The purpose of the Data Permission Microservice is to align the roles of AOT users with the roles defined in the configuration template. The roles are updated in the Azure Digital Twin KPI instance metadata.

-   After the roles are assigned, they will reflect on the KPI\'s Timeseries and its respective Contributor or Influencer KPI Timeseries as well.

-   The role assigned to users can be either Viewer or Owner.

## API Precondition

Two People Management APIs are used in the Data Permission Microservice: People Management Role Retrieval API and People Management Role Detail API. They are described in the subsequent sections.

### 

### People Management Role Retrieval API

This API fetches the RoleIDs for the plant. For example, if the assetId is C-B1-G1-R1-F1 then the API fetches all RoleIDs that are associated with this plant. To fetch the RoleID, the Authorization token for access valid user must exist.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **PROTOCOL**                 HTTP
  ---------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **PATH (Public Exposure)**   [https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plant/assetId/Roles](https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plant/%7bassetId%7d/Roles)

  **METHOD**                   GET

  **CONTENT TYPE**             application / json

  **Request URL**              [https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plant/assetId/Roles](https://apim-aot-azure-dev.azure-api.net/api/operation-heirarchy/plant/%7bassetId%7d/Roles)

  **JSON Response**            [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/PM%20Integration%20with%20SmartKPIs/2.0/PM_Role_Retrieval_JSON_Response.txt)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Input Header Parameters

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Parameter***   ***Description***                                                                                                                            ***M/O***   ***Max Length***  ***Type***
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------- ----------- ------------------ ------------
  Authorization     Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \}    M-Public           \-         String

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Input Path Parameters

  -------------------------------------------------------------------------------------------------------------------------------------------
  ***Parameter***   ***Description***                                                             ***M/O***   ***Max Length***   ***Type***
  ----------------- ----------------------------------------------------------------------------- ----------- ------------------ ------------
  assetid           External id of the KPI the asset is linked to \[e.g., path value\\]   M           255                String

  -------------------------------------------------------------------------------------------------------------------------------------------

###  People Management Role Detail API 

This API fetches details for selected RoleIDs. The details fetched are RoleName, users who have access, department, etc. To fetch the details, the authorization token must exist.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **PROTOCOL**                 HTTP
  ---------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **PATH (Public Exposure)**   

  **METHOD**                   POST

  **CONTENT TYPE**             application / json

  **Request URL**              

  **JSON Response**            [Link](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/PM%20Integration%20with%20SmartKPIs/2.0/PM_Role_Detail_JSON_Response.txt)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Input Header Parameters

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ***Parameter***   ***Description***                                                                                                                           ***M/O***   ***Max Length***   ***Type***
  ----------------- ------------------------------------------------------------------------------------------------------------------------------------------- ----------- ------------------ ------------
  Authorization     Token acquired from Azure AD based on the user credentials for further API calls. e.g., msal.accesstoken : \{ token: \"\\" \}   M-Public    \-                 String

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Workflow Diagram

The following diagram illustrates the workflow of the Data Permission Microservice.

![data permission workflow diagram](media/image6.png)\{width="12.802297681539807in" height="5.4610476815398075in"\}

## 

## 

## Workflow Description 

The following points explain the working flow of the Data Permission Microservice:

1.  The message passes through the message broker and depending on the message received, either of these two functions is called:

    -   smart_kpi_function_instance

    -   smart_kpi_configuration_service

2.  Depending on the scope of the final messages (event) received, the payload is generated by smartKPIinstance() and dataPermissionChange().

    -   smartKPIinstance(): This adds a role. The owner is provided access to newly added KPIs and for existing contributors/influencers, viewer access is provided.

    -   dataPermissionChange(): This updates the role as per the config template. It updates the new owner role for the specified KPI and provides viewer access to contributors/influencers.

3.  Role-related information is retrieved from the People Management Role Retrieval API. The information is filtered, and the role ID, name, and key-value pair are extracted.

4.  The final payload is generated by checking the current role and its contributor/influencer information. For more information refer to the next section, \'Conditions to View KPIs\'.

5.  For AOT\'s Azure version, the generated payload is passed through the Azure-based Data Permission API, which uses an ADT query to update the roles in the ADT KPI metadata instance.

> Two data sources are used for this action: MSSQL and Azure Digital Twin (ADT). MSSQL\'s KpiMaster table is used to retrieve uploaded template data. ADT is used to retrieve relationship details on the KPI instance and to update roles in metadata role mapping. Note that the influencing and contributing KPIs get updated with the required roles without actually updating the role. The Data Permission service adds existing/removes unneeded roles when updating the influencing and contributing KPIs.

For role addition/removal, a single list of owner/viewer role details of the given KPI is created, followed by the KPI\'s contributor and influencer.

Examples of Owner and Viewer accesses provided by the People Management APIs are as follows:


| Access | Example |
| --- | --- |
| Owner Access | RoleID_3BF3AFE6-8DE4-403A-932F-D84C24D4BCE9_R True |
|  | RoleID_3BF3AFE6-8DE4-403A-932F-D84C24D4BCE9_W True |
| Viewer Access | RoleID_3BF3AFE6-8DE4-403A-932F-D84C24D4BCE9_R True |
|  | RoleID_3BF3AFE6-8DE4-403A-932F-D84C24D4BCE9_R True |
|  | RoleID_3BF3AFE6-8DE4-403A-932F-D84C24D4BCE9_W False |


After role permissions are assigned, users can view the dashboard or drill down based on their role and permission.\
**Conditions to View KPIs**

The conditions to view the KPIs as per roles and permissions are:

-   The user should be able to drill down the entire KPI hierarchy of the parent KPI if the sensitivity requirements are met.

-   If a user has owner access to a KPI, then the user should have viewer access to its contributing and influencing KPIs as well as viewer access to further drill down in the KPI hierarchy.

-   If the owner role of a parent KPI gets updated, the old role (previous owner role) should still be able to view the contributing/influencing KPIs if the old role has owner/viewer access to other KPIs for which the contributing and influencing KPIs of the parent KPI are also contributing/influencing for other KPIs or if those APIs come up during the drill down of other KPIs.

-   If a role provides the owner access to a KPI for which the role already had viewer access, the user should be able to view the new KPI in the main dashboard as well as in the KPI drill down as a contributing/influencing KPI.

## 

## Azure Portal View

The user can view the uploaded template information in MSSQL\'s KpiMaster table.

> ![MSSQL KpiMaster table in Azure Portal](media/image7.png)\{width="13.68125in" height="5.819444444444445in"\}

Using the Data Permission Microservice, roles are added to the metadata of the given KPI under RoleMapping. The role information is provided in the Key value pair.

![A screenshot of Azure Digital Twins Explorer showing the role mapping info ](media/image8.png)\{width="11.283120078740158in" height="5.224329615048119in"\}

**Summary**

-   As per the role assigned to users, they can view the relevant KPIs on the UI.

-   The People Management APIs are used to update Timeseries for adding/updating roles.

> ![AOT UI showing the relevant KPIs](media/image9.png)\{width="11.166666666666666in" height="5.461748687664042in"\}

# Smart KPI Integration

This section summarizes how the People Management component is integrated with the Smart KPIs component using APIs.

![Diagram showing a sample integration, that is, how the people management component is integrated with the Smart KPIs component using APIs ](media/image10.png)\{width="5.354843613298338in" height="3.2395833333333335in"\}\
[]\{#_Toc215666513 .anchor\}**Metadata of People Management**

-   Custom tags

-   Owner

-   Viewer

##  Tenants of People Management

-   Users

-   Roles (Groups)

-   Asset Hierarchy

-   KPI Hierarchy

    -   Contributing

    -   Influencing

-   Intelligent Advisor

-   Data sensitivity

## Roles

### Admin

#### Smart KPIs (PM)

-   Admin to assign level (s) in AH, the role belongs to

-   Admin should have the flexibility to define if the role has access to sensitive data (KPI)

-   PM engine should auto-assign Owner and viewer access based on KPI hierarchy (Contributing and Influencing KPIs)

#### Smart KPIs

-   The KPI sensitivity tag should come from the Smart KPI configuration:

    -   Soft warning to viewers on not being able to see certain KPIs due to limited access -- contact Admin for access

    -   \$\$Validation -- flag to users

### [ ]\{.underline\}Non-Admin

#### Smart KPIs

-   Users will have access to all the underlying levels in the AH to which they belong.

-   Users cannot see Information beyond the AH levels to which they belong.

-   Users will see the KPIs for which they are an owner on the landing screen of Smart KPI.

-   Users will have access to underlying contributing/influencing KPIs provided the AH rule is honored.

-   Users will have access to sensitive information if the sensitive tag is enabled for their role.

## Use Cases

The subsequent sections describe the scenarios in which Smart KPIs integrate with People Management by communicating through their APIs. These sections describe the concept and process. For details such as the API preconditions, parameters, and JSON requests and responses for the APIs, refer to the corresponding sections in the [Smart KPIs API Reference](https://industryxdevhub.accenture.com/assetdetails/42) and the [People Management API Reference](https://industryxdevhub.accenture.com/assetdetails/64).

### 

### Use Case 1: GET- KPI dashboard

The KPI dashboard API is a part of the AOT-SmartKPI-Middleware Microservice that is invoked and consumed by the UI.

The KPI dashboard is a GET call to the Smart KPI AOT server hosted at the backend to get parent KPI details. On logging in, the KPI dashboard displays all the KPIs to which the user has owner access. Owners should have both read and write permissions on Asset Hierarchy and Timeseries.

To determine the kind of access each user has, the KPI Dashboard API calls a People Management API, **GET UsersByToken** to fetch the value for the isSensitive flag for each KPI. The value of the flag is either True or False. The value is true when the user has the relevant permission to view a KPI and false when the user does not have the permission to view that KPI. Thus, depending on the isSensitive flag value, only the KPI tiles that the user has access to are displayed on the dashboard by the Dashboard API.

###  Use Case 2: GET -- List API

The List API is part of the AOT-SmartKPI-Middleware API that is invoked by the UI and consumed by the UI. List API is a GET call to the Smart KPI AOT DEV server hosted to retrieve all timeseries available and to return it in JSON format. To retrieve timeseries and return them as JSON, it requires role details, which the List API fetches by calling a PM API- GETRoles.

The GETRoles API provides role details such as Role ID, Role Name, Role Type, Role Description, sensitivity status, creation details, associated Active Directory (AD) groups, users associated with the role, and departments associated with the role. The details required by the List API are Role ID, Department, and Department ID, which it uses to retrieve timeseries and generate the JSON response.

# 

### Use Case 3: POST- KPI Drilldown

The KPI drilldown API is part of the AOT-SmartKPI-Middleware Microservice that is invoked and consumed by the UI. It is a POST call to the Smart KPI AOT server hosted at the backend to get the contributing and influencing KPI details (external IDs) which are displayed to the user on clicking on the KPI tile. The contributing and influencing KPIs are defined below:

> [Contributing KPIs]\{.underline\}
>
> This represents all the KPIs of a selected KPI that directly contribute to the value/performance of the selected KPI. For example: for OEE at the plant level - the contributing KPIs can be availability, performance, and OEE at the system level among other KPIs.
>
> [Influencing KPIs]\{.underline\}
>
> This represents all the KPIs of a selected KPI that indirectly influence the value/performance of the selected KPI. For example: for OEE at the plant level - the influencing KPIs can be the number of safety incidents among other KPIs.
>
> The drilldown details, i.e., the contributing and influencing KPI details, displayed to a user are based on the user\'s role authorizations, which the Drilldown API fetches from a People Management GetAOTRoleById API.

Sensitivity tags of the KPI and the user role are used by the API to decide whether a user can view that KPI in drilldown or not. The POST KPI DRILLDOWN API fetches the sensitivity tag of the user\'s role from the PM API to validate against and display the drilldown details accordingly. The following points explain how a user\'s role and permissions affect the drilldown view.

-   If contributing/influencing KPIs have a sensitivity tag as \'Yes\' and the user role also has a sensitivity tag as \'Yes\', then the user can see that KPI in the drilldown.

-   If the contributing/influencing KPI has a sensitivity tag as \'Yes\' and the user role does not have a matching sensitivity tag, then the user cannot view see that KPI in the drilldown.

-   When users have multiple roles, they can see all the contributing or influencing KPIs for which the user has read permission through all the roles assigned to the user considering the above points.

-   When either or both the target and forecast timeseries data are not available in ADX, the KPI drilldown API will return \"NA\" as a response, Thus, it must be noted that the target and forecast timeseries are not mandatory for the parameters.

-   If the sensitivity requirements are met (both tags are \'Yes\') then the user can also drilldown the entire KPI hierarchy (contributing and influencing KPIs) of the parent KPI. The user should be able to view the parameters and their corresponding values.

-   If a user has owner access to a KPI, they also have viewer access to its contributing and influencing KPIs as well as view access to further drill down in the KPI hierarchy.

-   If the owner role of a parent KPI gets updated, the old role (previous owner role) can still view the contributing and influencing KPIs if the old role has owner/viewer access to other KPIs for which the contributing and influencing KPIs of the parent KPI are also contributing/ influencing or come up during the drill down of other KPIs.

-   If a role is provided owner access to a KPI for which the role already had viewer access, the user should be able to view the new KPI in the main dashboard as well as in the KPI drill down wherever the KPI comes up as an influencing/contributing KPI.

-   The Kafka message is integrated into the \'Define KPI in Azure\' process. This process enables the user to add/update roles associated with KPIs.

# 

### 

### Use Case 4: POST- RAG API

The RAG API is part of the AOT-SmartKPI-Middleware Microservice that is invoked and consumed by GetAssetRagInsightPriority API from AOT-OH-Module-Middleware APIs. It is a POST call to the Smart KPI AOT server hosted at the backend to get RAG status of an Asset based on all the KPIs RAG status.

RAG status of an Asset, which is based on KPIs RAG status, is defined on a priority basis as follows:

1.  *Red*

2.  *Amber*

3.  *Green*

The RAG status with highest priority will be picked. For example, consider an asset (Asset 1) who has the details shown below:

  -----------------------------------------------------------------------
               **KPI**                          **RAG Status**
  ---------------------------------- ------------------------------------
                KPI 1                               Amber

                KPI 2                               Green

                KPI 3                               Amber

                KPI 4                                Red

                KPI 5                               Green
  -----------------------------------------------------------------------

As shown in the table, *Asset 1* contains five KPIs with various RAG statuses. In this example, the RAG status of *Asset 1* will be Red because of the status of *KPI 4* even though the other four KPIs have lower priority statuses.

Additionally, user roles and sensitivity flags have been integrated so that:

1.  Each User Role must possess Owner-level permission for the Asset to obtain its RAG status.

2.  For KPIs to be factored into the RAG calculation, it is necessary that all User Roles have a minimum of Viewer access to the KPIs associated with an Asset.

3.  For the RAG calculation, all non-sensitive KPIs will be included, taking into account point 2.

4.  Sensitive KPIs will only factor into the RAG calculation if the user role includes viewer permissions for that KPI and if Role Sensitivity is marked as *Yes* for that specific role.

# 

# Result

Once the Roles have been added, they are visible to the user in the Timeseries, and the Assets are visible in the Azure Digital Twin portal.

![Result screenshot as per example described](media/image11.png)\{width="12.805964566929134in" height="6.5in"\}
