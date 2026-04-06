Source: https://docs.slack.dev/reference/methods/chat.postEphemeral

# chat.postEphemeral method

DocsCall generator

## Facts {#facts}

**Description**Sends an ephemeral message to a user in a channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/chat.postEphemeral
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.postEphemeral
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_postEphemeral
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().chatPostEphemeral
```

**Scopes**

Bot token:

[`chat:write`](/reference/scopes/chat.write)

User token:

[`chat:write`](/reference/scopes/chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 4: 100+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

Channel, private group, or IM channel to send message to. Can be an encoded ID, or a name.

**`user`**Required

`id` of the user who will receive the ephemeral message. The user should be in the channel specified by the `channel` argument.

_Example:_ `U0BPQUNTA`

### Optional arguments

**`as_user`**`boolean`Optional

(Legacy) Pass true to post the message as the authed user. Defaults to true if the chat:write:bot scope is not included. Otherwise, defaults to false.

_Example:_ `true`

**`attachments`**Optional

A JSON-based array of structured attachments, presented as a URL-encoded string.

_Example:_ `[{"pretext": "pre-hello", "text": "text-world"}]`

**`blocks`**Optional

A JSON-based array of structured blocks, presented as a URL-encoded string.

_Example:_ `[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]`

**`icon_emoji`**`string`Optional

Emoji to use as the icon for this message. Overrides `icon_url`.

_Example:_ `:chart_with_upwards_trend:`

**`icon_url`**`string`Optional

URL to an image to use as the icon for this message.

_Example:_ `http://lorempixel.com/48/48`

**`link_names`**`boolean`Optional

Find and link channel names and usernames.

_Example:_ `true`

**`markdown_text`**`string`Optional

Accepts message text formatted in markdown. This argument should not be used in conjunction with `blocks` or `text`. Limit this field to 12,000 characters.

_Example:_ `**This is bold text**`

**`parse`**Optional

