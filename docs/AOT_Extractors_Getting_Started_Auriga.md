---
id: aot-extractors-getting-started-auriga
title: AOT Extractors Getting Started Auriga
---

# Getting Started with Extractors

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including data integration extractors, that are assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT includes configurable Extractors – also known as data integration accelerators – that are designed to extract data from a client source system into Cognite Data Fusion (CDF) RAW.

The extractors contain reusable code developed with the Cognite Custom Extractor framework, can be readily deployed either in the cloud or on-premises.

The source system stores both information technology (IT) and operational technology (OT) data such as asset hierarchy, work order, real-time series, diagrams, and 3D models on the client side.

If there is a change in the Asset hierarchy information from the source system, the client can request to extract information to get the latest data. By changing the configuration information in the build, the client can trigger the instance of the application so that the requested asset hierarchy information is extracted and saved in CDF staging tables.

AOT Extractors are built using combinations of Microsoft Azure Services, Cognite’s Extractor Framework, and Python. The Extractors are triggered as needed to pull data from client source systems (SAP PM, PI AF, Hexagon, AVEVA, Bentley) and then push the data into CDF RAW. Cognite Python SDKs or other Extract, Transform, and Load (ETL) tools such as Azure Data Factory can also be used to develop a custom extractor to pull data from other unsupported source systems.

## Purpose

This document describes the prerequisites, user journey for setting extractors and links to the related detailed deployment documents.

## Audience

- Business Analysts

- Solution Architects

- Technical Architects

- Asset Delivery teams

## Prerequisites

- The source system and interface must be known.

- The service accounts must already exist.

- The permissions to connect the source system instance to the extractors must be granted.

