---
id: aot-twin-builder-and-viewer-getting-started-auriga
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

- The 3D models should have at least one root node (parent) in the component hierarchy.

- Pivot of the model must be at the center or bottom of the mesh.

- The scale of the model must be set at one.

- For the 3DCE decoupled version, the 3D model files should be available in GLB/GLTF format.

- Uploaded models must have unique names and instances.

- For the Model and POI mapping applications, map a model with asset hierarchy root node on the ‘Model mapping’ screen.

- Twin builder configuration users must have the ‘Admin_3D’ role.

- SVG file formats are acceptable for 2D schematics

## Related Links

- [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

- [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

- [AOT Resources](https://industryxdevhub.accenture.com/asset-home;search_text=aot)



- [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Audience

- Business Analyst

- Solution Architect

- Technical Architect

- Asset Delivery teams

## Contacts

- ``

- ``

- ``

- ``

## 

# User Journey

**3D**

The following diagram illustrates the current user journey for 3D Twin Builder and Viewer.

**Client Admin / ACN cons**

[Upload 3D models on the AOT ‘Models’ page by clicking ‘Upload Model’ action button.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

AOT Login

[Map 3D models with asset hierarchy (External ID) on Model Mapping screen.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

[On POI mapping page, map POIs to asset hierarchy data (External ID).](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

[Place Points of Interests (POI) on the POI Editor.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

[Create a layout on the ‘Plant Layout’ page.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_Plant_Layout_Tutorial_2_4.pdf)

Deployment Version

[Accept 3D file formats and all market leading 3D files formats.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

[Accepted 3D file formats – GLTF and GLB.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

Coupled

De-coupled

**Client Business User**

AOT Login

[Access 3D layout on clicking the pin](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[On clicking 3D toggle, the plant layout would show model mapping details.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[Drill down to the problem and analyze the performance through the layout using Insight, Actions, and KPI details](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[On clicking ‘POI’ toggle, the model mapping information pop up disappears, and POI information pop-up appears.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[The 3D globe/2D map view shows the geographical locations of the plants on Twin Viewer](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)..

**2D**

The following diagram illustrates the current user journey for 2D Twin Builder and Viewer.

**Client Business User**

AOT Login

[Access 2D layout on clicking the pin](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[On clicking the 2D frames, the user can navigate to linked SVG files or view the mapped KPI data.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[Drill down to the problem and analyze the performance through the layout using available data.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)

[On the top right, ‘Open Layout’ button navigates the user to the corresponding 3D plant layout (if available)](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)l

[The 3D globe/2D map view shows the geographical locations of the plants on Twin Viewer](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Viewer_UI_Guide_2_4.pdf)..

**Client Admin / ACN cons**

[Se](https://ts.accenture.com/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.2/AOT_Twin%20_Builder_UI_Guide_2_2.pdf)lect 2D twin on the Twin Builder [config](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.3/AOT_Twin%20_Builder_UI_Guide_2_3.pdf) component

AOT Login

[Configure 2D files from the ‘Layout’ tab.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

User can edit name of the components, map these to asset hierarchy nodes ([external](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf) ID), link them to different SVG files, map them to KPI data, etc.

[Upload 2D SVG files on the AOT ‘Files’ page by clicking ‘Upload Files’ action button.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.3/AOT_Twin%20_Builder_UI_Guide_2_3.pdf)

Link [various](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf) 2D layouts with [corresponding](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.3/AOT_Twin%20_Builder_UI_Guide_2_3.pdf) 3D layout (if available). This is 1:1 layout mapping.

Link 2D schematic boxes with PDF, Image or 3D layouts.

[Upload 2D Image/PDF files on the AOT ‘Files’ page by clicking ‘Upload Files’ action button.](https://ts.accenture.com/:b:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/AOT%202.4/AOT_Twin%20_Builder_UI_Guide_2_4.pdf)

# Source File Preparation

- The 2D viewer requires SVG files as an input.

- To ensure proper extraction, the SVG export options must be set correctly in Figma.

- The correct configuration is shown below.



# Resources

All documents mentioned in the table are available on the [IX Developer Hub](https://industryxdevhub.accenture.com/assetdetails/47).







``

``
Document
Description
Topic – Page Number
``
``

``
Twin Builder and Twin Viewer Architecture Blueprint
This document provides an architectural overview of the technology that powers AOT’s Twin Builder and Twin Viewer applications.
`Twin Builder Unity Application - 4`
Twin Viewer Unity Application - 5
IA and Twin Viewer Communication – 6
OH and Twin Viewer Communication – 7
`Smart KPI and Twin Viewer Communication – 8`
3DCE Couple/Decouple Approach - 9
Authentication - 10
``
``
AOT Twin Builder UI Guide
This document explains the features of the Twin Builder user interface.
`3D Twin Builder – 4`
Launching the UI – 4
Features - 4
Model Tab – 5
POI Editor Tab – 5
Mapper Tab - 6
`2D Twin Builder – 10`
Launching the UI – 10
Features – 11
File Management – 11
Layout Management – 11
Error Management -11
Application Tabs – 12
Files Tab – 12
Layout Tab – 13
``
``
Twin Builder Models Tutorial
This tutorial teaches the reader how to upload, edit, and delete models directly in the Twin Builder UI.
`Upload Model - 4`
Model List - 5
`View Model - 6`
Upload New Version - 7
``
``
AOT Twin Builder Plant Layout Tutorial
This tutorial teaches the reader how to work with plant layouts in Twin Builder.
`Plant Layout – 4`
Create Layout – 4
Place Models - 5
Manipulate Models - 6
Save Layout - 7
`Load Layout – 8`
Update Layout – 9
Delete Layout – 10
Move Camera - 11
``
``
AOT Twin Viewer UI Guide
This guide assists the reader to use the Twin Viewer features.
`Home Page – 4`
3D Twin Viewer UI – 5
Load Plant Layout – 5
View Layout in 3D – 6
Drill-down – 6
Entity Viewer – 7
Points of Interest – 7
Event-driven Real-time Sync – 8
Two-way Communication with IA – 11
Two-way Communication with Smart KPIs – 12
View 2D Schematic Layout - 13
`2D Twin Viewer UI – 14`
Load Plant Layout – 14
Drill-down – 14
Switching Layout from 2D to 3D – 15
Communication with Smart KPIs - 16
``
``
Twin Builder and Viewer API Reference
This document serves as a reference for the APIs used in AOT’s Twin Builder and Twin Viewer applications.
`Plantlayout (GET) - 5`
Plantlayout (POST) – 6
Plantlayout (PATCH) – 7
Plantlayout by ID (GET) - 8
Plantlayout (DELETE) - 9
AssetMapping (GET) – 10
AssetMapping (POST) - 11
AssetMapping Update (PATCH) - 12
AssetMapping (DELETE) - 13
Asset (GET) - 14
Asset (POST) - 15
Asset (PATCH) - 16
Asset (DELETE) - 17
Continuum Engine Login (GET) - 18
`ModelMW (GET) - 19`
ModelMW(POST) - 20
ModelMW (PATCH) - 21
ModelMW (DELETE) - 22
GRID (GET) - 23
GRID by ID (GET) - 24
GRID (POST) - 25
GRID (PATCH) - 26
GRID (DELETE) - 27
POI (GET) - 28
POI (POST) - 29
POI Mapping (POST) - 30
POI (DELETE) - 31
``
``
``
