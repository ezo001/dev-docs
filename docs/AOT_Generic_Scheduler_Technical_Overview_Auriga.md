---
id: aot-generic-scheduler-technical-overview-auriga
title: AOT Generic Scheduler Technical Overview Auriga
---

**Accenture Operations Twin**

**Generic Scheduler**

**TECHNICAL OVERVIEW**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin / Generic Scheduler |
| **Domain / Area** | Digital Twin / |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Ranganathan, Balamurugan |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | AOT Getting Started, AOT Architecture Blueprint |

**Contents**

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Repository [3](#repository)](#repository)

[Technology Stack [3](#technology-stack)](#technology-stack)

[Glossary [4](#glossary)](#glossary)

[Generic Scheduler Architecture [5](#generic-scheduler-architecture)](#generic-scheduler-architecture)

[Diagram [5](#diagram)](#diagram)

[Key [5](#key)](#key)

[Scheduling Expressions [6](#scheduling-expressions)](#scheduling-expressions)

[Cron [6](#cron)](#cron)

[Interval [6](#interval)](#interval)

[Date [6](#date)](#date)

[APIs [7](#apis)](#apis)

[GET – Get_Task [8](#get-get_task)](#get-get_task)

[GET – Get_Task_Details [9](#get-get_task_details)](#get-get_task_details)

[POST – Register_Task [10](#post-register_task)](#post-register_task)

[PUT – Update_Task [11](#put-update_task)](#put-update_task)

[DELETE – Delete_Task [12](#delete-delete_task)](#delete-delete_task)

[GET – GetJobDetails [13](#get-getjobdetails)](#get-getjobdetails)

[Kafka Message Broker [14](#kafka-message-broker)](#kafka-message-broker)

[Sample Message [14](#sample-message)](#sample-message)

[Database Tables [15](#database-tables)](#database-tables)

[Deployment [16](#deployment)](#deployment)

[Use Case Scheduling SmartKPIs [16](#use-case-scheduling-smartkpis)](#use-case-scheduling-smartkpis)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The Generic Scheduler Microservice is a service designed to facilitate task scheduling. It allows users to schedule tasks for execution at specific intervals or on specific dates. As a part of AOT, it is utilized by other AOT components, mainly Smart KPIs and Intelligent Advisor, to schedule tasks such as performing KPI calculations and generating insights.

## Purpose

This document provides parameters and examples for integrating, configuring, and deploying AOT’s Generic Scheduler in an application.

## Target Audience

- Developers

- Application Architects

- DevOps Engineers

## Prerequisites

- JSON file with attributes to create asset hierarchy

- Python SDK file as function code

- If deployed on CDF, access to the [CDF portal](https://fusion.cognite.com/accenture-operations-twin)

- Access to the [GIT repository](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_git/MarilynVPlatform)

## Contacts

- ``

- ``

## Related Links

- [AOT IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

- [Cognite Documentation](https://developer.cognite.com/)

## Repository

- Git branch name: feature/generic-scheduler-service

- Git folder path: Git -\`\>` Repos -\`\>` Files -\`\>` Common -\`\>` GenericSchedulerService

- Git folder link:  
  [MarilynVPlatform - Repos (azure.com)](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_git/MarilynVPlatform)

## Technology Stack

- SqlAlchemy 1.4.18

- Flask 2.2

- Flask-Migrate 3.1.0

- flask-sqlalchemy 3.0.2

- Flask-RESTful 0.3.9

- Pandas 1.4.3

- Requests 2.28.1

- azure-digitaltwins-core 1.2.0

- azure-identity 1.10.0

- azure-kusto-data 4.0.2

- pyodbc

- APScheduler

- confluent-kafka

## 

## Glossary

| **Term** | **Definition** |
|:---|:---|
| AOT (Accenture Operations Twin) | A collection of software accelerators and tools designed to integrate product, process, and live data from disparate IT and OT systems, providing a contextualized view of operations for better decision-making. |
| Generic Scheduler | A microservice within AOT that enables scheduling of tasks at specific intervals or dates, used by other AOT components like Smart KPIs and Intelligent Advisor for automated operations. |
| CRUD Operations | Refers to Create, Read, Update, and Delete operations that can be performed on scheduled tasks via the Generic Scheduler APIs. |
| APIM (API Management) | Acts as an API gateway, controlling access to the Generic Scheduler's APIs and managing authentication and authorization. |
| AKS Cluster | Azure Kubernetes Service cluster that hosts the Generic Scheduler and related services, activating scheduler jobs and maintaining logs. |
| Kafka Message Broker | A messaging system used to publish events triggered by the Generic Scheduler, allowing consumers to subscribe and process these events. |
| Scheduling Expression | Defines when and how often a task should be triggered. Supported types include Cron, Interval, and Date expressions. |
| Cron Expression | A scheduling format using minute, hour, day of month, month, and day of week fields to specify recurring task triggers. |
| Interval Expression | Specifies regular time intervals (days, hours, minutes, seconds, weeks) between task triggers, with optional start and end dates. |
| Date Expression | Triggers a task only once at a specified date and time. |
| Smart KPIs | Key Performance Indicators managed and scheduled by the Generic Scheduler, often involving hierarchical relationships and automated calculations. |
| Task | An individual scheduled operation managed by the Generic Scheduler, identified by a unique task ID and associated parameters. |
| Asset Hierarchy | The structured organization of assets (e.g., plants, equipment) used for mapping and scheduling KPIs within AOT. |
| API (Application Programming Interface) | Set of endpoints provided by the Generic Scheduler for managing tasks, including GET, POST, PUT, DELETE operations. |

# 

# Generic Scheduler Architecture 

The Generic Scheduler system architecture is diagrammed below and describes the Generic Scheduler which performs CRUD operations (Create, Read, Update, Delete) on tasks. The front end and Postman are used to interact with the scheduler. The system architecture includes several components, such as APIM, AKS Cluster, Azure SQL Server Database, Azure Kafka Topic Broker, and Storage Resources.

## Diagram



## Key





``

``
Component
Description
``
``

``
Frontend/ Postman
Provides a user interface to interact with the Generic Scheduler. Users can perform CRUD operations on tasks through this interface.
``
``
Generic Scheduler
Handles the management of tasks and exposes APIs for CRUD operations.
``
``
APIM
Acts as an API gateway, controlling access to the Generic Scheduler's APIs and managing authentication and authorization.
``
``
AKS Cluster
Hosts the Generic Scheduler and related services. It activates all scheduler jobs and maintains scheduler logs.
``
``
Kafka Message Topic
A Kafka message topic is utilized to publish events (PUSH events) triggered by the Generic Scheduler. Consumers can subscribe to these events and process them.
``
``
Storage Resources
`This component contains two main parts:`

Azure SQL Server Database: Stores and manages information related to scheduler operations. This includes CRUD scheduler operations and trigger job history.
Azure Kafka Topic Broker (Consumers): Acts as a message broker for Kafka topics. It allows consumers to subscribe and receive events pushed by the Generic Scheduler.
``
``
``
``

# 

# Scheduling Expressions

Three types of scheduling expressions are supported by the Generic Scheduler: Cron, Interval, and Date.

## Cron

- Cron expressions are used to schedule tasks based on a pattern of time and date fields.

- The expression consists of five fields representing minute, hour, day of the month, month, and day of the week, respectively.

- Asterisks (\*) in a field mean "any" and can be used to represent all possible values.

- Ranges can be specified using hyphens (-) and multiple values separated by commas (,).

- Forward slashes (/) can be used to define intervals.

This example cron expression triggers the task every minute, indefinitely.

`\>` \`"scheduling_exp": `{`
`\>`
`\>` "type": "cron",
`\>`
`\>` "value": `{`
`\>`
`\>` "expression": "\*/1 \* \* \* \*"
`\>`
`\>` `}`
`\>`
`\>` `}`

## Interval 

- Interval expressions trigger tasks at regular time intervals.

- The expression includes fields for specifying the number of days, hours, minutes, seconds, and weeks between task triggers.

- The start and end dates- are not mandatory, if not provided the task will be triggered infinitely after adding the job, the first trigger will occur after the interval time has elapsed from the time of adding the job, for instant trigger “instant_trigger” can be set to True.

- If start_date and end_date are given, the task will trigger for the first time at the time of start_date and will keep on triggering till the end \_date provided.

This example interval expression triggers the task every 3 minutes, starting from July 6, 2023, at 14:45:00, and continues indefinitely.

`\>` \`"scheduling_exp": `{`
`\>`
`\>` "type": "interval",
`\>`
`\>` "instant_trigger": true,
`\>`
`\>` "value": `{`
`\>`
`\>` "days": 0,
`\>`
`\>` "hours": 0,
`\>`
`\>` "minutes": 3,
`\>`
`\>` "seconds": 0,
`\>`
`\>` "start_date": "2023-07-06 14:45:00",
`\>`
`\>` "end_date": "2024-07-06 14:45:00",
`\>`
`\>` "weeks": 0
`\>`
`\>` `}`
`\>`
`\>` `}`\`

## Date 

- Date expressions trigger a task only once at a specified date and time.

- Unlike the previous two types, date expressions do not repeat.

This example date expression triggers the task on August 15, 2023, at 12:00:00, and it won't repeat.

`\>` \`"scheduling_exp": `{`
`\>`
`\>` "type": "date",
`\>`
`\>` "value": `{`
`\>`
`\>` "date": "2023-08-15 12:00:00"
`\>`
`\>` `}`
`\>`
`\>` `}`\`

# 

# APIs

The AOT-Generic-Scheduler microservice provides a set of APIs to manage these tasks efficiently.

| API | Description |
|----|----|
| GET – Get_Task | This API retrieves a complete list of scheduled tasks. |
| GET – Get_Task_Details | This API obtains detailed information about a specific task using its ID. |
| POST – Register_Task | This API inserts new tasks into the database with essential parameters. |
| PUT – Update_Task | This API updates existing tasks with the required modifications. |
| DELETE – Delete_Task | This API removes tasks from the main table and archives them in the 'scheduled_tasks_log' table. |
| GET – GetJobDetails | This API fetches the data based on the scheduler name provided in the parameters query. |

These APIs are specified in the subsequent sections.

In the API parameter descriptions, the M/O column heading stands for Mandatory / Optional.

## GET – Get_Task

The Get_Task API is part of the AOT-Generic-Scheduler microservice. This microservice is a GET call to the AOT server hosted at the back end to get the full list of tasks.

### Specification

| PROTOCOL | HTTPS |
|:---|----|
| PATH `\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/genericscheduler/scheduler/tasks |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header

| Parameter | Description | M/O\* | Type |
|----|:---|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Output Header






``

``
Parameter
Description
Type
``
``

``
Server
`Contains information about how the server handles requests`
[e.g., Werkzeug/2.1.2 Python/3.9.7]
String
``
``
Content-Type
Length of the content
String
``
``
Date
Date of operation execution e.g. - [Tue, 17 May 2022 06:30:16 GMT]
Datetime
``
``
Content-Length
Length of the content
Bytes
``
``
``

### Output Body

| Parameter | Description | Type |
|----|----|----|
| creation_date | Task creation date | String |
| mod_date | Task modification date | String |
| name | Distinct name of the task | String |
| parameters | parameters as user requirement | String |
| scheduling_exp/type | Scheduler task type | String |
| scheduling_exp/value | Value of scheduling expression based on its type | String |
| scope | Scope in the message to the message broker | String |
| task_id | The distinct ID of the task | String |

### Result

| **HTTP Code** | **Result Description** |
|---------------|------------------------|
| 200           | successful operation   |

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
Invalid Data
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

### Sample JSON Response

\[

`{`

"creation_date": "Mon, 17 Jul 2023 11:53:48 GMT",

"mod_date": "Wed, 26 Jul 2023 18:41:51 GMT",

"name": "cron1",

"parameters": `{`

"Task_Name": "X-Y",

"Task_No": "123",

"Task_Time": "11:11:11"

`}`

\]

## 

## GET – Get_Task_Details 

The Get_Task_Details API is part of the AOT-Generic-Scheduler microservice. This microservice is a GET call to the AOT server hosted at the back end to get details of tasks based on task ID.

### Specification

| PROTOCOL | HTTPS |
|----|----|
| PATH `\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/genericscheduler /scheduler/tasks/`\<`int:task_id`\>` |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |
| task_id | Distinct id of task. | M | String |

### Output Header

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body

| Parameter | Description | Type |
|----|----|----|
| creation_date | Task creation date | String |
| mod_date | Task modification date | String |
| name | Distinct name of the task | String |
| parameters | Parameters as user requirement | String |
| scheduling_exp/type | Scheduler task type | String |
| scheduling_exp/value/expression | Value of scheduling expression based on its type | String |
| scope | Scope in the message to the message broker | String |
| task_id | Distinct id of task. | String |

### Result

| HTTP Code | Result Description   |
|-----------|----------------------|
| 200       | successful operation |

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
Invalid Data
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

**Sample Request**

Query Parameter: task_id (example, here task_id = 68)

Request URL: `\<`https://apim-aot-mw-dev.azure-api.net/api/genericscheduler/scheduler/tasks/68`\>`

**Sample JSON Response**

`{`

    "creation_date": "Mon, 17 Jul 2023 11:53:48 GMT",

    "mod_date": "Wed, 26 Jul 2023 18:41:51 GMT",

    "name": "cron1",

    "parameters": `{`

        "Task_Name": "X-Y",

        "Task_No": "123",

        "Task_Time": "11:11:11"

    `}`,

    "scheduling_exp": `{`

        "type": "cron",

        "value": `{`

            "expression": "\*/1 \* \* \* \*"

        `}`

    `}`,

    "scope": "newscope",

    "task_id": 68

`}`

## 

## POST – Register_Task

The Register_Task API is part of the AOT-Generic-Scheduler microservice. This microservice is a POST call to the AOT server hosted at the back end to store a list of tasks in DB.

### Specification

| PROTOCOL | HTTPS |
|----|----|
| PATH  |
| METHOD | POST |
| CONTENT TYPE | application / json |

### Input Header

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body

| Parameter | Description | M/O | Type |
|----|----|----|----|
| name | Distinct name of the task | M | String |
| scope | Scope in the message to the message broker | M | String |
| scheduling_exp/type | Scheduler Task type | M | String |
| scheduling_exp/value | Value of scheduling expression based on its type | M | String |
| scheduling_exp/ instant_trigger | Flag for instant trigger functionality | O | Boolean |
| description | Description as per user requirement | M | String |
| parameters | Parameters as user requirement | M | String |

### Output Header






``

``
Parameter
Description
Type
``
``

``
Server
`Contains information about how the server handles requests`
[e.g., Werkzeug/2.1.2 Python/3.9.7]
String
``
``
Content-Type
Length of the content
String
``
``
Date
Date of operation execution e.g. - [Tue, 17 May 2022 06:30:16 GMT]
Datetime
``
``
Content-Length
Length of the content
Bytes
``
``
``

### Output Body

| Parameter | Description | Type |
|----|----|----|
| task_id | Task ID is a unique ID that is generated inside the SQL table and is assigned to the registered task. | String |

### Result

| HTTP Code | Result Description   |
|-----------|----------------------|
| 200       | successful operation |

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
Invalid Data
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

### 

### Sample JSON Request

`{`

"name": "interval1",

"scope": "development",

"scheduling_exp": `{`

"type": "interval",

"instant_trigger": true,

"value": `{`

"weeks": 0,

"days": 0,

"hours": 0,

"minutes": 1,

"seconds": 0

`}`

`}`,

"description": "created config",

"parameters": `{`

"frequency": `{`

"value": 5,

"unit": "Hour"

`}`,

"asset": \[

`{`

"assetId": "C-B1-G1-R2-F1-P-PP-U1-EGCA-GT",

"assetName": "C-B1-G1-R2-F1-P-PP-U1-EGCA-GT",

"plantId": "C-B1-G1-R2-F1",

"plantName": "C-B1-G1-R2-F1"

`}`

\]

`}`

`}`

###  Sample JSON Response

`{`

"task_id": 92

`}`

## 

## 

## PUT – Update_Task

The Update_Task API makes a PUT call to the AOT server hosted at the back end to update an existing task in the Generic Scheduler.

### Specification

| PROTOCOL | HTTPS |
|----|----|
| PATH  |
| METHOD | PUT |
| CONTENT TYPE | application / json |

### Input Header

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Body

| Parameter | Description | M/O | Type |
|----|----|----|----|
| name | Distinct name of the task | M | String |
| task_id | Distinct id of task. | M | String |
| scope | Scope in the message to the message broker | M | String |
| scheduling_exp/type | Scheduler Task type | M | String |
| scheduling_exp/value | Value of scheduling expression based on its type  | M | String |
| scheduling_exp/ instant_trigger | Flag for instant trigger functionality | O | Boolean |
| description | Description as per user requirement | M | String |
| parameters | Parameters as user requirement | M | String |

### Output Header

| Parameter | Description | Type |
|----|:---|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body

| Parameter | Description | Type |
|----|----|----|
| creation_date | Task creation date | String |
| mod_date | Task modification date | String |
| name | Distinct name of the task | String |
| parameters/Task_Name | Parameters as user requirement | String |
| scheduling_exp/type | Scheduler Task type | String |
| scheduling_exp/value | Value of scheduling expression based on its type  | String |
| scope | Scope in the message to the messagebroker | String |
| task_id | The distinct ID of the task | String |

### Result

| HTTP Code | Result Description   |
|-----------|----------------------|
| 200       | successful operation |

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
Invalid Data
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

### 

### Sample JSON Request

`{`

"task_id": 1,

"name": "interval1",

"scope": "testing",

"scheduling_exp": `{`

"type": "interval",

"instant_trigger": true,

"value": `{`

"weeks": 0,

"days": 0,

"hours": 0,

"minutes": 0,

"seconds": 50

`}`

`}`,

"description": "Testing pre fail",

"parameters": `{`

"frequency": `{`

"unit": "Day",

"value": "5"

`}`,

"asset": \[

`{`

"assetId": "C-B1-G1-R2-F1-P-PP-U1-EGCA-GT",

"assetName": "C-B1-G1-R2-F1-P-PP-U1-EGCA-GT",

"plantId": "C-B1-G1-R2-F1",

"plantName": "C-B1-G1-R2-F1"

`}`

\]

`}`

`}`

###  Response

"creation_date": "Wed, 26 Jul 2023 14:25:21 GMT",

"mod_date": "Wed, 26 Jul 2023 15:17:07 GMT",

"name": "tasknamenewdate",

"parameters": `{`

"Task_Name": "X-Y",

"Task_No": "123",

"Task_Time": "11:11:11"

`}`,

"scheduling_exp": `{`

"type": "date",

"value": "2023-07-26 15:20:00"

`}`,

"scope": "scope",

"task_id": 92`}`

## 

## 

## DELETE – Delete_Task

The Delete_Task API is part of the AOT-Generic-Scheduler microservice. This microservice is a DELETE call to the AOT server hosted at the back end to delete tasks based on task ID.

### Specification

| PROTOCOL | HTTPS |
|:---|----|
| PATH `\<`Public Exposure`\>` | https://apim-mw-aot-dev.azure-api.net/api/genericscheduler /scheduler/tasks/`\<`int:task_id`\>` |
| METHOD | DELETE |
| CONTENT TYPE | application / json |

### Input Header

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |
| task-id | Distinct id of task. | M | String |

### Output Header






``

``
Parameter
Description
Type
``
``

``
Server
`Contains information about how the server handles requests`
[e.g., Werkzeug/2.1.2 Python/3.9.7]
String
``
``
Content-Type
Length of the content
String
``
``
Date
Date of operation execution e.g. - [Tue, 17 May 2022 06:30:16 GMT]
Datetime
``
``
Content-Length
Length of the content
Bytes
``
``
``

### Output Body

| Parameter | Description | Type |
|----|----|----|
| message | Status of the delete request along with the task ID of the task the user wants to delete. | String |

### Result

| HTTP Code | Result Description   |
|-----------|----------------------|
| 200       | successful operation |

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
Invalid Data
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

### Sample JSON Response

`{`

"message": "`{'TaskID': 104, 'Status': 'Deleted Successfully'}`"

`}`

## GET – GetJobDetails

The GetJobDetails API is part of the AOT-Generic-Scheduler microservice and is a GET call for fetching the data based on the scheduler name provided in the parameters query.

### Specification

| PROTOCOL | HTTPS |
|:---|----|
| PATH `\<`Public Exposure`\>` | https://apim-aot-azure-dev.azure-api.net/api/genericscheduler/scheduler/jobs |
| METHOD | GET |
| CONTENT TYPE | application / json |

### Input Header

| Parameter | Description | M/O\* | Type |
|----|----|----|----|
| Authorization | Token acquired from Azure AD based on the user credentials for further API calls. | M | String |
| Content-Type | Length of content. E.g.- application/json | M | String |

### Input Query

| Parameter | Description   | M/O\* | Type   |
|-----------|---------------|-------|--------|
| names     | List of names | M     | String |

### Output Header

| Parameter | Description | Type |
|----|----|----|
| Server | Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\] | String |
| Content-Type | Length of the content | String |
| Date | Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\] | Datetime |
| Content-Length | Length of the content | Bytes |

### Output Body

| Parameter           | Description                                | Type    |
|---------------------|--------------------------------------------|---------|
| name/creation_date  | Task creation date                         | String  |
| name/mod_date       | Task modification date                     | String  |
| name/name           | Distinct name of the task                  | String  |
| name/parameters     | Parameters are user requirement            | Object  |
| name/scheduling_exp | Scheduling expressions parameters          | Object  |
| name/scope          | Scope in the message to the message broker | String  |
| name/task_id        | Distinct id of task.                       | Integer |

### Result

| HTTP Code | Result Description   |
|-----------|----------------------|
| 200       | successful operation |

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
Invalid Data
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
404
404
``
Bad request
``
``
``
``

### Sample JSON Response

`{`

"b49947bf-b940-45e1-b5a1-1dbb0f5ca581": `{`

"creation_date": "Thu, 18 Jan 2024 12:10:46 GMT",

"mod_date": "Thu, 18 Jan 2024 12:10:46 GMT",

"name": "b49947bf-b940-45e1-b5a1-1dbb0f5ca581",

"parameters": `{`

"Attribute": "Actual",

"Level": "Level 4",

"PlantName": "C-B1-G1-R1-F1",

"Status": "Initiated",

"kpi_config_id": "b49947bf-b940-45e1-b5a1-1dbb0f5ca581",

"kpiname": "Availability",

"timestamp": "2024-01-18 12:10:00",

"uid": "0b2aa317-44fa-4630-b915-a4e7d6e8ceb1"

`}`,

"scheduling_exp": `{`

"type": "interval",

"value": `{`

"days": 0,

"hours": 0,

"minutes": 5,

"seconds": 0,

"weeks": 0

`}`

`}`,

"scope": "Smart KPI Orchestration",

"task_id": 93

`}`

`}`

# 

# Kafka Message Broker

The Generic Scheduler Service is configured to send events to a designated Kafka Server and Topic. The Kafka Server receives the data and routes it to the appropriate Topic where the events can be consumed by downstream applications and services for further processing.

## Sample Message

`{`

"Type": "Add",

"Scopes": "Smart KPI Orchestration",

"Timestamp": "2024-01-09 08: 55: 52",

"Version": "1",

"Payload": \[

`{`

"creation_date": "Thu,04 Jan 2024 08: 15: 52 GMT",

"mod_date": "Thu,04 Jan 2024 08: 15: 52 GMT",

"name": "b49947bf-b940-45e1-b5a1-1dbb0f5ca581",

"parameters": `{`

"Attribute": "Actual",

"Level": "Level 4",

"PlantName": "C-B1-G1-R1-F1",

"Status": "Initiated",

"kpi_config_id": "b49947bf-b940-45e1-b5a1-1dbb0f5ca581",

"kpiname": "Availability",

"timestamp": "2023-01-04 08: 15: 00",

"uid": "0b2aa317-44fa-4630-b915-a4e7d6e8ceb1"

`}`,

"scheduling_exp": `{`

"type": "interval",

"value": `{`

"days": 0,

"hours": 0,

"minutes": 5,

"seconds": 0,

"weeks": 0

`}`

`}`,

"scope": "Smart KPI Orchestration",

"task_id": 4

`}`

\]

`}`

# 

# Database Tables

The Generic Scheduler uses the following tables from the "sql-scheduler-db” to manage scheduled tasks.

| Table | Description | Example |
|----|----|:--:|
| scheduled_tasks | This table stores information about currently active/running tasks (jobs). When a user registers a task (by calling the Register_Task API), the details of that task are stored in this table. | [Link](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Generic%20Scheduler/2.0/AOT_Generic_Scheduler_Tasks.xlsx?d=w303e1b15168b4a27b6b74048f4722a19&csf=1&web=1&e=sYoiah) |
| scheduled_tasks_log | This table stores information about deleted jobs (previously scheduled tasks that have been deleted). When a user deletes a task (by calling the Delete_Task API), the details of that task are moved from "scheduled_tasks" table to this table. In addition, the "state" property is marked as "DELETED". | [Link](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Generic%20Scheduler/2.0/AOT_Generic_Scheduler_Tasks_Log.xlsx?d=wc674a6b69e1f4411b7cb7c75fb1fc93e&csf=1&web=1&e=jViFPB) |
| scheduled_tasks_history | This table stores a history of events corresponding to task triggers. Whenever a task is triggered by the Generic Scheduler Service, a row of records is added to this table, describing task details and trigger time. | [Link](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Generic%20Scheduler/2.0/AOT_Generic_Scheduler_Tasks_History.xlsx?d=w32aa923f84c2488ea5378dccf7b0ca8f&csf=1&web=1&e=BUxm5l) |

# 

# Deployment

To deploy the generic scheduler application:

1.  Create a feature branch and clone the repo.

2.  Git clone "branch url"

3.  Make the necessary changes in the featured branch and commit the change.

4.  git add . or \[file name\]

5.  git commit -m "provide details about changes"

6.  Raise PR to merge the code to the destination branch \[main branch\].

7.  Run the pipeline manually.

8.  Check the status of deployment on the DevOps Azure portal.

## Use Case Scheduling SmartKPIs

The Generic Scheduler Microservice can be used as follows to create and update schedules for SmartKPIs:

1.  The KPI Hierarchy Processing component identifies low-level KPIs by analyzing contributing relationships within the KPI hierarchy and filtering out those that are only parameter-dependent.

2.  For each identified low-level KPI, a scheduling expression is calculated. This expression defines when and how often the KPI should be calculated.

3.  The calculated scheduling expressions are converted into a format that is compatible with the Generic Scheduler API.

4.  The component interacts with the Generic Scheduler API to create schedules for the identified low-level KPIs. It handles creating new schedules, updating existing ones, or archiving obsolete ones.

The use case is further described in the context of creating and updating schedules in the subsequent sections.

### Create

Consider the example of the KPI ‘Availability’, whose Asset hierarchy level mapping is Level 4.

- The KPI Calculation (Actual) formula is = (SK.latest('Run Hours','%') / SK.latest('Available Hours','%')) \* 100

- Identifying Low-Level KPIs: The component identifies low-level KPIs by analyzing Contributing relationships within the KPI hierarchy and filtering out those that are only parameter-dependent.

- Scheduling Expression Calculation: For each identified low-level KPI, a scheduling expression is calculated. This expression defines when and how often the KPI should be calculated.

- Converting to Scheduler Format: The calculated scheduling expressions are converted into a format that is compatible with the Generic Scheduler API.

- Creating Schedules: The component interacts with the Generic Scheduler API to create schedules for the identified low-level KPIs. It handles creating new schedules, updating existing ones, or archiving obsolete ones.

### Update

- After schedules are successfully created, the component updates the status of the corresponding KPIs. Lower-level KPIs are updated to "Published," and the status of upper-level KPIs is updated based on the completion of their contributing lower-level KPIs.

- The component also handles multi-plant scenarios where KPIs are aggregated across multiple plants. It ensures that the statuses of multi-plant KPIs are appropriately updated based on the statuses of their contributing plant-level KPIs.
