---
sidebar_position: 2
title: IAI Release Notes Index
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">IAI</p>
<p class="doc-type">RELEASE NOTES INDEX</p>
</div>

![](./media/IAI_Release_Notes_Index/image2.png)

## Introduction

*Industrial AI Foundation* (IAI) is a set of software accelerators for the rapid implementation of customized factory-to-cloud applications. These operations twin apps accelerate the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Starting with version 2.5, IAI is now included in the Industrial AI (IAI) initiative--- a multi- disciplinary approach combining Industry knowledge, Operational Technology and Advanced AI underpinned by cutting-edge AI Offerings, specifically tailored to client requirements across industries and domains.

As part of this initiative, we have launched Industrial AI Foundations, a set of flexible data services designed to support the fast rollout of Industrial AI solutions.

IAI and Plant Control Tower will continue to evolve within the Industrial AI Foundation portfolio, and future releases will be provided under the Industrial AI initiative.

### Purpose

This document serves as an index of release notes documents. The releases are sorted by date with the most recent release at the top of the table. Clicking the release number link opens the release notes document for that release.

### Target Audience

-   Client Delivery Teams Leveraging IAI

-   Asset Delivery Teams

-   Stakeholders, Solution Architects, Technical Architects

### Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [susarla.aditya@accenture.com](mailto:susarla.aditya@accenture.com)

-   [ankur.manchanda@accenture.com](mailto:ankur.manchanda@accenture.com)

## 

# Release Notes Index


