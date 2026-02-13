---
sidebar_position: 2
title: AOT Smart KPIs UI Guide Auriga
---

**Accenture Operations Twin**

Smart KPIs

UI GUIDE

Release Version: 2.5

**Metadata Table**

  -----------------------------------------------------------------------------------------------------------------
  **Field**                           **Value**
  ----------------------------------- -----------------------------------------------------------------------------
  **Asset / Solution Name**           Accenture Operations Twin/ Smart KPIs

  **Domain / Area**                   Performance Metrics

  **Owner (Team/Person)**             Tournier, Florian

  **Reviewers**                       Gali, Hanuman

  **Status**                          Draft / Approved

  **Confidentiality**                 Internal / Confidential

  **Source of Truth**                 [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V)

  **Related Assets / Alternatives**   Smart KPIs API Reference, Smart KPIs Admin Guide
  -----------------------------------------------------------------------------------------------------------------

# Contents \{#contents .TOC-Heading\}

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[KPI Factors [3](#kpi-factors)](#kpi-factors)

[Actual Value [3](#actual-value)](#actual-value)

[Historical Benchmark [3](#historical-benchmark)](#historical-benchmark)

[Target Value [3](#target-value)](#target-value)

[Forecast [3](#forecast)](#forecast)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Dashboard [4](#dashboard)](#dashboard)

[OT and Non-OT KPIs [5](#section)](#section)

[Sorting KPIs [6](#sorting-kpis)](#sorting-kpis)

[Trend Timeline Graph [7](#trend-timeline-graph)](#trend-timeline-graph)

[KPI Comparison in Trend Timeline [8](#kpi-comparison-in-trend-timeline)](#kpi-comparison-in-trend-timeline)

[KPI Tiles [9](#kpi-tiles)](#kpi-tiles)

[Aggregated Data [10](#aggregated-data)](#aggregated-data)

[Contributing KPIs [11](#contributing-kpis)](#contributing-kpis)

[Parameters [11](#parameters)](#parameters)

[Errored KPI Tile [12](#errored-kpi-tile)](#errored-kpi-tile)

[Calendar and KPI Tiles [12](#calendar-and-kpi-tiles)](#calendar-and-kpi-tiles)

[Role-based KPI Drilldown [13](#role-based-kpi-drilldown)](#role-based-kpi-drilldown)

[KPI Drilldown Details [13](#kpi-drilldown-details)](#kpi-drilldown-details)

[Parameters Drilldown [14](#parameters-drilldown)](#parameters-drilldown)

[Access-based KPI Drilldown [16](#access-based-kpi-drilldown)](#access-based-kpi-drilldown)

[Non-OT KPI Drilldown Details [17](#non-ot-kpi-drilldown-details)](#non-ot-kpi-drilldown-details)

[Contributing KPIs [19](#contributing-kpis-1)](#contributing-kpis-1)

[Event Table [19](#event-table)](#event-table)

[Batch Table [19](#batch-table)](#batch-table)

[Trend Timeline [20](#trend-timeline)](#trend-timeline)

[Asset Downtimes [21](#asset-downtimes)](#asset-downtimes)

[Calendar and Trend Timelines [22](#calendar-and-trend-timelines)](#calendar-and-trend-timelines)

[Date Picker [23](#date-picker)](#date-picker)

[Hours Selection [23](#hours-selection)](#hours-selection)

[Day Selection [24](#day-selection)](#day-selection)

[Week Selection [24](#week-selection)](#week-selection)

[Month Selection [24](#month-selection)](#month-selection)

[Quarter selection [24](#quarter-selection)](#quarter-selection)

[Half Year Selection [24](#half-year-selection)](#half-year-selection)

[Year Selection [24](#year-selection)](#year-selection)

[Custom Range selection [25](#custom-range-selection)](#custom-range-selection)

[Pagination and Auto-refresh [26](#pagination-and-auto-refresh)](#pagination-and-auto-refresh)

[KPI Details on Intelligent Advisor [27](#kpi-details-on-intelligent-advisor)](#kpi-details-on-intelligent-advisor)

[KPI Details on Operations Hierarchy [28](#kpi-details-on-operations-hierarchy)](#kpi-details-on-operations-hierarchy)

[Digital Twin Assistant [30](#digital-twin-assistant)](#digital-twin-assistant)

[Troubleshooting [31](#troubleshooting)](#troubleshooting)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools, including Smart KPIs, that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

Key Performance Indicators (KPIs) are measurable factors that are tracked to gauge performance, stimulate actions, and drive business productivity. The factors listed in the table on the side are used to form each KPI.

Smart KPIs is a Micro Front-end application that is mounted to the AOT application and is the landing page of the AOT application. It provides contextualized views of KPIs to AOT users in both the boardroom and on the shop floor. The Smart KPIs application is invaluable for tracking performance issues as well as the actions taken to improve performance.

## Purpose

This guide explains how to use the AOT Smart KPIs UI after deployment.

## Target Audience

End users of the AOT UI

## Prerequisites

-   AOT has been deployed.

-   Google Chrome browser is installed.

-   The graphic resolution must be set to either 1920 or 1440.

## KPI Factors

The factors involved in calculating KPIs are listed below.

### Actual Value

> This is the current value of the KPI that is calculated using the actual calculation logic defined in the KPI config template.

### Historical Benchmark

> This is the best performance value observed in the last 12 months.

### Target Value

> This is the desired performance/value of the KPI.

### Forecast

> This is the forecast for the current time interval that is calculated as a 7-day moving average.

##  Contacts

-   

-   

## Related Links

-   [AOT on CDF](https://operationstwin.accenturedigitalplant.com/)

-   [AOT on Azure](https://aot-azure.accenturedigitalplant.com/)

-   [Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

-   [Deployment Guide](https://industryxdevhub.accenture.com/assetdetails/53)

-   [Administration Guide](https://industryxdevhub.accenture.com/assetdetails/42)

## Glossary

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**                          **Definition**
  --------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  AOT (Accenture Operations Twin)   A suite of software accelerators and tools, including Smart KPIs, that integrates product, process, and live data from IT and OT systems to provide a comprehensive view of operations for better decision-making.

  Smart KPIs                        Micro Front-end application within AOT that provides contextualized views of KPIs, enabling users to track performance issues and actions taken to improve performance. It is the landing page of the AOT application.

  KPI (Key Performance Indicator)   Measurable factors tracked to gauge performance, stimulate actions, and drive business productivity. KPIs are formed from specific factors listed in the guide.

  Contributing KPIs                 KPIs that influence or contribute to the calculation of a parent KPI.

  RAG Logic                         Visual representation of Actual data against Target using Red-Amber-Green status in KPI tiles.

  Intelligent Advisor               AI-powered assistant in Azure deployments, enabling interaction with operational data using natural language for insights and root-cause analysis.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dashboard

The Smart KPIs Dashboard is the landing page of the application and includes:

1.  Header, which has options to switch between the Dashboard, Twin Viewer, and Reports.

2.  App launcher icon that expands a side menu with the following options: Home, Overview, Intelligent Advisor, Twin Builder, Smart KPI, People Management, and Operations Hierarchy.

3.  Intelligent Advisor and Operations Hierarchy side panel.

4.  Dropdown to choose various KPI Departments, which are sorted alphabetically.

5.  KPI Tiles show the KPI data -- Actual, Target, Historical Benchmark, and Forecast. KPI data is refreshed automatically in batches using lazy loading.

6.  Date picker to choose time frames from eight different options.

7.  Search bar and filter options.

8.  Paginator to navigate through different tiles.

9.  Trend Timeline graph that plots the data based on the selected time frame, shows Insights on the graph and allows the export of the graph as an image or a Microsoft Excel spreadsheet. The trend timeline is discussed further in the next section.

10. When deployed in Azure, an AI-powered assistant enables interaction with real-time and historical operational data using natural language. It simplifies access to structured and unstructured data, providing contextual insights, KPIs, actions, and root-cause analysis to support faster and smarter decision-making across assets, roles, and plants.

> ![Dashboard of the Smart KPIs application in AOT](media/image2.png)\{width="12.71875in" height="5.46875in"\}

## 

## OT and Non-OT KPIs

The dashboard displays both OT (Operations Twin) and NON-OT Key Performance Indicators (KPIs), as shown in the screenshot below.

-   OT KPIs are computed based on real-time data.

-   Non-OT KPIs are derived from event-based data.

This design ensures a comprehensive view of performance metrics by integrating both real-time and event-driven data.

![OT and NON-OT KPIS](media/image4.png)\{width="12.926642607174104in" height="5.774191819772528in"\}

## Sorting KPIs

KPIs can be sorted on the dashboard as per the following options.

-   Best Performing. KPIs are sorted as per performance, from best to least. The NDA (no data available) tiles appear at the end, since their performance deviation cannot be calculated.

-   KPI Name. The KPIs are sorted by their names in alphabetical order, regardless of the data shown on the tiles, as the sorting is solely based on the KPI name.

> ![A screenshot of sorted KPIs](media/image5.png)\{width="13.395833333333334in" height="3.90625in"\}

# Trend Timeline Graph

The trend timeline is a graphical representation of KPI trend data. The X-axis represents the time frame, and the Y-axis represents units of data. Functions of this view include:

-   Filtering by KPI, Department, and Date.

-   Export to PNG and XLS.

-   Dynamic legends, counts, and export functions are automatically aligned with graph data.

The Trend Timeline chart shows the Actual, Target, Forecast, and Historical benchmark trend of the selected KPI for the selected period in the calendar. By default, it shows seven days of data. Hovering over the Asset ID or KPI Name displays a tooltip that displays the complete details.

![Trend timeline with the tooltip message that displays complete details](media/image6.png)\{width="13.327080052493438in" height="4.785715223097113in"\}

## 

## KPI Comparison in Trend Timeline 

The trend timeline graph can compare the trends of two KPIs for two selected parameters. The trend timeline comparison view can be enabled by selecting a KPI in the *Compare To* dropdown. The X-axis represents the time frame, and the Y-axis represents units of data for the selected KPIs. Functions of the view include:

-   Comparing two KPIs by parameters such as Actual, Forecast, Target, and Historical Benchmark.

-   Two parameters can be compared at a time.

-   Export to XLS.

-   Reset to a single graph view by using the Reset button.

![KPI comparison in Trend Timeline](media/image7.png)\{width="13.935482283464568in" height="4.5in"\}

# 

# 

# KPI Tiles

The Smart KPIs MFE application displays all the KPI-related data in the form of KPI Tiles. A KPI Tile includes:

-   The Asset Name and KPI name. The KPI name is displayed partially when the character length exceeds the KPI tile width. Hovering over the Asset Name displays a tooltip that shows the complete name.

-   The Actual, Forecast, Historical Benchmark, and Target values of a KPI.

-   The date on which Actual is calculated.

-   A visual representation of the Actual data against the Target that the KPI needs to reach in the form of a progress bar, based on RAG logic.



-   The percentage change in KPI performance.



-   Calculation frequency of the KPI

-   An error message if the data is not present.

> ![KPI Tile](media/image8.png)\{width="6.5in" height="3.9166666666666665in"\}

## 

## Aggregated Data

Except for parameter tiles, the calculation frequency of the KPI is displayed in all KPI tiles, regardless of any calendar selection.

-   If the calculation frequency of the parent is different than the calculation frequency of the contributing KPIs, then the contributing KPI tiles will show the aggregated data of the KPI for the time range in which the parent KPI is being calculated.

-   The influencing KPI tiles will show the latest data of the KPI by default and will not have aggregated data attributes.

-   The parameter tiles will show the aggregated data of the parameter in which the parent KPI is being calculated, whether there is a difference in the calculation frequencies or not.

The screenshot on the right shows the parent KPI, which has a calculation frequency of two hours.

***\
***![screenshot of parent kpi with calculation frequency of two hours](media/image9.png)\{width="8.018685476815397in" height="3.7083333333333335in"\}

## Contributing KPIs

The screenshot below shows the result of differing calculation frequencies between the Parent KPI (two hours) and the Contributing KPIs (one hour). The aggregated data is displayed on the KPI Tiles.

![Screenshot that shows the result of different calculation frequencies between the Parent and Contributing KPIs](media/image10.png)\{width="9.011628390201224in" height="3.4912849956255467in"\}

### Parameters

In the screenshot below, the parameter tiles show the aggregated data of the parameter in which the parent KPI is being calculated, despite the calculation frequency difference.

![aggregated data of the parameter in which the parent KPI is being calculated despite the calculation frequency difference.](media/image11.png)\{width="6.0in" height="2.95in"\}

### Errored KPI Tile

As shown in the screenshot on the right, for any time period that is selected, if the value corresponding to the KPI is not available in the time series, or if the actual values are not available for the selected time period, then an error message is displayed.

![Errored KPI Tile](media/image12.png)\{width="3.5520975503062115in" height="3.3892924321959756in"\}

## Calendar and KPI Tiles

Eight different time frames are available for selection:

-   Hour(s)

-   Day(s)

-   Week(s)

-   Month(s)

-   Quarter(s)

-   Half-Year(s)

-   Year(s)

-   Custom

Once a time period is selected, the KPI Tiles update the data accordingly. For example, if the Week(s) option is selected from the calendar drop-down menu and Calendar Week 19 is picked, then KPI data for that week is displayed in the tiles. Click on the following thumbnail to launch a video demonstration of this action.

![Video thumbnail for the calendar and KPI tiles video ](media/image13.png)\{width="8.146928040244969in" height="3.9872386264216972in"\}

## Role-based KPI Drilldown

The role assigned to the AOT user determines which KPIs are displayed on the dashboard. On drilling down, the corresponding Contributing and Influencing KPIs for that role will be displayed as well. A sensitivity tag can also be assigned to the roles and KPIs. The value of the sensitivity tag determines the visibility of KPI details as follows:

-   A contributing/influencing KPI will only be visible in the drill-down if the KPI has a sensitivity tag equal to Yes, and the AOT user role also has that tag.

-   If the AOT user has multiple roles, and any one of the roles has that sensitivity tag, then they will be able to see that contributing/influencing KPI.

-   The technical details of the sensitivity tag and its corresponding API can be found in the [AOT Smart KPIs API Reference document.](https://industryxdevhub.accenture.com/assetdetails/42)

## KPI Drilldown Details

Clicking on one of the KPI Tiles displayed on the Dashboard reveals details about the KPI that include:

-   A detailed description of the KPI

-   The Aggregation Logic used to compute that KPI

-   The role to which the KPI is assigned

-   Contributing KPIs of the selected KPI

-   Influencing KPIs of the selected KPI

-   Trend Timeline graph

-   Parameter tiles if they are one of the contributing/influencing KPIs

The breadcrumb controls at the top of the page may be used to drill down through the KPIs at various levels of granularity, starting at the Plant level. For example, selecting *X-Y:OEE* at the Plant level reveals corresponding Contributing and Influencing KPIs at the Unit level. Selecting a Contributing KPI at the Unit level reveals any Contributing and Influencing KPIs at the system level and so on until there are no Contributing or Influencing KPIs left to display. To see a demonstration, play the following video.

![Video thumbnail for KPI drilldown details functionality](media/image14.png)\{width="8.054972659667541in" height="3.73661198600175in"\}

An authorized AOT user can continue to drill down to the parameter level. When no further drilldown is possible, one of the following messages is displayed.

-   You\'ve reached the end of the KPI Hierarchy. No further drill-down is possible.

-   Further drill-down disabled due to access restrictions. Please contact admin to get the required access.

> ![KPI tiles with tooltip messages for no further drilldown possible](media/image15.png)\{width="7.463100393700787in" height="3.5232556867891516in"\}

## 

## Parameters Drilldown

-   

-   Parameters are the lowest level of drill-down, and thus, the AOT user will not be allowed to drill down further by clicking the parameter tile.

-   Parameters have *Actual* values as well as any *Forecast* and *Target* values. There is no historical benchmark data present for the Parameters.

-   Parameters will show the Forecast values if the data is available in the parameter time series.

-   Parameters do not have RAG values, and hence, there is no RAG status displayed on the tiles for Parameters.

![KPI and Parameter tile comparison](media/image16.png)\{width="7.549346019247594in" height="3.7536636045494314in"\}

-   

-   

-   The trend timeline graph for Parameters may be viewed by selecting any Parameter from the *Select KPI* dropdown.

-   Any two Parameters or KPIs with the Parameters may be compared using the Comparison view of the Trend Timelines.

-   Since there is no historical benchmark data present for Parameters, the trend timeline graph is plotted without the Historical Benchmark line. A screenshot of an example trend timeline graph for this case is shown below.

![Trend timeline for Parameters](media/image17.png)\{width="14.024139326334208in" height="4.616279527559055in"\}

## Access-based KPI Drilldown 

This functionality enables viewing the KPIs for which the user has owner access in the dashboard, even if the user does not have access to the asset. The user is also restricted from drilling down to the KPI from the dashboard in the above scenario. On hovering over the KPI, a tooltip message is displayed - \'Further drill down disabled due to access restrictions. Please contact Admin to get the required access.\'

On selecting an asset in the OH panel, the user can view the KPIs for which the user has owner/viewer access to the KPIs and If the user does not have access to the asset which has been selected (or the asset corresponding to the KPI), the user is restricted from drilling down further. On hovering over the KPI, the user gets to see a tooltip with the message: \"Further drill down disabled due to access restrictions. Please contact admin to get the required access.\"

![KPI tile that displays the message \'Further drill down disabled due to access restrictions. Please contact Admin to get the required access.\'](media/image18.png)\{width="4.288577209098863in" height="4.902191601049869in"\}

## 

## Non-OT KPI Drilldown Details 

Clicking on one of the Non-OT KPI Tiles displayed on the Dashboard reveals details about the KPI that include:

-   A detailed description of the KPI

-   The Aggregation Logic used to compute that KPI

-   The role to which the KPI is assigned

    Contributors of the selected KPI

![Non OT KPI drilldown details](media/image19.png)\{width="12.90625in" height="5.761719160104987in"\}

Further details displayed on scrolling down are:

-   Trend Timeline graph

-   Downtimes in the form of a bar or pie chart

![Non OT KPI drilldown details](media/image20.png)\{width="12.9375in" height="6.27083552055993in"\}

## 

## 

## Contributing KPIs

The drilldown page dynamically decides which table to show based on KPI type: Events Table for event KPIs, Batch Table (with expand/collapse) for batch KPIs.

### Event Table

When a Non‑OT KPI in the dashboard is clicked, the *Events Table* is displayed showing the corresponding event data.

![Contributing KPIs in tabular view](media/image21.png)\{width="12.678571741032371in" height="1.9472681539807524in"\}

If there is no data available, a message stating \'No Records Found\' will be displayed, as shown in the screenshot below.

![Events table showing \'no records found\' message](media/image22.png)\{width="12.77361111111111in" height="1.4642858705161854in"\}

### Batch Table

When a Non‑OT KPI in the dashboard is clicked, a Batch Table appears displaying the corresponding batch data, with each row expandable to reveal all attribute values for the selected Batch ID.

![Batch table](media/image23.png)\{width="12.638270997375328in" height="2.0595352143482066in"\}

## 

## Trend Timeline

The trend timeline graph for Parameters may be viewed by selecting any Parameter from the Select KPI dropdown.

Any two Parameters or KPIs with the Parameters may be compared using the Comparison view of the Trend Timelines.

Since there is no historical benchmark data present for Parameters, the trend timeline graph is plotted without the Historical Benchmark line. A screenshot of an example trend timeline graph for this case is shown below.

![Trend timeline](media/image24.png)\{width="13.677106299212598in" height="4.753312554680665in"\}

## 

## Asset Downtimes

-   

-   For Non-OT KPIs, the user can visualize the Contributors as a bar chart or a pie chart based on the configuration.

-   The charts are visualized based on the asset downtime reason and duration.

-   The screenshot below shows an example of a bar chart, where the X-axis represents downtime reasons, and the Y-axis represents the cumulative duration.

![Asset downtime bar chart](media/image25.png)\{width="7.411280621172353in" height="3.099757217847769in"\}

![asset downtime piechart](media/image26.png)\{width="10.25515748031496in" height="4.881582458442694in"\}

# Calendar and Trend Timelines

Smart KPIs display and plot trend timeline graphs based on any timeframe selected from the Date picker. For example, when selecting *OCT* from the Month(s) period in the Date picker, the trend timeline graph is plotted with the X-axis populated with 30 days of the selected month as shown below.

![Date picker to select time range to plot trend timeline graphs](media/image27.png)\{width="11.058139763779527in" height="3.686046587926509in"\}

![Calendar and trend timeline](media/image28.png)\{width="11.0in" height="3.5104166666666665in"\}

# 

## Date Picker

The Smart KPIs date picker supports eight different date and time ranges to select from:

-   Hours

-   Days

-   Weeks

-   Months

-   Quarters

-   Half-year

-   Years

-   Custom

![Date picker UI component](media/image29.png)\{width="3.151162510936133in" height="3.399010279965004in"\}

### 

### Hours Selection 

The hour picker allows the AOT user to select from an hour range from a list of hours that appears beside the date picker popup.

![Hours selection UI component](media/image30.png)\{width="3.1506944444444445in" height="3.0286154855643046in"\}

### 

### Day Selection

The day picker allows the selection of a particular day.

![Days selection UI component](media/image31.png)\{width="3.084905949256343in" height="3.1371937882764653in"\}

###  Week Selection

The week picker enables the selection of an entire week at a time.

![ Weeks selection UI component](media/image32.png)\{width="3.0in" height="3.137253937007874in"\}

###  Month Selection

The month picker allows the selection of a particular month.

![ Month selection UI component](media/image33.png)\{width="3.216981627296588in" height="3.1432600612423447in"\}

### 

### Quarter selection

The quarter picker allows the selection of an entire quarter at a time. Example: Q1 -- Jan, Feb, Mar.

![Quarter selection UI component](media/image34.png)\{width="3.055718503937008in" height="3.081395450568679in"\}

### Half Year Selection

The half-year picker allows the selection of half a year at a time.

![Half Year selection UI component](media/image35.png)\{width="2.9418602362204727in" height="2.9968591426071742in"\}

### Year Selection

The year picker allows the selection of a year from a range of 16 years ending at the current year.

![Year selection UI component](media/image36.png)\{width="3.4509055118110235in" height="3.0116283902012246in"\}

### 

### 

### Custom Range selection

The custom range picker allows the selection of a custom range from a range of 16 years ending at the current year.

![UI component for Custom range selection](media/image37.png)\{width="6.1046511373578305in" height="3.8998206474190726in"\}

# 

# Pagination and Auto-refresh

The number of KPIs loaded per page on the dashboard is selectable via the page size dropdown. Lazy loading will load the KPIs in batches of 4, 8, 12, 16, or 20, depending on the selection.

The video on the side demonstrates the pagination and KPIs loading.

On the dashboard, the KPI tiles are auto-refreshed based on the calculation frequency configured and thus display the latest data available for the KPI.

![Thumbnail for video for Pagination and Vertical scrolling.](media/image38.jpeg)\{width="6.39042760279965in" height="3.1744181977252843in"\}

The following images depict how a KPI tile auto-refreshes. A message \'fetching data\' is displayed while the latest data for the KPI tile is fetched.

![KPI Tile with data before auto-refresh](media/image39.png)\{width="2.8758825459317587in" height="2.720930664916885in"\}

![\"fetching data\" message that displays when data is autorefreshing](media/image40.jpeg)\{width="3.245152012248469in" height="2.5116272965879265in"\}

![KPI tile after auto-refresh](media/image41.png)\{width="2.942483595800525in" height="2.7441863517060368in"\}

The data auto-updates when CDF functions execute (perform KPI computations). If the KPI computations fail, then the data is not fetched, and the auto-refresh fails. An error message is shown in this scenario.

# 

# KPI Details on Intelligent Advisor 

Smart KPIs application allows drill down to an Intelligent Advisor (IA) Insight and viewing of the details of the KPI from which the Insight was generated. Contributing and influencing KPIs and Trend Timelines may also be viewed. The AOT user can also:

-   Drill down into the KPI details by clicking on the KPI tile in the Insight details screen.

-   Drill down on all the existing hierarchy of the KPI, e.g., the drill down starts from the unit level, or plant level, depending on which level that insight was triggered on.

-   View the calculation frequencies of the drilled-into KPI and its contributing/influencing KPIs.

-   View the Historical benchmark and Forecast values of all the KPIs on the drilldown page.

-   View all the details of the parameters (Actual, Target, Forecast, Historical Benchmark, Aggregated Value), if they are present on the drilldown page.

To see a demonstration, play the video on the side.

Technical details about event-based communication can be found in the KPI Hierarchy and Calculation Technical Overview [here](https://industryxdevhub.accenture.com/assetdetails/42).

\
![Video thumbnail for KPI Details on Intelligent Advisor ](media/image42.png)\{width="7.263141951006125in" height="3.4077799650043743in"\}

# 

# KPI Details on Operations Hierarchy

As shown in the screenshot below, KPIs for an asset selected in the Operations Hierarchy pane are displayed in the main pane.

![OH Integration: KPIs for an asset selected in the Operations Hierarchy pane are displayed in the main pane. ](media/image43.png)\{width="11.679245406824148in" height="5.352987751531058in"\}

If an asset has been selected in the OH, the UI will filter all the departments present for that Asset and sort them alphabetically.

-   If there are KPIs configured for the already selected department and the selected asset, the same department will remain selected, and the KPIs corresponding to that department will be displayed.

-   If there are no KPIs configured for the previously selected department and the selected asset, but there are KPIs configured for other departments, the first department in the sorted department list will be selected, and the previously selected department will be removed from the list. The following video depicts this.

> ![video thumbnail of OH_Integration](media/image44.jpeg)\{width="5.649540682414698in" height="3.1770833333333335in"\}

The AOT user must have the appropriate access and meet the sensitivity requirements to view the KPIs. If no KPIs match the AOT user\'s role, then an error will be displayed as shown in the screenshot on the right.

![screenshot of access issue error](media/image45.png)\{width="3.779069335083115in" height="2.343844050743657in"\}

As shown below, drilling down into an asset that has a configured KPI displays the KPI detail of the selected asset.

![A screenshot that shows drilling down into an asset that has a configured KPI which displays the KPI detail of the selected asset.](media/image46.png)\{width="12.639535214348207in" height="5.687790901137358in"\}

# Digital Twin Assistant

In Azure deployments, clicking the robot icon in the ribbon launches an AI-powered assistant within AOT that enables interaction with real-time and historical operational data using natural language. It simplifies access to structured and unstructured data, providing contextual insights, KPIs, actions, and root-cause analysis to support faster and smarter decision-making across assets, roles, and plants.

![Digital Twin Assistant panel expanded which prompts to get started](media/image47.png)\{width="4.5in" height="7.151388888888889in"\}

# Troubleshooting 

The following table lists errors encountered in the UI and the course of action to resolve them.

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Problem / Error Message**                                            **Resolution**
  ---------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------
  KPI Not Configured                                                     Check that the parent KPI has been configured.

  Access Issue                                                           Contact the admin to get the required access.

  You\'ve reached the end of the KPI hierarchy.                          No further drilldown is possible.

  Further drilldown disabled due to access restrictions.                 Contact the admin to get the required access.

  Inadequate access to view the KPI details.                             Contact the admin to get the required access.

  Parameters are not visible after a calendar selection has been made.   Select the parameter in the trend timeline drop-down to view its data for the selected timeframe.

  The dashboard does not display properly.                               Set the resolution of the browser to 1440 or 1920.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
