---
id: aot-twin--builder-models-tutorial-auriga
title: AOT Twin  Builder Models Tutorial Auriga
---

**Accenture Operations Twin**

**Twin Builder Models**

**TUTORIAL**

Release Version: 2.5

**Metadata Table**

| **Field** | **Value** |
|:---|:---|
| **Asset / Solution Name** | Accenture Operations Twin / Twin Builder and Viewer |
| **Domain / Area** | Digital Twin / Visual monitoring and alerts |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya, Rane, Chetankumar |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Twin Builder UI Guide |



**Contents**

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Contact [3](#contact)](#contact)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#aot-documentsglossary)](#aot-documentsglossary)

[Working with Models [4](#working-with-models)](#working-with-models)

[Upload Model [4](#upload-model)](#upload-model)

[Delete Model [5](#delete-model)](#delete-model)

[Upload New Version [5](#upload-new-version)](#upload-new-version)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT’s Twin Builder application is implemented as Micro-Frontends (MFE) based on React. Twin Builder allows an admin user to create a dynamic floor layout using a Drag and Drop mechanism through a web-based user interface. The 3D visuals created in Twin Builder are viewable in Twin Viewer.

AOT has two versions- decoupled and coupled. In the decoupled version, only AOT models are used, and they are stored in the AOT space. In the coupled version, both 3DCE models and AOT models are used, and the models are stored on the 3DCE tenant. Additionally, the coupled version has a 3D model conversion feature which allows converting fbx, obj, and CAD files to glb.

## Purpose

This tutorial teaches the reader how to upload, edit, and view models directly in the Twin Builder UI.

## Contact

- [`chetankumar.rane@accenture.com`](mailto:`chetankumar.rane@accenture.com`)

- ``

## Target Audience

- AOT End Users

- Plant Designers

- Client IT Admins

## Prerequisites

- Twin Builder application must be deployed.

- The client should have 3D models (files) available to upload.

- The 3D model component hierarchy should have one root node (parent).

- The 3D models should have good rotational angle and scaling aspects.

- A compatible browser (Google Chrome or Microsoft Edge) must be installed.

## Related Links

- [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

- [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

- 

## [AOT Documents](https://industryxdevhub.accenture.com/asset-home;search_text=aot)Glossary

| Term | Definition |
|----|----|
| 3D Model | A digital representation of a physical object in three dimensions, used for visualization and analysis. |
| GLTF/GLB | File formats commonly used for 3D models; GLTF is JSON-based, and GLB is its binary version. |
| Root Node (Parent) | The top-most node in a 3D model’s hierarchy, serving as the parent to all other nodes. |
| Rotational Angle | The orientation or spin applied to a 3D model along its axes. |
| Scaling | The process of resizing a 3D model to fit specific dimensions or proportions. |
| Tag Field | The area in the application where the selected plant or object is displayed. |

# 

# Working with Models

The following pages explain how to upload, search, and view models.

## Upload Model

1.  Select a plant from the drop-down menu in the upper-right corner of the application.

2.  Put a title for the model to be uploaded.

3.  Confirm that the selected plant is shown in the *Tag* field.

4.  Upload a model in the valid file format (GLTF, GLB) and upload a thumbnail image.

5.  Click the *UPLOAD MODEL* option at the bottom of the dialog window to upload a model.

If the same model is required for a different use, then upload a copy of the model and save it with a different name. Avoid duplicate names for ease of use and identification.

Note that the model’s name must not exceed 25 characters.

**View Model**

Click on the tile that represents the new model to see a 3D view of the model. This page includes controls that can be used to upload a new version or switch to a different version.



## 

## Delete Model

To delete a model, click on the Delete button. To delete all versions of the model, click on the Delete All button.

There are certain validations made before the model is deleted, which are as follows.

- If POIs are added to the Model, then the model cannot be deleted until all POIs are deleted.

- If the Model is mapped using either Model Mapper or POI Mapper application, then the model cannot be deleted until the mapping is deleted.

- If a Model is placed in any layout, then it cannot be deleted until the layout is deleted.



## Upload New Version

1.  To upload a new version of this model, Click on *UPLOAD NEW*. A new dialog window opens to upload the new version.



2.  Confirm that the selected plant is shown in the *Tag* field

3.  

4.  Update the fields and click on the *Update New Version* option.



5.  When the model update is complete, the user can view the list of versions in the drop-down menu and select a version to view it in the window.