The prerequisites listed above are specific to the Extractors component. For information about general prerequisites, see the [AOT Getting Started](https://industryxdevhub.accenture.com/assetdetails/75). document.

##  Contacts

- ``

- ``

- ``

## Related Links

- [DevOps Wiki](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_wiki/wikis/Marilyn-V.wiki/1571/Extractors)

- [Cognite API](https://docs.cognite.com/api/v1/)

- [Cognite RAW](https://docs.cognite.com/api/v1/%22%20%EF%BF%BDHYPERLINK%20%22https://docs.cognite.com/cdf/integration/guides/extraction/raw_explorer/)

- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| **Term** | **Definition** |
|:---|:---|
| AOT (Accenture Operations Twin) | A suite of software accelerators and tools designed to integrate product, process, and live data from various IT and OT systems, providing a comprehensive view of operations for better decision-making. |
| Extractor | A configurable data integration accelerator that extracts data from client source systems and loads it into Cognite Data Fusion (CDF) RAW. Built using Cognite’s Extractor Framework, Azure Services, and Python. |
| Cognite Data Fusion (CDF) RAW | The data storage layer in Cognite’s platform where extracted data from source systems is staged for further processing and analysis. |
| IT Data | Information Technology data, such as asset hierarchies, work orders, and diagrams, stored in client systems. |
| OT Data | Operational Technology data, including real-time series, 3D models, and other operational information from client systems. |
| Source System | The original system (e.g., SAP PM, PI AF, Hexagon, AVEVA, Bentley) from which data is extracted using AOT Extractors. |
| Cognite Custom Extractor Framework | A development framework for building reusable extractors that connect to various source systems and transfer data to CDF RAW. |
| Azure Data Factory | A cloud-based ETL (Extract, Transform, Load) tool from Microsoft Azure, used to develop custom extractors for unsupported source systems. |
| ETL (Extract, Transform, Load) | A process for extracting data from source systems, transforming it as needed, and loading it into a target system like CDF RAW. |

# User Journey

The following diagram illustrates the user journey for Extractors.

Establish and validate connection between extractors and source system

Establish and validate internal connections between Pipeline and environment

Configure the extractor parameters such as frequency and data specifics

Configure and schedule transformation logic in CDF

Ensure environment readiness with all prerequisites / resources

a

**Accenture Delivery Team**

**Client IT Team**

Test connection between source to connector to RAW

Deploy the extractor

Assess and identify source systems

Facilitate access to source system

# 

# Resources






``

``
Document
Description
Topic/Page Number
``
``

``
AOT Extractors Architecture Blueprint
Describes the functionality, architecture, and availability of the AOT data integration accelerators.
`SAP PM Extractor - 5`
PI AF Extractor - 6
Hexagon Extractor - 7
Flat File Extractors - 8
Availability Matrix - 9
``
``
AOT SAP PM AH Extractor Deployment Guide
This document explains the process of extracting data from the source and pushing it into CDF RAW. Also addressed in the document are the prerequisites that must be fulfilled before the Extractor can be deployed as well as the steps to configure and deploy the Extractor either in the cloud or on-premises. After reading this document, a developer should be able to configure and run the extractor as well as verify the data flow from the source system to CDF.
`SAP PM Configuration - 4`
Function Module - 4
Open Data Protocol - 6
Transport and Package - 8
Cloud Deployment - 10
Configure Azure DevOps - 10
Build Pipeline - 14
Release Pipeline - 16
On-Prem Deployment - 19
Extractor Installation - 19
Extractor Start Procedure - 22
Extractor Stop Procedure - 23
``
``
AOT SAP PM WO Extractor Deployment Guide
This document explains how to extract data from the source system and load it into CDF RAW. It also covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF. The objective is to obtain Work Order details from SAP and make them available as an OData service for the Python extractor to consume and store in Cognite Staging areas.
`Architecture Diagram – 3`
SAP WO Configuration – 5
Function Module - 5
Open Data Protocol - 8
Transport and Package Creation - 10
Cloud Deployment - 12
Configure Azure DevOps - 12
Build Pipeline - 17
Release Pipeline - 19
On-Prem Deployment - 25
Extractor Installation - 25
Extractor Start Procedure - 28
Extractor Stop Procedure 29
``
``
AOT PI AF Extractor Python Deployment Guide
This document explains how to extract data from the source system and load it into CDF RAW using the PI AF extractor. It covers the prerequisites for deploying the Extractor, provides instructions for configuring and deploying it in the cloud, and enables the reader to verify the data flow from the source system to CDF.
`Cloud Deployment - 5`
Prerequisites - 5
Configure Environment – 6
Build Pipeline - 11
Release Pipeline - 13
On-Prem Deployment - 17
Prerequisites - 17
Installation - 17
Start Procedure - 20
Stop Procedure - 22
``
``
AOT Hexagon Extractor Deployment Guide
This document explains how to extract data from the source system and load it into CDF RAW. It covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it either in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF.
`Hexagon SDx Configuration – 4`
Cloud Deployment – 15
On-Prem Deployment - 24
``
``
AOT Flat File Extractor Deployment Guide
This document explains how to extract data from the source system and load it into CDF RAW using the Flat File extractor. It covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it either in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF.
`Features – 4`
Cloud Deployment – 5
On-Prem Deployment – 15
``
``
Automatic Asset Hierarchy Accelerator Deployment Guide
This document explains how to configure and run the automatic asset hierarchy element and verify the resulting transformation and asset hierarchy, events, relationships, or label actions in CDF. It also provides an understanding of the process of configuring the automatic asset hierarchy element and validating it in CDF. After reading the document, a developer should be able to perform these tasks successfully.
`Prepare Azure - 5`
Prepare Accelerator Config File - 7
Cognite Parameters - 7
Transformation Parameters - 8
Extraction Parameters - 9
Create a Build Pipeline - 10
Create a Release Pipeline - 12
Result - 17
``
``
AOT Simulator and IoT Hub Extractor Deployment Guide
This document explains the prerequisites and steps to configure and deploy the simulator on the cloud including the understanding of configuring the device twin to send data to IoT Hub.
`Simulator Deployment – 4`
IoT Hub Extractor Deployment – 12
Simulator Usage – 17
First-time Configuration – 21
Changing Attribute Value of a Device - 21
``
``
``

### Metadata Table

| **Field** | **Value** |
|:---|:---|
| **Asset / Solution Name** | Accenture Operations Twin / Data Integration Accelerators |
| **Domain / Area** | Extractors / Data Processing |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Joshi, Rishabh |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | AOT Extractors Architecture Blueprint |
