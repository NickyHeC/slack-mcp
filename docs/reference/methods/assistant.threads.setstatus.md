Source: https://docs.slack.dev/reference/methods/assistant.threads.setStatus

# assistant.threads.setStatus method

DocsCall generator

## Facts {#facts}

**Description**Set the status for an AI assistant thread.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/assistant.threads.setStatus
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.assistant.threads.setStatus
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.assistant_threads_setStatus
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().assistantThreadsSetStatus
```

**Scopes**

Bot token:

[`chat:write`](/reference/scopes/chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Special rate limits apply.](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel_id`**`string`Required

Channel ID containing the assistant thread.

**`thread_ts`**`string`Required

Message timestamp of the thread of where to set the status.

**`status`**`string`Required

Status of the specified bot user, e.g., 'is thinking...'. A two minute timeout applies, which will cause the status to be removed if no message has been sent.

### Optional arguments

**`loading_messages`**`array`Optional

The list of messages to rotate through as a loading indicator. Maximum of 10 messages.

## Usage info {#usage-info}

Scope update

The `assistant.threads.setStatus` API method accepts either the [`assistant:write`](/reference/scopes/assistant.write) or [`chat:write`](/reference/scopes/chat.write) scope for the time being. Soon, this method will only accept the [`chat:write`](/reference/scopes/chat.write) scope. Read all about the change in this [changelog article](/changelog/2026/03/05/set-status-scope-update).

Use this method to push status updates to users in apps using AI features.

This method helps apps set expectations for potentially slow responses; e.g. "app is thinking...". The status will be automatically cleared when the app sends a reply. Sending an empty string in the `status` field will also clear the status indicator. This can be handy if you want to clear the status indicator without sending a new message.

The status is displayed as `<App Name> <status>`, and Slack automatically inserts the `<App Name>`. So for the example below, if the app's name is `YourAssistantJeeves`, the status would render as `YourAssistantJeeves is working on your request...`.

You can also set a custom loading state via the `loading_messages` parameter. The `loading_messages` parameter is an array of strings that Slack will rotate through showing to serve as a loading indicator.

Consider the following

Localizing the status indicator and loading state messages for the end user is a great way to provide a smooth user experience for everyone.

Example request:

```
{   "status": "is working on your request...",   "channel_id": "D324567865",   "thread_ts": "1724264405.531769"}
```

### Rate limits {#rate-limits}

Rate limiting conditions for this method include a default rate limit that is sufficient for most apps, with custom overrides determined on a per-team basis. The default limit is 600 requests per minute (per app per team).

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response for invalid channel

```
{  "ok": false,  "error": "channel_not_found",  "detail": "Invalid channel_id"}
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

`channel_not_found`

Error returned when given an invalid channel\_id

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

`invalid_thread_ts`

Error returned when given an invalid thread\_ts

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

`reserved_username`

Reserved usernames are not allowed to be used.

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