Source: https://docs.slack.dev/reference/methods/chat.stopStream

# chat.stopStream method

DocsCall generator

## Facts {#facts}

**Description**Stops a streaming conversation.

**Method Access**

*   HTTP
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.stopStream
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.stopStream
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_stopStream
```

**Scopes**

Bot token:

[`chat:write`](/reference/scopes/chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

An encoded ID that represents a channel, private group, or DM

**`ts`**Required

The timestamp of the streaming message.

### Optional arguments

**`chunks`**`array`Optional

Array of streaming chunks that can contain either markdown text or task updates.

**`markdown_text`**`string`Optional

Accepts message text formatted in markdown. Limit this field to 12,000 characters.

_Example:_ `**This is bold text**`

**`blocks`**Optional

A list of blocks that will be rendered at the bottom of the finalized message.

**`metadata`**Optional

JSON object with event\_type and event\_payload fields, presented as a URL-encoded string. Metadata you post to Slack is accessible to any app or user who is a member of that workspace.

_Example:_ `{"event_type": "task_created", "event_payload": { "id": "11223", "title": "Redesign Homepage"}}`

## Usage info {#usage-info}

Use the `chat.stopStream` method to end a streaming conversation initiated with the [`chat.startStream`](/reference/methods/chat.startStream) method.

The Python Slack SDK and Node Slack SDK both provide a helper utility for the `chat.*Stream` methods that are surfaced in [Bolt for Python](/tools/bolt-python/concepts/message-sending) and [Bolt for JavaScript](/tools/bolt-js/concepts/message-sending).

### Using the chunks parameter {#chunks}

The `chunks` parameter can include [markdown text chunk](#markdown_text-chunks) objects, [task update chunk](#task_update-chunks) objects, or [plan update chunks](#plan_update-chunks).

#### markdown_text chunks {#markdown_text-chunks}

The `markdown_text` chunk is used for streaming text content with markdown formatting support.

```
{  "type": "markdown_text",  "text": "We love Sandra"}
```

#### task_update chunks {#task_update-chunks}

The `task_update` chunk object looks mighty similar to the [task card block](/reference/block-kit/blocks/task-card-block)!

The `task_update` chunk is used for displaying task progress in a timeline-style UI.

```
{  "type": "task_update",  "id": "unique_task_id",  "title": "Remind Sandra how amazing she is",  "status": "pending" | "in_progress" | "complete" | "error",  "details": "wow such good details",  "output": "amazing output here",  "sources": [      {      "type": "url",      "text": "Example.com",      "url": "https://example.com"    }  ]}
```

#### plan_update chunks {#plan_update-chunks}

The `plan_update` chunk is used for updating the title of a plan.

```
{  "type": "plan_update",  "title": "Sandra's new and improved plan"}
```

* * *

## Response {#response}

#### Typical success response when stopping a streaming message

```
{  "ok": true,  "channel": "C123ABC456",  "ts": "1503435956.000247",  "message": {    "text": "Here's the final streamed message content",    "bot_id": "B123ABC456",    "ts": "1503435956.000247",    "type": "message",    "subtype": "bot_message"  }}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
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

`as_user_not_supported`

The `as_user` parameter does not function with workspace apps.

`attachment_payload_limit_exceeded`

Attachment payload size is too long.

`cannot_reply_to_message`

This message type cannot have thread replies.

`channel_not_found`

Value passed for `channel` was invalid.

`channel_type_not_supported`

Channel type not supported.

`deprecated_endpoint`

The endpoint has been deprecated.

`duplicate_channel_not_found`

Channel associated with `client_msg_id` was invalid.

`duplicate_message_not_found`

No duplicate message exists associated with `client_msg_id`.

`ekm_access_denied`

Your message couldn’t be sent because your admins have disabled sending messages to this channel.

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

`invalid_metadata_format`

Invalid metadata format provided

`invalid_metadata_schema`

Invalid metadata schema provided

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`is_archived`

Channel has been archived.

`message_limit_exceeded`

Members on this team are sending too many messages. For more details, see https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces

`message_not_found`

The message was not found.

`message_not_in_streaming_state`

The message is not in a streaming state.

`message_not_owned_by_app`

The message is not owned by the app.

`messages_tab_disabled`

Messages tab for the app is disabled.

`metadata_must_be_sent_from_app`

Message metadata can only be posted or updated using an app-level token

`metadata_too_large`

Metadata exceeds size limit

`method_deprecated`

The method has been deprecated.

`missing_file_data`

Attempted to share a file but some required data was missing.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`no_text`

No message text provided

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`not_in_channel`

Cannot post user messages to a channel they are not in.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`rate_limited`

Application has posted too many messages, [read the Rate Limit documentation](/apis/web-api/rate-limits) for more information

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

A workspace preference prevents the authenticated user from posting.

`restricted_action_non_threadable_channel`

Cannot post thread replies into a non\_threadable channel.

`restricted_action_read_only_channel`

Cannot post any message into a read-only channel.

`restricted_action_thread_locked`

Cannot post replies to a thread that has been locked by admins.

`restricted_action_thread_only_channel`

Cannot post top-level messages into a thread-only channel.

`service_unavailable`

The service is temporarily unavailable

`slack_connect_canvas_sharing_blocked`

Admin has disabled Canvas File sharing in all Slack Connect communications

`slack_connect_file_link_sharing_blocked`

Admin has disabled Slack File sharing in all Slack Connect communications

`slack_connect_lists_sharing_blocked`

Admin has disabled Lists sharing in all Slack Connect communications

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_found`

This error occurs if, when using an org-wide token, the `channel_name` is passed instead of the `channel_id`.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_attachments`

Too many attachments were provided with this message. A maximum of 100 attachments are allowed on a message.

`too_many_contact_cards`

Too many contact\_cards were provided with this message. A maximum of 10 contact cards are allowed on a message.

`two_factor_setup_required`

Two factor setup is required.