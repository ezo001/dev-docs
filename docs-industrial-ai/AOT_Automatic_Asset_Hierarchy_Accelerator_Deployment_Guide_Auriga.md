---
sidebar_position: 2
title: AOT Automatic Asset Hierarchy Accelerator Deployment Guide Auriga
---

**Accenture Operations Twin**

Automatic Asset Hierarchy Accelerator

**DEPLOYMENT GUIDE**

Release Version 2.5

**Metadata Table**

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / Data Integration Accelerators

  **Domain / Area**                   Extractors / Data Processing

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Joshi, Rishabh

  **Status**                          Published / Complete

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   AOT Extractors Architecture Blueprint, AOT Extractors Getting Started
  -----------------------------------------------------------------------------------------------------------------

# 

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [4](#glossary)](#glossary)

[Background [4](#background)](#background)

[Prepare Azure [5](#prepare-azure)](#prepare-azure)

[Prepare Accelerator Config File [7](#prepare-accelerator-config-file)](#prepare-accelerator-config-file)

[Cognite Parameters [7](#cognite-parameters)](#cognite-parameters)

[Transformation Parameters [7](#transformation-parameters)](#transformation-parameters)

[Extraction Parameters [8](#extraction-parameters)](#extraction-parameters)

[Create a Build Pipeline [9](#create-a-build-pipeline)](#create-a-build-pipeline)

[Create a Release Pipeline [11](#create-a-release-pipeline)](#create-a-release-pipeline)

[Result [15](#result)](#result)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including extractors, which can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT\'s Automatic Asset Hierarchy accelerator has been specifically developed to simplify the process of creating the asset hierarchies required by Cognite Data Fusion (CDF). It can be used in combination with other extractors or by other means if the RAW data is already available in CDF. After an extractor or any other manual source has inserted data into the CDF table, this accelerator can be used to trigger the auto-creation of the Asset Hierarchy in CDF. Based on CDF Transformations, the user can use [Spark SQL queries](https://docs.cognite.com/cdf/integration/guides/transformation/write_sql_queries) to transform data from the CDF staging area and RAW, into [the CDF data model](https://docs.cognite.com/cdf/learn/cdf_basics/cdf_basics_datamodel). The accelerator supports four types of Transformation namely Asset Hierarchies, Events, Relationships, and Labels. Also, it supports multiple action types available for these transformations.

## Purpose

This document explains how to configure and run the automatic asset hierarchy element and verify the resulting transformation and asset hierarchy, events, relationships, or label actions in CDF. It also provides an understanding of the process of configuring the automatic asset hierarchy element and validating it in CDF. After reading the document, a developer should be able to perform these tasks successfully.

## Target Audience

Developers with the following skills:

-   Azure Pipeline creation

-   SonarQube

-   CDF

## Prerequisites

-   Azure license/subscription to create resources for implementation

-   Azure DevOps repository for extractor code and pipeline files

-   Azure service connections for SonarQube and Container Registry

-   Namespace in the AKS cluster for environments

-   Kubernetes Service Connection for AKS Cluster

-   SonarQube project name and key

-   [Lens](https://k8slens.dev/) app

## Contacts 

-   

-   

## Related Links

-   [How to Create an Azure Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=javascript%2Ctfs-2018-2%2Cbrowser)

-   [How to Create a Release Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops)

## Glossary

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Term                                    Definition
  --------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  Kubernetes Service Connection           A configuration that enables secure communication between Azure DevOps and a Kubernetes (AKS) cluster for deploying applications.

  AKS Cluster                             Azure Kubernetes Service cluster, a managed container orchestration service offered by Microsoft Azure.

  SonarQube Project Name and Key          Identifiers used in SonarQube to manage and track code quality metrics for a specific project.

  Lens App                                A desktop application that provides a graphical interface for managing and monitoring Kubernetes clusters.

  Azure Pipeline                          A continuous integration and delivery (CI/CD) service in Azure DevOps used to automate build, test, and deployment processes.

  Release Pipeline                        A workflow in Azure DevOps that automates the deployment of applications to various environments after build completion.

  Automatic Asset Hierarchy Accelerator   A tool that dynamically creates, schedules, and manages asset hierarchies in CDF based on configuration files.

  Transformation Destination Type         The target type in CDF where transformed data is sent, such as asset, event, or relationship.

  Transformation Action Type              The operation performed in CDF, such as creation, update, or deletion of assets or relationships.

  Extraction Pipeline                     A process that extracts data from a source system, transforms it, and loads it into CDF, providing run status notifications.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Background

Like AOT extractors, this accelerator is dynamic and config file-driven. Configurations like transformation details (external ID, name, query, schedule, Transformation Destination type, Transformation Action Type) and CDF environment details can be added to the config file so that the respective transformation is created, scheduled, and run as per the configured details. In return, asset hierarchies, events, relationships, and labels are created, updated, or deleted as necessary. When combined with extractors, the Automatic Asset Hierarchy element helps to automate the flow from AH Data extraction from the source system to Asset Hierarchy creation in CDF.

AOT\'s Automatic Asset Hierarchy accelerator has Extraction pipeline functionality to get an overview of both successful and failed pipeline runs on CDF UI. On every run, the extractor sends a Success/Failed detailed message about the run and notifies the list of contacts about the same based on the configurations.

Main features of the Automatic Asset Hierarchy creation:

-   User configurable based on the business needs

-   The timer option allows automatic operation on a configurable interval

-   Deployable On-Cloud with little user effort

-   Built-in validations and exception handling simplify configuration

-   Supports creating multiple transformations destination type and respective action type in CDF

Both a build pipeline and a release pipeline are needed to deploy the Automatic Asset Hierarchy Accelerator to an AKS Cluster. Before creating the pipelines, the environment must be prepared.

# 

# Prepare Azure

-   Create an Azure Key Vault.

-   Add the following secrets to the new Azure Key Vault:



-   **ClientId**: Provide the Client ID for CDF.

-   **ClientSecret**: Provide the Client Secret for CDF.

> ![Screenshot showing the \'Create a secret\' window and fields to be filled.](media/image2.png)\{width="5.397916666666666in" height="3.733997156605424in"\}

-   Create a key vault library in Azure DevOps and add the secrets created in the previous step.

> ![Screenshot showing the variable group and the secrets added to it.](media/image3.png)\{width="5.398549868766405in" height="3.1041666666666665in"\}

-   

-   Create a Library/Variable Group in Azure DevOps with the following parameters:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                           **Description**
  --------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  COGNITE_HOST                            Provide the host details for Cognite data fusion

  COGNITE_PROJECT                         Provide the project name for Cognite data fusion

  SCOPES                                  Provide the scopes for Cognite data fusion

  TOKEN_URL                               Provide the token URL for Cognite data fusion

  CONTAINER_REGISTRY_SERVICE_CONNECTION   Provide container registry service connection for build and release pipeline.

  SONARQUBE_SERVICE_CONNECTION            Provide service connection for SonarQube

  AUTOMATIC_ASSET_HR_CLI_PROJECT_KEY      Provide SonarQube project key for Automatic Asset Hierarchy Accelerator

  AUTOMATIC_ASSET_HR_CLI_PROJECT_NAME     Provide SonarQube project name for Automatic Asset Hierarchy Accelerator

  AUTOMATIC_AH_CONFIG_FILENAME            Provide the configuration filename that is used to run the extractor. The filenames are environment-specific for assethierarchy_dev_config.YAML, assethierarchy_itest_config.YAML and assethierarchy_prod_config.YAML
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![Screenshot of Variable group tab showing the parameters](media/image4.png)\{width="7.0325207786526684in" height="1.8020833333333333in"\}

-   Navigate to the pipeline file location \"Source/Extractors/AutomaticAssetHierarchy/pipeline/Dev/azure-pipelines.yml\" and ensure that the pipeline refers to the libraries created in the previous steps.

> ![Screenshot showing the location of azure-pipelines.yml file.](media/image5.png)\{width="7.031944444444444in" height="1.128041338582677in"\}

# 

# Prepare Accelerator Config File

Configure the parameters for Cognite, transformation, and extraction in the configuration file for the Automatic Asset Hierarchy Accelerator.

Parameters are mandatory unless specified as optional.

## Cognite Parameters

  -----------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                   **Description**
  ------------------------------- ---------------------------------------------------------------------------------------------------
  host                            Use the hostname for Cognite data fusion (CDF) added in the Azure DevOps library in earlier steps

  project                         Use the project name for CDF added in the Azure DevOps library in earlier steps

  idp-authentication. client-id   Use the client ID for CDF added in the Azure DevOps key vault library in earlier steps

  idp-authentication. secret      Use the client secret for CDF added in the Azure DevOps key vault library in earlier steps

  idp-authentication. scopes      Use the scopes for CDF added in the Azure DevOps library in earlier steps

  idp-authentication. token_url   Use the token_url for CDF added in the Azure DevOps library in earlier steps
  -----------------------------------------------------------------------------------------------------------------------------------

![screenshot of Cognite parameters](media/image6.png)\{width="3.6875in" height="1.759245406824147in"\}

## Transformation Parameters

The transformation parameters are listed in the table below.

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                **Description**
  ---------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Transformation_External_Id   Provide the external ID of Transformation.

  Transformation_Name          Provide the name of Transformation.

  Transformation_Type          Provide the destination type of the Transformation.  AvailableOptions: \[\'asset hierarchies\', \'labels\', \'events\', \'relationships\'\]. Refer note below.

  Action_Type                  Provide the action type of the transformation. AvailableOptions: \[\'create\', \'create or update\', \'update\', \'delete\'\]. Refer note below.

  SQLQuery                     Provide the Spark SQL query for the transformation.

  CDF_DataSetExternalID        Provide the CDF Dataset External ID to be linked to asset hierarchy/events/labels/relationships

  Schedule.Schedule_Time       Optional - Provide the Cron expression to schedule the transformation at a given time.

  Schedule.Is_paused           Optional - Provide a Boolean value. If true, the transformation is paused.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The table below lists the destinations and available actions for a transformation.

  ---------------------------------------------------------------------------
  **Transformation Type**   **Action Type**
  ------------------------- -------------------------------------------------
  asset hierarchies         create or update, delete

  labels                    Create, delete

  events                    Update, delete, create, create or update

  relationships             Update, delete, create, create or update
  ---------------------------------------------------------------------------

Note that:

-   Transformation Type (Destination) is the CDF Resource Type that a user wants to ingest data into.

-   The Action Type tells how the user wants to handle data that is already present at the destination.

-   CDF offers a variety of Destination and Action Types. Each Destination Type has its own set of Action Types.

![Screenshot showing the parameter and available actions for them](media/image7.png)\{width="7.083333333333333in" height="1.7855380577427822in"\}

## Extraction Parameters

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**               **Description**
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  datasetexternal_id          Provide the external ID of the Dataset in Cognite data fusion (CDF)

  dataset_name                Provide the name of the Dataset in CDF

  external_id                 Provide the external ID of the CDF extraction pipeline

  ep_name                     Provide the name of the CDF extraction pipeline

  contacts.name               Optional - Provide the name of the contact to whom the extraction pipeline notification should be sent.

  contacts.email              Optional - Provide the email of the contact to whom the extraction pipeline notification should be sent.

  contacts.sendnotification   Optional - Provide notification value. If the send notification value is true, then mail is sent to the respective mail ID else no mail is sent.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Screenshot showing the extraction pipeline config parameters](media/image8.png)\{width="3.070739282589676in" height="1.9895833333333333in"\}

# Create a Build Pipeline

The Build Pipeline is used to Dockerize the Extractor Package. The artifacts created here are used in the release pipeline for deployment.

1.  Navigate to Azure DevOps, select \"Pipelines\", and then select \"New Pipeline.\"

> ![Screenshot of Azure DevOps showing the pipelines screen and option for \'New Pipeline\'](media/image9.png)\{width="7.260416666666667in" height="1.7017136920384952in"\}

2.  Select \"Azure Repos Git\" then Select Repository Name that contains Automatic Asset Hierarchy Accelerator code and pipeline files and then select \"Existing Azure Pipelines YAML file.\"

> ![Screenshot of ADO showing the option of Azure Repos Git](media/image10.png)\{width="4.384714566929134in" height="1.9479166666666667in"\}![Screenshot of ADO showing \'Existing Azure Pipelines YAML file\' option](media/image11.png)\{width="6.041666666666667in" height="2.7756135170603673in"\}

3.  

4.  Select the branch and provide the pipeline file path as \"Source/Extractors/AutomaticAssetHierarchy/pipeline/Dev/azure-pipelines.yml\" and then select Continue.

![Screenshot showing the window and options to select branch and provide pipeline file path](media/image12.png)\{width="7.425940507436571in" height="3.403558617672791in"\}

5.  Review and save.

6.  Run the pipeline and wait for its successful completion.

![Screenshot showing the option \'Run pipeline\'.](media/image13.png)\{width="7.424568022747157in" height="1.407574365704287in"\}

# 

# Create a Release Pipeline

The Release pipeline deploys the Docker Image of the Automatic Asset Hierarchy Accelerator created by the build pipeline to the AKS Cluster.

1.  Create a release pipeline with two tasks for the AKS Cluster.

    -   The task with the delete command

    -   The task with create command

2.  Update the value of the service connection for the AKS cluster in the tasks.

> ![Screenshot showing the field that needs to be updated with the value of service connection for AKS cluster](media/image14.png)\{width="7.070138888888889in" height="3.0489982502187227in"\}

3.  Update the AKS file location in the tasks.

> ![Screenshot showing the AKS file location](media/image15.png)\{width="7.1066207349081365in" height="1.880295275590551in"\}

4.  

5.  Disable the delete task after running the pipeline the first time.

> ![Screenshot showing the option to disable the delete task from the pipeline](media/image16.png)\{width="6.864583333333333in" height="3.117665135608049in"\}

6.  Create a release from the release pipeline created in the previous step.

> ![Screenshot showing the page and option to \'Create release\'.](media/image17.png)\{width="6.927083333333333in" height="1.1256506999125109in"\}

7.  Once the release is completed, confirm that the deployment was successful on Azure DevOps.

> ![Screenshot showing the successful deployment on ADO.](media/image18.png)\{width="4.34375in" height="3.0949212598425198in"\}

8.  

9.  After deployment, validate successful deployment to the AKS cluster in the Azure portal.

> ![Screenshot showing the successful deployment to AKS cluster](media/image19.png)\{width="7.0312456255468065in" height="1.8164052930883638in"\}

10. Use [Lens](https://k8slens.dev/) to validate Automatic Asset Hierarchy Accelerator logs.

> ![Screenshot of Lens App](media/image20.png)\{width="7.134912510936133in" height="3.998523622047244in"\}

11. 

12. If everything looks good and AKS POD is created, enable the delete task that was previously disabled.

> ![Screenshot showing the option to enable and disable selected task](media/image21.png)\{width="7.1140157480314965in" height="3.260590551181102in"\}

13. Validate successful transformation run in CDF.

> ![Screenshot showing the successful transformation run in CDF](media/image22.png)\{width="7.088347550306212in" height="3.189757217847769in"\}

# 

# Result

When the deployment is completed, an extraction pipeline is created in CDF based on the details provided in the configuration file.

Success/Failure message is visible on the CDF portal and a notification email has been sent.

![An example of the Success message visible on CDF portal after deployment and extraction pipeline creation](media/image23.png)\{width="7.422717629046369in" height="0.9587674978127734in"\}

![An example of the Failure message visible on CDF portal after deployment and extraction pipeline creation](media/image24.png)\{width="7.43540791776028in" height="0.929426946631671in"\}
