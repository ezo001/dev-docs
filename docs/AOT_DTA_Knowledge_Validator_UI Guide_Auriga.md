---
id: aot-dta-knowledge-validator-ui-guide-auriga
title: AOT DTA Knowledge Validator UI Guide Auriga
---

**Accenture Operations Twin**

**Knowledge Validator**

**UI GUIDE**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|:---|:---|
| **Asset / Solution Name** | Accenture Operations Twin / Knowledge Validation Agent |
| **Domain / Area** | Digital Twin / Gen AI |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Zoltani, Judit-Kinga |
| **Status** | Draft / In Progress |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | DTA Expert Knowledge Architecture Blueprint |

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contact [3](#contact)](#contact)

[Related Links [3](#zainab.asgar.aliaccenture.comrelated-links)](#zainab.asgar.aliaccenture.comrelated-links)

[Glossary [3](#glossary)](#glossary)

[Background [4](#background)](#background)

[Intelligent Advisor [4](#intelligent-advisor)](#intelligent-advisor)

[People Management [4](#people-management)](#people-management)

[Recommendation Generation [5](#recommendation-generation)](#recommendation-generation)

[Intelligent Advisor Panel [5](#intelligent-advisor-panel)](#intelligent-advisor-panel)

[Digital Twin Assistant [5](#digital-twin-assistant)](#digital-twin-assistant)

[Usage [6](#usage)](#usage)

[Access [6](#access)](#access)

[Configuration [6](#configuration)](#configuration)

[Details [7](#details)](#details)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

## Purpose

This guide explains how to use Expert Knowledge functionality in AOT. It covers the following:

- Capturing and documenting expert knowledge

- Validating the submissions

- Reviewing and approving entries

- Accessing validated knowledge within AOT’s Recommendation Framework

##  Target Audience

- Plant Manager

- Maintenance personnel

- Business Analyst

- End users of AOT

## Prerequisites

- Familiarity with the AOT application

- Access to the Intelligent Advisor application

- Validator_ExpertKnowledge role must be assigned to the user to view and configure Expert Knowledge

## Contact

- ``

- 

- 

## `zainab.asgar.ali@accenture.comRelated` Links

- [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

- [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| **Term** | **Definition** |
|----|----|
| AOT | Accenture Operations Twin |
| DTA | Digital Twin Assistant – a chatbot feature in AOT that answers templatized queries |
| IA | Intelligent Advisor |
| Expert Knowledge | It is the text and image based specialized insights, experience, or best practices contributed by domain experts. |
| Knowledge Validator | A user interface within the AOT application to approve/reject the expert knowledge. |
| Validator_ExpertKnowledge | A designated admin role responsible for reviewing, approving, or rejecting submitted expert knowledge entries. |
| Generate Recommendation | A button used to generate recommendations based on approved expert knowledge related to similar insights. |

# Background

The Knowledge Validator UI is one part of AOT’s Expert Knowledge component, which integrates human expertise with AI scalability to optimize productivity and support informed decision-making. This feature allows users to systematically capture, validate, and reuse expert insights within the AOT platform. Submissions are assessed by the Knowledge Validation Agent and then reviewed by an appointed human Validator. Upon successful validation, these insights become part of AOT’s Recommendation Framework, which delivers actionable guidance for comparable scenarios and fosters continuous operational improvement. The Expert Knowledge component provides a comprehensive process for capturing, documenting, and disseminating valuable operational insights, facilitating the preservation and application of effective solutions and best practices for future use across similar contexts. The following sections describe how other AOT components are involved with Expert Knowledge.

## 

## Intelligent Advisor

Intelligent Advisor (IA) users can submit expert knowledge during the closure of an Insight. When closing an insight, the Expert Knowledge tab appears in the edit panel where the details of an insight are entered. Once a user submits expert knowledge from the Edit Insight panel, the information undergoes an automated validation process handled by the Knowledge Validation Agent. The agent evaluates the submitted content based on the following parameters:

- Toxicity

- Clarity

- Professionalism

- Action Oriented

If an image is provided, the agent also generates a short description of it. After the evaluation, the entry is placed in pending state, ready for review by a designated admin user. This ensures that all submitted knowledge entries meet quality standards before becoming part of AOT’s recommendation framework.

In the Edit Insight window in the Intelligent Advisor app, the Expert Knowledge tab allows users to record details about how the issue was identified and resolved, thereby creating a knowledge entry linked to the specific operational context. Within this tab, users can:

- Enter a Title and Description summarizing the learning or the resolution approach.

- Optionally upload an Image to visually support or enhance the explanation.

- Choose to include related actions associated with the insight for a more complete representation of the resolution process.

After the information is submitted, the entry is automatically sent for validation. Knowledge can be captured only at closing the insight. Once it is submitted, it will be sent to validation.

##  People Management

To be able to configure the Expert Knowledge Validation page and serve as a Validator the human user must possess the Validator_ExpertKnowledge role. Users associated with the dedicated Validator_ExpertKnowledge role are responsible for reviewing submitted entries. Only users assigned this role have access to the Knowledge Validator Configuration page that is specially designed for reviewing and managing expert knowledge submissions.

Within this application, the validator can view all details submitted by the user, along with the validation scores generated by the knowledge Validation Agent. The validator reviews the content to determine whether the information is accurate, relevant and useful for solving operational issues. Based on the assessment, the validator can take either of the two actions:

- Approve- The entry can be approved if it meets all validation criteria and provides useful insights.

- Reject- The entry should be rejected if it is incomplete, unclear or not relevant.

This structured review process ensures that only high quality, validated expert knowledge becomes part of AOT’s knowledge base, enabling reliable and actionable recommendations for future use.

## 

## 

## Recommendation Generation

The Recommendation Generation feature enables AOT users to leverage captured and validated Expert Knowledge to receive actionable guidance for resolving similar operational insights by using past learnings.

Users can update or capture new expert knowledge, ad-hoc, anytime. Once Expert Knowledge is captured and validated, it becomes available for generating recommendations for insights that belong to the same template from which the knowledge was originally recorded. This process can be initiated in two ways—through the IA panel and via the Digital Twin Assistant.

The component UIs indicate recommendation availability as follows:

- Once a recommendation is generated, the *Generate Recommendation* button becomes inactive.

- If no validated recommendation is available, the button remains inactive, and on hovering over the icon, a tooltip displays *Not Available*.

- If the validation is still pending approval, the button remains inactive, and on hovering over the icon, a tooltip displays *Pending*.

This ensures that only validated and relevant expert knowledge is used for recommendations, enhancing the operational excellence within AOT.

###  Intelligent Advisor Panel

Intelligent Advisor users can go to Recommendations and click on *Generate Recommendation* to retrieve relevant expert knowledge entries associated with similar insights.



###  Digital Twin Assistant

When using the Digital Twin Assistant (DTA), users can click on the *Generate Recommendation* icon under the relevant insight and retrieve the recommendation from validated expert knowledge by clicking on dropdown button to expand and view the full recommendation details and use More/Less option for concise or detailed visibility.



### 

# Usage

## Access

The Knowledge Validator is accessed from the side menu bar of AOT.



##  Configuration

When the Knowledge Validator is launched, the Expert Knowledge Validation page is loaded.

The page is organized into three tabs for efficient management of approvals:

| **Tab**  | **Purpose**                                       |
|----------|---------------------------------------------------|
| Pending  | Displays entries awaiting approval.               |
| Approved | Lists of entries that were reviewed and accepted. |
| Rejected | shows entries that were reviewed and declined.    |

Each tab provides key details for every expert knowledge entry, including:

- Knowledge Title

- Date of Submission

- Knowledge Provider

- Approver

- Date of Approval

- Link to the Expert Knowledge Detail



## Details

Clicking the Details link displays the pending date, the related insight, the knowledge provider, and any images included in the submission, as well as options to reject and approve the submission.


