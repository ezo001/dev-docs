---
sidebar_position: 2
title: AOT Twin Builder and Viewer Getting Started Auriga
---

# Getting Started with Twin Builder and Viewer

## Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including data integration extractors, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The Twin Builder application is implemented as Micro-Frontends (MFE) based on React. Twin Builder allows an admin user to create a dynamic floor layout using a Drag and Drop mechanism through a web-based user interface. The 2D schematics and 3D layouts configured in Twin Builder are viewable in Twin Viewer.

The Twin Viewer application is also implemented as an MFE based on React. Twin Viewer fetches and views 2D schematics and 3D layout content from the Twin Builder application. The visualization is augmented with information that resides in data ops platforms such as Azure or CDF (Cognite Data Fusion).

## Purpose

This document serves as a starting point for working with Twin Builder and Viewer applications. It illustrates the user journey for various roles/personas and describes the documentation available for the applications.

## Prerequisites

The prerequisites listed below are unique to the 3D and 2D components. For general prerequisites, see the [AOT Getting Started](https://industryxdevhub.accenture.com/assetdetails/75) document.

Comprehensive 3D models and 2D schematic files must exist and:

-   The 3D models should have at least one root node (parent) in the component hierarchy.

-   Pivot of the model must be at the center or bottom of the mesh.

-   The scale of the model must be set at one.

-   For the 3DCE decoupled version, the 3D model files should be available in GLB/GLTF format.

-   Uploaded models must have unique names and instances.

-   For the Model and POI mapping applications, map a model with asset hierarchy root node on the \'Model mapping\' screen.

-   Twin builder configuration users must have the \'Admin_3D\' role.

-   SVG file formats are acceptable for 2D schematics

## Related Links

-   [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [AOT Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)



-   [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Audience

-   Business Analyst

-   Solution Architect

-   Technical Architect

-   Asset Delivery teams

## Contacts

-   

-   

-   

-   

# User Journey

**3D**

The following diagram illustrates the current user journey for 3D Twin Builder and Viewer. See the [UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Twin%20_Builder_UI_Guide_2_5.pdf) for guidance on the steps of the journey.

![A diagram of a flowchart AI-generated content may be incorrect.](media/image4.png)\{width="13.297435476815398in" height="7.559857830271216in"\}

**2D**

The following diagram illustrates the current user journey for 2D Twin Builder and Viewer. See the [UI Guide](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Twin%20_Builder_UI_Guide_2_5.pdf) for guidance on the steps of the journey.

![A diagram of a flowchart AI-generated content may be incorrect.](media/image5.png)\{width="14.364274934383202in" height="7.657220034995626in"\}

# Source File Preparation

-   The 2D viewer requires SVG files as an input.

-   To ensure proper extraction, the SVG export options must be set correctly in Figma.

-   The correct configuration is shown below.

![A screenshot of a computer AI-generated content may be incorrect.](media/image6.png)\{width="14.234430227471567in" height="7.583333333333333in"\}

# 

# Resources

All documents mentioned in the table are available on the [IX Developer Hub](https://industryxdevhub.accenture.com/assetdetails/47).


| **Document** | **Description** | **Topic -- Page Number** |
| --- | --- | --- |
| [Twin Builder and Twin Viewer Architecture Blueprint](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Twin_Builder_and_Twin_Viewer_Architecture_Blueprint_2_5.pdf) | This document provides an architectural overview of the technology that powers AOT\'s Twin Builder and Twin Viewer applications. | Twin Builder Unity Application - 4 |
|  |  | Twin Viewer Unity Application -- 5 |
|  |  | 2D Schematic Viewer - 6 |
|  |  | IA and Twin Viewer Communication -- 7 |
|  |  | OH and Twin Viewer Communication -- 8 |
|  |  | Smart KPI and Twin Viewer Communication -- 9 |
|  |  | 3DCE Couple/Decouple Approach - 10 |
| AOT Twin Builder UI Guide | This document explains the features of the Twin Builder user interface. | 3D Twin Builder -- 4 |
|  |  | Launching the UI -- 4 |
|  |  | Features - 4 |
|  |  | Model Tab -- 5 |
|  |  | POI Editor Tab -- 5 |
|  |  | Mapper Tab -- 6 |
|  |  | 2D Twin Builder -- 10 |
|  |  | Launching the UI -- 10 |
|  |  | Features -- 11 |
|  |  | File Management -- 11 |
|  |  | Layout Management -- 11 |
|  |  | Error Management -11 |
|  |  | Application Tabs -- 12 |
|  |  | Files Tab -- 12 |
|  |  | Layout Tab -- 13 |
|  |  | Image POI Editor Tab - 14 |
| Twin Builder Models Tutorial | This tutorial teaches the reader how to upload, edit, and delete models directly in the Twin Builder UI. | Upload Model -- 4 |
|  |  | View Model -- 4 |
|  |  | Delete Model -- 5 |
|  |  | Upload New Version -- 5 |
| [AOT Twin Builder Plant Layout Tutorial](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Twin%20_Builder_Plant_Layout_Tutorial_2_5.pdf) | This tutorial teaches the reader how to work with plant layouts in Twin Builder. | Create Layout -- 4 |
|  |  | Place Models - 5 |
|  |  | Manipulate Models - 6 |
|  |  | Save Layout -- 7 |
|  |  | Load Layout -- 8 |
|  |  | Update Layout -- 9 |
|  |  | Delete Layout -- 10 |
|  |  | Move Camera - 11 |
| AOT Twin Viewer UI Guide | This guide assists the reader to use the Twin Viewer features. | Home Page -- 4 |
|  |  | 3D Twin Viewer UI -- 5 |
|  |  | Load Plant Layout -- 5 |
|  |  | View Layout in 3D -- 6 |
|  |  | Drill-down -- 6 |
|  |  | Points of Interest -- 7 |
|  |  | Event-driven Real-time Sync -- 8 |
|  |  | OH Communication -- 9 |
|  |  | Two-way Communication with IA -- 11 |
|  |  | Two-way Communication with Smart KPIs -- 12 |
|  |  | View 2D Schematic Layout -- 13 |
|  |  | 2D Twin Viewer UI -- 14 |
|  |  | Load Plant Layout -- 14 |
|  |  | Drill-down -- 14 |
|  |  | Batch and Product -- 15 |
|  |  | Image POI - 15 |
|  |  | Switching Layout from 2D to 3D -- 16 |
|  |  | Communication with Smart KPIs -- 17 |
|  |  | Communication with Intelligent Advisor - 17 |
| [Twin Builder and Viewer API Reference](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.5/AOT_Twin_Viewer_Builder_API_Reference_2_5.pdf) | This document serves as a reference for the APIs used in AOT\'s Twin Builder and Twin Viewer applications. | Plantlayout (GET) - 5 |
|  |  | Plantlayout (POST) -- 6 |
|  |  | Plantlayout (PATCH) -- 7 |
|  |  | Plantlayout by ID (GET) - 8 |
|  |  | Plantlayout (DELETE) - 9 |
|  |  | AssetMapping (GET) -- 10 |
|  |  | AssetMapping (POST) - 11 |
|  |  | AssetMapping Update (PATCH) - 12 |
|  |  | AssetMapping (DELETE) - 13 |
|  |  | Asset (GET) - 14 |
|  |  | Asset (POST) - 15 |
|  |  | Asset (PATCH) - 16 |
|  |  | Asset (DELETE) - 17 |
|  |  | Continuum Engine Login (GET) -- 18 |
|  |  | ModelMW (GET) - 19 |
|  |  | ModelMW(POST) - 20 |
|  |  | ModelMW (PATCH) - 21 |
|  |  | ModelMW (DELETE) - 22 |
|  |  | GRID (GET) - 23 |
|  |  | GRID by ID (GET) - 24 |
|  |  | GRID (POST) - 25 |
|  |  | GRID (PATCH) - 26 |
|  |  | GRID (DELETE) - 27 |
|  |  | POI (GET) - 28 |
|  |  | POI (POST) - 29 |
|  |  | POI Mapping (POST) - 30 |
|  |  | POI (DELETE) -- 31 |
|  |  | svgfiles (GET) -- 32 |
|  |  | svgfiles (POST) -- 33 |
|  |  | svgfiles by ID (GET) -- 34 |
|  |  | svgfiles (DELETE) -- 35 |
|  |  | linklayout (POST) - 36 |

