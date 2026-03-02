---
sidebar_position: 2
title: DT Getting Started
---

## Getting Started with Digital Thread Foundations

IX Digital Thread Foundations platform provides a vendor-agnostic framework to unify and virtualize data across connected products, operations, and services. It enables a single communication layer across PLM, ERP, ALM, MBSE, CAD, and simulation systems for seamless data exchange, operational efficiency, and lifecycle traceability. Reusable connectors and guided configuration accelerators reduce integration effort, speed deployment, and lower ownership costs.

### Purpose

This short document serves as a starting point for IX Digital Thread Foundations. It describes the prerequisites, POCs, and links to its resources.

### Prerequisites

Access to IX Digital Thread Foundations. To request access, contact the Infra team POC Tanushri Sharma, [tanushri.sharma@accenture.com](mailto:tanushri.sharma@accenture.com).

### Target Audience

-   Solution Architects

-   Data Engineers

-   Data Modelers

-   Business Analysts

-   Data Stewards

-   PLM Administrators

-   Manufacturing Engineers

###  Required Skills and Tools

-   Familiarity with Azure tools

-   Familiarity with

-   Familiarity with PLM, ALM, MBSE, ERP, or manufacturing systems

-   Understanding of BOM structures (EBOM, MBOM, Hybrid BOM)

-   Basic knowledge of APIs and data integration concepts

-   Experience with streaming or batch data pipelines (optional)

### Contacts

#### Business Team

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [karthik.ramachandra@accenture.com](mailto:karthik.ramachandra@accenture.com)

-   [riju.dhar@accenture.com](mailto:riju.dhar@accenture.com)

-   [vamsi.konambhotla@accenture.com](mailto:vamsi.konambhotla@accenture.com)

#### Technical Team

-   [laura.mosconi@accenture.com](mailto:laura.mosconi@accenture.com)

-   [stefano.giacco@accenture.com](mailto:stefano.giacco@accenture.com)

-   [l.bramhanapalli@accenture.com](mailto:l.bramhanapalli@accenture.com)

-   [phani.kumar.koduri@accenture.com](mailto:phani.kumar.koduri@accenture.com)

## 

# 

## Use Cases

IX Digital Thread comprises the following use cases.

-   Part Classification

-   Data Catalog

-   Battery Management

-   Data Products

-   BOM Management

-   Digital Thread Dashboard

### 

## Part Classification

Digital Thread's Part Classification System is an optimization engine designed to solve business challenges such as the rising number of components, lack of part management in systems, duplication of parts, and limited reuse. The solution features an intuitive user interface driven by IX Digital Thread on the back end.

