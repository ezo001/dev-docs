---
id: aot-twin--viewer-ui-guide-auriga
title: AOT Twin  Viewer UI Guide Auriga
---

**Accenture Operations Twin**

**Twin Viewer**

**UI GUIDE**

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
| **Related Assets / Alternatives** |  |

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contact [3](#contact)](#contact)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Home Page [4](#home-page)](#home-page)

[3D Twin Viewer [5](#d-twin-viewer)](#d-twin-viewer)

[Load Plant Layout [5](#load-plant-layout)](#load-plant-layout)

[View Layout in 3D [6](#view-layout-in-3d)](#view-layout-in-3d)

[Drill-down [6](#drill-down)](#drill-down)

[Detail View [7](#detail-view)](#detail-view)

[Points of Interest [7](#points-of-interest)](#points-of-interest)

[Event-driven Real-time Sync [8](#event-driven-real-time-sync)](#event-driven-real-time-sync)

[OH Communication [9](#oh-communication)](#oh-communication)

[Two-way Communication with Intelligent Advisor [11](#two-way-communication-with-intelligent-advisor)](#two-way-communication-with-intelligent-advisor)

[Two-way Communication with Smart KPIs [12](#two-way-communication-with-smart-kpis)](#two-way-communication-with-smart-kpis)

[View 2D Schematic Layout [13](#view-2d-schematic-layout)](#view-2d-schematic-layout)

[2D Twin Viewer [14](#d-twin-viewer-1)](#d-twin-viewer-1)

[Load Plant Layout [14](#load-plant-layout-1)](#load-plant-layout-1)

[Drill-down [14](#drill-down-1)](#drill-down-1)

[Batch And Product [15](#batch-and-product)](#batch-and-product)

[Image POI [15](#image-poi)](#image-poi)

[Switching Layout from 2D to 3D [16](#switching-layout-from-2d-to-3d)](#switching-layout-from-2d-to-3d)

[Communication with Smart KPIs [17](#communication-with-smart-kpis)](#communication-with-smart-kpis)

[Communication with Intelligent Advisor [17](#communication-with-intelligent-advisor)](#communication-with-intelligent-advisor)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT’s Twin Viewer is an immersive 2D and 3D environment, where end users can monitor, diagnose, and investigate operational data within the visual context of 2D and 3D models. Twin Viewer empowers organizations to enrich existing models with visualizations powered by AOT data, without the need for 2D/3D expertise. Visualizations can be easily consumed from web browsers.

The Twin Viewer application is implemented as Micro-Frontends (MFE) based on React. Twin Viewer fetches and views 2D and 3D content from the Twin Builder application. Visualization is augmented with information that resides in CDF (Cognite Data Fusion). For the 3D Twin Viewer, the application has both coupled and de-coupled versions. In the coupled version, the models are obtained from both the 3DCE model list and the AOT model list, and all models are stored on the 3DCE tenant. In the decoupled version, only AOT models are present, and they are stored in the AOT space.

## Purpose

This guide explains how to use the following Twin Viewer features:

- Globe/Map view.

- 2D/3D Layout of the factory.

- Augmentation of contextualized data.

- 360-degree view by orbiting around the 3D Model and Zoom in/out to see the 3D Model.

- 2D and 3D Model Drill-down functionality with specific data.

- Navigate to other AOT components (IA/KPI) via a single click.

##  Target Audience

- Plant designers

- Maintenance personnel

- Business Analyst

- End users of AOT

## Prerequisites

To visualize contextualized data on Twin Viewer, a plant layout (2D and/or 3D) must be created and saved using Twin Builder.

## Contact

- [`rishabh.b.joshi@accenture.com`](https://greetings.accenture.com/watch/x8MuW2xdxHTnX1iM7mD3b6)

- ``

## Related Links

- [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

- [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

- [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

- [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## Glossary

| Term | Definition |
|----|----|
| Twin Viewer | An application used to visualize plant layouts and contextualized data in either 2D or 3D formats. |
| Twin Builder | A tool used to create and save plant layouts for visualization in Twin Viewer. |
| Plant Layout | The schematic representation of a plant's floor, which can be viewed in 2D or 3D. |
| 2D Schematic Layout | A two-dimensional representation of the plant's layout, providing a simplified overview. |
| 3D Plant Layout | A three-dimensional model of the plant layout, offering a more detailed and immersive visualization. |
| Layout Type | The format in which the plant layout is presented, such as 2D schematic or 3D model. |
| LOAD LAYOUT | A function that loads the selected plant layout based on the user’s choices. |
| AOT | Refers to the Accenture Operations Twin application where Twin Viewer is accessed; also appears in related links. |

# Home Page

Twin Viewer is launched using the top menu bar found in the main AOT application. The video shows how the view can be toggled between two dimensions and three dimensions.

On the top navigation bar, click the toggle switch to change the theme from dark to light and vice versa,



# 3D Twin Viewer

## Load Plant Layout

The end user may choose a plant by clicking on the pin and selecting the Plant Layout option to navigate to the plant floor layout. The resulting pop-up displays plant-level details and two dropdown options:

1.  Layout type: Options available are 2D Schematic layout and 3D Plant layout.

2.  Plant Layout: Enables selecting the plant layout as per the layout type selected.

For 3D, select ‘3D Plant Layout’ and the required layout file from the dropdown options. Clicking the LOAD LAYOUT option loads the plant layout as per the selections made.

After the layout loads, you can return to the Globe/Map page by selecting the globe icon on the left. This enables you to select different plant locations and load corresponding layouts.

The dropdown menu with the plant layout name enables you to view the list of plant layouts available. You can load different layouts using this dropdown.



## View Layout in 3D

By default, the layout gets loaded in 3D view.

- The layout can be moved left, right, forward, and backward using the AWSD or arrow keys on the keyboard.

- The layout can be rotated 360 degrees by dragging the mouse left horizontally.

- The Details toggle displays the detailed view panel with insight, action, and KPI counts.

The video on the side demonstrates this functionality.



## Drill-down

Drill-down allows you to go deep into the 3D asset hierarchy and see the corresponding data of internal parts/sub-parts of the selected asset.

When you click on a 3D Asset, the app navigates one level down and shows the next level data of all mapped parts/sub-parts.

Users can view two types of data; one is Model Mapping, and another is POI data.

On the landing page, the Model Mapping data is displayed by default. When you click on any asset and drill down, they can see the POIs added on the mesh along with the POI-related data.

Note that the data on POIs is not clickable. User can hover over the POI to check the corresponding AOT information or use the POI toggle button to toggle all POIs with their AOT information.  


## Detail View

The detailed information panel may be accessed in two ways:

- From the Twin Viewer, select an asset and then click the See Details button to switch to the Entity Viewer detailed view.

- From detail panel we can also access 2D layout which is mapped to 3D model by clicking on 2D icon button.

- The detail can also be seen by switching detail toggle button.

The video on the right demonstrates the Entity Viewer functionality.



# 

## Points of Interest

By clicking on the POI Data toggle, Insight, Action, and Smart KPI related to the associated POI that was mapped in POI mapping are displayed.

The video on the right demonstrates the POI data view functionality.



# 

## Event-driven Real-time Sync 

Using the Azure PubSub event, Twin Viewer can communicate with other MFE apps like AOT’s Intelligent Advisor and Dashboard.

The video on the side demonstrates the real-time sync functionality.



Communication through the Azure Web PubSub event for the Insight event, Action event, and KPI event are described below:.

When a new insight is generated by the system, the server invokes a new insight event with the response which is received by the Twin Viewer and is shown on the UI. This is depicted in the video below.



When a user creates a new or updates an existing insight/action in the IA panel, the changes are reflected in the Twin Viewer Info panel as well as on the detail panel. This is depicted in the video below.



With the KPI event, the computation of the actual value is reflected in the KPI detail pane when the computation event is triggered from the KPI side. This is depicted in the video below.



## OH Communication

By clicking on the OH node, the operation hierarchy is displayed in the Twin Viewer. The model that is associated with the node is also highlighted.

The video on the right demonstrates the Viewer’s one-way communication with OH.



As demonstrated in the video on the right, if you select an OH node before navigating to the Twin Viewer application, then you will be rerouted to that node after selecting the plant layout.



Asset and node selections made in the Twin Viewer application are retained when shifting to the Operation Hierarchy application.

The Intelligent Advisor application and the dashboard are also synchronized as per the asset and node selected.



## 

## Two-way Communication with Intelligent Advisor

Twin Viewer can interact bidirectionally with other AOT components. For example, while visualizing the plant layout in Twin Viewer you can also access the details of Insights and Actions in the Intelligent Advisor Panel. To experience this functionality, follow the steps below:

1.  Load the plant layout.

2.  By loading the plant layout in 3D view, you can view the count of insights, actions, and KPIs as a small model pop-up.

3.  Next, click on the model pop-up. Doing this redirects you to a detailed UI with the count of insights, actions, and KPIs that are displayed as per their priority, new/close status, and RAG status, respectively.

4.  The count of insights and actions is sorted as follows:

    - Insights - High, Medium, Low Priority

    - Actions - In time, exceeded timeline.

5.  Click on the insights or actions row. Doing this will lead you to an expanded Intelligent Advisor panel, which provides details about the insights and actions filtered out as per the selected asset.

6.  When you click on the insights or action row, the Advisor Panel expands. This shows the two-way communication between Twin Viewer and Intelligent Advisor.

`\>` Note that to view the accurate insight count on the IA panel, you must ensure that all applied filters are deselected from the IA panel.



# 

## Two-way Communication with Smart KPIs

Twin Viewer interacts with the Smart KPI component in a similar way it interacts with IA. To experience this functionality, follow the steps below:

1.  Load the plant layout.

2.  By loading the plant layout in 3D view, you can view the count of insights, actions, and KPIs as a small model pop-up.

3.  Clicking on the model pop-up redirects you to a detailed page showing a count of insights, actions, and KPIs that are displayed as per their priority, new/close, and RAG status, respectively. In the video, the KPI count has been sorted as per RAG status Red Amber Green.

4.  Clicking on the KPI count, you are led to the KPI detail tile on the right side of the plant layout. In the KPI detail tile, KPIs are sorted as per RAG status and are filtered according to the selected asset. Thus, you see the RED status KPIs on the top, followed by AMBER status KPIs, and finally GREEN status KPIs at the end.

5.  By clicking on the ‘see details’ button on any KPI row, you are navigated to the detailed KPI page, and the corresponding KPI loads on the dashboard. This shows the two-way communication between Twin Viewer and Smart KPIs.



##  

## View 2D Schematic Layout

The ‘Open Layout’ option in the top-right corner of the plant layout screen enables viewing of the 2D Schematic Layout of the selected layout.

Note that this option is only available if the selected layout is linked with a 2D schematic (svg), and you are notified of the same by the message “2D Schematic available’ next to the ‘Open Layout’ option.

When the ‘Open Layout’ option is clicked, the 2D schematic layout loads. The 2D layout can be zoomed in and out for better viewability.



# 2D Twin Viewer

## Load Plant Layout

The end user may choose a plant by clicking on the pin and selecting the Plant Layout option to navigate to the plant floor layout. The resulting pop-up displays plant-level details and two dropdown options:

1.  Layout type: Options available are 2D Schematic layout and 3D Plant layout.

2.  Plant Layout: Enables selecting the plant layout as per the layout type selected.

For 2D, select ‘2D Schematic Layout’ and the required SVG file from the dropdown options. Clicking the LOAD LAYOUT option loads the plant layout as per the selections made.

After the layout loads, you can return to the Globe/Map page by selecting the globe icon on the left. This enables you to select different plant locations and load corresponding layouts.

The dropdown menu with the plant layout name enables you to view the list of plant layouts available. You can load different layouts using this dropdown.

If no SVG file is uploaded for the selected location, the dropdown list will display a non-selectable 'No Data' option.

## Drill-down

Drill-down allows you to go deep into the 2D asset and see the corresponding insights, actions, and KPIs of the asset and any sub-assets/internal parts.

- Selecting any of the three options—insights, actions, or KPIs—allows you to further explore their detailed information.

- When the Plant Layout option is chosen from the popup associated with the 2D asset, it displays the layout specific to that asset, including the configuration of its sub-assets.

- To navigate back to the previous layout, click on the Plant Layout icon located next to the Plant Layout dropdown menu.





## Batch And Product

This feature enables users to view batch and product order details.

- If the layout (svg file) is configured for Batch and Product, then user can see the “Batch and Product” UI.



- On enabling Live Batch button, users will be able to see Batch Details on the UI.

The following video shows how the batch and product order details can be viewed.  


## Image POI

POIs can be useful in images as follows.

1.  Users can click on element in SVG Layout and then click on the document icon on the mini popup

2.  When document gets loaded in the same screen as a popup, user can see the POI pins in the doc.

3.  Users can click on any pin, and a mini popup opens for the Asset Mapped for the POI pin.

4.  User can view Insights/Actions/KPI for that mapped asset .

The following video illustrates these points.  


## 

## 

## Switching Layout from 2D to 3D

There are two ways to navigate to the 3D layout from the 2D Viewer application:

1.  From the 2D schematic layout, click the Open Layout link. If the link does not appear, then the 3D layout is not available.

2.  From the details popup (by clicking on a box), there is a 3D option available. If it is enabled, it means the box/asset has a detailed 3D layout linked via the PlantLayout application.

`\>` 

## 

## Communication with Smart KPIs

Twin Viewer can interact with the Smart KPI component as follows:

1.  Click on the Element to open the KPI Detail panel.

2.  Click on the “KPI ()” Row to reveal a popup showing Smart KPI.

3.  Click on the “See Details” Button to navigate to the Dashboard with the corresponding KPI selected.



## Communication with Intelligent Advisor

Twin Viewer can interact with the Intelligent Advisor component as follows:

1.  Click on the Element to open the Detail panel.

2.  Click on the “Insights” Row to check the details of insights on the Intelligence Advisor Panel (Refer to above image).

3.  Click on the “Actions” Row to check the details of actions in the Intelligence Advisor Panel (Refer to above image).
