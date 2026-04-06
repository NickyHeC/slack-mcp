Source: https://docs.slack.dev/reference/methods/canvases.access.set

# canvases.access.set method

DocsCall generator

## Facts {#facts}

**Description**Sets the access level to a canvas for specified entities

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/canvases.access.set
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.canvases.access.set
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.canvases_access_set
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().canvasesAccessSet
```

**Scopes**

Bot token:

[`canvases:write`](/reference/scopes/canvases.write)

User token:

[`canvases:write`](/reference/scopes/canvases.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`canvas_id`**Required

Encoded ID of the canvas

_Example:_ `F1234ABCD`

**`access_level`**Required

Desired level of access

_Acceptable values:_ `read` `write` `owner`

### Optional arguments

**`channel_ids`**`array`Optional

List of channels you wish to update access for. Can only be used if user\_ids is not provided.

_Example:_ `["C1234ABCD"]`

**`user_ids`**`array`Optional

List of users you wish to update access for. Can only be used if channel\_ids is not provided.

_Example:_ `["U1234ABCD"]`

## Usage info {#usage-info}

Canvases are only available to Slack workspaces on a paid plan.

The `canvases.access.set` method sets the access level to a canvas for specified entities. Call the `canvases.access.set` method to establish and set the desired access level for the canvas.

Both `channel_ids` and `user_ids` cannot be passed at the same time.

The possible `access_level` values are as follows:

*   `read`: grants read access to the canvas.
*   `write`: grants read and write access to the canvas.
*   `owner`: makes the specified user in `user_ids` the owner. If `channel_ids` is provided with this access level, the API method will return an `invalid_arguments` error because only users can be owners. Only the current file owner can set another user as the owner. Upgrades to the owner level for users from a different team than the one the canvas belongs to is not allowed.

Share the canvas link in the channel or with the user you are trying to set access levels for, respectively. For instance, if you are passing the `user_ids` argument to update a specific user's access, you must have sent the user the canvas directly _first_. Even if the user is a member of a channel where the canvas has been shared, calling the `canvases.access.set` method with a `user_ids` argument will fail. Since the permissions are set at the channel level, they must also be changed at the channel level.

### Sharing canvases via DM or MPDM {#sharing-canvases-via-dm-or-mpdm}

Access levels can only be set for regular channels. Channel IDs associated with direct messages (DMs) or multi-party direct messages (MPDMs) will not be accepted and will result in an unsuccessful request. For sharing a canvas to DMs or MPDMs, use individual user IDs instead.

* * *

### Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response when attempting to change the access of a channel canvas

```
{  "ok": false,  "error": "canvas_not_found"}
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

`canvas_disabled_user_team`

Canvas is disabled on user's team

`canvas_not_found`

The canvas you wish to update permissions for is not available.

`channel_not_found`

A channel could not be found.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`failed_to_update_user_ids`

Failed to update the specified user\_ids.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

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

`invalid_parameters`

One of user\_ids or channel\_ids must be defined, but not both.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

User does not have permission to perform this action.

`service_unavailable`

The service is temporarily unavailable

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

`user_not_found`

A user could not be found.