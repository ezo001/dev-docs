---
id: aot-parameter-function-overview-auriga
title: AOT Parameter Function Overview Auriga
---

**ACCENTURE OPERATIONS TWIN**

**Parameter Function App**

**TECHNICAL OVERVIEW**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin / Parameter Function App |
| **Domain / Area** | Azure Digital Twin / Asset Management |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Gali, Hanuman |
| **Status** | Draft / In Progress |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Operations Hierarchy Deployment Guide, Operations Hierarchy UI Guide |

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Technology Stack [3](#technology-stack)](#technology-stack)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Parameter Function Architecture [4](#parameter-function-architecture)](#parameter-function-architecture)

[Data Flow [4](#data-flow)](#data-flow)

[Flow Diagram [4](#flow-diagram)](#flow-diagram)

[Azure Function App Logic [5](#azure-function-app-logic)](#azure-function-app-logic)

[Processing Incoming Telemetry Data [5](#processing-incoming-telemetry-data)](#processing-incoming-telemetry-data)

[Interfacing with Azure Digital Twins [5](#interfacing-with-azure-digital-twins)](#interfacing-with-azure-digital-twins)

[Caching Mechanism [5](#caching-mechanism)](#caching-mechanism)

[Error Handling and Logging [5](#error-handling-and-logging)](#error-handling-and-logging)

[Environment Variables [6](#environment-variables)](#environment-variables)

[Core Modules and Libraries [7](#core-modules-and-libraries)](#core-modules-and-libraries)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT’s Parameter Azure Function App is designed to process time telemetry data, interact with Azure Digital Twins (ADT), and maintain a synchronized state within ADT based on incoming events. It features capabilities to create, update, and manage digital twins and their relationships.

## Purpose

This document describes how parameters are created and updated in Azure Digital Twins (ADT) by the Parameter Function App. The target audience can utilize this information to efficiently manage and customize their ADT instances.

## Target Audience

- Developers

- Application Architects

## Prerequisites

- Azure subscription with access to Azure Digital Twins and Function Apps

- Python 3.7 or later

- Required Python packages include azure-functions, azure.core.exceptions, azure.digitaltwins.core, azure.identity, os, pandas, itertools, threading, datetime

## Technology Stack

| **Tools** | **Repository** |
|----|----|
| Azure Functions | Python library to write code for Azure Functions. |
| Azure Digital Twins Client | SDK to access Azure Digital Twins service. |

##  Contacts

- ``

- ``

- ``

## Related Links

- [AOT IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| **Term** | **Definition** |
|:---|:---|
| AOT (Accenture Operations Twin) | A collection of software accelerators and tools that integrate product, process, and live data from IT and OT systems to create a contextualized view of operations for better decision-making. |
| Azure Digital Twin (ADT) | A cloud-based service for creating digital representations of real-world entities and their relationships. |
| Azure IoT Hub | The ingestion point for device data, acting as a conduit to Azure Stream Analytics. |
| Azure Stream Analytics | Processes incoming telemetry data and forwards it to the Azure Function App. |
| Azure Function App | A serverless compute service that processes data, interacts with Azure Digital Twins, and manages digital twin relationships. |
| Cache System | A mechanism within the Function App to temporarily store processed data, optimizing performance and reducing load on Azure Digital Twins. |
| Telemetry Data | Data collected from IoT devices, typically including measurements, identifiers, and state information. |
| Azure API Management (APIM) | A service for managing APIs securely and at scale. |
| Azure Kubernetes Service (AKS) | A managed Kubernetes container orchestration service. |
| Azure Data Explorer (ADX) | A fast and highly scalable data analytics service for large volumes of data. |
| Digital Twins Client SDK | Software development kit for interacting with Azure Digital Twins. |
| Application Insights | Azure service for monitoring application performance and logging errors. |
| Thread Lock Mechanism | A concurrency control technique ensuring thread-safe operations in the cache. |
| Exception Blocks | Code structures used to capture and handle errors during execution. |
| Simulator | The source of telemetry data sent to Azure IoT Hub. |

# 

# 

# Parameter Function Architecture

This section introduces the architecture of Accenture’s Parameter Azure Function application, which has been designed for real-time telemetry processing with Azure Digital Twins. It provides an end-to-end view of how telemetry data from IoT devices is ingested, processed, and managed within Azure Digital Twins through the Function App.

## 

## Data Flow

1.  Data is sent from the simulator to Azure IoT Hub.

2.  Azure Stream Analytics picks up the data and applies any necessary transformations.

3.  The processed data is sent to the Azure Function App.

4.  The Azure Function App parses the data, performs logic, and interacts with Azure Digital Twins to create or update digital twins and their relationships.

##  Flow Diagram



| **Component** | **Description** |
|:---|----|
| Simulator | The source of telemetry data that is sent to Azure IoT Hub. |
| Azure IoT Hub | The ingestion points for device data and the conduit to Azure Stream Analytics. |
| Azure Stream Analytics | Processes incoming data and forwards it to the Azure Function App. |
| Azure Function App | The central focus of this architecture, which receives processed data, interacts with Azure Digital Twins to synchronize digital twin states and manage twin relationships. |
| Azure Digital Twins | The ADT instance where the digital twins are stored, updated, and managed based on the telemetry data. |
| Cache System | A caching mechanism within the Function App to optimize performance and reduce load on Azure Digital Twins. |

# 

# Azure Function App Logic

The Azure Function App operates for our real-time data processing and digital twin synchronization system. The core operational functions are described below.

## 

## Processing Incoming Telemetry Data

The Function App is triggered by HTTP requests, each carrying a payload of telemetry data from Azure Stream Analytics. The data is in JSON format. The Function App parses this payload and processes each item, extracting key information such as the device's unique identifiers, measurements, and state information.

## Interfacing with Azure Digital Twins

Upon processing the data, the Function App interacts with Azure Digital Twins using the Digital Twins Client SDK. The processed data is mapped to the digital twin's model, updating properties. The script supports creating new digital twins if they do not exist or updating existing twins.

## Caching Mechanism

To enhance performance, the Function App implements a caching mechanism. It temporarily stores processed data in memory, reducing the number of outbound calls to Azure Digital Twins. This cache is beneficial in scenarios with frequent or repetitive data points. A thread lock mechanism ensures that cache operations are thread-safe, allowing the Function App to handle concurrent requests without data corruption or performance bottlenecks.

## Error Handling and Logging 

Exception blocks are used to capture and handle errors that may occur during data processing, digital twin synchronization, or interactions with external services. Logging is an integral part of this, where each significant action and error is logged, providing transparency, and aiding in debugging and monitoring. The logs can be streamed to Azure Monitor or Application Insights for real-time analysis and alerting.



# Environment Variables

| Name | Description |
|----|----|
| ADXDatabaseName | The name of the Azure Data Explorer (ADX) database where your data will be stored. |
| ADXTable | The specific table within the ADX database that your Function App will interact with. |
| APPINSIGHTS_INSTRUMENTATIONKEY | The instrumentation key for Azure Application Insight. It is used for monitoring the performance of your application. |
| AZURE_CLIENT_ID | The Application (client) ID of an Azure Active Directory application. It's used for identity and access control within your application, particularly when interacting with Azure services that support Azure AD authentication. |
| AZURE_CLIENT_SECRET | The secret key for the Azure AD application. It's used in conjunction with the AZURE_CLIENT_ID to authenticate to Azure services. |
| AZURE_TENANT_ID | The directory tenant ID that the Azure AD application belongs to. This is used to specify the Azure AD instance your Function App is registered with. |
| AZURE_URL | The URL endpoint for your Azure Digital Twins service instance. It is used to send requests to manage your digital twins. |
| AzureWebJobsStorage | The connection string to the Azure storage account. It is used by the Azure Function App for operations such as managing triggers and logging runtime data. |
| ClusterURI | The URI of the Azure Data Explorer cluster that is connected. |
| FUNCTIONS_EXTENSION_VERSION | Specifies the version of the Azure Functions runtime to use. |
| FUNCTIONS_WORKER_RUNTIME | Specifies the language worker runtime to use in your Function App, for instance, "python" for Python-based functions. |
| SCM_DO_BUILD_DURING_DEPLOYMENT | This setting determines whether Azure should perform a build operation during the deployment process. |
| WEBSITE_CONTENTAZUREFILECONNECTIONSTRING | This is the connection string to the Azure Files storage account where the package file is stored. |
| WEBSITE_CONTENTSHARE | The file where the function app's content is stored. This is relevant for function apps that run from a ZIP package or Azure Files. |
| WEBSITE_RUN_FROM_PACKAGE | Indicates if the function app is running directly from a deployment package. This can point to a URL containing a .zip file with the app's content or set to "1" to run from a package in the current storage account. |



# 

# 

# Core Modules and Libraries

| **Name** | **Description** |
|:---|:---|
| Logging | Utilized for tracking events, errors, and informational messages that occur during the execution of the function. |
| Azure Functions | The framework for creating serverless functions in the cloud. |
| Azure Core and Digital Twins Client | SDKs to interact with Azure Digital Twins. |
| Azure Identity | Handles authentication across Azure services. |
| OS | Provides a way to interact with the operating system and environment variables. |
| Pandas | A data analysis library. It is used here to structure and manipulate data efficiently. |
| Itertools | Contains functions that are used for iterating through collections of data. |
| Threading | Supports concurrent execution to improve performance. |
| Datetime | Manages and formats dates and times. |
