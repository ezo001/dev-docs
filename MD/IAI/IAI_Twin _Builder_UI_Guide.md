---
sidebar_position: 2
title: IAI Twin  Builder UI Guide
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">Twin Builder</p>
<p class="doc-type">UI GUIDE</p>
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
| **Source of Truth** | [[Summary - Overview]](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) **Related Assets / Alternatives** ![](./media/IAI_Twin%20_Builder_UI_Guide/image2.png)
|  |

</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools that can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The 3D Twin Builder application is implemented as micro-frontends (MFE) based on React. The 3D Twin Builder allows an admin user to create and upload the models, map the available model using Model Mapping and/or POI mapping apps, and create a dynamic floor layout using a Drag-and-drop mechanism through a web-based user interface using the Plant Layout app. Where the models are stored depends on whether the coupled or de-coupled version is in use. The 3D visuals created in 3D Twin Builder are viewable in the 3D Twin Viewer.

The 2D Twin Builder application is also implemented as an MFE based on React. The 2D Twin Builder allows an admin user to upload the 2D Schematics (SVG, PDF, &amp; PNG format files) and map the available files using twin builder 2D configurator. The 2D visuals created in the 2D Twin Builder can be viewed in IAI\'s 2D Twin Viewer.

### Purpose

This document explains the features of both the 2D and 3D Twin Builder user interface.

### Prerequisites

-   2D and/or 3D Twin Builder applications must be deployed.



-   A compatible browser (Google Chrome or Microsoft Edge) must be installed.



