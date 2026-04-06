Source: https://docs.slack.dev/workflows/comparing-workflows-apps

# Comparing workflows and apps

With so many feature sets and tools available — many of which overlap with one another — it can be a little daunting to decide which path is right for you.

_You are in a maze of twisty little passages, all alike._

The following tables compare the features and some common development goals of these tools. May they offer additional guidance as you choose your own adventure.

### Development {#development}

Goal/feature

[Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)

[App created with Bolt](/quickstart)

[App created with Deno Slack SDK](/tools/deno-slack-sdk/guides/getting-started)

[Minimum Plan](https://app.slack.com/plans/T34263EUF?gad_source=1&acs_info=ZmluYWxfdXJsOiAiaHR0cHM6Ly9zbGFjay5jb20vcHJpY2luZyIK&gclid=CjwKCAiA5L2tBhBTEiwAdSxJX6xhfl1tGTCkR9bkQTJwNRQcdrTf8aOGQxY1HKmqiXowc06LvBqhARoCZiEQAvD_BwE&gclsrc=aw.ds)

Details

I want to choose which programming language I use to build my app.

\-

✅

\-

Free

[Slack API](/reference/methods) methods are accessible over HTTP, so the world is your oyster. Also worth noting is that [Slack maintains official libraries](/tools) for Python, JavaScript, and Java, as well as the Bolt application framework.

I want to integrate with third-party services (e.g. Google, JIRA) using APIs or webhooks.

✅

✅

✅

Free

Code integrations with Bolt apps are available any way you like. [Connector functions](/tools/deno-slack-sdk/reference/connector-functions) for integrating with third-party services are available for apps created with the Deno Slack SDK or via Workflow Builder.

I want to empower co-workers to automate Slack and integrations with other software without having to code.

✅

\-

\-

Paid

For no-code solutions, use Workflow Builder.

I want to interact with Slack APIs over HTTP (by using the [Web API](/apis/web-api/)).

✅

✅

✅

Free

You can use the Web API with both the Bolt framework and the Deno Slack SDK. You can also call API methods within Workflow Builder.

I want to respond to events happening within Slack (by using the [Events API](/apis/events-api/)).

\-

✅

✅

Free

This feature is compatible with Bolt apps. A subset of the Events API is available for apps created with the Deno Slack SDK via event triggers, but is not required.

I want to send messages with [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).

\-

✅

✅

Free

I want my app to be able to respond to webhooks.

✅

✅

✅

Free

I want my app to have an [App Home](/surfaces/app-home).

\-

✅

\-

Free

I want to use [slash commands](/interactivity/implementing-slash-commands).

\-

✅

✅

Free

Bolt apps can use slash commands in a variety of ways. Apps created with the Deno Slack SDK can only use slash commands to invoke the app.

I want to send files and images to users.

✅

✅

✅

Free

I want users to be able to send files.

✅

✅

✅

Free

I want to respond to Slack messages with embedded metadata.

✅

✅

✅

Free

I want users to be able to interact with my apps.

✅

✅

✅

Free

Any app will do, but the way you code interactivity will be different for each solution.

I want to retrieve data from or store data to a database.

\-

✅

✅

Free

Code database operations in Bolt apps any way you like. For apps created with the Deno Slack SDK, you can store data in a [Datastore](/tools/deno-slack-sdk/guides/using-datastores) hosted by Slack.

I want my app to be shareable and added to a message within Slack, bookmarked, or embedded in a Slack Canvas.

✅

\-

✅

Paid

Share apps created with the Deno Slack SDK or apps built via Workflow Builder with link triggers.

I want to develop an app as an additional service to our external website, which allows users to chat with a bot from inside of Slack.

\-

✅

\-

Free

The Deno Slack SDK doesn't support installing an app by others on their workspace (unless they are able to do so themselves via the Slack CLI). For example, if your app was open sourced on GitHub this would be possible, as another developer could clone it and install it in their workspace.

I want to integrate with Salesforce.

✅

✅

\-

Paid

Once Salesforce and Slack have been [connected](https://slack.com/help/articles/30754346665747-Connect-Salesforce-and-Slack), steps are available in Workflow Builder to create, read, update, and delete a record, as well as run a flow. With a Bolt app, the possibilities are even greater, as you can call the Salesforce API to carry out actions in Salesforce.

### Environment {#environment}

Goal/feature

[Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)

[App created with Bolt](/quickstart)

[App created with Deno Slack SDK](/tools/deno-slack-sdk/guides/getting-started)

[Minimum Plan](https://app.slack.com/plans/T34263EUF?gad_source=1)

Details

Works across multiple workspaces

✅

✅

✅

Enterprise Plan

Develop on Free plan

\-

✅

\-

Free

Both apps created with the Deno Slack SDK and Workflow Builder require that you be on a paid plan. Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox with access to all Slack features for free.

[Tokens](/authentication/tokens)

\-

✅

✅

Free

Both Bolt apps and apps created with the Deno Slack SDK make use of access tokens. Refer to [Token types](/authentication/tokens) for more information about the types available.

[Admin API](/admins)

\-

✅

\-

Enterprise Plan

[SCIM API](/admins/scim-api/)

\-

✅

\-

Business+ or Enterprise Plan

Discovery API

\-

✅

\-

Enterprise Plan

[Legal Holds API](/admins/legal-holds-api/)

\-

✅

\-

Enterprise Plan

[Audit Logs API](/admins/audit-logs-api/)

\-

✅

\-

Enterprise Plan

### Host and deploy {#host-and-deploy}

Goal/feature

[Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)

[App created with Bolt](/quickstart)

[App created with Deno Slack SDK](/tools/deno-slack-sdk/guides/getting-started)

[Minimum Plan](https://app.slack.com/plans/T34263EUF?gad_source=1)

Details

Host or distribute app myself

\-

✅

\-

Free

For self-hosted apps, you'll want to go with the Bolt framework.

Slack-hosted app

✅

\-

✅

Paid

For Slack-hosted apps, you'll want to go with the Deno Slack SDK, or build your app using Workflow Builder.

List app in [Slack Marketplace](/slack-marketplace)

\-

✅

\-

Free

### Security {#security}

Goal/feature

[Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder)

[App created with Bolt](/quickstart)

[App created with Deno Slack SDK](/tools/deno-slack-sdk/guides/getting-started)

[Minimum Plan](https://app.slack.com/plans/T34263EUF?gad_source=1)

Details

OAuth authentication

\-

✅

✅

Free

Still not sure where to begin? That's okay! We recommend following [our guide on creating a basic Slack app that can send messages using webhooks](/app-management/quickstart-app-settings). It'll give you an idea of what the Slack platform can do, and get those cogs in your head spinning.