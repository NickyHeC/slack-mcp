Source: https://docs.slack.dev/enterprise/developing-for-enterprise-orgs

# Developing apps for Enterprise orgs

[Enterprise orgs](/enterprise) allows large organizations to collaborate across many workspaces. While many apps, integrations, and bots will work as expected in an Enterprise org, there are enough new behaviors, conditions, and nuances to warrant reviewing your app for compatibility.

Read on if you are:

*   developing Slack apps for your own or other Enterprise org workspaces
*   readying Enterprise org support for tools, libraries, or frameworks

* * *

## Provisioning a sandbox {#sandbox}

Building properly for an [Enterprise org](/enterprise) or [shared channels](/apis/slack-connect/) requires experiencing the unique constraints and opportunities yourself. If you don't already have access to an Enterprise org of workspaces, the Slack Developer Program offers [developer sandboxes](/tools/developer-sandboxes) and the Slack Partner Developer Program offers [partner sandboxes](/tools/partner-sandboxes) for development and testing.

Sandboxes have a default lifespan of six months and are fully-featured Enterprise org environments that allow you to build against all of Slack's features safely and securely.

## Identifying Enterprise org workspaces {#identifying_an_enterprise_organization}

Workspaces don't always start out part of an Enterprise org. Thanks to mergers, acquisitions, and the inherent nature of life, any workspace may become part of an Enterprise org.

A single user may have an identity in Workspace A, and another in Workspace B. With an Enterprise org, you can reconcile those identities and make that user a cross-referenced entity identifiable across multiple workspaces.

### Enterprise IDs {#enterprise_id}

If your app is in a workspace that's part of an Enterprise organization, you will observe a constant and unique `enterprise_id` attribute through API methods and events. Below are notable methods:

*   [`auth.test`](/reference/methods/auth.test). We recommend using this method after [acquiring an OAuth token](/authentication). You'll want to poll it regularly for all workspaces you service, as workspaces migrate to an Enterprise org.
*   [`conversations.info`](/reference/methods/conversations.info). This API method appears in [shared channels](/apis/slack-connect/)
*   [`team.info`](/reference/methods/team.info).

If you store data, you'll want to warehouse the `enterprise_id` value. Just as you'd never store information about a user or their data without tying it to a workspace first, it's best to associate Enterprise org workspace data with its `enterprise_id`.

If your app is installed on multiple workspaces within an Enterprise organization, you may want to utilize that position effectively by grouping data by `enterprise_id` values and using those new values as your primary source of truth.

## Supporting the transition to an Enterprise org {#support}

Some platform features require additional support in Enterprise org workspaces.

Slack apps require you to:

