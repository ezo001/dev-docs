---
sidebar_position: 2
title: AOT People Management Getting Started
---

<div class="doc-title-block">
<p class="doc-asset-name">Getting Started with People Management</p>
<p class="doc-topic">Accenture Operations Twin (AOT) is a collection of software accelerators and tools, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.</p>
<p class="doc-type">AOT\'s People Management (PM) component is responsible for the management and propagation of roles and permissions throughout the application. It is configured for the management of Departments, Roles, and Users and is integrated with the client\'s Active directory.</p>
</div>

### Target Audience

-   Client and Asset Delivery Teams

-   Solution Architects

-   Technical Architects

-   Business Analysts and Consultants

### Purpose

This document describes the prerequisites, and overall flow for setting up and configuring People Management UI, and links to the related detailed documents.

### Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [susarla.aditya@accenture.com](mailto:susarla.aditya@accenture.com)

-   [rishabh.b.joshi@accenture.com](mailto:rishabh.b.joshi@accenture.com)

-   [b.h.ranganathan@accenture.com](mailto:b.h.ranganathan@accenture.com)

### Related Links

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45) 

-   [AOT Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [People Management Resources](https://industryxdevhub.accenture.com/assetdetails/64)

### Prerequisites

-   For the People Management component, at least one user must be assigned the role of Admin.

-   For general prerequisites, see the [AOT Getting Started](https://industryxdevhub.accenture.com/assetdetails/75) document.

## People Management User Journey


| **Step** | **Task** |
| --- | --- |
| 1 | Accenture Delivery Team creates an Admin user and deploys code [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Cognite_People_Management_Backend_Deployment_Guide_2_4.pdf) |
| 2 | Accenture Delivery Team creates AD group and adds users to the new group. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Cognite_People_Management_Backend_Deployment_Guide_2_4.pdf) |
| 3 | People Management Admin logs into AOT |
| 4 | If AD group is complete and updated, then admin can manually run sync services to update the database and skip to step 11. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) If AD group is incomplete and needs update, then admin must follow the remaining steps. |
| 5 | Admin creates departments. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |
| 6 | Admin creates roles based on the plant/Multiplant dropdown selection. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |
| 7 | Admin assigns one or more asset levels to the role. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |
| 8 | Admin assigns one or more departments to the role. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |
| 9 | Admin assigns one or more AD groups to the role. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |
| 10 | Admin assigns one or more additional users to the role as needed. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |
| 11 | Delivery team hands off to client. |
| 12 | Client Business User signs into AOT to view KPIs and insights data. [LINK](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) |


## 

# People Management Resources


| **Document** | **Description** | **Topic -- Page Number** |  |
| --- | --- | --- | --- |
| [AOT People Management Architecture Blueprint](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_Architecture_Blueprint_2_4.pdf) | &gt; This document describes the architecture, components, and layers of the People Management functionality. | Architecture - 4 |  |
| [AOT Cognite People Management Backend Deployment Guide](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Cognite_People_Management_Backend_Deployment_Guide_2_4.pdf) | &gt; This document provides information on the deployment of the People Management APIs including Infrastructure as Code Database (IaC DB), and Swagger file deployment. | Required Pipelines - 3 |  |
| [AOT Azure People Management Backend Deployment Guide](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Azure_People_Management_Backend_Deployment_Guide_2_4.pdf) |  | AOT-PeopleManagement-IaC-DB-&amp;-MS - 4 |  |
| [AOT People Management UI Guide](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf) | &gt; This document explains how to navigate through the People Management configuration UI once it has been deployed. After reading this document, the user would understand how to launch the PM Config UI and perform various actions like create, edit, revive, and delete on Roles and Departments. | People Management Dashboard -- 5 |  |
| [AOT People Management API Reference](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_API_Reference_2_4.pdf) | &gt; This reference document includes information about paths, inputs, outputs, and error management for APIs related to AOT People management configuration. Additionally, the document includes APIs used for configuration along with those that provide middleware functionality. | People Management Configuration APIs -- 4 |  |
| [AOT People Management Integration with SmartKPIs](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_Integration_with_SmartKPIs_2_4.pdf) | &gt; This guide explains how to integrate the people management (PM) component with AOT Smart KPIs by adding roles to the metadata for assets and time series. It should be used along with the API reference document that includes information about paths, inputs, outputs, and error management for APIs related to AOT Smart KPIs. | Authentication Token - 3 | Adding Roles to Assets - 16 |
| [AOT Azure People Management Integration with Smart KPIs](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Azure_People_Management_Integration_with_SmartKPIs_2_4.pdf) |  | Permission Types - 3 | Adding Roles to Timeseries - 17 Result - 18 |

