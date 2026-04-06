Source: https://docs.slack.dev/faq

# Slack developer FAQ

We know there's a lot to learn and read about all the integration points of the Slack platform. Here is a little more information you might find helpful!

## General {#general}

### How do I build a bot using Slack APIs? {#bot-APIs}

We have a [quickstart](/quickstart) guide that will walk you through the process!

### How do I set up a developer environment to build a Slack app? {#set-up-dev-environment}

You can provision sandbox environments by joining the [Slack Developer Program](https://api.slack.com/developer-program). Once you're ready to deploy your app, distributing the app will allow you to install it in other workspaces.

Start by [building a Slack app](/app-management/quickstart-app-settings) to contain all of your work—by default, it can only be installed on your own workspace. Follow the instructions in the UI to add features—most require that you provide a HTTP server Slack can reach.

Have more questions? Check out our [developer sandbox FAQs](/tools/developer-sandboxes#faqs)!

Are you a partner with us? The [Slack Partner Developer Program](https://api.slack.com/developer-program/partners) offers [partner sandboxes](/tools/partner-sandboxes).

### Is Slack down? {#downtime}

Of course we want Slack to be fully functional for users and developers at all times. Here are some tips in the unfortunate event you're having trouble and need to determine the cause of a Slack-related issue.

When possible, we report current status promptly on [status.slack.com](https://status.slack.com/) with any service disruption advisories, but you can also use the following methods:

*   Use the [Slack Status API](/reference/slack-status-api).
*   Send a HTTP GET request to the [`https://slack.com/api/api.test`](/reference/methods/api.test) API method. A HTTP 200 `application/json` response of `{"ok":true}` indicates at least part of the Slack [Web API](/apis/web-api/) is available.
*   Send a more complex, [authenticated](/authentication) request to [`https://slack.com/api/auth.test`](/reference/methods/auth.test) using a bot, user, or legacy [token](/authentication/tokens). Using this method exercises the authorization and API layer further than `api.test` and may grant you the serenity of greater confidence in Slack availability.
*   If using the legacy [Real Time Messaging (RTM) API](/legacy/legacy-rtm-api), try using [`rtm.connect`](/reference/methods/rtm.connect) to generate a WebSocket URL using a token with the proper permissions, then open the socket using a tool like [this browser-based WebSocket client for Google Chrome](https://chrome.google.com/webstore/detail/simple-websocket-client/pfdhoblngboilpfeibdedpjgfnlcodoo?hl=en).

Still unsure if Slack is down? Contact our enthusiastic [support team](https://my.slack.com/help/requests/new).

### How do I integrate a third-party service with Slack? {#third-party-services}

Check whether there is an app for a third-party service in the Slack Marketplace. If all else fails, you'll need to [code one for yourself](/quickstart).

You can also add [connector functions](/tools/deno-slack-sdk/reference/connector-functions) to your automations workflows. A growing library of third-party services are available.

### Apps vs. workflows {#workflow-apps}

Building a Slack app? Start [here](/quickstart). Building a workflow? Start [here](/workflows). For more about workflows and custom workflow steps, jump to [this section](#automations-workflow-apps).

## Authentication {#authentication}

### How do I authenticate my requests to Slack? {#authenticate-me}

#### By token {#by-token}

When working with Slack apps or the [Web API](/apis/web-api/), you'll often need to send access tokens, also known as bearer tokens, along with inbound requests within the authorization header. When creating an app for the first time, you'll be given your own user and bot token while going through the app creation process. In order to obtain other users' tokens, you'll need to send users through the [OAuth 2.0 authentication flow](/authentication). When you're working with Slack apps, you'll be awarded access tokens after a user approves your application.

#### By private URL {#by-URL}

Your [incoming webhook](/messaging/sending-messages-using-incoming-webhooks) URLs are unique to your integration or application and do not require token-based authentication. [Slash command response URLs](/interactivity/implementing-slash-commands#responding_to_a_command) also already encode your integration's or application's identity.

### How do I authenticate requests from Slack to me? {#authenticate-slack}

Use the [signing secret](/authentication/verifying-requests-from-slack) to compute a signature, and verify that the signature on the request matches. This process is _strongly_ preferred over the use of deprecated verification tokens.

You can also use [Mutual TLS](/authentication/verifying-requests-from-slack#mutual_tls). Mutual TLS verifies the identity of Slack in a TLS-terminating server, before a request reaches your application code.

### How does Slack authenticate its requests to my servers? {#authenticate-servers}

When you configure [Slash commands](/interactivity/implementing-slash-commands), you specify a URL for Slack to send requests to when qualifying conditions are met. Slack also provides you a token related to that integration.

Slack sends that URL a JSON payload containing a `token` field. Compare that field to values you've received from Slack. Refer to [validating slash commands](/interactivity/implementing-slash-commands#validating_the_command) for more information.

### When do authorization codes expire? {#authenticate-expire}

Authorization codes must be exchanged for an access token within 10 minutes by calling the [oauth.access](/reference/methods/oauth.access) API method as part of the [authorization flow](/authentication). Otherwise, the authorization code will expire, and you'll need to ask the user to go through the OAuth flow again.

### How do I revoke a token? {#revoke-token}

Use the [`apps.uninstall`](/reference/methods/apps.uninstall) API method to uninstall an app completely, revoking all tokens. If you want to dispose of a single OAuth access token, use the [`auth.revoke`](/reference/methods/auth.revoke) API method; it works with tokens from [Sign in with Slack](/authentication/sign-in-with-slack/) as well as from [Add to Slack](/legacy/legacy-slack-button).

For classic apps, revoking the last token associated between your application and a workspace effectively uninstalls the app for that workspace.

Members and administrators can remove your app through their [workspace administration interface](https://my.slack.com/apps/manage).

Though it's somewhat of a nuclear option, you also have the ability to revoke all tokens from your [developer dashboard](https://api.slack.com/apps) by selecting your application and clicking **Revoke all tokens**.

### How do I reset my client secret? {#client-secret}

To reset your client secret, go to your [developer dashboard](https://api.slack.com/apps), select the application, and click the **Change secret** button.

Don't forget to use your new secret when exchanging authorization codes for access tokens while authorizing users and workspaces with [OAuth 2.0](/authentication).

## Slash commands {#slash-commands}

### Why does Slack never reach my slash command URL? {#slash-URL}

Typically, if Slack cannot reach your slash command URL it's because it's inaccessible, does not have a valid or verifiable SSL certificate, or our request is timing out for some reason.

Slack invokes slash command URLs from its servers rather than from a Slack client app like Slack for Mac. This means that the URL we're trying to reach must be accessible to Slack's servers.

To determine whether your certificate is valid, consider using [this tool](https://www.ssllabs.com/ssltest/index.html) provided by SSL Labs.

### How do I validate a slash command's origin? {#slash-origin}

Keep track of the validation tokens and team IDs Slack gives you when commands are created and teams approve your app. Always validate that the `token` field in an incoming slash command request has been issued to you by Slack, and scope your data for that workspace.

## Incoming webhooks {#incoming-webhooks}

### Why can't I override the channel, icon, or user name of my incoming webhook? {#override}

You won't be able to override any of these fields when using an [incoming webhook](/messaging/sending-messages-using-incoming-webhooks) attached to a Slack app. Instead, those values will be provided from your Slack app configuration and any configuration provided by the team.

## Interactive messages {#message-buttons}

### Can I use a self-signed certificate for my action URL? {#action-URL}

No, SSL certificates must be signed by a reputable certificate authority. You may want to consider using one of the following low-cost providers:

*   [Let's Encrypt](https://letsencrypt.org/)
*   [CloudFlare](https://www.cloudflare.com/ssl/)

## Web API {#web-api}

### Can I send JSON when using HTTP POST? {#http-post}

Yes, the [Web API](/apis/web-api/) accepts both `application/x-www-form-urlencoded` POSTs as well as `application/json`.

Refer to [POST bodies](/apis/web-api/#post_bodies) for more information.

### How is the Web API rate limited? {#rate-limited}

Refer to our [rate limiting guide](/apis/web-api/rate-limits) for specific information on rate limits.

### How do I work with files? {#files}

Refer to our [working with files guide](/messaging/working-with-files) for specific information on working with files.

### How do I find a channel's ID if I only have its #name? {#channels-ID}

There are currently no methods to directly look up channels by name. Use the [`conversations.list`](/reference/methods/conversations.list) API method to retrieve a list of channels. The list includes each channel's `name` and `id` fields.

Many developers keep the list of channels in memory for swifter lookups. Poll the method occasionally to refresh your inventory or keep it updated with the [Events API](/apis/events-api/).

### How do I find a channel's name if I only have its ID? {#channels-name}

You can use similar instructions to the question above, or you can use the [`conversations.info`](/reference/methods/conversations.info) API method to obtain a specific channel's information, including its `name`.

### Do channel IDs stay the same when the name of the channel changes? {#channels}

Channel IDs remain the same, even when names are changed.

### Do channel IDs stay the same when moving between public and private? {#channels-visibility}

As of [September 2018](https://docs.slack.dev/changelog/2018/09/01/more-reasons-to-be-a-conversations-api-convert), channel IDs remain static even when a channel is converted between public and private.

Use the [Conversations API](/apis/web-api/using-the-conversations-api) to safely work with channels that have transitioned between public and private.

### How do I retrieve a single message? {#message}

Use the [`conversations.history`](/reference/methods/conversations.history) API method and a token with the [`channels:history`](/reference/scopes/channels.history) scope to retrieve a specific message in a public channel. [Learn more about this approach](/messaging/retrieving-messages#individual_messages).

## Events API {#events-api}

### How do I re-enable event subscriptions for my app? {#events-subscription}

If your app's subscriptions are disabled due to exceeding the Events API [failure limits](/apis/events-api/#failure_limits), manually re-enable them by visiting your [application's settings](https://api.slack.com/apps). If your app is part of the Slack Marketplace, use your **Live App Settings** instead of your development app.

### When should I use the Events API and when should I use Socket Mode or the legacy RTM API? {#events-socket-RTM}

Choose the [Events API](/apis/events-api/) if:

1.  You want to precisely [scope](/reference/scopes) the data you receive to just what your app needs.
2.  You prefer or must use an inbound request model due to one of the following: a) your hosting service is not able to maintain an outbound WebSocket connection, or b) you prefer to scale your application on an inbound request model instead of maintaining multiple long-lived WebSocket connections.
3.  You're converting an [outgoing webhook](/legacy/legacy-custom-integrations/legacy-custom-integrations-outgoing-webhooks) integration into something installable as a Slack app.
4.  You find the [retry behavior](/apis/events-api/#errors) reassuring for redundancy reasons.

Choose [Socket Mode](/apis/events-api/using-socket-mode) if:

1.  You're building an on-premise integration or have no ability to receive external HTTP requests.
2.  You're working on a distributed or mobile application without a server backend.
3.  You just prefer working with WebSockets. That's cool.
4.  You want data feed redundancy by opening additional WebSocket connections.
5.  You want messages to be delivered to you in real time.

Finally, choose the legacy [RTM API](/legacy/legacy-rtm-api) _only_ if:

1.  You have very specific needs that only the RTM API solves.
2.  You already have a classic app, as they can longer be created.
3.  You are okay with your app not working in the somewhat-near future, [as classic apps are slated to be deprecated.](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation)

### How do I make my bot appear active and present? {#bots}

The answer depends on whether you're using the Events API with or without the legacy RTM API:

*   With the Events API, you must toggle your presence by [managing your app](https://api.slack.com/apps)'s bot user config.
*   With the legacy RTM API, your bot is marked `active` while connected to a WebSocket.

Therefore, the presence of the bot depends on whether you are using the legacy RTM API (the bot is online when it's connected through the WebSocket), or it's always online when you turn this setting on. Refer to [bot presence](/apis/web-api/user-presence-and-status#bot_presence) for more information.

## Socket Mode {#socket-mode}

[Socket Mode](/apis/events-api/using-socket-mode) allows you to use the [Events API](/apis/events-api/) and [interactive features of the platform](/interactivity), without exposing a static HTTP endpoint to receive payloads. Instead, you use the WebSocket protocol and generate a URL at runtime.

The legacy [RTM API](/legacy/legacy-rtm-api) is another way of connecting your application to Slack. For most applications that can't use a static HTTP endpoint, [Socket Mode](/apis/events-api/using-socket-mode) is preferred over RTM.

## Legacy RTM API {#real-time-messaging-api}

### Can I start using the RTM API? {#can-i-start-using-the-rtm-api}

Most likely not. Classic apps can no longer be created, and the newer, granular permissions apps cannot access the RTM API. Try the [Events API](/apis/events-api/)!

### Can I keep using the RTM API? {#can-i-keep-using-the-rtm-api}

You can! But not forever. [Legacy classic apps are set to be deprecated November 2026](/changelog/2024-09-legacy-custom-bots-classic-apps-deprecation). Without those legacy apps, there will be no way to access the RTM API. Try the [Events API](/apis/events-api/) instead!

## App approvals {#app-approvals}

### How does my app get approved for the Slack Marketplace? {#get-approved}

Refer to the following guide: [Slack Marketplace review guide](/slack-marketplace/slack-marketplace-review-guide).

### What happens if I make changes to an application that has been approved for the Slack Marketplace? {#app-approval-change}

If you need to update your approved app to request new [OAuth scopes](/authentication/installing-with-oauth#asking) or to include new features, find your application's settings page at [https://api.slack.com/apps](https://api.slack.com/apps). Any changes you make here will not affect the published app.

Once you're ready to apply these changes to the published app, you'll need to [resubmit it for review](/slack-marketplace/slack-marketplace-review-guide).

### What kind of changes to my app will require being reviewed again? {#app-approval-review}

If you've submitted your app to the Slack Marketplace but need to make changes to how your app or bot is described, to the integration types packed into your app, or to request additional permissions, you'll need your app to be reviewed again.

Use the beta application corresponding to your submitted Slack app to make modifications to any of these features, such as:

*   Requesting new OAuth permission [scopes](/authentication/installing-with-oauth#asking)
*   Changing your message button action URLs
*   Changing your slash command execution URLs & other details about your [slash command](/interactivity/implementing-slash-commands)
*   Changing your [Events API](/apis/events-api/) subscription URLs or subscriptions
*   Changing your [bot user's](/authentication/tokens) username
*   Changing your app's OAuth configuration
*   Changing details about how your application is presented in the Slack Marketplace
    *   Application description
    *   Contact information
    *   Application icon
    *   Policy & Website URLs

Your client secret and signing secret may be regenerated as needed, without requesting further review.

### Do I need to submit my Slack App to the Slack Marketplace if I don't want to? {#slack-marketplace}

No, only submit your app to the Slack Marketplace if you want your app to be discoverable and installable from the Slack Marketplace. If you don't submit your app, we won't display it there, but it will be installable by any workspace you give the authorization URL to.

## Scaling your app {#scaling-your-app}

### How do I avoid long response times and timeouts while working on behalf of large workspaces? {#workspaces}

If using the [`conversations.list`](/reference/methods/conversations.list) API method, use the `exclude_members` parameter to trim long membership lists from each channel object.

## Team vs. workspace {#team-vs-workspace}

### Why is an ID for a workspace is called team_id, not workspace_id? {#workspace-naming}

Our bad. We used to overuse the term _team_ which could mean two different things—_the people you talk to_, as well as the Slack workspace, _the place you do work_!

Now, we use _workspace_ for all the Slack workspaces; however, our API remains the same as before. Wherever you see some objects containing `team_id`, it really is an ID for the workspace! In the API world, we use the two terms interchangeably.

## Transitioning from IRC & XMPP gateways {#gateways}

### How do I build an IRC or XMPP gateway for myself using the API? {#IRC-XMPP-APIs}

Building your own gateway for personal use is an undertaking.

The part of the gateway that reads from Slack should either connect to the legacy [RTM API](/legacy/legacy-rtm-api) over a WebSocket or listen for events using the [Events API](/apis/events-api/). Use the [Web API](/apis/web-api/) to post messages and perform channel operations. The XMPP or IRC part of the gateway is its own adventure to explore.

Choose the [token type](/authentication/tokens) that works best for you. Bot user tokens work well if your user is a bot, but poorly if your user is you. [Properly scoped](/authentication/tokens) user tokens work best, as they model your own relationship to Slack. The `client` scope is useful, but overly broad and not suitable for an app distributed on the Slack Marketplace. Using your user token to post as yourself when posting messages with the [`chat.postMessage`](/reference/methods/chat.postMessage) API method is best.

Apps operating as a gateway should **never** distribute their API keys, secrets, or tokens.

## Workflow Builder {#workflows}

### Is it possible to add a workflow to multiple channels? {#channels-workflows}

While you cannot add a single workflow to multiple channels, you can download a workflow file, import it into Slack, and update the channel in which it triggers. To download a workflow file, within Workflow Builder, click on the three dots beside the workflow you would like to download and click **Download workflow file**.

### Is it possible to have workflows branch into different paths based on answers? {#workflows-branch}

Yes! As of **July 2025**, adding conditional branching/conditional logic to workflows is available to Slack workspaces on Business+ or Enterprise plans. Refer to [this article](https://slack.com/help/articles/42799802523283-Add-a-branch-to-a-workflow) in the Slack help center for more details.

## Apps created with the Deno Slack SDK: developers {#automations-workflow-apps}

### How do I set up my development environment? {#setupenv}

Head to the [Quickstart guide](/tools/deno-slack-sdk/guides/getting-started) to use our automated installer script, or download the latest version of the Slack CLI and follow instructions to install it manually.

If you have installed the Slack CLI previously and have an older version, note that the minimum required Slack CLI version for an Enterprise org as of September 19th, 2023 is `v2.9.0`. If you attempt to log in with an older version, you'll receive a `cli_update_required` error from the Slack API. Run `slack upgrade` to get the latest version.

Using a combination of your favorite text editor, the Slack CLI, and the included Deno Slack SDK, you'll develop using TypeScript with a [Deno](/tools/deno-slack-sdk/guides/installing-deno) runtime environment.

### Which hosts are involved in the creation and execution of apps created with the Slack CLI? {#hosts}

Apps created with the Deno Slack SDK are closely tied to specific language runtimes and SDKs. As you install and utilize your developer tools, you should expect requests from your network to the following non-exhaustive list of hosts:

*   `api.slack.com`, configuration information and documentation resources
*   `downloads.slack-edge.com`, where binaries and other static resources are hosted by Slack
*   `slack.com`, where most of the individual APIs reside called by the Slack CLI and your app
*   `slackb.com`, general logging for your triggers, functions, and workflows
*   `slackd.com`, where we send information about errors, warnings, and other special conditions
*   `deno.land`, where the Typescript runtime, Deno, resolves & retrieves dependencies and versions
*   `jsr.io`, where additional runtime packages and related dependencies are registered

### How can two or more developers collaborate on an app? {#collaboration}

Refer to [team collaboration](/tools/deno-slack-sdk/guides/collaborating-with-teammates).

### How do I build a slash command in apps created with the Deno Slack SDK? {#slashcommands}

Workflows can be started manually by users via [link triggers](/tools/deno-slack-sdk/guides/creating-link-triggers). There are multiple ways to invoke a link trigger, and one of them is with a `/` keystroke via the [shortcut menu](/interactivity/implementing-shortcuts#global).

In other words, you can use a slash command to invoke a link trigger that will kick off a workflow.

### Which languages are supported in Slack's managed infrastructure? {#languages}

At this time, apps deployed to Slack's managed infrastructure are built with [Typescript](/tools/deno-slack-sdk/guides/developing-with-typescript) in a [Deno runtime environment](/tools/deno-slack-sdk/guides/developing-with-deno).

### What's the difference between running and deploying an app? {#runordeploy}

When you use [`slack run`](/tools/deno-slack-sdk/guides/developing-locally), the local development version of your app connects to Slack via socket mode directly from where you're developing. As you use Slack (or other tools) to interact with your app's triggers, workflows, and functions, data is sent back and forth against your latest saved code. Use this while you're still tweaking things. Your development app is generally only shared with other collaborators, though you can test the full range of trigger options anyway.

When you use [`slack deploy`](/tools/deno-slack-sdk/guides/deploying-to-slack), the fine computer instructions you've written are packaged up and deployed to Slack's managed infrastructure. As users interact with your app, data is swiftly and securely sent back and forth between Slack servers. Treat this instance of your app with care, especially as your userbase grows.

The local and deployed environments have different triggers associated with them. Triggers you create in a local context will not automatically be created in a deployed context once your app is deployed.

### Can I list my app in the Slack Marketplace? {#slack-marketplace}

Currently, automations apps are not eligible for listing in the Slack Marketplace.

### How do I call a third-party API? {#third-party}

An example of how to do this is shown in the [GitHub Issue tutorial](/tools/deno-slack-sdk/tutorials/github-issues-app), but the long and short of it is as follows:

*   Store API credentials as local environment variables. In the GitHub tutorial, for instance, your `.env` file could look like this:

```
github_name = slackbotsbestbuddygithub_token = ABC123DEF
```

*   Use the `env` [context property](/tools/deno-slack-sdk/guides/creating-custom-functions#context) to call environment variables from within your function.

```
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";export const MyFunctionDefinition = DefineFunction({  callback_id: "my_function",  title: "my function",  source_file: "functions/my_function.ts",  input_parameters: { properties: {}, required: [] },  output_parameters: { properties: {}, required: [] },});export default SlackFunction(  MyFunctionDefinition,  async ({ inputs, env }) => { // Add this    const headers = {      Authorization: `Bearer ${env.GITHUB_TOKEN}`,      "Content-Type": "application/json",    };    try {      const endpoint = "https://api.github.com/users/repos";      const response = await fetch(endpoint, { method: "GET", headers });      if (response.status != 200) {        // In the case where the API responded with non 200 status        const body = await response.text();        const error =          `Failed to call an API (status: ${response.status}, body: ${body})`;        return { error };      }      // Do cool stuff with your repo info here      const repos = await response.json();      return { outputs: {} };    } catch (err) {      const error = `Failed to call GitHub API due to ${err}`;      return { error };    }  },);
```

That's all! When you run your app, it will use the environment variables stored within your `.env` file. You won't be using your `.env` file when your app is deployed (nor should you ever commit that file to source control), so the real power of environment variables is seen when you use the `env` Slack CLI [helper](/tools/slack-cli/reference/commands/slack_env). Once your app is deployed using `slack deploy`, add your environment variable with the following command:

```
slack env add github_token ABC123DEF
```

If your token contains non-alphanumeric characters, wrap it in double quotes. Environment variables added via the `slack env add` command can be accessed via the `env` Slack CLI [helper](/tools/slack-cli/reference/commands/slack_env), which also allows you to `update` and `remove` them.

### Can I import additional libraries and SDKs? {#deno-library}

Yes, you can! To use a [Deno Third Party Module](https://deno.land/x), Deno imports modules using URLs. You can see how we do this for a test file in the [Deno GitHub functions sample app](https://github.com/slack-samples/deno-github-functions).

```
// /functions/create_issue_test.tsimport * as mf from "https://deno.land/x/mock_fetch@0.3.0/mod.ts";
```

### How can I use the Slack CLI to set up a Continuous Integration and Continuous Delivery (CI/CD) pipeline? {#cicd}

The Slack CLI is commonly used in local development (usually in an interactive mode with prompts), but can also be used for automating testing and deployments (done without interactivity by using flags) by way of a [CI/CD pipeline](/tools/slack-cli/guides/setting-up-ci-cd-with-the-slack-cli).

Running this type of automation requires authorization with a service token. Refer to [CI/CD authorization](/tools/slack-cli/guides/authorizing-the-slack-cli#ci-cd) for more details. You'll also need to accommodate requests from your network to a variety of hosts. Refer to [Which hosts are involved in the creation and execution of apps created with the Slack CLI?](#hosts) for more details.

## Automations platform: administrators {#admins}

Even some Slack developers are themselves Slack administrators, but if you're an admin you might find yourself here wondering these very same questions. If you don't find the answer to your administrative questions here, consult the [Slack help center for more user and admin-facing content](https://slack.com/resources/slack-for-admins/app-management).

### How do custom workflow steps work? {#custom-workflow-steps}

*   Developers can build and publish workflows for anyone in their Slack workspace or Enterprise organization to use. They can also build [custom workflow steps](/tools/deno-slack-sdk/guides/creating-custom-functions) that users will be able to add to workflows they create with Workflow Builder.
*   When developers build workflows and custom workflow steps, they can set access permissions to determine who can run a workflow or add a custom workflow step to a workflow. Admins can further [restrict access to custom workflow steps](https://slack.com/help/articles/13621100461203) if they’d like.
*   You can now view some workflows on the [published workflow dashboard](https://slack.com/help/articles/15363614064275/). Workflows built with Workflow Builder will still need to be viewed and managed from the **All Published Workflows** tab in Workflow Builder.

### How do I turn off developer access to custom workflow steps and workflows? {#admin_access}

The new custom workflow steps and workflows introduced to the Slack platform cannot be completely disabled. Instead, you can manage their installation via the [app approvals](https://slack.com/help/articles/222386767-Manage-app-approval-for-your-workspace) feature.

### How do I discover and manage which custom workflow steps and workflows are installed in my workspace? {#admin_manage}

From the [published workflow dashboard](https://slack.com/help/articles/15363614064275/), you can view a list of workflows in your workspace or Enterprise organization.

### How will I be charged for using the platform? {#pricing}

For the most up-to-date information about pricing, click here:

[Learn more about pricing](https://slack.com/help/articles/15363357403411/)

### Will existing custom integrations and Slack apps continue working? {#existing}

Existing Slack apps will continue working as expected. Some older apps might produce activity in Slack you can build custom workflow steps and workflows around. That said, automations are meant to co-exist with the rest of our platform and your existing integrations and customizations.

## Errata {#misc}

### Deployment and installation {#deployment}

The `slack deploy` command performs two operations:

1.  Deploys all functions associated with your app to the platform, and
2.  Installs your app into the selected workspace.

*   Slack is currently optimized for the first-party developer use case, in which the expectation is that the developer has access to the workspace where they’re building the app.
*   When the app is installed as part of `slack deploy`, the workflows that belong to that app are also “installed” (made available) in that workspace. Currently, there is no way for a coded workflow to be "installed" (via the parent app being installed) by anyone other than the developer. However, coded workflows do not have to be deployed alongside a trigger; since triggers don't belong to apps, all deployment and installation happens first and then a trigger is created separately afterward.
*   JSON or YAML-based app manifests are no longer how your app's configuration is canonically defined. Instead, both your app's configuration _and_ your function definitions will reside in `manifest.ts`.

## Feedback {#feedback}

Anything else on your mind? Let us know [here](/developer-support/#feedback)!