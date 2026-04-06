Source: https://docs.slack.dev/reference/methods/chat.update

# chat.update method

DocsCall generator

## Facts {#facts}

**Description**Updates a message.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/chat.update
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.update
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_update
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().chatUpdate
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

Channel containing the message to be updated. For direct messages, ensure that this value is a DM ID (starts with `D`) instead of a User ID (starts with either `U` or `W`).

**`ts`**`string`Required

Timestamp of the message to be updated.

_Example:_ `"1405894322.002768"`

### Optional arguments

**`as_user`**Optional

Pass true to update the message as the authed user. Bot users in this context are considered authed users.

_Example:_ `true`

**`attachments`**Optional

A JSON-based array of structured attachments, presented as a URL-encoded string.

_Example:_ `[{"pretext": "pre-hello", "text": "text-world"}]`

**`unfurled_attachments`**Optional

A JSON-based array of structured attachments, presented as a URL-encoded string.

_Example:_ `[{"pretext": "pre-hello", "text": "text-world"}]`

**`blocks`**Optional

A JSON-based array of structured blocks, presented as a URL-encoded string.

_Example:_ `[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]`

**`markdown_text`**`string`Optional

Accepts message text formatted in markdown. This argument should not be used in conjunction with `blocks` or `text`. Limit this field to 12,000 characters.

_Example:_ `**This is bold text**`

**`metadata`**Optional

JSON object with event\_type and event\_payload fields, presented as a URL-encoded string. If you don't include this field, the message's previous `metadata` will be retained. To remove previous `metadata`, include an empty object for this field. Metadata you post to Slack is accessible to any app or user who is a member of that workspace.

_Example:_ `{"event_type": "task_created", "event_payload": { "id": "11223", "title": "Redesign Homepage"}}`

**`link_names`**Optional

Find and link channel names and usernames. Defaults to `none`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `none`.

_Example:_ `true`

**`parse`**Optional

Change how messages are treated. Defaults to `client`, unlike `chat.postMessage`. Accepts either `none` or `full`. If you do not specify a value for this field, the original value set for the message will be overwritten with the default, `client`.

_Example:_ `none`

**`text`**Optional

How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.

_Example:_ `Hello world`

**`reply_broadcast`**`boolean`Optional

Broadcast an existing thread reply to make it visible to everyone in the channel or conversation.

_Default:_ `false`

_Example:_ `true`

**`file_ids`**`array`Optional

Array of new file ids that will be sent with this message.

_Example:_ `F013GKY52QK,F013GL22D0T or ["F013GKY52QK","F013GL22D0T"]`

## Usage info {#usage-info}

This method updates a message in a channel. Though related to [`chat.postMessage`](/reference/methods/chat.postMessage), some parameters of `chat.update` are handled differently.

Ephemeral messages created by [`chat.postEphemeral`](/reference/methods/chat.postEphemeral) or otherwise cannot be updated with this method.

New Slack apps may use this method with the [`chat:write`](/reference/scopes/chat.write) scope and either a bot or user token.

To define your message, refer to our [formatting spec](/messaging/formatting-message-text) and our guide to [composing messages](/messaging).

### text, blocks or attachments {#text-blocks-attachments}

This method will behave differently depending on whether `blocks` or `text` is supplied. Slack will always try to render the message using `blocks`, and use `text` only for notifications. If you don't include `blocks`, the message's previous `blocks` will only be retained if the `text` argument is not provided. If the `text` argument is provided and `blocks` are not provided, the `blocks` will be removed, and the provided `text` will be used for message rendering. To remove previous `blocks`, include an empty array for the `blocks` field. If `blocks` are used and a message is being updated, the `edited` flag will not be displayed on the message (the flag will be displayed on the message if using `text`).

Similarly, the `attachments` field is required when not presenting `text`. If you don't include `attachments`, the message's previous `attachments` will be retained. To remove previous `attachments`, include an empty array for this field.

## Valid message types {#valid-message-types}

Only messages posted by the authenticated user are able to be updated using this method. This includes regular chat messages, as well as messages containing the `me_message` subtype. Bot users may also update the messages they post.

Attempting to update other message types will return a `cant_update_message` error.

To use `chat.update` with a bot users token, you'll need to _think of your bot user as a user_, and pass `as_user` set to `true` while editing a message created by that same bot user.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "channel": "C123ABC456",  "ts": "1401383885.000061",  "text": "Updated text you carefully authored",  "message": {    "text": "Updated text you carefully authored",    "user": "U34567890"  }}
```

#### Typical error response

```
{  "ok": false,  "error": "cant_update_message"}
```

The response includes the `text`, `channel` and `timestamp` properties of the updated message so clients can keep their local copies of the message in sync.

### Updating interactive messages {#updating-interactive-messages}

If you're posting an [interactive message](/messaging/creating-interactive-messages), you may use `chat.update` to continue updating ongoing state changes around a message. Provide the `ts` field the message you're updating and follow the bot user instructions above to update message text, and remove or add blocks.

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

`block_mismatch`

Rich-text blocks cannot be replaced with non-rich-text blocks

`blocked_file_type`

Admin has disabled uploading this type of file.

`cant_broadcast_message`

Unable to broadcast this message.

`cant_update_message`

Authenticated user does not have permission to update this message.

`channel_not_found`

Value passed for `channel` was invalid.

`deprecated_endpoint`

The endpoint has been deprecated.

`edit_window_closed`

The message cannot be edited due to the team message edit settings

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_channel_migrating`

The channel is in the process of migrating and so the message cannot be updated at this time.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_deleted`

File to share deleted.

`file_is_deleted`

The file is deleted.

`file_not_found`

One or more of the provided file IDs could not be found.

`file_share_limit_reached`

The file has reached the share limit.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_attachments`

The attachments were invalid.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_blocks`

The blocks were invalid for the requesting user.

`invalid_blocks_format`

The `blocks` array is not a valid JSON object or doesn't match the Block Kit syntax.

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

`is_inactive`

The message cannot be edited within a frozen, archived or deleted channel.

`markdown_text_conflict`

Markdown text cannot be used in conjunction with `blocks` or `text` argument.

`max_file_sharing_exceeded`

Exceeded max allowed files shared.

`message_limit_exceeded`

Members on this team are sending too many messages. For more details, see https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces.

`message_not_found`

No message exists with the requested timestamp.

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

Message text is too long. The `text` field cannot exceed 4,000 characters.

`no_dual_broadcast_content_update`

Can't broadcast an old reply and update the content at the same time.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`no_text`

No message text provided

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`posting_to_channel_denied`

The user does not have permission to share files in this channel.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`slack_connect_blocked_file_type`

Files with certain extensions are blocked from being uploaded in all Slack Connect messages.

`slack_connect_canvas_sharing_blocked`

Admin has disabled sharing of canvas links in all Slack Connect messages.

`slack_connect_clip_sharing_blocked`

Admin has disabled Clip uploads in Slack Connect channels.

`slack_connect_file_link_sharing_blocked`

Admin has disabled Slack file sharing in all Slack Connect messages.

`slack_connect_file_upload_sharing_blocked`

Admin has disabled file uploads in all Slack Connect messages.

`streaming_state_conflict`

The message is currently streaming text and cannot be edited.

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_found`

Team associated with the message and channel could not be found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_attachments`

Too many attachments were provided with this message. A maximum of 100 attachments are allowed on a message.

`two_factor_setup_required`

Two factor setup is required.

`unable_to_share_files`

Sharing the files failed.

`update_failed`

Internal update failure.