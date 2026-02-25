---
sidebar_position: 2
title: IAI Getting Started
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Accenture</p>
<p class="doc-topic">Operations Twin</p>
<p class="doc-type">Getting Started Guide</p>
</div>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation |
| **Domain / Area** | Digital Twin |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya |
| **Status** | Draft / In Progress |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | IAI Release Notes, IAI Architecture Blueprint |
| # | \{#section .unnumbered\} |
</div>

## Introduction \{#introduction .unnumbered\}

Industrial AI Foundation (IAI) is a set of software accelerators for the rapid implementation of customized factory-to-cloud applications. These operations twin apps accelerate the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Starting with version 2.5, IAI is now included in the Industrial AI (IAI) initiative--- a multi- disciplinary approach combining Industry knowledge, Operational Technology and Advanced AI underpinned by cutting-edge AI Offerings, specifically tailored to client requirements across industries and domains. As part of this initiative, we have launched Industrial AI Foundations, a set of flexible data services designed to support the fast rollout of Industrial AI solutions. IAI and Plant Control Tower will continue to evolve within the Industrial AI Foundation portfolio, and future releases will be provided under the Industrial AI initiative.

### Key Links \{#key-links .unnumbered\}

-   [IAI on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [Asset Overview](https://kxdocuments.accenture.com/Contribution/8dce8c4d-2cb2-4c79-9805-7abc994cf28d)

-   [Nomenclature](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_wiki/wikis/Marilyn-V.wiki/1503/AOT-Nomenclature)

-   [Introduction to Cognite Data Fusion (CDF)](https://kxdocuments.accenture.com/Contribution/34bbec22-c131-4b5d-b435-d06978dc5234)

-   [IAI IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [IAI Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53)

-   [Getting Started with IAI on Azure](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Azure_Getting_Started_2_5.pdf)

### Suggested Reading \{#suggested-reading .unnumbered\}

-   [Industrial AI Foundation Micro front-end](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Micro_Front_End_MFE_Development_Guide_2_5.pdf)

-   [Industrial AI Foundation Technical Architecture](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_General_Architecture_2_5.pdf)

### More Learning \{#more-learning .unnumbered\}

-   [PCT Reference Application Overview](https://kxdocuments.accenture.com/contribution/cafb3be2-8324-4a0e-bc60-234270a2f53d)

-   [PCT for Discrete Manufacturing Example](https://kxdocuments.accenture.com/contribution/c66656e7-242f-4f89-bf13-f04c257a15de)

-   [PCT for Discrete -- Demo Video](https://mediaexchange.accenture.com/media/1_78520n2j)

### Contacts \{#contacts .unnumbered\}

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [susarla.aditya@accenture.com](mailto:susarla.aditya@accenture.com)

###  \{#section-1 .unnumbered\}

### Glossary \{#glossary .unnumbered\}


| **Term** | **Definition** |
| --- | --- |
| Digital Twin | A digital representation of physical assets, processes, or systems, used to simulate, monitor, and optimize real-world operations. In IAI, this refers to the contextualized integration of operational data. |
| Cognite Data Fusion (CDF) | A data platform used for integrating, contextualizing, and managing industrial data, serving as a core technology for IAI deployments. |
| Azure Kubernetes Service (AKS) | A managed Kubernetes container orchestration service on Microsoft Azure, used for deploying and managing containerized applications within IAI. |
| SonarQube | A tool for continuous inspection of code quality, used in IAI for static code analysis and maintaining code standards. |
| Unity | A cross-platform game engine, used in IAI for developing 3D visualizations and interactive digital twin experiences. |
| Angular | A web application framework for building front-end applications, used in IAI for UI development. |
| React JS | A JavaScript library for building user interfaces, especially for 3D visualizations in IAI. |
| Service Principal | An identity used by applications or services to access specific Azure resources, required for authentication and automation in IAI deployments. |
| Active Directory (AD) Integration | The process of connecting Microsoft Active Directory with CDF to enable user and role management, essential for People Management in IAI. |
| Dataset ID | A unique identifier for datasets in CDF, which must be consistent across asset hierarchies, KPI hierarchies, and timeseries for correct data retrieval and KPI computation in IAI. |
| External ID | A formatted identifier for timeseries parameters in CDF, following the convention AssetFloc:Name, used to uniquely reference operational data. |
| Asset Metadata | Mandatory descriptive fields (such as Asset Type, Unit of Measure, and Time Zone) that must be defined for assets in CDF, typically using the Automatic Asset Hierarchy Accelerator. |
| Kubernetes Service Connection | A configuration that allows Azure DevOps to interact with an AKS cluster for deploying and managing IAI components. |
| Pipeline Files | Configuration files that define automated build and deployment processes in Azure DevOps for IAI. |
| ARM Templates | Azure Resource Manager templates are used to automate the deployment of Azure resources required for IAI infrastructure. |
| 3DCE SaaS License | A license for 3D Content Engine Software as a Service, required for client implementations involving 3D visualization in IAI. |
| Micro Front-End (MFE) | An architectural approach where a web application is built as a composition of features owned by independent teams, referenced in IAI for modular UI development. |
| People Management | An IAI component for managing organizational roles and users, requiring AD integration for full functionality. |
| Smart KPI | An IAI component for configuring and customizing Key Performance Indicators, enabling advanced operational analytics. |
| Intelligent Advisor | An IAI component for providing recommendations and insights based on operational data. |
| Automatic Asset Hierarchy Accelerator | A tool for defining and managing asset metadata in CDF, ensuring all required fields are set before use in IAI. |
| # | \{#section-2 .unnumbered\} |
### Required Skills \{#required-skills .unnumbered\}

-   Cognite Data Fusion

-   Back-End Development

    -   Python

    -   Unity

    -   Storage Account  

    -   Azure Kubernetes Cluster  

    -   Container Registry  

    -   Namespace in the AKS cluster for environments  

    -   Kubernetes Service Connection for AKS Cluster  

    -   Sonar project and key  

-   Front-End Development

    -   Angular

    -   React JS (for 3D)

    -   Unity (for 3D)

### Required Tools and Licenses \{#required-tools-and-licenses .unnumbered\}

-   Cognite Data Fusion License

-   Back-End

    -   Python

    -   SonarQube

    -   Lens App

-   Front-End

    -   Node JS at least 10.13 up to 14.21.1 (for Angular 9)

    -   Angular CLI (global installation)

    -   Visual Studio Code

    -   Jasmine and Karma

    -   SonarQube

    -   VSTS Access (for installing shareable components)

    -   3DCE SaaS license for client implementation

    -   Unity license

-   Infrastructure

    -   Azure DevOps license/subscription

    -   Azure DevOps Repository

        -   Extractor code

        -   ARM templates

        -   Pipeline files

    -   Azure CLI

    -   Git Bash

    -   Sonar project and key

## Delivery Team Journey \{#delivery-team-journey .unnumbered\}


| **Step** | **Task** **Documentation** |
| --- | --- |
| 1 | Project Kick Off |
| 2 | Spin up Cognite instance |
| 3 | Integrate CDF with client\'s Active directory |
| 4 | Configure the data integration accelerator in IAI [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Extractors_Getting_Started_2_4.pdf) |
| 5 | Perform data transformation and contextualization |
| 6 | Deploy additional IAI components [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Deployment_Guide_2_4.pdf) |
| 7 | Configure Operations Hierarchy [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Operations_Hierarchy_Getting_Started_2_4.pdf) |
| 8 | Configure People Management [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_Getting_Started_2_4.pdf) |
| 9 | Configure Smart KPIs [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Smart_KPIs_Getting_Started_2_4.pdf) |
| 10 | Configure and customize Intelligent Advisor [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Intelligent_Advisor_Getting_Started_2_4.pdf) |
| 11 | Configure and customize Twin Builder and Viewer [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin_Builder_and_Viewer_Getting_Started_2_4.pdf) |
| 12 | Deploy IAI [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Deployment_Guide_2_4.pdf) |
| 13 | Hand over to client |
| # | \{#section-3 .unnumbered\} |
## General Prerequisites \{#general-prerequisites .unnumbered\}

The prerequisites listed below do not include special prerequisites that apply to individual components. To learn more about special prerequisites, see the [Getting Started Guide](https://industryxdevhub.accenture.com/assetdetails/75) for each IAI component. For more information about the following sections, see the [IAI Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53).

**Infrastructure**

Prerequisites related to infrastructure are listed below:

-   A service principal must exist on the Azure Portal for:

    -   authentication of the application.

    -   the service connection on Azure DevOps for running ARM templates. 

-   A library must exist to hold the parameters needed to run the infrastructure pipelines. 

-   Azure service connections must exist for the SonarQube project and Container Registry.

-   A namespace in the AKS cluster is needed for environments.

-   A Kubernetes Service Connection is required for the AKS Cluster.

**CDF -- AD Integration**

If deployed on Cognite Data Fusion (CDF), it is necessary to integrate Active Directory (AD) with CDF so that the People Management functionality works. This integration is generally performed by an Admin.

**Azure**

A Service Connector must be configured.

**Data Transformation**

For IAI to work properly, the source data must be in a format that the application can interpret. Generally speaking, parameter names must not include spaces or special characters. The fields listed below must be formatted by the developer before using IAI. It is assumed that the developer has the required skills and knowledge to handle the data transformation.

#### External ID

The Parameter Timeseries external must be formatted as *AssetFloc:Name*

For example:

> Externalid: X-Y-U1-EGCA:RunHours, in metadata \{\"Name\":\" Run Hours\"\}
>
> X-Y-U1-EGCA:RunHours_Target
>
> Note that except for the underscore character \'\_\' , which may be used for identifying the various attributes of parameters and KPIs, special characters are not allowed.

#### Dataset ID

The Dataset ID must be the same for:

-   Asset Hierarchy

-   KPI Hierarchy

-   Timeseries

> If the Dataset ID is not aligned, then the data is not retrieved correctly and the computation of the KPIs fails.
>
> The dataset ID can be specified in the transformations, otherwise, the dataset ID needs to be manually updated by the developer.

#### Asset Metadata

> Because metadata cannot be added through the UI, mandatory metadata fields such as Asset Type, UoM, and Time zone must be defined in advance using the [Automatic Asset Hierarchy Accelerator](https://industryxdevhub.accenture.com/assetdetails/46).
