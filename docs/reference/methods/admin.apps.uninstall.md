Source: https://docs.slack.dev/reference/methods/admin.apps.uninstall

# admin.apps.uninstall method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**Uninstall an app from one or many workspaces, or an entire enterprise organization.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.apps.uninstall
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.apps.uninstall
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_apps_uninstall
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminAppsUninstall
```

**Scopes**

User token:

[`admin.apps:write`](/reference/scopes/admin.apps.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 1: 1+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`app_id`**`string`Required

The ID of the app to uninstall.

_Example:_ `A12345`

### Optional arguments

**`team_ids`**`string`Optional

IDs of the teams to uninstall from (max 100). With an org-level token, this or `enterprise_id` is required.

**`enterprise_id`**`string`Optional

The enterprise to completely uninstall the application from (across all workspaces). With an org-level token, this or `team_ids` is required.

_Example:_ `E12345`

## Usage info {#usage-info}

Managing app approval

When used in an admin app to approve or restrict other app installs across an entire Enterprise organization, the UI-based process is disabled and the admin app solely manages apps.

This endpoint will uninstall an app from one or many workspaces, or an entire enterprise.

Exactly one of the arguments `enterprise_id` or `team_ids` is required to specify where the app should be removed.

Admin apps that work with [SCIM](/admins/scim-api/), [app management](/admins/managing-app-approvals), or certain other enterprise-level features cannot be uninstalled using this API. To remove one of those, please [contact support](mailto:devsupport@slack.com).

Uninstalling an app cannot be undone.

Once an application is uninstalled, users must reinstall it manually if they wish to restore it.

* * *

## Response {#response}

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`app_not_found`

The provided `app_id` was not found.

`can_not_uninstall`

This application can not be uninstalled via the API.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`enterprise_not_found`

The provided `enterprise_id` was not found.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

The Admin APIs feature is not enabled for this team.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`must_revoke_access`

Organization-deployed apps cannot be uninstalled from specific workspaces using this API.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`permission_denied`

You do not have permission to uninstall applications from the reqeusted org or workspaces.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

the user is not authorized to perform this action

`service_unavailable`

The service is temporarily unavailable

`specify_enterprise_or_teams`

Provide exactly one of `enterprise_id` or `team_ids`.

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`teams_not_found`

One or more of the provided `team_ids` were not found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_teams`

Too many IDs are present in `team_ids`.

`two_factor_setup_required`

Two factor setup is required.