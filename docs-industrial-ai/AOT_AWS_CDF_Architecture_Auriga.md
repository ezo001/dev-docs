---
sidebar_position: 2
title: AOT AWS CDF Architecture Auriga
---

Accenture Operations Twin

AWS/CDF Deployment

ARCHITECTURE BLUEPRINT

Release Version: 2.5

**Metadata Table**

  -------------------------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -------------------------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / AOT

  **Domain / Area**                   Digital Twin / Architecture

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Susarla, Aditya, Takó, István

  **Status**                          Draft / In Progress

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [[Summary - Overview]\{.underline\}](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   
  -------------------------------------------------------------------------------------------------------------------------------

# 

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Structure [4](#structure)](#structure)

[Enterprise Landscape [5](#enterprise-landscape)](#enterprise-landscape)

[Components and Services [6](#components-and-services)](#components-and-services)

[DataOps [7](#dataops)](#dataops)

[DataOps using Cognite Data Fusion [8](#section-4)](#section-4)

[Extractors [9](#extractors)](#extractors)

[Intelligent Advisor [10](#intelligent-advisor)](#intelligent-advisor)

[Domain Model [11](#domain-model)](#domain-model)

[Containers [12](#containers)](#containers)

[IA Insight Generation Interactions [14](#ia-insight-generation-interactions)](#ia-insight-generation-interactions)

[Deployment [15](#deployment)](#deployment)

[Smart KPIs [16](#smart-kpis)](#smart-kpis)

[Domain Model [17](#domain-model-1)](#domain-model-1)

[Containers [19](#containers-1)](#containers-1)

[Calculation Interactions [21](#calculation-interactions)](#calculation-interactions)

[Deployment [22](#deployment-1)](#deployment-1)

[Operations Hierarchy [23](#operations-hierarchy)](#operations-hierarchy)

[Domain Model [23](#domain-model-2)](#domain-model-2)

[Deployment [26](#deployment-2)](#deployment-2)

[Platform Tools [27](#platform-tools)](#platform-tools)

[Data Analytics Models [27](#data-analytics-models)](#data-analytics-models)

[Internationalization and Localization [30](#internationalization-and-localization)](#internationalization-and-localization)

[Scheduling service [32](#scheduling-service)](#scheduling-service)

[3D Visualization [33](#d-visualization)](#d-visualization)

[Consumers and Dependencies [34](#consumers-and-dependencies)](#consumers-and-dependencies)

[Deployment Diagrams [36](#deployment-diagrams)](#deployment-diagrams)

[People Management [37](#people-management)](#people-management)

[System context [38](#system-context)](#system-context)

[Containers [39](#containers-2)](#containers-2)

[Deployment diagrams [40](#deployment-diagrams-1)](#deployment-diagrams-1)

[Reporting [41](#reporting)](#reporting)

[System context [41](#system-context-1)](#system-context-1)

[Containers [42](#containers-3)](#containers-3)

[Applications [43](#applications-6)](#applications-6)

[Host App [44](#host-app)](#host-app)

[Configuration Apps [44](#configuration-apps)](#configuration-apps)

[Appendix [45](#appendix)](#appendix)

[Guiding Principles [45](#guiding-principles)](#guiding-principles)

[Patterns [45](#patterns)](#patterns)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Amazon Web Services (AWS) is a comprehensive and widely adopted cloud computing platform offered by Amazon. It provides a broad set of on-demand services, including computing power, storage, databases, networking, analytics, and machine learning, allowing organizations to build, deploy, and manage applications and infrastructure in the cloud efficiently and securely.

Cognite Data Fusion (CDF) is an industrial data platform developed by Cognite that enables organizations to collect, contextualize, and manage large volumes of data from diverse sources, including operational technology (OT) and information technology (IT) systems. CDF provides powerful tools for data integration, transformation, and visualization, supporting advanced analytics, digital twin creation, and scalable AI solutions across industrial environments.

## Purpose

The purpose of this document is to provide an overview of the architecture used to deploy AOT with CDF on AWS. After reading, the target audience should understand the overall architecture of the system and the technical implementation of its modules.

## Target Audience

Software architects, developers, and integrators with IT background, familiarity with a digital twin, data ingestion, data contextualization, knowledge graph, advanced analytics, artificial intelligence, Cognite, and AWS services and artifacts.

## Prerequisites

Familiarity with Cognite Data Fusion (CDF)

## Contacts

-   

-   

-   

## Related Links

-   [AOT Documents](https://industryxdevhub.accenture.com/asset-home;search_text=AOT) 

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45) 

-   [Official CDF Documentation](https://docs.cognite.com/cdf/)

-   [AOT Twin Builder and Twin Viewer Architecture Blueprint](https://industryxdevhub.accenture.com/assetdetails/47)

-   [AOT_People Management_Context Diagram](https://ts.accenture.com/:u:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT_People%20Management_Context.svg?csf=1&web=1&e=jiA5Ip)

-   [AOT People Management Architecture Blueprint](https://industryxdevhub.accenture.com/assetdetails/64)

## 

## Glossary


| **Term** | **Description** |
| --- | --- |
| Ingestion | Consuming data taken from external systems and storing it in the central data model of the DataOps platform |
| Data model | The data model is the central point of the DataOps platform on which AOT features are built and executed. It is optimized for modeling operations data and creating a knowledge graph. |
| Contextualization | Contextualization means creating relationships between entities inside the Knowledge Graph, this way giving a more complete context to each entity (data entry). The more complete the knowledge graph becomes the more possibilities for finding patterns and gaining knowledge will be. |
|  | A trivial example would be measurements stored in a timeseries linked to an asset, representing a piece of equipment, on which the measurements were performed. |
| Business Logic | The business logic can appear in several forms inside AOT, including Insight generator data analytics models and KPI value calculation functions. The logic can involve advanced analytics, AI, ML, or conventional business logic to consume and manipulate the knowledge graph. |
| APIs | Exposes data and business logic toward the external world. |
| Applications | Business applications, reports, and dashboards are implemented on top of the business logic and knowledge graph of the solution. |


# Structure

As illustrated right, AOT can be simplified into the following building blocks:

1.  Data is provided by external systems. These can be all the existing IT and OT systems within a business.

2.  The provided data is brought into AOT by extracting, transforming, and loading it. The raw data is transformed and brought together into one coherent domain model.

3.  The contextualization layer facilitates a fast and scalable contextualization of data. Relationships between discrete data elements coming from siloed data sources need to be built and stored to make possible logical navigation and reasoning, hence transforming the data into knowledge.

4.  The contextualized data is stored and provided as a knowledge graph. The knowledge graph is also the domain model of the business.

5.  Applications and advanced analytics models live on top of the knowledge graph. The individual applications are interoperating with other business applications via the application integration layer. This involves collaboration between the AOT applications but also with external applications.

6.  AOT provides a People Management module.

7.  At any point in time where data is generated and/or exchanged stream analytics possibility is provided.

![Diagram showing the architecture of Accenture Operations Twin (AOT) system. At the bottom, external data sources feed into ETL (Extract, Transform, Load) processes, followed by a contextualization layer. Above this is the AOT Knowledge Graph, which connects to multiple components: Smart KPIs, Intelligent Advisor, Operations Hierarchy, 3D Visualizer, advanced analytics models, applications, and People Management. At the top is an application integration layer. A vertical stream analytics section runs along the left side, indicating real-time data processing. Arrows show bidirectional data flow between layers and components.](media/image2.png)\{width="7.696080489938757in" height="6.535512904636921in"\}

![Diagram showing a data flow process with three main components: External data sources on the left, Knowledge Graph in the center, and Applications on the right. Arrows indicate data moving from external sources to the Knowledge Graph, then to Applications, with a feedback loop returning to Applications. A dashed line labeled \'Stream analytics\' runs across the top, connecting all three components.](media/image4.svg)\{width="5.446653543307087in" height="2.1875in"\}

# 

# Enterprise Landscape

The diagram below shows how AOT is integrated into the customer\'s ecosystem. Click the image to enlarge it.

![Diagram titled \'AOT System Landscape\' showing components and interactions within the Accenture Operations Twin (AOT) ecosystem. On the left, roles include Configurator, Operator, and System Administrator linked to Identity Provider. The center section, labeled \'Operations Twin Features,\' contains interconnected modules: AOT Platform Tools, AOT 3D Visualizer, AOT Smart KPIs, AOT Intelligent Advisor, AOT Operations Hierarchy, AOT Reporting, AOT People Management, and AOT DataOps. Arrows indicate data and message flows between these modules and external systems on the right, including Integrated Systems and Source Systems. The diagram highlights how insights, KPIs, and operational data are managed and exchanged across the AOT platform.](media/image6.svg)\{width="13.614583333333334in" height="6.882928696412948in"\}

-   AOT DataOps realizes the data ingestion, contextualization, and hosting of the AOT Knowledge Graph.

-   Operations Twin features (Smart KPIs, Intelligent Advisor, Operations Hierarchy, 3D Visualizer, Reporting) are the sub-systems of AOT that make building Business Applications possible.

-   PM and Platform Tools host cross-cutting, auxiliary features used by the Operations Twin features (People and Permission Management, Job Scheduling, Integration patterns with external systems, Localization and Internationalization, Integration of Data Analytics Models)

-   AOT integrates with the Source system to ingest data, with other business applications to collaborate, and with Data Analytics services.

# 

# Components and Services

The diagram below shows how AOT systems are realized on top of AWS services.

![](media/image8.svg)\{width="9.622916666666667in" height="6.697222222222222in"\}

-   Real-time data to be integrated via an arbitrary edge component and middleware into an IoT Hub instance. From here we channel the data into stream analytics for eventual analytics jobs to process it. Finally, it flows into the Knowledge graph.

-   The stream analytics component makes it possible to identify outstanding data points near-real time and to generate events into the Message Broker whenever needed.

-   Batch data to be integrated via Data Factory. Assuming that there will be some sort of edge environment the Data Factory Integration runtime would be deployed there.

-   The Knowledge Graph will be composed of CDF services. Amazon S3 will host the nonstructured data, while Structured Query Language (SQL) Databases will hold configuration and master data.

-   On AWS, the primary Machine Learning model execution environment is Sage Maker. These are the services that we are leveraging for teaching a model, deploying to cloud execution and on Edge execution and execute on top of the Knowledge Graph or the live data stream.

-   The microservices responsible for the business logic are impacted only on data access layer level. The executed business logic does not depend on the underlying DataOps platform.

The subsystems shown above are described in the sections that follow.

# DataOps

The DataOps system of AOT ingests data from various source systems and stores in a knowledge graph to maintain the Operations Twin. Furthermore, it contains the infrastructure and tooling for contextualization as well.

AOT sub-systems including Smart KPIs, Intelligent Advisor, 3D Visualizer, and Operations Hierarchy can use this knowledge graph to perform their operations.


| **Principle** | **Description** |
| --- | --- |
| Data Integration | > DataOps platforms facilitate the seamless integration of data from various sources, including databases, APIs, cloud services, and more. They often provide connectors and ETL (Extract, Transform, Load) capabilities to ensure data flows smoothly. |
| Data Quality and Governance | > These platforms enforce data quality standards and governance policies, ensuring that data is accurate, consistent, and compliant with regulations. They may include data profiling, cleansing, and validation tools. |
| Automation | > Automation is a central component of DataOps. Platforms automate repetitive tasks such as data ingestion, transformation, and deployment, reducing manual effort and minimizing errors. |
| Collaboration | > DataOps emphasizes collaboration between different teams, including data engineers, data scientists, analysts, and business stakeholders. DataOps platforms provide features for sharing and collaborating on data-related projects. |
| Version Control | > Like software development, DataOps platforms often incorporate version control systems to track changes in data pipelines, making it easier to manage and roll back to previous versions when needed. |
| Monitoring and Logging | > Comprehensive monitoring and logging capabilities help track the performance of data pipelines, detect anomalies, and troubleshoot issues in real time. |
| Scalability and Flexibility | > DataOps platforms are designed to scale with growing data volumes and evolving business needs. They can handle both batch and real-time data processing. |
| Security | > Robust security features, including access controls, encryption, and authentication, are essential to protect sensitive data within the platform. |
| Compliance and Auditing | > DataOps platforms assist in maintaining compliance with data privacy regulations by tracking and auditing data access and changes. |
| Cost Management | > They often include cost management tools to optimize data storage and processing expenses in cloud environments. |


The DataOps system of AOT is responsible for extracting data from external data sources, transforming and storing it into the knowledge graph. Furthermore, it holds tools for scaling the data contextualization work. The diagram below depicts the general context of the DataOps system.

![Diagram titled \'AOT DataOps Context\' showing relationships between components in the Accenture Operations Twin system. At the center is AOT DataOps, which ingests data from source systems (ETL) and stores it in a knowledge graph, providing infrastructure and tooling for contextualization. Below, Source Systems supply data to maintain the Operations Twin. Above, three modules---AOT Smart KPIs (for viewing KPIs in a hierarchy), AOT Intelligent Advisor (for creating insights about business operations), and AOT Operations Hierarchy (for displaying hierarchy details)---all use the knowledge graph provided by AOT DataOps. Arrows indicate data flow and dependencies.](media/image10.svg)\{width="6.89946741032371in" height="5.616278433945757in"\}

CDF is where the data is normalized and enriched by adding connections between data resources of various types and stored in a graph index in the cloud. For more information see the [Official Cognite Documentation](https://docs.cognite.com/cdf/).

## 

## DataOps using Cognite Data Fusion

The data is extracted from the source system using Cognite out-of-the-box and AOT-provided extractors, and is loaded into RAW, Cognite\'s data staging area. Using Cognite Transformations which are Spark SQL-based scripts the data from the staging area is transformed, contextualized, and built into the Knowledge Graph, the central point of the system. The Knowledge Graph data is consumed by the different AOT subsystems using the CDF APIs and SDKs. In the diagram right, data flows from bottom to top.

Cognite Data Fusion is a Software-as-a-Service offering, it doesn\'t require deployment only integration with the AOT systems. Integration consists of configuring Azure Active Directory integration between AOT and CDF, enabling data access through the common AD.

The following tables describe the role and functionality of the different components of the DataOps module:


| **Name** | **Responsibility** |
| --- | --- |
| Cognite provided [Extractors](https://docs.cognite.com/cdf/integration/concepts/extraction/) | Extractors connect to source systems and push data in its original format to Cognite Data Fusion (CDF) as part of the data integration workflow. Data can be extracted with prebuilt Cognite extractors or by creating a customer extractor using Python and .NET utilities packages and SDKs. |
| AOT provided Extractors | Using the Cognite-provided extractor utilities, AOT has built a set of extractors for operations twin use cases. See the subsection below for details. |
| [RAW](https://developer.cognite.com/dev/concepts/resource_types/raw/) | The RAW database and tables hold the source data in its original form to reduce source system queries for the same data for different use cases and minimize the data extractors\' logic. |
| data staging area |  |
| [Transformation](https://docs.cognite.com/cdf/integration/guides/transformation/transformations/) Services | A Transformation Service moves or enriches data from a source system, between data models, or from the Cognite Data Fusion (CDF) staging area into CDF by transforming data into CDF\'s data model or user-defined data models. |
| [Contextualization](https://docs.cognite.com/cdf/integration/concepts/contextualization/) Services | The advanced contextualization tools in Cognite Data Fusion enable users to combine machine learning with a powerful rules engine and the users\' domain expertise to map data from different source systems to each other in a custom data model. |
| [Knowledge Graph](https://docs.cognite.com/cdf/learn/cdf_basics/cdf_basics_datamodel) | A data model is an abstract model that organizes data elements and standardizes how they relate to one another and the properties of real-world entities. The CDF data model collects industrial data by resource types that let users define the data elements, specify their attributes, and model the relationships between them. The different resource types are used to both store and organize data. |
| [API](https://api-docs.cognite.com/) | Cognite\'s RESTful web API enables users to access (read and write) resources in Cognite Data Fusion. |
| [SDK](https://developer.cognite.com/sdks/) | Cognite has a large number of Software Development Kits (SDKs), both adapted to specific programming languages and specific use cases. All Cognite SDKs are open-source and available on GitHub. |


![Diagram titled \'AOT DataOps with Cognitive Extractor\' showing the flow of data and components in the Accenture Operations Twin system. At the top are three modules: AOT Intelligent Advisor (creates insights), AOT Smart KPIs (views KPIs in hierarchy), and AOT Operations Hierarchy (displays hierarchy details). These connect to the Cognitive Data Fusion DataOps Platform, which includes the CDF API and AOT Knowledge Graph. Below are Contextualization Services and Transformation Services for refining and transforming data. Further down is the IAW Extractor for entity matching and pushing data to the CDF. At the bottom, various extractors (SAP PM, PI AF, Hexagon, Files, and CDF Extractors) pull data from source systems like SAP PM, PI AF, Hexagon, and file storage. Arrows indicate data flow from source systems through extractors, contextualization, and transformation into the knowledge graph, supporting insights and KPIs. A legend color-codes components for Smart KPIs, DataOps, Intelligent Advisor, and Operations Hierarchy.](media/image12.svg)\{width="6.0811843832021in" height="9.197673884514435in"\}

# 

## Extractors

Part of the Ingestion layer, AOT\'s Extractors are data integration accelerators designed to extract data from a client source system and load it into the CDF RAW database and tables. They include reusable code developed using the Cognite Custom Extractor framework and can be readily built and deployed on the cloud or locally.

Cognite DataOps platform delivers a set of [Standard Extractors](https://docs.cognite.com/cdf/integration/concepts/extraction/) and a Custom Extractor Framework that enables the development of Custom Extractors for a source system that is not supported by default. Third-party services can also use the Cognite Python SDKs or other Extract Transform and Load (ETL) tools to build custom extractors. The AOT team has currently developed three extractors and plans to release more extractors in the future.

  -----------------------------------------------------------------------
  **Source System-Specific Extractors**       **Flat File Extractors**
  ------------------------------------------- ---------------------------
  SAP PM Extractor                            Local File System

  OSI PI AF Extractor                         

  Hexagon Extractor                           
  -----------------------------------------------------------------------

Once the data from the extractors are in CDF RAW, one of the options to transform the raw data into the CDF knowledge graph (Digital Twin) structure is to use the [transformation services](https://docs.cognite.com/cdf/integration/guides/transformation/transformations) that are built into CDF. AOT provides the possibility to dynamically create deployment pipelines to automate the deployment, configuration, and scheduling of the Spark SQL queries used by the CDF Transformation service.

The CDF Transformation service is based on the configuration provided by the users in a configuration file. In the configuration file, the user can specify all necessary parameters of a Transformation that would help to create and update the Knowledge Graph in Cognite Data Fusion. Some of the necessary parameters of a transformation are listed in the table on the right.

###  Configuration Parameters

-   External ID

-   Transformation Name

-   Spark SQL Query for Running the Transformation

-   CDF Database Name

-   CDF Database Table Name

-   CDF DataSetId

-   Schedule Time for Transformation Schedule

One of the main use cases of the Transformation in AOT is the creation of the Asset Hierarchy, which is a treelike structure representing a client\'s facility. The extractors extract the Asset Hierarchy from the client\'s source system--typically SAP PM--and then transform it into a CDF knowledge graph structure. In some cases, multiple asset hierarchies must be standardized and merged to form the complete representation of the plant in the CDF Data model/knowledge graph. The knowledge graph can be enhanced with additional data coming from:

-   Other source systems using the Transformation and contextualization services

-   An extractor (e.g., time series from sensors, events from alerting systems, etc.)

-   External services (Lambda Functions, Databricks, etc.)

See also: [AOT Extractors Architecture Blueprint](https://industryxdevhub.accenture.com/assetdetails/46)

## 

# Intelligent Advisor

The Intelligent Advisor (IA) is an AI-based solution that enables users of all types -- from shop floor workers to top management -- to focus on their most critical issues, with real-time-generated, prioritized, and contextualized insights and recommendations.

The IA system can help all levels of the value chain by predicting useful insights, highlighting the root causes, notifying relevant colleagues, recommending appropriate actions, and ultimately improving the performance of end-to-end operations.

The following diagram depicts the context of the Intelligent Advisor system within the AOT landscape.

![Diagram mapping Intelligent Advisor's integration with DataOps, Smart KPIs, People Management, Operations Hierarchy, Reporting, 3D Visualizer, and MLOps.](media/image14.svg)\{width="8.10465113735783in" height="6.1396402012248465in"\}

Intelligent Advisor enables the AOT user to run analytics models on the Knowledge Graph, which identifies patterns/issues and creates Insights. The configuration of IA consists of two domain objects:

-   Insight Category

-   Insight Template

The Insight categories represent the different types of Insights to be created. They are linked in a relationship to the Insight Templates that represent the configuration of the Insight screens with all the linked data to be displayed. The Intelligent Advisor is using the following AOT systems:

-   DataOps -- uses time-series data to create predictions using Machine Learning.

-   MLOps -- a platform tool used to execute a machine learning model so that predictions can be created based on historical and live data. It also includes a pipeline for training, evaluation, and deployment of the model.

-   Smart KPIs -- based on machine learning output and KPIs values, Intelligent Advisor will generate insights and actions if needed.

-   Operations Hierarchy -- reads assets hierarchy to generate insights and actions.

The Intelligent Advisor is using the following AOT systems:

-   Reporting -- uses insights and actions to generate reports.

-   3D Visualizer - requires the Insights/Actions information for the context of the 3D visualization.

## Domain Model

There are two parts to the Intelligent Advisor domain model -- the operational model and the configuration model. Information related to the configuration model is kept in the Insight Category entity. Kept information includes:

-   Identifiers that help to identify the related data analytics model

-   Frequency for executing the model

-   Insight template to be used for visualizing the generated insights

-   The theme of the generated insights

![IA Configuration Domain Model](media/image16.svg)\{width="2.641509186351706in" height="1.324274934383202in"\}

## Full IA Domain Model

The full domain model unites configuration with operational objects.

![Diagram titled \'Intelligent Advisor Domain Model\' showing an entity-relationship structure for insights and actions. Central entities include Insight and Action, each with attributes like id, title, description, timestamps, roles, and collaborators. Connected entities are Insight Category, Asset, Insight History, Action History, Work Order, and Insight History Item. Relationships are labeled, such as \'Category of,\' \'Insight for,\' \'Action of,\' and \'History of.\' Each entity box lists its properties, and arrows indicate cardinality and data flow between components.](media/image18.svg)\{width="5.833333333333333in" height="7.304350393700787in"\}

## Containers

Intelligent Advisor combines the following functional components:

-   Insight generation engine

-   Collaboration

-   Actions

-   Advisor panel

-   Insight Details

-   Insight lifecycle management

The following diagrams show the CDF / AWS-based architecture of Intelligent Advisor including:

-   Containers that are specific to the Intelligent Advisor backend services and micro-frontends.

-   Containers provided by the Platform Tools that are common and shared.

-   Containers that represent the AOT knowledge graph, in this specific case the CDF data model provided by the DataOps system of AOT.

The diagram on the right shows the individual components of the system with the most relevant connections highlighted. The color coding is explained in the legend. Click the image to enlarge it.

![](media/image20.svg)\{width="7.890604768153981in" height="8.666525590551181in"\}

The tables below define the responsibility of each of the components found in the diagram above.

### Applications

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                          **Responsibility**
  ------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Intelligent Advisor Configuration Application     The Intelligent Advisor Configuration Application is a standalone configuration application used to create insight category configurations. Two categories exist: KPI based and Predictive. Each insight category will have a different configuration page but with common and specific fields based on the selected category.

  Intelligent Advisor Sidepanel Application         Intelligent Advisor Sidepanel Application is a small micro-frontend application where insights and actions can be viewed and edited.

  Intelligent Advisor Insight Details Application   An application where a detailed view of an insight is shown together with recommendations, related actions, comments, graphical representation, and impacted KPIs.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Microservices

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                             **Responsibility**
  ------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Intelligent Advisor Configurations   The Intelligent Advisor Configurations microservice provides APIs for creating and saving insight configurations.

  Scheduler                            Based on a configuration, the scheduler will invoke the machine learning microservice to generate recommendations.

  Data Model                           A microservice that is responsible for the execution of machine learning models. It is triggered by the Scheduler microservice on a periodic interval using a Kafka topic. When the execution finishes, a new message is published on the output Kafka topic. This microservice can either execute the model using a platform tool machine learning implementation or an in-memory module.

  Insight generator engine             This microservice consumes messages generated by the Data Model microservice and based on the output value will decide if insights need to be created.

  Intelligent Advisor Microservice     The IA Microservice provides APIs used to access insights and actions based on assigned roles.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Data Storage

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                     **Responsibility**
  -------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  Knowledge Graph                              The KG represents the various entities of AOT (Assets, KPIs, Insights, Actions, etc.) and the relationship between these entities.

  Knowledge Data                               Stored knowledge data includes instances of Insights and Actions.

  Intelligent Advisor Configuration Database   The IA config DB stores the insight categories configuration.

  Scheduler Configuration Database             The scheduler config db stores the current configuration of the Scheduler microservice.

  Sequence generator Database                  The sequence generator db stores a unique sequence for each generated insight.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## IA Insight Generation Interactions

The diagram on the right shows the flow of the insight generation inside AOT.

Using the IA Configuration Application, a user can create a configuration object used to generate the insight based on a predefined frequency. The Scheduler microservice is responsible for triggering the Data Analytics microservice which in turn will execute the MLOps service to create predictions. The output of the ML model execution is compared against the KPI values, and the Insight generator engine will decide if a new Insight must be generated or not.

![](media/image22.svg)\{width="5.602083333333334in" height="9.958811242344707in"\}

## Deployment

The following two deployment diagrams explain where each of these system components is hosted, along with communication connections. Click the image to enlarge it.

![](media/image24.svg)\{width="8.990239501312336in" height="9.507866360454942in"\}

# Smart KPIs

The Smart KPIs system of AOT configures KPIs that are built on top of each other. The KPIs are calculated based on the configured formula and contributors, these being either parameters received from sensors, other calculated KPIs, or any other values provided by the AOT Knowledge Graph. The calculated KPIs are stored in the AOT Knowledge Graph and exposed through APIs to the Smart KPI Dashboard application, other AOT applications, and third-party custom applications. The diagram below shows the context of the Smart KPIs system within the AOT landscape. Click the image to enlarge it.

![The diagram titled "AOT Smart KPIs Context" shows a central green box labeled AOT Smart KPIs, which allows users to view KPIs about their operations in a hierarchy for drill-down analysis. Surrounding it are eight connected boxes: Operator (blue) for daily operations, Smart KPI Configurator (purple) for configuring KPIs and dependencies, AOT Intelligent Advisor (cyan) for business insights, AOT 3D Visualizer (teal) for visualizing facilities in 3D, and AOT Reporting (green) for dashboards and reports. Below, AOT DataOps (blue) manages data ingestion and knowledge graphs, AOT People Management (magenta) handles roles and assignments, and AOT Operations Hierarchy (red) displays hierarchy details. Arrows indicate data flow and relationships among these components, forming a context map for KPI management.](media/image26.svg)\{width="9.104166666666666in" height="5.648659230096238in"\}

As shown above, Operators and Smart KPIs configurators are the usual users of the Smart KPIs system. The Intelligent Advisor, 3D Visualization, and reporting systems are consumers of Smart KPIs. The following systems are the dependencies:

-   **DataOps** - provides the Knowledge Graph data for the KPI calculation.

-   **Operations Hierarchy** - provides the primary means for contextualizing KPI Instances (providing the scope of the KPI Instances).

-   **People Management** - provides the user roles and departments for implementing the proper data permissions of the system.\
    See also the following Smart KPIs resources at [IX Developer Hub](https://industryxdevhub.accenture.com/assetdetails/42):



-   AOT Smart KPIs UI Guide

-   AOT Smart KPIs Administration Guide

-   AOT KPI Hierarchy and Calculation Technical Overview

## 

## Domain Model

-   

The Smart KPIs domain model consists of two parts, the configuration, and the operational models. The configuration domain model has just one entity, the KPI Definition. This entity defines the following topics of KPI configuration:

-   Definition of KPI

-   Role and department

-   Formulas for calculations

-   Application Context (which is primarily the list of assets for which the KPI is calculated)

-   Calculation frequency

-   Unit of Measure

-   Red Amber Green (RAG) Configuration

-   Status and version

-   Additional custom attribute

-   KPI Definitions that contribute to or influence other KPI Definitions

![The diagram titled "AOT Smart KPIs Configuration Domain Model" shows a central box labeled KPI Definition containing a list of attributes such as id, name, description, department, formulaActual, formulaForecast, formulaHistoricalBenchmark, formulaTarget, responsibleRole, assetHierarchyLevel, mappedAssets, calculationFrequency, sensitivity, status, version, dependentAssetHierarchyLevel, ragConfig, unitOfMeasurement, and attributes. To the right, two connected elements labeled Contributors and Influencers are linked to the KPI Definition box with cardinality indicators: "1" near KPI Definition and "\*" near Contributors and Influencers, showing one-to-many relationships. The layout illustrates how KPI definitions relate to contributors and influencers in the domain model.](media/image28.svg)\{width="4.546511373578303in" height="3.972315179352581in"\}

![The diagram titled "AOT Smart KPIs Operational Domain Model" shows a central box labeled KPI Instance with attributes such as id, name, description, isActive, roles, and attributes. It connects to two roles: Contributors and Influencers, with one-to-many relationships indicated by cardinality markers. To the left, boxes for Asset and Parameter define supporting elements, each linked to KPI Instance. At the bottom, a Numeric Timeseries box stores timestamped values and connects to KPI Instance for Actuals, Forecast, Historic benchmark, and Target data. Arrows illustrate relationships among assets, parameters, KPI instances, and timeseries, forming a structured operational model for KPI management.](media/image30.svg)\{width="8.452121609798775in" height="4.476744313210848in"\}

The operational model consists of two main entities (KPI Instance and Parameter), one auxiliary entity (Numeric Timeseries), and one entity from the Operations Hierarchy system (Asset).

The KPI instance is created based on a KPI Definition. Besides the generic information, it includes 4 timeseries (Actual, Historic benchmark, Target, and Forecast) stored as Numeric Timeseries, the Contributor and Influencer relationships towards other KPI Instances, and references to Assets for defining the context of the KPI Instance.

Parameters are information provided by external systems used in the calculation formulas of KPIs.

## 

## The Smart KPIs Full Domain Model

The full domain model is a combination of the configuration and operational domain models. The link between the two is realized by the relationship between the KPI Definition and KPI Instances.\
![The diagram titled "AOT Smart KPIs Domain Model" shows a hierarchical structure starting with a large box labeled KPI Definition, which lists attributes such as id, name, description, department, formulas for actual, forecast, historical benchmark, and target, plus roles, hierarchy levels, contexts, calculation frequency, sensitivity, status, version, RAG configuration, unit of measurement, and attributes. Below it, an arrow labeled Instances connects to a second box, KPI Instance, containing fields like id, name, description, isActive, roles, and attributes. KPI Instance links to Contributors and Influencers with one-to-many relationships, and also connects to Asset and Parameter boxes on the left, which define supporting data. At the bottom, a Numeric Timeseries box stores timestamped values and links to KPI Instance for Actuals, Forecast, Historic benchmark, and Target. Arrows and cardinality markers illustrate relationships among all components.](media/image32.svg)\{width="8.767442038495188in" height="9.12723097112861in"\}

## 

## Containers

This section explains how the Smart KPIs component of AOT is built using Cognite Data Fusion (CDF) for DataOps and AWS for hosting platform services and web applications. The diagrams illustrate the architecture, including Smart KPIs-specific containers, shared Platform Tools containers, and the AOT knowledge graph represented by the CDF data model. Key connections are highlighted in the diagram; refer to the legend for color codes.

Click the image to enlarge it.

![](media/image34.svg)\{width="6.815100612423447in" height="9.437402668416448in"\}

The tables below describe the role and functionality of the different components of the SmartKPIs module.

### Applications


| > **Name** | > **Responsibility** |
| --- | --- |
| > Smart KPIs Configuration Application | > The Smart KPIs Configuration Application is a standalone web application, which can be accessed by Smart KPIs admin users to configure the SmartKPIs calculation engine. It interacts with the Configuration API and microservice to read and write configuration to the system. |
| > SmartKPIs Dashboard Application | > The Smart KPIs Dashboard application is a micro-frontend application embedded into the AOT business application. It provides a visualization layer of the SmartKPIs on a Dashboard. It interacts with the SmartKPIs API and microservice to retrieve KPI data. |


### Microservices


| > **Name** | > **Responsibility** |
| --- | --- |
| > Smart KPIs microservice | > The Smart KPIs microservice is a data access microservice. It enables KPI data querying for authenticated users based on their role assignments. It is used by the SmartKPIs Dashboard application but also by other modules of AOT (Intelligent Advisor, 3D viewer, etc.) or 3^rd^ party consumers. |
| > Smart KPIs Configuration | > The Smart KPIs Configuration microservice enables admin users to read the current configuration of the Smart KPIs engine and then create/update/archive the configuration using Excel configuration templates uploaded to the system. These templates are processed by the configuration microservice and stored in AOT configuration storage. |
| > Smart KPIs Orchestrator | > The Smart KPIs Orchestrator microservice works based on the KPI configuration provided by the admin users. It is event-based, processing calculation events and, based on the formulas provided by the configuration and the different interdependencies between the KPIs the orchestrator, identifies when all requirements for a KPI calculation are met, and then triggers this KPI calculation. |
| > Smart KPIs Calculation Microservice | > The Smart KPIs Calculation microservice is responsible for calculating the KPI values based on the KPI configuration. It can evaluate the KPI calculation formula, read all the contributing values, and make the calculation which is then saved back to the AOT DataOps storage. This microservice can calculate actual, forecast, historical benchmark, and planned values of a KPI. |
| > Smart KPIs Data Permissions | > The data permissions microservice is triggered by the Orchestrator or by the Scheduler microservice, It makes the different KPI calculations of a KPI instance (actual, forecast, historical benchmark, planned) |
| > Notification | > The Notification microservice is a common microservice part of the Platform Tools of AOT. It facilitates communication between the AOT Backend and Frontend. It is used by the SmartKPIs engine to send notifications to the front end whenever a KPI calculation is completed. These notifications are used by the front end to refresh KPI data only if it changes. |


### Data Storage


| > **Name** | > **Responsibility** |
| --- | --- |
| > Cognite Data Model / Knowledge Graph | > Represents the different entities of AOT (Assets, KPIs, Insights, Actions, etc.) and the relationship between these entities. In the case of Smart KPIs each Smart KPI instance is represented as an entity in the graph, and it is contextualized to the asset it belongs to and to the other KPI instances which are contributors or influencers of this KPI and this KPI instance is a contributor/influencer for. |
| > Configuration Database | > Stores the current configuration of the SmartKPIs engine. |
| > Orchestration Database | > Stores the intermediate data and the status of KPI calculations. It is maintained by the Orchestration service. It can be used also as a log of past calculations. |
| > Template Storage Blob | > Blob storage is used to store the XLS configuration templates uploaded by the user. |


## Calculation Interactions

The diagram on the right shows the interaction between the system components when performing KPI calculations.

### Flow

1.  The Scheduler Microservice triggers the calculation functions for KPIs that have only parameter contributors.

2.  The calculation function reads the input values of contributor KPIs and Parameters

3.  The calculation function calculates the new KPI value

4.  The calculation function saves back the calculated KPI value to the Knowledge Graph

5.  The calculation function raises an event notifying subscribers about the newly calculated KPI.

6.  The KPI Calculation Orchestrator, which is subscribed to this event, receives it and updates the orchestration information (dependency list of other KPIs to the newly calculated KPI) in the Database

7.  The KPI Calculation Orchestrator reads the list of KPI calculations that can now be executed based on the previously calculated KPI values

8.  KPI Calculation Orchestrator triggers KPI calculation functions for the KPIs that have all dependencies already calculated


| > ![](media/image36.svg)\{width="9.40625in" height="8.479597550306211in"\} |


# 

## Deployment

Two diagrams have been created to illustrate where the system components are hosted in relation to one another. Click each image to enlarge it.

![](media/image38.svg)\{width="9.729166666666666in" height="9.522840113735784in"\}

# Operations Hierarchy

The Operations Hierarchy (OH) sub-system provides the means to store logical and physical operational units in the AOT Knowledge Graph, manipulate, and visualize them.

The OH is populated primarily from the source systems (other systems from the client ecosystem, responsible for defining daily operations). However, adjustments are also possible from within the AOT applications themselves. The OH is usually the backbone of the Knowledge Graph in a production environment, therefore, all the other business applications depend on it within AOT.

![The diagram titled "AOT Operations Hierarchy Context" shows a central red box labeled AOT Operations Hierarchy, which displays operations hierarchy and provides details for each node. Surrounding it are eight connected components: Operator (blue) for daily operations, Operations Hierarchy Configurator (blue) for configuring hierarchy, AOT Smart KPIs (green) for viewing KPIs and drill-down analysis, AOT Intelligent Advisor (cyan) for business insights, AOT 3D Visualizer (olive) for visualizing facilities in 3D, and AOT Reporting (green) for dashboards and reports. Below, AOT DataOps (blue) manages data ingestion and contextualization, and AOT People Management (purple) handles roles and assignments. Arrows indicate data flows such as retrieving asset hierarchy, associating KPIs, and saving roles for authorization. Color coding differentiates roles, hierarchy management, and reporting functions.](media/image40.svg)\{width="10.458333333333334in" height="5.502038495188102in"\}

## Domain Model

The Asset object is the only object in the OH domain model.

![](media/image42.svg)\{width="2.4145833333333333in" height="1.2951388888888888in"\}

## Operations Hierarchy on CDF and AWS

![](media/image44.svg)\{width="7.526192038495188in" height="9.28125in"\}

The tables below describe the role and functionality of the different components of the Operations Hierarchy module.

### Applications

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                         **Responsibility**
  ------------------------------------------------ --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Operations Hierarchy Configuration Application   Operations Hierarchy Configuration Application provides the possibility to configure the OH and the roles assigned to the nodes of it

  Operations Hierarchy Side-panel Application      The Operations Hierarchy side panel application is responsible for visualizing the OH as an advanced tree view. It is a micro-frontend application that needs to be embedded into a host application.

  Entity Viewer Application                        The Entity Viewer Application is responsible for showing detailed information about a selected node from the OH combining information both from the OH and other parts of the Knowledge Graph. It is a micro-frontend application that needs to be embedded into a host application.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Microservices

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                             **Responsibility**
  ---------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Operations Hierarchy Microservice                    This microservice is a data access microservice. It enables OH data querying for authenticated users based on their role assignments.

  Operations Hierarchy Configuration Microservice      The configuration microservice provides the possibility of configuring the OH and the roles assigned to the OH nodes.

  Operations Hierarchy Data Permissions Microservice   Whenever a role assignment to OH is changed an event is raised so that the PH Permission Manager microservice can apply the right permissions on the relevant OH nodes. Likewise, the DataOps platform is also raising events whenever changes are applied in the OH so that the OH Permission Manager can react to it by applying the right permissions.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Data Storage

  -----------------------------------------------------------------------------------------------------------------
  **Name**                                **Responsibility**
  --------------------------------------- -------------------------------------------------------------------------
  Cognite Data Fusion / Knowledge Graph   Stores the operations hierarchy as the backbone of the knowledge graph.

  Configuration Database                  Stores configuration for the Operations Hierarchy.
  -----------------------------------------------------------------------------------------------------------------

## 

## Deployment

The following diagrams show how the OH sub-system is deployed. Click the image to enlarge it.

![](media/image46.svg)\{width="7.305402449693788in" height="9.441824146981627in"\}

# Platform Tools

## Data Analytics Models

Data Analytics Models are algorithms that identify patterns for specific use cases in the data. There are multiple types of models, implemented and hosted in different ways. The AOT Data Analytics Model provides patterns to utilize these algorithms within the AOT solution.

One of the use cases of advanced analytics/machine learning models in AOT is to enhance the Intelligent Advisor microservice\'s ability to create predictions of the possible functional state of an asset and react accordingly to the output.

### Model Execution Pattern

The generic Data Analytics Model execution microservice provides a generic way of integrating models into the AOT solution. The following diagram shows the approach and the generic reusable components. Click the image to enlarge.

![](media/image48.svg)\{width="7.427083333333333in" height="7.389841426071741in"\}

### MLOps

Machine Learning Operations (MLOps) is a functionality of Machine Learning engineering that focuses on streamlining the process of deploying machine learning models into production reliably and efficiently and maintaining and monitoring them. MLOps contains different pipelines for developing, publishing, training, evaluating, and registering Machine Learning models. It also provides services that can be used to gather insights and analytical data about the models\' performances.

For the AWS variant, the training of the model is done in Azure ML Studio, and once the model is created, it will be deployed on AWS SageMaker and used by AOT.

The following diagram depicts the end-to-end process of ML model training, deployment, and execution.

![](media/image49.png)\{width="11.770833333333334in" height="5.7565387139107616in"\}

-   The process of training models must be fed with training data. ML Ops has connectors to other Azure resources for reading data.

-   Once the model is trained and the expected score is reached the model can be deployed into a Kubernetes service to be executed.

-   Execution of the model happens using the \"Data Analytics model execution service\".

-   The first example of such an integration is the Predictive failure model for Intelligent Advisor.

#### 

#### MLOps Model training

A training data set is used to train the model. This set is made up of information taken from different data sources which is then transformed and pre-processed so that it can be used for training. There can be subsets of data used for training, validation, or testing the model. As part of the training process, an appropriate algorithm must be chosen to train the model before its performance is evaluated using the validation and test steps.

Version control systems can be used to track changes to the code, data, or configuration files. This helps track the history of model evolution, giving the possibility to observe the performance over multiple versions of the model or start over from a specific version. After the model is evaluated and deployed, using analytical tools we can extract performance data and use it to retrain the model making it better.

![The diagram titled "AOT MLOps -- Learning Process" illustrates the machine learning lifecycle within an MLOps framework. At the top, a section labeled Machine Learning Data Source contains two blue boxes: Static files and Business data, representing input sources. Below, the Machine Learning (Re)training Pipeline shows four sequential steps in blue boxes: Train model, Validate model, Deploy model, and Monitor model, connected by arrows indicating workflow. A curved arrow loops back from Monitor model to Train model, labeled "Retrain model," showing iterative improvement. Color coding uses orange for section titles and blue for process steps, with a dashed border around the entire MLOps structure.](media/image51.svg)\{width="3.3959864391951005in" height="4.41558508311461in"\}

#### MLOps Model Deployment

The ML model can be deployed in a Kubernetes service in the following ways:

-   Direct deployment inside the Data Model microservice as a .pkl file that will be loaded into memory and executed inside that microservice.

-   Deployment in a separate EKS that will be exposed by an endpoint and consumed by the Data Model microservice through HTTP API.

-   Direct deployment of the model on an edge machine.

#### Model Execution

In AOT, ML model execution is controlled by the Data Model Microservice. This microservice listens for a message from an event hub (pushed either by an AOT or external system) that contains information such as the model type and identification data needed to execute the model. Then, based on the type, a specific handler will be invoked which takes care of calling the appropriate MLOps model, providing all the necessary data as input to execute it. When it completes, another message containing the result is pushed to the event hub which can be consumed by an AOT or external system.

![](media/image53.svg)\{width="6.293754374453194in" height="4.644014654418198in"\}

## 

## Internationalization and Localization

Internationalization refers to designing products so they can be easily used in various countries. Companies use this approach when expanding globally, recognizing that consumers in different regions may have unique preferences or behaviors.

Localization adapts a product or service to fit a specific language and culture, making it appear locally developed. Allow users to choose their preferred language for all AOT application front ends.

The best approach is to develop a platform-agnostic, microservice-based CMS that supports adding languages and translations at runtime. As a standalone component, it can be delivered and reused across applications.

The goal is for users to select their preferred language upon logging into the AOT Application Platform. The system should store these preferences in the localization system and use caching to ensure micro-frontends load translations only once at initialization, making just one database call.

Based on CMS System architecture, in the localization database, we store data across multiple tables:

-   A Languages table stores a list of languages and their ISO code (i18n) ex: en-US, es-PR, de-CZ.

-   The Translations table stores all the string assets from the application that will be mapped to a certain language ID providing a key to identify the element with a unique name in the UI and the corresponding language translation.

-   A User preferences table that stores the user-chosen language for the AOT UI.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                                 **Responsibility**
  ---------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Localization Configuration Application   The application makes it possible to manage UoM systems for AOT.

  Localization microservice                The microservice makes it possible to manage and retrieve information about AOT UoM systems. The individual business applications of AOT use it for calculating and displaying data with the users\' desired UoM system.

  Localization Configuration Database      Stores UoM configuration.
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The container diagram below provides insights into how to use the internationalization component across AOT.

![](media/image55.svg)\{width="6.451544181977253in" height="6.863099300087489in"\}

### 

### Deployment

![](media/image57.svg)\{width="14.0in" height="4.08125in"\}

## Scheduling service

The Scheduler Service in AOT is a microservice in Python that is implemented in a multiprocessing/multi-thread manner. All tasks that need to be executed will be stored as scheduler configurations in the SQL Database.

The API of the microservice exposes the possibility to create, modify, and delete tasks. Every time a task is created the scheduler instantiates and schedules the task to run at the desired time. When a task is modified the scheduler determines the process of the current task and stops it and then instantiates a new task with the new settings. When a Task is deleted, the scheduler identifies its process and terminates it. Every Task operation is also reflected in the database configuration of the scheduler. When a task is executed, it raises an event as a message through the Message Broker and then writes an execution log to SQL Table to use later in case of system stop/restart. When the system starts/restarts, the Microservice loads all the tasks to be executed.

![](media/image59.svg)\{width="5.485321522309711in" height="6.480975503062117in"\}

### 

### Microservices


| > **Name** | > **Responsibility** |
| --- | --- |
| > Scheduler Microservice | > This microservice has the role of triggering events based on user-defined schedules. It exposes an API to set up the required scheduler jobs and when, based on the configuration, the time elapses it creates the triggering messages, which are sent to a Kafka topic. These events are consumed by subscribers to the topic which triggers business logic in the backend (KPI calculations, Insight creation, etc.) |


### Data Storage


| > **Name** | > **Responsibility** |
| --- | --- |
| > Scheduler Configuration Database | > Stores the scheduler configuration and historical information about scheduler executions. |


# 3D Visualization

As shown in the diagram below, the 3D system of AOT provides 3D visualization of the Plant(s) with contextualized data (KPIs and Insights) displayed on the 3D model with the possibility to drill down inside the visualization.\
The 3D module has two main components:

-   A 3D Visualizer Micro-Frontend integrated into the AOT business app

-   A 3D Builder application where the 3D model can be configured and the data from the Knowledge Graph contextualized to it.

![The diagram titled "AOT 3D Visualizer Context" shows a central black box labeled AOT 3D Visualizer, which visualizes facilities and processes in 3D using context data from the Operations Twin. At the top, two blue boxes represent user roles: Operator, who views 3D models and context data, and 3D Configurator, who uploads and configures models. Surrounding the visualizer are five connected components: AOT Intelligent Advisor (green) for insights and actions, AOT Smart KPIs (green) for KPI analysis, AOT People Management (purple) for managing roles and departments, AOT Operations Hierarchy (red) for hierarchy details, and 3DCE Core (gray) for 3D model content management. Arrows indicate data flows such as reading KPIs, roles, hierarchy, and insights. Color coding differentiates roles, visualization, and supporting systems.](media/image61.svg)\{width="8.606068460192477in" height="6.376213910761155in"\}

See also: [3D Builder and Viewer Architecture Blueprint](https://industryxdevhub.accenture.com/assetdetails/47)

##  Consumers and Dependencies

Operators and 3D Configurators are the usual users of the 3D system. They can explore the 3D models with contextualized data in the case of Operators or configure the visualization itself by setting the layout of plant(s), connections between the different models, and adding the data context links to build up the visualization. Dependencies for 3D visualization include Operations Hierarchy, People Management, Smart KPI, and Intelligent Advisor.

## 

## Implementation

In this detailed architecture, we describe how is AOT implemented on top of Cognite Data Fusion combined with AWS services. CDF provides the DataOps services, while AWS is the place for hosting the AOT platform services and web applications. The tables below describe the role and functionality of the different components of the 3D module:

### Applications

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                               **Responsibility**
  -------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  3D Visualizer Application              It is a micro-frontend application that is integrated into the AOT Business Application, and it has the role of displaying the 3D models of the Plant or any other asset from the hierarchy. It also provides all the contextualized data of the asset and provides the users with the drill-down functionality, going deeper into the 3D model to see the subcomponents of the model and the contextualized data.

  3D Builder/Configuration Application   This is a stand-alone micro-frontend application that combines all the tools necessary to upload, manage, enhance, and contextualize 3D models and create layouts from these models. The different tools are Unity3D and/or React-based components which enable Model Management, Point of Interest editing/mapping, Model mapping, and Twin builder.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Microservices

  ---------------------------------------------------------------------------------------------------------------------------------------------------------
  **Name**                        **Responsibility**
  ------------------------------- -------------------------------------------------------------------------------------------------------------------------
  3D Configuration Microservice   This microservice provides access to the saved data (3D models, mappings, etc.) and the possibility to modify the data.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------

### Data storage

  --------------------------------------------------------------------------------------------------------------
  **Name**                         **Responsibility**
  -------------------------------- -----------------------------------------------------------------------------
  3D Models and Mappings Storage   Stores 3D visualization-related data (3D models, mapping files, POI, etc.).

  --------------------------------------------------------------------------------------------------------------

Both the CDF and AWS architectures of 3D Builder and Viewer consist of:

-   containers that are specific to the 3D module.

-   containers that are common and shared, hence provided by the Platform Tools.

-   the different other modules of AOT (Smart KPIs, Intelligent Advisor, Operations Hierarchy, etc.) providing the data to be displayed on the 3D View.

The diagram below describes the individual components of the system with the most relevant connections highlighted. Check the legend of the diagrams to learn the color coding. Click the image to enlarge it.

![](media/image63.svg)\{width="13.706902887139108in" height="9.384555993000875in"\}

## Deployment Diagrams

![](media/image65.svg)\{width="5.133944663167104in" height="9.137952755905511in"\}

![](media/image67.svg)\{width="4.713030402449694in" height="9.17211832895888in"\}

# People Management

The role of the People Management (PM) module is to enable admin users to administer a user\'s access to data and functionality in the platform. The People Management Configuration Application allows admin users to create and manage AOT Roles, link active directory groups to AOT Roles, and change user permissions.

![The diagram shows a simple relationship flow for user access mapping. It starts with a box labeled Users, which "belongs to" AD Groups. AD Groups are "linked to" AOT Roles, and AOT Roles are "mapped to" Data. An additional arrow connects Users directly to AOT Roles with the label "linked to." All boxes and arrows are green, and the layout is linear from left to right, illustrating how user membership in Active Directory groups determines role assignments and ultimately data access.](media/image68.png)\{width="9.0in" height="1.0931813210848644in"\}

## Components

-   Functional permissions: Permissions to access configuration pages of various components. Access to configuration screens will be restricted to only users with admin roles.

-   Data permissions: Permission defined to AOT business objects (asset hierarchy, KPIs, Insights, etc.) based on roles and responsibilities. The users have access only to the data their roles are mapped to.

Data permissions are managed using custom metadata entries on each CDF object (e.g., Asset, Timeseries, Events, etc.) inside the Knowledge Graph. All the Roles that have owner or viewer access to that object will have the access rights represented on the object\'s metadata.

Managing these metadata entries on the objects is the responsibility of the module the data belongs to (e.g., KPIs which are represented as Timeseries in the Knowledge Graph will be managed by the SmartKPIs module). The access rights of an object might be influenced by the access rights of objects from another module (e.g., Insights linked to KPIs will influence the access rights of the KPI objects).

Since data permissions in AOT are influenced by changes happening in different modules and changes on a data object of one module may impact the data permissions of an object in a different module, we have introduced an event-driven change feed architecture, where each AOT module can publish their changes related to data permissions (e.g. owner changed, etc.) of objects and any dependent module can subscribe to these changes and update the data permissions of its objects accordingly. This change feed consists of:

-   Event Broker that stores the published events and notifies the subscribers of any new events

-   Event Publisher microservices, which publish module-related configuration or object create/update events to the Message Broker

-   Event Subscriber microservices, which process the events from the feed and make the necessary data permissions-related updates to the relevant objects.

##  Layers

-   People Management Configuration UI: interface provided to admin users where AOT Roles can be created and managed, different Active directory groups can be linked to AOT Roles, user permissions can be changed, etc.

-   People Management APIs and Backend services: enable querying and updating of User and Role information, mapping the Roles to Active Directory Groups, checking of user authorizations, etc.

-   All AOT backend services will use People Management services/APIs to determine the exact data access the AOT user has and limit the returned datasets only to the data accessible by the user based on their role.

-   CDF DataOps platform: where the data is stored and tagged (in CDF resource metadata) with all the relevant information, enabling the user to access the data and also determines the level of access (read/write)

For user Authentication Azure Active Directory is used. In AWS API Gateway all API calls are authorized using a validation function that checks if a valid JWT token generated by Azure AD is present on the request.

For user Authorization, each AOT micro-frontend will need to determine the user\'s access privileges to the functionality and data based on the user\'s AOT roles. There are two ways a user can be linked to AOR roles, thus have access to AOT applications and data:

-   the user is a member of at least one AD Group, which is assigned to at least one AOT role

-   the user is directly assigned to a Role in AOT

To enable fast authorization of the user to AOT, each microservice needs to store a local cache of user roles and AD group-role mappings.

See also: [AOT People Management Architecture Blueprint](https://industryxdevhub.accenture.com/assetdetails/64)

## System context

People Management stores the assignments of users and groups to AOT roles and departments. It is being used by most of the AOT systems and plays an important role for data access and roles assignment.

![Diagram showing People Management at the center, managing roles and access for users and groups, with connections to Smart KPIs, Intelligent Advisor, 3D Visualizer, Operations Hierarchy, and Reporting modules.](media/image70.svg)\{width="13.15625in" height="5.708333333333333in"\}

**\
**

## Containers

This section explains how AOT is implemented on top of AWS services.

The following diagrams show the details of the AWS-based People Management architecture including:

-   containers that are specific to People Management

-   containers that are common and shared, hence provided by the Platform Tools

-   integration with the Identity Provider (in this case Azure Active Directory)

The following container diagram describes the individual components of the system, with the most relevant connections highlighted.

### Applications

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  People Management Application   This application allows People Management Configurator admin users to configure the roles assignments in the scope of AOT for users and groups
  ------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Microservices

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  People Management microservice   The Smart KPI, Intelligent Advisor, 3D Visualization, Operations Hierarchy, and the Reporting systems are the consumers of the role mapping from People Management because all these systems need to validate each interaction with the signed-in user based on the users\' roles. Therefore, this service provides the APIs needed for these operations.
  -------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Notification Service             It pushes notifications to People Management application whenever changes are made.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Data storage

  ----------------------------------------------------------------------------------
  People Management Database   Stores AOT users, roles, and departments.
  ---------------------------- -----------------------------------------------------

  ----------------------------------------------------------------------------------

![](media/image72.svg)\{width="6.345750218722659in" height="7.016666666666667in"\}

**\
**

## Deployment diagrams

The following two deployment diagrams explain where each of these system components are hosted.

[Diagram without connections]\{.underline\}

![](media/image74.svg)\{width="4.5333497375328085in" height="7.688288495188101in"\}\
[Diagram showing communication connections]\{.underline\}

![](media/image76.svg)\{width="4.022939632545932in" height="7.506449037620297in"\}

# 

# Reporting

AOT reporting system allows creating reports in third-party tools taking data from AOT, but also provides framework to embed these reports into the AOT Business Application in cases needed.

## System context

The reporting modules will read data from the AOT Knowledge Graph through the AOT APIs, primarily from Operations Hierarchy, Smart KPIs, and Intelligent Advisors. It will also use the People Management module for restricting permissions to content.

![Diagram showing reporting modules reading data from knowledge graph, Operations Hierarchy, Smart KPIs, Intelligent Advisor, and People Management for permissions.](media/image78.svg)\{width="7.772804024496938in" height="4.40625in"\}

##  Containers

As shown in the container diagram, the following components make up the system.

In this case, the report configurator will create the report in Power BI, integrate data from AOT backend into it, and publish it to make it available online. Next step is to configure the AOT reporting application to know about this online report.

After the configuration is done, generic users having the necessary permissions can visualize in the AOT Business Application the reports.

###  Applications

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Reporting Application                 This application makes possible embedding reports provided by external platforms into AOT Business Application and navigating between them.
  ------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------
  Reporting Configuration Application   This application makes it possible configuring reports provided by external platforms to be shown in the Reporting Application.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Microservices

  ---------------------------------------------------------------------------------------
  Reporting Configuration Microservice   Stores reporting configuration information.
  -------------------------------------- ------------------------------------------------

  ---------------------------------------------------------------------------------------

### Data storage

  -----------------------------------------------------------------------------------
  Reporting Configuration Database   Stores reporting configuration information.
  ---------------------------------- ------------------------------------------------

  -----------------------------------------------------------------------------------

![](media/image80.svg)\{width="11.46875in" height="7.70900043744532in"\}

# Applications 

The AOT application pages can be divided into two categories: Business and Configuration.

The diagram below shows the AOT Application landscape. Click the image to enlarge it.

![The diagram titled "AOT Micro-Frontend Dependency Structure" shows a browser-based architecture for AOT applications. At the top, a Browser Local Storage component connects to multiple Micro-Frontend Dependency Resolvers, each representing a feature such as Operations Hierarchy, Smart KPIs, Insight Details, 3D Visualizer, Intelligent Advisor Skills Panel, and Reporting Widgets. Each resolver is linked to an AOT Service Provider layer that handles authentication and navigation. Below, corresponding applications include Reporting Configuration, People Management Configuration, Smart KPI Configuration, Intelligent Advisor Configuration, 3D Editor, and Operations Hierarchy Configuration, all integrated with the service provider for authentication and navigation. At the bottom, arrows point to AOT API and Push Notification Service, indicating backend communication. Color coding differentiates micro-frontends, service providers, and configuration applications, while arrows show data flow between layers.](media/image82.svg)\{width="14.197158792650919in" height="8.162790901137358in"\}

## Host App

The AOT Host App is built from embedded micro-frontend (MFE) applications. Each MFE has a well-defined purpose and is viable on its own. The AOT Host App is responsible for hosting the embedded MFEs, ensuring authentication, and channeling information between components. It is also responsible for facilitating navigation logic, resolving dependencies, and maintaining the URL.\
**Embedded MFEs**


| > **Name** | > **Description** |
| --- | --- |
| > Operation Hierarchy | > A side panel with a tree view displaying the asset hierarchy. |
| > Smart KPI | > Displays the list of the calculated actual, forecasted, and historical KPI values for the selected asset, along with the description, calculation formula, and trendline charts. It is possible to drill down for a selected KPI to view the details of the influencing and contributing KPI values. |
| > Intelligent Advisor Side Panel | > Displays the list of active Insights in a side panel. |
| > Insight details | > Displays the details of a selected insight from the side panel, such as description, actions, contributors, and even KPI details if the insight was generated based on one. |
| > 3D Visualizer | > Displays the 3D model of a plant or area configured in the 3D editor, along with adding insight, actions, and alerts on top of it. |
| > Entity Viewer | > Displays a detailed dashboard for a selected asset. |
| > Reporting | > This visualizes reports defined in the system. |


## 

## Configuration Apps

The AOT Configuration applications are a set of stand-alone MFE applications that allow the configuration of specific modules.

###  Stand-alone MFEs


| > **Name** | > **Description** |
| --- | --- |
| > Smart KPI Config App | > Allows the configuration of Smart KPIs either by uploading an Excel file or by configuring the KPIs manually. The user can download the Excel template for the base KPI configurations via file download. It is also possible to download the current configuration as an Excel file. The KPI configurations can have various statuses and when published, they become available in CDF for use. |
| > 3D Editor App | > The 3D editor defines a plant or area layout as a 3D model, which can be viewed and analyzed in the 3D viewer. |
| > Intelligent Advisor Config App | > Allows the user to maintain the insight category and template configuration used by Intelligent Advisor. |
| > People Management Config App | > The role of the People Management module is to enable admin users to administer a user\'s access to data and functionality in the platform. |
|  | > |
|  | > The People Management Configuration Application allows admin users to create and manage AOT Roles, link Active directory groups to AOT Roles, and change user permissions.\ |
|  | > People management has two components: |
|  | 1. Functional permissions to access the configuration pages of various components. This will be a custom development and is part of AOT. |
|  | 2. Data permissions defined to data points inside CDF (asset hierarchy, KPIs, Insights, etc.) that are based on roles and responsibilities. The users have access only to the data to which their permissions are mapped. |
| > Reporting Configuration Application | > This configures reports to be presentable in AOT. The reports are preconfigured in their environment (currently PowerBI), however, whether they are visible and to whom are visible are controlled by AOT. |


# 

# Appendix

## Guiding Principles

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Principle**               **Meaning**
  --------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Keep it short and simple    Minimize the number of capabilities to fulfill the requirements and select a component landscape that is easy to develop, lightweight in run-time, and cost-effective to operate.

  Don\'t repeat yourself      Reuse components and consolidate the component selection based on their reusability potential through the component landscape.

  Fit for purpose             The solution should do what it needs to do -- no more and no less.

  Don\'t reinvent the wheel   Look for all technology options for each capability that you need to implement and choose a packaged or open-source solution before considering a custom solution.

  Prepare for failure         Recognize that every component, every process, and every person in your solution might become unavailable, and design the solution in a way that gracefully handles those situations. Evaluate failure modes and design a remediation that balances the cost of prevention with the cost of failure.

  Divide and conquer          Define precise interfaces between applications to improve maintainability. Separate different functions from each other and implement them in separate components.

  Black box                   Don\'t expose the implementation details of one component to another. Define interfaces between functional components and hide implementation complexity behind the interfaces.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Patterns


| **Pattern** | **Description** |
| --- | --- |
| Micro-frontends | Individual features are going to be implemented as separate stand-alone micro-frontend applications. |
|  | - The configuration applications are going to be completely stand-alone, while the different distinct components of the business application are implemented as embeddable micro-frontend applications. These are loaded into the main web application as independent units. |
|  | - All micro-frontend applications can be developed individually by different teams, without following any restrictions for the other components. |
|  | - The embeddable micro-frontends perform synchronization and data exchange between each other through a standardized way using event-based publish-subscribe communication. |
| Stateless middleware | Each execution starts from scratch without any contextual knowledge of the previous execution |
| Operations data in Cognite | Using CDF as a backend provides a contextualized way to store the operations data. |
| Lazy loading/initialization | Objects are initialized at the first usage, instead of a time and resource-consuming initialization phase. |
| Event-based asynchronous | This enables the advantages of multithreaded applications while hiding many of the complex issues inherent in the multithreaded design. Using a class that supports this pattern can allow the execution of long-running tasks in the background without blocking tasks, running multiple tasks in parallel, and waiting for available resources. |
| Publish-subscribe | This is a messaging pattern where senders of messages---called publishers---do not program the messages to be sent directly to specific receivers---called subscribers---but instead categorize published messages into classes without any information about the subscribers. The subscribers decide on the reception of the different data by subscribing to different topics. |
| Adapter pattern | By applying this pattern to containers, communication between containers is kept consistent. Having a standard way of communicating via a set of contracts helps to make requests in the same way and lets the user expect the same response format. |

