---
sidebar_position: 2
title: DT CDC Debezium Connector
hide_title: true
---

<div class="doc-title-block">
<p class="doc-asset-name">DIGITAL THREAD FOUNDATIONS</p>
<p class="doc-topic">CDC Debezium Connector</p>
<p class="doc-type">OVERVIEW</p>
</div>

<p class="doc-version">Release Version: 1.2</p>


## Introduction

A digital thread refers to the continuous and consistent flow of information throughout the entire lifecycle of a product or system - from design and development to operation and maintenance. It enables the integration of data from different stages and sources, allowing effective traceability, seamless collaboration, and efficient decision-making by unleashing the power of sleeping data. The digital thread is considered a key aspect of Industry 4.0 and the digital transformation of the manufacturing industry. It is the core of what we call the Enterprise Operating System (EOS). Digital Thread is a communication framework that helps integrate various enterprise systems involved in the engineering and manufacturing product life cycle.

Change Data Capture (CDC) is a process that captures and streams changes in data sources to downstream systems in real-time. IX Digital Thread utilizes CDC connectors to ensure that data flows seamlessly across various stages of the product lifecycle, enabling timely insights and decisions. The Debezium connector is an open-source tool designed to facilitate CDC by streaming real-time changes from various databases to downstream systems such as Kafka and EventHub. In the context of IX Digital Thread the Debezium Connector is used to efficiently monitor databases for changes, such as inserts, updates, and deletes, without requiring intrusive modifications to the database itself. By streaming these changes to platforms like Kafka and EventHub, Debezium enables maintaining a consistent and up-to-date view of data. This capability not only enhances data accuracy and traceability but also facilitates improved collaboration and faster decision-making across teams, reinforcing the integrity of the digital thread.

### Purpose

This document provides a comprehensive guide on how to create and use the Debezium connector with Postman to stream data changes from SQL Server to Kafka and EventHub. Additionally, it outlines the necessary steps for updating the connector settings and monitoring the data flow to maintain optimal performance and accuracy.

###  Target Audience

Software architects, developers, and integrators with IT backgrounds.

### Related Links

-   [IX Digital Thread Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=ix%20digital%20thread)

