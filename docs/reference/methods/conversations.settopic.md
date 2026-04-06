Source: https://docs.slack.dev/reference/methods/conversations.setTopic

# conversations.setTopic method

DocsCall generator

## Facts {#facts}

**Description**Sets the topic for a conversation.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.setTopic
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.setTopic
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_setTopic
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsSetTopic
```

**Scopes**

Bot token:

[`channels:manage`](/reference/scopes/channels.manage)[`channels:write.topic`](/reference/scopes/channels.write.topic)[`groups:write`](/reference/scopes/groups.write)[`groups:write.topic`](/reference/scopes/groups.write.topic)[`im:write`](/reference/scopes/im.write)[`im:write.topic`](/reference/scopes/im.write.topic)[`mpim:write`](/reference/scopes/mpim.write)[`mpim:write.topic`](/reference/scopes/mpim.write.topic)

User token:

[`channels:write`](/reference/scopes/channels.write)[`channels:write.topic`](/reference/scopes/channels.write.topic)[`groups:write`](/reference/scopes/groups.write)[`groups:write.topic`](/reference/scopes/groups.write.topic)[`im:write`](/reference/scopes/im.write)[`im:write.topic`](/reference/scopes/im.write.topic)[`mpim:write`](/reference/scopes/mpim.write)[`mpim:write.topic`](/reference/scopes/mpim.write.topic)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

Conversation to set the topic of

**`topic`**`string`Required

The new topic string. Does not support formatting or linkification.

_Example:_ `Apply topically for best effects`

## Usage info {#usage-info}

This method is used to change the topic of a conversation. The calling user must be a member of the conversation. Not all conversation types support a new topic.

* * *

## Response {#response}

#### A conversation object is returned:

```
{  "ok": true,  "channel": {    "id": "C12345678",    "name": "tips-and-tricks",    "is_channel": true,    "is_group": false,    "is_im": false,    "is_mpim": false,    "is_private": false,    "created": 1649195947,    "is_archived": false,    "is_general": false,    "unlinked": 0,    "name_normalized": "tips-and-tricks",    "is_shared": false,    "is_frozen": false,    "is_org_shared": false,    "is_pending_ext_shared": false,    "pending_shared": [],    "parent_conversation": null,    "creator": "U12345678",    "is_ext_shared": false,    "shared_team_ids": [      "T12345678"    ],    "pending_connected_team_ids": [],    "is_member": true,    "last_read": "1649869848.627809",    "latest": {      "type": "message",      "subtype": "channel_topic",      "ts": "1649952691.429799",      "user": "U12345678",      "text": "set the channel topic: Apply topically for best effects",      "topic": "Apply topically for best effects"    },    "unread_count": 1,    "unread_count_display": 0,    "topic": {      "value": "Apply topically for best effects",      "creator": "U12345678",      "last_set": 1649952691    },    "purpose": {      "value": "",      "creator": "",      "last_set": 0    },    "previous_names": []  }}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_arguments",  "response_metadata": {    "messages": [      "[ERROR] missing required field: topic"    ]  }}
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

`is_archived`

Channel has been archived.

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

`not_in_channel`

Authenticated user is not in the channel.

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

`too_long`

Topic was longer than 250 characters.

`two_factor_setup_required`

Two factor setup is required.

`user_is_restricted`

Setting the topic is a restricted action.