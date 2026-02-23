---
sidebar_position: 2
title: IAI AH Creation Azure
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">Asset Hierarchy</p>
<p class="doc-type">CREATION GUIDE (AZURE)</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

<div class="metadata-for-agents" aria-hidden="true">
Metadata Table


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / Smart KPIs |
| **Domain / Area** | Performance Metrics |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Jitendra Chauhan, Shriraj |
| **Status** | Published / In Progress |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Smart KPIs UI Guide, Smart KPIs Admin Guide |
| # | \{#section .TOC-Heading\} |

</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools that can be assembled to deliver client solutions. Operations Hierarchy (OH) is an IAI component that helps the user navigate through the plant\'s asset hierarchy and view 360-degree information associated with each node. An ideal operations hierarchy representation would start with a Company-level node, followed by Region, Plant, Line, Unit, System, Subsystem, Equipment, and so on. When integrated with other IAI components, the OH can be used to view detailed information like insights and filtered KPIs related to each level or node.

To deploy OH on IAI\'s Azure version, a template is needed for creating the asset hierarchy (AH). This template contains details of Assets such as Name, Description, Parent, and Asset Type, which are some of the mandatory fields to be defined. As per requirement, the template can be used to define more fields as well. The AH is created through the Azure Data Factory (ADF) Pipeline after the successful upload of the template in a blob container. The AH will be visible in Azure Digital Twin Instance after the successful run of the ADF pipeline.

### Purpose

This document explains how the Asset Hierarchy is created and updated through the ADF pipeline on IAI\'s Azure version.

### Target Audience

-   Software Architects

-   Developers

-   Integrators with IT Background

###  Business Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [rishabh.b.joshi@accenture.com](mailto:rishabh.b.joshi@accenture.com)

### Technical Contacts

-   [s.jitendra.chauhan@accenture.com](mailto:s.jitendra.chauhan@accenture.com)

-   [yash.srivastava@accenture.com](mailto:yash.srivastava@accenture.com)

### 

## Glossary


| **Term** | **Definition** |
| --- | --- |
| Operations Hierarchy (OH) | An IAI component that allows users to navigate a plant\'s asset hierarchy and view detailed, 360-degree information associated with each node (Company, Region, Plant, Line, etc.). |
| Asset Hierarchy (AH) | A structured representation of assets within an organization, created using a template and managed through Azure Data Factory pipelines. |
| Azure Data Factory (ADF) | A cloud-based data integration service used to create, schedule, and orchestrate data pipelines for processing and transforming data, including the creation and updating of the Asset Hierarchy. |
| Blob Storage | Microsoft Azure\'s object storage solution for the cloud, used here to store templates and processed files required for asset hierarchy creation. |
| Azure Digital Twin | A platform that enables the creation of digital representations of real-world assets, systems, and environments. The Asset Hierarchy becomes visible in the Azure Digital Twin instance after successful pipeline execution. |
| Asset Hierarchy Template | An Excel (.xlsx) file containing mandatory columns such as \"Functional Loc,\" \"Description,\" \"AssetType,\" \"Update_Flag,\" and \"SupFunctLoc.\" This template is uploaded to Blob Storage to trigger the asset hierarchy creation process. |
| NDJSON (Newline Delimited JSON) | A file format where each line is a valid JSON object, used for efficient processing of large datasets and required as input for certain Azure Digital Twin APIs. |
| assets-raw-template | A Blob Storage container that holds raw input files, such as the original asset hierarchy templates and configuration columns. |
| JOBSAPI | An API provided by Azure Digital Twin for creating and managing digital twins based on the processed asset hierarchy data. |
| Durable Azure Function | A serverless function in Azure that performs long-running operations, such as updating or archiving assets in the digital twin environment. |
| isActive Property | A property of a digital twin asset indicating whether it is active (true) or archived (false). |

## 

# Background

### Technology Stack

-   Azure data factory pipeline

