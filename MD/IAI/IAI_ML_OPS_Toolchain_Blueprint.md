---
sidebar_position: 2
title: IAI ML OPS Toolchain Blueprint
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">ML OPS Toolchain Blueprint</p>
<p class="doc-type">ARCHITECTURE AND INTEGRATION</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / Intelligent Advisor |
| **Domain / Area** | Advisory / Decision Automation |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Zoltani, Judit-Kinga, Kumar Singh, Rajnish |
| **Status** | Published / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [[Summary - Overview]](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Intelligent Advisor UI Guide, Intelligent Advisor Delivery Guide ![](./media/IAI_ML_OPS_Toolchain_Blueprint/image2.png)
|  |

</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools, including Intelligent Advisor, which can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

IAI Intelligent Advisor can be integrated with Azure MLOps to unlock AI use cases such as predictive maintenance. IAI can run machine learning models that have been deployed on Azure ML Studio. IAI can include the flow of data preparation, model training, evaluation, registration, and deployment of the ML model in Azure MLOps. Additionally, IAI can include the flow for vendor-trained ML Models and deploy them in Azure MLOps.

### Target Audience

-   Client Delivery Teams Leveraging IAI Intelligent Advisor

-   Asset Delivery Teams

-   Solution Architects, Technical Architects, Data Scientists, Data Engineers

### Purpose

This document provides an overview of the Azure machine learning infrastructure and describes how to integrate it with IAI\'s Intelligent Advisor framework.

### Prerequisites

-   A Business Analyst (BA) must be engaged by the IAI team to define the requirements.

-   A customized spreadsheet must be provided by the BA for creation of the hierarchies described later in this document.

-   Access to code is required.

### Contact

-   [rajnish.kumar.singh@accenture.com](mailto:rajnish.kumar.singh@accenture.com)

-   [florin.horodinca@accenture.com](mailto:florin.horodinca@accenture.com)

-   [judit-kinga.zoltani@accenture.com](mailto:judit-kinga.zoltani@accenture.com)

### Related Links

-   [Cognite Documentation](https://docs.cognite.com/cdf/air/)

-   [Release Notes](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Shared%20Documents/Released%20Documentation/Accenture%20Operations%20Twin%20(AOT)/1.0/Release%20Notes%20-%20AOT%201.0.pdf?csf=1&amp;web=1&amp;e=d4cjke)

-   [IAI Architecture Documents](https://industryxdevhub.accenture.com/assetdetails/53)

###  Glossary


| **Term** | **Definition** |
| --- | --- |
| IAI (Industrial AI Foundation) | A suite of software accelerators and tools designed to integrate product, process, and live data from diverse IT and OT systems, providing a contextualized view of operations to enhance decision-making and optimize processes. |
| Intelligent Advisor | An accelerator within IAI that can be integrated with Azure MLOps to enable advanced AI use cases, such as predictive maintenance. |
| Azure MLOps | A set of practices and tools on Microsoft Azure that streamline the lifecycle of machine learning models, including data preparation, training, evaluation, registration, and deployment. |
| Azure ML Studio | A cloud-based environment in Azure for building, training, and deploying machine learning models. |
| MLOps | The discipline combining machine learning, DevOps, and data engineering to automate and monitor the entire ML lifecycle. |
| DevOps | A set of practices that combines software development and IT operations to shorten the development lifecycle and deliver high-quality software continuously. |
| Workflow Pipeline | The sequence of processes involved in preparing data, training, evaluating, registering, and deploying machine learning models. |
| Vendor-trained ML Models | Machine learning models developed and trained by external vendors, which can be integrated and deployed within Azure MLOps. |
| Client Delivery Teams | Teams responsible for delivering solutions to clients using IAI Intelligent Advisor. |
| Asset Delivery Teams | Teams focused on delivering and managing assets, potentially leveraging IAI and machine learning solutions. |
| Solution Architect | A professional who designs comprehensive technical solutions, including integrating IAI Intelligent Advisor with Azure MLOps. |
| Technical Architect | A specialist who determines the technical requirements and architecture for implementing solutions using IAI and Azure MLOps. |
| Data Scientist | A practitioner who builds machine learning models and leverages data analytics within the IAI and Azure ML framework. |
| Data Engineer | An expert responsible for preparing and managing data flows, supporting machine learning processes in IAI and Azure MLOps. |
| Predictive Maintenance | An AI-driven use case enabled by integrating IAI Intelligent Advisor with Azure MLOps, focusing on forecasting asset failures to optimize maintenance schedules. |
| IT and OT Systems | Information Technology (IT) and Operational Technology (OT) systems, whose data integration is a central feature of IAI. |

## 

# Background

### 

## MLOps Design Patterns

Design patterns are a set of best practices and reusable solutions used to combat several common problems that occur in data science and software development. Azure MLOps Design patterns categorize the most commonly occurring problems and provide various blueprints to easily recognize and solve them.

###  What is MLOps Azure

MLOps Azure is a machine learning engineering culture and practice that aims at unifying ML system development (Dev) and ML system operation (Ops). It applies DevOps principles and practices such as continuous integration, delivery, and deployment to the machine learning process, with an aim for faster experimentation, development, and deployment of Azure ML models into production and test environments. MLOps is a set of processes designed to transform experimental Machine Learning models into production services ready to make decisions in the real world. MLOps can:

-   Create reproducible ML pipelines.

-   Improve time to market via faster deployments.

-   Increase model robustness.

-   Provide more flexibility to train and compare different ML models.

-   Create reusable software environments.

-   Register, package, and deploy models from anywhere.

-   Automate the end-to-end ML lifecycle with Azure Machine Learning and Azure Pipelines.

###  MLOps Versus DevOps

MLOps is based on the same principles as DevOps, but with an additional focus on data validation and continuous training and evaluation. The differences between the two are outlined below.

#### DevOps

-   Code components are tested and validated.

-   The focus is on specific software.

-   The model is not monitored.

-   Handles code versioning.

-   Allows software reuse only.

#### MLOps

-   Data and models are tested along with code components.

-   The focus includes the entire ML pipeline and system.

-   The deployed model is constantly monitored with Azure Monitor.

-   Handles data/model versioning.

-   Allows model reuse by retraining models.

### 

# Architecture

The diagram below illustrates how IAI Intelligent Advisor is integrated with MLOps for an AI application using Azure DevOps and Azure Machine Learning. The orange block provides the context for ML Ops in the diagram.

![Diagram AOT Intelligent Advisor, which generates business insights, surrounded by Operator, Intelligent Advisor Configurator, AOT 3D Visualizer, AOT Reporting, AOT DataOps, AOT Smart KPIs, AOT People Management, AOT Operations Hierarchy, SAP PM, and ML Ops. Arrows indicate data flow and interactions between these elements and the central advisor.](./media/IAI_ML_OPS_Toolchain_Blueprint/image3.jpg)

The following points describe how the ML Ops functions in executing the ML model:

-   The user saves the configuration for the model from the IAI Intelligent Advisor UI. The configuration defines necessary parameters such as data source identifier, equipment, frequency of trigger, etc.

-   ML Model execution can be triggered in IAI with Scheduler or from an external system. The scheduler creates the process to trigger and run the model (the deployed ML algorithm) at the configured frequency.

-   The input data to run the ML Model is taken from Azure (blob, data lake, DB, etc.) or the CDF time series.

-   The model microservice from IAI Intelligent Advisor utilizes the deployed ML Model endpoint from Azure MLOps.

-   ML Model output is processed and saved according to the business requirements.

##### 

## Methods to Consume ML Model

IAI provides the UI to configure model parameters such as frequency to trigger, equipment, and data input identifiers. ML models can be scheduled to run with a configured frequency. Output from the deployed ML model is processed and used according to the business logic. The following table describes the model types that can be deployed.


| **Model Type 1** | **Model Type 2** | **Model Type 3** |
| --- | --- | --- |
| 1. IAI can already deploy the vendor model directly into IA. | 1. The model is deployed in Azure ML Studio. | 1. The model is deployed in Azure ML Studio. |
| 2. The model microservice from IA invokes the handler for the model when the configuration is saved from the IAI UI. | 2. The model microservice deployed in the IAI framework invokes the handler for Model type 2 when the configuration is saved from the IAI UI. | 2. The model microservice deployed in the IAI framework invokes the handler for Model type 3 when the configuration is saved from the IAI UI. |
| 3. The handler checks the model configuration, retrieves the data from the IAI knowledge graph, and pre-processes it. | 3. The handler checks the model configuration, retrieves the data from the IAI knowledge graph, and pre-processes it. | 3. The handler checks the data identifier from the model configuration and sends it to the ML Model engine deployed in Azure MLops. |
| 4. The pre-processed data is sent as input to the in-memory model engine, which is the ML model (pkl) file directly deployed in Kubernetes with the docker in the IAI IA framework. | 4. The pre-processed data is sent to the ML Model deployed on Azure MLOps. | 4. The ML Model engine fetches the data from the IAI Knowledge graph and uses it as input. |


The figure below depicts the ML model execution scenarios. Click on the image for an enlarged view.

![Flowchart titled \'ADT ML model execution architecture\' showing how an external system triggers machine learning model execution via a data model microservice connected to Azure Digital Twins. The microservice routes data to model-specific handlers and an in-memory ML engine, which processes and returns results. Machine learning models are trained and deployed for scoring. Arrows indicate data flow between components.](./media/IAI_ML_OPS_Toolchain_Blueprint/image4.png)

### MLOps Workflow Pipeline

> ![Flowchart showing five steps in a machine learning model lifecycle: data preprocessing, training, evaluation, registration, and deployment. A feedback loop labeled \'re-train trigger\' connects back to training, indicating continuous improvement.](./media/IAI_ML_OPS_Toolchain_Blueprint/image5.png)
As diagrammed above, Machine Learning (ML) projects are constructed by several different steps. They are described in the following table:


| **Step** | **Description** |
| --- | --- |
| Data Pre-processing | Data preparation (cleaning, transformation, etc.), data versioning, and data registration to Azure MLOps. |
| Train Model | Run training code/algorithm and output a model file. |
| Evaluate Model | Compare the performance of the newly trained model with the model in production. If the new model performs better than the production model, the following steps are executed. If not, they will be skipped. |
| Register Model | Take the best model and register it with the Azure ML Model registry, which allows version-control. |
| Deploy Model | Deploy the registered model on Azure MLOps as an endpoint. |


### Operationalization of the MLOps Model

This architecture describes how continuous integration (CI), continuous delivery (CD), and retraining pipelines are implemented for an AI application using Azure DevOps and Azure Machine Learning.

-   The ML model is packaged and validated using the Azure ML CLI.

-   Once the ML model is registered, Azure ML + Azure DevOps is used to deploy it.

-   A release definition can be defined in Azure Pipelines to help coordinate a release. Using the DevOps extension for Machine Learning as well as artifacts from Azure ML, Azure Repos, and GitHub can be included as part of the Release Pipeline.

-   In the release definition, we can leverage the Azure ML CLI\'s model deploy command to deploy the Azure ML model to the cloud (ACI or AKS).

![A flowchart illustrating the operationalization of a machine learning model using Azure DevOps and Azure Machine Learning. It begins with an Azure DevOps build pipeline triggered by new code, running data sanity and unit tests. One-time setup steps include creating a machine learning workspace and compute, and publishing the ML pipeline. Triggers---data-driven, schedule-driven, and metrics-driven---initiate the pipeline from Azure Storage. The ML pipeline trains, evaluates, and registers the model, which is managed by AML Model Management. The Azure DevOps release pipeline handles staging and QA by packaging the model into an image, deploying it on Azure Container Instances (ACI), and testing it. Production deployment uses Azure Kubernetes Service (AKS). Both environments include monitoring via Application Insights and scoring services. Arrows show data flow from Azure Storage through testing and deployment stages.](./media/IAI_ML_OPS_Toolchain_Blueprint/image6.png)
