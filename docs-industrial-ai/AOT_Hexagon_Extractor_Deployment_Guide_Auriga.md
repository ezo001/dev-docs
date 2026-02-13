---
sidebar_position: 2
title: AOT Hexagon Extractor Deployment Guide Auriga
---

**Accenture Operations Twin**

Hexagon Extractor

**DEPLOYMENT GUIDE**

Release Version: 2.5

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

#  \{#section .TOC-Heading\}

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Assumptions [3](#assumptions)](#assumptions)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [4](#glossary)](#glossary)

[Hexagon SDx Configuration [5](#section-2)](#section-2)

[SPFVNet Server Connection [5](#spfvnet-server-connection)](#spfvnet-server-connection)

[Create Asset Hierarchy on HxGN SDx [9](#create-asset-hierarchy-on-hxgn-sdx)](#create-asset-hierarchy-on-hxgn-sdx)

[Add Properties to Tags [10](#add-properties-to-tags)](#add-properties-to-tags)

[API Configuration [13](#api-configuration)](#api-configuration)

[Cloud Deployment [15](#cloud-deployment)](#cloud-deployment)

[Prerequisites [15](#prerequisites)](#prerequisites)

[Configure the Environment [15](#configure-the-environment)](#configure-the-environment)

[Create a Build Pipeline [19](#create-a-build-pipeline)](#create-a-build-pipeline)

[Create a Release Pipeline [21](#create-a-release-pipeline)](#create-a-release-pipeline)

[On-Prem Deployment [24](#on-prem-deployment)](#on-prem-deployment)

[Prerequisites [24](#prerequisites-1)](#prerequisites-1)

[Install the Extractor [24](#install-the-extractor)](#install-the-extractor)

[Start the Extractor [26](#start-the-extractor)](#start-the-extractor)

[Stop the Extractor [27](#stop-the-extractor)](#stop-the-extractor)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including extractors, which can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT extractors are data integration accelerators that are developed to automate and ease the process of extracting data from enterprise source systems and moving it to CDF RAW. AOT's Hexagon extractor extracts Asset Hierarchy data from Hexagon (SDx) source system. It processes and transforms the extracted data to a format that Cognite recognizes before pushing that data to CDF RAW. Hexagon extractor grants users the flexibility to configure the source system (SDx) and respective Cognite details to match the Data extraction method. Main features of the Hexagon Extractor:

-   User configurable, based on the business needs

-   The timer option allows automatic operation on a configurable interval

-   Deployable for both On-Cloud and On-Premises with little user effort

-   Built-in validations and exception handling simplify the configuration

-   Supports single source system

## Purpose

This document explains how to extract data from the source system and load it into CDF RAW. It covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it either in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF.

## Target Audience

This guide is designed for use by developers with the following skills:

-   Azure Pipeline creation

-   Sonar Qube

-   Cognite Data Fusion

-   Hexagon

## Assumptions

It is assumed that the configurations described in this guide are made in the client environment. If attempting deployment in the Accenture environment, use the IP address of the server instead of the app server name to avoid issues with authentication.

## Contacts

-   

-   

## Related Links

-   [How to create an Azure Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=javascript%2Ctfs-2018-2%2Cbrowser)

-   [How to create a Release pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops)

-   [PPM Documentation (hexagonppm.com)](https://docs.hexagonppm.com/)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

# 

## Glossary

  ----------------------------------------------------------------------------------------------------------------------------------------------------
  Term                        Definition
  --------------------------- ------------------------------------------------------------------------------------------------------------------------
  Client Environment          The user's operational setting where configuration and deployment take place, separate from the Accenture environment.

  App Server Name             The network name of an application server, used for authentication and access within a given environment.

  IP Address                  A unique numerical identifier assigned to each device on a network, often used to access servers directly.

  Azure Pipeline              A set of automated processes in Azure DevOps that help build, test, and deploy code efficiently.

  Release Pipeline            An automated workflow in Azure DevOps for deploying applications to various environments after testing.

  PPM Documentation           Documentation related to Project Portfolio Management, which outlines processes, configurations, and features.

  SPFVNet Server Connection   A connection type required to access the HxGN SDx tool, established via specific network configurations.

  HxGN SDx                    A Hexagon solution for managing engineering information, assets, and data throughout their lifecycle.

  Root Certificate            A trusted digital certificate used to authenticate users and devices on a network.
  ----------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Hexagon SDx Configuration

Hexagon SDx configuration includes:

-   SPFVNet Server Connection

-   Asset Hierarchy Creation in Hexagon Server

-   Add Properties to Tags

-   Create API

## 

## SPFVNet Server Connection

To access the HxGN SDx tool, a SPFVNet Server connection is needed. Follow the steps to establish the SPFVNet connection:

-   Open PowerShell and paste the commands below and edit the username to create the root certificate.

\$cert = New-SelfSignedCertificate -Type Custom -KeySpec Signature \`

-Subject \"CN=P2SRoot[Shivani]\{.mark\}\" -KeyExportPolicy Exportable \`

> -HashAlgorithm sha256 -KeyLength 2048 \`
>
> -CertStoreLocation \"Cert:\\CurrentUser\\My\" -KeyUsageProperty Sign -KeyUsage CertSign

-   Repeat the above step and use the below commands to create a child certificate.

> New-SelfSignedCertificate -Type Custom -DnsName P2SChildCert -KeySpec Signature \`
>
> -Subject \"CN=P2SChild[Shivani]\{.mark\}\" -KeyExportPolicy Exportable \`
>
> -HashAlgorithm sha256 -KeyLength 2048 \`
>
> -CertStoreLocation \"Cert:\\CurrentUser\\My\" \`
>
> -Signer \$cert -TextExtension @(\"2.5.29.37=\{text\}1.3.6.1.5.5.7.3.2\")

-   Go to "Manage user certificates" and find newly created certificates.

> ![Certmgr showing the certificates](media/image2.png)\{width="3.271936789151356in" height="1.81878937007874in"\}

-   Right-click on the Root Certificate and select All tasks. Then, export.

-   A certificate wizard will open. Select Next. On the screen shown below, select No, do not export the private key.

> ![Certificate Export Wizard window showing the option \"No, do not export the private key\"](media/image3.png)\{width="3.8229166666666665in" height="3.0619127296587925in"\}

-   Click Next and select Base -64 encoded X.509(.CER).

> ![Certificate Export Wizard window showing the option selected \"Base-64 encoded X.509 (.CER)](media/image4.png)\{width="4.635416666666667in" height="4.461586832895888in"\}

-   Click Next and specify any folder path to save the certificates. Share the root certificate with the Hexagon infrastructure/server management team so that they will upload the certificate in the portal and provide the VPN package.

> ![Certificate Export Wizard window showing the field to enter File name.](media/image5.png)\{width="3.8628280839895015in" height="3.84375in"\}

-   

-   Navigate to Network and Internet settings and connect to SPFVnet.

> ![Screenshot showing the option to connect to SPFVnet](media/image6.png)\{width="5.796558398950131in" height="3.875009842519685in"\}

-   In the Remote Desktop Connection, provide the Server IP, username, and password. Then, click Connect.

> ![Screenshot of remote desktop connection](media/image7.png)\{width="4.035770997375328in" height="2.5567311898512686in"\}

-   In the remote desktop, launch the HxGN SDx Desktop Client.

> ![Screenshot of how to launch HXGN SDX Desktop client from Start menu](media/image8.png)\{width="6.2877602799650045in" height="3.290107174103237in"\}

-   

-   On the LOG IN page, click **New** and enter the following information:

  -----------------------------------------------------------------------
  **Field**                   **Value**
  --------------------------- -------------------------------------------
  Name                        SDxSiteServer

  Web Host                    SDxAppServer

  Web Directory               SDxSiteServer
  -----------------------------------------------------------------------

-   Check the Trusted Site box and click **OK**.

> ![HXGN SDX Dashboard Login. Fields shown are to enter Name, Web host, web directory, and the option to select Trusted site](media/image9.png)\{width="6.344628171478565in" height="3.5650109361329836in"\}

## 

## Create Asset Hierarchy on HxGN SDx

-   Open HxGN SDX Desktop Client Application.

-   Click on Create/Update Scope Tab at the bottom and select plant.

> ![Screenshot of HxGN SDX Desktop client showing the \'Create/Update Scope\' option](media/image10.png)\{width="6.479588801399825in" height="3.6621642607174105in"\}

-   To create a new Tag Type, right-click on Tag Types in the left panel and then select New Tag Type.

> ![Screenshot showing the \'New Tag Type\...\' option](media/image11.png)\{width="6.44428258967629in" height="2.0492016622922136in"\}

-   Under the new Tag Type, create new Tags and select the Parent Tag as per requirement.

> ![Screenshot showing the Parent Tag option](media/image12.png)\{width="6.470988626421697in" height="2.1709251968503938in"\}

## Add Properties to Tags

-   Open Data Validator Administration for mapping template format.



-   Select Import Mapping from the dropdown list using the Tag Create Mapping format.

> ![Import Mapping in dropdown list using Tag Create Mapping format.](media/image13.png)\{width="6.461278433945757in" height="3.4448195538057744in"\}

-   Create Sample Data input for tags and tags properties according to the above import mapping format.

-   Login with HxGN SDx Web Client by using this URL 

-   Select Load manager.

> ![Screenshot showing the Load Manager option](media/image14.png)\{width="6.395267935258093in" height="3.383507217847769in"\}

-   Select Load Tags (SDx).

> ![Screenshot showing the Load Tags (SDx) option](media/image15.png)\{width="6.408333333333333in" height="1.9559109798775154in"\}

-   

-   Add text in the Description field and then move to step 2.

> ![Screenshot showing the description field and the option to proceed to Step 2](media/image16.png)\{width="6.242725284339458in" height="3.46753937007874in"\}

-   In step 2, upload the sample input file format and then click FINISH.

-   Click Show My Load Jobs to check the status of import, validation, and export processes.

> ![Screenshot showing the option \'Show My Load Jobs\'](media/image17.png)\{width="5.862173009623797in" height="2.2953116797900264in"\}

-   Select Load Tag Properties.

> ![Screenshot showing the option \'Load Tag Properties\'](media/image18.png)\{width="5.573487532808399in" height="1.4823370516185477in"\}

-   

-   Add text in the Description field then move to step 2.

> ![Screenshot showing the description field and the option to proceed to Step 2](media/image19.png)\{width="6.465567585301837in" height="3.522286745406824in"\}

-   In step 2, upload the tag properties and then click FINISH.

> ![screenshot showing the upload of tag properties and Finish option](media/image20.png)\{width="6.84375in" height="3.2883366141732284in"\}

-   Validate output file format (design properties of tags).

> ![Output file format (design properties of tags) ](media/image21.png)\{width="8.23884186351706in" height="0.67043416447944in"\}

## 

## API Configuration

HxGN SDx provides RESTful APIs to extract data. To use these APIs, the Smart Clients URL is needed for retrieving data. This URL can be configured with the HxGN SDx Desktop Client server.

-   Log in to  and in the left panel, click on Smart Clients.

> ![Smart API Manager screenshot depicting the Smart Clients page](media/image22.png)\{width="6.127639982502187in" height="5.154422572178477in"\}

-   Create a new Smart Client for new URL Configuration (1). Enter the Smart Client's name e.g., SDXAPI (2), and click Next (3).

> ![Screenshot showing creation of new smart client](media/image23.png)\{width="6.450339020122485in" height="3.0313068678915136in"\}

-   

-   The following window and details are displayed when the smart client is successfully created:

> ![Smart Client window that opens up after naming the smart client as SDXAPI](media/image24.png)\{width="6.364548337707786in" height="3.3861931321084864in"\}

-   Click on Secret to update the secret.

> ![Screenshot showing the Secret update option](media/image25.png)\{width="6.399104330708662in" height="1.2336253280839895in"\}

-   Select Secret and copy the Client Secret Value to be used in the hexagon extractor. Then click on Next.

> ![Screenshot depicting the field to update Secret](media/image26.png)\{width="5.572501093613298in" height="1.635919728783902in"\}

# 

# Cloud Deployment

Two pipelines are needed to deploy the Flat File Extractor to an AKS Cluster. This section includes step-by-step guidance for:

-   Prerequisites that need to be fulfilled before Extractor can be deployed and used.

-   Setting up the Azure DevOps environment.

-   Creating a Build Pipeline for Dockerizing the Extractor Package.

-   Creating a Release Pipeline for deploying the Docker image to the AKS cluster.

-   Validating if the RAW table has the right data in CDF RAW.

## Prerequisites

A cloud subscription with the following:

-   Azure license/subscription to create resources for implementation

-   Azure DevOps repository for extractor code, and pipeline files

-   Azure service connections for SonarQube and Container Registry

-   Namespace in the AKS cluster for environments

-   Kubernetes Service Connection for AKS Cluster

-   Sonar project and key

## Configure the Environment

1.  Create an Azure Key Vault.

2.  Add the following secrets in the Azure Key Vault created in the previous step:

-   **ClientID**: Provide a client ID to connect to Cognite data fusion

-   **ClientSecret:** Provide a client secret to connect to Cognite data fusion

-   **HXGClientID**: Provide a client ID value generated by Smart API Manager when registering the Smart Client.

-   **HXGClientSecret**: Provide a Client Secret from the SAM authentication server.

-   **HXGResource**: Provide a registered web API resource from the SAM authentication server

> ![Create a secret window](media/image27.png)\{width="4.354166666666667in" height="3.463403324584427in"\}

3.  

4.  Create a key vault library in Azure DevOps and add the secrets created in the previous step.

> ![screenshot of variable group created for create pipeline steps](media/image28.png)\{width="4.270833333333333in" height="2.046441382327209in"\}

5.  Create a Library/Variable Group in Azure DevOps with the following parameters:

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Variable**                            **Description**
  --------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  COGNITE_HOST                            Provide the host details for Cognite data fusion

  COGNITE_PROJECT                         Provide the project name for Cognite data fusion

  SCOPES                                  Provide the scopes for Cognite data fusion

  TENANT_ID                               Provide the tenant ID for Cognite Data fusion

  HXG_CONFIG_FILENAME                     Provide the configuration filename that is used to run the extractor. The filenames are environment specific for e.g., hexagonextractor_dev_config.yaml, hexagonextractor_itest_config.yaml and hexagonextractor_prod_config.yaml

  CONTAINER_REGISTRY_SERVICE_CONNECTION   Provide container registry service connection for build and release pipeline.

  SONARQUBE_SERVICE_CONNECTION            Provide service connection for SonarQube

  HXG_ASSET_HIERARCHY_ENDPOINT            Provide endpoint to get Design parameter of tag information from SDx server

  HXG_CDF_DATABASE                        Provide the database name in CDF where the table would be created

  HXG_CDF_TABLE                           Provide a table name where asset hierarchy data will be uploaded

  HXG_GRANT_TYPE                          Provide a grant type from the SAM authentication server

  HXG_KEY_COLUMN                          Provide a column name for filtering data to upload into the CDF RAW table

  HXG_SCOPE                               Provide a Scope as the service ID from the SAM authentication server. The default value is \'ingr.api'

  HXG_TOKEN_ENDPOINT                      Provide Hexagon client request access token
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![Screenshot of variable group library created with the specified parameters](media/image29.png)\{width="6.302083333333333in" height="2.7022615923009625in"\}

6.  

7.  Navigate to the pipeline file location "Source/Extractors/HexagonExtractor/pipeline/Dev/azure-pipelines.yml" and ensure that the pipeline is referring to the libraries created in the previous steps.

> ![Specified pipeline that reflects the variable groups created in previous steps.](media/image30.png)\{width="6.407345800524935in" height="0.8280030621172354in"\}

8.  Configure the following parameters in the configuration file for the Hexagon Extractor

-   Provide timer value in seconds to schedule the extractor:

> ![Screenshot showing timer_value : 0](media/image31.png)\{width="5.78125in" height="1.1875in"\}

-   Add mandatory Cognite-related config parameters:

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

> ![Screenshot showing the parameters specified to connect to Cognite server](media/image32.png)\{width="6.291101268591426in" height="2.3603313648293964in"\}

-   

-   Add Mandatory Hexagon SDx system-related configurations:

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                      **Description**
  ---------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  hexagon_asset_hierarchy_endpoint   Use the hexagon asset hierarchy endpoint added in the Azure DevOps library in earlier steps. It is used to get the Design parameter of tag information from the SDx server.

  hexagon_token_endpoint             Use the hexagon access token from the SAM authentication server, added in the Azure DevOps library in earlier steps

  grant_type                         Use the grant type from the SAM authentication server added in the Azure DevOps library in earlier steps

  client_id                          Use the SDx client Id added in the Azure DevOps key vaults library in earlier steps. It is generated by Smart API Manager (SAM) when registering the Smart Client.

  Client_secret                      Use the SDx client secret added in the Azure DevOps key vaults library in earlier steps

  Scope                              Use the scope value from the SAM authentication server added in the Azure DevOps library in earlier steps

  Resource                           Use the resource name from the SAM authentication server added in the Azure DevOps key vaults library in earlier steps

  Key-column                         Use the unique column name present in the data added in the Azure DevOps library in earlier steps

  destination.database               Use the database name in CDF where the table would be created and added in the Azure DevOps library in earlier steps

  destination.table                  Use the table name where asset hierarchy data will be uploaded and added in the Azure DevOps library in earlier steps
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![Screenshot showing the Hexagon SDx system related configurations](media/image33.png)\{width="5.581395450568679in" height="2.14669072615923in"\}

## 

## Create a Build Pipeline

The Build Pipeline is used to Dockerize the Extractor Package. The artifacts created here are used in the release pipeline for deployment. To create a build pipeline:

1.  Navigate to Azure DevOps, select pipelines, and then select **New Pipeline**.

> ![Azure DevOps screenshot showing option to select New Pipeline](media/image34.png)\{width="6.256643700787402in" height="1.5761493875765529in"\}

2.  Select **Azure Repos Git** and select the Repository Name that contains Hexagon Extractor code and pipeline files.

> ![Screenshot highlighting \'Azure Repos Git\'](media/image35.png)\{width="6.223353018372704in" height="3.5998053368328957in"\}

3.  Select \'Existing Azure Pipelines YAML file'.

> ![Azure DevOps screenshot showing the option to select Existing Azure Pipelines YAML file.](media/image36.png)\{width="6.271726815398075in" height="3.071949912510936in"\}

4.  

5.  Select the branch and provide the pipeline file path as "Source/Extractors/HexagonExtractor/pipeline/Dev/azure-pipelines.yml" and then select Continue.

> ![Azure DevOps screenshot showing option to input pipeline file path](media/image37.png)\{width="6.219913604549431in" height="2.8378357392825895in"\}

6.  Review and save.

7.  Run the pipeline and wait for its successful completion.

> ![Screenshot showing option to Run pipeline and see its status ](media/image38.png)\{width="6.563468941382327in" height="1.4494324146981628in"\}

## Create a Release Pipeline

The Release pipeline deploys the Docker Image of Hexagon Extractor created by the build pipeline to the AKS Cluster. To create Hexagon Extractor release pipeline:

1.  Create a release pipeline with two tasks for AKS Cluster.

    -   task with delete command

    -   task with create command

2.  Update the value of the service connection for the AKS cluster in the tasks.

> ![Screenshot showing the value updated of service connection for AKS cluster in tasks](media/image39.png)\{width="6.167442038495188in" height="2.6982556867891514in"\}

3.  Update the AKS file location in the tasks.

> ![Screenshot showing the AKS file location in the tasks.](media/image40.png)\{width="6.134996719160105in" height="2.850217629046369in"\}

4.  If this is the first run, then disable the delete task from the pipeline.

> ![Screenshot showing options to enable and disable the task from the pipeline](media/image41.png)\{width="6.137774496937883in" height="3.3246281714785653in"\}

5.  Create a release from the release pipeline created in the previous step.

> ![Screenshot showing the \'Create release\' option.](media/image42.png)\{width="3.6511712598425197in" height="1.140990813648294in"\}

6.  Once the release is completed, confirm successful deployment on Azure DevOps.

> ![Screenshot showing the successful deployment on Azure DevOps.](media/image43.png)\{width="5.125909886264217in" height="3.5027055993000875in"\}

7.  Next, validate the successful deployment to the AKS cluster in the Azure portal.

> ![Screenshot showing the successful deployment to AKS cluster in Azure portal.](media/image44.png)\{width="6.353812335958005in" height="2.6474212598425195in"\}

8.  Validate Hexagon Extractor logs using the [Lens](https://k8slens.dev/) app.

> ![Screenshot of Hexagon Extractor logs in Lens app.](media/image45.png)\{width="6.431781496062992in" height="2.9479002624671917in"\}

9.  If everything looks good and AKS POD is created, enable the delete task that was previously disabled.

> ![Screenshot of Azure DevOps showing the option to enable the delete task that was previously disabled.](media/image46.png)\{width="6.320898950131234in" height="2.660044838145232in"\}

10. Validate the creation of the database and table with asset hierarchy data on the CDF Portal.

# 

# On-Prem Deployment

The HexagonExtractor Windows Service is created to give users the option of deploying the Hexagon Extractor on-premises. The HexagonExtractor Windows service is installed through a batch script that runs all the necessary commands required for the installation. Hexagon Extractor extracts asset hierarchy data from the hexagon SDx system and inserts it into CDF RAW.

## Prerequisites

-   Install Python (version 3.9 or later)

-   Install SPFVnet for accessing the Hexagon SDx system

## Install the Extractor

Follow the below steps to install Hexagon Extractor on the premise:

1.  Edit the hexagon\_**config.yaml** file to update the following:

    A.  Add the path of a log file to store extractor logs.

> ![screenshot showing path of a log file to store extractor logs.](media/image47.png)\{width="5.386792432195976in" height="1.2793635170603674in"\}

B.  Add timer value in seconds to schedule the extractor.

> ![Screenshot showing timer value in seconds to schedule the extractor.](media/image48.png)\{width="6.000002187226596in" height="1.0283016185476817in"\}

C.  Add mandatory Cognite-related details.

  ------------------------------------------------------------------------------------
  **Parameter**                   **Description**
  ------------------------------- ----------------------------------------------------
  host                            Provide the hostname for Cognite data fusion (CDF)

  project                         Provide the project name for CDF

  idp-authentication. client-id   Provide the client Id for CDF

  idp-authentication. secret      Provide the client secret for CDF

  idp-authentication. scopes      Provide the scopes for CDF

  idp-authentication. tenant      Provide the tenant Id for CDF
  ------------------------------------------------------------------------------------

D.  

E.  Add Hexagon SDx system-related configuration.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Parameter**                      **Description (as per values added to Azure DevOps library in earlier steps)**
  ---------------------------------- ------------------------------------------------------------------------------------------------------------------------------
  hexagon_asset_hierarchy_endpoint   Provide the hexagon asset hierarchy endpoint. It is used to get the Design parameter of tag information from the SDx server.

  hexagon_token_endpoint             Provide the hexagon access token from the SAM authentication server.

  grant_type                         Provide the grant type from the SAM authentication server.

  client_id                          Provide the SDx client ID. It is generated by Smart API Manager when registering the Smart Client.

  Client_secret                      Provide the SDx client secret.

  Scope                              Provide the scope value from the SAM authentication server.

  Resource                           Provide the resource name from the SAM authentication server.

  Key-column                         Provide a unique column.

  destination.database               Provide the database name in CDF where the table will be created.

  destination.table                  Provide the table name where asset hierarchy data will be uploaded.
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

> ![Screenshot showing the added Hexagon SDx system related configuration parameters](media/image49.png)\{width="6.161639326334209in" height="2.5930227471566054in"\}

2.  Edit the WSInstallation.bat file to add the absolute path of the Python folder and HexagonWindowsService.py file.

3.  To install the Hexagon Extractor on the premise, right-click on the WSInstallation.bat file and select **Run as Administrator.** It will install all the required Python modules and the Hexagon extractor as a windows service.

4.  Verify following libraries are installed correctly in the system:

    A.  pywin32 module

    B.  cognite-extractor-utils module

    C.  pythonX.dll

    D.  pythonXX.dll

    E.  pythoncomXX.dll

    F.  pywintypesXX.dll

![Screenshot showing the files copied to respective location.](media/image50.png)\{width="6.856534339457568in" height="0.9210269028871391in"\}

## Start the Extractor

1.  Click the Start button and search for "Services" and select **Run as Administrator**.

> ![Start menu showing the Services App and Run as Administrator option](media/image51.png)\{width="6.686562773403325in" height="3.4547233158355204in"\}

2.  Search for the "HexagonExtractor" service name, right-click on it, and select **Start**.

> ![Screenshot showing the Hexagon Extractor in the services window](media/image52.png)\{width="6.60863188976378in" height="1.5833180227471566in"\}

3.  Once the Hexagon Extractor starts running, check the logs in the log file on the given path in the configuration file.

4.  Validate the creation of the database and tables with asset hierarchy data on the CDF portal.

## 

## Stop the Extractor

1.  Click the Start button and search for "Services" and select **Run** **as** **Administrator**.

> ![Screenshot of Services app as searched in the Start menu showing option to Run as administrator.](media/image51.png)\{width="6.541446850393701in" height="3.379747375328084in"\}

2.  Search for the "HexagonExtractor" service name, right-click on it, and select **Stop**.

> ![Screenshot of Services showing the options to Stop the Hexagon Extractor](media/image53.png)\{width="6.6286089238845145in" height="4.1212423447069115in"\}