-   Blob Storage

-   Azure digital twin

-   Azure function app

-   CI/CD pipeline for deploying Azure data factory pipeline and Azure Function app.

###  Prerequisites

To get started with the AH creation, the following resources are required.

-   Blob Storage

-   Azure Data Factory

-   Azure Function App

-   Asset Hierarchy Template (.xlsx File) includes mandatory columns:

    -   \"Functional Loc\"

    -   \"Description\"

    -   \"AssetType\"

    -   \"Update_Flag\"

    -   \"SupFunctLoc\"

### 

# Setup

The Blob Container folder structure and the Azure Data Factory must be set up for the successful execution of ADF pipelines.

### Blob Container

The Blob storage folder must be set up according to the structure described in this section. The blob storage must contain two containers: assets-processed-template and assets-raw-template.

![Blob container structure](./media/IAI_AH_Creation_Azure/image2.png)

#### assets-processed-template

This container is comprised of:

-   Folder (nd-json-file): This folder contains the NDJSON formatted file created by \"ND-JSON-Converter\" an Azure Function App for JOBs API input folder. Note that the naming convention difference is intended as nd-json-file, NDJSON, and ND-JSON-Converter refer to three different entities---folder name, file format, and the Azure function app respectively.

-   Multiplant AH-QA.json: The JSON file created from the copy data activity in the ADF parent pipeline Asset Hierarchy (AH),

![asset-processed-template structure](./media/IAI_AH_Creation_Azure/image3.png)

#### 

### assets-raw-template

This container comprises two folders:

-   AssetConfigurationsColumns

-   AssetHierarchyTemplate

![asset-raw-template structure](./media/IAI_AH_Creation_Azure/image4.png)

The AssetConfigurationColumns folder is a JSON file in which there are two keys:

-   fixedColumns: This is a dictionary, where the keys \"FunctionalLoc\", \"Description\", \"AssetType\", \"Update_Flag\", and \"SupFunctLoc\" are stored. The corresponding value fields are Column names from the template.

-   dynamicColumns: This is a list of extra columns that may be required in AH as a part of Asset_Metadata.

> ![AssetConfigurationColumns JSON file](./media/IAI_AH_Creation_Azure/image5.png)
>
> The AssetHierarchyTemplate folder contains the template that must be uploaded to trigger the ADF pipeline. The template must have all the columns that are mentioned in the JSON file in the AssetConfigurationColumns folder. See also [Sample Template](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT_OH_Multiplant-Asset-Hierarchy.xlsx).

### 

## Azure Data Factory (ADF)

ADF must contain three pipelines and two datasets.

**Pipelines**

-   ADF-Parent-pipeline-AH:- Used for template file conversion and triggering child pipelines depending upon the value of the Scan_Update flag which determines whether the asset hierarchy must be created, updated, or archived.

-   ADF-child-pipeline-JOBSAPI: Used for asset hierarchy creation.

-   ADF-child-pipeline-DurableFunctionApp: Used for updating and archiving the asset.

**Datasets**

-   LatestExcelFile: An inbuilt dataset for Excel files in ADF.

-   LatestFileConvertedtoJson: An inbuilt dataset for JSON files in ADF.

![pipelines and datasets](./media/IAI_AH_Creation_Azure/image6.png)

## 

# Pipelines

### ADF-Parent-pipeline-AH

When the AH template is uploaded in the \"AssetHiererchyTemplate\" folder, \"ADF-parent-pipeline-AH\" is triggered automatically and will execute all the steps mentioned below.

1.  **Copy data --** This step converts the uploaded AH template, which is in Excel (.xlsx) to JSON format.

2.  **Azure function (Scan Update_Flag) --** This API calls the Azure function Scan Update_Flag, which scans the uploaded template and searches for Add/Update/Archive flags. According to the flag found, the function returns a response, which is passed further.

