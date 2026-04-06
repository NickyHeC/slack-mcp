Source: https://docs.slack.dev/reference/methods/usergroups.create

# usergroups.create method

DocsCall generator

## Facts {#facts}

**Description**Create a User Group.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/usergroups.create
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.usergroups.create
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.usergroups_create
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().usergroupsCreate
```

**Scopes**

Bot token:

[`usergroups:write`](/reference/scopes/usergroups.write)

User token:

[`usergroups:write`](/reference/scopes/usergroups.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`name`**`string`Required

A name for the User Group. Must be unique among User Groups.

_Example:_ `My Test Team`

### Optional arguments

**`channels`**`array`Optional

A comma separated string of encoded channel IDs for which the User Group uses as a default.

**`additional_channels`**`array`Optional

A comma separated string of encoded channel IDs for which the User Group can custom add usergroup members too.

**`description`**`string`Optional

A short description of the User Group.

**`handle`**`string`Optional

A mention handle. Must be unique among channels, users and User Groups.

**`include_count`**`boolean`Optional

Include the number of users in each User Group.

_Example:_ `true`

**`team_id`**`string`Optional

Encoded team id where the user group has to be created, required if org token is used.

**`enable_section`**`boolean`Optional

Configure this user group to show as a sidebar section for all group members. Note: Only relevant if group has 1 or more default channels added.

_Example:_ `true`

## Usage info {#usage-info}

This method is used to create a User Group.

In order to call this method successfully, you'll need to ensure that your workspace settings allow you to manage user groups; otherwise you will receive a `permission_denied` error.

To update this setting, navigate to **Tools & settings > Workspace settings > Permissions > User Groups** within your workspace and update who can create, disable, or modify user groups from the drop-down menus.

The `team_id` is only relevant when using an org-level token. This field will be ignored if the API call is sent using a workspace-level token.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
```

If successful, the command returns a [usergroup object](/reference/objects/usergroup-object), including preferences:

```
    {        "ok": true,        "usergroup": {            "id": "S0615G0KT",            "team_id": "T060RNRCH",            "is_usergroup": true,            "name": "Marketing Team",            "description": "Marketing gurus, PR experts and product advocates.",            "handle": "marketing-team",            "is_external": false,            "date_create": 1446746793,            "date_update": 1446746793,            "date_delete": 0,            "auto_type": null,            "created_by": "U060RNRCZ",            "updated_by": "U060RNRCZ",            "deleted_by": null,            "prefs": {                "channels": [                ],                "groups": [                ]            },            "user_count": "0"        }    }
```

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

`bad_handle`

Handle is invalid

`deprecated_endpoint`

The endpoint has been deprecated.

`description_too_long`

Given usergroup description is too long

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`forbidden_handle`

Handle is invalid

`handle_already_exists`

Handle is already in use on this workspace

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

`invalid_channel_provided`

An invalid channel ID was provided

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_group_provided`

An invalid group ID was provided

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_argument`

A required argument is missing.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`missing_subteam_name`

Subteam name is required

`name_already_exists`

Name is already in use on this workspace

`name_too_long`

Name too long.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`paid_teams_only`

Usergroups can only be used on paid Slack teams

`permission_denied`

The user does not have permission to create a User Group.

`plan_upgrade_required`

This workspace does not have access to User Groups, as that feature is only available on Standard and above plans.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`target_team_must_be_specified_in_org_context`

No target team was specified but the team in context is an org

`target_team_not_on_org`

Target team specified is not on the org in context

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.