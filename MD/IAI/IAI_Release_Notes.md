---
sidebar_position: 2
title: IAI Release Notes
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">IAI 2.5</p>
<p class="doc-type">RELEASE NOTES</p>
</div>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation |
| **Domain / Area** | Digital Twin |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya, Rane, Chetankumar |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | IAI Getting Started |

</div>

## Introduction

*Industrial AI Foundation* (IAI) is a set of software accelerators for the rapid implementation of customized factory-to-cloud applications. These operations twin apps accelerate the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Starting with version 2.5, IAI is now included in the Industrial AI (IAI) initiative--- a multi- disciplinary approach combining Industry knowledge, Operational Technology and Advanced AI underpinned by cutting-edge AI Offerings, specifically tailored to client requirements across industries and domains.

As part of this initiative, we have launched Industrial AI Foundations, a set of flexible data services designed to support the fast rollout of Industrial AI solutions.

IAI and Plant Control Tower will continue to evolve within the Industrial AI Foundation portfolio, and future releases will be provided under the Industrial AI initiative.

### Purpose

This document describes new features for version 2.5 as well as any bug fixes and enhancements made to previously released features. It also includes a section for known issues and limitations.

### 

## Target Audience

-   Delivery Teams

-   Stakeholders, Solution Architects, Technical Architects

### Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [susarla.aditya@accenture.com](mailto:susarla.aditya@accenture.com)

-   [ankur.manchanda@accenture.com](mailto:ankur.manchanda@accenture.com)

###  Related Links

