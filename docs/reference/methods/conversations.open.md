Source: https://docs.slack.dev/reference/methods/conversations.open

# conversations.open method

DocsCall generator

## Facts {#facts}

**Description**Opens or resumes a direct message or multi-person direct message.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.open
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.open
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_open
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsOpen
```

**Scopes**

Bot token:

[`channels:manage`](/reference/scopes/channels.manage)[`groups:write`](/reference/scopes/groups.write)[`im:write`](/reference/scopes/im.write)[`mpim:write`](/reference/scopes/mpim.write)

User token:

[`channels:write`](/reference/scopes/channels.write)[`groups:write`](/reference/scopes/groups.write)[`im:write`](/reference/scopes/im.write)[`mpim:write`](/reference/scopes/mpim.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`channel`**Optional

Resume a conversation by supplying an `im` or `mpim`'s ID. Or provide the `users` field instead.

**`return_im`**`boolean`Optional

Boolean, indicates you want the full IM channel definition in the response.

**`users`**`string`Optional

Comma separated lists of users. If only one user is included, this creates a 1:1 DM. The ordering of the users is preserved whenever a multi-person direct message is returned. Supply a `channel` when not supplying `users`.

**`prevent_creation`**`boolean`Optional

Do not create a direct message or multi-person direct message. This is used to see if there is an existing dm or mpdm.

## Usage info {#usage-info}

The [Conversations API](/apis/web-api/using-the-conversations-api) method opens a direct message (DM) or a multi-person direct message (MPIM).

You can then send a message to the conversation using the [`chat.postMessage`](/reference/methods/chat.postMessage) method.

Creating channels

Use the [\`conversations.create](/reference/methods/conversations.create) method instead for public or private channels.

##### Using the users parameter {#users-parameter}

Provide 1 to 8 user IDs in the `users` parameter to open or resume a conversation. Providing only 1 ID will create a direct message. Providing more than 1 will create a multi-person direct message (`mpim`).

Don’t include the ID of the user you’re calling `conversations.open` on behalf of – we do that for you.

If there are no conversations already in progress including that exact set of members, a new multi-person direct message conversation begins.

Subsequent calls to `conversations.open` with the same set of users will return the already existing conversation.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "channel": {    "id": "D069C7QFK"  }}
```

#### Passing return_im will expand the response to include more info about a conversation

```
{  "ok": true,  "no_op": true,  "already_open": true,  "channel": {    "id": "D069C7QFK",    "created": 1460147748,    "is_im": true,    "is_org_shared": false,    "user": "U069C7QF3",    "last_read": "0000000000.000000",    "latest": null,    "unread_count": 0,    "unread_count_display": 0,    "is_open": true,    "priority": 0  }}
```

#### Typical error response

```
{  "ok": false,  "error": "channel_not_found"}
```

The response structure is altered by providing `return_im` parameter. When set to `false`, the default, just a conversation's ID is returned. When set to `true`, the entire conversation object is returned.

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

`channel_not_found`

Value passed for `channel` was invalid.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

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

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_user_combination`

All external people must already be in at least one channel together to send a message.

`method_deprecated`

The method has been deprecated.

`method_not_supported_for_channel_type`

This type of conversation cannot be used with this method.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The calling token is not granted the necessary scopes to complete this operation.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`not_enough_users`

Needs at least 2 users to open

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

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_users`

Needs at most 8 users to open

`two_factor_setup_required`

Two factor setup is required.

`user_disabled`

A specified `user` has been disabled.

`user_not_found`

Value(s) passed for `users` was invalid.

`user_not_visible`

The calling user is restricted from seeing the requested user.

`users_list_not_supplied`

Missing `users` in request