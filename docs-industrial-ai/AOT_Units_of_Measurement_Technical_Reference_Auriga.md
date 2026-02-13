---
sidebar_position: 2
title: AOT Units of Measurement Technical Reference Auriga
---

**Accenture Operations Twin**

**Units of Measurement**

**TECHNICAL REFERENCE**

Release Version: 2.5

**Metadata Table**

  ---------------------------------------------------------------------------------------------------------------
               **Field**                                               **Value**
  ----------------------------------- ---------------------------------------------------------------------------
       **Asset / Solution Name**                   Accenture Operations Twin / Units of Measurement

           **Domain / Area**                                      Digital Twin / UoM

        **Owner (Team/Person)**                                    Tournier, Florian

             **Reviewers**                                     Ranganathan, Balamurugan

              **Status**                                         Complete / Published

          **Confidentiality**                                   Internal / Confidential

          **Source of Truth**                                     Summary - Overview

   **Related Assets / Alternatives**   Operations Hierarchy Deployment Guide, Operations Hierarchy API Reference
  ---------------------------------------------------------------------------------------------------------------

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Prerequisites [3](#prerequisites)](#prerequisites)

[Contacts [3](#contacts)](#contacts)

[Related Links [3](#related-links)](#related-links)

[Glossary [3](#glossary)](#glossary)

[Background [3](#background)](#background)

[UOM Conversion [4](#uom-conversion)](#uom-conversion)

[Percentage Comparison [5](#percentage-comparison)](#percentage-comparison)

[Units of Measurement Configuration APIs [5](#units-of-measurement-configuration-apis)](#units-of-measurement-configuration-apis)

[GET- GetUoMByUnitSystemAndType [6](#get--getuombyunitsystemandtype)](#get--getuombyunitsystemandtype)

[GET- GetUnitSystems [7](#get--getunitsystems)](#get--getunitsystems)

[GET- GetUoMConversions [8](#get--getuomconversions)](#get--getuomconversions)

[GET- GetUoM [9](#get--getuom)](#get--getuom)

[GET- GetUoMByUnitSystemId [10](#get--getuombyunitsystemid)](#get--getuombyunitsystemid)

[GET- GetUoMEquivalents [11](#get--getuomequivalents)](#get--getuomequivalents)

# Introduction

Accenture Operations Twin (AOT) is a collection of software accelerators and tools that can be assembled to deliver client solutions. AOT accelerates the integration of product, process, and live data from disparate IT and OT systems, creating a comprehensive and contextualized view of operations to enable better decisions and optimized processes.

The Units of Measurement Configuration module is an AOT component that helps in providing foundational information on Units of Measurement such as Unit Systems, Units of Measurement, and Units of Measurement conversion formulae that are utilized by AOT\'s Smart KPI and Intelligent Advisor components. This supports AOT in handling various units of measurements as per requirement.

## Purpose

This reference document includes information about the Middleware APIs that help in providing information on Units of Measurement like Unit Systems, Units of Measurement, and Units of Measurement Conversion Formulae that are utilized by other AOT components.

## Target Audience

This guide is designed for use by developers with the following skills:

-   SQL Server

-   API Management Service

##  Prerequisites

-   An API testing tool such as [Postman](https://app.getpostman.com/app/download/win64) can be used to test the APIs.

-   To fetch the response from certain APIs, the following entities must already exist:

    -   Authorization token

    -   unitSystemId

    -   unitType

    -   Query String

    -   source_uom_id

    -   destination_uom_id

    -   source_unitsystem_id

    -   destination_unitsystem_id

## Contacts

-   

-   

-   

## Related Links

-   [AOT Documentation](https://industryxdevhub.accenture.com/asset-home;search_text=aot)

-   [AOT Release Notes](https://industryxdevhub.accenture.com/assetdetails/45)

## 

## Glossary

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Term**                             **Definition**
  ------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------
  SQL Server                           A relational database management system developed by Microsoft, used for storing and retrieving data as requested by other software applications.

  API Management Service               A platform that helps organizations publish, secure, and manage APIs for internal and external consumption.

  AOT (Analytics Operations Toolkit)   A suite of applications and tools designed to support analytics operations, including handling units of measure and Smart KPIs.

  Unit of Measure (UoM)                A standard quantity used to specify measurements, such as kilograms, liters, or pieces, which may vary between configurations.

  Smart KPIs                           An application within AOT designed to manage and display key performance indicators, including handling mismatches in units of measure.

  KPI Config Template                  A configuration template in the Smart KPIs application used to set up parameters and their standard units of measure.

  Equivalent Value                     The converted value of a parameter or KPI, shown in the user\'s configured unit of measure to ensure consistency and usability.

  Unit System ID                       An identifier for a specific system of units, used to distinguish between standard and user-default unit systems.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Background

As per requirement, different or multiple units of measure (UoM) may be required to enhance usability of any application. Thus, AOT is designed to support multiple units of measure to handle mismatches and conversions between standard and configured values.

For instance, AOT\'s Smart KPIs application is designed to handle mismatches of UoM in the KPI Config Template and the KPI/parameter data. The app accomplishes this by calculating and displaying the equivalent values. In certain scenarios, the Smart KPIs application will display the equivalent value instead of the configured or standard value. For more information on the configuration template, refer to the [Smart KPIs Administration Guide](https://industryxdevhub.accenture.com/assetdetails/42).

# 

# UOM Conversion

As the first step, the Smart KPIs application captures and saves all the details required for any conversion which might be needed from the standard UoM to the configured or equivalent UoM. The formula used for the conversion is - (a + b\*x) /( c\*x + d), where \'x\' is the value to be converted. The details captured in this step are:

-   AOT Standard Unit System ID

-   Units of measure present in the AOT Standard Unit System

-   Unit System ID defaulted for the User

-   Units of measure present in the user-default Unit System

-   Equivalent UoM Mappings between various unit systems

-   Conversion data - a,b,c,d values required for the conversion using the above formula.

For each KPI Tile and Trendline, a Detail API call and a Trendline API call is made respectively which gives furthermore information that are needed for the conversion. Listed below are the parameters that are picked up from the Detail API response of each KPI -

-   StandardUoM: Standard unit of measure defined for the KPI

-   ConfiguredUoM: Unit of measure configured for the KPI in the template

-   UnitSystemID: Unit system ID of the KPI or the asset

For the KPI Tiles, the below procedure is followed for carrying out the conversion process for each of the attributes (Actual, Forecast, Target, Historical Benchmark and RAG) -

1.  Check if the unit system for the user is same as the unit system of the KPI, which is picked up from the Detail API response.\*

2.  If yes, check if the standard primary UoM (picked up from the Detail API response) is same as that of the configured UoM (picked up from the Detail API response).

3.  If no, convert the standard primary UoM to the configured UoM and show KPI attributes (Actual, Forecast etc..) in configured UoM, by using the following function:

> public static getConversionData (sourceUom, targetUoM, uomConversionData): any\{
>
> return uomConversionData?. UoMs?.filter((cpata) =\> \{
>
> return cData.fromUnitId === sourceUom && cData.toUnitId === targetUoM
>
> \})\[0\];
>
> \}

\*See also: [AOT People Management Integration with Smart KPIs](https://industryxdevhub.accenture.com/assetdetails/42)

**Where:**

-   sourceUom is the standardUoM returned in the response

-   targetUoM is the configuredUoM returned in the response

-   uomConversionData is the data fetched in the first step which contains list of all the a,b,c,d values for conversions between all possible source and target UoMs

As shown below, the result of this method will be one object that will contain the a,b,c,d values for the provided inputs.

> a: 0
>
> b: 2.20462
>
> c: 0
>
> d: 1
>
> fromUnitId: \"0508B9F1-CA9F-407D-8489-28A7A3EF09A0\"
>
> fromUnitName: \"Kilogram\"
>
> toUnitId: \"C1FCBC71-D966-4201-98D4-1A27FF809C37\"
>
> toUnitName: \"Pound\"

In-the-next-step,-the-conversion-is-done-using-the-above-a.b.c.d-values-and-the-formula-

> public static getConvertedValues (sourceValue, a,b,c,d) number \{ return (a + b\* sourceValue) / (c sourceValue + d);
>
> \}

If-no, identify-equivalent-UoM-of-the-configured-UoM-using-the-equivalent-mapping-data-fetched-in-the-first-step.

For-identifying-the-equivalent-UoM, the-below-method-is-used-

> public static fetchEquivalentUom (sourceUoMID, sourceUoM, targetUomID, equivalentUoMsList): any\{
>
> return equivalentUoMsList?.UoMEquivalents?.filter((item)=\>\{
>
> return item.source_unit_system_id === sourceUOMID &&
>
> item.destination_unit_system_id === targetUomID &&
>
> item.source_uom === sourceUoM
>
> \})\[0\];
>
> \}

In the example above, sourceloMID-is-the-configured-UoM.

**And:**

-   The-source-unit-system-would-be-unit-system-mapping-of-the-KPI identified-in-the-first-step.

-   Target-unit-system would be the unit-system-of-the-user-as-identified in the first-step.

-   The result of the function would-be-the-equivalent UoM-object as below:

> destination_unit system: \"Imperial unit system\"
>
> destination_unit system id: \"36A86650-4653-432C-AA20-010490387015
>
> destination_uon: \"Ib\"
>
> destination_uom id: \"CIFCBC71-0966-4201-9804-1A27FF80932
>
> source_unit_system: \"netric unit system\"
>
> source_unit_system id: \"31201098-5320-4564-4486-80CDED04A36\"
>
> source uom: \"g\" source_won_id: \"0591-CAF-4070-8180-287430940\"

Using the above-source-and-destination-os the conversion process is initiated by fetching the abud values and \"getConversion Values\" method-mentioned above.

Once the abcd values are fetched, the given input (Actual / Target / Forecast / Historical-Benchmark/RAG) value-is-converted using the get ConvertedValues method mentioned above.

For-Parameters,-the-above-process-remains the same except, the \"Configureduod\" parameter in the responses is replaced by \"SoutcelloM\" since we-do-not-have-Configure-LIOMs for parameters and the source UoM-comes as-a-feed-from-the-Source-systems.

# Percentage Comparison

Before a date has been selected in the Date picker, the percentage comparison is shown in the KPI tile. The percentage comparison is calculated as \[(current value - previous value)/previous value\]\*100.

-   If a date value other than Today is selected, the percentage comparison is not calculated and is hidden in the KPI tile.

-   If the percentage comparison value is positive, the arrow points upwards in the tile.

-   If the percentage comparison value is negative, the arrow points downwards in the tile.

-   The color of the arrow is dependent/based on the configuration provided in the KPI Config template or KPI config tool.

# Units of Measurement Configuration APIs

The Python-based Units of Measurement Configuration APIs listed below are built and hosted on a cloud-agnostic Kubernetes environment. End Users are provided access to these APIs via API Management (Azure Services), which also helps in User Authentication. See the related links section for more information on APIs.

Units of Measurement Configuration APIs are developed using Flask, which is a microweb framework. It uses an Object Relational Mapper (ORM) approach to communicate with the database. SQL Alchemy is the SQL toolkit that has been used to achieve the ORM approach.

The API described below should be used by providing the Authentication Token. All the time zones are in [Epoch time (UTC](https://www.epochconverter.com/)) format.

The configuration APIs to provide the information on Units of Measurement are as follows:


| > **API Name** | > **Description** |
| --- | --- |
| > GET- GetUoMByUnitSystemAndType | API for fetching the list of units based on unit system and unit type. |
| > GET- GetUnitSystems | API for fetching the list of all the unit systems in AOT. |
| > GET- GetUoMConversions | API for fetching the list of all unit conversions. |
| > GET- GetUoM | API for fetching the unit of measurement details. |
| > GET- GetUoMByUnitSystemId | API for fetching the list of UoM by using unit system ID. |
| > GET- GetUoMEquivalents | API for fetching a list of UoM Equivalents in other unit systems of a particular UoM by using source UoM ID, source Unit System ID, Destination UoM ID, and Destination Unit System ID. |


The APIs listed in the table above are described on the pages that follow.

## 

## GET- GetUoMByUnitSystemAndType

This API is used for fetching the list of units based on unit system and unit type.

### Specifications

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Content-Type Protocol                  HTTPS
  -------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PATH AOT (Cognite) (Public Exposure)   [https://apim-mw-aot-dev.azure-api.net/api/unit-of-measurement/metadata/measurementUnit/byunitsystemandtype?unitSystemId=\{unitSystemId\}&unitType=\{unitType\}](https://apim-mw-aot-dev.azure-api.net/api/unit-of-measurement/metadata/measurementUnit/byunitsystemandtype?unitSystemId=%7bunitSystemId%7d&unitType=%7bunitType%7d)

  PATH AOT (Azure) (Public Exposure)     https://apim-aot-azure-dev.azure-api.net/api/unit-of-measurement/metadata/measurementUnit/byunitsystemandtype?unitSystemId=\{unitSystemId\}&unitType=\{unitType\}

  METHOD                                 GET

  CONTENT TYPE                           application / json
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Header Parameters

  ------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                         M/O        Type
  ---------------- ----------------------------------------------------------------------------------- ---------- --------
  Authorization    Token acquired from Azure AD based on the user credentials for further API calls.   M          String

  Content-Type     Type of content. E.g.- application/json                                             M          String
  ------------------------------------------------------------------------------------------------------------------------

### Input Body Parameters

  -------------------------------------------------------------------------------------
  Parameter        Description                                      M/O        Type
  ---------------- ------------------------------------------------ ---------- --------
  unitSystemId     Provide a unique identifier of the unit system   M          String

  unitType         Provide the type of unit of measurement          M          String
  -------------------------------------------------------------------------------------

### Output Header Parameters

  -------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                                                           Type
  ---------------- --------------------------------------------------------------------------------------------------------------------- ----------
  Server           Contains information about how the server handles the request \[e.g., Werkzeug/2.1.2 Python/3.9.7\]                   String

  Content-Type     Type of the content                                                                                                   String

  Date             Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\]                                                  Datetime

  Content-Length   Length of the content                                                                                                 Bytes

  Connection       A general header specifying whether the current network connection stays open once the current transaction finishes   String
  -------------------------------------------------------------------------------------------------------------------------------------------------

### Output Body Parameters 

  ---------------------------------------------------------------------------------------------------------
  Parameter           Description                                                                  Type
  ------------------- ---------------------------------------------------------------------------- --------
  UoMId               Unique identifier of the unit of measurement                                 String

  MeasurementType     Type of the measurement corresponding to the unit of measurement             String

  MeasurementUnit     Unit of Measurement                                                          String

  MeasurementSystem   Unit System corresponding to the unit of measurement                         String

  DisplayName         The name of the unit that will be displayed as the unit name                 String

  Symbol              Symbol of the unit of measurement                                            String

  IsPrimary           Returns true if the unit of measurement is the Primary unit of measurement   String
  ---------------------------------------------------------------------------------------------------------

### Result

  ----------------------------------------------------------------------------------
  **HTTP Code**   **Result Description**
  --------------- ------------------------------------------------------------------
  200             The list of units based on unit system and unit type is fetched.

  ----------------------------------------------------------------------------------

### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | > Unauthorized User / Header Token could be missing |
| 400 | 400 | > Bad request |


### Sample JSON Responses

-   If the unit system is given as Null:

> \{ \"message\": \"Please enter valid unit system.\" \}

-   If the unit type is given as Null:

> \{ \"message\": \"Please enter valid unit type.\" \}

-   If the unit system and unit type are given as Null:

> \{ \"message\": \"Please enter valid unit system and unit type.\" \}

-   If the unit system is a non-null value but an invalid ID:

> \{ \"message\": \"Error occurred while retrieving unit of measurements\", \"error\": \"Given UnitSystem Id \[\\] is not a valid UUID, Please provide a valid UnitSystemId to process.\" \}

-   If the unit system and unit type are valid:

> \{ \"UoMs\": \[ \{ \"UoMId\": \"\", \"MeasurementType\": \"\", \"MeasurementUnit\": \"\", \"MeasurementSystem\": \"\", \"DisplayName\": \"\", \"Symbol\": \"\", \"IsPrimary\": \"\" \} \] \}

## 

## GET- GetUnitSystems

This API is used for fetching the list of all the unit systems in AOT.

### Specifications

  --------------------------------------------------------------------------------------------------------------------------------------------
  PROTOCOL                               HTTPS
  -------------------------------------- -----------------------------------------------------------------------------------------------------
  PATH AOT (Cognite) (Public Exposure)   

  PATH AOT (Azure) (Public Exposure)     

  METHOD                                 GET

  CONTENT TYPE                           application / json
  --------------------------------------------------------------------------------------------------------------------------------------------

### Input Header Parameters

  ------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                         M/O   Type
  --------------- ----------------------------------------------------------------------------------- ----- --------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls.   M     String

  Content-Type    Type of content. E.g.- application/json                                             M     String
  ------------------------------------------------------------------------------------------------------------------

### Output Header Parameters

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                                                            Type
  ---------------- ---------------------------------------------------------------------------------------------------------------------- ----------
  Server           Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\]                       String

  Content-Type     Type of the content                                                                                                    String

  Date             Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\]                                                   Datetime

  Content-Length   Length of the content                                                                                                  Bytes

  Connection       A general header specifying whether the current network connection stays open once the current transaction finishes.   String
  --------------------------------------------------------------------------------------------------------------------------------------------------

### Output Body Parameters

  --------------------------------------------------------------------------------------------------------------------------------
  Parameter              Description                                                                                      Type
  ---------------------- ------------------------------------------------------------------------------------------------ --------
  Id                     Unique identifier of the unit system                                                             String

  UnitSystem             Name of the unit system                                                                          String

  Description            Description of the unit system                                                                   String

  IsStandardUnitSystem   Returns true if the unit system is an AOT Standard unit system                                   String

  CreatedOn              Date of creation of the unit system in the units of measurement database                         String

  CreatedById            User ID of the user who created the unit system in the units of measurement database             String

  CreatedByUserName      The username of the user who created the unit system in the units of measurement database        String

  UpdatedOn              Date of last update of the unit system in the units of measurement database                      String

  UpdatedById            User ID of the user who last updated the unit system in the units of measurement database        String

  UpdatedByUserName      The username of the user who last updated the unit system in the units of measurement database   String
  --------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  HTTP Code       Result Description
  --------------- -------------------------------------------------------
  200             A list of all the unit systems in AOT is fetched.

  -----------------------------------------------------------------------

### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | > Unauthorized User / Header Token could be missing |
| 400 | 400 | > Bad request |


### Sample JSON Response

\{

\"UoMSystems\" :

\[

\{

\"Id\":\"\",

\"UnitSystem\":\"\",

\"Description\":\"\",

\"IsStandardUnitSystem\": \"\",

\"CreatedOn\" :\"\",

\"CreatedById\" :\"\",

\"CreatedByUserName\" :\"\",

\"UpdatedOn\" :\"\",

\"UpdatedById\" :\"\",

\"UpdatedByUserName\" : \"\"

\}

\]

\}

## 

## GET- GetUoMConversions

This API is used for fetching the list of all unit conversions.

### Specifications

  ------------------------------------------------------------------------------------------------------------------------------------------------
  PROTOCOL                               HTTPS
  -------------------------------------- ---------------------------------------------------------------------------------------------------------
  PATH AOT (Cognite) (Public Exposure)   

  PATH AOT (Azure) (Public Exposure)     

  METHOD                                 GET

  CONTENT TYPE                           application / json
  ------------------------------------------------------------------------------------------------------------------------------------------------

### Input Header Parameters

  ------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                         M/O   Type
  --------------- ----------------------------------------------------------------------------------- ----- --------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls.   M     String

  Content-Type    Type of content. E.g.- application/json                                             M     String
  ------------------------------------------------------------------------------------------------------------------

### Output Header Parameters

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                                                            Type
  ---------------- ---------------------------------------------------------------------------------------------------------------------- ----------
  Server           Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\]                       String

  Content-Type     Type of the content                                                                                                    String

  Date             Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\]                                                   Datetime

  Content-Length   Length of the content                                                                                                  Bytes

  Connection       A general header specifying whether the current network connection stays open once the current transaction finishes.   String
  --------------------------------------------------------------------------------------------------------------------------------------------------

### Output Body Parameters

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter      Description                                                                                                                                 Type
  -------------- ------------------------------------------------------------------------------------------------------------------------------------------- --------
  fromUnitId     Unique identifier of the unit of measurement which needs to be converted                                                                    String

  fromUnitName   Name of the unit of measurement which needs to be converted                                                                                 String

  toUnitId       Unique identifier of the unit of measurement to which the unit needs to be converted                                                        String

  toUnitName     Name of the unit of measurement to which the unit needs to be converted                                                                     String

  a              Value of \'a\' variable in standard conversion formula i.e. (a+bx)/(cx+d) where x is the value in source unit which needs to be converted   Float

  b              Value of \'b\' variable in standard conversion formula i.e. (a+bx)/(cx+d) where x is the value in source unit which needs to be converted   Float

  c              Value of \'c\' variable in standard conversion formula i.e. (a+bx)/(cx+d) where x is the value in source unit which needs to be converted   Float

  d              Value of \'d\' variable in standard conversion formula i.e. (a+bx)/(cx+d) where x is the value in source unit which needs to be converted   Float
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------
  HTTP Code    Result Description
  ------------ ----------------------------------------------------------
  200          A list of all the unit conversions is fetched.

  -----------------------------------------------------------------------

### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | > Unauthorized User / Header Token could be missing |
| 400 | 400 | > Bad request |


**Sample JSON Response**

\{

\"UoMs\": \[

\{

\"fromUnitId\": \"\",

\"fromUnitName\":\"\",

\"toUnitId\": \"\",

\"toUnitName\": \"\",

\"a\": 0.0,

\"b\": 0.001,

\"c\": 0.0,

\"d\": 1.0

\}

\]

\}

## 

## GET- GetUoM

This API is used for fetching the unit of measurement details.

### Specifications

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PROTOCOL                               HTTPS
  -------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  PATH AOT (Cognite) (Public Exposure)   [https://apim-mw-aot-dev.azure-api.net/api/unit-of-measurement/metadata/measurementUnit?QueryString=\{QueryString\}]\{.underline\}

  PATH AOT (Azure) (Public Exposure)     [https://apim-aot-azure-dev.azure-api.net/api/unit-of-measurement/metadata/measurementUnit?QueryString=\{QueryString\}]\{.underline\}

  METHOD                                 GET

  CONTENT TYPE                           application / json
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Input Header Parameters

  ---------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                         M/O      Type
  --------------- ----------------------------------------------------------------------------------- -------- --------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls.   M        String

  Content-Type    Type of content. E.g.- application/json                                             M        String
  ---------------------------------------------------------------------------------------------------------------------

### Input Body Parameters

  ---------------------------------------------------------------------------------------------------------------
  Parameter     Description                                                                     M/O      Type
  ------------- ------------------------------------------------------------------------------- -------- --------
  QueryString   Provide measurement unit, display name or symbol of the unit as a QueryString   M        String

  ---------------------------------------------------------------------------------------------------------------

### Output Header Parameters

  --------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                                                            Type
  ---------------- ---------------------------------------------------------------------------------------------------------------------- ----------
  Server           Contains information about how the server handles requests \[e.g., Werkzeug/2.1.2 Python/3.9.7\]                       String

  Content-Type     Type of the content                                                                                                    String

  Date             Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\]                                                   Datetime

  Content-Length   Length of the content                                                                                                  Bytes

  Connection       A general header specifying whether the current network connection stays open once the current transaction finishes.   String
  --------------------------------------------------------------------------------------------------------------------------------------------------

### Output Body Parameters

  ---------------------------------------------------------------------------------------------
  Parameter         Description                                                        Type
  ----------------- ------------------------------------------------------------------ --------
  UoMId             Unique identifier of the unit of measurement                       String

  MeasurementType   Type of the measurement corresponding to the unit of measurement   String

  MeasurementUnit   Unit of Measurement                                                String

  DisplayName       The name of the unit that will be displayed as the unit name       String

  Symbol            Symbol of the unit of measurement                                  String
  ---------------------------------------------------------------------------------------------

### Result

  ---------------------------------------------------------------------------------------------
  HTTP Code             Result Description
  --------------------- -----------------------------------------------------------------------
  200                   The Unit of Measurement is fetched based on the provided QueryString.

  ---------------------------------------------------------------------------------------------

### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | > Unauthorized User Header Token could be missing |
| 400 | 400 | > Bad request |


**Sample JSON Response**

\{

\"UoMId\":\"\",

\"MeasurementType\":\"\",

\"MeasurementUnit\":\"\",

\"DisplayName\":\"\",

\"Symbol\":\"\"

\}

## 

## GET- GetUoMByUnitSystemId

This API is used for fetching the list of UoM by using unitSystemId.

### Specifications


| ### PROTOCOL | ### HTTPS |
| --- | --- |
| ### PATH AOT (Cognite) (Public Exposure) | ### https://apim-mw-aot-dev.azure-api.net/api/unit-of-measurement/measurementUnits/byUnitSystemId/\{unitSystemId\} |
| ### PATH AOT (Azure) (Public Exposure) | ### https://apim-aot-azure-dev.azure-api.net/api/unit-of-measurement/measurementUnits/byUnitSystemId/\{unitSystemId\} |
| ### METHOD | ### GET |
| ### CONTENT TYPE | ### application / json |


### Input Header Parameters

  ----------------------------------------------------------------------------------------------------------------------
  Parameter       Description                                                                         M/O       Type
  --------------- ----------------------------------------------------------------------------------- --------- --------
  Authorization   Token acquired from Azure AD based on the user credentials for further API calls.   M         String

  Content-Type    Type of content. E.g.- application/json                                             M         string
  ----------------------------------------------------------------------------------------------------------------------

### Input Body Parameters

  --------------------------------------------------------------------------------------
  Parameter      Description                                          M/O       Type
  -------------- ---------------------------------------------------- --------- --------
  unitSystemId   Provide unique identifier of existing unit system.   M         String

  --------------------------------------------------------------------------------------

### Output Header Parameters

  -------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter        Description                                                                                                           Type
  ---------------- --------------------------------------------------------------------------------------------------------------------- ----------
  Server           Contains information about how the server handles the request \[e.g., Werkzeug/2.1.2 Python/3.9.7\]                   String

  Content-Type     Type of the content                                                                                                   String

  Date             Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\]                                                  Datetime

  Content-Length   Length of the content                                                                                                 Bytes

  Connection       A general header specifying whether the current network connection stays open once the current transaction finishes   String
  -------------------------------------------------------------------------------------------------------------------------------------------------

### Output Body Parameters

  ---------------------------------------------------------------------------------------------------------
  Parameter           Description                                                                  Type
  ------------------- ---------------------------------------------------------------------------- --------
  UoMId               Unique identifier of the unit of measurement                                 String

  MeasurementType     Type of the measurement corresponding to the unit of measurement             String

  MeasurementUnit     Unit of Measurement                                                          String

  MeasurementSystem   Unit System corresponding to the unit of measurement                         String

  DisplayName         The name of the unit that will be displayed as the unit name                 String

  Symbol              Symbol of the unit of measurement                                            String

  IsPrimary           Returns true if the unit of measurement is the Primary unit of measurement   String
  ---------------------------------------------------------------------------------------------------------

### Result

  -------------------------------------------------------------------------------------------
  HTTP Code   Result Description
  ----------- -------------------------------------------------------------------------------
  200         A list of Units of Measurement is fetched based on the provided unitSystemId.

  -------------------------------------------------------------------------------------------

### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | > Unauthorized User / Header Token could be missing |
| 400 | 400 | > Bad request |


### Sample JSON Response

\{

\"UoMs\": \[

\{

\"UoMId\":\"\",

\"MeasurementType\":\"\",

\"MeasurementUnit\":\"\",

\"MeasurementSystem\":\"\",

\"DisplayName\":\"\",

\"Symbol\":\"\",

\"IsPrimary\": \"\"

\}

\]

\}

## 

## GET- GetUoMEquivalents

This API fetches the list of UoM Equivalents in other unit systems of a particular UoM by using the source UoM ID, source Unit System ID, Destination UoM ID, and Destination Unit System ID.

### Specifications


| ### PROTOCOL | ### HTTPS |
| --- | --- |
| ### PATH AOT (Cognite) (Public Exposure) | ### |
| ### PATH AOT (Azure) (Public Exposure) | ### |
| ### METHOD | ### GET |
| ### CONTENT TYPE | ### application / json |


### Input Header Parameters

  --------------------------------------------------------------------------------------------------------------------------
  Parameter           Description                                                                         M/O       Type
  ------------------- ----------------------------------------------------------------------------------- --------- --------
  Authorization       Token acquired from Azure AD based on the user credentials for further API calls.   M         String

  Content-Type        Type of content. E.g.- application/json                                             M         String
  --------------------------------------------------------------------------------------------------------------------------

### Input Query Parameters

  -----------------------------------------------------------------------------------------------------
  Parameter                   Description                                            M/O       Type
  --------------------------- ------------------------------------------------------ --------- --------
  source_uom_id               Provide uom_id of the source uom                       M         String

  destination_uom_id          Provide uom_id of the destination uom                  M         String

  source_unitsystem_id        Provide unitsystem_id of the source unit system        M         String

  destination_unitsystem_id   Provide unitsystem_id of the destination unit system   M         String
  -----------------------------------------------------------------------------------------------------

### Output Header Parameters

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter            Description                                                                                                           Type
  -------------------- --------------------------------------------------------------------------------------------------------------------- ----------
  Server               Contains information about how the server handles the request \[e.g., Werkzeug/2.1.2 Python/3.9.7\]                   String

  Content-Type         Type of the content                                                                                                   String

  Date                 Date of operation execution e.g. - \[Tue, 17 May 2022 06:30:16 GMT\]                                                  Datetime

  Content-Length       Length of the content                                                                                                 Bytes

  Connection           A general header specifying whether the current network connection stays open once the current transaction finishes   String
  -----------------------------------------------------------------------------------------------------------------------------------------------------

### Output Body Parameters

  ---------------------------------------------------------------------------------------
  Parameter                    Description                                       Type
  ---------------------------- ------------------------------------------------- --------
  source_unit_system_id        Unit System ID of the source unit system          String

  source_uom_id                UoM ID of the source UoM                          String

  destination_unit_system_id   Unit System ID of the destination unit system     String

  destination_uom_id           UoM ID of the destination                         String

  source_unit_system           Unit System ID of the source unit system          String

  source_uom                   UoM name of the source_uom                        String

  destination_unit_system      Unit system name of the destination unit system   String

  destination_uom              UoM name of the destination UoM                   String
  ---------------------------------------------------------------------------------------

### Result

  -----------------------------------------------------------------------------------------------------
  HTTP Code             Result Description
  --------------------- -------------------------------------------------------------------------------
  200                   A list of Units of Measurement is fetched based on the provided unitSystemId.

  -----------------------------------------------------------------------------------------------------

### Error Management


| HTTP Code | Error Code | Error Description |
| --- | --- | --- |
| 500 | 500 | Generic Error |
| 400 | 401 | > Unauthorized User / Header Token could be missing |
| 400 | 400 | > Bad request |


**Sample JSON Response**

\{

\"UoMEquivalents\":

\[

\{

\"source_unit_system_id\": \"\",

\"source_uom_id\": \"\",

\"destination_unit_system_id\": \"\",

\"destination_uom_id\": \"\",

\"source_unit_system\": \"\",

\"source_uom\": \"\",

\"destination_unit_system\": \"\",

\"destination_uom\": \"\"

\}

\]

\}
