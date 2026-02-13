---
sidebar_position: 2
title: AOT Twin  Builder Plant Layout Tutorial Auriga
---

Accenture Operations Twin

Twin Builder Plant Layout

TUTORIAL

Release Version: 2.5

**Metadata Table**

  -------------------------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -------------------------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin / Twin Builder and Viewer

  **Domain / Area**                   Digital Twin / Visual monitoring and alerts

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Susarla, Aditya, Rane, Chetankumar

  **Status**                          Published / Complete

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [[Summary - Overview]\{.underline\}](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   Twin Builder UI Guide
  -------------------------------------------------------------------------------------------------------------------------------

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#section)](#section)

[Purpose [3](#purpose)](#purpose)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Target Audience [3](#target-audience)](#target-audience)

[Contact [3](#contact)](#contact)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Create Layout [4](#create-layout)](#create-layout)

[Place Models [5](#_Toc218772047)](#_Toc218772047)

[Manipulate Models [6](#section-1)](#section-1)

[Save Layout [7](#_Toc218772049)](#_Toc218772049)

[Load Layout [8](#section-2)](#section-2)

[Update Layout [9](#section-3)](#section-3)

[Delete Layout [10](#section-4)](#section-4)

[Move Camera [11](#section-5)](#section-5)

# 

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes. 

The Twin Builder application is implemented as Micro-Frontends (MFE) based on React. Twin Builder allows an admin user to create a dynamic floor layout using a Drag and Drop mechanism through a web-based user interface. The 3D visuals created in Twin Builder are viewable in Twin Viewer.

## Purpose

This tutorial teaches the reader how to work with plant layouts in Twin Builder.

## Prerequisites

-   Twin Builder application must be deployed.

-   A compatible browser (Google Chrome or Microsoft Edge) must be installed.

## Target Audience

-   AOT End Users

-   Plant Designers

-   Client IT Admins

## Contact

-   [rishabh.b.joshi@accenture.com](mailto:anobika.roy@accenture.com)

-   

## Related Links

-   [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

-   [AOT Documents](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

## Glossary

  ------------------------------------------------------------------------------------------------------------------------------------------------------
  Term           Definition
  -------------- ---------------------------------------------------------------------------------------------------------------------------------------
  Plant Layout   The arrangement of equipment, machinery and assets within a plant, represented visually in a grid for design and management purposes.

  Asset List     A catalogue of available models or items that can be placed within the plant layout grid.

  Model          A digital representation of equipment or asset that can be placed on the plant layout grid.

  Grid           The visual structure of tiles used to organize and position models within the plant layout.

  Tile           An individual cell within the grid, used as a location for placing models.
  ------------------------------------------------------------------------------------------------------------------------------------------------------

# Create Layout

To create a new plant layout or update an existing layout, open the \'Plant Layout\' tab from the header.

Select a plant from the plant selection dropdown.

Enter a unique name for the layout (Min 3 and Max 25 characters (Alphanumeric, \_ only)), select the size of the layout, and then click the Generate Layout button to create a layout of the selected size.

Click on the \'Select A Layout\' dropdown to select and open an existing layout on the grid.

![Thumbnail image for Create Layout Video](media/image2.png)\{width="6.692390638670166in" height="3.9085411198600175in"\}

[]\{#_Toc218772047 .anchor\}

# Place Models 

Click on the Add button to get the asset list. On the center panel, you will get a model list. Select a model and then right click on the grid cell to place the selected model.

![Plant Layout tab showing the selected model](media/image3.png)\{width="6.65913823272091in" height="3.5208333333333335in"\}

![Asset list](media/image4.png)\{width="3.3854166666666665in" height="5.478540026246719in"\}

If the layout has no tiles available for placing models or if all models are placed but tiles remain, the Add button will be disabled with a note.

# 

# Manipulate Models

On the grid, click on a model to open the edit menu. The menu opens at the left side of the screen and enables navigation to various features which are described in the table below. Click the video on the right for a brief demo.

  ------------------------------------------------------------------------------------------------------------------------------------------------------
  **Feature**         **Description**
  ------------------- ----------------------------------------------------------------------------------------------------------------------------------
  Move Asset          This option is used for moving assets from one block to another block.

  Tile Size           This option is used to show what Tile Size we have set while placing the assets.

  Rotate Asset        This option gives the user the ability to rotate the asset by different degrees with respect to the Y--axis.

  Asset Map           This option helps to select the POI mapping version with the respective selected model.

  Linking 2D Layout   This option provides a list of 2D layouts associated with the selected plant ID, which can be linked to corresponding 3D assets.

  Connections         This creates a connection between the assets. The user can specify the connection name.

  Delete Asset        This option is used to remove assets from the grid.

  Close Menu          This option is used to close the menu.
  ------------------------------------------------------------------------------------------------------------------------------------------------------

![Thumbnail image for Manipulate Models Video](media/image5.png)\{width="6.5in" height="3.4923611111111112in"\}[]\{#_Toc218772049 .anchor\}

# Save Layout

Use the *Save* button located in the top right corner to save the newly created layout.

![Plant Layout page showing the Save option](media/image6.png)\{width="6.575694444444444in" height="4.315178258967629in"\}

# 

# Load Layout

Using the *Select a Layout* dropdown, the user can load the created layouts. Click on the layout name to load the layout. Once the layout is loaded, the keyboard\'s arrow keys can be used to move the layout left, right, forward, and backward.

![UI showing the Generate Layout side menu bar and the grid](media/image7.png)\{width="6.577597331583552in" height="3.4314545056867893in"\}

# 

# Update Layout

Once the layout is loaded, the user can edit the layout as needed. Clicking on the *Update* option updates the changes made to an existing layout.

Note: If no models are left to add and no space is available on the layout, the Add button will be disabled.

![Screenshot of the \'Plant Layout\' section in Accenture\'s TWIN BUILDER software. The interface displays a 3D grid populated with various industrial components representing a plant layout. Navigation tabs appear at the top, with \'Plant Layout\' highlighted. On the right side are \'Delete Layout\' and \'Update\' buttons for modifying the layout. The interface supports designing and managing virtual representations of physical industrial environments.](media/image8.png)\{width="6.550255905511811in" height="3.7865387139107614in"\}

# 

# Delete Layout

Once the layout is loaded, the user can delete the layout. Clicking on the *Delete Layout* option deleted layout will not be visible in the existing layout.

![Thumbnail image for Delete Layout Video](media/image9.png)\{width="6.565020778652668in" height="4.163544400699912in"\}

# 

# Move Camera

The A, D, W, and S keys on the keyboard can be used to move the camera angle upwards, downwards, or sideways. The mouse wheel can be used to zoom in and out. By holding the left-click button and moving the cursor, the layout can be rotated.

  -----------------------------------------------------------------------
    **Key**   **Action**
  ----------- -----------------------------------------------------------
       A      move right

       D      move left

       W      move forward

       S      move backward
  -----------------------------------------------------------------------

![Thumbnail image for Move Camera video](media/image10.png)\{width="6.650084208223972in" height="4.337563429571303in"\}
