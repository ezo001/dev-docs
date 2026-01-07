---
id: aot-micro-front-end-mfe-development-guide-auriga
title: AOT Micro Front End MFE Development Guide Auriga
---

**Accenture Operations Twin**

Micro Frontend

DEVELOPMENT GUIDE

Release Version: 2.4

**Metadata Table**

| **Field** | **Value (Example)** |
|----|----|
| **Asset / Solution Name** | Accenture Operations Twin/Micro-Frontend |
| **Domain / Area** | Web Development/Software Architecture |
| **Owner (Team/Person)** | Tournier, Florian |
| **Reviewers** | Zoltani, Judit-Kinga |
| **Status** | Draft / Approved |
| **Confidentiality** | Internal / Confidential |
| **Source of Truth** | [Summary - Overview](https://dev.azure.com/DigitalPlantProject/Marilyn%20V) |
| **Related Assets / Alternatives** | AOT General Architecture Blueprint, AOT Azure Architecture Blueprint |

# Contents

[Introduction [3](#introduction)](#introduction)

[Purpose [3](#purpose)](#purpose)

[Target Audience [3](#target-audience)](#target-audience)

[Related Links [3](#related-links)](#related-links)

[Contacts [3](#contacts)](#contacts)

[Glossary [3](#glossary)](#glossary)

[Background [4](#background)](#background)

[Monolithic Approach [4](#monolithic-approach)](#monolithic-approach)

[Micro Frontend Concept [4](#micro-frontend-concept)](#micro-frontend-concept)

[Comparison to Micro Services [4](#comparison-to-micro-services)](#comparison-to-micro-services)

[Benefits [4](#benefits)](#benefits)

[Frontends Comparison [5](#frontends-comparison)](#frontends-comparison)

[Implementation Pattern [5](#implementation-pattern)](#implementation-pattern)

[Routing [5](#routing)](#routing)

[Composition [6](#composition)](#composition)

[Communication [6](#communication)](#communication)

[Common Mistakes [7](#common-mistakes)](#common-mistakes)

[General Rules [7](#general-rules)](#general-rules)

[AOT Architecture [8](#section-1)](#section-1)

[AOT Structure [8](#aot-structure)](#aot-structure)

[AOT Micro Frontends [9](#aot-micro-frontends)](#aot-micro-frontends)

[AOT Software Design Elements [10](#aot-software-design-elements)](#aot-software-design-elements)

[Single-SPA [10](#single-spa)](#single-spa)

[Framework [10](#framework)](#framework)

[How it Works [10](#how-it-works)](#how-it-works)

[Benefits of Single-SPA [10](#benefits-of-single-spa)](#benefits-of-single-spa)

[MFE Integration [11](#mfe-integration)](#mfe-integration)

[Configuration [11](#configuration)](#configuration)

[MFE Container [12](#mfe-container)](#mfe-container)

[Generate Component Module [12](#generate-component-module)](#generate-component-module)

[Route the Container Module to the Application [15](#route-the-container-module-to-the-application)](#route-the-container-module-to-the-application)

[Skeleton code for micro frontend [15](#skeleton-code-for-micro-frontend)](#skeleton-code-for-micro-frontend)

[Running the Codes [15](#running-the-codes)](#running-the-codes)

[Testing [16](#testing)](#testing)

[MFE Use Case – Smart KPIs [17](#mfe-use-case-smart-kpis)](#mfe-use-case-smart-kpis)

[Smart KPIs Library [17](#smart-kpis-library)](#smart-kpis-library)

[KPI Tile [17](#kpi-tile)](#kpi-tile)

[Parameter Tile [18](#parameter-tile)](#parameter-tile)

[Error Tile [18](#error-tile)](#error-tile)

[Reusable Components Reference [19](#reusable-components-reference)](#reusable-components-reference)

[Input Models [20](#input-models)](#input-models)

[API Calls and Integration [22](#api-calls-and-integration)](#api-calls-and-integration)

[Library Installation [23](#library-installation)](#library-installation)

[Execution [23](#execution)](#execution)

[Authentication [24](#authentication)](#authentication)

[Insight Drilldown [24](#insight-drilldown)](#insight-drilldown)

[API Calls [25](#api-calls)](#api-calls)

[AOT Header Application [27](#aot-header-application)](#aot-header-application)

[AOT Component Configuration [27](#aot-component-configuration)](#aot-component-configuration)

[AOT-COMMON Repository [28](#aot-common-repository)](#aot-common-repository)

[Committing Changes [29](#committing-changes)](#committing-changes)

[Application Insights [29](#application-insights)](#application-insights)

# Introduction

The Accenture Operation Twin (AOT) application enables a comprehensive and contextualized view of operations by integrating product, process, and live data from disparate IT and OT systems. It is a set of micro-frontend applications that has a well-defined purpose and is viable on its own.

The micro-frontend architecture requires all major function groups to be segregated from the rest of the application. The segregation of the content of a micro-frontend means the complete separation of the source code from that of the main application and the separate hosting of it. AOT uses a third-party, open-source framework called Single Page Application (Single-SPA) to integrate the micro-frontends into the main application. Single-SPA’s Parcel feature simplifies the mounting of the micro-frontend applications.

## Purpose

This document explains how to create an Angular-based micro-frontend application from a Single-SPA application and how to mount it to an existing web application.

## Target Audience

Application developers familiar with Angular, NodeJS, Node Package Managers (NPM/Yarn), and basic HTML, CSS, and JS.

## Related Links

- [Using Angular CLI](https://angular.io/cli/generate#module-command)

- [Sample branch](https://dev.azure.com/DigitalPlantProject/Marilyn%20V/_git/MarilynVPlatform?version=GBia-template-viewer) for this documentation

- [Sample template project](https://github.com/matt-gold/single-spa-angular-cli) from GitHub

- [Single-SPA frame](https://single-spa.js.org/)work

- [Single-SPA Parcel Module](https://single-spa.js.org/docs/ecosystem-angular/#parcels)

## Contacts

- `kathleen.m.gomez@accenture.com`

- `lyecca.m.c.gallardo@accenture.com`

## Glossary

| Term | Definition |
|----|----|
| Micro Frontend (MFE) | A web architecture pattern where features are owned by independent, cross-functional teams; each MFE is a self-contained module with its own repository, build, and deployment. |
| Single-SPA | An open-source framework for integrating multiple JavaScript micro-frontends into a single application, enabling independent mounting and deployment. |
| Monolithic Approach | Traditional method of building web applications as a single, feature-rich page, which can become difficult to maintain as the application grows. |
| Parcel Module | A Single-SPA feature that simplifies mounting micro-frontends by acting as a container for them. |
| Routing (Internal/External) | Internal routing occurs within a single application; external routing is managed by a shell layer for different micro-frontends, often using frameworks like Single-SPA. |
| Composition (Client/Server-side) | Client-side composition updates HTML markup in the browser, often using web components; server-side composition assembles UI fragments between the web server and browser. |
| RAG Status | A color-coded status (Red, Amber, Green) used to indicate the health or performance of KPIs. |
| Smart KPIs | A component providing contextualized KPI views, including tiles and graphs, for tracking and analyzing performance. |

# Background

## Monolithic Approach

The monolithic approach is to build a feature-rich and powerful browser application on a single page. Over time, however, the frontend layer, which is often developed by a separate team, becomes difficult to maintain as improvements and new functionalities are added and implemented with time. A monolithic approach to a large front-end application becomes unmanageable. Thus, to solve this issue, micro frontends are implemented. By using the micro-frontend concept, large frontend applications can be segregated into smaller modules that are not only easy to manage but also act independently.

## Micro Frontend Concept

In the micro-frontend concept, a website or web app exists as a composition of features that are owned by independent teams. Each team has a distinct area of business or mission they care about and specialize in. The team is cross-functional and develops features end-to-end from database to user interface. See the diagram on the next page.

A micro-frontend is essentially a microservice that exists within a browser. Micro frontend code can be written in pure JavaScript or any of the JavaScript frameworks. Each micro-frontend has a git repository, a package.json file, and a build tool configuration. As a result, each micro-frontend has an independent build process and an independent deployment/continuous integration.

## Comparison to Micro Services

While Micro frontends bear some similarities to Microservices, there are also some differences. The table below compares the two.

| **Architecture** | **Microservices** | **Micro-frontends** |
|----|:--:|:--:|
| A monolithic team gets split into separate independent teams, which helps improve scalability and code complexity. Each team works on a specific feature of the application separately, developing it from end to end. | Yes | Yes |
| Back-end services communicate with each other over the network. | Yes | No |
| Exist within a single browser tab and communicate via browser memory | No | Yes |
| Independent builds and deployments | Yes | Yes |

## Benefits





``

``
Feature
Description
``
``

``
Technology agnostic
``
Micro frontend architecture gives flexibility to the individual teams to choose the tech stack for their micro frontend, which improves and makes the development cycle fast with enhanced features.
``
``
``
Faster and isolated development and deployment
``
The development process also highly improves by adopting the micro-frontend architecture. As with this architecture, we can have smaller independent teams that work on different features, and the development and deployment processes become faster.
``
``
``
Individual testing and fewer regression issues
``
With isolated teams on the front end, the development, testing, and deployment cycles become smoother and help build resilient applications.
``
``
``
Maintainability
``
Monolithic applications are bound to become large. Hence, making it harder to maintain. The micro-frontends built on smaller parts help maintainability through the divide-and-conquer approach. This guarantees easily testable smaller features, and the overall time for testing is reduced.
``
``
``
Scalability
``
With the modular and decoupled micro-frontend architecture, we can scale up an application to multiple teams as a new frontend element or change the existing frontend that would not affect the rest of the frontend and other teams’ work. So, this allows a team with different backgrounds and skills to choose the tech stack for their micro-frontend accordingly and focus on continuous growth.
``
``
``
``

## Frontends Comparison





### Implementation Pattern

In creating a large website, the implementation of several separate pages or features can be done by different teams. But there could also be certain elements of the web page, like the header and footer that may be present on multiple pages. What differentiates a micro frontend from reusable components is that micro frontends can be deployed as separate, independent projects.

To integrate and assemble different fragments and pages into one interface, front-end integration must be done through routing, composition, and communication.

### Routing

There are two types of routing, Internal and External routing. Internal routing is done inside a particular application, while External routing is a shell layer for different micro-frontend applications. Meta-frameworks such as Single-SPA are used for external routing. This framework provides:

- *APIs for the communication between the applications*

- *Module loader to load several pages asynchronously*

- *Separate UI component wrappers* to connect various components

|  |
|----|

### Composition

Composition refers to where each different part is positioned within a certain page. The two main types of composition are described in the table below.

| Composition Type | Description |
|----|----|
| Client-side | HTML markup is updated directly in the web browser. This could be made possible using Web components. The objective was to create each part as a web component that could be deployed as an independent JavaScript file. Web Components depend on HTML and DOM APIs that can be accessed by other frontend frameworks to receive and send data. |
| Server-side | The server is responsible for the UI composition. A separate service performs the assembly of each fragment located between the web server and the browser. |

### Communication

Although it is best to lessen the interaction between each component, there are instances when the micro-frontends would need to exchange some data with one another. This is possible using web workers and event emitters.

- Web workers are used by web content to run scripts in the background. These can perform tasks without interfering with the performance of the webpage.

- Event emitters are used in components to emit custom events. This allows different components to listen and respond according to the changes done to the components they are subscribed to.

## 

## Common Mistakes

| Mistake | Consequences |
|:---|----|
| Lack of design system | Without a proper design system, several issues may occur. There could be duplicates of the same functionality that may cause some conflicts. |
| Redundant dependencies | A micro-frontend architecture consists of several front-end applications that should be able to work independently. With this, there is a possibility that there would be several of the same libraries in each micro-frontend. This would make the application excessively bigger and may cause some rendering problems. |
| Incorrect application splitting | Dividing the application into smaller parts incorrectly may inflict some difficulties. This may cause some impediments to the improvement of the application since it could make it harder to track or update the components that are needed by the other applications. |

## General Rules

| Rule | Reasoning |
|:---|----|
| Zero coupling between micro-frontends | To achieve the benefits of this architecture, accidental coupling should be avoided as much as possible; this will unlock the flexibility and scalability that the Micro Frontend pattern has to offer as well as future-proofing your applications by allowing incremental upgrades or future complete rewrites of parts of your application. Each Micro frontend should be able to render in isolation or inside a container application. The data required should be loaded by each Micro Frontend and avoid data waterfalls. |
| Separate code bases | Each Micro Frontend should have its codebase and the version control of choice shouldn’t have any impact on the way the project is developed or deployed. |
| Each micro-frontend should be deployed independently | Each Micro Frontend should have its own CI / CD pipeline and be able to deploy to production on demand without any dependencies on other Micro frontends. A common anti-pattern that should be avoided is “The deployment queue of hell” where different Micro frontends are so tightly coupled that they need to be deployed in a specific order to avoid breaking the application. |
| Micro-frontends should be tested separately | Because Micro Frontends are required to render independently as well as inside a container application, it makes sense to also test them independently using unit and integration tests for both scenarios. |
| Micro-frontends should be versioned | When a new Micro-Fronted is deployed to production, the previous version should not be deleted, and the new version should be tagged with a version number using semantic versioning or similar. It is up to the container applications to decide what specific version of a particular Micro Frontend to use or always use the latest version instead. |
| Minimal Communication | Communication between Micro Frontends should be minimal and simple, avoiding global state and framework-specific solutions as much as possible. If two or more Micro Frontends are sharing a lot of messages to provide their minimal functionality, they might be too tightly coupled, and they could share a similar enough purpose that they should be integrated into one. |
| CSS should be scoped | CSS loaded from one Micro frontend should not affect others. |

# 

# AOT Architecture

The AOT Business Application (formerly Core Umbrella) is responsible for hosting the embedded micro-frontends. Besides hosting the micro-frontend applications, the AOT Business Application is responsible for ensuring the authentication and channeling of information between components. The AOT Business Application uses the Single-SPA Framework to host the micro-frontend applications.

## AOT Structure



## AOT Micro Frontends





``

``
AOT MFE
Description
``
``

``
Operation Hierarchy
``
Logic grouping of assets/operations in a plant or multiple plants across regions that are owned by an organization. This provides the user with the ability to drill down to the point of interest.
An example of top-down asset hierarchy could be - company/region/plant/unit/system/equipment.
``
``
``
Smart KPIs
``
Smart KPIs is an AOT component that provides a contextualized view of KPIs to the users who could be in the boardroom or on the shop floor and would use Smart KPIs to track the performance of their respective KPIs and act.
``
``
``
Intelligent Advisor Side Panel
``
IA is an AOT component that combines the following key components: Insight generation engine, collaboration, Actions, Advisor panel, Insight Viewer template, and Insight lifecycle management. The Intelligent Advisor is an AI-based solution that enables different types of users - from shop floor workers to top management - to focus on their most critical issues, with real-time-generated, prioritized, and contextualized insights and recommendations. Can help all levels of the value chain by predicting useful insights, highlighting the root causes, notifying relevant colleagues, recommending appropriate actions, and ultimately improving the performance of end-to-end operations.
``
``
``
Entity Viewer
``
Operations Hierarchy is a component of AOT that helps the user navigate through the plant's hierarchy and be able to view 360-degree information associated with each node (Entity). This would be a unified view that helps the business user in exploring the contextualized data, which in turn would help in speeding up the problem investigation/ analysis. The end user can configure the Entity Viewer through the template and visualize the same on the UI.
``
``
``
Insight Details
``
A way to roll out the displayed insights information, and the details of the UI based on the corresponding specific template. The UI will access data through predefined templates. The template will define the structure of the information that will be used in the UI, and it will define the way the information is organized in the display.
``
``
``
Twin Viewer
``
AOT component for 3D visualization of the plant
``
``
``
Header
``
AOT header component which displays details like the User Profile details, roles the user has, and navigation links to different Config applications.
``
``
``
Component Configuration
``
It is an MFE application that shows all the different config applications in one place in the form of Tiles and helps the user navigate through them.
``
``
``
Reports
``
The Reports component of AOT enables various users – from shop floor workers to top management – to view PowerBI reports and analyze the parameters, through real-time-generated data, allowing the user to conduct a root-cause analysis and collaborate to resolve the problem.
``
``
``
Map
The MAP MFE provides a 2D/3D globe view, where plant-level data is displayed as map markers. These markers then showcase the corresponding plant-level IA and KPI data.
``
``
``

## 

## AOT Software Design Elements

| Element | Purpose |
|----|----|
| Dependency Resolver | This component allows micro-frontends to resolve their dependencies or to publish information to resolve others' dependencies. It has to be a well-isolated component in each micro-frontend to make it possible to easily change its implementation based on another technology. The current implementation goes with native features of the browser, local storage, and custom events. Public events are shared via emitting custom events from the applications. The same event data is saved in the local storage for later use. |
| AOT Service Provider | For maintainability and extendibility, the code for calling APIs from the backend shall be isolated in each application. |

# Single-SPA

Single-SPA is a framework for bringing together multiple JavaScript micro-frontends into a single frontend application. A Single Page Application (SPA) is a specific type of web application that makes navigation possible without having to refresh the page. Codes like HTML, CSS, JS, etc. are pulled up dynamically by loading the page just once.

## Framework

- Since the body content of the single document is updated through JavaScript APIs like XMLHttpRequest and Fetch, it offers a user experience that's fast and responsive. 

- Single-spa framework lets users navigate websites without loading entire new pages from the server. This results in improved performance and a smoother experience overall.

- A Single-Spa Framework incorporates utilities that help streamline the development process. Repetitive coding tasks are automated, making a variety of components ready to use.

- These frameworks also offer features such as HTML and AJAX support, URL routing, data caching, improved performance, and added protection against security vulnerabilities. 

- Unlike traditional web apps, single-spa frameworks are client-side applications that work with the speed and performance of a server-side-rendered app.

- Traditional web apps have many pages, each of which must be reloaded every time they have user requests. With single-spa frameworks, when the server gets a request, only those specific web components are reloaded, while other parts of the page remain as they are. 

## How it Works

When visiting a web page that was built using a single-spa framework, the HTML doc is only sent from the server for the first request. Subsequent requests are completed by sending only JSON data. This means that instead of reloading the entire web page, a SPA will rewrite only the content on that current page, eliminating wait times for extra reloading. The HTML file that a Single-Spa application sends back from the server contains placeholder elements, as well as some files, including JavaScript and CSS code (including systemjs, angularjs, package.json, and others). It does not include any data or content inside the files. When the JavaScript files are executed, a request is sent back to the server for content, and this content is uploaded to the web browser’s HTML code. The dynamic updates of the DOM in the web browser eliminate the need to refresh or reload the web pages. Since JavaScript is downloaded with the initial page load, the SPAs update seamlessly when the server responds.

## Benefits of Single-SPA

- [Use multiple frameworks](https://single-spa.js.org/docs/ecosystem#help-for-frameworks) on the same page [without page refreshing](https://single-spa.js.org/docs/building-applications) (examples including but not restricted to [React](https://single-spa.js.org/docs/ecosystem-react), [AngularJS](https://single-spa.js.org/docs/ecosystem-angularjs), [Angular](https://single-spa.js.org/docs/ecosystem-angular), and [Ember](https://single-spa.js.org/docs/ecosystem-ember))

- Deploy the micro-frontends independently

- Write code using a new framework, without rewriting the existing app

- Lazy load code for improved initial load time

# MFE Integration

Micro frontend applications must be integrated into the AOT Business Application. Basic web application skills and some knowledge of Angular, NodeJS, Node Package Managers (NPM/Yarn), basic HTML, CSS, and JS would be helpful as it is not possible to cover every detail in this guide.

## Configuration

When integrating a micro-frontend application into the Business Application, the file ‘environment-variable-config.json’ must be modified with the addition of a new key-value pair entry on the imports object within the configuration file. The key should be the application name and the value should be the micro-frontend application entry point.

For example: *“intelligentAdvisor”: “http://localhost:4202/main.js”*

Code Example: src/assets/config/environment-variable-config.json

`&#123;`

"accentureADConfig": `&#123;`

"tenantId": `&#123;tenantId&#125;`,

"clientId": `&#123;clientId&#125;`,

"redirectUri": "http://localhost:4201/auth",

"msalAuthorityURL": "https://login.microsoftonline.com/",

"environment": "dev"

`&#125;`,

"imports": `&#123;`

"intelligentAdvisor": `&#123;intelligentAdvisorURL&#125;`,

"testing": "http://localhost:4200/main.js" //this is our sample micro frontend that we want to integrate

`&#125;`,

"singleSPA": `&#123;`

"commonScripts": [

"https://cdnjs.cloudflare.com/ajax/libs/systemjs/6.3.1/system.min.js",

"https://cdnjs.cloudflare.com/ajax/libs/systemjs/6.3.1/extras/amd.min.js",

"https://cdnjs.cloudflare.com/ajax/libs/systemjs/6.3.1/extras/named-exports.js",

"https://cdnjs.cloudflare.com/ajax/libs/systemjs/6.3.1/extras/named-register.min.js"

]

`&#125;`,

"CDFConfig": `&#123;`

"tenantId": `&#123;tenantId&#125;`,

"clientId": `&#123;clientId&#125;`,

"cluster": "api",

"project": `&#123;projectName&#125;`

`&#125;`

`&#125;`

## 

## MFE Container 

To be able to render a micro-frontend application in the Business App, a container must be created. Since the Business App is coded in Angular, the steps below will also be based on Angular. The first step of container creation is the creation of a reusable component module.

### Generate Component Module

There are two methods for generating the component module. Both are very similar but differ in the amount of coding that is required. In this guide, the two methods will be identified as method one and method two.

#### Method One

1.  Go to your desired directory to create a new module.

2.  Use one of the two scripts below to create an angular module: ng generate module &lt;name&gt; [options] or ng g module &lt;name&gt; [options].

3.  After executing the script above it will create a new directory and one (1) module file. We also need to create two more files: spa-host.component.ts, spa-unmount.guard.ts.

&gt; Below is an example of what it should look like inside the Business Application.
&gt;
&gt; 

4.  After creating the files, insert the codes found on the pages to follow:

- spa-host.module.ts

- spa-host.component.ts



- spa-unmount.guard.ts

**spa-host.module.ts**

<!-- REMOVED: `import `&#123; RouterModule, Routes &#125;` from '@angular/router';` -->
```

import `&#123; CommonModule &#125;` from '@angular/common';

import `&#123; NgModule &#125;` from '@angular/core';

import `&#123; SpaUnmountGuard &#125;` from './spa-unmount.guard';
```

<!-- REMOVED: import `&#123; SpaHostComponent &#125;` from './spa-host.component'; -->

const routes: Routes = [

`&#123;`

path: '',

canDeactivate: [SpaUnmountGuard],

component: SpaHostComponent,

`&#125;`,

];

@NgModule(`&#123;`

##### spa-host.component.ts

<!-- REMOVED: import `&#123; Component, OnInit, ViewChild, ElementRef, OnDestroy, ChangeDetectionStrategy &#125;` from '@angular/core'; -->

<!-- REMOVED: import `&#123; ActivatedRoute &#125;` from '@angular/router'; -->

<!-- REMOVED: import `&#123; SingleSpaService &#125;` from '../../services/single-spa.service'; -->

<!-- REMOVED: import `&#123; Observable &#125;` from 'rxjs'; -->

@Component(`&#123;`

selector: 'app-spa-host',

template: '&lt;div #appContainer&gt;&lt;/div&gt;',

changeDetection: ChangeDetectionStrategy.OnPush

`&#125;`)

<!-- REMOVED: export class SpaHostComponent implements OnInit `&#123;` -->

constructor(private singleSpaService: SingleSpaService, private route: ActivatedRoute) `&#123; &#125;`

@ViewChild('appContainer', `&#123; static: true &#125;`)

appContainerRef: ElementRef;

appName: string;

ngOnInit() `&#123;`

this.appName = this.route.snapshot.data.app;

this.mount().subscribe();

`&#125;`

##### 

##### spa-unmount.guard.ts 

<!-- REMOVED: import `&#123; Injectable &#125;` from '@angular/core'; -->

<!-- REMOVED: import `&#123; CanDeactivate, ActivatedRouteSnapshot, RouterStateSnapshot &#125;` from '@angular/router'; -->

<!-- REMOVED: import `&#123; Observable &#125;` from 'rxjs'; -->

<!-- REMOVED: import `&#123; map &#125;` from 'rxjs/operators'; -->

<!-- REMOVED: import `&#123; SpaHostComponent &#125;` from './spa-host.component'; -->

@Injectable(`&#123; providedIn: 'root' &#125;`)

<!-- REMOVED: export class SpaUnmountGuard implements CanDeactivate&lt;SpaHostComponent&gt; `&#123;` -->

canDeactivate(

component: SpaHostComponent,

currentRoute: ActivatedRouteSnapshot,

currentState: RouterStateSnapshot,

nextState: RouterStateSnapshot

): boolean | Observable&lt;boolean&gt; `&#123;`

const currentApp = component.appName;

const nextApp = this.extractAppDataFromRouteTree(nextState.root);

if (currentApp === nextApp) `&#123;`

return true;

`&#125;`

return component.unmount().pipe(map(_ =&gt; true));

`&#125;`

Note: The SingleSpaService is already part of the Business App, so there is no need to create the service file.

#### 

#### Method Two

Method two utilizes the Parcel Module introduced by the single-SPA Framework. The Parcel Module contains a component named parcel, which acts as a container for a micro-frontend. This will simplify the creation of a container module within the Business App. The steps for this one will be similar to the previous implementation.

1.  Generate a module inside your desired directory using the command ng generate module &lt;name&gt; [options]

2.  In this example, we will still use *template-viewer-host* as the &lt;name&gt; of our module.

3.  After executing the script above it will create a new directory and one (1) module file.

4.  The component file template-viewer-host.component.ts must also be created.

&gt; 

5.  After creating the files, insert the codes found on the pages to follow.

    - template-viewer-host.component.ts

    - template-viewer-host.module.ts

##### template-viewer-host.component.ts

<!-- REMOVED: import `&#123; Component, OnInit &#125;` from '@angular/core'; -->

<!-- REMOVED: import `&#123; ActivatedRoute &#125;` from '@angular/router' -->

<!-- REMOVED: import `&#123; mountRootParcel &#125;` from 'single-spa'; -->

@Component(`&#123;`

selector: 'app-spa-host',

template: `&lt;parcel

[config]="config"

[mountParcel]="mountRootParcel"

[customProps]="customProps"

&gt;&lt;/parcel&gt;`

`&#125;`)

<!-- REMOVED: export class TemplateViewerHostComponent implements OnInit `&#123;` -->

applicationName: string;

config;

mountRootParcel = mountRootParcel;

customProps = `&#123;`

applicationName: ''

`&#125;`;

constructor(private activatedRoute: ActivatedRoute) `&#123;`&#125;

ngOnInit(): void `&#123;`

this.applicationName = this.activatedRoute.snapshot.data.app;

this.customProps.applicationName = this.applicationName;

this.config = async () =&gt; `&#123;`

return window.System.import(this.applicationName);

`&#125;`;

`&#125;`

`&#125;`

##### template-viewer-host.module.ts

<!-- REMOVED: import `&#123; NgModule &#125;` from '@angular/core'; -->

<!-- REMOVED: import `&#123; CommonModule &#125;` from '@angular/common'; -->

<!-- REMOVED: import `&#123; TemplateViewerHostComponent &#125;` from './template-viewer-host.component'; -->

<!-- REMOVED: import `&#123; RouterModule, Routes &#125;` from '@angular/router'; -->

<!-- REMOVED: import `&#123; ParcelModule &#125;` from 'single-spa-angular/parcel'; -->

const routes: Routes = [

`&#123;`

path: '',

component: TemplateViewerHostComponent

`&#125;`

];

@NgModule(`&#123;`

declarations: [TemplateViewerHostComponent],

imports: [CommonModule, RouterModule.forChild(routes), ParcelModule]

`&#125;`)

<!-- REMOVED: export class TemplateViewerHostModule `&#123;`&#125; -->

### Route the Container Module to the Application

After the container component module has been created, the module must be added to the Business App routing. In this example, we will put the routing inside the src/app/features/home/home.routing.ts file as shown.

... //We will add this additional object to the existing route code inside the file

`&#123;`

path: 'sample', //The pathname can be changed.

loadChildren: () =&gt;

import('../sample-comp/sample-comp.module').then(

(m) =&gt; m.SampleCompModule

),

canActivate: [MvRouteGuardService],

data: `&#123;app:'testing'&#125;` //The app name should be the same in the configuration file.

`&#125;`

## Skeleton code for micro frontend

A specific version of Angular is used in our current micro frontends, therefore, we will provide the necessary scripts for you to create the source code template that was used in creating the micro frontend using Single-Spa and Angular 9 framework.

1.  Create a new folder and use npm install @angular/cli@9.1.12 to install a local version of the Angular-CLI.

2.  Run ng new `&#123;projectName&#125;` --routing --prefix `&#123;projectName&#125;` to create a new angular project.

3.  In the project folder, run ng add single-spa-angular to install the single-spa framework.

4.  Update the existing 'empty-route' file:

&gt; `&#123;`
&gt;
&gt; path : '**',
&gt;
&gt; component: EmptyRouteComponent
&gt;
&gt; `&#125;`

5.  Replace the placeholder code in the app.component.html with your code, e.g., &lt;h1&gt;Hello Micro frontend&lt;/h1&gt;

## Running the Codes

The main web app and the micro-frontend app need to run concurrently. The single-spa framework requires that the main app is running before the micro-frontend app is started.

1.  Run the main web application by running one of the scripts below using CMD or Terminal from the root folder of the source code.

    1)  If using the node package manager:

npm start

2)  If using the yarn package manager:

yarn start

yarn start //if you are using yarn package manager

2.  Repeat the choice above from the root folder of the micro-frontend source code folder to run the micro-frontend web application.

## 

## Testing

The URL below can be used to test the micro-frontend application:

localhost:4201/home/sample

If an error is displayed related to running both the main web app and the micro frontend simultaneously, check the package.json file to make sure that the ports are set correctly.

Micro-frontend application package.json:

"name": "sample",

"version": "0.0.0",

D Debug

"scripts":`&#123;`

."ng": "ng",

"start": "npm-run serve: single-spa: sample",

"build" :- "ng-build",

"test":"ng test",

"lint": "ng lint",

"e2e": "ng e2e",

"build: single-spa:sample": "ng.build template -- prod --- deploy-url-http://localhost:4200/",

"serve: single-spa:sample": ."ng.s .-- project.template -- disable-host-check -- port.4200 -- deploy-url http://localhost:4200/ -- live-reload false"

# 

# MFE Use Case – Smart KPIs

This section describes how Smart KPIs are using the MFE. For other components, refer to other AOT documentation listed under Related Links.

## Smart KPIs Library

KPI Tiles and the Trendline graph functions are made reusable and structured through the implementation of an Angular Library. These key components are built as standalone components and deployed to Azure Artifacts that are easily installed by other developers and used by providing specific inputs. The component selectors corresponding to KPI Tiles and Trendline are “smartKPIs-kpi-tile”, “smartKPIs-chart-components”, and “smartKPIs-time-series-multi-line-chart” respectively. Features include:

<!-- REMOVED: - Trendline Graph: The entire Trendline Panel is reusable. The panel includes the KPI dropdowns, Export buttons, and Tooltip. -->

<!-- REMOVED: - The dropdowns and export buttons are now made optional for developers. Thus, if the team that is using the Smart KPIs trendline component library wants to show/hide any of these components, they can do it easily by just passing appropriate Boolean values to the smartKPIs-chart-components for each of the above-mentioned components. -->

- The “smartKPIs-time-series-multi-line-chart" is hosted in the “smartKPIs-chart-components”. Hence, the smartKPIs-chart-components act as a bridge between the Smart KPIs and the smartKPIs-time-series-multi-line-chart component.

- Using the comparison of Trendlines feature, the user can select any two KPIs and view the comparison graph for any two parameters (Actual, Target, Historical Benchmark, and Forecast).



### KPI Tile



- The tile will show the following data: Date and time of when it was created, Frequency, Actual value, Target value, Forecasted value, and Historical Benchmark.

- The Actual value, Target value, Forecasted value, and Historical Benchmark are based on the user's preferred Unit of Measure (In this case it is in pounds).

### 

### Parameter Tile



- This happens when the user updates the calendar selection and has reached the last level of the KPI drill-down.

### 

### Error Tile



- The “No Data Available” message will be shown when:

- there is a computation error

- when the simulator stopped

- when there is an improper calculation

- when there is an improper relationship defined, etc.

### 

### Reusable Components Reference 

The table below serves as a reference for the sable components. Data includes the respective Angular selectors, mandatory inputs, and usage examples for the Trendline Chart and KPI Tile components. A selector is used to identify each component uniquely in the component tree, and it also defines how the current component is represented in the HTML DOM.






``

``
Selector
Input
Usage
``
``

``
&lt;smartKPIs-kpi-tile&gt;
`Kpi: Data for KPI Tile of type KPI`
RAG: RAG status Ranges
enableBackground: Boolean value to show/hide header and background color of the tile
PanelExpanded: Boolean value to notify if the Intelligent Advisor panel is open or not
ShowComparisonPercentage: Boolean value to show/hide the percentage comparison details on the tile
`&lt;smartKPIs-kpi-tile (click)="doSomething()"`
*ngFor="let kpi of kpiList [enableTileBackgorund]="true" [kpi]="kpi"&gt;
&lt;/smartKPIs-kpi-tile&gt;
``
``
&lt;smartKPIs-chart-components&gt;
`SelectedKpi: Data of the KPI that is selected in the “Select KPI” dropdown in the trendline`
SelectedKpi2: Data for the KPI that is selected in the “Compare To” dropdown in the trendline
Kpis: List of KPIs to be populated in the dropdowns
TrendlineChartOptions: list of boolean values to show/hide the trendline components
PanelExpanded: Boolean value to notify if the Intelligent Advisor panel is open or not
NoGraphDisplayed: Boolean value to notify if there is no graph to be displayed
trendData: ProductionTrendData,
trendData$: Observable&lt;ProductionTrendData&gt;yLable: Score,
`&lt;smartKPIs-chart-components [selectedKpi]="selectedKpi" [selectedKpi2]="selectedKpi2" [kpis]="allKPIs"`
[slicedPage]="getSlicedPage()" [trendlineChartOptions] = "trendlineChartOption" [panelExpanded]="panelExpanded"
[noGraphDisplayed]="noGraphDisplayed" [trendData]='trendData' [trendData$]="trendData$" [yLable]="'Score'" (resetCompare)="resetCompareTo()"
(kpiSelected2)="onKPISelect2($event)" (kpiSelected)="onKPISelect($event)"&gt;&lt;/smartKPIs-chart-components&gt;
``
``
&lt;smartKPIs-time-series-multi-line-chart&gt;
`Data: ProductionTrendData, Data$: Observable&lt;ProductionTrendData&gt;, yLable: Score,`
Selected Kpi: Data of the KPI that is selected in the “Select KPI” dropdown in the trendline
SelectedKpi2: Data for the KPI that is selected in the “Compare To” dropdown in the trendline
Kpis: List of KPIs to be populated in the dropdowns
isPanelExpanded: Boolean value to notify if the Intelligent Advisor panel is open or not
kpiSelected: KPI selected in the Show KPI dropdown
kpiSelected2: KPI selected in the “Compare To” dropdown
`&lt;smartKPIs-time-series-multi-line-chart [selectedKPI2]="selectedKpi2" [isPanelExpanded]="panelExpanded" [data]='trendData' [data$]="trendData$" [yLable]="'Score'"`
[selectedKPI]="selectedKpi"&gt;&lt;/smartKPIs-time-series-multi-line-chart&gt;
``
``
``

### 

### Input Models 

The following table lists all the inputs that are consumed by the Smart KPIs Library along with their respective model structures.





``

``
Input
Model
``
``

``
kpi/selectedKpi/selectedKpi2
`productId: any;`
id: number;
externalId: string;
name: string;
kpiName:string;
kpi_Name:string;
role:string;
target?: `&#123;`
value?: number | string,
date?: string
`&#125;`;
actual?:`&#123;`
value?: number | string,
date?: string,
previousDate?: string,
previousValue?: number,
percentagecomparison?: number | string,
percentagecomparisoncolor?: string,
percentagecomparisontimestamp?: string
`&#125;`;
forecast?:`&#123;`
value?: number | string,
date?: string
`&#125;`;
historicalBenchmark?:`&#123;`
value?: number | string,
date?: string
`&#125;`;
uom: string;
uomToDisplay? : string;
configuredOrSourceUom? : string;
RAGStatus:RAGStatusRanges;
influencingKPIs?: KPI[];
contributingKPIS?: KPI[];
description?: string;
aggregationLogic?: string;
assetId: string;
assetName?:string;
uomSystemId? : string;
uId: string;
kpiTitle: string;
responsibleRole: string;
error? : `&#123;`
"err": `&#123;`
"code":string;
"messageTitle":string,
"message":string;
"innermessage":string;
"value":string
`&#125;`
`&#125;`;
information? : `&#123;`
"info": `&#123;`
"code":string;
"messageTitle":string,
"message":string;
"innermessage":string;
"value":string
`&#125;`
`&#125;`,
deviation?:number;
direction?:string;
isKpi?:boolean;
isSameCalcfreq?:boolean;
aggregatedValue?:string;
startdateAggregate?:string;
enddateAggregate?:string;
calculationActual?:string;
calcFrequency?:string;
batchId?:string;
aggregatedvalue?:string;
relationship?:string;
isAdequateAccess?:boolean;
aggregate?:number;
calendarOption?:string;
displayEmptyTile?: boolean;
disableFurtherDrillDown? : boolean;
disableDrillDownMessage? :string;
``
``
``





``

``
Input
Model
``
``

``
RAG
``&#123;
'Amber-Mandatory'?:minMaxRange;
'Green-Mandatory'?:minMaxRange;
'Red-Mandatory'?:minMaxRange;
'Amber-optional'?:minMaxRange;
'Green-optional'?:minMaxRange;
'Red-optional'?:minMaxRange;
`&#125;`
``
``
enableBackground
boolean
``
``
trendData
`ProductionTrendData `&#123;
lines: ProductionLine[] = [];
today: Date = new Date(new Date().setHours(0,0,0));
ticks:`&#123;in:string, count:number&#125;`;
isComparison: boolean = false;
paramSelected: boolean = false;
`&#125;`
``
``
`ProductionLine `&#123;
assetKpiName?:string='';
name: string = '';
color: string = 'white';
dashed: boolean = false;
type: DataType = DataType.SIMPLE;
values: ProductionValue[] = [];
show: boolean = true;
checked?: boolean = false;
error? : string = 'none'
`&#125;`
``
``
`ProductionValue `&#123;
time: Date = new Date();
value: number = 0;
insightsCount?: number = 1200;
insightIds?: number[] = [];
actionsCount?: number = 0;
insightsIconClicked: boolean = false;
`&#125;`
``
``
TrendlineChartOptions
`ChartOptions`&#123;
kpiDropdown : boolean;
compareTo : boolean;
exportToPNG : boolean;
exportToXlS : boolean;
`&#125;`
``
``
``

### 

### API Calls and Integration

The tables below serve as a brief reference for the API calls made in the Dashboard and Drilldown pages.

#### Dashboard Calls





``

``
API
Purpose
``
``

``
https://apim-aot-mw-dev.azure-api.net/ api/smartkpi/assets/all/kpis/all
To fetch all the assets tagged to the User role
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/`&#123;assetid&#125;`/kpis/`&#123;uid&#125;`/detail
`To fetch the details of each KPI –`
Actual, target, forecast, historical benchmark values, RAG
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/trendline
To fetch all the data points for all four parameters for a list of KPIs
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/all/kpis/all/deviation
To fetch the performance deviation values for all the KPIs
``
``
``

#### Drilldown Calls





``

``
API
Purpose
``
``

``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/`&#123;assetid&#125;`/kpis/`&#123;uid&#125;`
To fetch information on the selected KPI
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/`&#123;assetid&#125;`/kpis/`&#123;uid&#125;`/detail
`To fetch the details of each KPI –`
Actual, target, forecast, historical benchmark values, RAG
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/assets/`&#123;assetid&#125;`/kpis/`&#123;uid&#125;`/drilldown
To fetch the list of contributing and influencing KPIs for the selected KPI
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/trendline
To fetch all the data points for all four parameters for a list of KPIs
``
``
https://apim-aot-mw-dev.azure-api.net/api/smartkpi/deviation
To fetch the performance deviation values for all the KPIs
``
``
``

The details of the above-mentioned APIs can be found in the [API Reference Document](https://industryxdevhub.accenture.com/assetdetails/42).

### 

### Library Installation

The Smart KPI MFE application is mounted on top of the Host Application. Thus, both applications are running simultaneously on separate terminals.



1.  In the directory where package.json is found, add a .npmrc file to the project.

2.  Add the following content to your .npmrc file to make sure that npm has access to the registry where the library is published:

registry=https://pkgs.dev.azure.com/DigitalPlantProject/f328897f-a8db-4569-afc6-38baa455969/_packaging/aot-angularlib/npm/registry/

always-auth=true

3.  If vsts-auth is already installed, skip to step 4. Otherwise, install vsts-auth using the command:

npm install -g vsts-npm-auth --registry  --always-auth false

4.  Add an Azure Artifacts token to the user-level .npmrc file:

vsts-npm-auth -config .npmrc

5.  Install the library:

npm install @aot/smart-kpis-widgets

### Execution

To run the Smart KPIs MFE application on your local machine:

1.  Navigate to the Host Application with the path:

&lt;Project Folder&gt;MarilynVPlatformConsumptionUICoreUmbrellamarilynv-uimarilynv-umbrella-ui

2.  Run the Host Application.

npm start

3.  Navigate to the Smart KPIs application.

C:Usersellina.priyadarshiniDocumentsMarilynVPlatformConsumptionUIsmart-kpis-micro-appsmart-kpis-micro-app-ui

4.  Run the application.

npm start

5.  In the environment-variable-config.json of the Host Application, change the URL of smartKPIs: http://localhost:4204/main.js

### 

### Authentication

Smart KPIs is an Angular-based MFE application that is authenticated using Azure Active Directory. Once the user is authenticated, an MSAL token is generated and stored in local storage. Then, a custom event is triggered so that the other MFE applications can subscribe to the event and use the same token.

## Insight Drilldown

The AOT application provides the user with the ability to view the Insight details and drill down from the Insight Viewer into the KPI from which the Insight was generated. The user can also view any contributing and influencing KPIs as well as the Trendlines. Communication between the Intelligent Advisor and Smart KPIs is done based on Custom Events, wherein an event is emitted at Template Viewer when the KPI for which the insight was generated is clicked. The event is listened to and subscribed to by the Smart KPI frontend and based on the event details shared by the Template viewer, further API calls are made. For example, given the event data:

assetName: "X-Y-U3-SWLPC"

calendarOption: "noselection"

componentName: "Intelligent Advisor"

endDate: "2023-08-03T05:50:00.000Z"

kpiName: "Availability"

kpiUID: "2c14eff6-df47-481e-b24d-76cdf37f5fbf"

startDate: "2023-08-03T05:50:00.000Z"

The URL for the drilldown page is formed using the assetName , kpiName, and kpiUID parameters as shown below.



### 

### API Calls

When the URL is followed, API calls are made to populate the details in the drilldown page by using the startDate, endDate, and calendarOption parameters.

The first API call is a GET call that returns some basic information on that KPI.





The second API call then fetches the information about the KPI that generated the Insight.









Once the response of the Detail API arrives, the subsequent drilldown API call is made and the cycle repeats.

The API call shown below fetches the Contributing and Influencing KPIs for the selected KPI.







# 

# AOT Header Application

The Header MFE application is a common component for all other MFE components and appears at the top of the application. It displays details such as:

- Navigation links to other MFE applications – Smart KPIs, Twin Viewer, and Reports.

- User profile details such as username, roles, and option to sign out of the application.

- The dots menu on the side contains options to navigate to:

- The component configuration home page.

- Different configuration applications based on the user roles.



# AOT Component Configuration 

The Component Configuration MFE is also a common component for all other MFEs and is comprised of tiles that help the user navigate to different configuration applications. The user can navigate to the Component Configuration home page by clicking on the ‘Overview’ button in the side menu.



# 

# AOT-COMMON Repository

The AOT-COMMON is a unified repository that hosts the front-end code for both Azure and CDF versions of AOT, as shown on the right below). A unified repository ensures seamless operation, maintenance, feature compatibility, and enhanced performance. The environment configuration [JSON file](https://ts.accenture.com/:t:/r/sites/GlobalDocTemplates/Published%20Documents/AOT/Linked%20Files/AOT_COMMON_Repo_JSON_Structure.txt) (shown on the left below) is structured to support both Azure and CDF as well. This simplifies configuration management for both environments as well as for any upcoming platforms (e.g., AWS) to be integrated into AOT as per requirement.





## 

## Committing Changes

The following section describes the process of committing the changes made to the MFEs to both environments (CDF and Azure).

1.  Initialize Submodules: git submodule init

2.  Update Submodules: git submodule update

3.  Navigate to the Parent Directory (if you are not in the parent directory already): cd ../..

4.  List Files (Optional): ls

5.  Access a Submodule: cd AOT-Common

6.  Switch Branch from where the commit ID needs to be linked: git checkout &lt;source branch&gt;

7.  Pull Latest Changes: git pull

8.  Return to the Main Directory: cd ..

9.  Stage the changes: git add .

10. Check Git Status (Optional): git status

11. Commit Changes: git commit

12. Push Changes: git push origin &lt;branch name&gt;

13. Raise a Pull Request: raise PR to &lt;target branch name&gt;

# Application Insights

Azure Application Insights includes pageviews logging that:

- helps you monitor and analyze user interactions with web applications.

- tracks every time a user visits a page on your web application. This data is captured and sent to Azure Application Insights, where it can be analyzed to understand user behavior, popular pages, and navigation paths.

- can be analyzed using Kusto Query Language (KQL) in Azure Monitor Logs to understand user behavior.

- supports custom dashboards for visualizing metrics like bounce rates, average session duration, and popular pages.


