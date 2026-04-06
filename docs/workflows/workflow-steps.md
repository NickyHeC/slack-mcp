Source: https://docs.slack.dev/workflows/workflow-steps

# Workflow steps

Custom workflow steps combine the utility of [Workflow Builder](/workflows/workflow-builder) with the custom functionality of your choosing. Workflow steps are functions that you add to an app that can then be used as steps in [Workflow Builder](/workflows/workflow-builder). You have the flexibility to create an app that contains workflow steps using the Deno Slack SDK, the Bolt framework, or entirely on your own, sans Slack tooling. This guide will talk through the differences in tooling to create workflow steps, how to manage your apps with workflow steps, and distribution options.

Custom workflow steps can be:

*   Slack-hosted, when created with the [Deno Slack SDK](/tools/deno-slack-sdk) and the [Slack CLI](/tools/slack-cli).
*   Self-hosted, when created with the Bolt framework (see [Bolt for Python](/tools/bolt-python/concepts/custom-steps), [Bolt for JavaScript](/tools/bolt-js/concepts/custom-steps), and [Bolt for Java](/tools/java-slack-sdk/guides/custom-steps) documentation to support this).
*   Used on their own or made available as steps for users in Workflow Builder with either the Deno Slack SDK or the Bolt framework. Any user can combine a limited set of steps and triggers to quickly set up an automation.
*   Connected to a Workflow Builder-created workflow via [Workflow Buttons](/tools/deno-slack-sdk/guides/creating-link-triggers#workflow_buttons) (as long as the second workflow is a [link trigger](/tools/deno-slack-sdk/guides/creating-link-triggers#workflow_buttons_create)).

However, note that you cannot:

*   Develop custom workflow steps using a Free plan.
*   Bring entire coded workflows into Workflow Builder—you can only bring in custom functions as Workflow Builder steps.
*   Run a workflow on an event (for example, "Workflow A executed").
*   Access a larger variety of APIs such as the [Admin API methods](/admins/managing-channels), [Slack SCIM API](/admins/scim-api/), and [Audit Logs API](/admins/audit-logs-api/).
*   Use the [app settings](https://api.slack.com/apps) to manage workflow steps in an app created with the Deno Slack SDK; Deno-based apps must use the CLI.
*   List your coded workflow in the [Slack Marketplace](/slack-marketplace).

## SDKs for building apps with workflow steps {#tooling}

The following Slack SDKs support custom workflow steps.

SDK

Language(s) supported

Hosting

Database option

More information

Bolt framework and underlying Slack SDK

[Python](/tools/bolt-python/concepts/custom-steps), [JavaScript](/tools/bolt-js/concepts/custom-steps), [Java](/tools/java-slack-sdk/guides/custom-steps)

Self-hosted

Use whichever external database suits your needs

The Bolt framework supports steps and are self-hosted.

[Deno Slack SDK](/tools/deno-slack-sdk/)

TypeScript

Slack-hosted

Use [datastores](/tools/deno-slack-sdk/guides/using-datastores), a Slack-hosted way to store data

The Deno Slack SDK is optimized for workflows, so it enables you to build steps, build workflows with your own steps, Slack steps, and connector steps, as well as utilize Slack datastores. Deno Slack SDK apps are hosted on Slack.

## Managing your app {#managing}

Slack offers two options for app management. Apps created with the Deno Slack SDK use the CLI exclusively, and apps created with the Bolt framework can be created in the CLI or the app settings.

➡️ Follow [this quickstart guide](/tools/deno-slack-sdk/guides/getting-started) to get started with the Slack CLI for a Deno Slack SDK app.

➡️ Pick your preferred language, then follow the quickstart for creating a Bolt app in [Python](/tools/bolt-python/getting-started), [JavaScript](/tools/bolt-js/getting-started) or [Java](/tools/java-slack-sdk/guides/getting-started-with-bolt); these guides show both options.

Adding workflow steps to your app requires it to be an org-ready app. To learn what this means and how to prepare your app in the app settings, refer to our [guide on org-ready apps](/enterprise/organization-ready-apps).

## Defining a custom workflow step {#defining}

How you define your custom workflow step varies based on which path of app creation you've selected.

### For Bolt apps {#for-bolt-apps}

Whether you created your app via the [app settings](https://api.slack.com/apps) or the CLI, you should add your custom step definitions in the [app settings](https://api.slack.com/apps) because this manifest is your app's source of truth. To add workflow steps to your app, first select your app from the list [here](https://api.slack.com/apps), then navigate to **App Manifest** and add the following event subscription, then save your changes:

```
    "settings": {        ...        "event_subscriptions": {            "bot_events": [                "function_executed"            ]        },    }
```

Once that is taken care of, navigate to **Workflow Steps** in the left nav menu. Click **Add Step** and heed any immediate warnings that may pop up, such as adding bot scopes and enabling your app for org-wide distribution. Then name your step, define its `callback_id`, and add any desired`input_parameters` and `output_parameters`. You will see the step reflected in this screen as well as in the app manifest. Navigate to **App Manifest** to see your newly created workflow step.

A step called "Update report" with a `callback_id` of `update_report` and two required input parameters, `report_date` and `report_update`, is reflected in the manifest like this:

```
    "functions": {        "update_report": {            "title": "Update report",            "description": "",            "input_parameters": {                "report_date": {                    "type": "slack#/types/date",                    "title": "Report Date",                    "description": "",                    "is_required": true,                    "name": "report_date"                },                "report_update": {                    "type": "string",                    "title": "Report Update",                    "description": "",                    "is_required": true,                    "name": "report_update"                }            },            "output_parameters": {}        }    }
```

### For apps built with the Deno Slack SDK {#for-apps-built-with-the-deno-slack-sdk}

Similar to Bolt apps, a function definition for the custom step needs to be added to the manifest. However, because these apps are not managed in the app settings, that looks a bit different. For an app created with the Deno Slack SDK, add the function definition in the `manifest.json` file locally. It may look something like this:

```
// /manifest.ts// Import the functionimport { GreetingFunctionDefinition } from "./functions/greeting_function.ts"// ...export default Manifest({  //...  functions: [GreetingFunctionDefinition],  //...});
```

## Implement function logic {#logic}

Once you've added your custom steps to your app manifest, you must implement the logic for how they will execute. This varies based on how you choose to write your app logic (refer to each framework's documentation linked above for specifics). Regardless of how the custom steps are implemented, they must finish by calling either the [functions.completeSuccess](/reference/methods/functions.completeSuccess) method or the [functions.completeError](/reference/methods/functions.completeError) method.

In [Bolt](/workflows/workflow-steps#anatomy), `complete` and `fail` are utility methods you can call at the completion of a function. Reference the [Custom steps for Bolt apps](/workflows/workflow-steps) guide.

In Deno, you will return either an `error` or `completed` object, along with the `outputs`. See the [Custom functions for workflows](/tools/deno-slack-sdk/guides/creating-custom-functions) guide for reference.

## App distribution {#distribution}

Distribution works differently for Slack apps that contain workflow steps when the app is within a standalone (non-Enterprise org) workspace versus within an Enterprise organization.

*   **Within a standalone workspace**: Slack apps that contain workflow steps can be installed on the same workspace and used within that workspace. We do not support distribution of workflow steps to other standalone workspaces (also known as public distribution).
*   **Within an organization**: Slack apps that contain workflow steps should be org-ready (enabled for private distribution) and installed on the organization level. They must also be granted access to at least one workspace in the organization for the steps to appear in Workflow Builder.

Apps containing workflow steps cannot be distributed publicly or submitted to the Slack Marketplace. We recommend sharing your code as a public repository in order to share workflow steps.

To protect your organization, external users (those outside your organization connected through Slack Connect) cannot use a workflow that contains [connector steps](/tools/deno-slack-sdk/reference/connector-functions) or [workflow steps](/workflows/workflow-steps) built by your organization.This may manifest in a `home_team_only` warning.

Refer to [this help center article](https://slack.com/help/articles/14844871922195-Slack-administration--Manage-workflow-usage-in-Slack-Connect-conversations#enterprise-grid-1) for more details.

## Next steps {#next-steps}

Curious about building your own?

➡️ Check out the tutorial for creating a **new** Bolt app with a custom step in [JavaScript](/tools/bolt-js/tutorials/custom-steps-workflow-builder-new) or [Python](/tools/bolt-python/tutorial/custom-steps-workflow-builder-new) and the tutorial for adding a custom step to an **existing** Bolt app in [JavaScript](/tools/bolt-js/tutorials/custom-steps-workflow-builder-existing) or [Python](/tools/bolt-python/tutorial/custom-steps-workflow-builder-existing).

➡️ Read more about [building workflow steps with the Deno Slack SDK here](/tools/deno-slack-sdk/guides/creating-custom-functions). Then check out a [step-by-step tutorial](/tools/deno-slack-sdk/tutorials/workflow-builder-custom-step/) for this functionality.