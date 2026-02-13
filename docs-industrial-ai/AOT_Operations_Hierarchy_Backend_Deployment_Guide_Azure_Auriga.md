---
sidebar_position: 2
title: AOT Operations Hierarchy Backend Deployment Guide Azure Auriga
---

**Accenture Operations Twin**

**Operations Hierarchy**

**BACKEND DEPLOYMENT GUIDE (AZURE)**

Release Version: 2.5

**Metadata Table**

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / Operations Hierarchy

  **Domain / Area**                   Digital Twin / Asset Management

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Ranganathan, Balamurugan

  **Status**                          Published / Approved

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   Operations Hierarchy UI Guide, Operations Hierarchy API Reference
  -----------------------------------------------------------------------------------------------------------------

#  \{#section .TOC-Heading\}

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [4](#glossary)](#glossary)

[Deployment Pipeline [5](#deployment-pipeline)](#deployment-pipeline)

[AOT- OperationsHierarchy-Module-IaC-MS Pipeline [5](#aot--operationshierarchy-module-iac-ms-pipeline)](#aot--operationshierarchy-module-iac-ms-pipeline)

[Stage 1: CreateImage [5](#stage-1-createimage)](#stage-1-createimage)

[Stage 2: DeployApplication [5](#stage-2-deployapplication)](#stage-2-deployapplication)

[Stage 3: APIMIntegration [5](#stage-3-apimintegration)](#stage-3-apimintegration)

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Operations Hierarchy (OH) is an AOT component that lets users navigate the plant\'s asset hierarchy and access comprehensive node data. Presented as a tree or two-dimensional view of the plant structure, OH typically starts at the company level and drills down through regions, plants, lines, units, systems, subsystems, and equipment. Integrated with other AOT tools, OH enables access to insights and filtered KPIs for each node.

## Purpose

This guide outlines the deployment process for the OH Module APIs, including Infrastructure as Code Microservice (IaC MS) and Swagger file deployment. It explains how to set up the backend for OH for AOT on the Azure platform and details the creation of resources including the API management platform. **Prerequisites**

-   Azure license/subscription to create resources for implementation.

-   Azure DevOps repository for extractor code, ARM templates, and pipeline files.

-   A service connection on Azure DevOps for running ARM templates.

-   A library to hold the parameters needed to run the template pipeline.

-   Azure service connections for SonarQube and Container Registry.

-   Storage Account

-   Azure Kubernetes Cluster

-   Container Registry

-   Namespace in the AKS cluster for environments

-   Kubernetes Service Connection for AKS Cluster

-   Sonar project and key

## Target Audience

Developers with the following skills:

-   Python

-   Azure Pipelines

-   Swagger Document

## Contacts

-   

-   

## Related Links

-   [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   AOT OH [Documentation](https://industryxdevhub.accenture.com/assetdetails/76)

-   [[AOT Release Notes]\{.underline\}](https://industryxdevhub.accenture.com/assetdetails/45)

## 

## Glossary

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**                       **Definition**
  ------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------
  Azure Pipelines                A cloud-based service in Azure DevOps that automates the building, testing, and deployment of code projects.

  Swagger Document               A specification for describing and documenting RESTful APIs, enabling both humans and computers to understand the API\'s capabilities.

  API Management (APIM)          A platform for managing, publishing, and securing APIs, providing a central point for API access and monitoring.

  IaC (Infrastructure as Code)   The practice of managing and provisioning infrastructure through machine-readable definition files, rather than manual processes.

  Pipeline                       A sequence of automated processes or stages that deliver software from development to deployment.

  Deployment                     The process of releasing, installing, and configuring a software application into a production environment.

  Test Cases                     Specific scenarios designed to verify that a software application functions as expected under various conditions.

  APIs                           Application Programming Interfaces, which allow different software applications to communicate with each other.

  Image                          A packaged version of an application or environment, often used to ensure consistency across deployments.

  Environment                    A distinct configuration space (such as development, testing, or production) where applications are developed, tested, or deployed.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Deployment Pipeline

The deployment depends on the AOT OperationsHierarchy-Module-IaC-MS and AOT- OperationsHierarchy-Config-IaC-MS pipeline to create the environment, build the image, run test cases, and deploy the APIs in the API Management using a swagger file. The outcome of this pipeline will enable the user to validate the APIs deployed on the APIM. There are three stages of the pipeline. Each stage serves a specific purpose as described below.

## AOT- OperationsHierarchy-Module-IaC-MS Pipeline

The deployment process consists of three main stages:

### Stage 1: CreateImage

In this stage, the DockerContanerBuildAndPush process is used to run test cases, perform a SonarQube check, build the Docker image, and push the image to the container registry. An artifact is then created for use in the next stage. This process is defined in the jobimagebuildtemplate.yml file.

### Stage 2: DeployApplication

The KubernetesDeployment process utilizes the artifact produced in the previous step to deploy the Docker container. The configuration for this stage is found in the jobapplicationdeploytemplate.yml file.

### Stage 3: APIMIntegration

During this stage, the ApiImportAutomation process leverages the Swagger Document to import and create the API. The corresponding file for this step is ohapideployment.yml.

The YML files listed above can be found at the following file paths:

-   Consumption/DataAccess/OperationsHierarchy/Module_APIs/oh_middleware/oh_ms/pipeline/

-   Consumption/DataAccess/OperationsHierarchy/Configuration/oh_config_middleware/oh_config_ms/pipelineDeployment Steps\\

1.  Create a library in the DevOps portal with the following variable groups.

    a.  DEV-AOT-AZURE-INFRASTRUCTURE-VARIABLE

    b.  DEV-AOT-AZURE -APP-GLOBAL-VARIABLE

    c.  DEV-AOT-AZURE-OH-BE-VARIABLE



1.  



2.  Update the library with the corresponding variables listed in the sheet [AOT_Azure_OH_Backend_Deployment_Variables.xlsx](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20OH%20Backend%20Deployment%20Guide/AOT_Azure_OH_Backend_Deployment_Variables.xlsx?d=w8bc80a63f4af481c9731f9e59aa27160&csf=1&web=1&e=KI5hWt).

> ![Creating library with variable group in ADO](media/image2.png)\{width="5.948249125109362in" height="3.781806649168854in"\}

3.  

4.  Update the pipeline file with the relevant library name as shown in the screenshots below for both Module and Config APIs.

![Module APIs pipeline file](media/image3.png)\{width="3.0520833333333335in" height="4.197240813648294in"\}

![Config APIs pipeline file](media/image4.png)\{width="3.071514654418198in" height="4.190840988626421in"\}

![Pipeline file updation](media/image5.png)\{width="6.570833333333334in" height="5.4683683289588805in"\}

5.  

6.  Check each YML file found in the folder below to verify that the configured values in each step are updated as necessary.

-   Consumption/DataAccess/OperationsHierarchy/Module_APIs/oh_middleware/oh_ms/pipeline/

> ![azure-pipelines.yml file folder structure for OH module APIs](media/image6.png)\{width="3.6073304899387577in" height="4.94878937007874in"\}

-   Consumption/DataAccess/OperationsHierarchy/Configuration/oh_config_middleware/oh_config_ms/pipeline

> ![azure pipeline yml file in folder structure for config middleware](media/image7.png)\{width="3.6687707786526684in" height="5.349470691163605in"\}

7.  Open the YML files and verify that the parameters are present under the CreateImage, DeployApplication, and ApiImportAutomation stages.

8.  

9.  Create and then run the pipeline from the following pipeline files:

-   Consumption/DataAccess/OperationsHierarchy/Module_APIs/oh_middleware/oh_ms/pipeline/azure-pipelines.yml

-   Consumption/DataAccess/OperationsHierarchy/Configuration/oh_config_middleware/oh_config_ms/pipeline/azure-pipelines.yml

In the Azure portal, validate that the correct set of APIs was created in API management and that their policies were updated for both OH Module Middleware and OH Config Middleware.

![APIM screen for module APIs](media/image8.png)\{width="7.0472222222222225in" height="3.707670603674541in"\}

![APIM screen for config APIs](media/image9.png)\{width="7.0472222222222225in" height="3.645670384951881in"\}
