Source: https://docs.slack.dev/reference/methods/admin.usergroups.listChannels

# admin.usergroups.listChannels method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**List the channels linked to an org-level IDP group (user group).

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.usergroups.listChannels
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.usergroups.listChannels
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_usergroups_listChannels
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminUsergroupsListChannels
```

**Scopes**

User token:

[`admin.usergroups:read`](/reference/scopes/admin.usergroups.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`usergroup_id`**Required

ID of the IDP group to list default channels for.

_Example:_ `S00000000`

### Optional arguments

**`team_id`**`string`Optional

ID of the the workspace.

_Example:_ `T00000000`

**`include_num_members`**`boolean`Optional

Flag to include or exclude the count of members per channel.

_Example:_ `true`

## Usage info {#usage-info}

This method's response is limited to the channels that the requesting token (and thus, the installing [Org Admin or Owner](https://slack.com/help/articles/360018112273-Roles-in-Slack#enterprise-grid-plan-1)) can see.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "channels": [    {      "id": "C024BE91L",      "name": "fun",      "team_id": "T024BE911",      "num_members": 34    },    {      "id": "C024BE91K",      "name": "more fun",      "team_id": "T024BE912"    },    {      "id": "C024BE91M",      "name": "public-channel",      "team_id": "T024BE911",      "is_redacted": true,      "num_members": 34    },    {      "id": "C024BE91N",      "name": "some more fun",      "team_id": "T024BE921"    }  ]}
```

#### Typical error response if the token provided is not associated with an Org Admin or Owner

```
{  "ok": false,  "error": "not_an_admin"}
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

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

The Admin APIs feature is not enabled for this workspace.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

The workspace specified is not part of this Enterprise organization.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_user`

The calling user is not valid.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed`

The calling user is not an admin or does not have necessary role

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

The token provided is not associated with an Org Admin or Owner.

`not_an_enterprise`

The token passed in does not belong to an Enterprise organization.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_found`

The workspace was not found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`usergroup_not_found`

The IDP group provided was not found.

`usergroup_not_linked_to_team`

The IDP group provided is not linked to the specified workspace.