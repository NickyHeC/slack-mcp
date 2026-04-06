Source: https://docs.slack.dev/reference/methods/chat.scheduleMessage

# chat.scheduleMessage method

DocsCall generator

## Facts {#facts}

**Description**Schedules a message to be sent to a channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/chat.scheduleMessage
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.scheduleMessage
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_scheduleMessage
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().chatScheduleMessage
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

Channel, private group, or DM channel to send message to. Can be an encoded ID, or a name. See [below](#channels) for more details.

**`post_at`**`integer`Required

Unix timestamp representing the future time the message should post to Slack.

_Example:_ `299876400`

### Optional arguments

**`as_user`**`boolean`Optional

Set to `true` to post the message as the authed user, instead of as a bot. Defaults to false. Cannot be used by [new Slack apps](/quickstart). See [chat.postMessage](chat.postMessage#authorship).

_Example:_ `true`

**`attachments`**`string`Optional

A JSON-based array of structured attachments, presented as a URL-encoded string.

_Example:_ `[{"pretext": "pre-hello", "text": "text-world"}]`

**`blocks`**`string`Optional

A JSON-based array of structured blocks, presented as a URL-encoded string.

_Example:_ `[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]`

**`link_names`**`boolean`Optional

Find and link user groups. No longer supports linking individual users; use syntax shown in [Mentioning Users](/messaging/formatting-message-text#mentioning-users) instead.

_Example:_ `true`

**`markdown_text`**`string`Optional

Accepts message text formatted in markdown. This argument should not be used in conjunction with `blocks` or `text`. Limit this field to 12,000 characters.

_Example:_ `**This is bold text**`

**`parse`**`string`Optional

Change how messages are treated. See [chat.postMessage](chat.postMessage#formatting).

_Acceptable values:_ `none` `full`

_Example:_ `full`

**`reply_broadcast`**`boolean`Optional

Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.

_Example:_ `true`

**`text`**`string`Optional

How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.

_Example:_ `Hello world`

**`thread_ts`**`string`Optional

Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.

**`unfurl_links`**`boolean`Optional

Pass true to enable unfurling of primarily text-based content.

_Example:_ `true`

**`unfurl_media`**`boolean`Optional

Pass false to disable unfurling of media content.

_Example:_ `false`

**`metadata`**Optional

JSON object with event\_type and event\_payload fields, presented as a URL-encoded string. Metadata you post to Slack is accessible to any app or user who is a member of that workspace.

_Example:_ `{"event_type": "task_created", "event_payload": { "id": "11223", "title": "Redesign Homepage"}}`

## Usage info {#usage-info}

Bug alert

Messages scheduled with `chat.scheduleMessage` will not post if the `metadata` parameter is used.

This method schedules a [message](/messaging) for delivery to a public channel, private channel, or direct message (DM) conversation at a specified time in the future. Messages scheduled through this method can be seen by calling the [`chat.scheduledMessages.list`](/reference/methods/chat.scheduledMessages.list) API method.

## The text, blocks and attachments fields {#text-blocks-attachments}

The usage of the `text` field changes depending on whether you're using `blocks`. If you're using `blocks`, this is used as a fallback string to display in notifications. If you aren't, this is the main body text of the message. It can be formatted as plain text, or with `mrkdwn`.

## Restrictions {#restrictions}

You will only be able to schedule a message up to 120 days into the future. If you specify a `post_at` timestamp beyond this limit, you’ll receive a `time_too_far` error response. Additionally, you cannot schedule more than 30 messages to post within a 5-minute window to the same channel. Exceeding this will result in a `restricted_too_many` error.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "channel": "C123ABC456",  "scheduled_message_id": "Q1298393284",  "post_at": "1562180400",  "message": {    "text": "Here's a message for you in the future",    "username": "ecto1",    "bot_id": "B123ABC456",    "attachments": [      {        "text": "This is an attachment",        "id": 1,        "fallback": "This is an attachment's fallback"      }    ],    "type": "delayed_message",    "subtype": "bot_message"  }}
```

#### Typical error response if the post_at is invalid (ex. in the past or too far into the future)

```
{  "ok": false,  "error": "time_in_past"}
```

The response includes the `scheduled_message_id` assigned to your message. Use it with the [`chat.deleteScheduledMessage`](/reference/methods/chat.deleteScheduledMessage) API method to delete the message before it is sent.

For details on formatting, usage in threads, and rate limiting, refer to the [`chat.postMessage`](/reference/methods/chat.postMessage) API method documentation.

## Channels {#channels}

You **must** specify a public channel, private channel, or DM conversation with the `channel` argument. Each one behaves slightly differently based on the authenticated user's permissions and additional arguments:

#### Post to a channel {#post-to-a-channel}

You can either pass the channel's name (`#general`) or the encoded ID (`C123ABC456`) and the message will be posted to that channel. The channel's ID can be retrieved through the [`conversations.list`](/reference/methods/conversations.list) API method.

#### Post to a DM {#post-to-a-dm}

Pass the DM conversation's channel ID (`D123ABC456`) or a user's ID (`U123ABC456`) as the value of `channel` to post to that DM conversation.

The DM conversation's channel ID can be retrieved by calling the [`conversations.list`](/reference/methods/conversations.list) API method. Use the `types` parameters to return only `im` conversations. You may receive a `channel_not_found` error if your app doesn't have permission to enter into an direct message with the intended user.

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

`invalid_blocks`

Blocks submitted with this message are not valid

`invalid_blocks_format`

The `blocks` is not a valid JSON object or doesn't match the Block Kit syntax.

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

`invalid_time`

value passed for `post_time` was invalid.

`invalid_token`

The passed token is invalid or not supported by this method.

`is_archived`

Channel has been archived.

`markdown_text_conflict`

Markdown text cannot be used in conjunction with `blocks` or `text` argument.

`message_limit_exceeded`

Members on this team are sending too many messages. For more details, see https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces

`metadata_must_be_sent_from_app`

Message metadata can only be posted or updated using an app-level token

`metadata_too_large`

Metadata exceeds size limit

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`msg_too_long`

Message text is too long

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

`restricted_action_thread_only_channel`

Cannot post top-level messages into a thread-only channel.

`restricted_too_many`

Too many messages were scheduled in the channel for a given period. See [usage info](/reference/methods/chat.scheduleMessage#restrictions) for additional details

`service_unavailable`

The service is temporarily unavailable

`slack_connect_file_link_sharing_blocked`

Admin has disabled Slack File sharing in all Slack Connect communications

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`time_in_past`

value passed for `post_time` was in the past.

`time_too_far`

value passed for `post_time` was too far into the future.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_attachments`

Too many attachments were provided with this message. A maximum of 100 attachments are allowed on a message.

`two_factor_setup_required`

Two factor setup is required.