-   For 2D, the SVG file should be extracted properly from Figma, refer to [Getting Started with Twin Viewer and Builder](https://industryxdevhub.accenture.com/assetdetails/47) for more information.

###  Target Audience

-   Business Analyst

-   IAI End Users

-   Plant Designers

-   Client IT Admins

### Contact

-   [rishabh.b.joshi@accenture.com](mailto:rishabh.b.joshi@accenture.com)

-   [[chetankumar.rane@accenture.com]](mailto:chetankumar.rane@accenture.com)

-   [prabhjeet.g.singh@accenture.com](mailto:prabhjeet.g.singh@accenture.com)

### Related Links

-   [IAI on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [IAI on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [IAI Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

### Glossary


| Term | Definition |
| --- | --- |
| IAI | Abbreviation for \'Application Orchestration Tool\', a platform used for managing and deploying applications. |
| CDF | Refers to \'Common Data Framework\', a structure for organizing and accessing data across applications. |
| Azure | Microsoft\'s cloud computing platform, offering a range of services including hosting, databases, and analytics. |
| Twin Builder | A user interface within the IAI application for creating and managing 3D digital twins. |
| 3D Content Management System | A system for organizing and handling 3D models and related assets within the Twin Builder UI. |
| POI Editor | Point of Interest Editor; a tool for marking and managing specific locations or objects in the 3D environment. |
| Mapper | A feature that allows users to visualize and link spatial data within the Twin Builder UI. |
| Overview Page | The main dashboard or landing page in the IAI application, providing access to key features and tools. |


## 3D Twin Builder

### Launching the UI

Twin Builder can be launched from the IAI application in two ways.


> Method one is to select the Twin Builder option from the side menu which is displayed when clicking the grid menu on the left side of the screen.
>
> ![](./media/IAI_Twin%20_Builder_UI_Guide/image3.png)
\
> Method two is to launch the application from the overview page.
>
> ![](./media/IAI_Twin%20_Builder_UI_Guide/image4.png)

### Features

The following table summarizes the main features of the Twin Builder UI, which are discussed in the subsequent sections.


| **Model -- 3D Content Management System** | **POI Editor** | **Mapper** | **Plant Layout** |
| --- | --- | --- | --- |
| - Model Catalog Page | - Asset List | - Model Mapping | - Create new layout |
| - Model Viewer | - Add POI | - POI Mapping | - Load and modify the existing layout |
| - Delete Model | - Remove POI |  | - Save the layout |



### Model Tab

IAI Twin Builder can process GLB, GLTF, OBJ, and FBX 3D model file formats stored in the Azure Blob-like storage. Models can be a single mesh file or multi-mesh 3D file consolidated together.

-   The Model tab of the UI displays the collection of existing models.

-   The **UPLOAD MODEL** button is used to upload a new model.

-   The dropdown button beside the **UPLOAD MODEL** button allows the user to change the plant.

-   As the user makes changes to the plant, the catalog page refreshes and shows the selected plant models.

-   Use the Model Viewer (click on Model Tile) to view and delete the model or specific version.

    Search for a model by its name from the model search option.

> See the [Models Tutorial](https://industryxdevhub.accenture.com/assetdetails/47) for more details.

![Screenshot of the \'Model\' section in Accenture\'s Twin Builder interface. A pop-up window titled \'Upload Model\' allows users to enter a title and select tags such as \'Warehouse Demo\' and \'Entrance_Demo.\' Users can drag and drop files to upload. A 3D model of a cylindrical object with a smaller cylinder on top is displayed in the window.](./media/IAI_Twin%20_Builder_UI_Guide/image5.jpeg)

Using the POI Editor, the user can add, remove, move, and save POIs (points of interest) to the available model from the model list. The video shows the following steps:

1.  Select the plant from the plant dropdown.

2.  Select the model from the model list.

3.  Click on \'view model\' to see the 3D model.

4.  Using the top menu, add, remove, and move POIs as necessary.

5.  Click on the Save POI button from the top menu.

6.  To remove POI, delete all mappings using the POI Editor.

Note that navigating to other tabs before the selected tab has fully loaded will not work as the application can load only one MFE at a time. This is applicable across the application.

![DT_3D_POI_Editor](./media/IAI_Twin%20_Builder_UI_Guide/image6.jpeg)

### Mapper Tab

#### Model Mapping

Model mapping shows the catalog of mapped 3D models. Select the plant before starting the model mapping. It has an \'ADD MAPPING\' option to map new 3D model(s) to a particular Cognite ID (asset hierarchy) in the model hierarchy.

Note that the admin user must first map a model on the \'Model mapping\' application before navigating to the \'POI mapping\' application.

#### Add New Asset Mapping

The ADD MAPPING button can be used to open a separate wizard for mapping new assets. Below are the steps to add new asset mapping:

1.  Enter the required details: Title and Model. Note that the title must not exceed 25 Characters.

2.  Right-click to bring up the Context menu which displays two options: X-Ray and Asset Mapping.

3.  Click on Asset Mapping. The asset hierarchy will be visible.

    a.  Click on the check box to select the external ID.

    b.  Click on the add button to map the selected external ID with the asset part.

> Note that while mapping, one context id should be mapped with only one mapping. Mapping the same context ID to multiple mapping is not acceptable.

4.  For mapping the multi-level children, select the X-Ray option to see the children of the selected mesh. Note that the base node and root node must be the same for the same model.

5.  Repeat the Model Mapping function mentioned in Step 3 for each child.

6.  Once done with all level mappings, click on the Map Asset Button. This will save the Model Mapping data on the server.

7.  The home button will close the drill down/X-Ray mode of the selected 3D asset.

8.  The cancel button is used to cancel the mapping and close the Model Mapping experience.

![DT_3D_Model_Mapping](./media/IAI_Twin%20_Builder_UI_Guide/image7.jpeg)

The video below shows how to add new asset mapping.

![Add_Model_Mapping](./media/IAI_Twin%20_Builder_UI_Guide/image8.jpeg)

####  Delete Asset Mapping

To delete the existing mapped asset:

1.  Go to the Model Mapping Catalog page.

2.  Open the Model Viewer popup.

3.  Click on the DELETE BUTTON to delete the selected mapped asset.

The video on the right shows how to delete asset mapping.\
![Delete Model Mapping](./media/IAI_Twin%20_Builder_UI_Guide/image9.jpeg)

**Edit Asset Mapping**

To edit the information in the existing mapped asset:

1.  Go to the Model Mapping Catalog page.

2.  Open the Model Viewer popup.

3.  Click on the EDIT BUTTON to edit the selected mapped asset.

4.  The \'Edit Popup\' window will open.

The video on the right shows how to edit asset mapping.

![Edit Mapping](./media/IAI_Twin%20_Builder_UI_Guide/image10.jpeg)

#### POI Mapping

POI mapping is required to map the created POIs on the model in the POI editor. The below steps describe how to map the POI and the corresponding video on the side demonstrates them.

1.  Select the plant from the plant selection dropdown.

2.  Select the model from the model list.

3.  If the selected model has a POI, it will be visible on the right side of the screen with the mapping version selection or the option to create a new mapping version.

4.  If the selected model does not have any POIs, a pop-up window displays that there is no POI mapped with that model.

5.  Click on View Model to see the 3D model.

6.  After the model loads, set its base node.

-   The base node must match the root node of the model.

-   Only one context ID can be mapped with a single model.

7.  To add mapping to the POIs, click them to view the hierarchy. Select a node from the hierarchy to map with the POI. Repeat this step for each POI mapping.

8.  Click on the Save Map option when mapping is complete, and the POI mapping data is saved to the server.

9.  To Delete the mapping version, remove it from all Plant Layouts.

10. Clicking the back arrow button cancels the mapping selections, closes the POI mapping screen, and opens the model list.

**Note**:

-   Do not map multiple POIs to the same context ID in the same mapping version.

-   Also, now the user can map POIs to immediate child nodes.

> ![DT_3D_POI_Mapping](./media/IAI_Twin%20_Builder_UI_Guide/image11.gif)

#### Plant Layout

The Unity-based Plant Layout component is used to create, modify, and save the 3D plant layouts. Admin users can create, modify, and save the layout. The numbered list below corresponds to the callouts on the screenshots.

1.  The Plant Layout component tab.

2.  Select the plant from the plant selection dropdown.

3.  Create a Layout by adding a name and grid size.

4.  Clicking the Generate Layout button displays the Assets window and Tile Properties.

5.  Click on the Add Button to see the model list.

6.  Grid/mesh structure that shows the asset selected for the creation of plant layout.

7.  Delete Layout button.

8.  Model Manipulation Panel

Below, the central panel shows the set of available models as thumbnails. The Load More button loads the models which are not present currently on screen.

![](./media/IAI_Twin%20_Builder_UI_Guide/image12.png)

Note that the tile properties panel (not shown) may be used to change the tile size model to be placed on the grid. See the [Plant Layout tutorial](https://industryxdevhub.accenture.com/assetdetails/47) for more details.

![](./media/IAI_Twin%20_Builder_UI_Guide/image13.png)

![](./media/IAI_Twin%20_Builder_UI_Guide/image14.png)

## 2D Twin Builder

### Launching the UI

The 2D Twin Builder can be launched from the IAI application in two ways.

1.  

2.  **Side menu**:

    -   Click the grid menu icon to expand the side menu panel.

    -   Select the Twin Builder option from the menu

    -   Click 2D Twin on the left side of the screen.

> ![2D Twin option in side menu](./media/IAI_Twin%20_Builder_UI_Guide/image15.png)
3.  **Overview page**:

    -   Access the overview page from the side menu panel.

    -   Select the 2D Twin tile to launch the application.

> ![](./media/IAI_Twin%20_Builder_UI_Guide/image16.png)

### Features

The main features of the 2D Twin Builder UI are as follows:

#### 

### File Management

2D Twin Builder can process SVG file formats stored in the Azure Blob-like storage. The Figma exported SVG file can contain text, images, and other visual elements.

The UI facilitates file management through:

-   Layout Catalog

-   Layout Viewer

-   Delete 2D Layout

####  Layout Management

2D Twin Builder

-   Load and modify the existing layout

-   Save the layout

-   Map elements of the layout to assets

-   Link multiple layouts

####  Error Management

If there are no Files available in the selected plant, the system will throw an error.

![error message when no files are available](./media/IAI_Twin%20_Builder_UI_Guide/image17.png)

Continue reading for more information on these features.

### Application Tabs

#### Files Tab

The Files tab of the UI displays the collection of existing SVG Files. Controls include:

1.  Plant selection

2.  File upload

3.  Model Search

4.  Upload File dialog

See the [Models Tutorial](https://industryxdevhub.accenture.com/assetdetails/47) for more details.

![A screenshot of a computer AI-generated content may be incorrect.](./media/IAI_Twin%20_Builder_UI_Guide/image18.png)

#### Layout Tab

On the Layout tab, Administrators can view, modify, and map assets, link SVG files, and save the layout. With the slider on the left, the SVG file can be zoomed in and out. Controls include:

1.  Plant selection

2.  Layout loading

3.  Layout Linking

As shown in the video, the SVG file can be configured in real time. The user can map AssetID, modify element Name, link available SVG, make elements clickable, and add Overlay of SVG.

**Note**:

-   To set the KPI / Insight / Action Icon color in the elements, the element ID must be set to respective tags from the list. For eg. \"Set_KPI_Icon_Color\", \"Set_Insight_Icon_Color\", etc.

-   To set the KPI / Insight / Action data count in the elements, the element ID must be set to respective tags from the list. For eg. \"Set_KPI_DATA_Count\", \"Set_Insight_DATA_Count\", etc.

-   To set the Batch numbers dynamically in the elements, the element ID must be set to \"Batch_Numbers\" from the list.

![2D Schematics Configurator Demo ](./media/IAI_Twin%20_Builder_UI_Guide/image19.gif)

#### Image POI Editor Tab

On the Image POI Editor tab, Administrators can upload documents, add and map multiple POIs to assets, link them to an SVG layout, and view asset details in the 2D Viewer.

1.  Only png/pdf documents can be uploaded.

2.  Multiple POI\'s can be added on a document.

3.  Each POI can be mapped to an AssetID, and can be interacted with in Twin viewer to see the details of that asset

4.  Uploaded Documents can be linked to a SVG layout to view the details in Twin viewer

The image below gives an overview of the POI Editor tab. Refer the video on the side for a demonstration of the functionalities described above.

![A screenshot of a computer AI-generated content may be incorrect.](./media/IAI_Twin%20_Builder_UI_Guide/image20.png)

![](./media/IAI_Twin%20_Builder_UI_Guide/image21.png)
