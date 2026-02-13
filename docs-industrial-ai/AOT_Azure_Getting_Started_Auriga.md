---
sidebar_position: 2
title: AOT Azure Getting Started Auriga
---

# Getting Started with AOT on Azure

*Accenture Operations Twin* (AOT) is a set of software accelerators for the rapid implementation of customized factory-to-cloud applications. These operations twin apps accelerate the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Starting with version 2.5, AOT is now included in the *Industrial AI* (IAI) initiative--- a multi- disciplinary approach combining Industry knowledge, Operational Technology and Advanced AI underpinned by cutting-edge AI Offerings, specifically tailored to client requirements across industries and domains.

As part of this initiative, we have launched Industrial AI Foundations, a set of flexible data services designed to support the fast rollout of Industrial AI solutions.

AOT and Plant Control Tower will continue to evolve within the Industrial AI Foundation portfolio, and future releases will be provided under the Industrial AI initiative.

## Key Links

-   [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [Asset Overview](https://kxdocuments.accenture.com/Contribution/8dce8c4d-2cb2-4c79-9805-7abc994cf28d)

-   [Nomenclature](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_wiki/wikis/Marilyn-V.wiki/1503/AOT-Nomenclature)

-   [AOT IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [AOT Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53)

## Contacts

-   

-   

## Suggested Reading

-   [Accenture Operations Twin Micro front-end](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Micro_Front_End_MFE_Development_Guide_2_5.pdf)

-   [Accenture Operations Twin Technical Architecture](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_General_Architecture_2_5.pdf)

# Required Skills

## Back-End Development

-   Python

-   Unity

-   Azure Blob Storage  

-   Azure Kubernetes Cluster  

-   Container Registry  

-   Namespace in the AKS cluster for environments  

-   Kubernetes Service Connection for AKS Cluster  

-   Sonar project and key  

-   Azure Data factory

-   Azure data explorer

-   Azure SQL database

-   Azure Pubsub notification

-   Azure Stream Analytics

-   Azure Function Apps

-   Azure App Service

-   Azure Digital Twin

-   Azure APIM

-   Azure Cosmos DB

-   Azure Network Service

## Front-End Development

-   Angular

-   React JS (for 3D)

-   Unity (for 3D)

## 

# Required Tools and Licenses

## Back-End

-   Python

-   SonarQube

-   Lens App

## Front-End

-   Node JS at least 10.13 up to 14.21.1 (for Angular 9)

-   Angular CLI (global installation)

-   Visual Studio Code

-   Jasmine and Karma

-   SonarQube

-   VSTS Access (for installing shareable components)

-   3DCE SaaS license for client implementation - optional

-   Unity license

## Infrastructure

-   Azure Subscription

-   Azure Devops license/subscription

-   Azure Devops Repository

    -   Extractor code

    -   ARM templates

    -   Pipeline files

-   Azure CLI

-   Git Bash

-   Sonar project and key

# 

# Delivery Team Journey

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Step   Activity
  ------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1      Project Kick Off (Non-AOT)

  2      Spin up Azure Client subscription with Groups, Roles and Service principles (Non-AOT)

  3      Twin creation -- Planning for Onboarding client devices and extract data from Client\'s Source System or aggregate AH from multiple systems.

  4      [DevOps to deploy all AOT components](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Azure_Deployment_Guide_2_4.pdf)

  5      [Operations Hierarchy configuration -- role to asset mapping](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Operations_Hierarchy_Getting_Started_2_4.pdf)

  6      [People Management configuration](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_Getting_Started_2_4.pdf)

  7      [Smart KPI component configuration -](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Azure_KPI_Hierarchy_and_Calculation_Technical_Overview_2_4.pdf) [Upload KPI template](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Azure_KPI_Hierarchy_and_Calculation_Technical_Overview_2_4.pdf)

  8      [Upload excel files for creating insight category hierarchy](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Intelligent_Advisor_Getting_Started_2_4.pdf)

  9      [Intelligent Advisor component configuration, customization, and sanity checks](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Intelligent_Advisor_Getting_Started_2_4.pdf)

  10     [3D Twin component configuration/ customization and sanity check](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin_Builder_and_Viewer_Getting_Started_2_4.pdf)

  11     [Customization of components and overall Application sanity check, data verification, trial run](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Azure_Deployment_Guide_2_4.pdf)

  12     Handover to client
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# General Prerequisites

The prerequisites listed below do not include special prerequisites that apply to individual components. To learn more about special prerequisites, see the [Getting Started Guide](https://industryxdevhub.accenture.com/assetdetails/75) for each AOT component. For more information about the following sections, see the [AOT Azure Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53).

**Infrastructure**

Prerequisites related to infrastructure are listed below:

-   A service principle must exist on the Azure Portal for:

    -   authentication of the application.

    -   the service connection on Azure DevOps for running ARM templates.

    -   Azure service communications.

-   A library must exist to hold the parameters needed to run the infrastructure pipelines.

-   Azure service connections must exist for the SonarQube project and Container Registry.

-   A namespace in the AKS cluster is needed for environments.

-   A Kubernetes Service Connection is required for the AKS Cluster.

-   Database along with modeling

-   ADF and ADT pipeline services

-   APIM to host APIs

-   Azure AD, Groups, Roles

**Azure -- AD Integration**

Because AOT includes People Management capabilities, it is necessary to integrate Azure Active Directory (AD) with Groups and Roles. This integration is generally performed by an Admin.

**Azure**

A Service Connector must be configured.

**Data Transformation**

For AOT to work properly, the source data must be in a format that the application can interpret. Generally speaking, parameter names must not include spaces or special characters. The fields listed below must be formatted by the developer before using AOT. It is assumed that the developer has the required skills and knowledge to handle the data transformation.

### External ID- Parameter

The Parameter Timeseries external must be formatted as AssetFloc:Name

For example:

> Externalid: X-Y-U1-EGCA_RunHours, in metadata \{\"Name\":\" Run Hours\"\}
>
> X-Y-U1-EGCA:RunHours_Target

Note that except for the underscore character \'\_\' , which may be used for identifying the various attributes of parameters and KPIs, special characters are not allowed.

### External ID -KPI

The KPI\'s external id format is Assetloc_UID

> For example:
>
> C-B1-G1-R1-F1-P-PP-U3-SWLPB_e8cd9a71-77f1-47b4-8afe-82ebb94be10b

### External ID -- Assets

The external ID for assets is Assetloc.

> For Example:
>
> C-B1-G1-R1-F1-P

### Asset Metadata

Because metadata cannot be added through the UI, mandatory metadata fields such as Asset Type, UoM, and Time zone must be defined in advance using the [Automatic Asset Hierarchy Accelerator](https://industryxdevhub.accenture.com/assetdetails/46).