Change how messages are treated. Defaults to `none`. See [below](#formatting).

_Acceptable values:_ `none` `full` `mrkdwn` `false`

_Example:_ `full`

**`text`**Optional

How this field works and whether it is required depends on other fields you use in your API call. [See below](#text_usage) for more detail.

_Example:_ `Hello world`

**`thread_ts`**Optional

Provide another message's `ts` value to post this message in a thread. Avoid using a reply's `ts` value; use its parent's value instead. Ephemeral messages in threads are only shown if there is already an active thread.

**`username`**`string`Optional

Set your bot's user name.

_Example:_ `My Bot`

## Usage info {#usage-info}

This method posts an ephemeral message, which is visible only to the assigned user in a specific public channel, private channel, or private conversation.

Ephemeral message delivery is not guaranteed — the user must be currently active in Slack and a member of the specified `channel`. By nature, ephemeral messages do not persist across reloads, desktop and mobile apps, or sessions. Once the session is closed, ephemeral messages will disappear and cannot be recovered.

Use ephemeral messages to send users context-sensitive messages, relevant to the channel they're detectably participating in. Avoid sending unexpected or unsolicited ephemeral messages.

### Text usage: text, blocks or attachments {#text-blocks-attachments}

The usage of the `text` field changes depending on whether you're using `blocks`. If you're using `blocks`, this is used as a fallback string to display in notifications. If you aren't, this is the main body text of the message. It can be formatted as plain text, or with `mrkdwn`.

The `text` field is not enforced as required when using `blocks` or `attachments`. However, we highly recommended that you include `text` to provide a fallback when using `blocks`, as described above.

### Formatting {#formatting}

Messages are formatted as described in the [formatting spec](/messaging/formatting-message-text). You can specify values for `parse` and `link_names` to change formatting behavior.

The optional `attachments` argument should contain a JSON-encoded array of attachments.

For more information, see the [attachments spec](/messaging/formatting-message-text). If you're using a Slack app, you can also use this method to attach [message buttons](/legacy/legacy-messaging/legacy-message-buttons).

For best results, limit the number of characters in the `text` field to a few thousand bytes at most. Ideally, messages should be short and human-readable, if you need to post longer messages, please consider [uploading a snippet instead](/reference/methods/files.upload). (A single message should be no larger than 4,000 bytes.)

Consider reviewing our [message guidelines](/surfaces/app-design#messaging), especially if you're using attachments or message buttons.

### Authorship {#authorship}

How message authorship is attributed varies by a few factors, with some behaviors varying depending on the kinds of tokens you're using to post a message.

### Legacy concerns {#legacy}

Information in the section below applies only to classic apps.

#### Legacy authorship {#legacy_authorship}

Classic apps using the umbrella `bot` scope can't request additional scopes to adjust message authorship.

For classic apps, the best way to control the authorship of a message is to be explicit with the `as_user` parameter.

If you don't use the `as_user` parameter, `chat.postEphemeral` will guess the most appropriate `as_user` interpretation based on the kind of token you're using.

If `as_user` is not provided at all, then the value is inferred, based on the scopes granted to the caller: If the caller _could_ post with `as_user` passed as `false`, then that is how the method behaves; otherwise, the method behaves as if `as_user` were passed as `true`.

#### When as_user is false {#when-as_user-is-false}

When the `as_user` parameter is set to `false`, messages are posted as "[`bot_messages`](/reference/events/message/bot_message)", with message authorship attributed to the user name and icons associated with theSlack app.

#### When as_user is true {#when-as_user-is-true}

Set `as_user` to `true` and the authenticated user will appear as the author of the message. Posting as the authenticated user **requires** the `client` or the more preferred `chat:write:user` [scopes](/reference/scopes).

### Target channels and users {#target-channels-and-users}

You **must** specify a conversation container (public channel, private channel, or an IM channel) by providing its ID to the `channel` argument. You also must specify a target `user`.

Each type of channel behaves slightly differently based on the authenticated user's permissions and additional arguments. If the target `user` is not in the given channel, the ephemeral message will not be delivered, and we'll return a `user_not_in_channel` error.

Workspace apps will receive a `no_permission` error when they are not a member of the specified `channel`.

Note that the `user` parameter expects a user's `id`, and not a username or display name.

##### Post to a public channel {#post-to-a-public-channel}

You can either pass the channel's name (`#general`) or encoded ID (`C024BE91L`), and the message will be posted to that channel. The channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.

##### Post to a private group {#post-to-a-private-group}

As long as the authenticated user is a member of the private group, you can either pass the group's name (`secret-group`) or encoded ID (`G012AC86C`), and the message will be posted to that group. The private group's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.

##### Post to an IM channel {#post-to-an-im-channel}

Posting to an IM channel is a little more complex depending on the value of `as_user`.

*   If `as_user` is false:
    *   Pass a username (`@chris`) as the value of `channel` to post to that user's @slackbot channel _as the bot_.
    *   Pass the IM channel's ID (`D023BB3L2`) as the value of `channel` to post to that IM channel _as the bot_. The IM channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.
*   If `as_user` is true:
    *   Pass the IM channel's ID (`D023BB3L2`) as the value of `channel` to post to that IM channel _as the authenticated user_. The IM channel's ID can be retrieved through the [conversations.list](/reference/methods/conversations.list) API method.

To send a direct message to the user _owning_ the token used in the request, provide the `channel` field with the a conversation/IM ID value found in a method like [`conversations.list`](/reference/methods/conversations.list).

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "message_ts": "1502210682.580145"}
```

#### Typical error response

```
{  "ok": false,  "error": "user_not_in_channel"}
```

The `message_ts` included with the response _cannot_ be used with [`chat.update`](/reference/methods/chat.update), as it does not represent an actual message written to the database like it does with other api methods.

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

`cannot_reply_to_message`

This message type cannot have thread replies.

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

`invalid_attachments`

Attachments that contain blocks are not valid

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

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`is_archived`

Channel has been archived.

`markdown_text_conflict`

Markdown text cannot be used in conjunction with `blocks` or `text` argument.

`message_limit_exceeded`

Members on this team are sending too many messages. For more details, see https://slack.com/help/articles/115002422943-Usage-limits-for-free-workspaces

`messages_tab_disabled`

Messages tab for the app is disabled.

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

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

A workspace preference prevents the authenticated user from posting.

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

`too_many_attachments`

Too many attachments were provided with this message. A maximum of 100 attachments are allowed on a message.

`two_factor_setup_required`

Two factor setup is required.

`user_not_in_channel`

Intended recipient is not in the specified channel.