-   [Part Classification UI](https://ix-digitalthread-components-dev.accenture.com/partClassification/)

-   [Use Case Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_Part_Classification_Use_Case_Overview_1_1.pdf)

### Data Catalog

IX Digital Thread's data catalog is a centralized repository that organizes and stores metadata about an organization\'s data assets, making it easier for users to discover, understand, and utilize data effectively. It provides detailed descriptions, including data source, structure, lineage, and usage information, ensuring a comprehensive view of the data landscape. The application is implemented as Micro Frontends (MFE) based on Angular 16.

-   [Data Catalog UI](https://ix-digitalthread-components-dev.accenture.com/dataCatalog/)

-   [UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_Data_Catalog_UI_Guide_1_1.pdf)

### Data Products

A data product is a digital product that supplies information or knowledge to clients, usually in an organized and uniform structure. Data products are created to satisfy specific business requirements or to address particular issues, and they can serve as the foundation for decision-making, operational enhancement, or the generation of new revenue streams. IX Digital Thread Foundations enables the creation of reliable and efficient data products.

The data products created for Digital Thread Foundations enable the creation of an end-to-end data management system by ingesting data from various sources, virtualizing, and exposing them via APIs for consumption by client applications or dashboards.

The solution provides real-time or near-real-time data updates, ensures data quality and security through data governance policies, and tracks data lineage.

#### Battery Management System

The Battery Management System (BMS) is a data product that helps different components communicate and work together. This makes it easier for users to work with data. The system can handle any type of industrial data. Azure Data Factory (ADF) pipelines are used to move data from different sources into a PostgreSQL database. ADF also checks the data to make sure it is correct.

-   [Data Products Overview](https://industryxdevhub.accenture.com/assetdetails/104)

-   [Battery Management System Workflow Overview](https://industryxdevhub.accenture.com/assetdetails/107)

###  BOM Management

IX Digital Thread\'s BOM Management application is designed to help users efficiently compare and transform an Engineering Bill of Materials (EBOM) into a Manufacturing Bill of Materials (MBOM) within a structured workflow. This conversion process ensures that engineering data is accurately translated into a manufacturable format while maintaining traceability and version control. Furthermore, the application provides streamlined BOM management experience by offering additional functionalities such as data quality checks, multisystem integration, hybrid BOM automation, and analytics through a single, search-driven interface The Digital Thread Dashboard is also a key functionality offered, which provides real-time view of health, performance, and status of digital threads across integrated platforms.

-   [BOM Management Application](https://ixts-components-dev.accenture.com/mbom/)

-   [BOM Management documentation](https://industryxdevhub.accenture.com/assetdetails/115)

The primary functionalities of the application are described in further detail below.

#### BOM Comparison and Conversion

This feature enables scalable and traceable BOM transformation and comparison across the product lifecycle. Users can perform single or batch BOM conversions using configurable rules and templates, ensuring consistency and accuracy at scale. 

#### Data Quality Check

The Data Quality and Governance framework ensures the accuracy, consistency, and reliability of data across the digital thread. Users can define customizable data quality checkpoints aligned to business rules and enforce them at multiple stages of BOM conversion and comparison. 

#### Hybrid BOM Automation

Hybrid BOM Automation accelerates the creation of manufacturing-ready BOMs by automatically merging engineering and design BOM data from multiple systems. 

#### Multi-System Integration

This feature enables seamless integration and synchronization across engineering and lifecycle management systems.

-   Change Data Capture (CDC) ensures accurate and duplicate-free requirement synchronization between MBSE and PLM systems.

-   ALM-PLM integration maintains real-time consistency of requirements, while PM-ALM automation improves traceability by automatically triggering Jira tasks when new requirements are created. 

#### Timeseries KPIs and Analytics

This feature provides real-time analytics and performance insights using streaming KPI pipelines. Apache Flink processes time-series data, which is enriched and stored in Azure Data Explorer (ADX) for advanced visualization and analysis. Users can compare raw versus transformed metrics to assess data quality, process efficiency, and operational performance.

#### Digital Thread Dashboard

The Digital Thread Dashboard is the central command hub within the IX Digital Thread Foundations platform. It provides real-time visibility into the health, performance, and status of digital threads across integrated enterprise systems (e.g., PLM, ERP, ALM). The dashboard streamlines project monitoring, accelerates decision-making, and improves operational execution by consolidating data into a single, unified interface.

## Resources

The following table lists all documentation assets related to IX Digital Thread Foundations and its use cases.


| Document | Description |
| --- | --- |
| [Digital Thread Foundations Architecture](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Architecture_1_2.pdf) | This document provides an overview of Industry X Digital Thread Foundations architecture to help readers understand the overall architecture of the system and the technical implementation of its modules. |
| [Digital Thread Foundations Functional Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Functional_Overview_1_2.pdf) | This document provides an overview of the key functionalities of IX Digital Thread Foundations. |
| [Digital Thread SDK Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_SDK_Guide_1_2.pdf) | This document describes IX Digital Thread's Software Development Kit and how to implement a project using it. |
| Digital Thread Connectors Integration Guides (Links in description) | This asset provides information on the connectors utilized by IX Digital Thread Foundations. Links to the dedicated documents for each connector are as follows: - [Kafka Connectors Configuration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_CDC_Kafka_Connectors_Configuration_1_1.pdf) - [Jira Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_Jira_Connector_Integration_Guide_1_1.pdf) - [SAP Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_SAP_Connector_1_1.pdf) - [CDC Debezium Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_CDC_Debezium_Connector_1_1.pdf) - [HTTP Source and Sink Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_CDC_HTTP_Connector_1_1.pdf) - [IIoT Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_IIoT_Connector_1_1.pdf) - [MES Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_MES_Connector_1_1.pdf) - [Teamcenter Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/IXDT%201.1/DT_Teamcenter_Connector_1_1.pdf) - [S4HANA Connecter Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_S4HANA_Connector_1_2.pdf) - [Polarion Connector Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Polarion_Connector_1_2.pdf) |
| [Query Engine API Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Query_Engine_API_Reference_1_2.pdf) | The Query Engine is a gateway that facilitates interaction between the user and external source systems of IX Digital Thread Foundations. This document serves as an API reference for IX Digital Thread's Query Engine application |
| [Policy Engine Use Case Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Policy_Engine_Use_Case_Overview_1_2.pdf) | This document describes Digital Thread's Policy Engine implementation and usage to assist the target audience in understanding and authoring business policies for Digital Thread applications. |
| [Part Classification Use Case Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Part_Classification_Use_Case_Overview_1_2.pdf) | This document describes IX Digital Thread's Part Classification system and its usage. |
| [Data Catalog UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Data_Catalog_UI_Guide_1_2.pdf) | This document explains the features of IX Digital Thread's Data Catalog user interface. |
| [Data Catalog API Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Data_Catalog_API_Reference_1_2.pdf) | This document serves as an API reference for IX Digital Thread's Data Catalog application. |
| [Data Discovery Automation Architecture Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Data_Discovery_Automation_Architecture_Overview_1_2.pdf) | This document provides an overview of IX Digital Thread's Data Discovery Automation architecture. |
| [Data Discovery Automation Pipelines Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Data_Discovery_Automation_Pipelines_Overview_1_2.pdf) | This document provides an overview of the pipeline framework utilized by IX Digital Thread to implement Data Discovery Automation. |
| [Data Products Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Data_Products_Overview_1_2.pdf) | This document provides a component-based overview of IX Digital Thread's data products. |
| [Data Products API Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Data_Product_API_Reference_1_2.pdf) | This reference document includes information about paths, inputs, outputs, and error management for APIs related to Data Products. The document includes descriptions of APIs used for configuration as well as descriptions of APIs that provide middleware functionality. |
| [ADF Workflow Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_ADF_Workflow_1_2.pdf) | This document provides an overview of the ADF workflow implemented for Digital Thread Foundations. It depicts the Batch Data Pipeline Flow and the integration of the Great Expectations (GE) Validation Workflow and outlines each stage from data extraction to final transmission. |
| [ADF Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_ADF_Integration_Guide_1_2.pdf) | This guide describes the key components and functions of Azure Data Factory. The documentation focuses on enabling users to effectively utilize ADF for data integration, transformation, and orchestration within the project's ecosystem. |
| [Battery Management System Workflow Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_UC_ADF_BMS_Workflow_1_2.pdf) | This document delves into a specific Azure Data Factory (ADF) workflow designed for the Software-defined Battery Management System (BMS) use case within the Digital Thread\'s framework. This workflow demonstrates how ADF streamlines data movement, transformation, and integration across diverse sources related to battery management data. |
| [Battery Management System Pipelines Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_UC_ADF_BMS_Pipelines_1_2.pdf) | The purpose of this document is to provide a comprehensive description of the execution of Azure Data Factory pipelines used in the battery management use case within the IX Digital Thread framework. These pipelines efficiently orchestrate data movement and transformation from source to destination. The discussion includes their core objectives and execution methods, including triggering mechanisms |
| [Azure Monitor Functional Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Azure_Monitor_Functional_Overview_1_2.pdf) | This document provides an overview of Azure Monitor within the context of the IX-Digital Thread (IXDT). It covers Azure Monitor\'s architecture, functionalities, and capabilities, focusing on data collection, analysis, visualization, and response mechanisms. Additionally, it delves into practical use cases and best practices for leveraging Azure Monitor effectively for monitoring DT's Azure resources and applications. |
| [Azure Monitoring Dashboards UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Azure_Monitoring_Dashboards_UI_Guide_1_2.pdf) | This document outlines essential procedures for efficiently managing the IX Digital Thread monitoring infrastructure. From navigating dashboards and workbooks to troubleshooting issues, it provides comprehensive guidance to users to ensure smooth operations and optimize performance. |
| [Azure Jobs Monitor Tutorial](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Azure_Jobs_Monitor_Tutorial_1_2.pdf) | This document serves as a short tutorial on how to view the Azure Jobs Monitoring Dashboard and Flink jobs-related visualizations for the job's log, metrics, etc. |
| [BOM Management Functional Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Management_Functional_Overview_1_2.pdf) | This document describes the functionality of the BOM Management use case of the IX Digital Thread Foundations platform. |
| [BOM Management Database Technical Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Management_Database_Technical_Overview_1_2.pdf) | This document provides a detailed description of the Postgres database (ixts-dev-psqldb) utilized for EBOM to MBOM conversion by IX Digital Thread. |
| [BOM Conversion Architecture](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Conversion_Architecture_1_2.pdf) | This document describes the technical architecture of the IX Digital Thread Foundations BOM Conversion asset |
| [BOM Management API Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Management_API_Reference_1_2.pdf) | This document serves as an API reference for the IX Digital Thread BOM Management application. |
| [BOM Management UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Management_UI_Guide_1_2.pdf) | This document provides a comprehensive overview of the user interface (UI) for the IX Digital Thread Foundations' BOM Management application. It details the layout, navigation, and functionalities available within the application, guiding users through each feature and workflow. |
| [BOM Conversion Flink Job Overview](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Conversion_Flink_Job_Overview_1_2.pdf) | This document provides an overview of the Flink job used for BOM Conversion feature of the BOM Management application. |
| [BOM Comparison Flink Job Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Comparison_Flink_Job_Overview_1_2.pdf) | This document provides an overview of the Flink job used for the BOM Comparison feature of the BOM Management application. |
| [BOM Data Quality Check Flink Job Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_BOM_Data_Quality_Check_Flink_Job_Overview_1_2.pdf) | This document provides an overview of the Flink jobs used for BOM Data Quality Check feature of the BOM Management application. |
| [Timeseries Flink Job Overview](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/1.2/DT_Timeseries_Flink_Job_Guide_1_2.pdf) | This document provides an overview of the Timeseries Flink job, which is designed to handle time-series data from IoT and OPC sensors. |
##### Metadata Table


<div class="metadata-for-agents" aria-hidden="true">
| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Digital Thread |
| **Domain / Area** | Engineering |
| **Owner (Team/Person)** | Karthik Ramachandra |
| **Reviewers** | Karthik Ramachandra |
| **Status** | Approved / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** |  |
| **Related Assets / Alternatives** | AOT / Engineering Orch / Engineering Agents |
</div>
