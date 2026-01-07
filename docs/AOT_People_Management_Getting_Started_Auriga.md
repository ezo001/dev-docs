---
id: aot-people-management-getting-started-auriga
title: AOT People Management Getting Started Auriga
---

Getting Started with People Management

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT’s People Management (PM) component is responsible for the management and propagation of roles and permissions throughout the application. It is configured for the management of Departments, Roles, and Users and is integrated with the client’s Active directory.

## Target Audience

- Client and Asset Delivery Teams

- Solution Architects

- Technical Architects

- Business Analysts and Consultants

## Purpose

This document describes the prerequisites, and overall flow for setting up and configuring People Management UI, and links to the related detailed documents.

## Contacts

- ``

- ``

- ``

- ``

## Related Links

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45) 

- [AOT Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- [People Management Resources](https://industryxdevhub.accenture.com/assetdetails/64)

## Prerequisites

- For the People Management component, at least one user must be assigned the role of Admin.

- For general prerequisites, see the [AOT Getting Started](https://industryxdevhub.accenture.com/assetdetails/75) document.

# People Management User Journey

AOT Login

(PM Admin)

AOT Login

[View KPIs and Insights data as per assigned Role](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[Assign additional User(s) to the Role (if required)](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[Assign AD Group(s) to the Role](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[Assign Department(s) to the Role](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[Create Department(s)](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[As part of Code deployment, provide an Admin user](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Cognite_People_Management_Backend_Deployment_Guide_2_4.pdf)

[Create Role(s) based on the Plant/Multi-plant dropdown selection](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[Manually run Sync services to update DB](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

[Create AD groups and add users to it](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Cognite_People_Management_Backend_Deployment_Guide_2_4.pdf)

AD group is updated

**No**

**Yes**

**Accenture Delivery Team**

**Client IT/Admin Team**

**Client Business User**

[Assign Asset Level(s) to the Role](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_People_Management_UI_Guide_2_4.pdf)

# People Management Resources







``

``
Document
Description
Topic – Page Number
``
``

``
AOT People Management Architecture Blueprint
``
This document describes the architecture, components, and layers of the People Management functionality.
``
`Architecture - 4`
Layers - 4
Components - 5
Functional Permissions - 5
Data Permissions - 5
Integration with other AOT components - 6
Tenants of People Management - 7
Integration of People Management with Smart KPIs - 8
Integration of People management with Intelligent Advisor - 8
Integration of People management with Twin Builder - 8
``
``
`AOT Cognite People Management Backend Deployment Guide`
AOT Azure People Management Backend Deployment Guide
``
This document provides information on the deployment of the People Management APIs including Infrastructure as Code Database (IaC DB), and Swagger file deployment.
``
`Required Pipelines - 3`
AOT-PeopleManagement-IaC-DB-&-MS - 4
AOT-PM-API-Deployment-Using-Swaggerfile - 8
``
``
AOT People Management UI Guide
``
This document explains how to navigate through the People Management configuration UI once it has been deployed. After reading this document, the user would understand how to launch the PM Config UI and perform various actions like create, edit, revive, and delete on Roles and Departments.
``
`People Management Dashboard – 5`
Roles – 6
Departments – 15
Troubleshooting – 18
``
``
AOT People Management API Reference
``
This reference document includes information about paths, inputs, outputs, and error management for APIs related to AOT People management configuration. Additionally, the document includes APIs used for configuration along with those that provide middleware functionality.
``
`People Management Configuration APIs – 4`
Azure WebPubSub APIs - 38
``
``
`AOT People Management Integration with SmartKPIs`
AOT Azure People Management Integration with Smart KPIs
``
This guide explains how to integrate the people management (PM) component with AOT Smart KPIs by adding roles to the metadata for assets and time series. It should be used along with the API reference document that includes information about paths, inputs, outputs, and error management for APIs related to AOT Smart KPIs.
``
`Authentication Token - 3`
Permission Types - 3
Functional Permissions - 4
Data Permissions - 5
Main Layers - 6
Authentication and Authorization – 6
Caching - 7
Data Permission Microservice - 8
Smart KPI Integration – 14
`Adding Roles to Assets - 16`
Adding Roles to Timeseries - 17
Result - 18
``
``
``
