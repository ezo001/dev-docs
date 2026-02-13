---
sidebar_position: 2
title: AOT Azure Stream Analytics Technical Overview Auriga
---

**Accenture Operations Twin**

**Azure Stream Analytics**

**TECHNICAL OVERVIEW**

Release Version: 2.5

**Metadata Table**

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / AOT

  **Domain / Area**                   Azure / Architecture

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Prathamesh Pingale, Snehanka

  **Status**                          Published / Approved

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   AOT Azure Getting Started, AOT Azure Architecture Blueprint
  -----------------------------------------------------------------------------------------------------------------

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Glossary [3](#glossary)](#glossary)

[Data Flow [4](#data-flow)](#data-flow)

[Data Flow Diagram [4](#data-flow-diagram)](#data-flow-diagram)

[Data Flow Diagram Key [4](#data-flow-diagram-key)](#data-flow-diagram-key)

[Configuration [5](#configuration)](#configuration)

[Input [5](#input)](#input)

[Output [6](#output)](#output)

[ADTFunctionAppOutput [6](#adtfunctionappoutput)](#adtfunctionappoutput)

[ADXOutput [7](#adxoutput)](#adxoutput)

[UDF Query [8](#udf-query)](#udf-query)

[Transformed CTE [8](#transformed-cte)](#transformed-cte)

[SELECT INTO \[ADXOutput\] [8](#select-into-adxoutput)](#select-into-adxoutput)

[SELECT INTO \[ADTFunctionAppOutput\] [8](#select-into-adtfunctionappoutput)](#select-into-adtfunctionappoutput)

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Azure Stream Analytics is a real-time data analytics service, designed to process and analyze high volumes of fast streaming data from various sources. It provides a powerful, low-latency solution for transforming raw data into actionable insights, enabling businesses to make timely decisions. With its SQL-like query language, seamless integration with Azure IoT Hub and Event Hubs, and the capability to output to various Azure services, Stream Analytics simplifies complex event processing, analytics, and data-driven applications. Ideal for scenarios like IoT telemetry, web clickstream analytics, and live dashboarding, it offers a scalable, reliable platform for your streaming data needs.

## Purpose

This document describes the technical details of how Azure Stream Analytics is utilized by AOT\'s Azure version.

## Target Audience

-   Developers

-   Application Architects

-   DevOps Engineers

## Prerequisites

-   JSON file with attributes to create the asset hierarchy

-   Python SDK file as function code

-   Access to the [GIT repository](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_git/MarilynVPlatform)

## Contacts

-   

-   

-   

## Glossary

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**                         **Definition**
  -------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------
  Azure API Management (APIM)      A platform for managing, publishing, and securing APIs at scale within the Azure ecosystem.

  Azure Kubernetes Service (AKS)   A managed Kubernetes container orchestration service, simplifying the deployment and management of containerized applications.

  Azure Data Explorer (ADX)        A fast and highly scalable data analytics service optimized for large volumes of structured, semi-structured, and unstructured data.

  Azure Stream Analytics           A real-time analytics service that processes and analyses data streams from various sources, such as IoT devices or cloud applications.

  Azure IoT Hub                    A cloud service that acts as a central message hub for secure and reliable communication between IoT applications and devices.

  Telemetry Data                   Data collected from remote devices or sensors, typically used for monitoring, analysis, and decision-making purposes.

  User-Defined Functions (UDFs)    Custom functions written by users to extend the capabilities of query languages, enabling bespoke data processing logic.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Data Flow

The Azure Stream Analytics data flow consists of ingestion, processing, and routing of data as follows.

**Data Ingestion**

-   The simulator transmits the telemetry data.

-   Azure IoT Hub acts as the entry point, securely receiving the telemetry data in real time.

**Data Processing**

-   The raw data is then channelled into Azure Stream Analytics Job, where it is processed.

-   Real-time analytics is performed through SQL-like queries and User-Defined Functions (UDFs) to extract actionable insights and detect anomalies or patterns.

**Data Routing**

Upon processing, the data is bifurcated along two paths:

-   One stream goes to Azure Data Explorer, where it is stored for long-term analysis, historical trend monitoring, and complex querying.

-   Simultaneously, another stream heads towards the Azure Function App.

## Data Flow Diagram

![Azure Stream Analytics Data Flow](media/image2.png)\{width="7.488052274715661in" height="2.4513582677165355in"\}

### Data Flow Diagram Key

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Component**            **Description**
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------
  Simulator                The source of telemetry data that is sent to Azure IoT Hub.

  Azure IoT Hub            Acts as the central entry point for IoT device data, securely ingesting real-time telemetry from a wide network of connected devices.

  Azure Stream Analytics   Processes and analyzes streaming data in real time, applying custom transformations and analytics to extract actionable insights from raw telemetry.

  Azure Data Explorer      Receives processed data for long-term storage and complex analysis, enabling deep insights into historical data patterns and trends.

  Azure Function App       Receives processed data, interacts with Azure Digital Twins to synchronize digital twin states, and manages twin relationships.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# **Configuration**

To reference the real-time telemetry data streamed from IoT devices, Azure IoT Hub has been designated as an input source for Azure Stream Analytics.

## Input

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Property**                 **Value**                    **Description**
  ---------------------------- ---------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Input Alias                  iot-hub-input                This is the reference name used within the Azure Stream Analytics job to identify the input source coming from an Azure IoT Hub.

  Subscription                 Microsoft Azure Enterprise   Indicates the Azure subscription that the IoT Hub is associated with. This determines the billing context for the service.

  IoT Hub                      iot-aot-azure-dev            The specific IoT Hub from which the data is being ingested. The name suggests that this IoT Hub is part of a development environment.

  Consumer Group               \$Default                    The name of the consumer group within the IoT Hub that is being used to read the events. Consumer groups are used to enable multiple consuming applications to each have a separate view of the event stream, and to read the stream independently at their own pace and with their offsets.

  Shared Access Policy Name    iothubowner                  Specifies the name of the shared access policy used to authenticate with the IoT Hub. This policy will dictate the permissions that the Stream Analytics job has over the IoT Hub.

  Shared Access Policy Key     \*\*\*\*\*\*\*\*\*\*\*       The key associated with the shared access policy, which is not displayed for security purposes. This key is necessary to establish a secure connection between the Stream Analytics service and the IoT Hub.

  Endpoint                     Messaging                    Defines the endpoint type that is being used to connect to the IoT Hub. The Messaging endpoint is used for cloud-to-device and device-to-cloud messages.

  Partition Key                (Not specified)              An optional field that can be used to specify a partition key for incoming events. Here we have not specified.

  Event Serialization Format   JSON                         The format in which event data is serialized. Here it is set to JSON, indicating that incoming events are expected to be in JSON format.

  Encoding                     UTF-8                        The character encoding used for the incoming event data. UTF-8 is the standard encoding that supports all characters and symbols.

  Event Compression Type       None                         Specifies if any compression is applied to the incoming event data. In this case, it is set to None, meaning there is no compression, and the data will be ingested as is.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Output

Two outputs must be configured -- ADTFunctionAppOutput, and ADXOutput. For processed telemetry data to be sent to Azure Data Explorer (ADX), the output alias must be set to ADXOutput. This configuration ensures that the telemetry data is automatically forwarded to ADX after processing and analysis.

### ADTFunctionAppOutput

The table below includes the configuration values for the ADTFunctionAppOutput.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Property**      **Value**                         **Description**
  ----------------- --------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Output Alias      ADTFunctionAppOutput              This is the identifier used within the Azure Stream Analytics job to refer to the specific output stream being sent to an Azure Function App.

  Subscription      Microsoft Azure Enterprise        The Azure subscription under which the Function App is hosted and billed.

  Function App      func-aot-parameter-metadata-dev   The name of the Azure Function App that receives the output data.

  Function          func_parameter_create_update      This is the function within the Function App that will be triggered when data is received.

  Key Name          (Saved Key)                       A reference to the authentication key that has been previously set up and saved, used to authorize the data transfer from the Stream Analytics job to the Azure Function App.

  Key               \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*    The actual value of the authentication key is obscured for security purposes. This key is crucial to authenticate the data transfer between services.

  Max batch size    (blank by default)                This optional setting allows specifying the maximum size of each data batch sent to the Function App. It is default in this case.

  Max batch count   10                                Specifies the maximum number of events in a batch sent to the Function App. Here, a maximum of 10 events will be grouped and sent together.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### ADXOutput

The table below includes the configuration values for the ADXOutput.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Property**          **Value**                           **Description**
  --------------------- ----------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Output Alias          ADXOutput                           This is the reference name within Azure Stream Analytics for the destination where processed data will be sent.

  Subscription          Microsoft Azure Enterprise          This indicates under which Azure subscription the ADX instance is provisioned, which would be used for billing and management purposes.

  Cluster               adx-aot-test                        This refers to the specific Azure Data Explorer cluster that the data will be sent to. The cluster provides the compute and storage resources required to perform data analytics.

  Database              adx-aot-test/AOTIAADX               This is the target database present in the Azure Data Explorer cluster where the data is stored. This database holds the tables that are used for running queries and storing data.

  Authentication Mode   Managed Identity: System assigned   This specifies the authentication method being used to access Azure Data Explorer. A system-assigned managed identity is an Azure Active Directory identity automatically created and managed by Azure. It\'s used by the Stream Analytics job to authenticate to the ADX cluster securely.

  Table                 AllParametersTimeseriesData         The name of the table within the specified database of Azure Data Explorer where the data will be inserted.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# UDF Query

This Azure Stream Analytics query transforms and routes data from Azure IoT Hub to Azure Data Explorer (ADX) and an Azure Function App using a series of SQL-like statements, incorporating a User-Defined Function (UDF) for data transformation. The extractParameters User-Defined Function (UDF) in Azure Stream Analytics is a component for preprocessing and transforming raw IoT data into a structured format. Written in JavaScript, this UDF takes a single record from the data stream as its argument and performs several key operations to extract and organize data.

## Transformed CTE

The query begins with a Common Table Expression (CTE) named *Transformed* that serves as a preprocessing step. It applies a UDF called *extractParameters* to each piece of input data from the Azure IoT Hub \[iot-hub-input\]. This function transforms the raw input data into a more structured format, encapsulating it within the *TransformedData* alias. This transformation process includes extracting and restructuring key information from the raw IoT data, making it ready for further analysis and processing.

> WITH Transformed AS (
>
>     SELECT
>
>         UDF.extractParameters(input) AS TransformedData
>
>     FROM
>
>         \[iot-hub-input\] as input
>
> )

## SELECT INTO \[ADXOutput\]

This part of the query takes the structured data (TransformedData) from the CTE and selects specific fields: external_id, timestamp, value, the system processing timestamp (as system_timestamp), and an attribute from the metadata. It then outputs this selected data into Azure Data Explorer (\[ADXOutput\]). Here, the data can be stored, further analyzed, and queried over time to uncover insights.

> SELECT
>
>     TransformedData.external_id AS external_id,
>
>     TransformedData.timestamp AS timestamp,
>
>     TransformedData.value AS value,
>
>     System.Timestamp() AS system_timestamp,
>
>     TransformedData.metadata.attribute AS attribute
>
> INTO
>
>     \[ADXOutput\]
>
> FROM
>
>     Transformed

## SELECT INTO \[ADTFunctionAppOutput\]

The query also includes a second output action, which selects the entire TransformedData from the CTE without specifying individual fields. This complete dataset is then routed into an Azure Function App (\[ADTFunctionAppOutput\]). Azure Function Apps can execute custom logic or processes based on the incoming data, such as sending notifications, automating responses, or integrating with other services or databases.

> SELECT
>
>     TransformedData.external_id AS external_id,
>
>     TransformedData.timestamp AS timestamp,
>
>     TransformedData.value AS value,
>
>     System.Timestamp() AS system_timestamp,
>
>     TransformedData.metadata.attribute AS attribute
>
> INTO
>
>     \[ADXOutput\] FROM Transformed
