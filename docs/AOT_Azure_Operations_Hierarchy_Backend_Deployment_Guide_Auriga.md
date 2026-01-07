---
id: aot-azure-operations-hierarchy-backend-deployment-guide-auriga
title: AOT Azure Operations Hierarchy Backend Deployment Guide Auriga
---

**AOT on Azure**

**Operations Hierarchy**

**BACKEND DEPLOYMENT GUIDE**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin / Operations Hierarchy |
| **Domain / Area** | Digital Twin / Asset Management |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Ranganathan, Balamurugan |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Operations Hierarchy UI Guide, Operations Hierarchy API Reference |

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Deployment Pipeline [4](#deployment-pipeline)](#deployment-pipeline)

[AOT- OperationsHierarchy-Module-IaC-MS Pipeline [4](#aot--operationshierarchy-module-iac-ms-pipeline)](#aot--operationshierarchy-module-iac-ms-pipeline)

[Deployment Steps [5](#deployment-steps)](#deployment-steps)

# 

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Operations Hierarchy (OH) is an AOT component that lets users navigate the plant's asset hierarchy and access comprehensive node data. Presented as a tree or two-dimensional view of the plant structure, OH typically starts at the company level and drills down through regions, plants, lines, units, systems, subsystems, and equipment. Integrated with other AOT tools, OH enables access to insights and filtered KPIs for each node.

## Purpose

This guide outlines the deployment process for the OH Module APIs, including Infrastructure as Code Microservice (IaC MS) and Swagger file deployment. It explains how to set up the backend for OH for AOT on the Azure platform and details the creation of resources including the API management platform.  
**Prerequisites**

- Azure license/subscription to create resources for implementation.

- Azure DevOps repository for extractor code, ARM templates, and pipeline files.

- A service connection on Azure DevOps for running ARM templates.

- A library to hold the parameters needed to run the template pipeline.

- Azure service connections for SonarQube and Container Registry.

- Storage Account

- Azure Kubernetes Cluster

- Container Registry

- Namespace in the AKS cluster for environments

- Kubernetes Service Connection for AKS Cluster

- Sonar project and key

##  Target Audience

Developers with the following skills:

- Python

- Azure Pipelines

- Swagger Document

## Contacts

- ``

- ``

## Related Links

- [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- AOT OH [Documentation](https://industryxdevhub.accenture.com/assetdetails/76)

- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

# 

# 

## Glossary

| **Term** | **Definition** |
|----|----|
| Azure Pipelines | A cloud-based service in Azure DevOps that automates the building, testing, and deployment of code projects. |
| Swagger Document | A specification for describing and documenting RESTful APIs, enabling both humans and computers to understand the API’s capabilities. |
| API Management (APIM) | A platform for managing, publishing, and securing APIs, providing a central point for API access and monitoring. |
| IaC (Infrastructure as Code) | The practice of managing and provisioning infrastructure through machine-readable definition files, rather than manual processes. |
| Pipeline | A sequence of automated processes or stages that deliver software from development to deployment. |
| Deployment | The process of releasing, installing, and configuring a software application into a production environment. |
| Test Cases | Specific scenarios designed to verify that a software application functions as expected under various conditions. |
| APIs | Application Programming Interfaces, which allow different software applications to communicate with each other. |
| Image | A packaged version of an application or environment, often used to ensure consistency across deployments. |
| Environment | A distinct configuration space (such as development, testing, or production) where applications are developed, tested, or deployed. |

# Deployment Pipeline

The deployment depends on the AOT- OperationsHierarchy-Module-IaC-MS and AOT- OperationsHierarchy-Config-IaC-MS pipeline to create the environment, build the image, run test cases, and deploy the APIs in the API Management using a swagger file. The outcome of this pipeline will enable the user to validate the APIs deployed on the APIM. There are three stages of the pipeline. Each stage serves a specific purpose as described below.

## AOT- OperationsHierarchy-Module-IaC-MS Pipeline

| **Stage** | **Purpose** | **Name** | **Process** | **File** |
|:---|:---|:---|:---|:---|
| 1 | CreateImage | DockerContanerBuildAndPush | To run test cases, run a SonarQube check, build the docker image and push the image to the container registry, then create the Artifact for the next stage. | jobimagebuildtemplate.yml |
| 2 | DeployApplication | KubernetesDeployment | Use the Artifact created in the previous step and the deploying docker container. | jobapplicationdeploytemplate.yml |
| 3 | APIMIntegration | ApiImportAutomation | Use the Swagger Document to import and create the API. | ohapideployment.yml |

The YML files listed in the table above can be found at the following file paths:

- Consumption/DataAccess/OperationsHierarchy/Module_APIs/oh_middleware/oh_ms/pipeline/

- Consumption/DataAccess/OperationsHierarchy/Configuration/oh_config_middleware/oh_config_ms/pipeline

# 

# 

# Deployment Steps

1.  Create a library in the DevOps portal with the following variable groups.

    1.  DEV-AOT-AZURE-INFRASTRUCTURE-VARIABLE

    2.  DEV-AOT-AZURE -APP-GLOBAL-VARIABLE

    3.  DEV-AOT-AZURE-OH-BE-VARIABLE

2.  Update the library with the corresponding variables listed in the sheet [AOT_Azure_OH_Backend_Deployment_Variables.xlsx](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20OH%20Backend%20Deployment%20Guide/AOT_Azure_OH_Backend_Deployment_Variables.xlsx?d=w8bc80a63f4af481c9731f9e59aa27160&csf=1&web=1&e=KI5hWt).



3.  Update the pipeline file with the relevant library name as shown in the screenshots below for both Module and Config APIs.

  

4.  Check each YML file found in the folder below to verify that the configured values in each step are updated as necessary.

Consumption/DataAccess/OperationsHierarchy/Module_APIs/oh_middleware/oh_ms/pipeline/



Consumption/DataAccess/OperationsHierarchy/Configuration/oh_config_middleware/oh_config_ms/pipeline



5.  Open the YML files and verify that the parameters are present under the *CreateImage*, *DeployApplication*, and *ApiImportAutomation* stages.

6.  Create and then run the pipeline from the following pipeline files:

    1.  Consumption/DataAccess/OperationsHierarchy/Module_APIs/oh_middleware/oh_ms/pipeline/azure-pipelines.yml

    2.  Consumption/DataAccess/OperationsHierarchy/Configuration/oh_config_middleware/oh_config_ms/pipeline/azure-pipelines.yml

7.  In the Azure portal, validate that the correct set of APIs was created in API management and that their policies were updated for both OH Module Middleware and OH Config Middleware.




