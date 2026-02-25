---
sidebar_position: 2
title: IAI PI AF Extractor Python Deployment Guide
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">PI AF EXTRACTOR</p>
<p class="doc-type">DEPLOYMENT GUIDE</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / Data Integration Accelerators |
| **Domain / Area** | Extractors / Data Processing |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Joshi, Rishabh |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | IAI Extractors Architecture Blueprint, IAI Extractors Getting Started ![](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image1.png)
|  |

</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools, including extractors, that can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

IAI extractors, also known as data integration accelerators, are developed to automate and simplify the process of extracting data from enterprise source systems and moving it to CDF RAW. IAI\'s PI AF Extractor establishes a connection with the OSI PI system and reads asset hierarchy data from the OSI PI system. It processes and transforms the extracted data to a format that Cognite recognizes before pushing that data to CDF RAW.

### Purpose

This document explains how to extract data from the source system and load it into CDF RAW using the PI AF extractor. It covers the prerequisites for deploying the Extractor, provides instructions for configuring and deploying it in the cloud, and enables the reader to verify the data flow from the source system to CDF.

###  Target Audience

Developers with the following skills:

-   Cognite Data Fusion 

-   Azure Pipeline creation 

-   SonarQube 

-   OSI PI

### Prerequisites

-   Cognite Data Fusion

-   Azure DevOps

-   SonarQube

-   OSI PI

