---
sidebar_position: 2
title: AOT DTA Expert Knowledge Architecture Auriga
---

**Accenture Operations Twin**

**DTA- Expert Knowledge**

**ARCHITECTURE AND IMPLEMENTATION**

Release Version: 2.5

**Metadata Table**

  -------------------------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -------------------------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / AOT

  **Domain / Area**                   Digital Twin / Architecture

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       [Horodinca]\{.underline\}, Florin and Takó, István

  **Status**                          Draft / In Progress

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [[Summary - Overview]\{.underline\}](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   
  -------------------------------------------------------------------------------------------------------------------------------

![](media/image2.png)\{width="1.0277777777777777in" height="1.0694444444444444in"\}

# ![](media/image3.png)\{width="0.9888888888888889in" height="1.023611111111111in"\} \{#section .TOC-Heading\}

**Contents**

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Business Contacts [3](#business-contacts)](#business-contacts)

[Technical Contacts [3](#technical-contacts)](#technical-contacts)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Cloud Resources [3](#cloud-resources)](#cloud-resources)

[Deployment [3](#deployment)](#deployment)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Expert Knowledge Submission Architecture [4](#submission)](#submission)

[Validation Agent Workflow [5](#validation)](#validation)

[Reviewer workflow- Approve/Reject [7](#review)](#review)

[Recommendation Generation [8](#recommendations)](#recommendations)

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including Digital Twin Assistant, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Expert Knowledge is a functionality of the Digital Twin Assistant (DTA) designed to capture and preserve knowledge about the suggestions and actions taken to resolve various issues. This enables the system to provide relevant recommendations, assisting users in effectively addressing similar issues in future.

## Purpose

This document explains the architecture and integration of the Expert Knowledge framework within the AOT application. It outlines how expert insights are captured, validated using AI-generated scores and utilized for recommendation as part of AOT\'s Generative AI recommendation framework.

## Target Audience

Software architects, developers, and integrators with IT backgrounds.

## Business Contacts

-   

-   [judit-kinga.zoltani@accenture.com](file:///C:/Users/zainab.asgar.ali/Downloads/judit-kinga.zoltani@accenture.com)

## Technical Contacts

-   florin.horodinca@accenture.com

##  Prerequisites

-   Python 3.10

-   Install the libraries provided in requirements file from the repository

-   Azure Repository Access

## Cloud Resources

  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Resource**          **Function**
  --------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  Azure OpenAI          LLM models used are gpt-4o, text-embedding-3-small

  Azure Cosmos DB:      Collections created are graphql_queries(to store query and question mapping), user_chat_history(to store context history)

  AI Search:            A vector database to store the embeddings of the unstructured documents (with semantic-ranker enabled)

  Storage account:      A container to store the queries and unstructured docs.

  Function app:         A HTTP trigger-based function to facilitate the ingestion of queries to cosmos and unstructured docs to AI Search (whenever required)

  Kubernetes Service:   To deploy the GenAI Implementation API
  -------------------------------------------------------------------------------------------------------------------------------------------------------------

## Deployment

The docker file and the CI/CD pipeline are available in AOT\'s-Azure repo. The resource group APIs and connection strings in the pipeline variable group library must be updated before deploying to the environment.

## Related Links

-   [Data processing Repo](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_git/AOT-Azure?path=/Ingestion/GenAI-Functionapp)



-   [GenAI API Repo](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_git/AOT-Azure?path=/Consumption/DataAccess/GenAI/GenAIQueryAPI/genai_middleware/genai_ms/app/gen_ai)

## Glossary

  -------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**             **Definition**
  -------------------- ----------------------------------------------------------------------------------------------------------------------------------
  Function App         A serverless compute service that enables running event-triggered code, such as processing HTTP requests for data ingestion.

  Kubernetes Service   A platform for deploying, scaling, and managing containerized applications, used here for GenAI Implementation API.

  Docker File          A text document containing instructions to build a Docker container image for application deployment.

  CI/CD Pipeline       Automated processes for continuous integration and delivery, facilitating code building, testing, and deployment.

  Cosmos DB            A globally distributed NoSQL database service used for storing application data such as insights and submissions.

  Blob Storage         Azure\'s object storage solution for storing unstructured data, such as uploaded images.

  Expert Knowledge     Information submitted by users detailing how an insight was resolved, often linked with recommendations and supporting data.

  Insight              An actionable observation or recommendation generated by the system, which may trigger expert knowledge submission upon closure.

  Validation Agent     An automated system that assesses the submitted expert knowledge for parameters like toxicity and clarity.

  GenAI API            An interface for interacting with generative AI models, typically deployed via Kubernetes Service in this architecture.
  -------------------------------------------------------------------------------------------------------------------------------------------------------

# 

# Submission

Expert knowledge can be submitted when a user closes an Insight. At that moment, a new tab appears where a Title can be provided together with the details of how that insight was resolved. Additionally, an image can be uploaded to enhance the information.\
The expert knowledge data is linked to Insight template based on these keys:

-   Type

-   Theme

-   Sub-type

-   PlantId

When a recommendation is generated, it will be stored on the expert knowledge object, meaning it will be available for all insights belonging to the same template.

The following diagram shows this flow:

![The Expert Knowledge Diagram illustrates the process of submitting new expert knowledge within the Intelligent Advisor system. On the left, the Intelligent Advisor Insight Details Application, built with Angular as a micro-frontend, allows users to submit new expert knowledge. In the center, the Intelligent Advisor Microservice, implemented using Azure Kubernetes and Python, exposes APIs to provide access to insights and actions based on roles. On the right, two backend components are shown: Expert Knowledge Image Storage, hosted on Microsoft Azure Blob, which stores uploaded expert knowledge images, and AOT Intelligent Advisor Data, implemented with Azure Cosmos DB, which stores data belonging to Intelligent Advisor. The workflow includes three steps: first, new expert knowledge is submitted via HTTP; second, the backend saves the new expert knowledge data and stores related images; and third, a validation agent is triggered for the submitted expert knowledge using Kafka Topic. A legend at the bottom right explains system boundaries and highlights AOT Intelligent Advisor and AOT DataOps components.](media/image4.png)\{width="13.487917760279965in" height="6.271142825896763in"\}

# Validation 

## Agent Workflow

Once the user submits the knowledge from Intelligent Advisor Details Application, the information is saved in Intelligent Advisor database (Cosmos DB) in a draft state. If an image has been provided, it is stored in blob storage. At that moment, the submitted information must be validated by the validation agent, which will return a scoring result for each of these parameters:

-   Toxicity

-   Clarity

-   Professionalism

-   Action-Oriented

To do this, IA microservice will generate a message on a Kafka topic with the necessary information that needs to be validated, and the GenAI microservice will take it and invoke the Validation Agent. The message received contains information needed to identify the sender service so that the result can be sent to the right one. The agent will take the information received and will validate it. If any image is provided, it will generate a brief description of it.\
The Expert Knowledge Validation Agent is instructed to return the response in a JSON object format that has these fields:

\{

\'clarity\': \{

\'value\': \'X/5\',

\'description\': \'xyz\'

\},

\'professionalism\': \{

\'value\': \'X/5\',

\'description\': \'xyz\'

\},

\'action_oriented\': \{

\'value\': \'X/5\',

\'description\': \'xyz\'

\},

\'toxicity\': \{

\'value\': \'X/1\',

\'description\': \'xyz\'

\},

\'summary\': \'xyz\',

\'error\': \'\'

\}

The *error* field will contain a description of the errors encountered during validation (i.e. the image description could not be generated).

Once the agent finishes the validation, the result will be sent back to the Kafka topic and IA microservice will pick it up and update the relevant Expert Knowledge with the score data and will also put it in \"Pending\" state. This means the data is ready to be reviewed by a reviewer person.

![The Expert Knowledge Diagram illustrates the validation and scoring process for Intelligent Advisor. On the left, GenAI Agents perform various tasks, including downloading images for validation and calling the OpenAI LLM model to process provided information. At the top, the OpenAI LLM component is shown as the model used for performing tasks. In the center, the Intelligent Advisor Microservice, built on Azure Kubernetes using Python, exposes APIs to provide access to insights and actions based on roles. Below it, the Expert Knowledge Image Storage, hosted on Microsoft Azure Blob, stores uploaded expert knowledge images. On the right, the AOT Intelligent Advisor Data component, implemented with Azure Cosmos DB, stores data belonging to Intelligent Advisor. The workflow includes four steps: downloading the image for validation, calling the LLM, returning expert knowledge scoring, and updating the scoring in the backend. A legend at the bottom right explains system boundaries and highlights AOT Intelligent Advisor and AOT DataOps components.](media/image5.png)\{width="12.616452318460192in" height="8.18008639545057in"\}

# Review

## Human Reviewer Workflow

The review can be done in a new application dedicated for reviewing Expert Knowledge. The user can see all the information that was submitted along with the validation result from the agent. It will then decide if all the information is relevant and can be used to solve the issues and will act on it: it will approve or reject the expert knowledge. The following diagram shows this process:

![The Expert Knowledge Diagram illustrates the review and update process for Intelligent Advisor. On the left, the Expert Knowledge Review Application, built with Angular as a micro-frontend, provides reviewers the ability to approve or reject submitted expert knowledge. In the center, the Intelligent Advisor Microservice, implemented using Azure Kubernetes and Python, exposes APIs that allow access to insights and actions based on user roles. On the right, the AOT Intelligent Advisor Data component, hosted in Azure Cosmos DB, stores data belonging to the Intelligent Advisor. The workflow shows two steps: first, expert knowledge is approved or rejected via HTTP, and second, the status of the expert knowledge is updated in the backend. A legend at the bottom right explains system boundaries and highlights AOT Intelligent Advisor and AOT DataOps components.](media/image6.png)\{width="11.239944225721786in" height="4.880637576552931in"\}

# Recommendations

The captured and validated expert knowledge can be used to generate recommendation for Insights belonging to the same template of which it was captured. This can be done through the Insight details application/window, or through the Digital Twin Assistant when information about the isights is requested. The flow can be seen in the following diagram:\
Once the user clicks on the button to generate recommendation, the IA service will send a kafka message with required information to GenAI microservice. It is instructed to rely only on the provided information to generate a recommendation which will be sent back to IA microservice through kafka topic, where it will be saved on the expert knowledge object.

![Expert Knowledge Diagram showing system interactions for Intelligent Advisor. The diagram includes five main components: OpenAI LLM (top), GenAI Agents (left), Expert Knowledge Image Storage (center), Intelligent Advisor Microservice (bottom center), and AOT Intelligent Advisor Data (right). Arrows indicate data flow: GenAI Agents call the LLM and download image recommendations, trigger recommendation generation, and interact with the microservice. The microservice exposes APIs for insights and actions, stores recommendations in a database, and fetches required information from AOT Intelligent Advisor Data. The UI component, Intelligent Advisor Insight Details Application, is shown at bottom left. A legend at the bottom right explains system boundaries and external systems.](media/image7.png)\{width="10.729587707786527in" height="7.182155511811024in"\}
