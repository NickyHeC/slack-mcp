Source: https://docs.slack.dev/reference/methods/chat.postMessage

# chat.postMessage method

DocsCall generator

## Facts {#facts}

**Description**Sends a message to a channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/chat.postMessage
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.postMessage
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_postMessage
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().chatPostMessage
```

**Scopes**

Bot token:

[`chat:write`](/reference/scopes/chat.write)

User token:

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

**`channel`**`string`Required

An encoded ID or channel name that represents a channel, private group, or IM channel to send the message to. See [below](#channels) for more details.

### Optional arguments

**`as_user`**`boolean`Optional

(Legacy) Pass true to post the message as the authed user instead of as a bot. Defaults to false. Can only be used by classic apps. See [legacy `as_user` parameter](#legacy_as_user) below.

_Example:_ `true`

**`attachments`**Optional

A JSON-based array of structured attachments, presented as a URL-encoded string.

_Example:_ `[{"pretext": "pre-hello", "text": "text-world"}]`

**`blocks`**Optional

A JSON-based array of structured blocks, presented as a URL-encoded string.

_Example:_ `[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]`

**`current_draft_last_updated_ts`**`string`Optional

This field represents the timestamp of the draft's last update at the time this API is called. If the current message is a draft, this field can be provided to ensure synchronization with the server.

_Example:_ `1524523204.000192`

**`icon_emoji`**Optional

Emoji to use as the icon for this message. Overrides `icon_url`.

_Example:_ `:chart_with_upwards_trend:`

**`icon_url`**Optional

URL to an image to use as the icon for this message.

_Example:_ `http://lorempixel.com/48/48`

**`link_names`**`boolean`Optional

