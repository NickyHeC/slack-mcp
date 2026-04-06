Source: https://docs.slack.dev/admins/managing-app-approvals

# Managing app approvals

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

An admin app can [approve](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization) or restrict other app installs across an entire Enterprise org. The app handles app management for each workspace in the org, replacing the [UI process](https://slack.com/help/articles/360024269514#manage-approved-apps).

Be careful: when you install an app to manage app approvals in an Enterprise organization, you must process all app approvals and restrictions with this app, and the workspace-level UI **App Management Settings** UI options will be disabled. If you wish to restore the **App Management Setting** UI, you'll need to revoke the token you used to approve apps, or delete the app management app entirely.

* * *

## Overview {#overview}

When an admin enables the [**Approve apps**](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization) setting in Slack, apps must then be requested by a Slack user and approved by an admin before they're actually installed for a team to use. The approval process helps admins ensure that each app installed on a workspace is trustworthy.

However, for Enterprise organization admins handling approvals, app requests for each individual workspace in the organization can add up to a major time-suck.

[Previously, approving or restricting an app install request could only happen in a UI separate from the Slack client](https://slack.com/help/articles/360000281563-Manage-apps-in-an-Enterprise-organization).

![App install request in UI](/assets/images/app-install-request-394d83209854bf88af0a4f52fcbd3aac.png)

Now, app approval can be managed by a single app across all workspaces. Instead of using the UI, Enterprise organization admins can delegate the approval work to an app. The app can implement any specific logic that the admin would like—for example, allowlisting the Google Drive app on any workspace.

When you use an app to handle app management with this API, it replaces the App Management UI. The _Approve apps_ setting is turned on for each workspace automatically.

Keep reading for a more detailed walk-through on app management.

* * *

## Scopes {#scopes}

Two scopes enable an app to manage app install approvals across an Enterprise org: [`admin.apps:read`](/reference/scopes/admin.apps.read) and [`admin.apps:write`](/reference/scopes/admin.apps.write).

*   The [`admin.apps:read`](/reference/scopes/admin.apps.read) scope allows the app to list app install requests, and to subscribe to the [`app_requested`](#events) event.
*   The [`admin.apps:write`](/reference/scopes/admin.apps.write) scope allows the app to [approve](/reference/methods/admin.apps.approve) or [restrict](/reference/methods/admin.apps.restrict) requests for an app install.

All `admin.*` scopes are obtained using the normal [OAuth flow](/authentication), but there are a few extra requirements. The OAuth installation must be initiated by an Enterprise org admin or owner. Also, the install must take place on the Enterprise org, not on an individual workspace using the workspace switcher during the install flow.

![Installing the app on a workspace](/assets/images/workspace-v-org-audit-10f163aac79dc5f2c15e3ebe8267dbf4.png)

Check out the [`admin.apps:read`](/reference/scopes/admin.apps.read) documentation for more detail.

* * *

## Listen with the app_requested event {#events}

Now that you've got your management app off the ground, you can begin listening for app install requests. The [`app_requested`](/reference/events/app_requested) event from the [Events API](/apis/events-api/) notifies your app of exactly those requests. It's triggered any time a user on any team in your Enterprise organization requests that an app be installed.

Subscribe to the `app_requested` event by navigating to your [App page](https://api.slack.com/apps) and selecting **Event Subscriptions** in the sidebar. The **Add Workspace Event** button will lead you to the `app_requested` event. You'll need to reinstall your app for your subscription to take effect.

Here's the truncated shape of an `app_requested` event:

```
{  "type": "app_requested",  "app_request":{      'id': string,      'app': {        'id': string,        'name': string,        'description': string,        'help_url': string,        'privacy_policy_url': string,        'app_homepage_url': string,        'app_directory_url': string,        'is_app_directory_approved': boolean,        'is_internal': boolean,        'developer_type': string,        'additional_info': ?string      },      ...  }}
```

In addition to the `app` field that contains details about the app that's been requested, you'll also see some other useful fields, some of which don't always appear if they're not relevant:

*   `previous_resolution`: whether the app was approved or restricted previously.
*   `user`: the user that requested the install.
*   `team`: the team that the user requested the install on.
*   `scopes`: the scopes that the requested install will grant on your workspace.

The developer\_type in each app helpfully describes its origin.

*   `internal`: the app was developed as part of this Enterprise org or workspace.
*   `third_party`: the app was developed by a third party, such as (but not limited to) those found in the Slack Marketplace.
*   `slack`: the app was built with love by Slack. Hello!

For a full payload example of an `app_requested` event, check out the [`app_requested`](/reference/events/app_requested) page.

Once you've got your ear to the ground listening for app install requests, read on to learn how to respond.

* * *

## Manage with approve and restrict methods {#methods}

### Approve an app install request {#approve}

Approve an app request with the [`approve`](/reference/methods/admin.apps.approve) method:

```
curl -F token=xoxp-... -F team_id=T9876 -F request_id=1234 https://slack.com/api/admin.apps.approve
```

The token is required, and must be imbued with the [`admin.apps:write`](/reference/scopes/admin.apps.write) scope. Follow the instructions in the [scope documentation](/reference/scopes/admin.apps.write) to obtain an admin scope.

You can use either `request_id` or `app_id` to identify which app to approve. Either can be obtained directly from the [`app_requested` event described above](#events), or from the [`list` method described below](#list). The `team_id` is also required: it specifies which workspace the app should be approved on.

You'll receive an `"ok": true` response when your approval is successful.

### Restrict an app install request {#restrict}

Similarly, you can restrict an app install with the [`restrict`](/reference/methods/admin.apps.restrict) method:

```
curl -F token=xoxp-... -F request_id=1234 https://slack.com/api/admin.apps.restrict
```

As above, the token is required, and must be imbued with the [`admin.apps:write`](/reference/scopes/admin.apps.write) scope. Follow the instructions in the [scope documentation](/reference/scopes/admin.apps.write) to obtain an admin scope. Either a `request_id` or `app_id` is also required to identify which app to restrict, and a `team_id` is required as well.

You'll receive an `"ok": true` response when your restriction is successful.

### List app install requests {#list}

Use the [`list`](/reference/methods/admin.apps.requests.list) method to see pending app install requests. The `list` method only shows requests that haven't yet been approved or restricted by your app.

```
curl -F token=xoxp-... -F team_id=T9876 https://slack.com/api/admin.apps.requests.list
```

You'll receive a response containing a list of `app_requests`, each of which is identical to what's found in the [`app_requested` event payload described above](#events).

* * *

## Sample app {#sample}

If you're looking for a sample app that uses these methods, look no further than this [admin app management app](https://github.com/slackapi/admin_app_management) built by Slack on GitHub.

* * *

## Apps created with the Deno Slack SDK {#workflow-apps}

[Apps created with the Deno Slack SDK](/tools/deno-slack-sdk) also have an admin approval process, and can have workflows added to them after approval. Those workflows still need to respect the approved scopes discussed above. For more information about the admin approval process for these apps, refer to [admin approval](/tools/deno-slack-sdk/guides/controlling-permissions-for-admins#approval-admins).

* * *

## Parting words {#parting-words}

App approvals build confidence that your organization is safe and secure. However, managing apps for every workspace in an Enterprise organization can take time and pull focus away from the most critical tasks.

Use the APIs for app management to build an app that automates app management, and gain peace of mind without the labor-intensive manual work.