Source: https://docs.slack.dev/reference/methods/admin.users.session.list

# admin.users.session.list method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**List active user sessions for an organization

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.users.session.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.users.session.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_users_session_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminUsersSessionList
```

**Scopes**

User token:

[`admin.users:read`](/reference/scopes/admin.users.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`team_id`**`string`Optional

The ID of the workspace you'd like active sessions for. If you pass a `team_id`, you'll need to pass a `user_id` as well.

_Example:_ `T1234`

**`user_id`**`string`Optional

The ID of user you'd like active sessions for. If you pass a `user_id`, you'll need to pass a `team_id` as well.

_Example:_ `U1234`

**`limit`**`integer`Optional

The maximum number of items to return. Must be between 1 - 1000 both inclusive.

_Default:_ `1000`

_Example:_ `100`

**`cursor`**`string`Optional

Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.

_Example:_ `5c3e53d5`

## Usage info {#usage-info}

This [Admin API](/admins) lists active login sessions to your Slack organization.

If no `user_id` and `team_id` are passed, you'll receive a paginated list of _all_ sessions.

When you pass `user_id` and `team_id` (which must be used together), you'll receive a list of active sessions by that user on the workspace specified by `team_id`.

These sessions can be used to reset a session with the [`invalidate` method](/reference/methods/admin.users.session.invalidate): the user will be logged out and forced to login again. If the user has multiple sessions with multiple devices, the other sessions will be unaffected.

If you'd like to reset _all sessions_ for a given user, use the [`admin.users.session.reset`](/reference/methods/admin.users.session.reset) method instead.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "active_sessions": [    {      "user_id": "U012S9M77JP",      "team_id": "E011E2SBBFC",      "session_id": 1112275520242,      "recent": {        "device_hardware": "Intel",        "os": "OS X",        "os_version": "10.15.7",        "slack_client_version": "91.0.4472.77",        "ip": "24.6.145.138"      },      "created": {        "device_hardware": "Intel",        "os": "OS X",        "os_version": "10.15.7",        "slack_client_version": "91.0.4472.77",        "ip": "24.6.145.138"      }    }  ]}
```

Inside an `active_session`, you'll find two objects: `recent` and `created`.

`recent` signifies the most recent version of the session, while `created` represents the original version of the session. This covers the case where the same session persists across multiple `slack_client_version`s (or OS versions or IPs).

If the session hasn't changed since creation, you'll **only** find `created` and not `recent`.

Both `recent` and `created` contain the following info:

*   `device_hardware`: The type of device for the session.
*   `os`: The operating system for the device.
*   `os_version`: The version of the OS.
*   `slack_client_version`: The version of the Slack client, if available.
*   `ip`: The IP address for the session.

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

`admin_unauthorized`

The owner of this token isn't authorized to list sessions.

`bots_not_allowed`

Bot sessions are not listed by this method.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

This method is only available to Enterprise customers.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

The provided token doesn't have access to this endpoint.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_cursor`

The cursor passed was invalid.

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

`missing_team`

A `team_id` must be provided with a `user_id`.

`missing_user`

A `user_id` must be provided with a `team_id`.

`no_active_sessions`

No active sessions were found.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

The owner of this token isn't an Org Owner or Admin.

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

There was an error finding the requested workspace.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

This method is currently not available.

`user_not_found`

There was an error finding the requested user.