3.  **If Condition --** This step consumes the response from the Azure function (Scan Update_Flag) and checks the following IF conditions

    a.  If Add flag exists: If the value of \"Add_flag\" is \"true\", then ADF-child-pipeline-JOBSAPI is executed and if the value is \"false\" then ADF-child-pipeline-JOBSAPI will not be executed.

    b.  If Update_Archive flag exists: If the value of \"Update_Archive_flag\" is \"true\" then ADF-child-pipeline-DurableFunctionApp is executed if the value is \"false\" then ADF-child-pipeline-DurableFunctionApp will not be executed.

![ADF Parent pipeline AH flow](./media/IAI_AH_Creation_Azure/image7.png)

### 

## ADF-child-pipeline-JOBS-API

When the Add flag exists, the ADF-child-pipeline-JOBSAPI is called, and it performs the following steps:

-   **Azure Function (****ND JSON Converter) --** This calls the Azure function, ND JSON Converter, which converts the converted JSON file (from Copy Data Activity) to ND JSON format and saves that file in the nd-json folder (under asset-processed-template container).

-   **Web --** This API calls the JOBSAPI by the PUT method. This API is provided by Azure Digital Twin. The input parameter for this API is the location of the ND JSON file. After calling JOBSAPI, a job for the creation of twins will be created in Azure Digital Twin.

-   **Until** **--** This API calls the JOBSAPI to get the status of the job that was created by the above \"Web\" activity. Job status can be \'succeeded\', \'failed\', or \'notstarted\'. When the job succeeds, the Operation Hierarchy is visible on the Azure Digital Twin Explorer.

> Below is the workflow diagram for ADF-child-pipeline-JOBSAPI.

![ADF child pipeline JOBS API flow](./media/IAI_AH_Creation_Azure/image8.png)

After successful execution of this pipeline, logs will appear as below on the Azure Data Factory studio.

![execution logs](./media/IAI_AH_Creation_Azure/image9.png)

### 

## ADF-child-pipeline-DurableFunctionApp

When the Update_Archive flag exists, the ADF-child-pipeline-DurableFunctionApp is called, and it performs the following steps:

-   **Azure Function --** The Durable Azure Function is called. The name of the JSON file (from Copy Data Activity) is passed as the input parameter, and Update/Archive the asset based on the Update_Flag in the uploaded template and returns a URL for checking the completion status of the Function App.

After uploading the template with Update_Flag as Add for assets and the successful run of the ADF pipeline, the Azure Digital Twin will have the new twins in AH. A sample screenshot of the same is given below.

-   **Set Variable --** In this step, the final status (succeeded/failed) is obtained from the Durable Function app output URL.

![ADF-child-pipeline-DurableFunctionApp flow](./media/IAI_AH_Creation_Azure/image10.png)

Successful execution of this pipeline appears as below.

![execution logs](./media/IAI_AH_Creation_Azure/image11.png)

## 

# Implementation/Result

### Add

After uploading the template with Update_Flag as \'Add\' for assets and the successful run of the ADF pipeline, the Azure Digital Twin will have the new twins updated with the AH. A sample screenshot of the same is given below.

![ADT explorer showing the result of the ADF pipeline with OH of the twins created](./media/IAI_AH_Creation_Azure/image12.png)

### 

## 

### Update

Once the template with the Update_Flag for the assets set to Update has been uploaded and the ADF pipeline has been run successfully, the properties of twins with Update as Update_Flag will get updated. The updated properties can be seen by clicking the updated twin.

![Twin properties showing the update](./media/IAI_AH_Creation_Azure/image13.png)

### 

## Archive

Once the template with Update_Flag for the assets set to Archive has been uploaded and the ADF pipeline has been run successfully, the isActive property of twins with Archive as Update_Flag will be updated to false. If needed, the isActive property can be reverted to true by uploading the template again with Update_Flag as \'update\' for the required twin.

![Twin properties showing the Archive](./media/IAI_AH_Creation_Azure/image14.png)
