---
sidebar_position: 2
title: AOT Smart KPIs Getting Started Auriga
---

# Getting Started with Smart KPIs

Accenture Operations Twin (AOT) is a set of software accelerators for the rapid implementation of customized factory-to-cloud Operations Twin applications. An Operations Twin accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Smart KPIs is a no-code framework that provides users the ability to configure, compute, and visualize KPIs in the dashboard. Using Smart KPIs, users in the boardroom, on the shop floor, or anywhere in between can get a contextualized view of operational performance through KPIs and can critically analyze business performance and drive decisions. Smart KPIs link the strategic KPIs at the company or business level with tactical and operational KPIs at the plant or unit level and provide a transparent view of performance.

## Purpose

This document describes the overall flow for setting up, configuring, and visualizing Smart KPIs and the related prerequisites.

## Target Audience

-   Client and Asset Delivery Teams

-   Solution Architects

-   Technical Architects

-   Business Analysts and Consultants

## Contacts

-   

-   

-   

-   

## Related Links

-   [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [IX Developer Hub](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

## 

## Glossary

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**                          **Definition**
  --------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  AOT (Accenture Operations Twin)   A set of software accelerators for rapid implementation of customized factory-to-cloud Operations Twin applications, integrating product, process, and live data from IT and OT systems for a comprehensive view of operations.

  Smart KPIs                        A no-code framework that allows users to configure, compute, and visualize KPIs in dashboards, linking strategic, tactical, and operational KPIs for transparent performance analysis

  KPI (Key Performance Indicator)   Quantitative metrics used to evaluate business performance at strategic, tactical, or operational levels

  UoM (Unit of Measurement)         The standard unit used to quantify KPI values, such as hours, pieces, or percentages. UoM mapping ensures consistency across KPIs.

  CDF (Cognite Data Framework)      A platform for deploying AOT, where functions and configuration files are uploaded to enable data integration and KPI computation

  Asset                             Any physical or digital resource tracked within the AOT platform for KPI measurement and analysis.

  Role                              A set of permissions and responsibilities assigned to users, determining access to assets and KPI configuration tools

  Dashboard                         The user interface in AOT where KPIs are visualized, analyzed, and compared, supporting drilldown and time series analysis

  KPI Config Template               A template used to define, configure, and upload KPIs into the AOT platform, including hierarchy, UoM mapping, and contributing relationships

  Scheduler                         A component or service that automates the execution of KPI calculations and other functions at defined intervals within the AOT platform
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Smart KPIs User Journey

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   **Step**  **Task or Action**
  ---------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      1      Project Kick Off

      2      Accenture Delivery Team uploads the CDF function zip files to CDF -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_Administration_Guide_2_5.pdf)

      3      Accenture Consultant and Client Admin create the template with necessary dropdowns to add the KPIs -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_Administration_Guide_2_5.pdf)

      4      Accenture Consultant and Client Admin configure SmartKPI template to add/update/archive KPIs -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_Administration_Guide_2_5.pdf)

      5      Accenture Consultant and Client Admin sign into AOT

      6      Accenture Consultant and Client Admin upload the template using SmartKPI config tool -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_Administration_Guide_2_5.pdf)

      7      Accenture Consultant and Client Admin use the KPI Engine -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_KPI_Hierarchy_and_Calculation_Technical_Overview_2_5.pdf)

      8      Handover to Client

      9      Client Business User signs into AOT

      10     Client Business User reviews KPIs -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_UI_Guide_2_5.pdf)

      11     Client Business User drills down into KPIs to investigate contributing/influencing KPIs -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_UI_Guide_2_5.pdf)

      12     Client Business User Compare time series data between KPIs -- [LINK](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_UI_Guide_2_5.pdf)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Smart KPIs Resources

The links below are to documents related to the Smart KPIs component.


