Source: https://docs.slack.dev/reference/methods/admin.users.invite

# admin.users.invite method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**Invite a user to a workspace.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.users.invite
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.users.invite
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_users_invite
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminUsersInvite
```

**Scopes**

User token:

[`admin.users:write`](/reference/scopes/admin.users.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`team_id`**Required

The ID (`T1234`) of the workspace.

**`email`**`string`Required

The email address of the person to invite.

_Example:_ `joe@email.com`

**`channel_ids`**`string`Required

A comma-separated list of `channel_id`s for this user to join. At least one channel is required.

_Example:_ `C1A2B3C4D,C26Z25Y24`

### Optional arguments

**`custom_message`**`string`Optional

An optional message to send to the user in the invite email.

_Example:_ `Come and join our team!`

**`real_name`**`string`Optional

Full name of the user.

_Example:_ `{"Joe Smith"}`

**`resend`**`boolean`Optional

Allow this invite to be resent in the future if a user has not signed up yet. Resending can only be done via the UI and has no expiration. (default: false)

_Example:_ `true`

**`is_restricted`**`boolean`Optional

Is this user a multi-channel guest user? (default: false)

**`is_ultra_restricted`**`boolean`Optional

Is this user a single channel guest user? (default: false)

**`guest_expiration_ts`**`string`Optional

Timestamp when guest account should be disabled. Only include this timestamp if you are inviting a guest user and you want their account to expire on a certain date.

_Example:_ `0123456789.012345`

**`email_password_policy_enabled`**`boolean`Optional

Allow invited user to sign in via email and password. Only available for Enterprise org teams via admin invite.

_Example:_ `true`

## Usage info {#usage-info}

This Admin API invites a user to a workspace. If this method is used on a workspace-level user who is deactivated on the org level, the user will be reactivated on both the workspace and the org level.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
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

`already_in_team`

The user is already on the team.

`already_in_team_invited_user`

The user has already been invited to the team.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`failed_looking_up_user`

We couldn't find the requested user.

`failed_to_send_invite`

The invite failed to send.

`failed_to_validate_caller`

The token calling this method doesn't have permission to invite a user.

`failed_to_validate_channels`

`channel_ids` was invalid.

`failed_to_validate_custom_message`

`extra_message` was invalid.

`failed_to_validate_expiration`

`expiration_ts` was invalid.

`failed_to_validate_team`

The team calling this method was invalid.

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

`invalid_email`

Email address was not valid.

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

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

The user token does not have admin privileges.

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

`team_id` was not found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`user_disabled`

The user is disabled.