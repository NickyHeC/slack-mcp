Source: https://docs.slack.dev/reference/methods/chat.deleteScheduledMessage

# chat.deleteScheduledMessage method

DocsCall generator

## Facts {#facts}

**Description**Deletes a pending scheduled message from the queue.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/chat.deleteScheduledMessage
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.deleteScheduledMessage
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_deleteScheduledMessage
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().chatDeleteScheduledMessage
```

**Scopes**

Bot token:

[`chat:write`](/reference/scopes/chat.write)

User token:

[`chat:write`](/reference/scopes/chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The channel the scheduled\_message is posting to

_Example:_ `C123456789`

**`scheduled_message_id`**`string`Required

`scheduled_message_id` returned from call to chat.scheduleMessage

_Example:_ `Q1234ABCD`

### Optional arguments

**`as_user`**`boolean`Optional

Pass true to delete the message as the authed user with `chat:write:user` scope. Bot users in this context are considered authed users. If unused or false, the message will be deleted with `chat:write:bot` scope.

_Example:_ `true`

## Usage info {#usage-info}

This method deletes a pending scheduled message before it is sent.

There are two ways to determine the `scheduled_message_id` of a message you wish to delete:

*   The response of the [`chat.scheduleMessage`](/reference/methods/chat.scheduleMessage) endpoint contains the `scheduled_message_id` needed to delete that message.
*   You can also retrieve the `scheduled_message_id`s for all the messages you've scheduled by calling [`chat.scheduledMessages.list`](/reference/methods/chat.scheduledMessages.list).

## Restrictions {#restrictions}

You cannot delete scheduled messages that have already been posted to Slack _or_ that will be posted to Slack within 60 seconds of the delete request. If attempted, this method will respond with an `invalid_scheduled_message_id` error.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response if no message is found

```
{  "ok": false,  "error": "invalid_scheduled_message_id"}
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

`bad_token`

The provided `token` was invalid.

`channel_not_found`

The `channel` passed is either an invalid ID or does not exist.

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

`invalid_scheduled_message_id`

The `scheduled_message_id` passed is either an invalid ID, or the scheduled message it's referencing has already been sent or deleted.

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