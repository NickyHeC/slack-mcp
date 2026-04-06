Source: https://docs.slack.dev/admins/managing-workflow-and-connector-permissions

# Managing workflow and connector permissions

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

While Workspace Admins and Org Admins can manage workflow permissions and approval requests from the admin settings site dashboard, they may find using the API directly for these actions is more efficient, especially when it comes to bulk actions.

Each of the methods outlined here accepts an OAuth user token with the specified scope. If you're working with a classic app, read more about authorization [here](/authentication/installing-with-oauth), and if you're exploring new frontiers with workflows, read more about authorization [here](/tools/deno-slack-sdk/guides/integrating-with-services-requiring-external-authentication).

Read on to discover the API methods that help admins manage [workflows](/tools/deno-slack-sdk/guides/creating-workflows), [functions](/tools/deno-slack-sdk/guides/creating-custom-functions), and [connectors](/tools/deno-slack-sdk/reference/connector-functions) in their org.

## App management {#apps}

Use the following methods to manage apps in your org.

Method

Description

[`admin.apps.activities.list`](/reference/methods/admin.apps.activities.list)

Retrieves logs for an org or team

[`admin.apps.approve`](/reference/methods/admin.apps.approve)

Approves an app for installation in a workspace

[`admin.apps.clearResolution`](/reference/methods/admin.apps.clearResolution)

Clears an app resolution, undoing the effect of `admin.apps.approve` or `admin.apps.restrict`

[`admin.apps.restrict`](/reference/methods/admin.apps.restrict)

Restricts an app for installation in a workspace

[`admin.apps.uninstall`](/reference/methods/admin.apps.uninstall)

Uninstalls an app from one or many workspaces or an entire enterprise org

[`admin.apps.approved.list`](/reference/methods/admin.apps.approved.list)

Lists approved apps for an org or workspace

[`admin.apps.requests.cancel`](/reference/methods/admin.apps.requests.cancel)

Cancels an app request for a team

[`admin.apps.requests.list`](/reference/methods/admin.apps.requests.list)

Lists app requests for a team or workspace

[`admin.apps.restricted.list`](/reference/methods/admin.apps.restricted.list)

Lists restricted apps for an org or workspace

[`admin.apps.config.lookup`](/reference/methods/admin.apps.config.lookup)

Looks up the app config for connectors by their IDs

[`admin.apps.config.set`](/reference/methods/admin.apps.config.set)

Sets the app config for a connector

## Workflow management {#workflows}

Use the following methods to manage workflows in your org.

Method

Description

[`admin.workflows.search`](/reference/methods/admin.workflows.search)

Searches workflows within the team or enterprise

[`admin.workflows.permissions.lookup`](/reference/methods/admin.workflows.permissions.lookup)

Looks up permissions for a set of workflows

[`admin.workflows.unpublish`](/reference/methods/admin.workflows.unpublish)

Unpublishes workflows within the team or enterprise

[`admin.workflows.collaborators.add`](/reference/methods/admin.workflows.collaborators.add)

Adds collaborators to workflows within the team or enterprise

[`admin.workflows.collaborators.remove`](/reference/methods/admin.workflows.collaborators.remove)

Removes collaborators from workflows within the team or enterprise

## Function management {#functions}

Use the following methods to manage functions in your org.

Method

Description

[`admin.functions.list`](/reference/methods/admin.functions.list)

Looks up functions by a set of apps

[`admin.functions.permissions.lookup`](/reference/methods/admin.functions.permissions.lookup)

Looks up the visibility of multiple Slack functions and includes the users if it is limited to particular named entities

[`admin.functions.permissions.set`](/reference/methods/admin.functions.permissions.set)

Sets the visibility of a Slack function and defines the users or workspaces if it is set to `named_entities`