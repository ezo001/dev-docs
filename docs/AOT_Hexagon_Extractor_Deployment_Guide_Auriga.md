---
id: aot-hexagon-extractor-deployment-guide-auriga
title: AOT Hexagon Extractor Deployment Guide Auriga
---

**Accenture Operations Twin**

Hexagon Extractor

**DEPLOYMENT GUIDE**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|:---|:---|
| **Asset / Solution Name** | Accenture Operations Twin / Data Integration Accelerators |
| **Domain / Area** | Extractors / Data Processing |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Joshi, Rishabh |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | AOT Extractors Architecture Blueprint, AOT Extractors Getting Started |

# 

# 

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Assumptions [3](#assumptions)](#assumptions)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [4](#glossary)](#glossary)

[Hexagon SDx Configuration [4](#hexagon-sdx-configuration)](#hexagon-sdx-configuration)

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

#  Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including extractors, which can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT extractors are data integration accelerators that are developed to automate and ease the process of extracting data from enterprise source systems and moving it to CDF RAW. AOT’s Hexagon extractor extracts Asset Hierarchy data from Hexagon (SDx) source system. It processes and transforms the extracted data to a format that Cognite recognizes before pushing that data to CDF RAW. Hexagon extractor grants users the flexibility to configure the source system (SDx) and respective Cognite details to match the Data extraction method. Main features of the Hexagon Extractor:

- User configurable, based on the business needs

- The timer option allows automatic operation on a configurable interval

- Deployable for both On-Cloud and On-Premises with little user effort

- Built-in validations and exception handling simplify the configuration

- Supports single source system

## Purpose

This document explains how to extract data from the source system and load it into CDF RAW. It covers the prerequisites for deploying the Extractor and provides step-by-step instructions for configuring and deploying it either in the cloud or on-premises. After reading the document, a developer should be able to configure and run the Extractor and verify the data flow from the source system to CDF.

## Target Audience

This guide is designed for use by developers with the following skills:

- Azure Pipeline creation

- Sonar Qube

- Cognite Data Fusion

- Hexagon

## Assumptions

It is assumed that the configurations described in this guide are made in the client environment. If attempting deployment in the Accenture environment, use the IP address of the server instead of the app server name to avoid issues with authentication.

## Contacts

- ``

- ``

## Related Links

- [How to create an Azure Pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/create-first-pipeline?view=azure-devops&tabs=javascript%2Ctfs-2018-2%2Cbrowser)

- [How to create a Release pipeline](https://docs.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops)

- [PPM Documentation (hexagonppm.com)](https://docs.hexagonppm.com/)

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

# 

## Glossary

| Term | Definition |
|----|----|
| Client Environment | The user’s operational setting where configuration and deployment take place, separate from the Accenture environment. |
| App Server Name | The network name of an application server, used for authentication and access within a given environment. |
| IP Address | A unique numerical identifier assigned to each device on a network, often used to access servers directly. |
| Azure Pipeline | A set of automated processes in Azure DevOps that help build, test, and deploy code efficiently. |
| Release Pipeline | An automated workflow in Azure DevOps for deploying applications to various environments after testing. |
| PPM Documentation | Documentation related to Project Portfolio Management, which outlines processes, configurations, and features. |
| SPFVNet Server Connection | A connection type required to access the HxGN SDx tool, established via specific network configurations. |
| HxGN SDx | A Hexagon solution for managing engineering information, assets, and data throughout their lifecycle. |
| Root Certificate | A trusted digital certificate used to authenticate users and devices on a network. |

# Hexagon SDx Configuration

Hexagon SDx configuration includes:

- SPFVNet Server Connection

- Asset Hierarchy Creation in Hexagon Server

- Add Properties to Tags

- Create API

## 

## SPFVNet Server Connection

To access the HxGN SDx tool, a SPFVNet Server connection is needed. Follow the steps to establish the SPFVNet connection:

- Open PowerShell and paste the commands below and edit the username to create the root certificate.

`\>` \$cert = New-SelfSignedCertificate -Type Custom -KeySpec Signature \`
`\>`
`\>` -Subject "CN=P2SRootShivani" -KeyExportPolicy Exportable `
`\>`
`\>` -HashAlgorithm sha256 -KeyLength 2048 \`
`\>`
`\>` -CertStoreLocation "Cert:\CurrentUser\My" -KeyUsageProperty Sign -KeyUsage CertSign

- Repeat the above step and use the below commands to create a child certificate.

`\>` New-SelfSignedCertificate -Type Custom -DnsName P2SChildCert -KeySpec Signature \`
`\>`
`\>` -Subject "CN=P2SChildShivani" -KeyExportPolicy Exportable `
`\>`
`\>` -HashAlgorithm sha256 -KeyLength 2048 \`
`\>`
`\>` -CertStoreLocation "Cert:\CurrentUser\My" \`
`\>`
`\>` -Signer \$cert -TextExtension @("2.5.29.37=`{text}`1.3.6.1.5.5.7.3.2")

- Go to “Manage user certificates” and find newly created certificates.

`\>` 

- Right-click on the Root Certificate and select All tasks. Then, export.

- A certificate wizard will open. Select Next. On the screen shown below, select No, do not export the private key.

`\>` 

- Click Next and select Base -64 encoded X.509(.CER).

`\>` 

- Click Next and specify any folder path to save the certificates. Share the root certificate with the Hexagon infrastructure/server management team so that they will upload the certificate in the portal and provide the VPN package.

`\>` 

- 

- Navigate to Network and Internet settings and connect to SPFVnet.

`\>` 

- In the Remote Desktop Connection, provide the Server IP, username, and password. Then, click Connect.

`\>` 

- In the remote desktop, launch the HxGN SDx Desktop Client.

`\>` 

- On the LOG IN page, click **New** and enter the following information:

| **Field**     | **Value**     |
|---------------|---------------|
| Name          | SDxSiteServer |
| Web Host      | SDxAppServer  |
| Web Directory | SDxSiteServer |

- Check the Trusted Site box and click **OK**.

`\>` 

## 

## Create Asset Hierarchy on HxGN SDx

- Open HxGN SDX Desktop Client Application.

- Click on Create/Update Scope Tab at the bottom and select plant.

`\>` 

- To create a new Tag Type, right-click on Tag Types in the left panel and then select New Tag Type.

`\>` 

- Under the new Tag Type, create new Tags and select the Parent Tag as per requirement.

`\>` 

## Add Properties to Tags

- Open Data Validator Administration for mapping template format.



- Select Import Mapping from the dropdown list using the Tag Create Mapping format.

`\>` 

- Create Sample Data input for tags and tags properties according to the above import mapping format.

- Login with HxGN SDx Web Client by using this URL 

- Select Load manager.

`\>` 

- Select Load Tags (SDx).

`\>` 

- 

- Add text in the Description field and then move to step 2.

`\>` 

- In step 2, upload the sample input file format and then click FINISH.

- Click Show My Load Jobs to check the status of import, validation, and export processes.

`\>` 

- Select Load Tag Properties.

`\>` 

- 

- Add text in the Description field then move to step 2.

`\>` 

- In step 2, upload the tag properties and then click FINISH.

`\>` 

- Validate output file format (design properties of tags).

`\>` 

## 

## API Configuration

HxGN SDx provides RESTful APIs to extract data. To use these APIs, the Smart Clients URL is needed for retrieving data. This URL can be configured with the HxGN SDx Desktop Client server.

- Log in to  and in the left panel, click on Smart Clients.

`\>` 

- Create a new Smart Client for new URL Configuration (1). Enter the Smart Client’s name e.g., SDXAPI (2), and click Next (3).

`\>` 

- 

- The following window and details are displayed when the smart client is successfully created:

`\>` 

- Click on Secret to update the secret.

`\>` 

- Select Secret and copy the Client Secret Value to be used in the hexagon extractor. Then click on Next.

`\>` 

# 

# Cloud Deployment

Two pipelines are needed to deploy the Flat File Extractor to an AKS Cluster. This section includes step-by-step guidance for:

- Prerequisites that need to be fulfilled before Extractor can be deployed and used.

- Setting up the Azure DevOps environment.

- Creating a Build Pipeline for Dockerizing the Extractor Package.

- Creating a Release Pipeline for deploying the Docker image to the AKS cluster.

- Validating if the RAW table has the right data in CDF RAW.

## Prerequisites

A cloud subscription with the following:

- Azure license/subscription to create resources for implementation

- Azure DevOps repository for extractor code, and pipeline files

- Azure service connections for SonarQube and Container Registry

- Namespace in the AKS cluster for environments

- Kubernetes Service Connection for AKS Cluster

- Sonar project and key

## Configure the Environment

1.  Create an Azure Key Vault.

2.  Add the following secrets in the Azure Key Vault created in the previous step:

- **ClientID**: Provide a client ID to connect to Cognite data fusion

- **ClientSecret:** Provide a client secret to connect to Cognite data fusion

- **HXGClientID**: Provide a client ID value generated by Smart API Manager when registering the Smart Client.

- **HXGClientSecret**: Provide a Client Secret from the SAM authentication server.

- **HXGResource**: Provide a registered web API resource from the SAM authentication server

`\>` 

3.  

4.  Create a key vault library in Azure DevOps and add the secrets created in the previous step.

`\>` 

5.  Create a Library/Variable Group in Azure DevOps with the following parameters:

| **Variable** | **Description** |
|----|----|
| COGNITE_HOST | Provide the host details for Cognite data fusion |
| COGNITE_PROJECT | Provide the project name for Cognite data fusion |
| SCOPES | Provide the scopes for Cognite data fusion |
| TENANT_ID | Provide the tenant ID for Cognite Data fusion |
| HXG_CONFIG_FILENAME | Provide the configuration filename that is used to run the extractor. The filenames are environment specific for e.g., hexagonextractor_dev_config.yaml, hexagonextractor_itest_config.yaml and hexagonextractor_prod_config.yaml |
| CONTAINER_REGISTRY_SERVICE_CONNECTION | Provide container registry service connection for build and release pipeline. |
| SONARQUBE_SERVICE_CONNECTION | Provide service connection for SonarQube |
| HXG_ASSET_HIERARCHY_ENDPOINT | Provide endpoint to get Design parameter of tag information from SDx server |
| HXG_CDF_DATABASE | Provide the database name in CDF where the table would be created |
| HXG_CDF_TABLE | Provide a table name where asset hierarchy data will be uploaded |
| HXG_GRANT_TYPE | Provide a grant type from the SAM authentication server |
| HXG_KEY_COLUMN | Provide a column name for filtering data to upload into the CDF RAW table |
| HXG_SCOPE | Provide a Scope as the service ID from the SAM authentication server. The default value is ‘ingr.api’ |
| HXG_TOKEN_ENDPOINT | Provide Hexagon client request access token |

`\>` 

6.  

7.  Navigate to the pipeline file location “Source/Extractors/HexagonExtractor/pipeline/Dev/azure-pipelines.yml” and ensure that the pipeline is referring to the libraries created in the previous steps.

`\>` 

8.  Configure the following parameters in the configuration file for the Hexagon Extractor

- Provide timer value in seconds to schedule the extractor:

`\>` 

- Add mandatory Cognite-related config parameters:

| **Parameter** | **Description** |
|:---|:---|
| host | Use the hostname for Cognite data fusion (CDF) added in the Azure DevOps library in earlier steps |
| project | Use the project name for CDF added in the Azure DevOps library in earlier steps |
| idp-authentication. client-id | Use the client Id for CDF added in the Azure DevOps key vault library in earlier steps |
| idp-authentication. secret | Use the client secret for CDF added in the Azure DevOps key vault library in earlier steps |
| idp-authentication. scopes | Use the scopes for CDF added in the Azure DevOps library in earlier steps |
| idp-authentication. tenant | Use the tenant Id for CDF added in the Azure DevOps library in earlier steps |

`\>` 

- 

- Add Mandatory Hexagon SDx system-related configurations:

| **Parameter** | **Description** |
|----|----|
| hexagon_asset_hierarchy_endpoint | Use the hexagon asset hierarchy endpoint added in the Azure DevOps library in earlier steps. It is used to get the Design parameter of tag information from the SDx server. |
| hexagon_token_endpoint | Use the hexagon access token from the SAM authentication server, added in the Azure DevOps library in earlier steps |
| grant_type | Use the grant type from the SAM authentication server added in the Azure DevOps library in earlier steps |
| client_id | Use the SDx client Id added in the Azure DevOps key vaults library in earlier steps. It is generated by Smart API Manager (SAM) when registering the Smart Client. |
| Client_secret | Use the SDx client secret added in the Azure DevOps key vaults library in earlier steps |
| Scope | Use the scope value from the SAM authentication server added in the Azure DevOps library in earlier steps |
| Resource | Use the resource name from the SAM authentication server added in the Azure DevOps key vaults library in earlier steps |
| Key-column | Use the unique column name present in the data added in the Azure DevOps library in earlier steps |
| destination.database | Use the database name in CDF where the table would be created and added in the Azure DevOps library in earlier steps |
| destination.table | Use the table name where asset hierarchy data will be uploaded and added in the Azure DevOps library in earlier steps |

`\>` 

## 

## Create a Build Pipeline

The Build Pipeline is used to Dockerize the Extractor Package. The artifacts created here are used in the release pipeline for deployment. To create a build pipeline:

1.  Navigate to Azure DevOps, select pipelines, and then select **New Pipeline**.

`\>` 

2.  Select **Azure Repos Git** and select the Repository Name that contains Hexagon Extractor code and pipeline files.

`\>` 

3.  Select ‘Existing Azure Pipelines YAML file’.

`\>` 

4.  Select the branch and provide the pipeline file path as “Source/Extractors/HexagonExtractor/pipeline/Dev/azure-pipelines.yml” and then select Continue.

`\>` 

5.  Review and save.

6.  Run the pipeline and wait for its successful completion.

`\>` 

## Create a Release Pipeline

The Release pipeline deploys the Docker Image of Hexagon Extractor created by the build pipeline to the AKS Cluster. To create Hexagon Extractor release pipeline:

1.  Create a release pipeline with two tasks for AKS Cluster.

    - task with delete command

    - task with create command

2.  Update the value of the service connection for the AKS cluster in the tasks.

`\>` 

3.  Update the AKS file location in the tasks.

`\>` 

4.  If this is the first run, then disable the delete task from the pipeline.

`\>` 

5.  Create a release from the release pipeline created in the previous step.

`\>` 

6.  Once the release is completed, confirm successful deployment on Azure DevOps.

`\>` 

7.  Next, validate the successful deployment to the AKS cluster in the Azure portal.

`\>` 

8.  Validate Hexagon Extractor logs using the [Lens](https://k8slens.dev/) app.

`\>` 

9.  If everything looks good and AKS POD is created, enable the delete task that was previously disabled.

`\>` 

10. Validate the creation of the database and table with asset hierarchy data on the CDF Portal.

# 

# On-Prem Deployment

The HexagonExtractor Windows Service is created to give users the option of deploying the Hexagon Extractor on-premises. The HexagonExtractor Windows service is installed through a batch script that runs all the necessary commands required for the installation. Hexagon Extractor extracts asset hierarchy data from the hexagon SDx system and inserts it into CDF RAW.

## Prerequisites

- Install Python (version 3.9 or later)

- Install SPFVnet for accessing the Hexagon SDx system

## Install the Extractor

Follow the below steps to install Hexagon Extractor on the premise:

1.  Edit the hexagon\_**config.yaml** file to update the following:

    1.  Add the path of a log file to store extractor logs.

`\>` 

2.  Add timer value in seconds to schedule the extractor.

`\>` 

3.  Add mandatory Cognite-related details.

| **Parameter** | **Description** |
|:---|:---|
| host | Provide the hostname for Cognite data fusion (CDF) |
| project | Provide the project name for CDF |
| idp-authentication. client-id | Provide the client Id for CDF |
| idp-authentication. secret | Provide the client secret for CDF |
| idp-authentication. scopes | Provide the scopes for CDF |
| idp-authentication. tenant | Provide the tenant Id for CDF |

4.  

5.  Add Hexagon SDx system-related configuration.

| **Parameter** | **Description (as per values added to Azure DevOps library in earlier steps)** |
|:---|:---|
| hexagon_asset_hierarchy_endpoint | Provide the hexagon asset hierarchy endpoint. It is used to get the Design parameter of tag information from the SDx server. |
| hexagon_token_endpoint | Provide the hexagon access token from the SAM authentication server. |
| grant_type | Provide the grant type from the SAM authentication server. |
| client_id | Provide the SDx client ID. It is generated by Smart API Manager when registering the Smart Client. |
| Client_secret | Provide the SDx client secret. |
| Scope | Provide the scope value from the SAM authentication server. |
| Resource | Provide the resource name from the SAM authentication server. |
| Key-column | Provide a unique column. |
| destination.database | Provide the database name in CDF where the table will be created. |
| destination.table | Provide the table name where asset hierarchy data will be uploaded. |

`\>` 

2.  Edit the WSInstallation.bat file to add the absolute path of the Python folder and HexagonWindowsService.py file.

3.  To install the Hexagon Extractor on the premise, right-click on the WSInstallation.bat file and select **Run as Administrator.** It will install all the required Python modules and the Hexagon extractor as a windows service.

4.  Verify following libraries are installed correctly in the system:

    1.  pywin32 module

    2.  cognite-extractor-utils module

    3.  pythonX.dll

    4.  pythonXX.dll

    5.  pythoncomXX.dll

    6.  pywintypesXX.dll



## Start the Extractor

1.  Click the Start button and search for “Services” and select **Run as Administrator**.

`\>` 

2.  Search for the “HexagonExtractor” service name, right-click on it, and select **Start**.

`\>` 

3.  Once the Hexagon Extractor starts running, check the logs in the log file on the given path in the configuration file.

4.  Validate the creation of the database and tables with asset hierarchy data on the CDF portal.

## 

## Stop the Extractor

1.  Click the Start button and search for “Services” and select **Run** **as** **Administrator**.

`\>` 

2.  Search for the “HexagonExtractor” service name, right-click on it, and select **Stop**.

`\>` 