-   [Lens](https://k8slens.dev/) app

Additional prerequisites for deployment are mentioned in respective sections.

### Contacts

-   [hanuman.prasad.gali@accenture.com](mailto:hanuman.prasad.gali@accenture.com)

-   [rishabh.b.joshi@accenture.com](mailto:rishabh.b.joshi@accenture.com)

### Related Links

-   [How to create an Azure Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&amp;tabs=javascript%2Ctfs-2018-2%2Cbrowser)

-   [How to create a Release Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops)

-   [IAI IX Developer Hub Resources](https://industryxdevhub.accenture.com/asset-home;search_text=AOT)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary


| Term | Definition |
| --- | --- |
| Azure Pipeline | A set of automated processes in Azure DevOps used to build, test, and deploy code projects. |
| Release Pipeline | An Azure DevOps pipeline designed to automate the deployment of applications to various environments. |
| AKS Cluster | Azure Kubernetes Service cluster, a managed container orchestration service for deploying and managing containerized applications. |
| Containerizing | The process of packaging software and its dependencies into a container, enabling consistent deployment across environments. |
| PI AF Extractor | A tool that extracts data from PI Asset Framework systems, allowing configuration for multiple sources and assets. |
| Root Asset | The primary asset within a source system from which data extraction begins. |
| On-Prem | Short for \"on-premises\", referring to systems and software deployed within an organization\'s local infrastructure rather than in the cloud. |
| Exception Handling | Built-in methods for detecting and managing errors during the process, ensuring system stability. |
| Timer Option | A configurable feature that enables automatic operation at specified intervals. |
## Features

IAI\'s PI AF Extractor provides users the flexibility to pre-configure multiple source systems, root assets, and other required details in a configuration file. A pipeline is used for both containerizing the extractor and running it on an Azure Kubernetes Cluster. It also includes an extraction pipeline for tracking both successful and failed pipeline runs on CDF UI. On every run, the extractor sends a Success/Failure message about the run and notifies the list of contacts about the same based on the configurations.

The major features of the PI AF Extractor include:

-   User configurable based on business needs

-   The Timer option allows automatic operation at a configurable interval

-   Deployable On-Cloud and On-Prem with minimal user effort

-   Built-in validation and exception handling simplify the configuration

-   Supports multiple source systems and root assets, and respective CDF details 

## 

# Cloud Deployment

Two pipelines are needed to deploy the extractor to an AKS Cluster.

This section includes step-by-step guidance for:

-   Prerequisites that need to be fulfilled before Extractor can be deployed and used 

-   Setting up the Azure DevOps environment

-   Creating a Build Pipeline for Dockerizing the Extractor Package

-   Creating a Release Pipeline for Deploying the Docker Image to AKS Cluster

-   Validating in CDF RAW if the RAW table has the right data

### Prerequisites

-   PI server username and password 

-   Web API URL for each PI AF asset hierarchy

-   Azure license/subscription to create resources

-   Azure DevOps repository for extractor code, and pipeline files

-   Azure service connections for SonarQube and Container Registry

-   Namespace in the AKS cluster for environments

-   Kubernetes Service Connection for AKS Cluster

-   Sonar project and key

### 

## Configure the Environment

A build pipeline and a release pipeline are used to deploy the PI AF Extractor to an AKS Cluster. Follow these steps before creating pipelines:

-   Create an Azure Key Vault.

-   Add the following secrets in the Azure Key Vault created in the previous step: 


| ClientID | Provide the Client ID for CDF |
| --- | --- |
| ClientSecret | Provide the Client Secret for CDF |
| PIUserName | Provide the username for OSI PI Server |
| PIPassword | Provide the password for OSI PI Server &gt; ![Screenshot of Create a secret dialog window](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image3.png)
|  |
| - | Create a key vault library in Azure DevOps and add the secrets created in the previous step. &gt; ![Screenshot of key vault library in Azure DevOps and added secrets created in the previous step.](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image4.png)
|  |
| - | Create a Library/Variable Group in Azure DevOps with the following parameters: |
| **Variable** | **Description** |
| COGNITE_HOST | Provide the host details for CDF. |
| COGNITE_PROJECT | Provide the project name for CDF. |
| SCOPES | Provide the scopes for CDF. |
| TENANT_ID | Provide the tenant ID for CDF. |
| PI_SERVER_WEBAPI_ENDPOINT | Provide the PI server WebAPI endpoint of the OSI PI server. |
| PI_KEY_COLUMN | Provide the key column for filtering data to upload into the CDF RAW table. |
| PI_CONFIG_FILENAME: | Provide the configuration filename that is used to run the extractor. The filenames are environment-specific e.g., pi_config_dev.yaml, pi_config_itest.yaml, and pi_config_prod.yaml |
| CONTAINER_REGISTRY_SERVICE_CONNECTION | Provide container registry service connection for build and release pipeline. |
| SONARQUBE_SERVICE_CONNECTION | Provide service connection for SonarQube. |
| PIAF_CLI_PROJECT_KEY | Provide SonarQube project key for PI AF extractor. |
| PIAF_CLI_PROJECT_NAME | Provide SonarQube project name for PI AF extractor. &gt; ![Screenshot of variable group library AOT-CommonServices-Extractor-dev](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image5.png)
|  |
| - | Navigate to the pipeline file location \"Source/Extractors/PIAF-extractor-2.0/pipeline/Dev/azure-pipelines.yml\" and ensure that the pipeline is referring to the libraries created in the previous steps. &gt; ![Screenshot showing the pipeline file location](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image6.png)
|  |
| - | Configure the following parameters in the configuration file for the PIAF Extractor: |
| - | Provide timer value in seconds to schedule the extractor. &gt; ![screenshot depicting the timer value provided in seconds](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image7.png)
|  |
| - | Mandatory Cognite-related config parameters: |
| **Parameter** | **Description** |
| host | Use the hostname for Cognite data fusion (CDF) added in the Azure DevOps library in earlier steps |
| project | Use the project name for CDF added in the Azure DevOps library in earlier steps |
| idp-authentication. client-id | Use the client Id for CDF added in the Azure DevOps key vault library in earlier steps |
| idp-authentication. secret | Use the client secret for CDF added in the Azure DevOps key vault library in earlier steps |
| idp-authentication. scopes | Use the scopes for CDF added in the Azure DevOps library in earlier steps |
| idp-authentication. tenant | Use the tenant Id for CDF added in the Azure DevOps library in earlier steps &gt; ![Screenshot of the Cognite related config parameters](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image8.png)
|  |
| - | Mandatory OSI PI-related config parameters: PI AF Extractor allows the configuration of multiple OSI PI Systems. Also, multiple root asset details can be configured to fetch asset hierarchy data from the OSI PI systems. |
| **Parameter** | **Description** |
| pi_webapi_endpoint | Use the PI Server WebAPI endpoint of the OSI PI server added in the Azure DevOps library in earlier steps. |
| username | Use the username of the OSI PI system added in the Azure DevOps key vault library in earlier steps. |
| password | Use the password of the OSI PI system added in the Azure DevOps key vault library in earlier steps. |
| key-column | Use the key column for filtering data to upload into the CDF RAW table added in the Azure DevOps library in earlier steps. |
| assets.destination.database | Provide a database name in CDF where the table would be created. |
| assets.destination.table | Provide a table name where asset hierarchy data will be uploaded. |
| assets.path | Provide the root asset\'s path from the OSI PI Server. |
| assets.category_name | OPTIONAL - Provide category name from OSI PI Server to filter child elements in the asset hierarchy. &gt; ![Screenshot of OSI PI related config parameters](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image9.png)
|  |
| - | Extraction pipeline-related config parameters: |
| **Parameter** | **Description** |
| datasetexternal_id | Provide the External id of the Dataset in Cognite data fusion (CDF) |
| dataset_name | Provide the name of the Dataset in CDF |
| external_id | Provide external id of CDF extraction pipeline |
| ep_name | Provide the name of the CDF extraction pipeline |
| contacts.name | OPTIONAL - Provide the name of the contact to whom the extraction pipeline notification should be sent. |
| contacts.email | OPTIONAL - Provide the email of the contact to whom the extraction pipeline notification should be sent. |
| contacts.sendnotification | OPTIONAL - Provide notification value. If the send notification value is true, then mail is sent to the respective mail ID, otherwise, no mail is sent. &gt; ![Screenshot of updating the Extraction pipeline related config parameters](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image10.png)
|  |

### 

## Create a Build Pipeline 

The Build Pipeline is used to Dockerize the Extractor Package. The artifacts created here are used in the release pipeline for deployment.

To create a build pipeline, follow the steps below:

-   Navigate to Azure DevOps, select Pipelines, and then select New Pipeline.

> ![Screenshot showing the New Pipeline option in Azure DevOps](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image11.png)
-   Select **Azure Repos Git**. Then select the Repository Name that contains the PI AF Extractor code and pipeline files.

> ![Screenshot of Azure DevOps showing the option Azure Repos Git](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image12.png)

-   Select \'Existing Azure Pipelines YAML file\'.

> ![Screenshot of Azure DevOps showing the option \'Existing Azure Pipelines YAML file\'](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image13.png)
-   Select the branch, provide the pipeline file path as \"Source/Extractors/PIAF-extractor-2.0/pipeline/Dev/azure-pipelines.yml\", and then select **Continue.**

> ![Screenshot that shows configuring the pipeline and the dialog window to select an existing YAML file.](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image14.png)
-   Review and save.

-   Run the pipeline and wait for its successful completion.

### Create a Release Pipeline

The Release pipeline deploys the Docker Image of the PI AF Extractor created by the build pipeline to the AKS Cluster.

Follow the below steps to create the PI AF Extractor release pipeline:

-   Create a release pipeline with two tasks for AKS Cluster.

    -   task with delete command

    -   task with create command

-   Update the value of the service connection for the AKS cluster in the tasks.

> ![Screenshot showing the updated value of service connection for AKS cluster in the tasks](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image15.png)
-   Update the AKS file location in the tasks.

> ![Screenshot showing how the AKS file location is updated in the tasks](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image16.png)

-   If this is the first run, then disable the delete task from the pipeline. 

> ![Screenshot showing the disabling of the delete task from the pipeline](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image17.png)
-   Create a release from the release pipeline created in the previous step. 

> ![Screenshot showing the option \'Create Release\'](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image18.png)
-   Once the release is completed, confirm that the deployment is successful on Azure DevOps.

> ![Screenshot showing the successful deployment on Azure DevOps](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image19.png)
-   After deployment is complete, check the Azure Portal to validate that the deployment to the AKS cluster was successful.

> ![Screenshot showing the successful validation of deployment to AKS cluster in Azure portal](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image20.png)
-   Validate PI AF Extractor logs on the [Lens](https://k8slens.dev/) app. Note that the Lens App is an external tool to check logs of the AKS Cluster.

> ![Screenshot of Lens app showing the logs](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image21.png)

-   If everything looks good and the AKS POD is created, enable the delete task that was previously disabled.

> ![Screenshot showing the options to enable the delete task that was previously disabled.](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image22.png)
-   Validate the creation of the database and table with asset hierarchy data on the CDF Portal.

> ![Screenshot of validating the creation of database and table with asset hierarchy data on Cognite Data Fusion Portal.](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image23.png)
-   When the deployment is complete, an extraction pipeline is created in CDF based on the details provided in the configuration file. A Success/Failure message can be visualized on the CDF portal. Also, a notification is sent to the respective email address.

> ![Success message displayed in CDF after deployment is complete successfully](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image24.png)
## 

# On-Prem Deployment 

The PI AF Extractor Windows Service is created to give users the option of deploying the PI AF Extractor on-premises. The PI AF Extractor Windows service is installed through a batch script that runs all the necessary commands required for the installation. The PI AF Extractor extracts asset hierarchy data from one or more OSI PI systems and inserts it into CDF RAW.

### Prerequisites

-   PI server username and password 

-   Web API URL for each PI AF asset hierarchy

-   Install Python

### Install the Extractor

Follow the below steps to install PI AF Extractor on-premises:

-   Edit **pi_config.yaml** file to update the following:

-   Add the path of a log file to store extractor logs.

> ![Screenshot showing the added path of a log file to store extractor logs.](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image25.png)
-   Add timer value in seconds to schedule the extractor.

> ![Screenshot showing the added timer value in seconds to schedule the extractor.](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image7.png)
-   Add mandatory Cognite-related details:


| **Parameter** | **Description** |
| --- | --- |
| host | Provide the hostname for CDF |
| project | Provide the project name for CDF |
| idp-authentication. client-id | Provide the client Id for CDF |
| idp-authentication. secret | Provide the client secret for CDF |
| idp-authentication. scopes | Provide the scopes for CDF |
| idp-authentication. tenant | Provide the tenant Id for CDF |
| - | Add extraction pipeline-related details: |
| **Parameter** | **Description** |
| datasetexternal_id | Provide the external Id of the dataset in CDF. |
| dataset_name | Provide the name of the dataset in CDF. |
| external_id | Provide external Id of CDF extraction pipeline. |
| ep_name | Provide the name of the CDF extraction pipeline. |
| contacts.name | OPTIONAL - Provide the name of the contact to whom the extraction pipeline notification should be sent. |
| contacts.email | OPTIONAL - Provide the email of the contact to whom the extraction pipeline notification should be sent. |
| contacts.sendnotification | OPTIONAL - Provide notification value. If the send notification value is true, then mail is sent to the respective mail Id else no mail is sent. |
| - | Add OSI PI system configurations: |
| **Parameter** | **Description** |
| pi_webapi_endpoint | Provide the PI Server WebAPI endpoint of the OSI PI server. |
| username | Provide the username of the OSI PI system. |
| password | Provide the password of the OSI PI system. |
| key-column | Provide the key column for filtering data to upload into the CDF RAW table. |
| assets.destination.database | Provide a database name in CDF where the table would be created. |
| assets.destination.table | Provide a table name where asset hierarchy data will be uploaded. |
| assets.path | Provide assets path from OSI PI system. |
| assets.category_name | OPTIONAL - Provide the category name from the OSI PI system to filter child elements in the asset hierarchy. |
| - | Edit **WSInstallation.bat** file to add the absolute path of the Python folder and PIAFWindowsService.py file as shown below. &gt; ![Screenshot showing the Edit of WSInstallation.bat file to add the absolute path of python folder and PIAFWindowsService.py file ](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image26.png)
|  |
| - | For the on-premise installation of the PI AF Extractor, right-click on the WSInstallation.bat file and select Run as Administrator. The file installs all the required Python modules and PI AF extractor as a windows service. |
| - | Verify the following libraries are installed correctly in the system. |
| - | pywin32 module |
| - | cognite-extractor-utils module |
| - | pythonX.dll |
| - | pythonXX.dll |
| - | pythoncomXX.dll |
| - | pywintypesXX.dll &gt; ![Screenshot of the libraries installed in the system](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image27.png)
|  |

### 

## Start the Extractor

-   Click the **Start** button, search for \"Services\", and select **Run as Administrator.** 

> ![Screenshot of Services app in Start menu showing the option to run as adminstrator](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image28.png)
-   Search for the \"PIAFExtractor\" service name, right-click on it, and select **Start**.

> ![Screenshot showing the PIAF Extractor and the option to Start the service](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image29.png)
-   Once the PI AF Extractor starts running, check the logs in the log file specified in the configuration file.

-   Validate the creation of the database and tables with asset hierarchy data on the CDF portal.

> ![Screenshot of CDF portal where the database and tables with asset hierarchy data are created](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image23.png)
-   Validate the creation of the extraction pipeline with a success message on the CDF portal.

> ![Success message shown on CDF portal](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image24.png)
### 

## Stop the Extractor

-   Click the **Start** button, search for \"Services\", and select **Run as Administrator.** 

> ![Screenshot showing the Services App in Start menu and the option to run as adminstrator](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image28.png)
-   Search for the \"PIAFExtractor\" service name, right-click on it, and select **Stop**.

> ![Screenshot showing the PIAF Extractor service and the option to Stop](./media/IAI_PI_AF_Extractor_Python_Deployment_Guide/image30.png)