-   [HTTP Connector](https://github.com/castorm/kafka-connect-http)

-   [Debezium Official Documentation](https://debezium.io/documentation/reference/stable/connectors/sqlserver.html)

### Business Contacts

-   [florian.tournier@accenture.com](mailto:florian.tournier@accenture.com)

-   [laura.mosconi@accenture.com](mailto:laura.mosconi@accenture.com)

-   [karthik.ramachandra@accenture.com](mailto:karthik.ramachandra@accenture.com)

### Technical Contacts

-   [laura.mosconi@accenture.com](mailto:laura.mosconi@accenture.com)

-   [stefano.giacco@accenture.com](mailto:stefano.giacco@accenture.com)

-   [rushna.jabi@accenture.com](mailto:rushna.jabi@accenture.com)

### Glossary


| **Term** | **Definition** |
| --- | --- |
| Debezium | An open-source distributed platform for change data capture (CDC) that streams all database changes in real time. |
| Kafka | A distributed streaming platform used to build real-time data pipelines and streaming applications. |
| EventHub | A big data streaming platform and event ingestion service that can receive and process millions of events per second. |
| Connector | A component that integrates Debezium with source databases and sinks, enabling change data capture and streaming. |
| Change Data Capture (CDC) | A technique for identifying and capturing changes made to data in a database so that downstream systems can respond in real time. |
| Zookeeper | A centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services, often used with Kafka. |

## 

# Prerequisites

The following prerequisites are required to create the Debezium connector. Accesses required can be obtained by reaching out to the Technical Contacts.


| \# | Prerequisite |
| --- | --- |
| 1 | Install kafka_2.12-3.5.1 .\\bin\\windows\\zookeeper-server-start.bat .\\config\\zookeeper.properties .\\bin\\windows\\kafka-server-start.bat .\\config\\server.properties |
| 2 | Access to EventHub |
| 3 | APIM subscription key is required for the management of APIs, allowing for secure access, monitoring, and version control. |
| 4 | ADX |
| 5 | Kubernate access for logs : kubectl get pods -n prod kubectl logs -n prod ix-kafka-debezium-6fc5fb8f79-rtpjq |
| 6 | Token generation link access b2c link access |
| 7 | Script to generate an authorization token ./newdev_azurefunction.sh |
| 8 | Postman |
| 9 | Azure Client VPN |
| 10 | Kusto Query let \_startTime = datetime(2024-03-08T09:01:58Z); let \_endTime = datetime(2024-04-18T09:01:58Z); utilization_table |
|  | \ | where (unixtime_nanoseconds_todatetime(tolong(after.event_time_utc))) between (\[\'\_startTime\'\] .. \[\'\_endTime\'\]) and after.ent_id == 5 and after.reas_cd == 69 where isnotnull(after.event_time_utc) project event_time = (unixtime_nanoseconds_todatetime(tolong(after.event_time_utc))), reas_cd = toint(after.reas_cd), adx_time = unixtime_milliseconds_todatetime(tolong(ts_ms)) order by event_time asc take 5 |
| 11 | [HTTP Connector](https://github.com/castorm/kafka-connect-http) |



## API Management Service

In this service, several APIs are configured to streamline functionality and enhance integration.

### CDC API Configuration

-   API Name: cdc-api

-   Methods Available:

    -   GET: Used for retrieving the created connectors from the CDC service.

    -   POST: Utilized to Create connector.

    -   DELETE: Used to delete the connector.

![Screenshot of CDC API Configurations in APIM ](./media/DT_CDC_Debezium_Connector/image2.png)

## 

# Create Debezium Connector

### Azure VPN

To access the SQL Server, users must first connect to the designated Virtual Machine (VM). This is essential for ensuring secure and controlled access to the database.

**Steps to Connect:**

1.  Coordinate with the Infrastructure Team to gain access to the VM.

2.  Request the necessary credentials (username and password) to log in to the VM.

3.  Use a remote desktop application (RDP for Windows or SSH for Linux) to connect to the VM.

4.  Launch SQL Server Management Studio (or your preferred SQL client) on the VM.

5.  Use the provided credentials to securely connect to the SQL Server instance.

![Screenshot of Azure VPN Client](./media/DT_CDC_Debezium_Connector/image3.png)

### Remote access

The user connects to the VM using Remote Desktop Connection, logs in with their credentials and then opens SQL Server Management Studio (SSMS). By selecting Windows Authentication, they can access SQL Server without needing a username or password, as it will be accessible directly.\
![Remote desktop connection window](./media/DT_CDC_Debezium_Connector/image4.png)

### Update util_history file

After gaining SQL access to the ix-dev-MESDB, you will find a table named util_history. You can update the reas_cd and event_time_local values either by using an SQL query or manually by right-clicking on the table and selecting the edit option available.

![Microsoft SQL Server Management Studio window](./media/DT_CDC_Debezium_Connector/image5.png)

![util_history file](./media/DT_CDC_Debezium_Connector/image6.png)

### 

## Create the Connector

Use Postman to create a Debezium connector for monitoring changes in a SQL Server database as follows:

1.  Open Postman.

2.  Set the Request Type

3.  Enter the Endpoint 

4.  Add Headers

    -   Ocp-Apim-Subscription-Key: 48d02ddb432xxxxxa0c5bc3b376a8fb1 (reach out to an admin/technical contact for the key value)

    -   Authorization: \{Bearer token\}

5.  Add the Request Body

6.  Click on the Body tab and select Raw. Choose JSON from the dropdown.

7.  Input the JSON configuration shown right.

8.  Send the Request

9.  Check the Response: Review the response to ensure the connector was created successfully.

10. Create Debezium Connector: After sending the request to create the Debezium connector, you should receive a [response](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/IX%20Thread/Linked%20Files/DT_Debezium_Connector_Response.txt) with a 201 Created status code. This indicates that the connector was successfully created.

![Postman screenshot showing how to create the Connector](./media/DT_CDC_Debezium_Connector/image7.png)

### Get Available Connectors

To retrieve a list of all available connectors:

1.  Open Postman.

2.  Set the Request Type: GET

3.  Enter the Endpoint: 

4.  Click on the Headers tab and add the following key-value pairs:

    a.  Ocp-Apim-Subscription-Key: 48d02ddb432xxxxxa0c5bc3b376a8fb1

    b.  Authorization: \{Bearer token\}

5.  Click the Send button to submit your request.

6.  Check the response pane to view the list of available connectors.

![Postman showing the get_connectors query](./media/DT_CDC_Debezium_Connector/image8.png)

### Get Connector Status

To check the status of a specific connector:

1.  Open Postman

2.  Set the Request Type: GET

3.  Enter the Endpoint: [https://ix-dev-apimgmt.azure-api.net/cdc-api/connectors/\{connector_name\}/status](https://ix-dev-apimgmt.azure-api.net/cdc-api/connectors/%7bconnector_name%7d/status)

4.  Click on the Headers tab and add the following key-value pairs:

    a.  Ocp-Apim-Subscription-Key: 48d02ddb432xxxxxa0c5bc3b376a8fb1

    b.  Authorization: \{Bearer token\}

5.  Click \'Send\'

6.  Check the response pane for the status code and details about whether the connector\'s current state will be in a running or failed state.

![Postman screenshot that shows the GET connector status](./media/DT_CDC_Debezium_Connector/image9.png)

## 

# Generate Topic

After creating the Debezium connector, Azure Event Hub automatically generates a topic as shown in the image below.

Azure Event Hub is a managed real-time data ingestion service that enables high-throughput and low-latency collection of large volumes of data from various sources. It is ideal for big data analytics and event streaming, with seamless integration into other Azure services for scalable event processing.

![eventhub automatically generates a topic](./media/DT_CDC_Debezium_Connector/image10.png)

## Analyze Data

The topic automatically created in EventHub should be selected to access the \"Analyze Data\" option, as illustrated in the screenshot.\
![screenshot of eventhub showing \'analyze data\' option](./media/DT_CDC_Debezium_Connector/image11.png)

## 

# Ingest Data

### Destination 

**Cluster Subscription:**

Select the appropriate subscription where the cluster resides. In the screenshot, the subscription is set to Industry X Digital Thread Component.

**Cluster:**

Specify the Azure Data Explorer (ADX) cluster for ingestion. In this case, the cluster is selected as ix-dev-adx.westeurope.

**Database:**

Choose the database within the cluster where the data will be ingested. Here, the selected database is kafka-connect.

**Table:**

Select the destination table where the data should be ingested. You can choose an existing table or create a new table. In the example, the existing table chosen is utilization_table.

![destination tab](./media/DT_CDC_Debezium_Connector/image12.png)

### Source 

**Data Connection Name:**

Automatically generated as kafka-connect-avevames-ix-dev-MESDB. This name links the Event Hub to your Kafka connection for data analysis.

**Event Hub:**

The Event Hub is automatically selected based on the data connection. This is where the data will be ingested.

**Consumer Group:**

The default consumer group is selected, which will handle data processing.

![source tab](./media/DT_CDC_Debezium_Connector/image13.png)

### Schema 

No action is required in the Schema tab, so simply review the auto-generated schema and click Next to proceed. The system will automatically handle the schema mapping based on the selected source and destination.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

After the ingestion process, you will be redirected to Azure Data Explorer to verify the data ingestion. Navigate to the ADX cluster ix-dev-adx.westeurope.

![ADX cluster screenshot](./media/DT_CDC_Debezium_Connector/image16.png)

Under the database kafka-connect, you should see the data being ingested into the utilization_table from the Kafka Connect data connection.

![adx screenshot showing the databases](./media/DT_CDC_Debezium_Connector/image17.png)

![adx showing the kafka-connect database](./media/DT_CDC_Debezium_Connector/image18.png)

Clicking on Kafka Connect in ADX will show the linked Event Hub, confirming that the data connection is successfully created and operational.

![adx kafka-connect screenshot showing linked event hub](./media/DT_CDC_Debezium_Connector/image19.png)

![adx kafka connect data connections](./media/DT_CDC_Debezium_Connector/image20.png)

## Check Logs

To complete the ingestion setup, check the logs and monitor data changes in ADX as follows:

1.  Navigate to ADX Cluster ix-dev-adx.westeurope

2.  To access the database: inside the ADX cluster, locate the kafka-connect database. This is where the ingested data from Event Hub is stored.

3.  Click on Explore: In the Azure Data Explorer UI, click on the Explore button to open the query interface.

4.  Query Your Data: After clicking Explore, select Query Your Data. This will open a new window where you can write and execute queries to check the data.

![ADX screenshot showing option to query your data](./media/DT_CDC_Debezium_Connector/image21.png)

## Custom Queries

Custom Kusto queries can be used to view logs, monitor the data flow, or check changes in the SQL database. For example, you can run queries like:

![Azure data explorer - custom queries screen](./media/DT_CDC_Debezium_Connector/image22.png)

## Create a Dashboard 

After verifying the ingestion process and running queries. Create a dashboard in Azure Data Explorer (ADX) to visualize data and track results in real-time.

1.  Open Azure Data Explorer

2.  In the ADX interface, locate and click on the option to create a new Dashboard.

3.  Provide Dashboard Details:

    a.  Data Source Name: Enter the name of the data source you want to use.

    b.  Cluster URI: Enter the cluster URI where your data is stored. In this case, it would be: 

    c.  Database: Specify the database where the ingested data is located. In this case name is kafka-connect

    d.  Set Query Result Cache Max Age: For performance, you can set the Query Result Cache Max Age to 30 seconds.

4.  Click on the Create button to generate the dashboard.

5.  When the dashboard is created, we can start adding visual elements such as charts, tables, or graphs to monitor and visualize the data. We can customize these based on the queries we ran earlier to track real-time data.

> ![Azure Data explorer - create a new data source](./media/DT_CDC_Debezium_Connector/image23.png)
After creating the dashboard, write a Kusto Query (KQL) to fetch data, such as utilization_table. Select a visualization type like a pie or bar chart to display the results. Customize the chart as needed, and the dashboard will refresh automatically.

![dashboard showing visualization](./media/DT_CDC_Debezium_Connector/image24.png)