| **Document** | **Description** | **Topic -- Page Number** |
| --- | --- | --- |
| [AOT Smart KPIs Administration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_Administration_Guide_2_5.pdf) | This document outlines how to create, configure, and upload Smart KPIs in the AOT platform, including building a KPI dashboard, adding new KPIs, and updating or archiving existing ones. | About KPIs -- 4 |
|  |  | Configuration -- 5 |
|  |  | KPI Creation Flow -- 8 |
|  |  | Creating New KPIs -- 9 |
|  |  | Updating and Archiving KPIs - 15 |
| AOT KPI Hierarchy and Calculation Technical Overview | This document summarizes the process of uploading the Smart KPIs Config Template, establishing the required KPI hierarchy for CDF functions, forming relationships between KPIs and assets, and handling the creation, scheduling, and execution of CDF functions. | **CDF**: |
| [AOT Azure KPI Hierarchy and Calculation Technical Overview](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Azure_KPI_Hierarchy_and_Calculation_Technical_Overview_2_5.pdf) |  | KPI Hierarchies - 4 |
|  |  | Create KPI Hierarchy Function - 8 |
|  |  | KPI Calculations -- 10 |
|  |  | Scheduling -- 10 |
|  |  | Orchestrator Microservice - 12 |
|  |  | Simulated Value Creation - 16 |
|  |  | Execution of Scheduled Functions -- 17 |
|  |  | UoM Configuration -- 18 |
|  |  | Computation Engine - 21 |
|  |  | **Azure**: |
|  |  | KPI Hierarchies -- 5 |
|  |  | Hierarchy Flows -- 7 |
|  |  | Create KPI Hierarchy Function -- 8 |
|  |  | KPI Calculations -- 11 |
|  |  | Scheduling and Sequencing - 10 |
|  |  | Orchestrator Microservice -- 10 |
|  |  | Simulated Value Creation - 14 |
|  |  | Execution of Scheduled Functions -- 15 |
|  |  | UoM Configuration - 16 |
|  |  | Computation Engine -- 19 |
| AOT Smart KPIs API Reference | This reference document includes information about paths, inputs, outputs, and error management for APIs related to AOT Smart KPIs. The document includes descriptions of APIs used for configuration as well as descriptions of APIs that provide middleware functionality. | Smart KPIs Configuration MS APIs -- 5 |
| [AOT Azure Smart KPIs API Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Azure_Smart_KPIs_API_Reference_2_5.pdf) |  | Smart KPIs Microservice APIs - 9 |
| AOT Smart KPis PM Integration Guide | This document explains how to integrate the people management component with AOT Smart KPIs by adding roles to the metadata for assets and timeseries. It includes information about paths, inputs, outputs, and error management for the APIs related to AOT Smart KPIs. This document and the API Reference are used collectively for the integration. | Smart KPI -- PM Integration -- 5 |
| [AOT Azure SmartKPIs PM Integration Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Azure_People_Management_Integration_with_SmartKPIs_2_5.pdf) |  | Data Permission Microservice -- 5 |
|  |  | APIs -- 9 |
|  |  | Adding Roles to Assets -- 11 |
|  |  | Adding Roles to Timeseries - 12 |
|  |  | Smart KPI Integration -- 17 |
|  |  | Use Cases -- 13 |
| [AOT Smart KPIs UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Smart_KPIs_UI_Guide_2_5.pdf) | This guide explains how to use the AOT Smart KPIs UI after deployment. | Dashboard - 4 |
|  |  | Trend Timeline - 7 |
|  |  | KPI Tiles - 9 |
|  |  | Aggregated Data -- 10 |
|  |  | Contributing KPIs -- 11 |
|  |  | Calendar and KPI Tiles -- 12 |
|  |  | Role-based KPI Drilldown -- 13 |
|  |  | KPI Drilldown Details - 13 |
|  |  | Parameters Drilldown- 14 |
|  |  | Access-based KPI Drilldown -- 16 |
|  |  | Non-OT KPI Drilldown - 17 |
|  |  | Calendar and Trend Trendlines -- 22 |
|  |  | Date Picker -- 23 |
|  |  | Pagination and Auto-refresh -- 26 |
|  |  | KPI Details on Intelligent Advisor - 27 |
|  |  | KPI Details on Operations Hierarchy-- 28 |
|  |  | Digital Twin Assistant - 30 |
|  |  | Troubleshooting - 31 |
| [AOT UoM Technical Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Units_of_Measurement_Technical_Reference_2_5.pdf) | This reference document includes information about the Middleware APIs that help in providing information on Units of Measurement like Unit Systems, Units of Measurement, and Units of Measurement Conversion Formulae that are utilized by other AOT components. | Background -- 3 |
|  |  | UoM Conversion -- 4 |
|  |  | Percentage Comparison -- 5 |
|  |  | UoM Configuration APIs -- 5 |
| [AOT Generic Scheduler Technical Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Generic_Scheduler_Technical_Overview_2_5.pdf) | The parameters and examples shown in this document may be used by the target audience to integrate, configure, and deploy AOT\'s Generic Scheduler into an application. | Generic Scheduler Architecture -- 5 |
|  |  | Scheduling Expressions -- 6 |
|  |  | API Specifications -- 7 |
|  |  | Kafka Message Broker -- 14 |
|  |  | Database Tables -- 15 |
|  |  | Deployment -- 16 |
|  |  | Use Case -- Schedling Smart KPIs -- 16 |


# 

# Prerequisites

The prerequisites below are unique to the Smart KPIs component. For general prerequisites, refer to the [AOT Getting Started](https://industryxdevhub.accenture.com/assetdetails/75) document.

-   Departments and Roles must already exist.

    -   The departments and roles are created in the People Management Config tool.

    -   The corresponding role IDs must be available.



-   KPI Config templates should have proper UoM mapping for both parent KPIs and it\'s contributing KPIs.

    -   The Standard UnitSystem is set the first time of the configuration and cannot be changed later. Similarly, when a UoM has been set as Primary in the Standard UoM list, it cannot be changed.

    -   Checking UoM from any one asset among the assets listed in the asset mapping list for any KPI is should have same local UoM SystemID for that KPI.



-   Roles must have the necessary asset-level permissions as shown in the [example script](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/Adding_Roles_and_Asset_Hierarchy_Example_Script.txt).

-   For AOT deployed on CDF (Cognite Data Framework), the CDF functions zip file must be uploaded into CDF as described in the [AOT Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53). Equivalent deployment activities for AOT-Azure are described in [AOT Azure Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53).

## Metadata Table

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / Smart KPIs

  **Domain / Area**                   Performance Metrics

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Susarla, Aditya, Thejash.S.Suresh

  **Status**                          Complete / Published

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   Smart KPIs UI Guide, Smart KPIs Admin Guide
  -----------------------------------------------------------------------------------------------------------------