-   [Architectural Blueprints](https://ts.accenture.com/:f:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints?csf=1&amp;web=1&amp;e=eQKBIB)

-   [Cognite Documentation](https://docs.cognite.com/cdf/air/)

-   [IAI Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [Azure Digital Twins](https://learn.microsoft.com/en-us/azure/digital-twins/overview)

-   [AIIS on ARC](https://reinventionconsole.accenture.com/console/explore/asset-details/ZmEwY2U5MDUtMWQ1OS00YWNiLThjOGEtMWM0NDE5YjhlNzNk/MjFiZTJmNjctZGRjMy00Y2IzLWI4ZDItNjc2NWQ0YzE1MGQ0)

-   [PCT/AIIS Integrated Implementation](https://ts.accenture.com/:p:/r/sites/AOT-Flutura/Shared%20Documents/General/R1%20GTM/PCT_AIIS_Integration.pptx)

## Release Highlights

-   Amazon Web Services (AWS) has been added to the list of supported cloud ecosystems and data platform vendors.

-   A new Batch Analysis module enables users to trace production orders and product genealogy, leverage validated expert recommendations, and benefit from streamlined navigation and performance optimizations.

-   A new Expert Knowledge module uses IX GenAI's Knowledge Validation Agent and IAI's Recommendation Framework to enhance the capture and validation of expert knowledge used for generation of actionable recommendations.

-   Light mode readability has been improved across all IAI components.

-   Google Cloud Platform (GCP), beta version, has been added to the list of supported cloud ecosystems and data platform vendors.

In addition to the above application-based improvements, IAI's development team delivered expanded [architectural blueprints](https://ts.accenture.com/:f:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints?csf=1&amp;web=1&amp;e=eQKBIB) and documented industry-specific use cases -- spanning across, pharma, automotive, oil and gas, CPG, and energy consumption optimization (ECO) -- that demonstrate IAI's versatility in addressing real-world manufacturing challenges.

## New Features and Enhancements

### Batch Analysis Module

IAI's new Batch Analysis module has been introduced for discrete and batch manufacturing industries. It enables users to trace production orders and product genealogy across production and consumption processes. This new module is overlaid with IAI's existing components (Operations Hierarchy, Smart KPIs, Twin Builder, and Twin Viewer) to provide the following functionalities:

-   View detailed batch information including product, process, genealogy, and material tracking.

-   Filter batches by time and process using interactive dashboards for performance analysis.

-   Save Golden Batch profiles to compare with new batches.

-   Track live batch status and progress on 2D plant schematics and access batch details and production order information instantly.

-   Enhanced SKPI template now includes batch filters and custom KPIs.

-   Navigate directly from the SKPI dashboard to batch analysis to compare attributes.

-   Select specific product variants in the 2D schematic to filter and visualize process flow and batch activity.

-   View specific production order details in the 2D schematic to trace execution and related batches.

### 2D/3D Builder and Viewer

-   Batch Analysis Module. Users can view batch and product order details through the 2D schematic component. Refer to previous section for more details.

-   Users may now create multiple versions under 3D POI mapping and messaging for leaf nodes.

-   Dependency of immediate children has been removed and needs only to be mapped in POI and 3D model mapping applications

-   All pop-ups have been redesigned for better user experience.

-   To prevent accidental deletion, users are now prompted before 2D files are deleted.

-   Schematic loading time for the 2D viewer has been reduced.

-   Handling of overlapping pins for multiple plants at a location has been enabled in Globe/Map view.

-   2D Twin Builder users can now access a drop-down selection of mapping commands for KPI/Insight/Action color icon and count.

-   Access to KPIs and the related drilldowns in Twin Viewer is now limited to users with the proper access rights.

-   3D builder UX has been aligned with the latest IAI design system to ensure uniformity and standardization.

### Operations Hierarchy

-   Assets in the Operations Hierarchy may now be analyzed based on the batches associated with that asset. Users can now navigate to batch analysis screens directly from the OH module, and can more easily analyze the data points associated to Process, Product, Attributes, and more corresponding to the selected process.

-   When configuring templates in the Entity Viewer, images are now supported.

-   When viewing operation hierarchy (OH), the user can now skip entire levels of dependent assets.

### Smart KPIs

-   New validations for archiving KPIs are now included when uploading the Smart KPIs configuration template. These new validations ensure that the archived KPIs are not renamed when KPI names are updated and thus improves validation error detection in the KPI template configuration.

-   Subtractions in denominator values and division operations are now possible for KPI calculations.

-   The Trendline Chart has been enhanced with zoom functionality for easier visualization.

-   The Deviation API response time has been optimized to load KPI tiles more efficiently with a faster response time.

-   Implemented chart.js to improve the loading aspects via caching mechanism.

### Intelligent Advisor

-   The new Expert Knowledge module for Intelligent Advisor (IA) uses IX GenAI's Knowledge Validation Agent and IAI's Recommendation Framework to enhance the capture and validation of expert knowledge used for the generation of actionable recommendations. Insights now allow capturing expert knowledge descriptions and images. The new Knowledge Validation Agent evaluates submissions for clarity, professionalism, toxicity, and actionability, and creates image descriptions. Users with the new Validator Expert Knowledge role can accept or reject entries based on AI-generated scores. Validated knowledge is stored for recommendation generation. Once the entries are accepted, recommendations can be generated in both the Intelligent Advisor and Digital Twin Assistant.

-   Access to KPIs and the related drilldowns is now limited to users with the proper access rights.

### 

## Engineering Workbench

The Engineering Workbench (EWB) integration from the 2.4 release has been enhanced and now consumes data from IAI graph directly. As a result:

-   IAI users can navigate to EWB to create, host, configure, and fine tune ML models on EWB, based on the data in ADT and ADX sources

-   IAI users can operationalize ML models on IAI and utilize the outcomes to configure insight on Intelligent Advisor.

### Architectural Blueprints

An architectural Blueprint is a high-level plan that shows how the system's technologies, services, and components are structured and connected. It helps map out microservices, containers, and platform deployments so teams can easily understand how everything fits together and operates. The following blueprints were delivered for the 2.5 release:

-   [Snowflake](https://ts.accenture.com/:p:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints/Operations%20Twin_Snowflake%20Blueprint_20250904.pptx?d=w3177d22655744e04a5c79afa3435afae&amp;csf=1&amp;web=1&amp;e=pZxTCW) (Relational AI, Snowpark, Kafka)

-   [AIIS](https://ts.accenture.com/:p:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints/Operations%20Twin_AIIS%20Blueprint_20250728.pptx?d=wda5013788a0b4ddb89b6d185bf4fca8c&amp;csf=1&amp;web=1&amp;e=ExdDv9) (JanusGraph, OpenTS Database, Azure Data Lake, Kubernetes)

-   [Azure + DataMosaix](https://ts.accenture.com/:p:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints/Operations%20Twin_Azure_DataMozaix%20Blueprint_20250915.pptx?d=w831636813c02495eafa80e797b6c7854&amp;csf=1&amp;web=1&amp;e=RBhU7J) (FactoryTalk EdgeManager, DataMoszaix, Azure Web Apps)

-   [MDS](https://ts.accenture.com/:p:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints/Operations%20Twin_MDS%20Blueprint_20250827.pptx?d=w4c4f3ca8ac9a4318ab6d994eabc3b2e5&amp;csf=1&amp;web=1&amp;e=xagOJe) (ADF, IoT Hub, ADX, Azure Data Lake, Kubernetes)

-   [AWS](https://ts.accenture.com/:p:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints/Operations%20Twin_AWS%20Blueprint_20250728.pptx?d=w47ab2d1211a74ecf97058b6ef03ea14b&amp;csf=1&amp;web=1&amp;e=tvLJ8l) (AWS Glue, IoT SiteWise, TwinMaker, Timestream, S3, Elastic Kubernetes)

-   [GCP](https://ts.accenture.com/:p:/r/sites/IX-AccentureOperationsTwin/Shared%20Documents/General/8.%20Architecture/Blueprints/Operations%20Twin_GCP_ECO_Blueprint.pptx?d=w6e7e1a08c1bb4ea7a78b187d2b07188a&amp;csf=1&amp;web=1&amp;e=2L9hFo) (Energy consumption optimization )

## Known Issues and Limitations

-   In Intelligent Advisor, if a Role is mapped to a large dataset (All Groups in Active Directory Groups), then Department and Role fields cannot be populated at the creation of an Insight or Action.

-   In Smart KPIs:

    -   When KPIS are sorted by performance in the dashboard screens, the tiles with NDA values appear randomly instead of last.

    -   The Deviation API that is responsible for populating KPI tiles with aggregated values between a start and an end date is loading slowly when applying custom date range, half-yearly and yearly selections.

    -   When deployed on AWS, HBM values do not match with the KPI tiles for calendar selection on the dashboard.

    -   When deployed on AWS, the Role_ID is not getting updated on the back end.

    -   In the CDF variant, decimal values in Smart KPI calculations are inconsistently displayed in some cases. For instance, decimal values are shown rounded up to only the second or third place instead of the expected fourth or fifth place .
