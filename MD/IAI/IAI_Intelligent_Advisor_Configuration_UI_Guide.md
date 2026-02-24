---
sidebar_position: 2
title: IAI Intelligent Advisor Configuration UI Guide
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">Industrial AI Foundation</p>
<p class="doc-topic">Intelligent Advisor Configuration</p>
<p class="doc-type">UI GUIDE</p>
</div>

<p class="doc-version">Release Version: 2.5</p>

**Metadata Table:**


<div class="metadata-for-agents" aria-hidden="true">
| **Field** | **Value** |
| --- | --- |
| **Asset / Solution Name** | Industrial AI Foundation / Intelligent Advisor |
| **Domain / Area** | Advisory / Decision Automation |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Susarla, Aditya, Kannan, Jishnu |
| **Status** | Draft / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | Intelligent Advisor UI Guide, Intelligent Advisor Delivery Guide ![](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image2.png)
|  |

</div>

## Introduction

Industrial AI Foundation (IAI) is a collection of software accelerators and tools, including the Intelligent Advisor (IA) Configuration application, which can be assembled to deliver client solutions. IAI accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

IA is an IAI component and an AI-based solution that enables users of different types to focus on critical issues with real-time generated, prioritized, and contextualized Insights and recommendations. It combines the following functional components: Insight generation engine, collaboration, Actions, Advisor panel, Insight Viewer template, and Insight lifecycle management.

### Purpose

This guide explains how to use IAI\'s Intelligent Advisor Configuration UI. 

### Target Audience

End users of the IAI UI.

###  Prerequisites

-   IAI has been deployed.

-   Google Chrome browser is supported.

### Related Links

