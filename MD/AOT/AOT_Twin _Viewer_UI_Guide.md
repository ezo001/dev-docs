---
sidebar_position: 2
title: AOT Twin  Viewer UI Guide
---

<div class="doc-title-block">
<p class="doc-asset-name">Accenture Operations Twin</p>
<p class="doc-topic">Twin Viewer</p>
<p class="doc-type">UI GUIDE</p>
</div>

![](./media/AOT_Twin%20_Viewer_UI_Guide/image1.png)

Release Version: 2.5

<div class="metadata-for-agents" aria-hidden="true">

**Metadata Table**


| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Accenture Operations Twin / Twin Builder and Viewer |
| **Domain / Area** | Digital Twin / Visual monitoring and alerts |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya, Rane, Chetankumar |
| **Status** | Published / Complete |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [[Summary - Overview]](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) **Related Assets / Alternatives** |

</div>

## Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

AOT\'s Twin Viewer is an immersive 2D and 3D environment, where end users can monitor, diagnose, and investigate operational data within the visual context of 2D and 3D models. Twin Viewer empowers organizations to enrich existing models with visualizations powered by AOT data, without the need for 2D/3D expertise. Visualizations can be easily consumed from web browsers.

The Twin Viewer application is implemented as Micro-Frontends (MFE) based on React. Twin Viewer fetches and views 2D and 3D content from the Twin Builder application. Visualization is augmented with information that resides in CDF (Cognite Data Fusion). For the 3D Twin Viewer, the application has both coupled and de-coupled versions. In the coupled version, the models are obtained from both the 3DCE model list and the AOT model list, and all models are stored on the 3DCE tenant. In the decoupled version, only AOT models are present, and they are stored in the AOT space.

### Purpose

This guide explains how to use the following Twin Viewer features:

-   Globe/Map view.

-   2D/3D Layout of the factory.

-   Augmentation of contextualized data.

-   360-degree view by orbiting around the 3D Model and Zoom in/out to see the 3D Model.

-   2D and 3D Model Drill-down functionality with specific data.

-   Navigate to other AOT components (IA/KPI) via a single click.

###  Target Audience

-   Plant designers

-   Maintenance personnel

-   Business Analyst

-   End users of AOT

### Prerequisites

To visualize contextualized data on Twin Viewer, a plant layout (2D and/or 3D) must be created and saved using Twin Builder.

### Contact

