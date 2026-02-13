---
sidebar_position: 2
title: AOT SAP WO Extractor Deployment Guide Auriga
---

**Accenture Operations Twin**

**SAP Work Order Extractor**

**DEPLOYMENT GUIDE**

Release Version:2.5

**Metadata Table**

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / Data Integration Accelerators

  **Domain / Area**                   Data Processing

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Joshi, Rishabh

  **Status**                          Published / Complete

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   AOT Extractors Architecture Blueprint, AOT Extractors Getting Started
  -----------------------------------------------------------------------------------------------------------------

# Contents \{#contents .TOC-Heading\}

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

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools -- including extractors -- that are assembled to deliver client solutions. AOT accelerates the integration of the product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT extractors are data integration accelerators that are developed to automate and ease the process of extracting data from enterprise source systems. After the data is extracted, it is processed and transformed into a format that Cognite recognizes. Finally, the processed and transformed data is pushed to CDF RAW.

The SAP Work Order (WO) Extractor gives users the power to send SAP work order data to CDF without having to manually run commands. Once the configuration file is built, the extractor can refer to the Root Functional Location, extract the work order details from SAP, and push that data to CDF RAW. Furthermore, the SAP WO extractor grants a user the flexibility to configure one or more source systems as well as the Cognite details that enable data extraction.

## Purpose

This document explains how to extract data from the source system and load it into CDF RAW. It also covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF. The objective is to obtain Work Order details from SAP and make them available as an OData service for the Python extractor to consume and store in Cognite Staging areas.