Find and link user groups. No longer supports linking individual users; use syntax shown in [Mentioning Users](/messaging/formatting-message-text#mentioning-users) instead.

_Example:_ `true`

**`markdown_text`**`string`Optional

Accepts message text formatted in markdown. This argument should not be used in conjunction with `blocks` or `text`. Limit this field to 12,000 characters.

_Example:_ `**This is bold text**`

**`metadata`**Optional

JSON object with event\_type and event\_payload fields, presented as a URL-encoded string. You can also provide Work Object entity metadata using this parameter. Metadata you post to Slack is accessible to any app or user who is a member of that workspace.

_Example:_ `{"event_type": "task_created", "event_payload": { "id": "11223", "title": "Redesign Homepage"}}`

**`mrkdwn`**`boolean`Optional

Disable Slack markup parsing by setting to `false`. Enabled by default.

_Default:_ `true`

_Example:_ `false`

**`parse`**Optional

Change how messages are treated. See [below](#formatting).

_Example:_ `full`

**`reply_broadcast`**`boolean`Optional

Used in conjunction with `thread_ts` and indicates whether reply should be made visible to everyone in the channel or conversation. Defaults to `false`.

_Example:_ `true`

**`text`**Optional

How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.

_Example:_ `Hello world`

**`thread_ts`**Optional

Provide another message's `ts` value to make this message a reply. Avoid using a reply's `ts` value; use its parent instead.

**`unfurl_links`**`boolean`Optional

Pass true to enable unfurling of primarily text-based content.

_Example:_ `true`

**`unfurl_media`**`boolean`Optional

Pass false to disable unfurling of media content.

_Example:_ `false`

**`username`**Optional

Set your bot's user name.

_Example:_ `My Bot`

## Usage info {#usage-info}

This method posts [a message](/messaging) to a public channel, private channel, or direct message (DM, or IM) conversation.

Consider reviewing our [message guidelines](/surfaces/app-design), especially if you're using attachments or message buttons.

### The text, blocks and attachments fields {#text-blocks-attachments}

The usage of the `text` field changes depending on whether you're using `blocks`. If you're using `blocks`, this is used as a fallback string to display in notifications. If you aren't, this is the main body text of the message. It can be formatted as plain text, or with `mrkdwn`.

The `text` field is not enforced as required when using `blocks` or `attachments`. However, we highly recommended that you include `text` to provide a fallback when using `blocks`, as described above.

#### Accessibility considerations {#accessibility}

It is expected behavior that screen readers will default to the top-level `text` field of your post, and will not read the content of any interior `blocks` in the underlying structure of the message. Therefore, to make an accessible app, you must either:

*   include all necessary content for screen reader users in the top-level `text` field of your message, or
*   do not include a top-level `text` field if the message has `blocks`, and allow Slack attempt to build it for you by appending content from supported `blocks` to be read by the screen reader.

#### JSON POST support {#JSON_POST}

When POSTing with `application/x-www-form-urlencoded` data, the optional `attachments` argument should contain a JSON-encoded array of [attachments](/messaging/formatting-message-text).

Send JSON!

As of [October 2017](/changelog/2017-10-keeping-up-with-the-jsons), it's possible to send a well-formatted `application/json` POST body to `chat.postMessage` and other [Web API](/apis/web-api/) write methods. No need to carefully URL-encode your JSON `attachments` and present all other fields as URL encoded key:value pairs; just send JSON instead.

### Formatting messages {#formatting}

Messages are formatted as described in the [formatting spec](/messaging/formatting-message-text). The formatting behavior will change depending on the value of `parse`.

By default, URLs will be hyperlinked. Set `parse` to `none` to remove the hyperlinks.

The behavior of `parse` is different for text formatted with `mrkdwn`. By default, or when `parse` is set to `none`, `mrkdwn` formatting is implemented. To ignore `mrkdwn` formatting, set `parse` to `full`.

#### Unfurling content {#unfurling}

By default, we unfurl all links in any messages posted by users and Slack apps. We also unfurl links to media-based content within [Block kit blocks](/reference/block-kit/blocks).

If you want to suppress link unfurls in messages containing [Block Kit blocks](/reference/block-kit/blocks), set `unfurl_links` and `unfurl_media` to false.

For more detailed information about link unfurling, refer to [unfurling links in messages](/messaging/unfurling-links-in-messages).

#### Truncating content {#truncating}

For best results, limit the number of characters in the `text` field to 4,000 characters. Ideally, messages should be short and human-readable. Slack will [truncate messages](/changelog/2018-truncating-really-long-messages) containing more than 40,000 characters. If you need to post longer messages, please consider [uploading a snippet instead](/reference/methods/files.upload).

If using `blocks`, the limit and truncation of characters will be determined by the specific type of [block](/reference/block-kit/blocks).

### Threads and replies {#threads}

Provide a `thread_ts` value for the posted message to act as a reply to a parent message. Sparingly, set `reply_broadcast` to `true` if your reply is important enough for everyone in the channel to receive.

See [threading message](/messaging#threading) for a more in-depth look at message threading.

### Channels {#channels}

You **must** specify a public channel, private channel, or an IM channel with the `channel` argument. Each one behaves slightly differently based on the authenticated user's permissions and additional arguments, as discussed in the sections below.

#### Post to a public channel {#public}

Pass the channel name or the channel's ID (`C123456`) to the `channel` parameter and the message will be posted to that channel. The channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.

#### Post to a private channel {#private}

As long as the authenticated user is a member of the private channel, pass the channel's ID (`C123456`) to the `channel` parameter and the message will be posted to that channel. The private channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.

#### Post to a multi-person direct message channel {#mpdm}

As long as the authenticated user is a member of the multi-person direct message (a "private group" or MPIM), you can pass the group's ID (`G123456`) and the message will be posted to that group. The private group's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.

#### Post to a direct message channel {#dm}

Posting to direct messages (also known as DMs or IMs) can be a little more complex, depending on what you actually want to accomplish.

If you want your app's bot user to start a 1:1 conversation with another user in a workspace, provide the user's ID as the `channel` value and a direct message conversation will be opened if it isn't open already. Resultant messages and associated direct message objects will have a direct message ID you can use from that point forward, if you'd rather.

Bot users **cannot** post to a direct message conversation between two users using `chat.postMessage`. If your app was involved in the conversation, then it would be a multi-person direct message instead. Apps can post to direct message conversations between users when a [shortcut](/interactivity/implementing-shortcuts) or [slash command](/interactivity/implementing-slash-commands) belonging to that app is used in the conversation.

You will receive a `channel_not_found` error if your app doesn't have permission to enter into a DM with the intended user.

Passing a "username" as a `channel` value is deprecated, along with [the whole concept of _usernames_ on Slack](/changelog/2017-09-the-one-about-usernames).

Please _always_ use channel-like IDs instead to make sure your message gets to where it's going.

#### Getting a user's ID {#get-userID}

A list of user IDs can be retrieved via the [`users.list`](/reference/methods/users.list) API method.

### Begin a conversation in a user's App Home {#app_home}

Start a conversation with users in your [App Home](/surfaces/app-home).

With the `chat:write` scope enabled, call `chat.postMessage` and pass a user's ID (`U123456`) as the value of `channel` to post to that user's App Home channel. You can use their direct message channel ID (as found with `conversations.open`, for instance) instead.

### Rate limiting {#rate_limiting}

`chat.postMessage` has special [rate limiting](/apis/web-api/rate-limits) conditions. It will generally allow an app to post 1 message per second to a specific channel. There are limits governing your app's relationship with the entire workspace above that, limiting posting to several hundred messages per minute. Generous burst behavior is also granted.

### Channel membership {#channel_membership}

New Slack apps do _not_ begin life with the ability to post in all public channels.

For your new Slack app to gain the ability to post in all public channels, request the [`chat:write.public`](/reference/scopes/chat.write.public) scope.

* * *

### Sending messages as other entities {#authorship}

Apps can publish messages that appear to have been created by a user in the conversation. The message will be attributed to the user and show their profile photo beside it.

This is a powerful ability and must only be used when the user themselves gives permission to do so. For this reason, this ability is only available when an app has requested and been granted an additional scope — [`chat:write.customize`](/reference/scopes/chat.write.customize).

Your app should only use this feature in response to an inciting user action. It should never be unexpected or surprising to a user that a message was posted on their behalf, and it should be heavily signposted in advance.

To modify the appearance of the app, make calls to [`chat.postMessage`](/reference/methods/chat.postMessage) while providing any of the following parameters:

*   `username` to specify the username for the published message.
*   `icon_url` to specify a URL to an image to use as the profile photo alongside the message.
*   `icon_emoji` to specify an emoji (using colon shortcodes, eg. `:white_check_mark:`) to use as the profile photo alongside the message.

If the `channel` parameter is set to a User ID (beginning with `U`), the message will appear in that user's direct message channel with Slackbot. To post a message to that user's direct message channel with the app, use the DM ID (beginning with `D`) instead.

The [`chat.delete`](/reference/methods/chat.delete) method has no accommodations for impersonation. If a message is sent impersonating another user, you will not be able to call `chat.delete` to delete that same message.

* * *

## Response {#response}

#### Response including the "timestamp ID" (ts) and the channel-like thing where the message was posted. It also includes the complete message object, as parsed by our servers. This may differ from the provided arguments as our servers sanitize links, attachments, and other properties. Your message may mutate.

```
{  "ok": true,  "channel": "C123ABC456",  "ts": "1503435956.000247",  "message": {    "text": "Here's a message for you",    "username": "ecto1",    "bot_id": "B123ABC456",    "attachments": [      {        "text": "This is an attachment",        "id": 1,        "fallback": "This is an attachment's fallback"      }    ],    "type": "message",    "subtype": "bot_message",    "ts": "1503435956.000247"  }}
```

#### Typical error response if too many attachments are included

```
{  "ok": false,  "error": "too_many_attachments"}
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

`deprecated_endpoint`

The endpoint has been deprecated.

`draft_already_deleted`

The draft has already been deleted.

`draft_already_sent`

The draft has already been sent.

`draft_has_conflict`

The client draft version is out of sync with the server draft version.

`draft_not_found`

The draft was not found.

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

`invalid_blocks`

Blocks submitted with this message are not valid.

`invalid_blocks_format`

The `blocks` is not a valid JSON object or doesn't match the Block Kit syntax.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_metadata_format`

Invalid metadata format provided.

`invalid_metadata_schema`

Invalid metadata schema provided.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`is_archived`

Channel has been archived.

`markdown_text_conflict`

Markdown text cannot be used in conjunction with `blocks` or `text` argument.

`message_limit_exceeded`

Members on this team are sending too many messages. For more details, see https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces.

`messages_tab_disabled`

Messages tab for the app is disabled.

`metadata_must_be_sent_from_app`

Message metadata can only be posted or updated using an app-level token.

`metadata_too_large`

Metadata exceeds size limit.

`method_deprecated`

The method has been deprecated.

`missing_file_data`

Attempted to share a file but some required data was missing.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`msg_blocks_too_long`

Blocks submitted with this message are too long.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`no_text`

No message text provided.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`not_in_channel`

Cannot post user messages to a channel they are not in.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`rate_limited`

Application has posted too many messages, [read the Rate Limit documentation](/apis/web-api/rate-limits) for more information.

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

Admin has disabled Canvas File sharing in all Slack Connect communications.

`slack_connect_file_link_sharing_blocked`

Admin has disabled Slack File sharing in all Slack Connect communications.

`slack_connect_lists_sharing_blocked`

Admin has disabled Lists sharing in all Slack Connect communications.

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

* * *

## Legacy concerns {#legacy}

Information in the section below applies only to classic apps.

This feature works differently for classic apps.

### Legacy authorship {#legacy_authorship}

Classic apps using the umbrella `bot` scope can't request additional scopes to adjust message authorship.

#### Legacy as_user parameter {#legacy_as_user}

For classic apps, the best way to control the authorship of a message was to be explicit with the legacy `as_user` parameter. If you didn't use the `as_user` parameter, `chat.postMessage` would guess the most appropriate `as_user` interpretation based on the kind of token you were using. If `as_user` was not provided at all, the value was inferred based on the scopes granted to the caller: If the caller _could_ post with `as_user` passed as `false`, then that was how the method behaved; otherwise, the method behaved as if `as_user` were passed as `true`. When the `as_user` parameter was set to `false`, messages were posted as "[`bot_messages`](/reference/events/message/bot_message)", with message authorship attributed to the user name and icons associated with the classic app.

#### Effect on identity {#legacy_identity_effect}

Token types provide varying default identity values for `username`, `icon_url`, and `icon_emoji`.

*   [Test tokens](/legacy/legacy-custom-integrations/legacy-custom-integrations-tokens) inherits the icon and username of the token owner.
*   Slack App user token with `chat:write:user` inherits the icon and username of the token owner.
*   Slack App bot user token inherits Slack App's icon and app's bot username.

#### Legacy identity rules in DMs {#legacy_identity_dm}

If using `icon_url`, `icon_emoji`, or `username` with `chat.postMessage` and a direct message, some special rules apply to ensure the receiver is crystal clear about who is sending the message:

*   If the legacy `as_user` argument was false:
    *   Pass the DM channel's ID (`D123456`) as the value of `channel` to post to that DM channel _as the app, bot, or user associated with the token_. You can change the icon and username that go with the message using the `icon_url` and `username` parameters. The IM channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.
*   If the legacy `as_user` parameter was true:
    *   Pass the DM channel's ID (`D123456`) or a user's ID (`U123456`) as the value of `channel` to post to that DM channel _as the app, bot, or user associated with the token_. The IM channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method. When `as_user` is true, the caller may _not_ manipulate the icon and username on the message.