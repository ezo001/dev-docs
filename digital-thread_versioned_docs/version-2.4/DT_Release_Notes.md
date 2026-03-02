---
sidebar_position: 2
title: DT Release Notes
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Digital Thread Foundations</p>
<p class="doc-topic">&amp;gt; **Release 1.2**</p>
<p class="doc-type">&amp;gt;</p>
</div>
> **RELEASE NOTES**
>
> Release Version: 1.2

<div class="metadata-for-agents" aria-hidden="true">
Metadata Table


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Digital Thread |
| **Domain / Area** | Engineering |
| **Owner (Team/Person)** | Karthik Ramachandra |
| **Reviewers** | Karthik Ramachandra |
| **Status** | Approved / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [link](https://dev.azure.com/IXAssets/IXAssetsProject/\_git/ixassets) |
| **Related Assets / Alternatives** | AOT / Engineering Orchestration / Engineering Agents |
</div>

## Introduction 

Industry X Digital Thread Foundations delivers industry-agnostic building blocks that create a virtualization layer over connected products, operations, and services. It provides a communication framework that connects different systems across the product lifecycle, enabling seamless data sharing and driving improvements in industrial and manufacturing processes. IX Digital Thread goes beyond data exchange to provide end-to-end, asset-relevant information that enhances efficiency and business value.

The 1.2 release introduces flexible, industry-agnostic building blocks that create a virtualization layer across connected products, operations, and services. It features improved Bill of Material (BOM) management through a structured and efficient workflow for converting Engineering BOMs (EBOMs) into Manufacturing BOMs (MBOMs) in batch. The conversion ensures accurate transformation of engineering data into manufacturable formats, with full traceability and version control. The comparison feature provides precise data analysis across systems, highlights discrepancies with full traceability.

The new Data Quality Check feature allows users to define quality checkpoints based on their preferences to ensure the accuracy and reliability of data throughout the digital thread. Additionally, the new Digital Thread Dashboard offers comprehensive management access and insights into the entire digital thread ecosystem.

### ** **Purpose

This document describes new features and enhancements to IX Digital Thread Foundations as part of the 1.2 release.

### Target Audience

-   Asset Delivery Teams

-   Stakeholders, Solution Architects, Technical Architects

### Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [laura.mosconi@accenture.com](mailto:laura.mosconi@accenture.com)

-   [karthik.ramachandra@accenture.com](mailto:karthik.ramachandra@accenture.com)

-   [vamsi.konambhotla@accenture.com](mailto:vamsi.konambhotla@accenture.com)

-   [riju.dhar@accenture.com](mailto:riju.dhar@accenture.com)

### Related Links 

-   [Microsoft Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/)

-   [IX Digital Thread Foundations Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=ix%20digital%20thread)

-   [IX Digital Thread BOM Documentation](https://industryxdevhub.accenture.com/assetdetails/115)

## 

# New Features and Enhancements

### 

## BOM Management UI Enhancements

-   A new search-driven BOM interface has been implemented to enable users to quickly locate, convert (single or batch), and compare BOMs from one unified entry point, significantly reducing navigation time.

-   Navigation and layout of the application have been enhanced to improve usability and overall user experience.

### BOM Conversion and Comparison

-   Batch BOM conversion is now available using configurable rules and templates, ensuring consistent and accurate BOM transformations at scale.

-   The application is now equipped with a high-fidelity BOM comparison engine that identifies differences and commonalities with full traceability, powered by Flink for streaming use cases and Java for processing.

-   Detailed comparison insights are now enabled in the application to support engineering change analysis and decision-making.

-   BOM conversion and comparison workflows now are intuitive with minimal manual steps, thus improving user productivity.

### BOM Data Quality Check 

BOM Data Quality Check feature is now available in the application. The functionality is based on a customizable framework allowing users to define and enforce quality checkpoints tailored to their business rules.

### Digital Thread Monitoring

-   A **Digital Thread Dashboard** is now available as part of the BOM management application. The dashboard provides a unified, real-time view of the entire digital thread ecosystem, including BOMs, integrations, and KPIs.

-   The **Monitoring Dashboard** has been enhanced to:

    -   Track BOM conversion and comparison status end-to-end.

    -   Display processing states, comments, and review feedback.

    -   Enable collaborative issue resolution and traceability.

###  Connected Systems

-   MBSE--PLM integration is implemented using CDC to ensure accurate, duplicate-free requirement synchronization with correct attribute mapping.

-   ALM--PLM synchronization has been done to maintain consistent requirement flow between systems with real-time updates.

-   PM--ALM triggering is implemented to automatically create Jira tasks when new Polarion requirements are added, thus improving traceability and developer visibility.

### Hybrid BOM Automation

Hybrid BOM automation is now implemented, which accelerates generation of manufacturing-ready BOMs by automatically merging EBOMs (from TC) with Design BOMs (from NX):

### Time-Series KPIs 

Implemented real-time KPI pipelines using Apache Flink to process streaming data and visualize raw versus transformed metrics for performance insights.

### App Config Network

Introduced the App Config Network, a flexible configuration framework enabling tailored IX Digital Thread deployments across multiple domains and use cases, aligned to specific business requirements.
