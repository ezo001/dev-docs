---
id: aot-people-management-api-reference-auriga
title: AOT People Management API Reference Auriga
---

**Accenture Operations Twin**

**People Management Configuration**

**API REFERENCE**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin / People Management |
| **Domain / Area** | Identity and Access Management |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Ranganathan, Balamurugan; Rishabh Joshi |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | People Management Architecture Blueprint, People Management API Reference |

**Contents**

[Introduction [3](#introduction)](#introduction)

[Target Audience [3](#target-audience)](#target-audience)

[Purpose [3](#purpose)](#purpose)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[People Management APIs [4](#people-management-apis)](#people-management-apis)

[POST- CreateOrUpdateAOTDepartment [5](#post--createorupdateaotdepartment)](#post--createorupdateaotdepartment)

[POST- CreateOrUpdateAOTRole [6](#post--createorupdateaotrole)](#post--createorupdateaotrole)

[GET- ValidateRoleName [7](#get--validaterolename)](#get--validaterolename)

[GET- ValidateDepartmentName [8](#get--validatedepartmentname)](#get--validatedepartmentname)

[GET- ValidateDepartmentDeletion [9](#get--validatedepartmentdeletion)](#get--validatedepartmentdeletion)

[GET- ValidateRoleDeletion [10](#get--validateroledeletion)](#get--validateroledeletion)

[POST- SearchADGroups [11](#post--searchadgroups)](#post--searchadgroups)

[POST- SearchUser [12](#post--searchuser)](#post--searchuser)

[GET- GetUsers [13](#get--getusers)](#get--getusers)

[GET- GetUsersByToken [14](#get--getusersbytoken)](#get--getusersbytoken)

[POST- GetUsersByRole [15](#post--getusersbyrole)](#post--getusersbyrole)

[POST- GetUsersByDepartment [16](#post--getusersbydepartment)](#post--getusersbydepartment)

[GET- GetRoles [17](#get--getroles)](#get--getroles)

[POST- GetRolesByUser [18](#post--getrolesbyuser)](#post--getrolesbyuser)

[GET- GetAdminRoles [19](#get--getadminroles)](#get--getadminroles)

[GET- GetRoleById [20](#get--getrolebyid)](#get--getrolebyid)

[GET- GetRolesByIds [21](#get--getrolesbyids)](#get--getrolesbyids)

[GET- GetDepartments [22](#get--getdepartments)](#get--getdepartments)

[POST- GetRolesByDepartment [23](#post--getrolesbydepartment)](#post--getrolesbydepartment)

[DELETE- DeleteAOTDepartment [24](#delete--deleteaotdepartment)](#delete--deleteaotdepartment)

[DELETE- DeleteAOTRole [25](#delete--deleteaotrole)](#delete--deleteaotrole)

[POST- SyncServiceAPI [26](#post--syncserviceapi)](#post--syncserviceapi)

[GET- LastRunSyncServiceAPI [26](#get--lastrunsyncserviceapi)](#get--lastrunsyncserviceapi)

[POST- MapUsersandRoles [27](#post--mapusersandroles)](#post--mapusersandroles)

[POST- MapGroupsandRoles [28](#post--mapgroupsandroles)](#post--mapgroupsandroles)

[POST- MapDepartmentsandRoles [29](#post--mapdepartmentsandroles)](#post--mapdepartmentsandroles)

[DELETE- DeleteDepartmentandRoleMapping [30](#delete--deletedepartmentandrolemapping)](#delete--deletedepartmentandrolemapping)

[DELETE- DeleteGroupandRoleMapping [31](#delete--deletegroupandrolemapping)](#delete--deletegroupandrolemapping)

[DELETE- DeleteUserandRoleMapping [32](#delete--deleteuserandrolemapping)](#delete--deleteuserandrolemapping)

[GET- GetADGroupRoleMappings [33](#get--getadgrouprolemappings)](#get--getadgrouprolemappings)

[GET- GetUserRoleMappings [34](#get--getuserrolemappings)](#get--getuserrolemappings)

[GET- GetUserAdGroupMappings [35](#get--getuseradgroupmappings)](#get--getuseradgroupmappings)

[POST- Azure Web PubSub [36](#post--azure-web-pubsub)](#post--azure-web-pubsub)

# Introduction

Accenture Operations Twin (AOT), an Industrial AI Foundation asset, is a set of software accelerators for the rapid implementation of customized factory-to-cloud applications. These operations twin apps accelerate the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The Industrial AI Foundation is a portfolio of composable data services for a rapid implementation of Industrial AI solutions that was developed as part of Accenture’s Industrial AI (IAI) initiative. IAI is a multi-disciplinary partnership between Accenture’s Data & AI and Industry X groups. The partnership was formed to address domain-specific challenges by employing state-of-the-art AI technology.

People Management (PM) is an AOT component that helps in managing the users, roles, and permissions for access to data and functionality. This component is duly integrated with the client's active directory to avoid duplicity and can also be integrated with other AOT components to fetch user-specific information. AOT’s People Management Configuration Middleware APIs can be used to query data about users, roles, and departments and perform create/update/delete operations on roles and departments.

## Target Audience

Developers with the following skills:

- SQL Server Management studio.

- Configure SQL database to Azure server.

- Install API-related DLL.

- API Management Service.

## Purpose

This reference document includes information about paths, inputs, outputs, and error management of AOT’s People Management configuration and middleware APIs.

## Prerequisites

An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64) may be useful.

## Contacts

- ``

- [`rishabh.b.joshi@accenture.com`](mailto:`rishabh.b.joshi@accenture.com`)

## Related Links

- [AOT PM Documentation](https://industryxdevhub.accenture.com/assetdetails/64)

- [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| **Term / Acronym** | **Definition** |
|:---|----|
| AOT (Accenture Operations Twin) | A collection of software accelerators and tools designed to integrate product, process, and live data from disparate IT and OT systems, providing a comprehensive view of operations for better decision-making and process optimization. |
| Active Directory (AD) | A Microsoft directory service used for identity and access management, integrated with AOT People Management for user and group management. |
| Department | An organizational unit within AOT, which can be created, updated, revived, or deleted using the API. |
| Role | A set of permissions or responsibilities assigned to users or departments in AOT, which can be managed via the API. |
| Group | A collection of users in Active Directory, which can be mapped to roles within AOT. |
| Authorization Token | A security credential acquired from Azure AD, required for authenticating API calls. |
| SQL Alchemy | A SQL toolkit and Object Relational Mapper (ORM) used by the Flask framework to communicate with the database. |
| Flask | A Python-based micro web framework used to develop the People Management Configuration APIs. |
| Kubernetes | A cloud-agnostic container orchestration platform used to host the APIs. |
| Epoch Time (UTC) | A time representation format used in the APIs, referring to the number of seconds since January 1, 1970 (Coordinated Universal Time). |
| Middleware API | APIs that provide a unified interface between the People Management Database and AOT Applications, enabling backend data visualization and actions. |
| Create/Update/Delete Operations | API functions that allow the creation, modification, or removal of roles and departments in AOT. |
| Azure Web PubSub | A service used to send messages to users, groups, or all users via the backend of an AOT application. |
| Admin Roles | Special roles in AOT with administrative privileges, retrievable via the API. |
| RoleId / DepartmentId / GroupId / UserId | Unique identifiers for roles, departments, groups, and users within AOT and AD. |

# 

# People Management APIs

The Python-based People Management Configuration APIs described in this document are developed using the Flask micro web framework and then hosted on a cloud-agnostic Kubernetes environment. SQL Alchemy is the SQL toolkit that has been used to achieve the Object Relational Mapper (ORM) approach used by Flask to communicate with the database. The PM APIs should be used by providing the Authentication Token that is managed by Azure API Management. All the time zones are in [Epoch time (UTC](https://www.epochconverter.com/)) format.

The Middleware APIs help in fetching the People Management information from the backend for the end users to visualize and perform actions on the backend data. The APIs allow the user to:

- Perform Create, Update, and Delete operations on Roles or Departments.

- Search Groups and Users for AD.

- Validate Department name, Role name, Department deletion, and Role deletion.

The middleware APIs provide a unified interface between the People Management Database (backend of AOT) and the consumers of the data (AOT Applications). These APIs are not only used by the People Management Configuration User Interface but are also consumed by other AOT components to get User (Roles and Departments) specific Information. The complete list of APIs can be found below.

- POST-CreateOrUpdateAOTDepartment

- POST- CreateOrUpdateAOTRole

- GET- ValidateRoleName

- GET-ValidateDepartmentName

- GET - ValidateDepartmentDeletion

- GET-ValidateRoleDeletion

- POST-SearchADGroups

- POST-SearchUser

- GET-GetUsers

- GET-GetUsersByToken

- POST-GetUsersByRole

- POST-GetUsersByDepartment

- GET-GetRoles

- POST-GetRolesByUser

- GET-GetAdminRoles

- GET- GetRoleById

- GET-GetDepartments

- POST-GetRolesByDepartment

- DELETE-DeleteAOTDepartment

- DELETE-DeleteAOTRole

- POST- SyncServiceAPI

- GET- LastRunSyncServiceAPI

- POST-MapUserandRolesAPI

- POST-MapGroupsandRolesAPI

- POST-MapDepartmentsandRolesAPI

- DELETE-DeleteDepartmentandRoleMapping

- DELETE- DeleteGroupandRoleMapping

- DELETE- DeleteUserandRoleMapping

- GET- GetADGroupRoleMappings

- GET- GetUserRoleMappings

- GET- GetUserAdGroupMappings

The APIs listed in the table above are described in detail in the sections that follow.

***API Preconditions***

To fetch the response from many of the APIs, the following entities exist:

- Authorization token

- DepartmentId

- DepartmentName

- DepartmentDescription

- ReviveArchivedDepartment

- Authorization token

- RoleId

- RoleName

- RoleDescription

- ReviveArchivedRole

- IsSensitive

- Departments

  - Remove/Add

    - DepartmentId

- Users

  - Remove/Add

    - UserId

- Groups

  - Remove/Add

    - GroupId

- Content-Type

## 

## POST- CreateOrUpdateAOTDepartment

This API is used to Create, Update, or Revive an AOT Department based on the request body.

- To create a department, department details are needed except the department ID, which is autogenerated.

- To update or revive a department, departmentId is mandatory and it returns the corresponding AOT department details.

### API Preconditions

| Content-TypePROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/departments |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/departments |
| METHOD | POST |
| CONTENT TYPE | application / json |

###  Input Header Parameters

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| DepartmentId | Provide the departmentId of the existing department if the department needs to be updated or revived. While there is no need to provide departmentid when creating a new department | M | String |
| DepartmentName | Provide a department name if new a department needs to be created. | M | String |
| DepartmentDescription | Provide a department description for departments | O | String |
| ReviveArchivedDepartment | Provide reviveArchivedDepartment as true to revive the AOT department. | O | Boolean |

\*Mandatory / Optional

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter              | Description                             | Type   |
|------------------------|-----------------------------------------|--------|
| Department Id          | Department ID from departments          | String |
| Department name        | Department name from departments        | String |
| Department Description | Department description from departments | String |

### Sample JSON Request

`{`

"DepartmentId": "",

"DepartmentName": "",

"DepartmentDescription": "",

"ReviveArchivedDepartment": ""

`}`

### Sample JSON Response

`{`

"Department":

`{`

"DepartmentId": "",

"DepartmentName": "",

"DepartmentDescription": ""

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | AOT department information is based on the created, updated, or revived departments. |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter valid department details
``
``
``
``

## 

## POST- CreateOrUpdateAOTRole

This API is used to Create, Update, or Revive an AOT Role based on the request body. To create a role, role details are needed except RoleID, as it is auto-generated. To update or revive a role, RoleID is mandatory, and it returns the corresponding AOT role details.

### API Preconditions

| PROTOCOL | HTTPS |
|:---|----|
| PATH AOT (Cognite) |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/roles |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| RoleId | Provide role Id of existing roles if roles need to be updated or revived. There is no need to provide a role ID while creating a new role | M | String |
| RoleName | Provide a role name if a new role needs to be created. | M | String |
| RoleDescription | Provide a description of the role | O | String |
| IsSensitive | Provide a Boolean value. If the value is true, there are some sensitive KPIs that users in those roles can access, otherwise not | M | Boolean |
| ReviveArchivedRole | Provide a ReviveArchivedRole as true to revive the AOT role | O | Boolean |
| Departments | Provide the departmentId to add or remove a RolesDepartmentsMapping in the Add or Remove list, respectively | O | String |
| Users | Provide the userId to add or remove a UserRolesMapping in the Add or Remove list, respectively | O | String |
| Groups | Provide the groupId to add or remove an ADGroupsMapping in the Add or Remove list, respectively | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | The role id of an AOT roles | String |
| RoleName | The role name of an AOT roles | String |
| RoleDescription | The role description of an AOT roles | String |
| RoleType | Role type of AOT roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are some sensitive KPIs that users in those roles can access, otherwise not. | Boolean |

### 

### Sample JSON Request

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"IsSensitive": "",

"ReviveArchivedRole": "",

"Departments":

`{`

"Remove":

\[

`{“DepartmentId": "“}`,

`{“DepartmentId": "“}`

\],

"Add":

\[

`{“DepartmentId": "“}`,

`{“DepartmentId": "“}`

\]

`}`,

"Users":

`{`

"Remove":

\[ `{“UserId": "“}`,

`{“UserId": "“}`

\],

"Add":

\[

`{“UserId": "“}`,

`{“UserId": "“}`

\]

`}`,

"Groups":

`{`

"Remove":

\[

`{“GroupId": "“}`,

`{“GroupId": "“}`

\],

"Add":

\[

`{“GroupId": "“}`,

\]

`}`

`}`

`{“GroupId": "“}`

### Sample JSON Response

`{`

"Role":

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"RoleType": "",

"IsSensitive": ""

`}`

`}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | AOT Role information is based on the created, updated, or revived roles. |

**Error Management**






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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter valid details
``
``
``
``

## 

## GET- ValidateRoleName

This API is used for validating the AOT role name within a plant based on a known role name and list of role IDs linked to the plant.

### API Preconditions

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/`{roleName}`/validateName?roleIds=`{roleIds}` |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/`{roleName}`/validateName?roleIds=`{roleIds}` |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description                   | M/O | Type   |
|-----------|-------------------------------|-----|--------|
| RoleName  | Provide a valid AOT role name | M   | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| RoleIds | Provides a list of active and inactive Role IDs associated with the specific Plant | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleArchived | The value of this parameter specifies whether the role name is active or not in the database. | Boolean |
| RoleExists | The value of this parameter specifies whether the role exists or not in the database. | Boolean |
| DeletedRoleId | DeletedRoleId based on the role name provided | Boolean |

### Sample JSON Response

`{`

"RoleArchived": false,

"RoleExists": false,

"DeletedRoleId": false

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | Boolean output for RoleExists, RoleArchived, and DeletedRoleId based on the role name provided. |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid role name for the request URL
``
``
``
``

## 

## GET- ValidateDepartmentName

This API is used for validating the AOT department name.

### API Preconditions

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/departments/`{departmentName}`/validateName |
| PATH AOT(Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/departments/`{departmentName}`/validateName |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls | M | String |

### Input Path Parameters

| Parameter | Description | Mandatory / Optional | Type |
|----|----|----|----|
| departmentName | Provide a valid AOT department name | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| DepartmentArchived | Specifies whether the department name is active or not in the database. | Boolean |
| DepartmentExists | Specifies whether the department exists or not in the database. | Boolean |
| DeletedDepartmentId | Deletes department ID based on the department name provided. | Boolean |

### Sample JSON Response

`{`

"DepartmentArchived": false,

"DepartmentExists": false,

"DeletedDepartmentId": false

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | Based on the department name, Boolean output for DepartmentExists, DepartmentArchived, and DeletedDepartmentId. |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid department name for the request URL
``
``
``
``

## 

## GET- ValidateDepartmentDeletion

This API is used for validating AOT department deletion.

### API Preconditions

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/departments/`{departmentId}`/validateDeletion |
| PATH AOT(Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/departments/`{departmentId}`/validateDeletion |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter    | Description                       | M/O | Type   |
|--------------|-----------------------------------|-----|--------|
| DepartmentId | Provide a valid AOT department ID | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter    | Description             | Type    |
|--------------|-------------------------|---------|
| CanbeDeleted | Return true/false value | Boolean |

### Sample JSON Response

`{`

"CanbeDeleted": false,

`}`

### Result

| **HTTP Code** | **Result Description**                              |
|---------------|-----------------------------------------------------|
| 200           | Showing CanbeDeleted value which is in Boolean type |

### Error Manegement






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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid department ID for the request URL
``
``
``
``

## 

## GET- ValidateRoleDeletion

This API is used for validating AOT role deletion.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- RoleId

### API Preconditions

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT(Cognite)`\<`Public Exposure`\>` | [https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/`{roleId}`/validateDeletion](https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/%7broleId%7d/validateDeletion) |
| PATH AOT(Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/`{roleId}`/validateDeletion |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description                 | M/O | Type   |
|-----------|-----------------------------|-----|--------|
| RoleId    | Provide a valid AOT role ID | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

Output Body Parameters

| Parameter    | Description             | Type    |
|--------------|-------------------------|---------|
| CanbeDeleted | Return true/false value | Boolean |

### Sample JSON Response

`{`

"CanbeDeleted": false,

`}`

Result

| **HTTP Code** | **Result Description**                              |
|---------------|-----------------------------------------------------|
| 200           | Showing CanbeDeleted value which is in Boolean type |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid role name for the request URL
``
``
``
``

## 

## POST- SearchADGroups

This API is used for retrieving a list of all AD groups. AD groups can also be filtered using the group name.

**API Precondition**

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- QueryString

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/groups/search |
| METHOD | POST |
| CONTENT TYPE | application / json |

**Input Header**

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

**Input Body**

| **BODY PARAM** |  |  |  |
|----|----|----|----|
| Parameter | Description | M/O | Type |
| QueryString | Provide a query string to filter AD groups by name | M | String |

**Sample JSON Request**

`{`

"QueryString": ""

`}`

### Output Header

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body

| Parameter | Description                | Type   |
|-----------|----------------------------|--------|
| GroupId   | Group ID of the AD group   | String |
| GroupName | Group Name of the AD group | String |

**Sample JSON Response**

`{`

"Groups": \[

`{`

"GroupId": "",

"GroupName": ""

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | The result is a list of all AD groups or selected AD groups whose names start with the query string present in the request body |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter valid query details
``
``
``
``

## 

## POST- SearchUser

This API is used for searching users from AD or AOT. While AOT users can be filtered using RoleIDs, no such filtering is available to AD users.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- QueryString

- AOTUsersOnly

- RoleIds

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/users/search |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| QueryString | Provide a query string to filter users whose display name or email starts with the query string | M | String |
| AOTUsersOnly | Provide a Boolean value. This value is true if the search is only for AOT users and false for all AD users. | M | Boolean |
| RoleIds | Provide an AOT Role ID (AOTUsersOnly as True, if AOT users with given roles need to be searched. AOTUsersOnly as False, RoleIds cannot be provided in case of AD users.) | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter         | Description                                | Type   |
|-------------------|--------------------------------------------|--------|
| UserId            | User ID of the AOT user                    | String |
| DisplayName       | The display name of the AOT user on the UI | String |
| FirstName         | First name of the AOT user                 | String |
| LastName          | Last name of the AOT user                  | String |
| UserPrincipalName | User principal name of the AOT user        | String |
| PhoneNumber       | Phone number of the AOT user               | String |
| Email             | Email of the AOT user                      | String |

### Sample JSON Request

`{`

"QueryString": "",

"AOTUsersOnly": "True/False (Give this value as true if the search should be only on AOT users and false if on all AD users)",

"RoleIds": \[

"",

""

\]

`}`

### Sample JSON Response

`{`

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"FirstName": "",

"LastName": "",

"UserPrincipalName": "",

"PhoneNumber": "",

"Email": ""

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description**        |
|---------------|-------------------------------|
| 200           | Displaying a user's AOT or AD |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter valid query details
``
``
``
``

## 

## GET- GetUsers

This API is used for AOT users based on ID. If no ID is given, then all AOT users will be returned.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- UserId





``

``
PROTOCOL
HTTPS
``
``

``
PATH AOT (Cognite) `\<`Public Exposure`\>`
`Without userId: https://apim-mw-aot-dev.azure-api.net/api/people-management/users`
With userId: https://apim-mw-aot-dev.azure-api.net/api/people-management/users /`{userId}`
``
``
PATH AOT (Azure)`\<`Public Exposure`\>`
`Without userId: https://apim-aot-azure-dev.azure-api.net/api/people-management/users`
With userId: https://apim-aot-azure-dev.azure-api.net/api/people-management/users/`{userId}`
``
``
METHOD
GET
``
``
CONTENT TYPE
application / json
``
``
``

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| userId | Provide a valid user ID for the request URL | O | String |
| IncludeUserRolesDepts | Provides IncludeUserRolesDepts as false to get only User info in the response. | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter         | Description                                 | Type   |
|-------------------|---------------------------------------------|--------|
| UserId            | The user id of the AOT user                 | String |
| DisplayName       | The display name of the AOT user on the UI  | String |
| FirstName         | First name of the AOT user                  | String |
| LastName          | Last name of the AOT user                   | String |
| UserPrincipalName | User principal name of the AOT user         | String |
| PhoneNumber       | Phone number of the AOT user                | String |
| Email             | Email of the AOT user                       | String |
| RoleId            | Role ID of the AOT user roles               | String |
| RoleName          | Role Name of the AOT user roles             | String |
| DepartmentId      | Department ID of the AOT user departments   | String |
| DepartmentName    | Department name of the AOT user departments | String |

### Sample JSON Response

`{`

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"FirstName": "",

"LastName": "",

"UserPrincipalName": "",

"PhoneNumber": "",

"Email": "",

"UserRoles": \[

`{`

"RoleId": "",

"RoleName": ""

`}`

\],

"UserDepartments": \[

`{`

"DepartmentId": "",

"DepartmentName": ""

`}`

\]

`}`

\]

`}`

### Result

| HTTP Code | Result Description                              |
|-----------|-------------------------------------------------|
| 200       | AOT users based on userId provided or all users |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid Authorization token
``
``
``
``

## GET- GetUsersByToken

This API is used for fetching user information by token. UserId is retrieved by decoding the token and the user will be returned.

### API Precondition

To fetch the response from the APIs, the following entities exist.

- Authorization token

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) |
| PATH AOT (Azure) `\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/users/bytoken |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters






``

``
Parameter
Description
M/O
``
``

``
QueryString
`Provide QueryString as UseToken to get Adgroups from tokens and fetch associated roles.`
Provide QueryString as UseGraph to get Adgroups from graph API using userId and fetch associated roles.
Provide QueryString as None to get Adgroups from both token and graph API and then fetch associated roles.
O
``
``
``

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter         | Description                                 | Type   |
|-------------------|---------------------------------------------|--------|
| UserId            | User ID of the AOT user                     | String |
| DisplayName       | The display name of the AOT user on the UI  | String |
| FirstName         | First name of the AOT user                  | String |
| LastName          | Last name of the AOT user                   | String |
| UserPrincipalName | User principal name of the AOT user         | String |
| PhoneNumber       | Phone number of the AOT user                | String |
| Email             | Email of the AOT user                       | String |
| RoleId            | Role ID of the AOT user roles               | String |
| RoleName          | Role Name of the AOT user roles             | String |
| DepartmentId      | Department ID of the AOT user departments   | String |
| DepartmentName    | Department name of the AOT user departments | String |

### Sample JSON Response

`{`

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"FirstName": "",

"LastName": "",

"UserPrincipalName": "",

"PhoneNumber": "",

"Email": "",

"UserRoles": \[

`{`

"RoleId": "",

"RoleName": ""

`}`

\],

"UserDepartments": \[

`{`

"DepartmentId": "",

"DepartmentName": ""

`}`

\]

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description**                           |
|---------------|--------------------------------------------------|
| 200           | AOT user is based on the UserId present in token |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid authorization token
``
``
``
``

## POST- GetUsersByRole

This API is for retrieving the list of users based on the RoleId present in the request body.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- Content-Type

- RoleIds

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)  |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/users/byRoles |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| RoleIds | Provide a list of roleIds whose associated users need to be retrieved | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter         | Description                                 | Type   |
|-------------------|---------------------------------------------|--------|
| UserId            | The user id of the AOT user                 | String |
| DisplayName       | The display name of the AOT user on the UI  | String |
| FirstName         | First name of the AOT user                  | String |
| LastName          | Last name of the AOT user                   | String |
| UserPrincipalName | User principal name of the AOT user         | String |
| PhoneNumber       | Phone number of the AOT user                | String |
| Email             | Email of the AOT user                       | String |
| RoleId            | Role Id of the AOT user roles               | String |
| RoleName          | Role Name of the AOT user roles             | String |
| DepartmentId      | Department ID of the AOT user departments   | String |
| DepartmentName    | Department name of the AOT user departments | String |

**Sample JSON Request**

`{`

"RoleIds": \[

"",

""

\]

`}`

**  
Sample JSON Response**

`{`

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"FirstName": "",

"LastName": "",

"UserPrincipalName": "",

"PhoneNumber": "",

"Email": "",

"UserRoles": \[

`{`

"RoleId": "",

"RoleName": ""

`}`

\],

"UserDepartments": \[

`{`

"DepartmentId": "",

"DepartmentName": ""

`}`

\]

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | list of AOT users based on the RoleId present in the request body |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid authorization token
Please enter valid role IDs
``
``
``
``

## 

## POST- GetUsersByDepartment

This API is used for retrieving a list of users based on a DepartmentId present in the request body.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- Content-Type

- DepartmentIds

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | [https://apim-mw-aot-dev.azure-api.net/api/people-management/users/byDepartments](https://apim-mw-aot-dev.azure-api.net/api/people-management/users/byRoles) |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/users/byDepartments |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| DepartmentIds | Provide a list of departmentIds whose associated users need to be retrieved | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter         | Description                                 | Type   |
|-------------------|---------------------------------------------|--------|
| UserId            | User ID of the AOT user                     | String |
| DisplayName       | The display name of the AOT user on the UI  | String |
| FirstName         | First name of the AOT user                  | String |
| LastName          | Last name of the AOT user                   | String |
| UserPrincipalName | User principal name of the AOT user         | String |
| PhoneNumber       | Phone number of the AOT user                | String |
| Email             | Email of the AOT user                       | String |
| RoleId            | Role ID of the AOT user roles               | String |
| RoleName          | Role Name of the AOT user roles             | String |
| DepartmentId      | Department ID of the AOT user departments   | String |
| DepartmentName    | Department name of the AOT user departments | String |

### Sample JSON Request

`{`

"DepartmentIds": \[

"",

""

\]

`}`

###  Sample JSON Response

`{`

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"FirstName": "",

"LastName": "",

"PhoneNumber": "",

"Email": "",

"UserRoles": \[

`{`

"RoleId": "",

"RoleName": ""

`}`

\],

"UserDepartments": \[

`{`

"DepartmentId": "",

"DepartmentName": ""

`}`

\]

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | list of AOT users based on the DepartmentId present in the request body |

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
Unauthorized User / `{Header Token}` could be missing
``
``
``
400
400
``
Bad request / Please enter the valid authorization token / Please enter valid department Ids
``
``
``
``

## 

## 

## GET- GetRoles

This API is used for fetching all AOT roles. If RoleID is given, it will return the corresponding AOT Role.

### API Precondition

To fetch the response from the APIs, the following entities must exist: Authorization token, RoleId





``

``
PROTOCOL
HTTPS
``
``

``
PATH AOT (Cognite)`\<`Public Exposure`\>`
`Without RoleId: https://apim-mw-aot-dev.azure-api.net/api/people-management/roles`
With RoleId: https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/`{roleId}`
``
``
PATH AOT (Azure)`\<`Public Exposure`\>`
`Without RoleId: https://apim-aot-azure-dev.azure-api.net/api/people-management/roles`
With RoleId: https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/`{roleId}`
``
``
METHOD
GET
``
``
CONTENT TYPE
application / json
``
``
``

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description                                         | M/O | Type   |
|-----------|-----------------------------------------------------|-----|--------|
| roleId    | Provide a valid role ID passed from the request URL | O   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | Role ID of the AOT roles | String |
| RoleName | Role Name of the AOT roles | String |
| RoleDescription | Role Description of the AOT Roles | String |
| RoleType | Role type of the AOT roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are sensitive KPIs that users in those roles can access, otherwise not | Boolean |
| CreatedBy | Name of the user who created the AOT role | String |
| CreatedTime | Creation Time of the AOT Role | Date Time |
| UsersCount | Count of users in the AOT Roles | String |
| UserId | The user ID of the AOT user | String |
| DisplayName | UI Display name of the AOT user | String |
| PhoneNumber | Phone number of the AOT user | String |
| Email | Email of the AOT user | String |
| GroupId | Group ID of the AD Group | String |
| GroupName | The group name of the AD Group | String |
| DepartmentId | Department ID of the AOT Department | String |
| DepartmentName | Department name of the AOT Department | String |
| DepartmentDescription | Department Description of the AOT Department | String |

### 

### Sample JSON Response

`{`

"Roles": \[

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"RoleType": "",

"IsSensitive": "",

"CreatedBy": "",

"CreatedTime": "",

"UsersCount": "",

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"PhoneNumber": "",

"Email": ""

`}`

`\>` \],

"ADGroups": \[

`{`

"GroupId": "",

"GroupName": ""

`}`

\],

"Departments": \[

`{`

"DepartmentId": "",

"DepartmentName": "",

"DepartmentDescription": ""

`}`

`}`

\]

`}`

###  Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | The list of all the AOT roles or a single role with a given RoleId |

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
`{Header Token}` could be missing
``
``
``
400
400
Bad request
``
``
``

## 

## POST- GetRolesByUser

This API is used for retrieving a list of roles based on UserIds present in the request body.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

- UserIds

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/byUser |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| UserIds | Provide a list of user IDs whose associated roles need to be retrieved | M | String |

### Sample JSON Request

`{`

"UserIds": \[

"",

""

\]

`}`

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | Role id of the AOT user roles | String |
| RoleName | Role name of the AOT user roles | String |
| RoleDescription | The role description of the AOT user roles | String |
| RoleType | Role type of the AOT user roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are some sensitive KPIs that users in those roles can access, otherwise not | Boolean |
| DepartmentId | Department ID of AOT user departments | String |
| DepartmentName | Department name of the AOT user department | String |

### Sample JSON Response

`{`

"Roles": \[

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"RoleType": "",

"IsSensitive": "",

"Departments": \[

`{`

"DepartmentId": "",

"DepartmentName": ""

`}`

\]

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | The list of the roles associated with the users present in the request body |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter valid userIds
``
``
``
``

## GET- GetAdminRoles

This API is used for retrieving a list of all the admin roles in AOT.

### API Precondition

To fetch the response from the APIs, the Authorization token must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/admin |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/admin |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | Role id of the AOT user roles | String |
| RoleName | Role name of the AOT user roles | String |
| RoleDescription | The role description of the AOT user roles | String |
| RoleType | Role type of the AOT user roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are some sensitive KPIs that users in those roles can access, otherwise not | Boolean |
| DepartmentId | Department ID of AOT user departments | String |
| DepartmentName | Department name of the AOT user department | String |

### Sample JSON Response

`{`

"Roles": \[

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"RoleType": "",

"IsSensitive": "",

"CreatedBy": "",

"CreatedTime": "",

"UsersCount": "",

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"PhoneNumber": "",

"Email": ""

`}`

\],

"ADGroups": \[

`{`

"GroupId": "",

"GroupName": ""

`}`

\],

"Departments": \[

`{`

"DepartmentId": "",

"DepartmentName": "",

"DepartmentDescription": ""

`}`

\]

`}`

\]

`}`

### Result

| HTTP Code | Result Description                 |
|-----------|------------------------------------|
| 200       | The list of the admin roles in AOT |

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
`{Header Token}` could be missing
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

## GET- GetRoleById

This API is used for retrieving a list of all the roles associated with a RoleId provided in the query parameter.

**API Precondition**

To fetch the response from the APIs, the Authorization token and RoleId must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/`{roleId}` |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/`{roleId}` |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| RoleId | Provide a valid existing roleId | M | String |
| IsDeletedRole | Provides ‘true’ if this role is deleted and is being fetched as a query parameter. | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | Role ID of the AOT user roles | String |
| RoleName | Role name of the AOT user roles | String |
| RoleDescription | The role description of the AOT user roles | String |
| RoleType | Role type of the AOT user roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are some sensitive KPIs that users in those roles can access, otherwise not | Boolean |
| DepartmentId | Department ID of AOT user departments | String |
| DepartmentName | Department name of the AOT user department | String |

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The list of the roles associated with the RoleId provided in the query parameter. |

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
`{Header Token}` could be missing
``
``
400
400
Bad request
``
``
``

## 

## GET- GetRolesByIds

This API is used for retrieving a list of all the roles associated with a list of RoleIds provided in the query parameter.

**API Precondition**

To fetch the response from the APIs, the Authorization token and List of RoleIds must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/roles/`{roleId}` |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/`{roleId}` |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description                              | M/O | Type   |
|-----------|------------------------------------------|-----|--------|
| RoleId    | Provide a list of existing valid RoleIds | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | Role id of the AOT user roles | String |
| RoleName | Role name of the AOT user roles | String |
| RoleDescription | The role description of the AOT user roles | String |
| RoleType | Role type of the AOT user roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are some sensitive KPIs that users in those roles can access, otherwise not | Boolean |
| DepartmentId | Department ID of AOT user departments | String |
| DepartmentName | Department name of the AOT user department | String |

### Sample JSON Response

`{`

"Roles": \[

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"RoleType": "",

"IsSensitive": "",

"CreatedBy": "",

"CreatedTime": "",

"UsersCount": "",

"Users": \[

`{`

"UserId": "",

"DisplayName": "",

"PhoneNumber": "",

"Email": ""

`}`

\],

"ADGroups": \[

`{`

"GroupId": "",

"GroupName": ""

`}`

\],

"Departments": \[

`{`

"DepartmentId": "",

"DepartmentName": "",

"DepartmentDescription": ""

`}`

\]

`}`

\]

`}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The list of the roles associated with the list of RoleIds provided in the query parameter. |

### Error Management

| HTTP Code | Error Code | Error Description                                   |
|-----------|------------|-----------------------------------------------------|
| 500       | 500        | Generic Error                                       |
| 400       | 401        | Unauthorized User / `{Header Token}` could be missing |
| 400       | 400        | Bad request                                         |

## GET- GetDepartments

This API is used for fetching all AOT departments. If DepartmentID is given, it will return the corresponding AOT Department.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.





``

``
PROTOCOL
HTTPS
``
``

``
PATH AOT (Cognite)`\<`Public Exposure`\>`
`Without department Id:`
https://apim-mw-aot-dev.azure-api.net/api/people-management/departments
With department Id:
https://apim-mw-aot-dev.azure-api.net/api/people-management/departments/`{departmentId}`
``
``
PATH AOT (Azure) `\<`Public Exposure`\>`
`Without department Id:`
https://apim-aot-azure-dev.azure-api.net/api/people-management/departments
With department Id:
https://apim-aot-azure-dev.azure-api.net/api/people-management/departments/`{departmentId}`
``
``
METHOD
GET
``
``
CONTENT TYPE
application / json
``
``
``

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| departmentId | Provide a valid department ID passed from the request URL | O | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| DepartmentId | Department ID of AOT user departments | String |
| DepartmentName | Department name of AOT user departments | String |
| DepartmentDescription | Department description of AOT user departments | String |
| CreatedBy | Name of the user who created the AOT department | String |
| CreatedTime | Creation Time of the AOT Department | Date Time |
| RolesCount | Count of roles in the AOT department | String |

### Sample JSON Response

`{`

"Departments": \[

`{`

"DepartmentId": "",

"DepartmentName": "",

"DepartmentDescription": "",

"CreatedBy": "",

"CreatedTime": "",

"RolesCount": ""

`}`

\]

`}`

### Result

| HTTP Code | Result Description |
|----|----|
| 200 | The list of AOT users based on the DepartmentId present in the request body |

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
`{Header Token}` could be missing
``
``
``
400
400
Bad request
``
``
``

## 

## POST- GetRolesByDepartment

This API is used for retrieving a list of roles based on DepartmentIds present in the request body.

### API Preconditions

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- Content-Type

- DepartmentIds

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/byDepartment |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| DepartmentIds | Provide a list of departmentIds whose associated roles need to be retrieved | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description | Type |
|----|----|----|
| RoleId | Role ID of an AOT user roles | String |
| RoleName | Role name of an AOT user roles | String |
| RoleDescription | The role description of an AOT user's roles | String |
| RoleType | Role type of an AOT user roles | String |
| IsSensitive | This is a Boolean value. If the value is true, there are sensitive KPIs that users in those roles can access. | Boolean |
| DepartmentId | Department ID of an AOT user department | String |
| DepartmentName | Department name of an AOT user department | String |

### 

### Sample JSON Request

`{`

"DepartmentIds": \[

"",

""

\]

`}`

###  Sample JSON Response

`{`

"roles": \[

`{`

"RoleId": "",

"RoleName": "",

"RoleDescription": "",

"RoleType": "",

"IsSensitive": "",

"Departments": \[

`{`

"DepartmentId": "",

"DepartmentName": ""

`}`

\]

`}`

\]

`}`

### 

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | The list of the roles associated with departments present in the request body |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter valid departmentIds
``
``
``
``

## DELETE- DeleteAOTDepartment

This API is used for disabling (soft deleting) the AOT department. The response contains a message with information about whether the department mapped to the given department ID was successfully deleted.

### API Preconditions

To fetch the response from the APIs, the Authorization token and DepartmentId must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`}` |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/departments/`{departmentId}` |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls | M | String |

### Input Path Parameters

| Parameter    | Description                                      | M/O | Type   |
|--------------|--------------------------------------------------|-----|--------|
| DepartmentId | Provide a valid department ID in the request URL | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Sample JSON Response

`{`

"message": "Department deleted successfully."

`}`

### Result

| **HTTP Code** | **Result Description**          |
|---------------|---------------------------------|
| 200           | Department deleted successfully |

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
`{Header Token}` could be missing.
Unauthorized User
``
``
``
400
400
``
Bad request
Please enter the valid department id for the request URL
``
``
``
``

## 

## DELETE- DeleteAOTRole

This API is used to disable (soft delete) the AOT role. The response contains a message with information about whether the role mapped to the given RoleId was successfully deleted.

### API Preconditions

To fetch the response from the APIs, the Authorization token and ruleId must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`}`` |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/roles/`{roleId}` |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description                                | M/O | Type   |
|-----------|--------------------------------------------|-----|--------|
| RoleId    | Provide a valid role ID in the request URL | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Sample JSON Response

`{`

"message": "Role deleted successfully."

`}`

### Result

| **HTTP Code** | **Result Description**    |
|---------------|---------------------------|
| 200           | Role deleted successfully |

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
`{Header Token}` could be missing.
Unauthorized User
``
``
``
400
400
``
Bad request
Please enter the valid role id for the request URL.
``
``
``
``

## 

## POST- SyncServiceAPI

This API is used to sync ADGroups and Users in People Management Database with any change in Azure Active Directory. This API also stores the Status, sync service’s start and end times, as well as the UserId in a log table in the PM Config Database. This API allows only one user to run a sync service at a time. Whenever another user attempts to run a sync service that is already running, an InProgress pop-up message is displayed to that user on the PM UI. This API sends completion/failure/InProgress status messages to the user on the PM UI by using Azure web pub API.

### API Preconditions

To fetch the response from the APIs, the Authorization token must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/syncservice |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/syncservice |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Result

| HTTP Code | Result Description         |
|-----------|----------------------------|
| 202       | Return sync service status |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
400
401
``
`{Header Token}` could be missing / Unauthorized User
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

## GET- LastRunSyncServiceAPI

This API is used to fetch the last run sync service timestamp and the user's name. The response contains a message with information about the end time of the last sync service run and the user's name who triggered it.

### API Precondition

To fetch the response from the APIs, the Authorization token must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/syncservice/lastRun |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/syncservice/lastRun |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Sample JSON Response:

`{`

"LastSyncedBy": "",

"LastSyncedDate": ""

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | Return the end time of the last sync service run and the user's name who triggered it |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
400
401
``
`{Header Token}` could be missing / Unauthorized User
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

## POST- MapUsersandRoles

This API is used to map the given AOT user to the given AOT role.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- userId

- roleId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/mappings/UsersWithRoles |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/mappings/UsersWithRoles |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content/Type | application / json | M | String |

### Input Body Parameters

| Parameter | Description | Type |
|----|----|----|
| UserId | Provide valid UserId of existing AOT users who needs to be mapped to the given role | String |
| RoleId | Provide valid RoleId of existing AOT roles which need to be mapped to the given AOT user | String |

### 

### Sample JSON Request 

`{`

"Mappings": \[

`{`

"UserId": "",

"RoleId": ""

`}`

\]

`}`

###  Sample JSON Response

`{`

"message": "User successfully mapped to the roles."

`}`

### Result

| HTTP Code | Result Description                                              |
|-----------|-----------------------------------------------------------------|
| 200       | Returns when the user successfully mapped to the given AOT role |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
400
401
``
`{Header Token}` could be missing / Unauthorized User
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

## POST- MapGroupsandRoles

This API is used to map the given AD group to the given AOT role.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- GroupId

- RoleId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)https://apim-mw-aot-dev.azure-api.net/api/people-management/mappings/GroupsWithRoles |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/mappings/GroupsWithRoles |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content/Type | application / json | M | String |

### Input Body Parameters

| Parameter | Description | Type |
|----|----|----|
| GroupId | Provide valid GroupId of existing AD groups which need to be mapped to the given role | String |
| RoleId | Provide valid RoleId of existing AOT roles which need to be mapped to the given AD group | String |

### 

### Sample JSON Request 

`{`

"Mappings": \[

`{`

"GroupId": "",

"RoleId": ""

`}`

\]

`}`

###  Sample JSON Response

`{`

"message": "User successfully mapped to the roles."

`}`

### Result

| HTTP Code | Result Description                                              |
|-----------|-----------------------------------------------------------------|
| 200       | Returns when the user successfully mapped to the given AOT role |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
400
401
``
`{Header Token}` could be missing / Unauthorized User
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

## POST- MapDepartmentsandRoles

This API is used to map the given AOT department to the given AOT role.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- DepartmentId

- RoleId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/mappings/RolesWithDepartment |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/mappings/RolesWithDepartment |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content/Type | application / json | M | String |

### Input Body Parameters

| Parameter | Description | Type |
|----|----|----|
| DepartmentId | Provide valid DepartmentId of existing AOT departments that needs to be mapped to the given role | String |
| Roleid | Provide valid Role ID of existing AOT roles which needs to be mapped to the given AOT user | String |

### Sample JSON Request 

`{`

"Mappings": \[

`{`

"DepartmentId": "",

"RoleId": ""

`}`

\]

`}`

### Sample JSON Response

`{`

"message": "Department successfully mapped to the roles."

`}`

### Result

| **HTTP Code** | **Result Description** |
|----|----|
| 200 | Returns when the department successfully mapped to the given AOT role |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
400
401
``
`{Header Token}` could be missing  Unauthorized User
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

## DELETE- DeleteDepartmentandRoleMapping

This API is used to soft delete the AOT role and AOT department mapping. The response will have a message with information on whether the mapping between the given AOT department and the AOT role was successfully deleted or not.

**API Precondition**

To fetch the response from the APIs, the following entities must exist.

- 

- Authorization token

- Content-Type

- DepartmentId

- RoleId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite) `\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/mappings/RolesWithDepartments/`{deparmentId}`/`{roleId}` |
| PATH AOT (Azure) https://apim-aot-azure-dev.azure-api.net/api/people-management/mappings/RolesWithDepartments/`{deparmentId}`/`{roleId}` |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Path Parameters

| Parameter    | Description                                      | M/O | Type   |
|--------------|--------------------------------------------------|-----|--------|
| DepartmentId | Provide a valid department ID in the request URL | M   | String |
| RoleId       | Provide a valid AOT role ID in the request URL   | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Sample Response

`{ “message": "Department Mapping to the Role successfully deleted.” }`

### Result

| **HTTP Code** | **Result Description**                              |
|---------------|-----------------------------------------------------|
| 200           | Department Mapping to the Role successfully deleted |

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
`{Header Token}` could be missing
``
``
``
400
400
``
Bad request
Please enter the valid departmentId and roleId for the request URL
``
``
``
``

## 

## DELETE- DeleteGroupandRoleMapping

Use this API to soft delete the AOT role and ADGroup mapping. The response will have a message with information on whether mapping between the given AOT role and ADGroup was successfully deleted or not.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

- GroupId

- RoleId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/mappings/GroupsWithRoles/`{groupId}`/`{roleId}` |
| PATH AOT (Azure) https://apim-aot-azure-dev.azure-api.net/api/people-management/mappings/GroupsWithRoles/`{groupId}`/`{roleId}` |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Path Parameters

| Parameter | Description                                    | M/O | Type   |
|-----------|------------------------------------------------|-----|--------|
| groupId   | Provide a valid ADGroupId in the request URL   | M   | String |
| roleId    | Provide a valid AOT role ID in the request URL | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Sample Response

`{ “message": "ADGroup Mapping to the Role successfully deleted.” }`

### Result

| **HTTP Code** | **Result Description**                                |
|---------------|-------------------------------------------------------|
| 200           | ADGroup Mapping to the Role was successfully deleted. |

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
Unauthorized User / `{Header Token}` could be missing
``
``
``
400
400
``
Bad request / Please enter the valid ADGroup and roleId for the request URL
``
``
``
``

## 

## DELETE- DeleteUserandRoleMapping

This API is used to soft delete AOT user and AOT role mapping. The response will have a message with information on whether mapping between the given AOT role and the AOT user was successfully deleted or not.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- Content-Type

- UserId

- RoleId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/mappings/UsersWithRoles/`{userId}`/`{roleId}` |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/mappings/UsersWithRoles/`{userId}`/`{roleId}` |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Path Parameters

| Parameter | Description                                    | M/O | Type   |
|-----------|------------------------------------------------|-----|--------|
| UserId    | Provide an AOT userId in the request URL       | M   | String |
| RoleId    | Provide a valid AOT role ID in the request URL | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Sample Response

`{ “message": "User Mapping to the Role successfully deleted.” }`

### Result

| **HTTP Code** | **Result Description**                        |
|---------------|-----------------------------------------------|
| 200           | User Mapping to the Role successfully deleted |

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
Unauthorized User / `{Header Token}` could be missing
``
``
``
400
400
``
Bad request / Please enter the valid userId and roleId for the request URL
``
``
``
``

## 

## GET- GetADGroupRoleMappings

This API is used to fetch all the AD Groups and their respective associated AOT Roles.

### API Precondition

To fetch the response from the APIs, the Authorization token must exist.

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/groups/directRoles |
| PATH AOT (Azure)https://apim-aot-azure-dev.azure-api.net/api/people-management/groups/directRoles |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter  | Description               | Type   |
|------------|---------------------------|--------|
| adgroup_id | Object ID of the AD Group | String |
| RoleId     | Role ID of the AOT roles  | String |

### Sample JSON Response

`{`

"`\<`adgroup_id`\>`": [

`{`

"RoleId": ""

`}`

\],

"`\<`adgroup_id`\>`": [

`{`

"RoleId": ""

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description**                                    |
|---------------|-----------------------------------------------------------|
| 200           | The key is AD Group Id and value is the list of AOT Roles |

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
Unauthorized User / `{Header Token}` could be missing
``
``
``
400
400
Bad request
``
``
``

## 

## GET- GetUserRoleMappings

This API is used to fetch a list of AOT Roles based on User ID. If the User ID is invalid, an empty list will be returned.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- userId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/users/`{UserId}`/directRoles |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/users/`{UserId}`/directRoles |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description                                 | M/O | Type   |
|-----------|---------------------------------------------|-----|--------|
| userId    | Provide a valid user ID for the request URL | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description                   | Type   |
|-----------|-------------------------------|--------|
| user_id   | User ID of the AOT user       | String |
| RoleId    | Role ID of the AOT user roles | String |

### Sample JSON Response

`{`

"`\<`user_id`\>`": [

`{`

"RoleId": ""

`}`,

`{`

"RoleId": ""

`}`

\]

`}`

### Result

| HTTP Code | Result Description                         |
|-----------|--------------------------------------------|
| 200       | The list of AOT Roles based on the User ID |

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
Unauthorized User / `{Header Token}` could be missing
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

## GET- GetUserAdGroupMappings

This API is used to fetch a list of AD Groups from the Active directory based on User ID.

### API Precondition

To fetch the response from the APIs, the following entities must exist.

- Authorization token

- userId

| PROTOCOL | HTTPS |
|----|----|
| PATH AOT (Cognite)`\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/people-management/user/`{UserId}`/groups |
| PATH AOT (Azure)`\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/people-management/user/`{UserId}`/groups |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header Parameters

| Parameter | Description | M/O | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |

### Input Path Parameters

| Parameter | Description                                 | M/O | Type   |
|-----------|---------------------------------------------|-----|--------|
| userId    | Provide a valid user ID for the request URL | M   | String |

### Output Header Parameters

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body Parameters

| Parameter | Description               | Type   |
|-----------|---------------------------|--------|
| user_id   | User ID of the AOT user   | String |
| GroupId   | Object ID of the AD Group | String |

### Sample JSON Response

`{`

"`\<`user_id`\>`": [

`{`

"GroupId": ""

`}`,

`{`

"GroupId": ""

`}`

\]

`}`

### Result

| **HTTP Code** | **Result Description**             |
|---------------|------------------------------------|
| 200           | List of AD Groups based on User ID |

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
Unauthorized User / `{Header Token}` could be missing
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

# 

## POST- Azure Web PubSub

This API is used to send messages to a list of users, groups, or all users using Azure Web PubSub Service based on the request body. Azure Web PubSub is an internal API, as it is used only by the backend of an AOT application and is not exposed to end users.

### API Precondition

To fetch the response from the APIs, the following entities must exist:

- Authorization token

- Request body

| PROTOCOL | HTTPS                                               |
|----------|-----------------------------------------------------|
| PATH     |  |
| METHOD   | POST                                                |

### Input Header Parameters

| Parameter | Description | M/O |
|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M |

### Input Body Parameters







``

``
Parameter
Description
M/O
Type
``
``

``
hub
Provide a name for the hub that will be used for web pub sub-client connections.
M
String
``
``
sendTo
`Provide the receiver type to whom the message should be sent. Available options are as follows:`

User
Group
All
``
M
String
``
``
userId
Provide a list of user IDs whenever the sendTo parameter is set to “User”
M
String
``
``
groupId
Provide a list of group IDs whenever the sendTo parameter is set to “Group”
M
String
``
``
message
`Provide the message that should be sent to`
a list of users, groups, or all users.
M
String/JSON
``
``
``

### Sample JSON Request

The following is the request body to send a message to one or more users.

`{`

"hub”: “”,

“sendTo”:”User”,

“userId”: \[\],

“message”: `{`}

`}`

The following is the request body to send a message to one or more Groups.

`{`

"hub”: “”,

“sendTo”:”Group”,

“groupId”: \[\],

“message”:`{`}

`}`

The following is the request body to send a message to All users.

`{`

"hub”: “”,

“sendTo”:”All”,

“message”: `{`}

`}`

### Sample Response

`{"message”: “Successfully published the message"}`

### Result

| **HTTP Code** | **Result Description**    |
|---------------|---------------------------|
| 200           | Message sent successfully |

### Error Management






``

``
HTTP Code
Error Code
Error Description
``
``

``
401
401
``
Unauthorized User / `{Header Token}` could be missing, expired, or invalid
``
``
``
400
400
``
Bad request / Invalid Request Body
``
``
``
``