| Release | &gt; Notable Changes |
| --- | --- |
| [2.5](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Release_Notes_2_5.pdf) | &gt; Amazon Web Services (AWS) and Google Cloud Platform (GCP, beta) are now supported as cloud ecosystems and data platform vendors. The Batch Analysis module allows users to trace production orders and product genealogy, access expert recommendations, and enjoy improved navigation and performance. The Expert Knowledge module, powered by IX GenAI\'s Knowledge Validation Agent and IAI\'s Recommendation Framework, enhances the validation and capture of expert knowledge for actionable insights. Light mode readability has been improved across all IAI components. Additionally, the development team has expanded architectural blueprints and documented industry use cases in sectors such as semiconductor, pharma, automotive, oil and gas, consumer packaged goods, specialty chemicals, and energy optimization, showcasing IAI\'s versatility in solving manufacturing challenges. |
| [2.4](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Release_Notes_2_4.pdf) | &gt; In the 2.4 release, a layered design was introduced to enhance code reusability and simplify porting across multiple data architectures and ecosystem platforms. The new architecture segregates data access code on both Azure and CDF, creating distinct Business and Data Access layers. This improved data storage and transaction handling, enabling seamless modification, maintenance, and extension of the application without affecting the data access layer. This segregation was applied across various microservices, configuration modules, APIs, and functions for Intelligent Advisor, Operations Hierarchy, Smart KPI, and People Management components. &gt; &gt; Secondly, IAI was ported on Accenture Industrial Intelligence Suite (AIIS) data platform. With this initial integration, IAI users can combine the ML capabilities of AIIS Engineering Workbench (EWB), with the self-service analytics of Plant Control Tower. The AIIS/Plant Control Tower integration may be demonstrated to clients and will continue to evolve in the next release. |
| [2.3](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.3/AOT_Release_Notes_2_3.pdf) | &gt; IAI 2.3 introduces three main improvements: Redesigned Builder and Viewer UIs include 2D views, AI-powered Digital Twin Assistant, and Event-based KPIs for analyzing events. |
| [2.2](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.2/AOT_Release_Notes_2_2.pdf) | &gt; IAI 2.2 introduces interface usability enhancements across the application and continued extension of functionalities for the Azure Digital Twin variant, which are detailed further in the document. |
| [2.1](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.1/AOT_Release_Notes_2_1.pdf) | &gt; IAI 2.1 introduces expanded functionality across the board for its Azure Digital Twin-based variant, including the availability of the KPI configuration module and Power BI reports. IAI 2.1 brings multi-plant support and globe view to the Twin Viewer component, optimized APIs for faster dashboard loading and a lighter and faster user interface. Numerous minor enhancements and bug fixes were also completed. |
| [2.0](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.0/AOT_Release_Notes_2_0.pdf) | &gt; The 2.0 release of IAI is the first major revision of this asset. It allows the deployment of IAI accelerators using Azure native services (Azure Digital Twin), as an alternative to Cognite Data Fusion. This presents more choices to clients for the implementation of the Data foundation at the heart of a Digital Twin. IAI version 2.0 also offers complete support for multiple plant deployment, including management of different units of measure. It brings numerous smaller enhancements, as well as performance improvements across the board. |
| [1.4](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%201.4/AOT_Release_Notes_1_4.pdf) | &gt; The 1.4 release of IAI boasts improved performance across the board. It also includes several enhancements and new features for Intelligent Advisor, Smart KPIs, Operations Hierarchy, and the 3D component. |
| [1.3](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%201.3/AOT_Release_Notes_1_3.pdf) | &gt; The 1.3 release of IAI features improved performance across the board. It introduces the Configuration UI for Intelligent Advisor that supports both KPI and ML-based insight configurations. The Smart KPI component is now integrated with People Management and Operations Hierarchy with a more reliable computation engine that can handle error scenarios augmented by a retry mechanism. Finally, IAI now supports multiple units of measure (UOM) at once. The addition of this functionality results in improved global/local views on the various components within IAI -- meaning that clients need not standardize various units of measure to effectively use IAI. |
| [1.2](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%201.2/AOT_Release_Notes_1_2.pdf) | &gt; The 1.2 release introduces both event-based scheduling and people management functions in the Smart KPI component to accommodate high-frequency KPI computations and role-based access control, respectively. Secondly, the Intelligent Advisor (IA) component has been integrated with SAP (for closing the loop) and now supports complete lifecycle management of Insights and Actions. Finally, IAI\'s Twin Builder component now includes functionality to upload 3D models that are then mapped to the asset hierarchy stored in the Cognite platform and eventually visualized in the Twin Viewer application. The 3D Viewer component has also been enhanced to show even more detail about Insights, Actions, and Smart KPI data. Other minor enhancements to functionality and performance, as well as bug fixes, are noted later in this document. |
| [1.1](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT_Release_Notes_1_1.pdf) | &gt; The 1.1 release introduces a People Management console for the assignment of user roles and departments, integrated with Smart KPI for role-based data access. It also brings a more robust KPI configuration process, enhancements to the Intelligent Advisor for manual Insight and Action creation, and composite 3D layouts with two-way interaction with IA and Smart KPI components. |
| [1.01](https://ts.accenture.com/sites/GlobalDocTemplates/Shared%20Documents/Released%20Documentation/Accenture%20Operations%20Twin%20(AOT)/1.0.1/AOT_Release_Notes_1_0_1.pdf) | &gt; The 1.0.1 minor release of the Industrial AI Foundation (IAI) delivered bug fixes in the Smart KPI component related to KPI config template upload, Calendar, and KPI tiles. The release also included some enhancements related to the IA Advisor panel and the SAP PM WO accelerator. |
| [1.0](https://ts.accenture.com/sites/GlobalDocTemplates/Shared%20Documents/Released%20Documentation/Accenture%20Operations%20Twin%20(AOT)/1.0/AOT_Release_Notes_1_0.pdf) | &gt; The 1.0 release of the Industrial AI Foundation (IAI) delivered MVP functionality for the Intelligent Advisor, Smart KPI, Data Ingestion Accelerators, and 3D Builder/Viewer components, using Cognite Data Fusion. IAI 1.0 also included a demonstrable Plant Control Tower application to showcase cross-component integration. |

