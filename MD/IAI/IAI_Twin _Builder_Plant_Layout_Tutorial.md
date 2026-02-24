---
sidebar_position: 2
title: IAI Twin  Builder Plant Layout Tutorial
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">Twin Builder Plant Layout</p>
<p class="doc-type">TUTORIAL</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / Twin Builder and Viewer |
| **Domain / Area** | Digital Twin / Visual monitoring and alerts |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya, Rane, Chetankumar |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [[Summary - Overview]](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Twin Builder UI Guide |

</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools that can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes. 

The Twin Builder application is implemented as Micro-Frontends (MFE) based on React. Twin Builder allows an admin user to create a dynamic floor layout using a Drag and Drop mechanism through a web-based user interface. The 3D visuals created in Twin Builder are viewable in Twin Viewer.

### Purpose

This tutorial teaches the reader how to work with plant layouts in Twin Builder.

### Prerequisites

-   Twin Builder application must be deployed.

-   A compatible browser (Google Chrome or Microsoft Edge) must be installed.

### Target Audience

-   IAI End Users

-   Plant Designers

-   Client IT Admins

### Contact

-   [rishabh.b.joshi@accenture.com](mailto:anobika.roy@accenture.com)

-   [chetankumar.rane@accenture.com](mailto:chetankumar.rane@accenture.com)

### Related Links

-   [IAI on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [IAI on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

-   [IAI Documents](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

### Glossary


| Term | Definition |
| --- | --- |
| Plant Layout | The arrangement of equipment, machinery and assets within a plant, represented visually in a grid for design and management purposes. |
| Asset List | A catalogue of available models or items that can be placed within the plant layout grid. |
| Model | A digital representation of equipment or asset that can be placed on the plant layout grid. |
| Grid | The visual structure of tiles used to organize and position models within the plant layout. |
| Tile | An individual cell within the grid, used as a location for placing models. |


## Create Layout

To create a new plant layout or update an existing layout, open the \'Plant Layout\' tab from the header.

Select a plant from the plant selection dropdown.

[]\{#_Toc218772047 .anchor\}

## Place Models 

Click on the Add button to get the asset list. On the center panel, you will get a model list. Select a model and then right click on the grid cell to place the selected model.

![Plant Layout tab showing the selected model](./media/IAI_Twin%20_Builder_Plant_Layout_Tutorial/image3.png)

On the grid, click on a model to open the edit menu. The menu opens at the left side of the screen and enables navigation to various features which are described in the table below. Click the video on the right for a brief demo.


| **Feature** | **Description** |
| --- | --- |
| Move Asset | This option is used for moving assets from one block to another block. |
| Tile Size | This option is used to show what Tile Size we have set while placing the assets. |
| Rotate Asset | This option gives the user the ability to rotate the asset by different degrees with respect to the Y--axis. |
| Asset Map | This option helps to select the POI mapping version with the respective selected model. |
| Linking 2D Layout | This option provides a list of 2D layouts associated with the selected plant ID, which can be linked to corresponding 3D assets. |
| Connections | This creates a connection between the assets. The user can specify the connection name. |
| Delete Asset | This option is used to remove assets from the grid. |
| Close Menu | This option is used to close the menu. ![Thumbnail image for Manipulate Models Video](./media/IAI_Twin%20_Builder_Plant_Layout_Tutorial/image5.png)
[]\{#_Toc218772049 .anchor\} |

## Save Layout

Use the *Save* button located in the top right corner to save the newly created layout.

![Plant Layout page showing the Save option](./media/IAI_Twin%20_Builder_Plant_Layout_Tutorial/image6.png)

## 

# Load Layout

Using the *Select a Layout* dropdown, the user can load the created layouts. Click on the layout name to load the layout. Once the layout is loaded, the keyboard\'s arrow keys can be used to move the layout left, right, forward, and backward.

![UI showing the Generate Layout side menu bar and the grid](./media/IAI_Twin%20_Builder_Plant_Layout_Tutorial/image7.png)

## 

# Update Layout

Once the layout is loaded, the user can edit the layout as needed. Clicking on the *Update* option updates the changes made to an existing layout.

Note: If no models are left to add and no space is available on the layout, the Add button will be disabled.

## 

# Move Camera

The A, D, W, and S keys on the keyboard can be used to move the camera angle upwards, downwards, or sideways. The mouse wheel can be used to zoom in and out. By holding the left-click button and moving the cursor, the layout can be rotated.


| **Key** | **Action** |
| --- | --- |
| A | move right |
| D | move left |
| W | move forward |
| S | move backward ![Thumbnail image for Move Camera video](./media/IAI_Twin%20_Builder_Plant_Layout_Tutorial/image10.png)
|  |
