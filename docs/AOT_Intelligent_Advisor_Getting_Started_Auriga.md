---
id: aot-intelligent-advisor-getting-started-auriga
title: AOT Intelligent Advisor Getting Started Auriga
---

# Getting Started with Intelligent Advisor

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including Intelligent Advisor, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The Intelligent Advisor (IA) is an AOT component and an AI-based solution that enables different types of users to focus on critical issues with real-time-generated, prioritized, and contextualized insights and recommendations. It combines the following functional components: Insight generation engine, collaboration, Actions, Advisor panel, Insight Viewer template, and Insight lifecycle management.

## Target Audience

- Client Delivery Teams Leveraging AOT Intelligent Advisor

- Asset Delivery Teams

- Business Analysts, Solution Architects, Technical Architects, Data Scientists, Data Engineers

## Contacts

- ``

- ``

- ``

- ``

- ``

- 

- `susarla.aditya@accenture.com`

## Related Links

- [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

- [AOT on AWS](https://hostapp-aws.accenturedigitalplant.com/)

- [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

- [AOT IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

## Glossary

| **Term** | **Definition** |
|:---|:---|
| AOT (Accenture Operations Twin) | A collection of software accelerators and tools designed to integrate product, process, and live data from various IT and OT systems, providing a comprehensive, contextualized view of operations for better decision-making and optimization. |
| Intelligent Advisor (IA) | An AI-based solution within AOT that generates real-time, prioritized, and contextualized insights and recommendations for users. Includes insight generation engine, collaboration, actions, advisor panel, and lifecycle management. |
| Insight Generation Engine | The core component of IA responsible for producing actionable insights from integrated data sources. |
| Advisor Panel | A user interface element that displays filtered insights based on user roles. |
| Insight Viewer Template | A customizable template for visualizing insights within the IA platform. |
| Insight Lifecycle Management | Processes and tools for managing the creation, review, and archiving of insights throughout their lifecycle. |
| CDF (Connected Digital Framework) | A platform used to configure and visualize insight categories, asset hierarchies, and other operational data. Integrated with AOT and IA for backend and frontend operations. |
| AWS | Amazon Web Services is Amazon's on-demand cloud computing platform used to host AOT and IA microservices. |
| Azure | Microsoft’s cloud computing platform, used to host and execute models, configure insights, and integrate with AOT and IA. |
| KPI (Key Performance Indicator) | A measurable value that demonstrates how effectively an organization is achieving key business objectives. Smart KPI components must be deployed for KPI-based insights. |
| ML (Machine Learning) Model | A predictive algorithm trained on contextualized data to generate insights. ML models must be created, trained, and deployed in specific formats (e.g., .pkl) for use in IA. |
| Template Viewer | A UI component for displaying insights by category, configured in CDF. |
| Smart KPI Configuration | The process of setting up KPI-based insights, including time series creation and component deployment. |
| Asset Hierarchy | The structured organization of assets (e.g., functional locations) used for contextualizing data and insights, often synchronized between SAP and AOT. |
| SAP | An enterprise resource planning (ERP) system that must be integrated with AOT for asset hierarchy and data communication. |
| People Management Component | A module that manages user rights and access within AOT and IA. |
| ML Ops Toolchain | A blueprint for integrating Azure machine learning infrastructure with AOT’s Intelligent Advisor framework, covering design patterns, workflows, and architecture. |

# Intelligent Advisor User Journey

[Train the model (Python)](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_Delivery_Guide_2_5.pdf)

IA Engine

**Client / Accenture Data Scientist**

**Accenture Delivery Team**

**Client Business User**

[Identify/develop data science algorithm](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_Delivery_Guide_2_5.pdf)

[Host and execute model in Azure](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_Delivery_Guide_2_5.pdf)

Configure insight categories in  
[CDF](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_Delivery_Guide_2_5.pdf) [Azure](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Azure_Intelligent_Advisor_Delivery_Guide_2_5.pdf) [AWS](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_AWS_Intelligent_Advisor_Delivery_Guide_2_5.pdf)

[Create Template viewer for each category - CDF](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_Delivery_Guide_2_5.pdf)

[Define Insight category from flat file](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_Delivery_Guide_2_5.pdf)

[Investigate Insight through Insight details](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_UI_Guide_2_5.pdf)

[View Insights in Advisor panel (duly filtered by role)](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Intelligent_Advisor_UI_Guide_2_5.pdf)

Smart KPI Configuration

AOT Login



**Azure**



**AWS**

**AWS**

**Azure**

**CDF**

**Azure**

**CDF**

**CDF**

# Resources

The documents listed in the table are also available at the [IX Developer Hub](https://industryxdevhub.accenture.com/assetdetails/43).






``

``
Document
Description
Important Topics
``
``

``
`AOT Intelligent Advisor Delivery Guide`
AOT Azure Intelligent Advisor Delivery Guide
AOT AWS Intelligent Advisor Delivery Guide
This document describes the end-to-end process of creating and maintaining insight categories, configuring insights, and defining Insight viewer templates.
`Generating Insights`
Create Insight Category Hierarchies
Leverage Azure and CDF to Generate Insights
Archiving Insights
UC1 – Predicting Control Valve Failure
UC2 – Smart KPI for OEE
Create a User Interface Template
(Topics are similar in the Azure and AWS versions of the document)
``
``
AOT Intelligent Advisor UI Guide
This guide explains how to use AOT’s Intelligent Advisor UI with Template Viewer.
`IA Applications – 5`
Main Application – 6
Intelligent Advisor Panel – 6
Operations Hierarchy Panel – 7
Digital Twins Panel – 7
Insights - 8
Actions - 17
Template Viewer - 25
Insight Details - 26
Recommendations - 27
Related Actions - 27
More Details - 28
``
``
Intelligent Advisor Configuration UI Guide
This guide explains how to use AOT’s Intelligent Advisor Configuration UI.
`Launch the Configuration UI – 5`
IA Configuration Landing Page – 6
Configure Insights – 8
Predictive Failure Configuration – 13
Custom Insight Category – 21
``
``
Intelligent Advisor API Reference
This reference document includes information about paths, inputs, outputs, and error management for APIs related to AOT Intelligent Advisor. The document includes descriptions of APIs used for configuration as well as descriptions of APIs that provide middleware functionality
`Event Data APIs – 4`
Configuration APIs – 7
ML Model Microservice APIs -11
``
``
ML Ops Toolchain Blueprint
This document provides an overview of the Azure machine learning infrastructure and describes how to integrate it with AOT’s Intelligent Advisor framework.
`MLOps Design Patterns – 4`
What is MLOps Azure – 4
MLOps Versus DevOps – 4
Architecture – 5
MLOps Workflow Pipeline - 7
``
``
``

# 

# Prerequisites

The prerequisites listed below are unique to Intelligent Advisor. For general prerequisites, see [AOT Getting Started](https://industryxdevhub.accenture.com/assetdetails/75). Before using AOT, the delivery team must:

1.  Create and configure Insight Categories (e.g., KPI-based or ML-based) on the back end. Without Insight Categories, users would not be able to configure insights.

    - For KPI-based insights:

      - The Smart KPI component must be deployed.

      - KPI time series needs to be created.

    - For ML-based insights:

      - Input data for ML models must flow into CDF, contextualized to the appropriate asset hierarchy level against which the ML model will be executed.

      - The list of assets for which the ML model can be configured must be provided in the Template by a Data Scientist.

      - ML model must be created and trained outside of CDF.

      - ML models must be available in the pkl format and deployed in the microservice.

2.  Create the relationship between Insight Categories and Templates in CDF. This is necessary to visualize the details at the front end.

3.  The [People Management component](https://industryxdevhub.accenture.com/assetdetails/64) must be configured to ensure that users have the appropriate rights.

4.  Configure the end system (e.g., SAP):

    - The SAP instance should be in place.

    - Access and communication have been established between SAP and AOT.

    - Asset hierarchy (functional location) from SAP matches AOT asset hierarchy.  
      Metadata Table

| **Field** | **Value** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin / Intelligent Advisor |
| **Domain / Area** | Advisory / Decision Automation |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Zoltani, Judit-Kinga |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Intelligent Advisor UI Guide, Intelligent Advisor Delivery Guide |