-   [IAI on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [IAI on Azure](https://aot-azure.accenturedigitalplant.com/)


-   [IAI Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)[IA IX Developer Hub Resources](https://industryxdevhub.accenture.com/assetdetails/43)

### Contact

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [[judit-kinga.zoltani@accenture.com](mailto:judit-kinga.zoltani@accenture.com)]

### 

## Glossary


| **Term** | **Definition** |
| --- | --- |
| Industrial AI Foundation (IAI) | A collection of software accelerators and tools, including the Intelligent Advisor (IA) Configuration application, designed to integrate product, process, and live data from IT and OT systems for comprehensive operational insights and optimization. |
| Intelligent Advisor (IA) | A component of IAI that uses AI to provide real-time insights, recommendations, and smart guidance to users, featuring an insight generation engine, collaboration tools, actions, advisor panel, insight viewer template, and insight lifecycle management. |
| IA IX Developer Hub | A resource hub for developers working on Intelligent Advisor Integration Experience (IX) related projects. |
| Component Configuration | The process or interface for setting up and managing application components within the platform. |
| Plant Drop-Down | A menu feature on the configuration page allowing users to select a specific plant or site for configuration. |
| UI (User Interface) | The interface of the application, which can be web-based or application-based, used for interacting with the system. |
| Google Chrome | A web browser recommended for compatibility with the application. |
| CDF | Cognite Data Fusion |
| Azure | Microsoft\'s cloud computing platform, referenced as a deployment option for IAI. |
| Configure Insights | A dropdown menu in the UI that provides options for configuring insights, including insights based on KPIs, predictive failure configuration, and custom insight categories. |
| Insights based on KPIs | Insights derived from Key Performance Indicators, configurable within the platform. |
| Predictive Failure Configuration | Configuration related to predicting failures using algorithms, asset selection, and impacted KPIs. |
| Custom Insight Category | Allows customization of insight categories, including theme, sub-type, priority, department, role, action time, frequency, and thresholds. |
| KPI (Key Performance Indicator) | Metrics used to evaluate the performance of assets, processes, or departments, configurable and selectable within the system. |
| KPI Configuration Validation | The process of validating KPI configurations to prevent duplicates and ensure correct setup, with error handling and visual indicators for conflicts. |
| Action In | The time frame within which a KPI or configuration must be actioned, selectable as 1-5 days or other intervals. |
| Frequency | The interval at which a KPI is measured or an action is performed (e.g., 1h, 5min, Hour, Day, Minute). |
| Threshold | Condition for KPI evaluation, such as Equal, Greater than, or Less than, with a user-defined value. |
| Impacted KPIs | KPIs that are affected by a configuration, selectable during the configuration process. |
| Algorithm | The method or model selected for predictive failure or custom insight configuration (e.g., Control Valve Failure, Custom predictive). |
| Asset Selection | The process of selecting assets for configuration, with options to select all, individual, or deselect assets, and manage duplicates. |
| Delete Configuration | The process of permanently removing a configuration, with confirmation prompts and warnings about data loss. |
| Configuration Validation | The process of checking for duplicate or conflicting configurations and providing corrective actions such as deleting duplicates. |
| Edit Configuration | The process of modifying an existing configuration, with pre-populated fields and options to save or cancel changes. |
| Role | The user role associated with a KPI or configuration (e.g., Reliability Engineer, Maintenance Manager, Quality Manager). |
| Department | The department associated with a KPI or configuration (e.g., Maintenance, Automation, Quality). |
| Priority | The importance level of a configuration (e.g., High, Medium, Low). |
| Theme | The overarching category or focus area for a configuration (e.g., Machine learning, Custom predictive). |
| Sub-type | A more specific classification within the theme (e.g., Forecast, Custom predictive). |
| Description | A text field for entering details about a configuration, typically 10--500 characters. |
| AH Level (Alert Hierarchy Level) | The alert hierarchy level associated with a KPI (e.g., System, Plant, Level 4). |
| Configurator Table | A table displaying user-created configurations for the selected plant, including details such as category, type, sub-type, template, role, department, action time, and last edited information. |
| Paginator | A UI element that displays a set number of configurations per page and allows navigation between pages. |
| Three Dots Menu | A menu providing options to edit or delete configurations. |
| Dark/Light Theme Toggle | A UI feature allowing users to switch between dark and light themes for the application. |
| Digital Twin Assistant | A generative AI-based assistant accessible when the platform is deployed in Azure. |


## Launch the Configuration UI

1.  

2.  From the header of the main application, click the 6-dot menu icon as shown on the right.

3.  From the *COMPONENT CONFIGURATION* menu, select either *Overview* or *Intelligent Advisor* to launch the Component Configuration landing page shown below.

![Intelligent Advisor tile](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image3.png)

4.  Select *Intelligent Advisor* from the listed components to launch the IA Configuration landing page.

![Component configuration menu showing the Intelligent Advisor option](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image4.png)

## IA Configuration Landing Page

These are the features available on this page:


| 1 | SELECT PLANT DROP-DOWN -- dropdown for Plant selection. |
| --- | --- |
| 2 | CONFIGURE INSIGHTS -- dropdown for the Insight configuration options. |
| 3 | CONFIGURATIONS TABLE -- displays the list of user-created configurations for the selected plant. |
| 4 | PAGINATOR -- displays eight configurations per page if configurations exist. Clicking the arrows flips the pages. |
| 5 | THREE DOTS MENU -- shows the Edit and Delete options. |
| 6 | Dar/Light Theme -- Clicking on the toggle button helps user to change the theme of an application form dark theme to light theme and vice versa. |
| 7 | Digital Twin Assistant -- When deployed in Azure, clicking the robot icon launches a generative AI based assistant. ![IA Configuration Landing Page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image5.png)
|  |


## Delete Configuration

Clicking the *Delete* option opens a popup message to confirm the permanent deletion.

![delete configuration](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image6.png)

![Delete Configuration message](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image7.png)

## 

# Configure Insights

As shown on the right, clicking the *Configure Insights* drop-down menu reveals three options for configuration:

-   Insights based on KPIs

-   Predictive Failure Configuration

-   Custom Insight Category

Note that the name values of the options listed above are defined on the backend during configuration and may be customized as needed.

These options are explained in the sections that follow.

![Configure Insights dropdown that displays 3 options: Custom, Insights based on KPIs, and Predictive Failure Configuration](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image8.jpeg)

## 

## Insights Based on KPIs

Selecting Insights based on KPIs from the Configure Insights menu opens the KPI Insights configuration page. The callouts on the page correspond with the numbered list below.

![Configure KPI Insights page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image9.png)

| 1 | SELECT KPIS -- Clicking this opens the KPI Selection screen. |
| --- | --- |
| 2 | KPI COUNT -- Shows the number of selected KPIs. If none are selected, a message indicates so. |
| 3 | CANCEL -- Redirects back to the Landing page without saving any selections. |
| 4 | SUBMIT CONFIGURATION -- Enabled only after one or more KPIs have been selected. |
| 5 | SELECTED KPIS -- This table shows details about the selected KPIs. |
| 6 | PAGINATOR --Shows a maximum of six (6) KPIs per page if KPIs have been selected. |
| 7 | ACTION IN -- Selection of the number of days in which the KPI must be actioned. |
| 8 | DELETE -- Removes the selected KPI row. |
| 9 | INTELLIGENT ADVISOR -- This link redirects to the Landing page without saving any selections. |


#### Select KPIs

Clicking the *SELECT KPIS* button opens a screen for selecting KPIs to configure. The list of KPIs is based on the selected Plant. The callouts on the image below correspond with the numbered list at the bottom.

![KPI SELECTION screen](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image10.png)

| 1 | CLOSE -- Closes the popup without saving the current state of the popup. |
| --- | --- |
| 2 | KPI OPTIONS -- Multiple KPIs can be selected. Configured KPIS are grayed out and cannot be selected. |
| 3 | SELECT -- Displays the number of user-selected KPIs and saves them. |

#### 

### KPI Configuration Validation

If an attempt is made to configure KPIs that have already been configured, then an error is displayed in a pop-up window. After closing the popup window, the rows with the selected KPIs are highlighted in red. The numbered list corresponds with the callouts in the following image.


| 1 | SELECT KPIS -- Disabled unless all configured KPIs have been removed. |
| --- | --- |
| 2 | ACTION IN -- This option is disabled at this stage. |
| 3 | DELETE DUPLICATES -- Deletes all the rows with configured KPIs in one instance. |
| 4 | SUBMIT CONFIGURATION -- Disabled unless all configured KPIs have been removed. ![Configure KPI Insights - KPI selection page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image11.png)
|  |

#### 

### Edit KPI Configuration

When the user clicks on *Edit* for a selected KPI row on the landing page, they are redirected to the Edit KPI Configuration screen.

![Edit KPI option](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image12.png)

The Edit KPI Configuration screen has the following features:


| 1 | ACTION IN -- This option allows the Action In field to be edited. |
| --- | --- |
| 2 | CANCEL -- When this option is clicked, the changes are not saved, and the user is redirected to the landing page. |
| 3 | SAVE CONFIGURATION -- This option saves the configuration. It remains disabled if the user does not make any changes. ![A screenshot of a computer](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image13.png)
|  |


### Predictive Failure Configuration

Selecting *Predictive Failure Configuration* from the Configure Insights menu opens the *Configure Predictive Failure* page that guides configuration with a two-step wizard. The callouts on the page correspond with the numbered list below.


-   Algorithm

    -   Algorithm

    -   Asset Selection

-   Configuration

    -   Configuration

    -   Impacted KPIs

![Screenshot showing the algorithm option](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image14.png)

![Screenshot showing the algorithm option when completed](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image14.png)

#### 

### Algorithm

1.  

2.  ALGORITHM -- The drop-down menu is used to select the algorithm that will be used on the configuration.

3.  CANCEL -- Return to the configuration landing page.

4.  NEXT STEP -- Clicking advances to the Asset Selection step.

![Configure Predictive Failure page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image15.png)

#### Asset Selection

1.  SELECT ASSETS -- Clicking calls a pop-up used to select the Assets in the configuration.

2.  BACK -- Clicking saves changes and returns to Step 1.

3.  NEXT STEP -- Clicking advances to Step 2.

4.  ASSET TABLE -- Shows selected assets.

5.  DELETE -- Clicking removes the selected asset from the table.

![Asset selection page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image16.png)

Clicking on *SELECT* *ASSETS* (1) opens the page shown below. The numbered list corresponds with the callouts in the image.

1.  CLOSE -- closes the popup without saving the selected Assets.

2.  SELECT ASSETS -- Select/deselect multiple Assets related to the selected plant. Configured Assets are grayed out and cannot be selected.

3.  SELECT -- shows the number of selected assets and saves the selection to be displayed on the Selected Assets table.

![Asset selection page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image17.png)

#### 

### Configuration

The second step of the wizard is used to set the configuration details. Mandatory fields are indicated by a red asterisk. The user controls work as described in the previous step. The configuration options to select are listed below.

-   Theme

-   Sub-type

-   Priority (High, Medium, Low)

-   Department

-   Role (Based on the selected Plant and Department)

-   Action In (1 Day, 2D, 3D, 4D, 5D, 6D, 1 Week, 2 Weeks, 3 Weeks, 1 Month)

-   Description (10 -- 500 characters)

-   Frequency (Hour, Day, Minute)

-   Frequency Value (Hour = 1-24, Day = 1-15, Minute = 1-60)

-   Threshold (Equal, Greater than, Less than)

-   Threshold Value (Depends on the end user\'s preferred Unit of Measure)

![configuration options video thumbnail](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image18.png)

#### Impacted KPIs

Optionally, this stage of the wizard can be used to select impacted KPIs. The controls are consistent with the previously described pages. The list of KPIs is based on the selected Plant. After the first selection is made, the C*REATE CONFIGURATION* button becomes available.

![AOT_IA_Config_2](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image19.jpeg)

#### 

### Configuration Validation

After clicking the *CREATE CONFIGURATION* button, the submitted configuration is validated. If any of the assets that were selected have already been configured, then a pop-up message appears if the user-selected assets are already configured. The configured assets are listed below the message. Closing the popup window reveals the Asset Selection screen. The numbered list below corresponds with the callouts in the image.

1.  SELECT ASSETS -- Disabled unless all configured assets have been removed.

2.  CONFIGURED ASSET ROW -- These are highlighted in red.

3.  DELETE DUPLICATES -- This option deletes all the rows with configured assets in one instance.

4.  NEXT STEP -- Disabled unless all configured assets have been removed.

![Configure Predictive Failure: Asset selection page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image20.png)

#### 

### Edit Configuration

Choosing *Edit* on the selected configuration row redirects to the Configuration screen.

![Image showing the Edit option on the selected row of the Predictive failure configuration](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image21.png)

The following image depicts the Configuration screen. The dropdowns are already populated with the previously saved data.

![Edit configuration page that allows the user to edit previously saved data for the configuration](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image22.png)

Clicking the NEXT STEP button allows the addition or removal of Impacted KPIs. Adding Impacted KPIs is optional.

![configure predictive failure- impacted KPIs page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image23.png)

### Custom Insight Category

Selecting *Custom Insight Category* from the Configure Insights menu opens the *Configure Custom Insight Category* page that guides configuration with a two-step wizard. The callouts on the page correspond with the numbered list below. This is used to exemplify a custom-created insight category. It uses the same algorithm as the predictive failure category, with some UI customization.

#### Algorithm

1.  ALGORITHM -- The drop-down menu is used to select the algorithm that will be used on the configuration.

2.  CANCEL -- Return to the configuration landing page.

3.  NEXT STEP -- Clicking advances to the Asset Selection step.

![Configure custom insight category page showing the algorithm feature](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image24.png)

#### Asset Selection


| 1\. | SELECT ASSETS \- Clicking calls a pop-up used to select the Assets in the configuration. |
| --- | --- |
| 2\. | BACK \- Clicking saves changes and returns to Step 1. |
| 3\. | NEXT STEP \- Clicking advances to Step 2. |
| 4\. | ASSET TABLE \- Shows selected assets. |
| 5\. | DELETE \- Clicking removes the selected asset from the table. ![Configure Custom Insight Category window showing Asset selection page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image25.png)
The *ASSET SELECTION* pop-up window has the following controls: 1. CLOSE\ - Closes the popup without saving the selected Assets. SELECT ASSETS\ - List of Assets with checkboxes. Users can select/deselect multiple Assets. Configured Assets are grayed out and cannot be selected. The Assets are based on the selected Plant. SELECT\ - Shows the number of selected assets and saves the selection to be displayed on the Selected Assets table. ![Asset selection page expanded with check boxes for assets](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image26.png)
|  |


#### Configuration

The second step of the wizard is used to set the configuration details. Mandatory fields are indicated by a red asterisk (\*). The selectable configuration options are listed below:

-   Theme

-   Sub-type

-   Department

-   Priority (High, Medium, Low)

-   Role (Based on the selected Plant and Department)

-   Action In (1 Day, 2D, 3D, 4D, 5D, 6D, 1 Week, 2 Weeks, 3 Weeks, 1 Month)

-   Description (10 -- 500 characters)

-   Frequency (Hour, Day, Minute)

-   Frequency Value (Hour = 1-24, Day = 1-15, Minute = 1-60)

-   Threshold (Equal, Greater than, Less than)

-   Threshold Value (Depends on user\'s preferred Unit of Measure)

![Configure Custom Insight Category window showing Configuration page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image27.png)

#### 

### Impacted KPIs

Optionally, this stage of the wizard can be used to select impacted KPIs. The controls are consistent with the previously described pages. The list of KPIs is based on the selected Plant.

![Configure Custom Insight Category window showing Impacted KPIs page](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image28.png)

#### Validation

After clicking the *CREATE CONFIGURATION* button, the submitted configuration is validated. If any of the assets that were selected have already been configured, then a pop-up message appears if the user-selected assets are already configured. After closing the popup window, the user is redirected to the Asset Selection screen. The numbered list below corresponds with the callouts in the following image.

1.  SELECT ASSETS -- This option allows the user to select assets. It remains disabled unless the user removes all configured assets.

2.  CONFIGURED ASSET ROW -- These are highlighted in red.

3.  DELETE DUPLICATES -- This option deletes all the rows with configured assets in one instance.

4.  NEXT STEP -- This option remains disabled unless the user removes all configured assets.

![Configure Custom Insight Category window showing Asset selection page with option to delete selected asset](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image29.png)

#### Edit Configuration

When the user clicks on *Edit* on the selected Predictive Failure configuration row, it redirects to the Configuration screen.

![Option to edit configuration](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image30.png)

The following image depicts the Configuration screen. The dropdowns are already populated with the previously saved data.

![Configure Custom Insight Category window showing the option to Edit the Configuration ](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image31.png)

Clicking on the *NEXT STEP* button allows the addition or removal of Impacted KPIs.

![Edit Configurations page showing the Impacted KPIs to edit/select](./media/IAI_Intelligent_Advisor_Configuration_UI_Guide/image32.png)
