---
sidebar_position: 2
title: AOT Azure Deployment Guide Auriga
---

Accenture Operations Twin

Azure Environment

**DEPLOYMENT GUIDE**

Release Version: 2.5

**Metadata Table**

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / AOT

  **Domain / Area**                   Azure / Deployment

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Shivananda, Prashanth

  **Status**                          Published / Approved

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   AOT CDF Deployment Guide
  -----------------------------------------------------------------------------------------------------------------

**Contents**

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Contact [3](#contact)](#contact)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Deployment Prerequisites [4](#deployment-prerequisites)](#deployment-prerequisites)

[Create Azure Pipeline [4](#create-azure-pipeline)](#create-azure-pipeline)

[Clone Repository [4](#clone-repository)](#clone-repository)

[Azure [4](#azure)](#azure)

[Service Principal Configuration [5](#service-principal-configuration)](#service-principal-configuration)

[Create ARM Service Connection [6](#create-arm-service-connection)](#create-arm-service-connection)

[Infrastructure Deployment [7](#infrastructure-deployment)](#infrastructure-deployment)

[Deployment Steps [7](#deployment-steps)](#deployment-steps)

[Deployment Details [7](#deployment-details)](#deployment-details)

[Data Ingestion [9](#data-ingestion)](#data-ingestion)

[Backend Deployment [11](#backend-deployment)](#backend-deployment)

[Application Deployment [11](#application-deployment)](#application-deployment)

[UI Artifacts [14](#ui-artifacts)](#ui-artifacts)

[UI Deployment [15](#ui-deployment)](#ui-deployment)

[Deployment Steps [16](#deployment-steps-2)](#deployment-steps-2)

[UI Components [17](#ui-components)](#ui-components)

[Other Configurations [18](#other-configurations)](#other-configurations)

[CORS(App Services) [18](#corsapp-services)](#corsapp-services)

[CORS (APIM) [18](#cors-apim)](#cors-apim)

[CORS (Storage Account) [19](#cors-storage-account)](#cors-storage-account)

[APIM [19](#apim)](#apim)

[NSG [20](#nsg)](#nsg)

[Client Env [21](#client-env)](#client-env)

[HostApp Deployment [21](#hostapp-deployment)](#hostapp-deployment)

[AAD User Settings [21](#aad-user-settings)](#aad-user-settings)

[Key Vault Configurations [21](#key-vault-configurations)](#key-vault-configurations)

[Interdependencies [22](#interdependencies)](#interdependencies)

[People Management [22](#people-management)](#people-management)

[Production Manager [22](#production-manager)](#production-manager)

[SmartKPI [22](#smartkpi)](#smartkpi)

[Generic Scheduler [22](#generic-scheduler)](#generic-scheduler)

[Intelligent -Advisor [22](#intelligent--advisor)](#intelligent--advisor)

[3D [22](#d)](#d)

[PowerBI [22](#powerbi)](#powerbi)

[Gen AI [22](#gen-ai-1)](#gen-ai-1)

[Graph QL [22](#graph-ql)](#graph-ql)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT can be deployed in both CDF (Cognite Data Fusion) and Azure environment. The Azure environment provides a general-purpose cloud-based platform, and CDF is specialized for industrial data and applications. The environment is selected depending on client requirements.

The deployment in Azure environment assumes an existing Azure subscription and Azure DevOps organization with appropriate roles. Key initial steps include creating an Azure pipeline using an existing YAML file, cloning the repository from Git (with URLs provided by the AOT product team), and creating a resource group within the Azure portal for deployment.

## Purpose

This document explains how the Azure variant of AOT application can be deployed in a client environment.

## Target Audience

Developers/Azure resources with the following skills:

-   Azure DevOps

-   Microsoft Azure

-   Microsoft Entra ID

-   SonarQube

## Contact

-   

-   [rekha.a.srinivas@accenture.com]\{.underline\}

## Related Links

-   [AOT Architecture and Deployment](https://industryxdevhub.accenture.com/assetdetails/53)

-   [How to Create a Release Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops)

-   [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/64)

-   [People Management Backend Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/64)

##  Glossary

  -----------------------------------------------------------------------
  **Term**    **Definition**
  ----------- -----------------------------------------------------------
  AAD         Azure Active Directory

  ACR         Azure Container Registry

  AKS         Azure Kubernetes Service

  APIM        Azure API Management

  Azure AD    Azure Active Directory

  ADT         Azure Digital Twin

  ADX         Azure Data Explorer

  ADF         Azure Data Factory

  DNS         Domain Name System

  IA          Intelligent Advisor

  NSG         Network Security Group

  OH          Operation Hierarchy

  PM          People Management

  RG          Resource Group

  SKPI        Smart KPI

  SKU         Stock Keeping Unit

  DLQ         Dead letter queue

  SASL        Simple Authentication and Security Layer

  DB          Database

  MS          Micro Service

  VNet        Virtual Network

  ARM         Azure Resource Manager
  -----------------------------------------------------------------------

# Deployment Prerequisites

Assuming Azure subscription is already in place and an Azure DevOps organization is already in place with necessary roles provided to perform the deployment.

## Create Azure Pipeline

An Azure pipeline needs to be created using the existent YAML file. The steps to create the Azure pipeline are as follows.

-   

-   In DevOps, select Pipelines.

-   Click on New Pipeline.

-   In Connect, select Azure Repos Git.

-   Select the repository in which the new pipeline needs to be created.

-   In Configure section, select the Existing Azure Pipelines YAML file path.

-   Then select the branch and path of the Existing Azure Pipelines YAML file path and click on Continue.

-   Click on save.

-   Finally, click on the three dots on the right and rename the pipeline accordingly.

## Clone Repository

Clone the repository from Git. Connect with the AOT product team for the Git URL.

## Azure

-   



-   Resource Group Creation: Create a Resource Group in the Azure portal, where the required resources need to be deployed.

-   Register the App: Create an app registration and record its client ID.

-   Generate a Client Secret: Create a client secret for the app registration.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ![Screenshot of interface showing options and fields for creating a resource group.](media/image2.png)\{width="7.847201443569554in" height="4.462497812773403in"\}   ![A screenshot of a computer Description automatically generated](media/image3.png)\{width="6.872023184601924in" height="6.040972222222222in"\}
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Service Principal Configuration

Set up the app registration/Service Principal to facilitate the authentication of users to the standalone UI components using the following parameters and configurations:

1.  Application ID

2.  Tenant ID

3.  Secret

4.  Single page application URLs. Please note if the URLs of the config apps are changed to custom domains, they will have to be added here.

    a.  \/auth e.g., https://app-aot-azure-api-hostapp-\.azurewebsites.net/auth

    b.  \ e.g., https://app-aot-azure-api-hostapp-\.azurewebsites.net/

    c.  \ e.g., https://app-aot-azure-ui-header-micro-app-prod.azurewebsites.net/auth

    d.  \/home/dashboard e.g., https://aot-azure.accenturedigitalplant.com/home/dashboard

    e.  \/auth e.g., https://app-aot-azure-ui-3d-builder-\.azurewebsites.net/auth

    f.  \/auth e.g., https://app-aot-azure-ui-oh-entity-viewer-template-upload-\.azurewebsites.net/auth

    g.  \/ e.g., https://app-aot-azure-ui-3d-builder-\.azurewebsites.net/

    h.  \/auth e.g., https://app-aot-azure-ui-intelligent-advisor-config-microapp-\.azurewebsites.net/auth

    i.  \/auth e.g., https://app-aot-azure-ui-peoplemanagementconfig-\.azurewebsites.net/auth

    j.  \.azurewebsites.net/auth

    k.  \.azurewebsites.net/

    l.  \.azurewebsites.net/

    m.  \ e.g., https://app-aot-azure-ui-expert-knowledge-validator-\.azurewebsites.net/

5.  API Permissions (Microsoft Graph Delegated Permissions) as per the table below.

  -------------------------------------------------------------------------------
  Group.Read.All       Delegated        Read all groups                  Yes
  -------------------- ---------------- -------------------------------- --------
  User.Read            Delegated        Sign in and read user profiles   No

  User.Read.All        Delegated        Read all users\' full profiles   Yes
  -------------------------------------------------------------------------------

6.  Expose API. Use the screenshot below as a reference.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image4.png)\{width="4.56424978127734in" height="3.119047462817148in"\}

# 

## Create ARM Service Connection

-   

-   Set Up ARM Service Connection: In the DevOps portal, manually create an ARM service connection using the previously noted client ID and client secret.

-   Assign the Owner access to the recently created App registration on the Azure resource group created earlier.

-   After following these steps, the validation is successful.

![New Azure service connection window and options](media/image5.png)\{width="4.908070866141732in" height="6.607074584426947in"\}

# 

# Infrastructure Deployment

## Deployment Steps

These are the standard deployment steps followed to deploy various AOT components in the Azure environment:

1.  Navigate to the respective YAML file.

2.  Create and update the infrastructure variable group. For the variables,

    refer to [AOT_Azure_Deployment_Variables.xlsx](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20Azure%20Deployment%20Guide/AOT_Azure_Deployment_Variables.xlsx?d=w17335dc8b01c46cda1bc43736ca7124b&csf=1&web=1&e=PX2gi3).

3.  Add the infrastructure variable group name to the YML file.

4.  Rename the client files based on the client.

5.  Use the YML file to set up the Azure DevOps pipeline.

## Deployment Details

The following table provides the pipeline details, the YML file, and any additional information or steps required in addition to the standard deployment procedure described in the previous section.


| Resource | Pre-deployment | Azure Pipeline YAML File Path | Post-deployment |
| --- | --- | --- | --- |
| AKS Cluster and ACR | Ensure that the Kubernetes version is updated to 1.30.0 or later. | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> AKS Creation | > Create an AKS Namespace and use the same for secret creation and image tag. |
|  |  |  | > |
|  |  |  | > After AKS and ACR have been set up, create the Service connections as shown in [here](https://ts.accenture.com/:i:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20Azure%20Deployment%20Guide/AKS_ACR_Service_Connections.png). |
|  |  |  | > |
|  |  |  | > Create the username and password, take the Login server and add it in Docker Registry and add the username as Docker ID and password as Docker Password in DevOps. |
| APIM | Ensure that APIM Subnet has a range in AKS VNet that doesn\'t overlap with the existing AKS SubNet. | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> APIM Creation | A CORS policy must be attached to APIM. Refer [CORS (APIM)](#cors-apim) section for more information. |
| Event Hub |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> Event Hub Creation |  |
| Cosmos DB |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> CosmosDB-Creation | Ensure that VNet is attached to Cosmos DB. |
| Pub-Sub |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\>Webpubsub-Creation |  |
| SQL Server and DB |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> SQLServer-Creation | Ensure that VNet is attached to SQL Server |
| Storage Account |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> StorageAccount-Creation | CORS must be updated in the 3d storage account. Refer [CORS (Storage Account)](#cors-storage-account) section for more information. |
|  |  |  | Provide storage blob data contributor access to the app registration. |
| ADX Resource and Table Creation |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> ADX-Resource Table creation | Provide the Service principal user role on ADX |
| ADF |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> ADF-Resource-Creation |  |
| Azure Digital Twin |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> DigitalTwin-Creation |  |
| ADT-Models |  | Processing/Middleware_IaC/\-infrastructure-azure-pipelines.yml \>\> DigitalTwinModel-Creation |  |
| Open AI Service |  | Processing/Middleware_IaC/Middleware-IAC-arm-templates/application-deployment/\-azure-app-deployment-pipelines-ai-services.yaml |  |


### 

### 

### Create AKS Service Connection

1.  In DevOps portal, under Project Settings select Service Connections.

2.  Click on New Service connection.

3.  Choose a service or connection type as Kubernetes.

4.  Select the Authentication method as KubeConfig.

5.  To Connect to the cluster, login to the Azure portal, navigate to the respective AKS cluster and click on connect. Run the commands in the command prompt to get the KubeConfig file.

6.  Copy and paste the contents of your KubeConfig file which we get when connected to the AKS cluster.

7.  Next select the name of the AKS cluster and click on verify.

8.  Once the verification is completed, provide the name of the service connection.

9.  Click on the checkbox to Grant access permission to all pipelines and then click on verify and save.

> ![](media/image6.png)\{width="5.037267060367454in" height="7.714285870516186in"\}\
> **\
> Create ACR Service Connection**

1.  In DevOps portal, Under Project settings select the service connections.

2.  Click on New Service connection.

3.  Choose a service or connection type as Docker Registry.

4.  Select the Registry type as Others.

5.  Login to Azure portal, navigate to the respective resource group and select the container registry and navigate to the Access keys. Enable the access keys if they are not yet enabled.

6.  Provide the name of the service connection.

7.  Click on the checkbox to Grant access permission to all pipelines and then click on verify and save.\
    \
    ![A screenshot of a login form AI-generated content may be incorrect.](media/image7.png)\{width="5.666666666666667in" height="8.140598206474191in"\}

# Data Ingestion

These are the standard deployment steps followed to deploy various AOT components in the Azure environment:

1.  Navigate to the respective pipeline and YAML file path.

2.  Add the Infrastructure and Global variable group names to the YML file. For the variables,

    refer to [AOT_Azure_Deployment_Variables.xlsx](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20Azure%20Deployment%20Guide/AOT_Azure_Deployment_Variables.xlsx?d=w17335dc8b01c46cda1bc43736ca7124b&csf=1&web=1&e=PX2gi3).

3.  Rename the client files based on the client.

4.  Use the YML file to set up the Azure DevOps pipeline.

> ![](media/image8.png)\{width="5.593803587051618in" height="0.8062489063867017in"\}


| Resource | Azure Pipeline YAML File Path | Post-deployment |
| --- | --- | --- |
| Parameter Metadata Function App | Ingestion/pipelines/ParametermetadataFunctionApp/application-deployment/\-azure-app-deployment-pipelines.yaml | Update the Global variable group with function app keys. |
| IoT Hub Simulator | Source/Device/pipelines/\-azure-app-deployment-pipelines.yml | For updating the Client secret in the Key vault refer to [Key Vault Configurations](#key-vault-configurations). |
|  | Resources deployed as part of IOT HUB Simulator: |  |
|  | > IOT HUB |  |
|  | > |  |
|  | > Azure IoT Hub Device Provisioning Service (DPS) |  |
|  | > |  |
|  | > Key Vault |  |
|  | > |  |
|  | > App service Plan |  |
|  | > |  |
|  | > App service |  |
|  | > |  |
|  | > Smart Device Simulator |  |
|  | > |  |
|  | > IOTHub Consumer Group |  |
|  | > |  |
|  | > Function App |  |
| Azure Stream Analytics | Ingestion/AzureStreamAnalytics/sa-parameters-event/pipeline/application-deployment/\-azure-app-deployment-pipelines.yaml |  |
| ND-JSON Converter Function App | Ingestion/pipelines/NDJsonFunctionApp/application-deployment/\-azure-app-deployment-pipelines.yaml. | Update the Global variable group with function app keys. |
| Asset Hierarchy Function App | Ingestion/AzureAssetHierarchy/pipeline/AssetHierarchyFunctionApp/application-deployment /\-azure-app-deployment-pipelines. yaml | Update the Global variable group with function app keys. |
| ADF Pipeline | Ingestion/AzureAssetHierarchy/ADF_Pipeline/application-deployment/\-azure-app-deployment-pipelines. yaml | Provide the Access policy for the ADF in the key vault to get the secrets. |


Note that for the IoT Hub Simulator, both build and release pipelines must be run. The release pipeline deployment steps are as follows:

1.  In the Azure DevOps portal, navigate to Azure pipelines \> Releases.

2.  Select the corresponding release pipeline

3.  Select \"Create a release\". The release pipeline is now triggered to run. An example is shown in the alongside image.

> ![](media/image9.png)\{width="8.725097331583552in" height="2.778050087489064in"\}

4.  

5.  When creating a new release pipeline/cloning the release pipeline, add and update all the tasks and include the service connection details inside all tasks.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image10.png)\{width="13.25867782152231in" height="5.815612423447069in"\}

# 

# Backend Deployment

**Prerequisites:**

In the Azure DevOps portal, create:

-   Infrastructure pipelines must be deployed.

-   A service connection for Docker Registry as described in the previous section.

-   A service connection for AKS, as described in the previous section.

-   Some components may require APIM Integration, make sure that the APIM integration stage is included in the template files as shown in the [APIM section](#apim).

-   Global variable groups should be completely updated.

## Application Deployment

This section describes the process for deployment of the following applications:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Component**                               **Component Description**
  ------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  AzureWebPubSub Component                    This API is used to publish content updates like publish/subscribe messages in real time between server and connected clients (for example, a single page web application) in real-time. Clients can be a list of users, groups, or all users as well.

  People Management Configuration Component   AOT\'s People Management functionality can be integrated with other AOT components such as Smart KPIs and Intelligent Advisor. The integration requires personal data like role and department to be fetched from Azure and displayed in AOT. To accomplish this objective, People Management APIs must be deployed in the backend.

  File Handler Component                      The File Handler microservice is used to upload a template file and store it in an Azure Blob storage account. It can also be used to download one or more files as a zip file from the Azure Blob Storage.

  Operations Hierarchy Component              These are APIs used to propagate Data Permissions to Asset Hierarchy.

  MultiPlantView Component                    MultiPlantView Microservice can be used to retrieve units of measurement details and conversion formulae between various units of measurements

  Production Manager                          Production Manager Service is a flask application with Kafka consumer and producer running simultaneously. The Consumer is linked to the event hub to consumer events and push to cosmos database to create/update machine status for Event-based KPIs and simultaneously send messages to event hub via producer for further computations. The API in the service is to get data from the Cosmos database as required.

  Smart KPIs Component                        These are the APIs used for the SmartKPI Dashboard.

  Generic Scheduler Component                 A microservice that schedules jobs based on a given frequency to perform KPI calculations or to generate insights.

  IA Component                                An IA application is a micro-frontend application, and every micro-frontend IA application has a separate microservice for obtaining or updating insights or actions from Azure.

  Function App                                The Function App is a Blob trigger application. When the Insight_Factory_Category.xlsx is uploaded to the ia-samples-workitems blob storage, the IA Function Microservice API for insight category creation is called. Similarly for Gen AI things it would be stored in the \"aot-genai-files\" container is uploaded to graphql_queries blob storage.

  3D CMS Component                            The 3D Content Management System (CMS) is used in AOT\'s Twin Builder and Twin Viewer applications.

  PowerBI Component                           This is the independent Power BI Microservice that allows connecting to and publishing Power BI reports.

  Gen AI Component                            This is the Independent Microservice to engage the AI services into Application.

  GraphQl Component                           This component APIs let users query the exact data they need through a single endpoint used for Chatbot service.

  Expert Knowledge Component                  This is the Independent Microservice which is used to connect with GenAI Service
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 

### Deployment Steps

1.  Navigate to the respective Azure pipeline YAML file path for the application.

2.  Create and add the variable group (s) in the Azure DevOps portal with the corresponding values listed in [AOT_Azure_Deployment_Variables.xlsx](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20Azure%20Deployment%20Guide/AOT_Azure_Deployment_Variables.xlsx?d=w17335dc8b01c46cda1bc43736ca7124b&csf=1&web=1&e=PX2gi3) to the YAML file.

3.  Set up the Azure DevOps pipeline with the above YML file.

4.  The variable groups used in the YML file of Azure DevOps Pipeline are categorized as below:

    a.  **Infrastructure Variable Group**: All the infrastructure-related values are included in this variable group.

    b.  **Global Variable Group**: The values that are commonly used across all components are included in this variable group.

    c.  **Component-Specific Variable Group(s)**: The values that are specific to the component either BE or FE are included in this variable group.

> The complete list of the variables is below.


| PROD-AOT-AZURE-PM-BE-VARIABLE |
| --- |
| PROD-AOT-AZURE-OH-BE-VARIABLE |
| PROD-AOT-AZURE-SKPI-BEVARIABLE |
| PROD-AOT-AZURE-IA-BE-VARIABLE |
| PROD-AOT-AZURE-UOM-BE-VARIABLE |
| PROD-AOT-AZURE-FILE-HANDLER-BEVARIABLE |
| PROD-AOT-AZURE-PRM-BE-VARIABLE |
| PROD-AOT-AZURE-GS-VARIABLE |
| PROD-AOT-AZURE-POWERBI-VARIABLE |
| PROD-AOT-AZURE-3D-BE-VARIABLE |


> Refer to this example in the image below for the alignment of the variables.
>
> ![A close-up of text AI-generated content may be incorrect.](media/image11.png)\{width="6.293616579177603in" height="1.2815069991251093in"\}

### 

### Component Level Details

This section describes the APIs for each application, their pipeline details, the YML files and respective selection.

#### PM and OH

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Sub-component                               Prerequisites                                                                                                                                                                   Services                                                                                                                           Azure Pipeline YAML File Path
  ------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Azure WebPubSub Component                   Infrastructure pipelines must be deployed.                                                                                                                                      AzureWebPubSub                                                                                                                     Consumption/DataAccess/\-pm-azure-pipelines.yml \>\> Azure WebPubSub MS

  People Management Configuration Component   Azure WebPubSub Microservice must be deployed. Update the Client ID in the SQL script to include a to-be admin user from the client environment.                                PeopleManagement_ms                                                                                                                Consumption/DataAccess/\-pm-azure-pipelines.yml \>\> PM Config MS

  Operations Hierarchy Component              PM pipeline must be deployed and OperationHierarchy_configuration and OperationHierarchy_DataPermissions microservices must be deployed. and Asset Hierarchy must be created.   OperationHierarchy_EntityViewer, OperationHierarchy_configuration, OperationHierarchy_DataPermissions, OperationHierarchy_module   Consumption/DataAccess/\-pm-azure-pipelines.yml \>\> OH Entity Viewer MS, Consumption/DataAccess/\-pm-azure-pipelines.yml \>\> OH Config MS, Consumption/DataAccess/\-pm-azure-pipelines.yml \>\> OH DP MS, Consumption/DataAccess/\-pm-azure-pipelines.yml \>\> OH Module MS
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Independent

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Sub-component                  Prerequisites                                                                            Services             Azure Pipeline YAML File Path
  ------------------------------ ---------------------------------------------------------------------------------------- -------------------- ------------------------------------------------------------------------
  File Handler Component         N/A                                                                                      FileHandler          Common/\-azure-pipelines.yml \>\> File Handler MS

  3D CMS Component               N/A                                                                                      aot-3d-cms           Common/\-azure-pipelines.yml \>\> 3D CMS

  Power BI Component             N/A                                                                                      PowerBi              Common/\-azure-pipelines.yml \>\> Power BI MS

  Production Manager Component   N/A                                                                                      Production Manager   Common/\-azure-pipelines.yml \>\> Production Manager

  Generic Scheduler Component    This pipeline must be deployed before SKPI Pipelines                                     GenericScheduler     Common/\-azure-pipelines.yml \>\> Generic Scheduler MS

  Unit of Measurement            This Pipeline must be deployed before SKPI orchestrator and Data Permission pipelines.   N/A                  Common/\-azure-pipelines.yml \>\> Unit of Measurement MS
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Smart KPI

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Sub-component          Prerequisites                                                  Services                                                                                                                                            Azure Pipeline YAML File Path
  ---------------------- -------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Smart KPIs Component   Ensure that People Management Microservice must be deployed.   smartkpiconfig_ms, smartkpi_ms, smartkpi_svc_kpi_datapermission_change, smartkpi_svc_kpi_orchestrator_svc, smartkpi_svc_kpi_computationengine_svc   Processing/SmartKPIs/\-skpi-azure-pipelines.yml \>\> SmartKPI Config MS, Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> SmartKPI MS, Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> SmartKPI Datapermission SVC MS, Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> SmartKPI Orchestrator SVC MS, Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> SmartKPI Computation MS

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### Intelligent Advisor


| Sub-component | Prerequisites | Services | Azure Pipeline YAML File Path |
| --- | --- | --- | --- |
| Intelligent Advisor | Generic Schedular should be deployed. | Ia_func_ms | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA FUNC MS |
|  |  | Ia_func_excelfileupload | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Excel File Upload |
|  |  | Ia_func_db_update_functionapp | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA DB Update Function App |
|  |  | Ia_model_ms | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Model MS |
|  |  | ia_mw_ms | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Middleware MS |
|  |  | ia_evaluatemodel_ms | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Evaluate MS |
|  |  | ia_awo | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Action WorkOrder MS |
|  |  | Ia_svc(ia_kpi_roleupdate) | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA KPI Role update MS |
|  |  | ia_config_ms | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Config MS |
|  |  | ia_wo | Processing/IntelligentAdvisor/\-ia-azure-pipelines.yml \>\> IA Workorder MS |


#### GraphQL

  ----------------------------------------------------------------------------------------------------------------------------
  Sub-component       Prerequisites    Services      Azure Pipeline YAML File Path
  ------------------- ---------------- ------------- -------------------------------------------------------------------------
  GraphQL Component   NA               graphql       AOT-Graphql/ \ix-graphql-mesh-gateway-cicd-pipeline. yaml

  ----------------------------------------------------------------------------------------------------------------------------

#### Gen AI

  ------------------------------------------------------------------------------------------------------------------------------------------------------
  Sub-component   Prerequisites        Services      Azure Pipeline YAML File Path
  --------------- -------------------- ------------- ---------------------------------------------------------------------------------------------------
  GenAI           Gen AI Deployement   GenAI         Consumption/DataAccess/GenAI/GenAIQueryAPI/genai_middleware/genai_ms/pipeline/azure-pipelines.yml

  ------------------------------------------------------------------------------------------------------------------------------------------------------

#### Expert Knowledge

  ----------------------------------------------------------------------------------------------------------------------
  Sub-component      Prerequisites    Services          Azure Pipeline YAML File Path
  ------------------ ---------------- ----------------- ----------------------------------------------------------------
  Expert Knowledge   NA               ExpertKnowledge   Ingestion/GenAI/ExpertKnowledge/pipeline / azure-pipelines.yml

  ----------------------------------------------------------------------------------------------------------------------

### 

# 

# UI Artifacts 

Artifacts must be created before deploying the UI components.

**Deployment Steps**

1.  Navigate to Artifacts Tab and create a new feed. ex: test-feed

2.  Depending on the artifact you want to deploy, clone an existing pipeline that deploys the same artifact in another environment.

3.  In the npm publish Task of the cloned pipeline

-   Select Choose \"Registry I select here\".

-   Make sure to update the registry information in the \'npm publish\'

4.  If a UI app contains. npmrc file, please make sure to update the path that according to the new feed.

5.  You can get the contents of .npmrc file when you connect to the feed by choosing \"Connect to feed\" and then \"npm\" as the package manager.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image12.png)\{width="11.963737970253717in" height="2.7391907261592303in"\}

  --------------------------------------------------------------------------------------------------------------------------------------
  **Component**                  **Azure Pipeline File Path**
  ------------------------------ -------------------------------------------------------------------------------------------------------
  Hostapp Widget Demo            Consumption/UI/Common/Components/Angular/angular-reusable-components \>\> host-app-widgets

  Asset Hierarchy Widgets Demo   Consumption/UI/Common/Components/Angular/angular-reusable-components/projects/asset-hierarchy-widgets

  Smart KPI Widgets Demo         Consumption/UI/Common/Components/Angular/angular-reusable-components \>\> smart-kpis-widgets

  Template Viewer Widgets Demo   Consumption/UI/Common/Components/Angular/angular-reusable-components \>\> template-viewer-widgets
  --------------------------------------------------------------------------------------------------------------------------------------

![A screenshot of a computer AI-generated content may be incorrect.](media/image13.png)\{width="4.559218066491688in" height="7.101534339457568in"\}

# 

# UI Deployment

-   As a prerequisite, the widgets must be deployed.

-   All UI components are found under the following Repository structure: Consumption/UI.


| UI Component | Description |
| --- | --- |
| 2D SVG Builder | 2D SVG Builder is an independent React application where users can upload SVG files exported from Figma. Users can configure the 2D schematics by linking files and mapping assets. |
| Twin Builder UI | Twin Builder UI is an independent React Application for 3D CMS and Unity builder app. |
| Twin Viewer UI | Twin Viewer UI is a Micro-frontend app for Unity visualizer and has integrated the Twin Viewer app into the Host App. |
| MAP MFE UI | Map MFE is a 2D/3D globe visualization micro-frontend application that has been integrated into the host application. |
| SVG Viewer MFE | This is a mfe which can be used to view the configured SVGs and view KPI count, color details and its data. |
| Component-configuration-micro-app | This is a Micro-frontend app. It is a type of navigation component. Using this, the user can see the applications that are accessible to them. The user can also navigate to the applications by clicking on them. |
| Header-micro-app (Header and Menu) | This is the header micro frontend app that has tabs based on user permissions and helps the user to switch between applications. |
| Intelligent-advisor-config-app | This is the micro frontend application used for creating a KPI and predictive failure insight. |
| Intelligent-advisor-micro-app | This pipeline deploys the following IA components: |
|  | - Insight generation engine |
|  | - Collaboration |
|  | - Actions |
|  | - Advisor panel |
|  | - Insight Viewer template |
|  | - Insight lifecycle management |
| Intelligent-advisor-template-viewer-micro-ap | This app displays insights information based on the details specified in the corresponding specific template. |
|  | Get the required custom npm package before building the application. |
|  | \"@aot/smart-kpis-widgets\": \"\^0.4.1\", |
|  | \"@aot/template-viewer-widgets\": \"0.0.3\", |
| Operations-Hierarchy-entity-viewer-micro-app | With this app, an end user can configure the Entity Viewer through the template and visualize the 360-degree information on the UI. |
| Operation-Hierarchy-entity-viewer-template-upload-micro-app | This app is used for the OH Entity Viewer Template Upload Config UI, which is used for preconfiguring data for assets that are viewed as part of Entity Viewer UI. It also performs various operations like uploading the template, downloading the latest available template, and viewing the information associated with the uploaded templates. |
| Operations-Hierarchy-micro-app | Operations Hierarchy is a component of AOT that helps the user to navigate through the plant\'s hierarchy and view 360-degree information associated with each node (Entity). |
| People Management UI | People Management Configuration is part of the PM module that focuses on the management of Departments, Roles, and Users. |
| Reports-micro-app | The Reports MFE is one of the AOT components that will enable different types of users - from shop floor workers to top management - to view Reports and analyze the parameters through real-time generated data, allowing the user to conduct an RCA and collaborate to resolve the problem. |
| Smart-kpi-config | This is a separate application used to configure the KPIs. |
| Smart-kpis-micro-app | Smart-kpis-micro-app is a micro-frontend application that is the landing page of the AOT application. It helps to track performance in the form of KPIs. Get the required custom npm package before building the application. \"@aot/smart-kpis-widgets\": \"\^0.6.6\" |
| Expert Knowledge Validator | This app is used to validate (approve ,reject) expert knowledge submitted by the experts |
| HostApps | HostApp is the host application that is the container to host all other Micro-frontend apps. |


## 

## Deployment Steps

1.  Navigate to the corresponding pipeline for the UI component.

2.  Create and add the variable group (s) in the Azure DevOps portal with the corresponding values listed in [AOT_Azure_Deployment_Variables.xlsx](https://ts.accenture.com/:x:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20Azure%20Deployment%20Guide/AOT_Azure_Deployment_Variables.xlsx?d=w17335dc8b01c46cda1bc43736ca7124b&csf=1&web=1&e=PX2gi3) to the YAML file.

3.  Open the YML file that is in the specified format for the UI component.

4.  The variable groups used in the YML file of Azure DevOps Pipeline are categorized as below:

    a.  Infrastructure Variable Group: All the infrastructure-related values are included in this variable group.

    b.  Global Variable Group: The values that are commonly used across all components are included in this variable group.

    c.  Component-Specific Variable Group: The values that are specific to the component either BE or FE

        are included in this variable group.

        The full list of the variables is as follows.

-   PROD-AOT-AZURE-PM-FE-VARIABLE

-   PROD-AOT-AZURE-OH-FE-VARIABLE

-   PROD-AOT-AZURE-SKPI-FE-VARIABLE

-   PROD-AOT-AZURE-IA-FE-VARIABLE

-   PROD-AOT-AZURE-HOSTAPP-VARIABLE

    PROD-AOT-AZURE-3D-FE-VARIABLE

    Refer to the image below to note the alignment of the variables.

> ![A close-up of words AI-generated content may be incorrect.](media/image14.png)\{width="7.284981408573929in" height="1.1047364391951007in"\}

5.  Enable CORS for the app service as needed. We need to add respective origin URLs as shown in the [CORS section](#corsapp-services).

## 

## 

## UI Components

This section provides the Azure Pipeline YAML file path and the CORs URL for each component.

### Frontend Component

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **UI Sub-Component**   **Azure Pipeline YAML File Path**                                             **CORS -- origin**
  ---------------------- ----------------------------------------------------------------------------- --------------------------------------------------------------------
  2D SVG Builder         Consumption/UI/\-3d-ui-azure-pipelines.yml \>\> 2D SVG MFE      E.g., 

  3D Visualizer          Consumption/UI/\-3d-ui-azure-pipelines.yml \>\> 3D Visualizer   N/A

  MAP MFE UI             Consumption/UI/\-3d-ui-azure-pipelines.yml \>\> MAP MFE        E.g., 
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### 2D and 3D Component

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **UI Sub-Component**   **Azure Pipeline YAML File Path**                                                                                          **CORS -- origin**
  ---------------------- -------------------------------------------------------------------------------------------------------------------------- -----------------------------------------------------
  2D Builder             Consumption/UI/\-configurator-ui-azure-pipelines.yml \>\> 2D Builder                                         N/A

  3D Builder             Consumption/UI/\-configurator-ui-azure-pipelines.yml \>\> 3D Builder                                         N/A

  SVG Viewer MFE         Consumption/UI/svg-mfe/svg-iac/Application-deployment/\-azure-app-deployment-pipelines.yml                   E.g., 

  Twin Viewer UI         Consumption/UI/3D-Visualizer/3D-Visualizer-iac/Application-deployment/\-azure-app-deployment-pipelines.yml   E.g., 
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Host App Configurator


| **UI Sub-Component** | **Azure Pipeline YAML File Path** | **CORS -- origin** |
| --- | --- | --- |
| Component-configuration-micro-app | Consumption/UI/\-hostapp-ui-azure-pipelines.yml \>\> Component Configuration | E.g., |
| Header-micro-app (Header and Menu) | Consumption/UI/\-hostapp-ui-azure-pipelines.yml \>\> Header MicroApp | E.g., |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
|  |  | > |
| Reports-micro-app | Consumption/UI/\-hostapp-ui-azure-pipelines.yml \>\> Reports Microapp | E.g., |
| expert-knowledge-validator-config-app | Consumption/UI/expert-knowledge-validator-config-app/expert-knowledge-validator-iac/expert-knowledge-validator-arm-templates/application-deployment/\-azure-app-deployment-pipelines.yml | E.g., |
| HostApp | Consumption/UI/\-hostapp-ui-azure-pipelines.yml \>\> Hostapp | N/A |


### Intelligent Advisor Frontend Component

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **UI Sub-Component**                            **Azure Pipeline YAML File Path**                                                  **CORS -- origin**
  ----------------------------------------------- ---------------------------------------------------------------------------------- -----------------------------------------------------
  Intelligent-advisor-config-app                  Consumption/UI/\-ia-ui-azure-pipelines.yml \>\> IA Config            N/A

  Intelligent-advisor-micro-app                   Consumption/UI/\-ia-ui-azure-pipelines.yml \>\> IA Microapp          E.g., 

  Intelligent-advisor-template-viewer-micro-app   Consumption/UI/\-ia-ui-azure-pipelines.yml \>\> IA Template Viewer   E.g., 
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### OH and PM Frontend Component

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **UI Sub-Component**                                          **Azure Pipeline YAML File Path**                                                                **CORS -- origin**
  ------------------------------------------------------------- ------------------------------------------------------------------------------------------------ ---------------------------------------------------
  Operations-Hierarchy-entity-viewer-micro-app                  Consumption/UI/\-pm-ui-azure-pipelines.yml \>\> OH Entity Viewer                   E.g., https://aot-azure.accenturedigitalplant.com

  Operation-Hierarchy-entity-viewer-template-upload-micro-app   Consumption/UI/\-pm-ui-azure-pipelines.yml \>\> OH Entity Viewer Template Upload   N/A

  Operations-Hierarchy-micro-app                                Consumption/UI/\-pm-ui-azure-pipelines.yml \>\> OH Microapp                        E.g., https://aot-azure.accenturedigitalplant.com

  People Management UI                                          Consumption/UI/\-pm-ui-azure-pipelines.yml \>\> PM Config                          N/A
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### SmartKPI Frontend Component

  ----------------------------------------------------------------------------------------------------------------------------------------------------------
  **UI Sub-Component**   **Azure Pipeline YAML File Path**                                               **CORS -- origin**
  ---------------------- ------------------------------------------------------------------------------- ---------------------------------------------------
  Smart-kpi-config       Consumption/UI/\-skpi-ui-azure-pipelines.yml \>\> SKPI Config     N/A

  Smart-kpis-micro-app   Consumption/UI/\-skpi-ui-azure-pipelines.yml \>\> SKPI MIcroapp   E.g., https://aot-azure.accenturedigitalplant.com
  ----------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Other Configurations

## CORS(App Services)

CORS must be updated in all app services.

-   Go to Resource group \>App service\> API\>CORS.

-   Add specific origin URLS as shown in the image

-   Space must not be present before and after the origin URLs.

![A screenshot of a computer AI-generated content may be incorrect.](media/image15.png)\{width="12.867036307961504in" height="4.091614173228346in"\}

## 

## **CORS (APIM**)

CORS must also be updated at the APIM level.

-   Navigate to Resource Group \> APIM \>APIS\>All APIs

-   In \"All APIs\", go to Inbound processing.

-   From the three-dot menu, click \"Code editor\".

-   Add corresponding [CORS policy script](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT%20Azure%20Deployment%20Guide/AOT_Azure_APIM_CORS_Policy_Script.txt) to the Code editor and save it.

![A screenshot of a computer AI-generated content may be incorrect.](media/image16.png)\{width="12.994613954505686in" height="5.874939851268591in"\}

## 

## CORS (Storage Account)

-   CORS must be added to the 3D storage account.



-   Go to the Resource group\>3d Storage account \>Resource Sharing (CORS).

-   Add specific origin URLS as shown in the image.

-   Space must not be present before and after the origin URLs.

![](media/image17.png)\{width="12.95880358705162in" height="5.00128937007874in"\}

## APIM

Some microservices require APIM Integration. Ensure that the stage for doing this is present in the main YAML file.

> ![A screenshot of a computer AI-generated content may be incorrect.](media/image18.png)\{width="12.978277559055119in" height="5.93205271216098in"\}

## NSG

An NSG must be attached to the Subnet that is linked to AKS. The Port AKS uses to contact the event hub should be included. The Outbound and Inbound Rule assigned on the AKS node must also be assigned to the NSGs.

After the app is deployed, a custom URL can be mapped to the HostApp UI default URL if needed.

![A screenshot of a computer AI-generated content may be incorrect.](media/image19.png)\{width="17.09181430446194in" height="7.379323053368329in"\}

## 

## 

## Client Env 

In the client env, the system roles script which contains admin roles must be run to specify the user as the admin user, following which the user can add other users to the roles through the PM UI. The path to find the script is:

AOT\\MarilynVPlatform\\Consumption\\DataAccess\\PeopleManagement\\Configuration\\pm_config_middleware\\pm_config_db\\pm_insert_data_system_roles.sql

## HostApp Deployment

The applicationhost.xdt file must be added to the root folder manually by accessing the advanced tools in the app service during HostApp deployment in the wwwroot, which is a folder in the app service folder structure.

## AAD User Settings

Guest users have the same access as members (most inclusive) and the access must be enabled under user settings.

## Key Vault Configurations

The following table describes the key vault configuration for the simulator.


| \# | Step |
| --- | --- |
| 1 | Add the key vault name in the variable group used in the simulator release pipeline. |
| 2 | Once the simulator release is executed, the following are automatically added to the key vault: |
|  | ClientSecret |
|  | DPSConnectionString |
|  | SmartDevicesEnrollmentGroupKey |
|  | SmartDeviceSimulatorKey |
|  | IngestionIotHubConnectionString |
| 3 | Add the saskey of IoTHub in the above key vault. |


Note that the two endpoints have different saskey values. Use the service endpoint to get the required saskey.

# Interdependencies 

The deployment of some AOT components depends on the configuration of other AOT components. Those interdependencies are listed below.

## People Management

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **\#**   **Pipeline**                                   **Dependency**
  -------- ---------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------
  1        AOT-AzureWebpubsub-ms-Deployment               No Dependency

  2        AOT-People Management -IAC-DB & MS             AOT-AzureWebpubsub-ms-Deployment should run first and then the service URL of Azure Web PubSub API must be updated in the library.

  3        AOT-FileHandler-MS                             No Dependency

  4        AOT-OperationsHeirarchy-Config-IaC-MS          No Dependency

  6        AOT-OperationsHeirarchy-Module-IaC-MS          Depends on Asset Hierarchy (AH) creation and People Management component

  7        AOT-OperationHeirarchy-DataPermission-IaC-MS   Dependent on the People Management Component

  8        AOT-OperationHierarchy-EntityViewer-IaC-MS     No Dependency

  9        AOT-UnitOfMeasurement-Config-MS                No Dependency
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Production Manager

  -----------------------------------------------------------------------------------------
  **\#**   **Pipeline**                       **Dependency**
  -------- ---------------------------------- ---------------------------------------------
  1        AOT-Azure-Production-Manager-SVC   Dependent on Simulator

  -----------------------------------------------------------------------------------------

## SmartKPI

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **\#**   **Pipeline**                                 **Dependency**
  -------- -------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  1\.      AOT-Consumer-Smartkpis-datapermission-svc    Ensure that ports 10255,9093 are open for connections in the VNet. Contributor access for the MongoDB and Storage Blob container

  2\.      AOT-Middleware-SmartKPIConfig-ms             People Management APIs utilized by the SKPI to get the role configured for the specific plant details need to be already present, and AH needs to be created.

  3\.      AOT-Middleware-Smartkpis-ms                  People Management APIs utilized by the SKPI to get the role configured for the specific plant details need to be already present, and AH needs to be created.

  4\.      AOT-Azure-SmartKPI-ComputationEngineSVC-MS   Asset hierarchy from PM Dev Team

  5\.      AOT-Consumer-KPI-Orchestrator-svc            Ensure ports 10255 and 9093 are open for connections in the VNet. Ensure that contributor access for the MongoDB and Storage Blob container is provided.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Generic Scheduler

  -------------------------------------------------------------------------------
  **\#**   **Pipeline**            **Dependency**
  -------- ----------------------- ----------------------------------------------
  1        AOT-Generic-Scheduler   Smartkpi pipelines should run before this

  -------------------------------------------------------------------------------

## Intelligent -Advisor 

  -------------------------------------------------------------------------------------------------------------------------------------------------
   **\#**  **Pipeline**                                     **Dependency**
  -------- ------------------------------------------------ ---------------------------------------------------------------------------------------
     1     AOT-IA-Funct-APIM-MW                             26 Timeseries should be created by Smart KPIs Dev Team

     2     AOT-Azure-IAFunc-DbUpdate-FunctionApp-Creation   IA Function Database should be present.

     3     AOT-IA-MW-APIM-Deployment                        IA-Model, SQL DB server, Smartkpi API, Azure WebPubSub API, and People Management API

     4     AOT-Azure-IAFunction-ExcelFileUploadPipeline     Function ms, function app, and Middleware should be deployed.

     5     AOT-IA-Model-APIM-MW                             26 Timeseries should be created by Smart KPIs Dev Team

     6     AOT-IA-EvaluateModel-APIM                        Smartkpi API

     9     AOT-Consumer-IA-Kpi-roleupdate-svc               No dependency

     10    AOT-IA-SAP-MW                                    SAP instance

     11    AOT-IA-AWO-MS                                    Azure WebPubSub API and People Management API

     12    AOT-IA-Config-APIM                               SQL DB server
  -------------------------------------------------------------------------------------------------------------------------------------------------

##  3D 

  ------------------------------------------------------------------------
  **\#**    **Pipeline**                       **Dependency**
  --------- ---------------------------------- ---------------------------
  1         AOT-3D-CMS                         No Dependency

  ------------------------------------------------------------------------

## PowerBI

  ------------------------------------------------------------------------
  **\#**    **Pipeline**                       **Dependency**
  --------- ---------------------------------- ---------------------------
  1         AOT-PowerBI-MS                     No Dependency

  ------------------------------------------------------------------------

## Gen AI

  ------------------------------------------------------------------------
  **\#**    **Pipeline**                       **Dependency**
  --------- ---------------------------------- ---------------------------
  1         GENAI-Deployement                  No Dependency

  2         Gen-ai Function App                No Dependency
  ------------------------------------------------------------------------

## Graph QL

  ------------------------------------------------------------------------
  **\#**    **Pipeline**                       **Dependency**
  --------- ---------------------------------- ---------------------------
  1         AOT-Azure-Graphql                  No Dependency

  ------------------------------------------------------------------------

**Expert Knowledge**

  --------------------------------------------------------------------------
  **\#**    **Pipeline**                         **Dependency**
  --------- ------------------------------------ ---------------------------
  1         AOT-Azure-GenAI-ExpertKnowledge-MS   No Dependency

  --------------------------------------------------------------------------
