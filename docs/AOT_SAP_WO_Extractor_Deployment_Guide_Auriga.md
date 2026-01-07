---
id: aot-sap-wo-extractor-deployment-guide-auriga
title: AOT SAP WO Extractor Deployment Guide Auriga
---

**Accenture Operations Twin**

**SAP Work Order Extractor**

**DEPLOYMENT GUIDE**

Release Version:2.5

**Metadata Table**

| **Field** | **Value** |
|:---|:---|
| **Asset / Solution Name** | Accenture Operations Twin / Data Integration Accelerators |
| **Domain / Area** | Data Processing |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Joshi, Rishabh |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | AOT Extractors Architecture Blueprint, AOT Extractors Getting Started |

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#_Toc214351075)](#_Toc214351075)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Architecture Diagram [4](#architecture-diagram)](#architecture-diagram)

[SAP WO Configuration [5](#sap-wo-configuration)](#sap-wo-configuration)

[Function Module [5](#function-module)](#function-module)

[Creation [5](#creation)](#creation)

[Structures and Tables Creation [5](#structures-and-tables-creation)](#structures-and-tables-creation)

[Update [5](#update)](#update)

[Open Data Protocol [8](#open-data-protocol)](#open-data-protocol)

[Creation [8](#creation-1)](#creation-1)

[Transport and Package Creation [10](#transport-and-package-creation)](#transport-and-package-creation)

[Cloud Deployment [12](#cloud-deployment)](#cloud-deployment)

[Prerequisites [12](#prerequisites)](#prerequisites)

[Configure Azure DevOps [12](#configure-azure-devops)](#configure-azure-devops)

[Create a Build Pipeline [17](#create-a-build-pipeline)](#create-a-build-pipeline)

[Create a Release Pipeline [19](#create-a-release-pipeline)](#create-a-release-pipeline)

[On-Prem Deployment [25](#on-prem-deployment)](#on-prem-deployment)

[Prerequisites [25](#prerequisites-1)](#prerequisites-1)

[Install the Extractor [25](#install-the-extractor)](#install-the-extractor)

[Start the Extractor [28](#start-the-extractor)](#start-the-extractor)

[Stop the Extractor [29](#stop-the-extractor)](#stop-the-extractor)

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools – including extractors – that are assembled to deliver client solutions. AOT accelerates the integration of the product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT extractors are data integration accelerators that are developed to automate and ease the process of extracting data from enterprise source systems. After the data is extracted, it is processed and transformed into a format that Cognite recognizes. Finally, the processed and transformed data is pushed to CDF RAW.

The SAP Work Order (WO) Extractor gives users the power to send SAP work order data to CDF without having to manually run commands. Once the configuration file is built, the extractor can refer to the Root Functional Location, extract the work order details from SAP, and push that data to CDF RAW. Furthermore, the SAP WO extractor grants a user the flexibility to configure one or more source systems as well as the Cognite details that enable data extraction.

## Purpose

This document explains how to extract data from the source system and load it into CDF RAW. It also covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF. The objective is to obtain Work Order details from SAP and make them available as an OData service for the Python extractor to consume and store in Cognite Staging areas.

**Target Audience**

This guide is designed for use by developers with the following skills:

- Sonar Qube

- Cognite Data Fusion

- SAP

- Python

## Contacts

- ``

- ``

## Related Links

- [How to create OData Service](https://blogs.sap.com/2019/10/07/creation-of-odata-services-for-beginners/)

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| Term | Definition |
|----|----|
| Cognite Data Fusion | An industrial data platform that enables integration, contextualization, and visualization of data from multiple sources. |
| SAP | A global enterprise software company specializing in business operations and customer relations solutions. |
| Python | A high-level, interpreted programming language known for its simplicity and versatility in data analytics and automation. |
| OData | An open data protocol used for querying and updating data over the web, leveraging standard web technologies such as HTTP and AtomPub. |
| Function module | A reusable set of source code statements in SAP, designed to perform specific tasks with defined importing and exporting parameters. |
| Subprogram | A module containing reusable code statements, often used to structure and organize programming tasks within larger applications. |

# Architecture Diagram



# 

# SAP WO Configuration

Configuration of SAP WO includes three deployment tasks:

**Function module**

Subprograms that contain a set of reusable source code statements with importing and exporting parameters and exceptions.

**  
Open data protocol**

OData is a Web protocol for querying and updating data, applying, and building on Web technologies such as HTTP, Atom Publishing Protocol (AtomPub), and RSS (Really Simple Syndication) to provide access to information from a variety of applications.

**  
Transport and package**

An SAP Transport is a kind of ‘Container/Collection’ of changes that are made in the development system. It also records information regarding the type of change, the purpose of transport, the request category, and the target system.

## Function Module 

### Creation

1.  In SAP, use t-code “se37” to access the Function Builder.

2.  In the name field, enter the name of the function module, and then click Create.

3.  Choose the function group as `\<`ZCOGNITE`\>` and enter a short text description.

4.  Click Save.

### Structures and Tables Creation

1.  Enter t-code “se11”.

2.  Select the Data Type Radio button, enter a new name for the Structure, and click Create.

3.  Select the Structure Radio Button and press Enter.

4.  Enter a short description and add the required fields in the rows for the structure and their description.

5.  Click on *Save* and open t-code “se11” for table creation.

6.  Select the Data Type Radio button and enter a new name for Structure. Then, click Create.

7.  Select the Table Radio Button and press Enter.

8.  Enter a short description and select the Line Type radio button. Then, enter the name of the structure created.

9.  Now add details like Primary Key, Secondary Key, Attributes, etc., if needed, and click on Save.

### Update

1.  Use the t-code “se37” to access the function module.

2.  In the name field, enter the name of the function module that you have created, and then click the Change button.

3.  In the Tables tab, import the table created in the above step by clicking on the Insert Row button.

`\>` 

4.  

5.  Edit the source code to suit the use case.

`\>` 

6.  In the Import tab, enter any parameters (e.g., Root Functional Location) that are needed during the execution of the function module.

`\>` 

7.  

8.  Execute the function module using F8 or the button highlighted in the screenshot below.

`\>` 

9.  Enter the parameter and execute it using F8 or the button highlighted in the screenshot below.

`\>` 

## 

## Open Data Protocol 

### Creation

1.  Open the t-code “SEGW” and create a new project using the Create Project button.

`\>` 

2.  Create a new Entity type and Entity sets using the Import option \`\>` DDIC structure by right-clicking on the Data Model.

`\>` 

3.  Enter the name and the ABAP structure that was created during the creation of the function module.

`\>` 

4.  

5.  After creation, the screen is similar to as depicted in the image below.

`\>` 

6.  Use the red and white Generate Runtime Object button to launch the Model and Service Definition window.

`\>` *[Image: ]*

7.  Check for the successful creation of the service and model.

`\>` 

8.  Use the t-code “IWFND/MAINT_SERVICE” to activate and maintain the nodes.

`\>` 

## 

## Transport and Package Creation

A Workbench request and a package to carry the TADIR objects are required to transport any OData service.

1.  Use t-code “SE01” to open the Transport Organizer window, click on Create, and select Workbench Request.

`\>` *[Image: ]*

1.  Use the t-code “SE80” to create the package. Select the package from the dropdown list that is under the Repository Browser. To create a package, enter the package name and click on the **Display** icon.

`\>` 

2.  To capture all the details, add the new ZCDF package to the previous transport while creating the new package. Standard OData Service TADIR Objects are listed in the table below.

| **Short Description** | **Program ID** | **Object Type** | **Object Name** |
|----|----|----|----|
| Package | R3TR | DEVC | Z\*\*\*\_PKG |
| SAP Gateway: Model Metadata | R3TR | IWSG | Z`\<`Service Group`\>`_SRV_0001 |
| SAP Gateway: Service Groups Metadata | R3TR | IWOM | Z`\<`Service model name`\>`_MDL_0001_BE |
| ICF Service | R3TR | SICF | `\<`System ID`\>`******* |

3.  

4.  While creating the SEGW project, add everything to the workbench request. The final package is now created.

`\>` 

5.  Validate the final transport request once it is successfully created.

`\>` 

# 

# Cloud Deployment

Two pipelines are needed to deploy the extractor to an AKS Cluster. This section includes step-by-step guidance for:

- Prerequisites that need to be fulfilled before the extractor can be deployed and used.

- Setting up the Azure DevOps environment.

- Creating a Build Pipeline for Dockerizing the Extractor Package.

- Creating a Release Pipeline for deploying the Docker image to the AKS cluster.

- Validating the data in the RAW table in CDF RAW.

## Prerequisites 

- 

- [Lens](https://k8slens.dev/)A cloud subscription with the following: 

  - SAP PM ABAP resource to validate the Client environment and to make necessary configuration changes.

  - Azure license/subscription to create resources for implementation.

  - Azure DevOps repository for extractor code and pipeline files.

  - Azure service connections for SonarQube and Container Registry.

  - Namespace in the AKS cluster for environments.

  - Kubernetes Service Connection for AKS Cluster.

  - Sonar project and key.

## Configure Azure DevOps

Before creating the pipelines, the Azure DevOps environment must be prepared.

1.  Create an Azure Key Vault.

2.  Add the following secrets in the Azure Key Vault created in the previous step:

| **Secret** | **Description** |
|----|----|
| ClientID | Provide the Client ID for Cognite Data Fusion |
| ClientSecret | Provide the Client Secret for Cognite Data Fusion |
| SapUserName | Provide the SAP Username to perform authentication with the SAP system |
| SapPassword | Provide the SAP Password to perform authentication with the SAP system |
| SapWOkey | Provide the SAP key to perform authentication with the SAP system |

`\>` 

3.  

4.  Create a key vault library in Azure DevOps and add the secrets created in the previous step.

`\>` 

5.  Create a Library/Variable Group in Azure DevOps with the following parameters:

| **Variable** | **Description** |
|----|----|
| COGNITE_HOST | Provide the host details for Cognite data fusion. |
| COGNITE_PROJECT | Provide the project name for Cognite data fusion. |
| SCOPES | Provide the scopes for Cognite data fusion. |
| TENANT_ID | Provide the tenant ID for Cognite data fusion. |
| SAP_WO_CONFIG_FILENAME | Provide the configuration filename that is used to run the extractor. The filenames are environment-specific e.g., sap\_wo_dev_config.yaml, sap\_ wo_itest_config.yaml and sap\_ wo_prod_config.yaml. |
| CONTAINER_REGISTRY_SERVICE_CONNECTION | Provide container registry service connection for build and release pipeline. |
| SONARQUBE_SERVICE_CONNECTION | Provide service connection for SonarQube. |
| SAP_CLI_PROJECT_KEY | Provide SonarQube project key for SAP WO extractor. |
| SAP_CLI_PROJECT_NAME | Provide SonarQube project name for SAP WO extractor. |

`\>` 

6.  

7.  Navigate to the pipelines file location “Source/Extractors/sap-extractor-work-order/pipeline/Dev/azure-pipelines.yml” and ensure that the pipeline refers to the libraries created in the previous steps.

`\>` 

8.  Configure the following parameters in the configuration file for the SAP WO extractor:

- Provide timer value in seconds to schedule the extractor.

`\>` 

- Mandatory Cognite-related config parameters:

| **Parameter** | **Description** |
|----|----|
| host | Use the hostname for Cognite data fusion (CDF) added in the Azure DevOps library in earlier steps |
| project | Use the project name for CDF added in the Azure DevOps library in earlier steps |
| idp-authentication. client-id | Use the client Id for CDF added in the Azure DevOps key vault library in earlier steps |
| idp-authentication. secret | Use the client secret for CDF added in the Azure DevOps key vault library in earlier steps |
| idp-authentication. scopes | Use the scopes for CDF added in the Azure DevOps library in earlier steps |
| idp-authentication. tenant | Use the tenant Id for CDF added in the Azure DevOps library in earlier steps |

`\>` 

- 

- Mandatory SAP WO config parameters:

| **Parameter** | **Description** |
|----|----|
| host | Provide a hostname for the SAP system |
| port | Provide a port number for the SAP system |
| endpoint | Provide an endpoint to connect to the SAP system |
| key | Use the SAP WO key to perform authentication with the SAP system added in the Azure DevOps library in earlier steps |
| Key_column | Provide a unique column name present in the data |
| assets.destination.database | Provide a database name in CDF where the table would be created |
| assets.destination.table | Provide a table name where Work order data will be uploaded |
| full_load | Provide a Boolean value. When the full load is true, then full load functionality is executed. And when full load is false, then incremental load functionality is executed. |
| IInProcess | Provide a string value to get data for in-process work orders. |
| IMaintPlant | Provide the name of the maintenance plant from SAP |
| ITplnr | Provide a name of the Functional location from SAP |
| IOutstanding | Provide a string value to get data for outstanding work orders |
| ICompleted | Provide a string value to get data for completed work orders. |
| Extractor_Last_Run_Table | Provide an extractor last run table name that will be used in CDF RAW |
| Extractor_key | Provide work order details type whose last run date is required that is stored in Extractor_Last Run table from CDF RAW |
| Log_Table | Provide a log table name that will be used in CDF RAW |

`\>` 
`\>`
`\>` Note that the SAP WO Extractor allows the configuration of multiple SAP Systems. Also, multiple root asset details can be configured to fetch work order header, notifications, operations, and components data from the SAP systems.

- 

- Extraction pipeline-related config parameters:

| **Parameter** | **Description** |
|----|----|
| datasetexternal_id | Provide the External id of the Dataset in Cognite data fusion (CDF) |
| dataset_name | Provide the name of the Dataset in CDF |
| external_id | Provide external id of CDF extraction pipeline |
| ep_name | Provide the name of the CDF extraction pipeline |
| contacts.name | Optional - Provide the name of the contact to whom the extraction pipeline notification should be sent. |
| contacts.email | Optional - Provide the email of the contact to whom the extraction pipeline notification should be sent. |
| contacts.sendnotification | Optional - Provide notification value. If the send notification value is true, then mail is sent to the respective mail Id else no mail is sent. |

`\>` 

## 

## Create a Build Pipeline

The Build Pipeline is used to Dockerize the Extractor Package. The artifacts created here are used in the release pipeline for deployment. To create a build pipeline:

1.  Navigate to Azure DevOps, select pipelines, and then select *New Pipeline*.

`\>` 

2.  Select *Azure Repos Git* and then select the *Repository Name* that contains SAP WO Extractor code and pipeline files.



3.  Select ‘*Existing Azure Pipelines YAML file’*.

`\>` 

4.  Select the branch, provide the pipeline file path as “Source/Extractors/sap-extractor-work-order/pipeline/Dev/azure-pipelines.yml”, and click on Continue.

`\>` 

5.  Review and save.

6.  Run the pipeline and wait for its successful completion.

`\>` 

## 

## Create a Release Pipeline

The Release pipeline deploys the Docker Image of the SAP WO Extractor created by the build pipeline to the AKS Cluster. Follow the steps below to create the SAP WO Extractor release pipeline:

1.  Create a release pipeline with two tasks for AKS Cluster.

    - task with delete command

    - task with create command

2.  Update the value of the service connection for the AKS cluster in the tasks.

`\>` 

3.  Update the AKS file location in the tasks.

`\>` 

4.  

5.  If this is the first run, then disable the delete task from the pipeline.

`\>` 

6.  Create a release from the release pipeline created in the previous step.



7.  Once the release is completed, confirm successful deployment on Azure DevOps.

`\>` 

8.  

9.  After deployment is complete, validate the successful deployment to the AKS cluster in the Azure portal.

`\>` 

10. Validate SAP WO Extractor logs on the [Lens](https://k8slens.dev/) app.

`\>` 

11. 

12. If everything looks good and the AKS POD has been created, re-enable the delete task that was previously disabled.

`\>` 

13. Validate the creation of database and table with Work Order header, notification, operations, and components on CDF Portal.

    1.  WO Header

`\>` 

2.  

3.  WO Notification

`\>` 

4.  WO Operations

`\>` 

5.  

6.  WO Components

`\>` 

14. On Deployment Completion, an extraction pipeline is created in CDF based on the details provided in the configuration file. Success/Failure messages can be visualized on the CDF portal. Also, a notification is sent to the respective email address.

`\>` 
`\>`
`\>` 

# 

# On-Prem Deployment

The SAP WO Extractor Windows Service is created to give users the option of deploying SAP WO Extractor on-premises.

The SAP WO Extractor Windows service is installed through a batch script that runs all the necessary commands required for the installation.

SAP WO Extractor extracts work order data from one or more SAP systems and inserts it into CDF RAW.

## Prerequisites

- SAP server username, password, and SAP WO key.

- Web API URL for each SAP work order.

- Python must be installed.

## Install the Extractor 

1.  Edit *sap_wo_config.yaml* file to update the following:

- Add the path of a log file to store extractor logs.

`\>` 

- Add timer value in seconds to schedule the extractor.

`\>` 

- Add Cognite-related details described in the table below.

| **Parameter** | **Description** | **Optional(O)/Mandatory(M)** |
|----|----|----|
| host | Provide the hostname for Cognite data fusion (CDF) | M |
| project | Provide the project name for CDF | M |
| idp-authentication. client-id | Provide the client Id for CDF | M |
| idp-authentication. secret | Provide the client secret for CDF | M |
| idp-authentication. scopes | Provide the scopes for CDF | M |
| idp-authentication. tenant | Provide the tenant Id for CDF | M |

- Add extraction pipeline-related details.

| **Parameter** | **Description** | **M/O** |
|----|----|----|
| datasetexternal_id | Provide the external Id of the dataset in CDF. | M |
| dataset_name | Provide the name of the dataset in CDF. | M |
| external_id | Provide external Id of CDF extraction pipeline. | M |
| ep_name | Provide the name of the CDF extraction pipeline. | M |
| contacts.name | Provide the name of the contact to whom the extraction pipeline notification should be sent. | O |
| contacts.email | Provide the email of the contact to whom the extraction pipeline notification should be sent. | O |
| contacts.sendnotification | Provide notification value. If the send notification value is true, then mail is sent to the respective mail Id else no mail is sent. | O |

- 

- Add SAP WO system configurations

| **Parameter** | **Description** | **M / O** |
|----|----|----|
| host | Provide a hostname for the SAP system. | M |
| port | Provide a port number for the SAP system. | M |
| endpoint | Provide an endpoint to connect to the SAP system. | M |
| key | Provide an SAP key to perform authentication with the SAP system added in the Azure DevOps library in earlier steps. | M |
| Key_column | Provide a unique column name present in the data. | M |
| assets.destination.database | Provide a database name in CDF where the table would be created. | M |
| assets.destination.table | Provide a table name where work order data will be uploaded. | M |
| full_load | Provide a Boolean value. When the full load is true, then full load functionality is executed. And when full load is false, then incremental load functionality is executed. | M |
| Change_date | Provide the date of the last run of the extractor. It will be used for incremental load functionality | O |
| IMaintPlant | Provide the name of the maintenance plant from SAP. | M |
| ITplnr | Provide a name of the Functional location from SAP. | O |
| IInProcess | Provide a full load value, this parameter is required for RFC. | M |
| IOutstanding | Provide a string to get data for outstanding work orders. | O |
| ICompleted | Provide a string value to get data for completed work orders. | O |
| ICreatedDateStart | Provide a date in a string value to get data between the selected time period. This is the start time. | O |
| ICreatedDateEnd | Provide a date in a string value to get data between the selected time period. This is the end time. | O |
| Extractor_Last_Run_Table | Provide an extractor last run table name that will be used in CDF RAW. | M |
| Extractor_key | Provide work order details type whose last run date is required that is stored in Extractor_Last Run table from CDF RAW. | M |
| Log_Table | Provide a log table name that will be used in CDF RAW. | M |

2.  Edit the *WSInstallation.bat* file to add the absolute path of the Python folder and WorkOrderWindowsService.py file as shown below.

`\>` 

3.  To install the SAP WO Extractor on the premise, right-click on the WSInstallation.bat file and select Run as Administrator. It installs all the required Python modules and SAP WO extractor as a windows service.

4.  

5.  Verify the following libraries are installed correctly in the system.

    - pywin32 module

    - cognite-extractor-utils module

    - pythonX.dll

    - pythonXX.dll

    - pythoncomXX.dll

    - pywintypesXX.dll

`\>` 
`\>`
`\>` 

## 

## Start the Extractor

1.  Click the Start button, search for “Services”, and select Run as Administrator.

`\>` 

2.  Search for the “SAPWorkOrderExtractor” service name, right-click on it, and select Start.

`\>` 

3.  Once the SAPWorkOrderExtractor starts running, check the logs in the log file on the given path in the configuration file.

4.  Validate the creation of database and table with Work Order header, notification, operations, and components on CDF Portal.

`\>` 

5.  Validate the creation of the extraction pipeline with a success message on the CDF portal.

`\>` 

## 

## Stop the Extractor

1.  Click the Start button, search for “Services”, and select Run as Administrator.

`\>` 

2.  Search for the “SAPWorkOrderExtractor” service name, right-click on it, and select Stop.

`\>` 