-   [rishabh.b.joshi@accenture.com](https://greetings.accenture.com/watch/x8MuW2xdxHTnX1iM7mD3b6)

-   [chetankumar.rane@accenture.com](mailto:chetankumar.rane@accenture.com)

### Related Links

-   [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

### Glossary


| Term | Definition |
| --- | --- |
| Twin Viewer | An application used to visualize plant layouts and contextualized data in either 2D or 3D formats. |
| Twin Builder | A tool used to create and save plant layouts for visualization in Twin Viewer. |
| Plant Layout | The schematic representation of a plant\'s floor, which can be viewed in 2D or 3D. |
| 2D Schematic Layout | A two-dimensional representation of the plant\'s layout, providing a simplified overview. |


## 3D Twin Viewer

### Load Plant Layout

The end user may choose a plant by clicking on the pin and selecting the Plant Layout option to navigate to the plant floor layout. The resulting pop-up displays plant-level details and two dropdown options:

1.  Layout type: Options available are 2D Schematic layout and 3D Plant layout.

2.  Plant Layout: Enables selecting the plant layout as per the layout type selected.

For 3D, select \'3D Plant Layout\' and the required layout file from the dropdown options. Clicking the LOAD LAYOUT option loads the plant layout as per the selections made.

After the layout loads, you can return to the Globe/Map page by selecting the globe icon on the left. This enables you to select different plant locations and load corresponding layouts.

The dropdown menu with the plant layout name enables you to view the list of plant layouts available. You can load different layouts using this dropdown.

[VIDEO LINK](https://greetings.accenture.com/watch/FtfHiA4nVUB89tDS2GxNbG?)

![Load Plant Layout Video showing how to select plant locations on a globe and load different plant layouts in Twin Viewer.](./media/AOT_Twin%20_Viewer_UI_Guide/image4.gif)

### View Layout in 3D

By default, the layout gets loaded in 3D view.

-   The layout can be moved left, right, forward, and backward using the AWSD or arrow keys on the keyboard.

-   The layout can be rotated 360 degrees by dragging the mouse left horizontally.

-   The Details toggle displays the detailed view panel with insight, action, and KPI counts.

The video on the side demonstrates this functionality.

### Drill-down

Drill-down allows you to go deep into the 3D asset hierarchy and see the corresponding data of internal parts/sub-parts of the selected asset.

When you click on a 3D Asset, the app navigates one level down and shows the next level data of all mapped parts/sub-parts.

Users can view two types of data; one is Model Mapping, and another is POI data.

### Detail View

The detailed information panel may be accessed in two ways:

-   From the Twin Viewer, select an asset and then click the See Details button to switch to the Entity Viewer detailed view.

-   From detail panel we can also access 2D layout which is mapped to 3D model by clicking on 2D icon button.

-   The detail can also be seen by switching detail toggle button.

By clicking on the POI Data toggle, Insight, Action, and Smart KPI related to the associated POI that was mapped in POI mapping are displayed.

The video on the right demonstrates the POI data view functionality.

[VIDEO LINK](https://greetings.accenture.com/watch/ChAEuZdrQcZVDpqz1VJW35)

![Video Thubnail for Points of Interest](./media/AOT_Twin%20_Viewer_UI_Guide/image8.png)

## 

## 

### Event-driven Real-time Sync 

Using the Azure PubSub event, Twin Viewer can communicate with other MFE apps like AOT\'s Intelligent Advisor and Dashboard.

The video on the side demonstrates the real-time sync functionality.

[VIDEO LINK](https://greetings.accenture.com/watch/r8uECZ64tPQ9Z3S2BZ9zBJ?)

![Video demonstrating event-driven real-time synchronization between Twin Viewer and other AOT applications using Azure PubSub.](./media/AOT_Twin%20_Viewer_UI_Guide/image9.png)

Communication through the Azure Web PubSub event for the Insight event, Action event, and KPI event are described below:.

When a new insight is generated by the system, the server invokes a new insight event with the response which is received by the Twin Viewer and is shown on the UI. [VIDEO LINK](https://greetings.accenture.com/watch/8NSeaL2J2vpyv3Ac4ETAWp?)

![Video showing how new insights generated by the system are displayed in Twin Viewer.](./media/AOT_Twin%20_Viewer_UI_Guide/image10.jpeg)

When a user creates a new or updates an existing insight/action in the IA panel, the changes are reflected in the Twin Viewer Info panel as well as on the detail panel. [VIDEO LINK](https://greetings.accenture.com/watch/rYwrUEdYmJnMXZEPZncpwS?)

By clicking on the OH node, the operation hierarchy is displayed in the Twin Viewer. The model that is associated with the node is also highlighted.

The video on the right demonstrates the Viewer\'s one-way communication with OH.

[VIDEO LINK](https://greetings.accenture.com/watch/qyjcj3BWgzkNaiiCMmjS8G?)

![Video demonstrating how selecting an OH node displays the operation hierarchy and highlights the associated model in Twin Viewer.](./media/AOT_Twin%20_Viewer_UI_Guide/image13.png)

As demonstrated in the video on the right, if you select an OH node before navigating to the Twin Viewer application, then you will be rerouted to that node after selecting the plant layout.

[VIDEO LINK](https://greetings.accenture.com/watch/qyjcj3BWgzkNaiiCMmjS8G?)

![Video showing how selecting an OH node before entering Twin Viewer reroutes the user to that node after plant layout selection.](./media/AOT_Twin%20_Viewer_UI_Guide/image14.png)

Asset and node selections made in the Twin Viewer application are retained when shifting to the Operation Hierarchy application.

The Intelligent Advisor application and the dashboard are also synchronized as per the asset and node selected.

[VIDEO LINK](https://greetings.accenture.com/watch/orTaQkswUWpBNzX4etSqQE?)

![Video demonstrating how asset and node selections in Twin Viewer are retained when switching to the Operation Hierarchy application.](./media/AOT_Twin%20_Viewer_UI_Guide/image15.png)

### 

## Two-way Communication with Intelligent Advisor

Twin Viewer can interact bidirectionally with other AOT components. For example, while visualizing the plant layout in Twin Viewer you can also access the details of Insights and Actions in the Intelligent Advisor Panel. To experience this functionality, follow the steps below:

1.  Load the plant layout to view the count of insights, actions, and KPIs as a small model pop-up.

2.  Next, click on the model pop-up. Doing this redirects you to a detailed UI with the count of insights, actions, and KPIs that are displayed as per their priority, new/close status, and RAG status, respectively.

3.  The count of insights and actions is sorted as follows:

    -   Insights - High, Medium, Low Priority

    -   Actions - In time, exceeded timeline.

4.  Click on the insights or actions row. Doing this will lead you to an expanded Intelligent Advisor panel, which provides details about the insights and actions filtered out as per the selected asset.

5.  When you click on the insights or action row, the Advisor Panel expands. This shows the two-way communication between Twin Viewer and Intelligent Advisor.

> Note that to view the accurate insight count on the IA panel, you must ensure that all applied filters are deselected from the IA panel.

[VIDEO LINK](https://greetings.accenture.com/watch/5Pkok4EEfCBCymauzK8kSQ?)

[![Video showing two-way communication between Twin Viewer and Intelligent Advisor, including viewing and expanding insights and actions for selected assets.](./media/AOT_Twin%20_Viewer_UI_Guide/image16.png)
](https://greetings.accenture.com/watch/5Pkok4EEfCBCymauzK8kSQ?)

## 

## 

Twin Viewer interacts with the Smart KPI component in a similar way it interacts with IA. To experience this functionality, follow the steps below:

1.  Load the plant layout.

2.  By loading the plant layout in 3D view, you can view the count of insights, actions, and KPIs as a small model pop-up.

3.  Clicking on the model pop-up redirects you to a detailed page showing a count of insights, actions, and KPIs that are displayed as per their priority, new/close, and RAG status, respectively. In the video, the KPI count has been sorted as per RAG status Red Amber Green.

[VIDEO LINK](https://greetings.accenture.com/watch/5Pkok4EEfCBCymauzK8kSQ?)

The \'Open Layout\' option in the top-right corner of the plant layout screen enables viewing of the 2D Schematic Layout of the selected layout.

## 2D Twin Viewer

### Load Plant Layout

The end user may choose a plant by clicking on the pin and selecting the Plant Layout option to navigate to the plant floor layout. The resulting pop-up displays plant-level details and two dropdown options:

1.  Layout type: Options available are 2D Schematic layout and 3D Plant layout.

2.  Plant Layout: Enables selecting the plant layout as per the layout type selected.

For 2D, select \'2D Schematic Layout\' and the required SVG file from the dropdown options. Clicking the LOAD LAYOUT option loads the plant layout as per the selections made.

After the layout loads, you can return to the Globe/Map page by selecting the globe icon on the left. This enables you to select different plant locations and load corresponding layouts.

The dropdown menu with the plant layout name enables you to view the list of plant layouts available. You can load different layouts using this dropdown.

If no SVG file is uploaded for the selected location, the dropdown list will display a non-selectable \'No Data\' option.

### Drill-down

Drill-down allows you to go deep into the 2D asset and see the corresponding insights, actions, and KPIs of the asset and any sub-assets/internal parts.

-   Selecting any of the three options---insights, actions, or KPIs---allows you to further explore their detailed information.

-   When the Plant Layout option is chosen from the popup associated with the 2D asset, it displays the layout specific to that asset, including the configuration of its sub-assets.

-   To navigate back to the previous layout, click on the Plant Layout icon located next to the Plant Layout dropdown menu.

[VIDEO LINK](https://greetings.accenture.com/watch/kpAcQGUxcuY6m16go7auB9?)

![Video showing how to select plant locations and load layouts in the 2D Twin Viewer.](./media/AOT_Twin%20_Viewer_UI_Guide/image19.png)

[VIDEO LINK](https://greetings.accenture.com/watch/PuoZKRExhdgT2uyjt7FNmN?)

![Video demonstrating drill-down into asset layouts to view sub-assets in the 2D Twin Viewer.](./media/AOT_Twin%20_Viewer_UI_Guide/image20.png)

### Batch And Product

This feature enables users to view batch and product order details.

-   If the layout (svg file) is configured for Batch and Product, then user can see the \"Batch and Product\" UI.



-   On enabling Live Batch button, users will be able to see Batch Details on the UI.


### Image POI

POIs can be useful in images as follows.

1.  Users can click on element in SVG Layout and then click on the document icon on the mini popup

2.  When document gets loaded in the same screen as a popup, user can see the POI pins in the doc.

3.  Users can click on any pin, and a mini popup opens for the Asset Mapped for the POI pin.

4.  User can view Insights/Actions/KPI for that mapped asset .

The following video illustrates these points.\
[VIDEO LINK](https://greetings.accenture.com/watch/cWNGkv8erKcPPYjoHau9M6)

![Video Thumbnail for Image POI video](./media/AOT_Twin%20_Viewer_UI_Guide/image22.png)

### 

## 

### Switching Layout from 2D to 3D

There are two ways to navigate to the 3D layout from the 2D Viewer application:

1.  From the 2D schematic layout, click the Open Layout link. If the link does not appear, then the 3D layout is not available.

2.  From the details popup (by clicking on a box), there is a 3D option available. If it is enabled, it means the box/asset has a detailed 3D layout linked via the PlantLayout application.

> ![Image showing the option to switch from a 2D schematic layout to a 3D layout for detailed visualization.](./media/AOT_Twin%20_Viewer_UI_Guide/image23.png)
### 

## Communication with Smart KPIs

Twin Viewer can interact with the Smart KPI component as follows:

1.  Click on the Element to open the KPI Detail panel.

2.  Click on the \"KPI ()\" Row to reveal a popup showing Smart KPI.

3.  Click on the \"See Details\" Button to navigate to the Dashboard with the corresponding KPI selected.

![Image showing how to open the KPI detail panel and navigate to the dashboard with the corresponding KPI selected.](./media/AOT_Twin%20_Viewer_UI_Guide/image24.png)

### Communication with Intelligent Advisor

Twin Viewer can interact with the Intelligent Advisor component as follows:

1.  Click on the Element to open the Detail panel.

2.  Click on the \"Insights\" Row to check the details of insights on the Intelligence Advisor Panel (Refer to above image).

3.  Click on the \"Actions\" Row to check the details of actions in the Intelligence Advisor Panel (Refer to above image).