[]\{#_Toc214351075 .anchor\}**Target Audience**

This guide is designed for use by developers with the following skills:

-   Sonar Qube

-   Cognite Data Fusion

-   SAP

-   Python

## Contacts

-   

-   

## Related Links

-   [How to create OData Service](https://blogs.sap.com/2019/10/07/creation-of-odata-services-for-beginners/)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

  --------------------------------------------------------------------------------------------------------------------------------------------------------------
  Term                  Definition
  --------------------- ----------------------------------------------------------------------------------------------------------------------------------------
  Cognite Data Fusion   An industrial data platform that enables integration, contextualization, and visualization of data from multiple sources.

  SAP                   A global enterprise software company specializing in business operations and customer relations solutions.

  Python                A high-level, interpreted programming language known for its simplicity and versatility in data analytics and automation.

  OData                 An open data protocol used for querying and updating data over the web, leveraging standard web technologies such as HTTP and AtomPub.

  Function module       A reusable set of source code statements in SAP, designed to perform specific tasks with defined importing and exporting parameters.

  Subprogram            A module containing reusable code statements, often used to structure and organize programming tasks within larger applications.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------

# Architecture Diagram

![Diagram depicting the Data Integration Architecture](media/image2.png)\{width="9.19924321959755in" height="3.761981627296588in"\}

# 

# SAP WO Configuration

Configuration of SAP WO includes three deployment tasks:

**Function module**

Subprograms that contain a set of reusable source code statements with importing and exporting parameters and exceptions.

**\
Open data protocol**

OData is a Web protocol for querying and updating data, applying, and building on Web technologies such as HTTP, Atom Publishing Protocol (AtomPub), and RSS (Really Simple Syndication) to provide access to information from a variety of applications.

**\
Transport and package**

An SAP Transport is a kind of \'Container/Collection\' of changes that are made in the development system. It also records information regarding the type of change, the purpose of transport, the request category, and the target system.

## Function Module 

### Creation

1.  In SAP, use t-code \"se37\" to access the Function Builder.

2.  In the name field, enter the name of the function module, and then click Create.

3.  Choose the ZCOGNITE function group and enter a short text description.

4.  Click Save.

### Structures and Tables Creation

1.  Enter t-code \"se11\".

2.  Select the Data Type Radio button, enter a new name for the Structure, and click Create.

3.  Select the Structure Radio Button and press Enter.

4.  Enter a short description and add the required fields in the rows for the structure and their description.

5.  Click on *Save* and open t-code \"se11\" for table creation.

6.  Select the Data Type Radio button and enter a new name for Structure. Then, click Create.

7.  Select the Table Radio Button and press Enter.

8.  Enter a short description and select the Line Type radio button. Then, enter the name of the structure created.

9.  Now add details like Primary Key, Secondary Key, Attributes, etc., if needed, and click on Save.

### Update

1.  Use the t-code \"se37\" to access the function module.

2.  In the name field, enter the name of the function module that you have created, and then click the Change button.

3.  In the Tables tab, import the table created in the above step by clicking on the Insert Row button.

> ![Screenshot of function module showing the \"insert row\" button](media/image3.png)\{width="8.593990594925634in" height="2.1354166666666665in"\}

4.  

5.  Edit the source code to suit the use case.

> ![Screenshot of the Function module showing the source code that can be edited.](media/image4.emf)\{width="8.52361111111111in" height="4.547002405949256in"\}

6.  In the Import tab, enter any parameters (e.g., Root Functional Location) that are needed during the execution of the function module.

> ![Screenshot of import tab where parameters can be entered](media/image5.emf)\{width="7.705965660542432in" height="3.321738845144357in"\}

7.  

8.  Execute the function module using F8 or the button highlighted in the screenshot below.

> ![Screenshot of the function module showing the execute button](media/image6.emf)\{width="7.125in" height="3.197230971128609in"\}

9.  Enter the parameter and execute it using F8 or the button highlighted in the screenshot below.

> ![Screenshot showing the execute button after entering the parameters](media/image7.emf)\{width="8.23611111111111in" height="2.7880063429571305in"\}

## 

## Open Data Protocol 

### Creation

1.  Open the t-code \"SEGW\" and create a new project using the Create Project button.

> ![Screenshot of SAP](media/image8.png)\{width="4.8920844269466315in" height="2.506159230096238in"\}

2.  Create a new Entity type and Entity sets using the Import option \> DDIC structure by right-clicking on the Data Model.

> ![Screenshot of SAP](media/image9.png)\{width="2.8333333333333335in" height="1.2410465879265091in"\}

3.  Enter the name and the ABAP structure that was created during the creation of the function module.

> ![Screenshot of SAP](media/image10.png)\{width="6.732384076990376in" height="4.140941601049869in"\}

4.  

5.  After creation, the screen is similar to as depicted in the image below.

> ![Screenshot of SAP](media/image11.png)\{width="5.347916666666666in" height="2.234027777777778in"\}

6.  Use the red and white Generate Runtime Object button to launch the Model and Service Definition window.

> ![](media/image12.png)

7.  Check for the successful creation of the service and model.

> ![Screenshot of SAP](media/image13.png)\{width="5.567028652668417in" height="1.3096139545056869in"\}

8.  Use the t-code \"IWFND/MAINT_SERVICE\" to activate and maintain the nodes.

> ![Screenshot of SAP](media/image14.png)\{width="6.963896544181977in" height="1.1790266841644794in"\}

## 

## Transport and Package Creation

A Workbench request and a package to carry the TADIR objects are required to transport any OData service.

1.  Use t-code \"SE01\" to open the Transport Organizer window, click on Create, and select Workbench Request.

> ![](media/image15.png)

1.  Use the t-code \"SE80\" to create the package. Select the package from the dropdown list that is under the Repository Browser. To create a package, enter the package name and click on the **Display** icon.

> ![Screenshot of SAP](media/image16.png)\{width="6.12746719160105in" height="2.653986220472441in"\}

2.  To capture all the details, add the new ZCDF package to the previous transport while creating the new package. Standard OData Service TADIR Objects are listed in the table below.

  ----------------------------------------------------------------------------------------------------------------
  **Short Description**                  **Program ID**   **Object Type**   **Object Name**
  -------------------------------------- ---------------- ----------------- --------------------------------------
  Package                                R3TR             DEVC              Z\*\*\*\_PKG

  SAP Gateway: Model Metadata            R3TR             IWSG              Z\\_SRV_0001

  SAP Gateway: Service Groups Metadata   R3TR             IWOM              Z\\_MDL_0001_BE

  ICF Service                            R3TR             SICF              \\*\*\*\*\*\*\*
  ----------------------------------------------------------------------------------------------------------------

3.  

4.  While creating the SEGW project, add everything to the workbench request. The final package is now created.

> ![Screenshot of SAP](media/image17.png)\{width="6.957175196850394in" height="3.897463910761155in"\}

5.  Validate the final transport request once it is successfully created.

> ![Screenshot of SAP](media/image18.png)\{width="8.458755468066492in" height="4.059027777777778in"\}

# 

# Cloud Deployment

Two pipelines are needed to deploy the extractor to an AKS Cluster. This section includes step-by-step guidance for:

-   Prerequisites that need to be fulfilled before the extractor can be deployed and used.

-   Setting up the Azure DevOps environment.

-   Creating a Build Pipeline for Dockerizing the Extractor Package.

-   Creating a Release Pipeline for deploying the Docker image to the AKS cluster.

-   Validating the data in the RAW table in CDF RAW.

## Prerequisites 

-   

-   [Lens](https://k8slens.dev/)A cloud subscription with the following: 

    -   SAP PM ABAP resource to validate the Client environment and to make necessary configuration changes.

    -   Azure license/subscription to create resources for implementation.

    -   Azure DevOps repository for extractor code and pipeline files.

    -   Azure service connections for SonarQube and Container Registry.

    -   Namespace in the AKS cluster for environments.

    -   Kubernetes Service Connection for AKS Cluster.

    -   Sonar project and key.

## Configure Azure DevOps

Before creating the pipelines, the Azure DevOps environment must be prepared.

1.  Create an Azure Key Vault.

2.  Add the following secrets in the Azure Key Vault created in the previous step:

  ---------------------------------------------------------------------------------------
  **Secret**     **Description**
  -------------- ------------------------------------------------------------------------
  ClientID       Provide the Client ID for Cognite Data Fusion

  ClientSecret   Provide the Client Secret for Cognite Data Fusion

  SapUserName    Provide the SAP Username to perform authentication with the SAP system

  SapPassword    Provide the SAP Password to perform authentication with the SAP system

  SapWOkey       Provide the SAP key to perform authentication with the SAP system
  ---------------------------------------------------------------------------------------

> ![screenshot of secret creation ](media/image19.png)\{width="3.955224190726159in" height="3.225132327209099in"\}

3.  

4.  Create a key vault library in Azure DevOps and add the secrets created in the previous step.

> ![screenshot of key vault creation](media/image20.png)\{width="6.322916666666667in" height="3.88702646544182in"\}

5.  Create a Library/Variable Group in Azure DevOps with the following parameters:

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Variable**                            **Description**
  --------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  COGNITE_HOST                            Provide the host details for Cognite data fusion.

  COGNITE_PROJECT                         Provide the project name for Cognite data fusion.

  SCOPES                                  Provide the scopes for Cognite data fusion.

  TENANT_ID                               Provide the tenant ID for Cognite data fusion.

  SAP_WO_CONFIG_FILENAME                  Provide the configuration filename that is used to run the extractor. The filenames are environment-specific e.g., sap\_wo_dev_config.yaml, sap\_ wo_itest_config.yaml and sap\_ wo_prod_config.yaml.

  CONTAINER_REGISTRY_SERVICE_CONNECTION   Provide container registry service connection for build and release pipeline.

  SONARQUBE_SERVICE_CONNECTION            Provide service connection for SonarQube.

  SAP_CLI_PROJECT_KEY                     Provide SonarQube project key for SAP WO extractor.

  SAP_CLI_PROJECT_NAME                    Provide SonarQube project name for SAP WO extractor.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![screenshot of library](media/image21.png)\{width="6.424242125984252in" height="1.9804997812773404in"\}

6.  

7.  Navigate to the pipelines file location \"Source/Extractors/sap-extractor-work-order/pipeline/Dev/azure-pipelines.yml\" and ensure that the pipeline refers to the libraries created in the previous steps.

> ![Screenshot of the azure-pipeline.yml file ](media/image22.emf)\{width="7.0151520122484685in" height="1.8723283027121609in"\}

8.  Configure the following parameters in the configuration file for the SAP WO extractor:

-   Provide timer value in seconds to schedule the extractor.

> ![screenshot of timer value](media/image23.png)\{width="5.052083333333333in" height="0.958066491688539in"\}

-   Mandatory Cognite-related config parameters:

  -----------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                   **Description**
  ------------------------------- ---------------------------------------------------------------------------------------------------
  host                            Use the hostname for Cognite data fusion (CDF) added in the Azure DevOps library in earlier steps

  project                         Use the project name for CDF added in the Azure DevOps library in earlier steps

  idp-authentication. client-id   Use the client Id for CDF added in the Azure DevOps key vault library in earlier steps

  idp-authentication. secret      Use the client secret for CDF added in the Azure DevOps key vault library in earlier steps

  idp-authentication. scopes      Use the scopes for CDF added in the Azure DevOps library in earlier steps

  idp-authentication. tenant      Use the tenant Id for CDF added in the Azure DevOps library in earlier steps
  -----------------------------------------------------------------------------------------------------------------------------------

> ![screenshot specifying the parameter to connect Cognite server](media/image24.png)\{width="6.84375in" height="2.325181539807524in"\}

-   

-   Mandatory SAP WO config parameters:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                 **Description**
  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  host                          Provide a hostname for the SAP system

  port                          Provide a port number for the SAP system

  endpoint                      Provide an endpoint to connect to the SAP system

  key                           Use the SAP WO key to perform authentication with the SAP system added in the Azure DevOps library in earlier steps

  Key_column                    Provide a unique column name present in the data

  assets.destination.database   Provide a database name in CDF where the table would be created

  assets.destination.table      Provide a table name where Work order data will be uploaded

  full_load                     Provide a Boolean value. When the full load is true, then full load functionality is executed. And when full load is false, then incremental load functionality is executed.

  IInProcess                    Provide a string value to get data for in-process work orders.

  IMaintPlant                   Provide the name of the maintenance plant from SAP

  ITplnr                        Provide a name of the Functional location from SAP

  IOutstanding                  Provide a string value to get data for outstanding work orders

  ICompleted                    Provide a string value to get data for completed work orders.

  Extractor_Last_Run_Table      Provide an extractor last run table name that will be used in CDF RAW

  Extractor_key                 Provide work order details type whose last run date is required that is stored in Extractor_Last Run table from CDF RAW

  Log_Table                     Provide a log table name that will be used in CDF RAW
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![Screenshot of the SAP WO related config parameters](media/image25.png)\{width="5.3327143482064745in" height="5.123829833770778in"\}
>
> Note that the SAP WO Extractor allows the configuration of multiple SAP Systems. Also, multiple root asset details can be configured to fetch work order header, notifications, operations, and components data from the SAP systems.

-   

-   Extraction pipeline-related config parameters:

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**               **Description**
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------
  datasetexternal_id          Provide the External id of the Dataset in Cognite data fusion (CDF)

  dataset_name                Provide the name of the Dataset in CDF

  external_id                 Provide external id of CDF extraction pipeline

  ep_name                     Provide the name of the CDF extraction pipeline

  contacts.name               Optional - Provide the name of the contact to whom the extraction pipeline notification should be sent.

  contacts.email              Optional - Provide the email of the contact to whom the extraction pipeline notification should be sent.

  contacts.sendnotification   Optional - Provide notification value. If the send notification value is true, then mail is sent to the respective mail Id else no mail is sent.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![Screenshot of the extraction pipeline related config parameters](media/image26.png)\{width="4.032236439195101in" height="2.7567989938757655in"\}

## 

## Create a Build Pipeline

The Build Pipeline is used to Dockerize the Extractor Package. The artifacts created here are used in the release pipeline for deployment. To create a build pipeline:

1.  Navigate to Azure DevOps, select pipelines, and then select *New Pipeline*.

> ![screenshot of azure devops](media/image27.png)\{width="8.668055555555556in" height="2.356956474190726in"\}

2.  Select *Azure Repos Git* and then select the *Repository Name* that contains SAP WO Extractor code and pipeline files.

![screenshot of azure devops](media/image28.png)\{width="5.46875in" height="3.1272287839020123in"\}

3.  Select \'*Existing Azure Pipelines YAML file\'*.

> ![screenshot of azure devops](media/image29.png)\{width="6.104166666666667in" height="3.309704724409449in"\}

4.  Select the branch, provide the pipeline file path as \"Source/Extractors/sap-extractor-work-order/pipeline/Dev/azure-pipelines.yml\", and click on Continue.

> ![screenshot of azure devops](media/image30.png)\{width="8.635416666666666in" height="4.064620516185477in"\}

5.  Review and save.

6.  Run the pipeline and wait for its successful completion.

> ![Screenshot of the Build Pipeline with the Run pipeline option shown](media/image31.emf)\{width="6.90625in" height="1.4587576552930883in"\}

## 

## Create a Release Pipeline

The Release pipeline deploys the Docker Image of the SAP WO Extractor created by the build pipeline to the AKS Cluster. Follow the steps below to create the SAP WO Extractor release pipeline:

1.  Create a release pipeline with two tasks for AKS Cluster.

    -   task with delete command

    -   task with create command

2.  Update the value of the service connection for the AKS cluster in the tasks.

> ![Screenshot showing the field to update the value of the service connection for AKS cluster](media/image32.emf)\{width="8.641522309711286in" height="3.6979166666666665in"\}

3.  Update the AKS file location in the tasks.

> ![Screenshot showing the field to update the AKS file location in the tasks](media/image33.emf)\{width="8.683514873140858in" height="3.1319444444444446in"\}

4.  

5.  If this is the first run, then disable the delete task from the pipeline.

> ![Screenshot showing the option to enable/disable the delete task from the pipeline](media/image34.emf)\{width="7.28125in" height="3.5288199912510936in"\}

6.  Create a release from the release pipeline created in the previous step.

![Screenshot depicting the \"Create release\" button](media/image35.emf)\{width="6.25in" height="1.0409984689413823in"\}

7.  Once the release is completed, confirm successful deployment on Azure DevOps.

> ![Screenshot depicting the successful deployment on Azure DevOps](media/image36.emf)\{width="4.544317585301838in" height="3.439394138232721in"\}

8.  

9.  After deployment is complete, validate the successful deployment to the AKS cluster in the Azure portal.

> ![screenshot of azure devops](media/image37.png)\{width="8.65625in" height="3.7601607611548555in"\}

10. Validate SAP WO Extractor logs on the [Lens](https://k8slens.dev/) app.

> ![screenshot of lens app](media/image38.png)\{width="8.572916666666666in" height="3.8423851706036745in"\}

11. 

12. If everything looks good and the AKS POD has been created, re-enable the delete task that was previously disabled.

> ![Screenshot depicting the option to enable the delete task that was previously disabled](media/image39.emf)\{width="8.71875in" height="2.9143318022747158in"\}

13. Validate the creation of database and table with Work Order header, notification, operations, and components on CDF Portal.

    a.  WO Header

> ![Screenshot of WO Header on CDF portal](media/image40.emf)\{width="8.746486220472441in" height="3.7730260279965004in"\}

b.  

c.  WO Notification

> ![Screenshot of WO Notification on CDF portal](media/image41.emf)\{width="8.206944444444444in" height="3.432512029746282in"\}

d.  WO Operations

> ![Screenshot of WO Operations on CDF portal](media/image42.emf)\{width="8.217643263342083in" height="3.4805675853018374in"\}

e.  

f.  WO Components

> ![Screenshot of WO Components on CDF portal](media/image43.emf)\{width="8.29940069991251in" height="3.5in"\}

14. On Deployment Completion, an extraction pipeline is created in CDF based on the details provided in the configuration file. Success/Failure messages can be visualized on the CDF portal. Also, a notification is sent to the respective email address.

> ![Screenshot of success message in CDF portal](media/image44.emf)\{width="8.652123797025371in" height="0.8541666666666666in"\}
>
> ![Screenshot of failure message in CDF portal](media/image45.png)\{width="8.770833333333334in" height="1.3342191601049869in"\}

# 

# On-Prem Deployment

The SAP WO Extractor Windows Service is created to give users the option of deploying SAP WO Extractor on-premises.

The SAP WO Extractor Windows service is installed through a batch script that runs all the necessary commands required for the installation.

SAP WO Extractor extracts work order data from one or more SAP systems and inserts it into CDF RAW.

## Prerequisites

-   SAP server username, password, and SAP WO key.

-   Web API URL for each SAP work order.

-   Python must be installed.

## Install the Extractor 

1.  Edit *sap_wo_config.yaml* file to update the following:

-   Add the path of a log file to store extractor logs.

> ![Screenshot of path of a log file to store extractor logs](media/image46.emf)\{width="4.426085958005249in" height="0.7472769028871391in"\}

-   Add timer value in seconds to schedule the extractor.

> ![screenshot of timer value](media/image47.png)\{width="6.810416666666667in" height="1.386111111111111in"\}

-   Add Cognite-related details described in the table below.

  -------------------------------------------------------------------------------------------------------------------
  **Parameter**                   **Description**                                      **Optional(O)/Mandatory(M)**
  ------------------------------- ---------------------------------------------------- ------------------------------
  host                            Provide the hostname for Cognite data fusion (CDF)   M

  project                         Provide the project name for CDF                     M

  idp-authentication. client-id   Provide the client Id for CDF                        M

  idp-authentication. secret      Provide the client secret for CDF                    M

  idp-authentication. scopes      Provide the scopes for CDF                           M

  idp-authentication. tenant      Provide the tenant Id for CDF                        M
  -------------------------------------------------------------------------------------------------------------------

-   Add extraction pipeline-related details.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**               **Description**                                                                                                                         **M/O**
  --------------------------- --------------------------------------------------------------------------------------------------------------------------------------- ---------
  datasetexternal_id          Provide the external Id of the dataset in CDF.                                                                                          M

  dataset_name                Provide the name of the dataset in CDF.                                                                                                 M

  external_id                 Provide external Id of CDF extraction pipeline.                                                                                         M

  ep_name                     Provide the name of the CDF extraction pipeline.                                                                                        M

  contacts.name               Provide the name of the contact to whom the extraction pipeline notification should be sent.                                            O

  contacts.email              Provide the email of the contact to whom the extraction pipeline notification should be sent.                                           O

  contacts.sendnotification   Provide notification value. If the send notification value is true, then mail is sent to the respective mail Id else no mail is sent.   O
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-   

-   Add SAP WO system configurations

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                 **Description**                                                                                                                                                                **M / O**
  ----------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ -----------
  host                          Provide a hostname for the SAP system.                                                                                                                                         M

  port                          Provide a port number for the SAP system.                                                                                                                                      M

  endpoint                      Provide an endpoint to connect to the SAP system.                                                                                                                              M

  key                           Provide an SAP key to perform authentication with the SAP system added in the Azure DevOps library in earlier steps.                                                           M

  Key_column                    Provide a unique column name present in the data.                                                                                                                              M

  assets.destination.database   Provide a database name in CDF where the table would be created.                                                                                                               M

  assets.destination.table      Provide a table name where work order data will be uploaded.                                                                                                                   M

  full_load                     Provide a Boolean value. When the full load is true, then full load functionality is executed. And when full load is false, then incremental load functionality is executed.   M

  Change_date                   Provide the date of the last run of the extractor. It will be used for incremental load functionality                                                                          O

  IMaintPlant                   Provide the name of the maintenance plant from SAP.                                                                                                                            M

  ITplnr                        Provide a name of the Functional location from SAP.                                                                                                                            O

  IInProcess                    Provide a full load value, this parameter is required for RFC.                                                                                                                 M

  IOutstanding                  Provide a string to get data for outstanding work orders.                                                                                                                      O

  ICompleted                    Provide a string value to get data for completed work orders.                                                                                                                  O

  ICreatedDateStart             Provide a date in a string value to get data between the selected time period. This is the start time.                                                                         O

  ICreatedDateEnd               Provide a date in a string value to get data between the selected time period. This is the end time.                                                                           O

  Extractor_Last_Run_Table      Provide an extractor last run table name that will be used in CDF RAW.                                                                                                         M

  Extractor_key                 Provide work order details type whose last run date is required that is stored in Extractor_Last Run table from CDF RAW.                                                       M

  Log_Table                     Provide a log table name that will be used in CDF RAW.                                                                                                                         M
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2.  Edit the *WSInstallation.bat* file to add the absolute path of the Python folder and WorkOrderWindowsService.py file as shown below.

> ![ Screenshot of how to Edit WSInstallation.bat file to add the absolute path of Python folder and WorkOrderWindowsService.py file ](media/image48.emf)\{width="7.781303587051618in" height="4.135416666666667in"\}

3.  To install the SAP WO Extractor on the premise, right-click on the WSInstallation.bat file and select Run as Administrator. It installs all the required Python modules and SAP WO extractor as a windows service.

4.  

5.  Verify the following libraries are installed correctly in the system.

    -   pywin32 module

    -   cognite-extractor-utils module

    -   pythonX.dll

    -   pythonXX.dll

    -   pythoncomXX.dll

    -   pywintypesXX.dll

> ![screenshot of windows start menu](media/image49.png)\{width="4.751873359580053in" height="3.8541666666666665in"\}
>
> ![screenshot of installed libraries](media/image50.png)\{width="8.15in" height="1.12170384951881in"\}

## 

## Start the Extractor

1.  Click the Start button, search for \"Services\", and select Run as Administrator.

> ![screenshot of windows services app actions](media/image51.png)\{width="5.15625in" height="2.6625371828521436in"\}

2.  Search for the \"SAPWorkOrderExtractor\" service name, right-click on it, and select Start.

> ![Screenshot of Services window showing the option to Start the "SAPWorkOrderExtractor\" service](media/image52.emf)\{width="6.34375in" height="2.2498326771653545in"\}

3.  Once the SAPWorkOrderExtractor starts running, check the logs in the log file on the given path in the configuration file.

4.  Validate the creation of database and table with Work Order header, notification, operations, and components on CDF Portal.

> ![Screenshot of WO Header table](media/image40.emf)\{width="8.550676946631672in" height="3.6885586176727907in"\}

5.  Validate the creation of the extraction pipeline with a success message on the CDF portal.

> ![Screenshot of success message in CDF portal](media/image44.emf)\{width="8.57156605424322in" height="0.8462150043744532in"\}

## 

## Stop the Extractor

1.  Click the Start button, search for \"Services\", and select Run as Administrator.

> ![screenshot of windows services app actions](media/image51.png)\{width="4.708333333333333in" height="2.436117672790901in"\}

2.  Search for the \"SAPWorkOrderExtractor\" service name, right-click on it, and select Stop.

> ![Screenshot of Services window showing the SAPWorkOrderExtractor service and the Stop option](media/image53.emf)\{width="7.093365048118985in" height="3.043478783902012in"\}