*   Support [global user IDs](#user_ids).
*   Support users from other [workspaces](#identifying_an_enterprise_organization) within the same Enterprise org using your application features.

The [Events API](/apis/events-api/) requires you to:

*   Support events & messages containing [global user IDs](#user_ids).
*   Support users from other [workspaces](#identifying_an_enterprise_organization) in [shared channels](/apis/slack-connect/).

The [Web API](/apis/web-api/) requires you to:

*   Support user ID fields containing [global user IDs](#user_ids).
*   Support users from other [workspaces](#identifying_an_enterprise_organization) in [shared channels](/apis/slack-connect/).
*   Use [`users.info`](/reference/methods/users.info) to retrieve additional information on cross-workspace user IDs not found in [`users.list`](/reference/methods/users.list).

[Slash commands](/interactivity/implementing-slash-commands) require you to:

*   Toggle on **Escape channels, users, and links sent to your app** for all Slash commands within the _Slash Commands_ app management page. This will allow you to identify channels and users by ID. See the [Slash commands guide](/interactivity/implementing-slash-commands##creating_commands) for more info.
*   Support user ID fields containing [global user IDs](#user_ids)
*   Be aware that Slash commands can only be invoked by users belonging to the workspace it is installed in.

Legacy integrations

[Legacy bot users](/legacy/legacy-bot-users) are more likely than other integration points to require additional work for exemplary performance on Enterprise org workspaces.

[Legacy custom integrations](/legacy/legacy-custom-integrations/legacy-custom-integrations-migration) have few programmatic signals to interpret and off-the-shelf code may not know how to handle certain situations like [shared channels](/apis/slack-connect/).

[Legacy message buttons](/legacy/legacy-messaging/legacy-message-buttons) require you to support user ID fields containing [global user IDs](#user_ids) and to support action invocations by users from other workspaces.

[Legacy RTM API](/legacy/legacy-rtm-api) usage will require additional effort to prevent duplicative messages and other undesired behaviors. See [Using the RTM API in an Enterprise org](/legacy/legacy-rtm-api#enterprise) for more detail.

### Enable organization-wide installation {#opt}

To install your app in an Enterprise organization, it must become org-ready:

1.  Navigate to **OAuth & Permissions**, scroll down to **Scopes**, and add any bot scope to your app, such as [`team:read`](/reference/scopes/team.read). A bot scope is required for the next step to be available.
2.  In the **Org Level Apps** section in the sidebar, select **Opt-In**, then select **Yes, Opt-in** at the confirmation prompt. This will be reflected in the app manifest as follows:

```
    "settings": {        "org_deploy_enabled": true,        ...    }
```

3.  From the **Manage Distribution** section in the app settings sidebar, you will now see that **Private Distribution** is enabled Private distribution lets your app gain access to all of the workspaces in an organization.
4.  Select **Collaborators** under the **Settings** section. Add an Org Admin user as a collaborator.

Requesting to install the app to an organization means that an Org Admin will receive a direct message from Slackbot to review the request. Approving a request to install to the org means the admin installs the app to the org, then further decides which workspaces to add it to.

For more information about how to add apps to workspaces from your Enterprise organization, refer to [Manage apps in an Enterprise org](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization).

### Implement an OAuth flow {#oauth}

If you plan on making your app available for other organizations to install, or to list it in the Slack Marketplace, it is recommended that you follow the [OAuth flow](/authentication/installing-with-oauth). This option is only available to apps that do not have [custom steps](/workflows/workflow-steps).

When an Org Admin installs your app across the entire organization, it will not yet be installed to any workspaces in the organization. Therefore, once you have completed the OAuth flow, you'll likely want to redirect an installing Admin back to a modal that will allow them to add the app to individual workspaces. For example:

```
https://app.slack.com/manage/ORG_ID/integrations/profile/APP_ID/workspaces/add
```

You need to determine whether the installation happened on an organization, as opposed to an individual workspace. In order to do that, look for the `is_enterprise_install` boolean field in the [`oauth.v2.access`](/reference/methods/oauth.v2.access) API method response:

```
{    "ok": true,    "access_token": "xoxb-XXXX",    "token_type": "bot",    "scope": "identify,users:read",    "bot_user_id": "W123ABC456",    "app_id": "A123ABC456",    "team": null,    "enterprise": {        "id": "E123ABC456",        "name": "Jesse Slacksalot"    },    "is_enterprise_install": true,    "authed_user": {        "id": "WXXXX",        "access_token": "xoxp-XXXX"            ...    }}
```

You'll also want to consider redirecting your installer after OAuth for your organization-ready app, since the app won't actually be added to any workspaces yet. Consider redirecting to a modal that adds the app to workspaces, so that you can remind the installing Org Admin that they still need to do so:

```
https://app.slack.com/manage/ENTERPRISE_ID/integrations/profile/APP_ID/workspaces/add
```

### Handle unknown users gracefully {#handling_unknown_users}

If your app is used as part of a shared channel, it will encounter users it is not aware of, and the [`users.list`](/reference/methods/users.list) API method won't return users from other workspaces in its payload.

To find users from another workspace in an Enterprise org, use the [`users.info`](/reference/methods/users.info) method and query by their "foreign" user ID. Many apps need only a user's ID, and won't need additional information to operate.

Not only will you encounter user IDs belonging to other workspaces, but you'll also encounter the artifacts of their existence and workspace cross-pollination. Messages will be authored by these users, and if they fall within your app's functionality, you should respond as you normally would. Messages may also mention users on other workspaces. If your messages contain interactive elements, you may receive invoked actions from these users, and should handle them just as you would a "native" workspace user.

If you provide a slash command, you'll want to handle mentions of members from other workspaces. We strongly recommend turning on [entity resolution](/interactivity/implementing-slash-commands#entity_resolution) so that you can resolve mentioned users.

### Handle user object changes {#user_object_changes}

In order to work across an organization, your app needs to be prepared for users and channels that span multiple workspaces. You'll likely want to map users in Slack to users in your system.

If your app already stored some local IDs from a workspace that subsequently merged into an Enterprise organization, the [translation layer](/reference/methods/migration.exchange) will continue to work as it did before.

For more insight into working with users in Enterprise organizations, check out [the guide to single-workspace Enterprise apps](/enterprise/developing-for-enterprise-orgs#user_object_changes).

User objects on Enterprise org workspaces now have an `enterprise_user` attribute, containing fields with additional context about the user in the larger Enterprise organization:

`enterprise_user` fields

Description

`id`

The user's ID, which might start with `U` or `W`.

`enterprise_id`

The unique ID for this particular Enterprise organization.

`enterprise_name`

The name of this umbrella organization.

`is_admin`

A boolean value indicating whether this user administers this Enterprise organization.

`is_owner`

A boolean value indicating whether this user is the owner of this enterprise organization.

`teams`

An array of team (workspace) IDs within the containing enterprise organization that this user belongs to.

#### User IDs {#user_ids}

Within an Enterprise org, all users have a single, global ID beginning with either the letter `U` or `W`. The specific prefix does not indicate anything in particular.

Slack will automatically convert users' pre-Enterprise migration ID references to their singular Enterprise ID. This allows your app to remain backwards compatible for users identified on a workspace before the days of Enterprise orgs.

Users created after a workspace became part of an Enterprise will have no pre-Enterprise-migration ID.

### Shared channel considerations {#shared-channels}

Your odds of encountering a [Slack Connect](/apis/slack-connect/) channel are high when developing an app for an Enterprise org. These channels are [shared](/enterprise#understanding_shared_channels) between one or more workspaces or organizations.

When you develop your app, decide which features should work with Slack Connect channels.

Once you've done that, remember to determine the type of conversation you're working with before you perform an action. Call the [`conversations.info`](/reference/methods/conversations.info) method if you need to determine what kind of channel, DM, or MPDM you're dealing with.

### Internal integration considerations {#internal_integrations}

As with all Slack apps, installation and ownership of apps is on a workspace basis. Apps that are locked to a [single workspace](/app-management/distribution) cannot be installed across an Enterprise org.

### Slack Marketplace considerations {#slack_marketplace}

If your app is part of the Slack Marketplace, you'll want to let us know that you've prepared it for Enterprise org workspaces. We'll do some additional testing and give you feedback on anything that could be improved.

## Using APIs with organization-ready apps {#using-apis}

For the most part, APIs at Slack work the same with all apps. However, there are some exceptions.

### Use the team_id parameter {#methods}

Since your app's token now can represent installations in many workspaces, some API methods will require a `team_id` parameter to indicate which workspace to act on.

You may have certain installations of your app that are on a single workspace, while other installations are deployed across organizations. A safe option is to always pass a `team_id` parameter to these methods. If your token is a single-workspace installation, the `team_id` parameter will be accepted, but ignored.

Here's the full list of methods that require a `team_id` parameter when used by an organization-ready app:

*   [bots.info](/reference/methods/bots.info)
*   [chat.scheduledMessages.list](/reference/methods/chat.scheduledMessages.list)
*   [conversations.create](/reference/methods/conversations.create)
*   [conversations.list](/reference/methods/conversations.list)
*   [files.list](/reference/methods/files.list)
*   [migration.exchange](/reference/methods/migration.exchange)
*   [reactions.list](/reference/methods/reactions.list)
*   [search.all](/reference/methods/search.all)
*   [search.files](/reference/methods/search.files)
*   [search.messages](/reference/methods/search.messages)
*   [team.accessLogs](/reference/methods/team.accessLogs)
*   [team.billableInfo](/reference/methods/team.billableInfo)
*   [team.integrationLogs](/reference/methods/team.integrationLogs)
*   [team.profile.get](/reference/methods/team.profile.get)
*   [users.conversations](/reference/methods/users.conversations)
*   [users.list](/reference/methods/users.list)
*   [usergroups.users.update](/reference/methods/usergroups.users.update)
*   [usergroups.users.list](/reference/methods/usergroups.users.list)
*   [usergroups.update](/reference/methods/usergroups.update)
*   [usergroups.list](/reference/methods/usergroups.list)
*   [usergroups.create](/reference/methods/usergroups.create)
*   [usergroups.disable](/reference/methods/usergroups.disable)
*   [usergroups.enable](/reference/methods/usergroups.enable)

You can call API endpoints that do not use a `team_id` parameter, but the behavior may be inconsistent. For example, you can call the `conversations.read` API method to retrieve information from channels that are shared across multiple workspaces within the organization using an org token, even if the app is not deployed to any workspaces within the org. However, if a channel only exists on a single workspace, the app will fail to retrieve any information and will return a `team_access_not_granted` error instead.

### Use the context_team_id field {#context-team-id}

You may also come across the `context_team_id` field in your org-wide travels.

We use this field behind the scenes to resolve which channels come from which workspaces within the organization, and what roles and preferences are applied to those channels. For all channel types, this field represents the perspective through which the viewing user is accessing the channel. Let's look at an example.

Let's say there is an Enterprise org instance called Middle Earth. Within that instance, there are two workspaces: Rohan and Gondor. You are a user in the Gondor workspace.

*   For both workspace's non-shared channels—or for all channels that may be shared, but are hosted by your team (in this case, Gondor)—the team ID comes from the `team_id` field.
*   Now, someone in the Rohan workspace shares the _#oath-of-eorl_ channel with Gondor. In this case, since the shared channel is hosted by the "away" workspace, the team ID comes from the `context_team_id` field.

This field is used in outgoing dispatches only (such as Block Kit actions and other similar events); that is, it's not a field you'll be supplying to an API method call. We just wanted you to be aware of it and what it's used for in case it shows up in your logs! However, you _can_ optionally supply this same information by using the `client_context_team_id` field when calling any API method that requires the `channel` argument. A couple examples are the [`chat.postMessage`](/reference/methods/chat.postMessage) or [`chat.update`](/reference/methods/chat.update) API methods.

### Leverage additional event payload info {#events}

[Event](/reference/events) payloads now contain information on the \[`authorizations`\] they apply to.

You'll see the `is_enterprise_install` boolean inside the `authorizations` object. This boolean tells you whether the event is being sent to an organization-wide installation of your app.

```
{    "token": "XXYYZZ",    "is_ext_shared_channel": false,    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {...},    "type": "event_callback",    "event_id": "Ev123ABC456",    "event_time": 1234567890,    "authorizations": [        {            "enterprise_id": "E324567",            "team_id": "T423567",            "user_id": "W43567",            "is_bot": false,            "is_enterprise_install": true        }    ]}
```

The `authorizations` object is truncated at a single installation. If you're not sure which installations have the ability to see the event, call the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) API method to get a full installation list.

### Leverage additional events and methods {#new}

There are events and methods to help you keep track of which workspaces within an organization-wide deployment your app actually has access to.

Two [Events API](/apis/events-api/) events indicate to you when your organization-ready app has gained or lost access to a new workspace within your org:

*   [`team_access_granted`](/reference/events/team_access_granted)
*   [`team_access_revoked`](/reference/events/team_access_revoked)

Subscribe to these events to have an up-to-date list of workspaces to monitor and act in.

In addition, you can now use the [`auth.teams.list`](/reference/methods/auth.teams.list) API method to obtain a full list of workspaces your organization-ready app has been approved for. Call the method with your token acquired from installing your app in an Enterprise organization.

### The Events API {#events_api}

If you're using the [Events API](/apis/events-api/), you don't have to worry about duplicate messages from [shared channels](/apis/slack-connect/). We'll only send one event, regardless of how many workspaces within the organization your app is installed on.

Look for the `authorizations` field that arrives as part of the "wrapper" around delivered events. It contains a team ID within an organization that this delivery is on behalf of. Use the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) API method to obtain a full list of authorizations.

Here's an example payload of a shared channel's message being delivered on behalf of multiple workspaces:

```
{    "token": "JhjZd2rVax7ZwH7jRYyWjbDl",    "team_id": "T111AAA111",    "api_app_id": "A123ABC456",    "event": {        "type": "message",        "user": "W123ABC456",        "text": "It's time to slacktivate!",        "team": "T111AAA111",        "source_team": "T111AAA111",        "user_team": "T111AAA111",        "user_profile": {            "avatar_hash": "g56821b98743",            "image_72": "https://...png",            "first_name": "Jesse",            "real_name": "Jesse Slacksalot",            "name": "jesse.slacksalot"        },        "ts": "1485371714.000002",        "channel": "C123ABC456",        "event_ts": "1485371714.000002"    },    "type": "event_callback",    "authorizations": [        {            "enterprise_id": "E123ABC456",            "team_id": "T222BBB222",            "user_id": "U123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],}
```

In this example, the application is installed on two workspaces within an Enterprise organization, and is party to a conversation in a shared channel. The `source_team` field encapsulates the workspace within the Enterprise org that the message originates from, which is team `T111AAA111`. The message is then delivered as a single event for both teams `T111AAA111` and `T222BBB222` (though you'd have to query the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) API method to see both). For descriptions of other notable fields, see below:

Field

Description

`team_id`

This field encapsulates the team a user is logged into that is part of a particular channel. It is provided in a message, and can change depending on the session.

`team`

The workspace where the event is happening (or just happened) right now. This is typically the workspace the app is installed on.

`source_team`

This field encapsulates the workspace within the Enterprise org that the message originates from.

`user_team`

The team the user sending the message belongs to.

`authorizations`

This field shows one installation of your app that the event is visible to. Use the [`apps.event.authorizations.list`](/reference/methods/apps.event.authorizations.list) API method for a full list.

## When a workspace migrates to an Enterprise organization {#migration}

In most cases, an Enterprise org is formed by combining multiple independent Slack workspaces together. During this period of time where data is migrated and made compatible with an org's structures, platform interactions may be unavailable, both for users and your applications. For the Web API, you may encounter the `team_added_to_org` error during this time.

Migration time varies depending team-to-team and organization-to-organization. When encountering errors, practice an exponential backoff strategy to help manage these periods by attempting connections at incrementally increasing rates: 1 second to 3 seconds to 10 seconds to 30 seconds to 1 minute, and so on.

To best plan for migrations, subscribe to Enterprise org-related [app events](/apis/events-api/#app_events) as part of the Events API. Using these events, your app can pause and resume activity as appropriate:

*   [`grid_migration_started`](/reference/events/grid_migration_started)
*   [`grid_migration_finished`](/reference/events/grid_migration_finished)

If your app has disabled the translation layer, use the [`migration.exchange`](/reference/methods/migration.exchange) method to receive global user IDs for any of your stored local user IDs.

Refer to [migrating existing apps to an Enterprise org](/enterprise/migrating-to-organization-wide-deployment) for more information.

### Toggle the translation layer {#toggling_transition_layer}

For existing apps, the best thing you can do is to use the [`migration.exchange`](/reference/methods/migration.exchange) method to update all records you have for an existing workspace with those from an Enterprise org.

That way, you won't need to worry about a "translation layer" or maintaining two IDs for a single user.

Slack Apps can turn on a translation layer in their app settings that will display "local" historical user IDs beginning with `U` for users that existed prior to an Enterprise org migration for a workspace the app was already installed on. It also lets you use these classic user IDs within a migrated workspace; it's meant to be used temporarily.

We strongly recommend you turn this translation layer off after using [`migration.exchange`](/reference/methods/migration.exchange) and going all-in with global user IDs, regardless of which letter they start with.

Disable the translation layer by navigating to [application management](https://api.slack.com/apps) for your app and finding the **User ID Translation** panel. If you need to update local user IDs you've stored in a database or in other ways, first use the [`migration.exchange`](/reference/methods/migration.exchange) method with the relevant [user or bot tokens](/authentication/tokens) to receive global user IDs in bulk.

## Next steps {#next-steps}

✨ Read more about [using Slack Connect API methods](/apis/slack-connect/using-slack-connect-api-methods/).