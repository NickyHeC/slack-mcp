Source: https://docs.slack.dev/reference/methods/conversations.rename

# conversations.rename method

DocsCall generator

## Facts {#facts}

**Description**Renames a conversation.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.rename
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.rename
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_rename
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsRename
```

**Scopes**

Bot token:

[`channels:manage`](/reference/scopes/channels.manage)[`channels:write`](/reference/scopes/channels.write)[`groups:write`](/reference/scopes/groups.write)[`im:write`](/reference/scopes/im.write)[`mpim:write`](/reference/scopes/mpim.write)

User token:

[`channels:write`](/reference/scopes/channels.write)[`groups:write`](/reference/scopes/groups.write)[`im:write`](/reference/scopes/im.write)[`mpim:write`](/reference/scopes/mpim.write)

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

ID of conversation to rename

**`name`**`string`Required

New name for conversation.

## Usage info {#usage-info}

This method renames a conversation. Some types of conversations cannot be renamed.

Only the user that originally created a channel, a Workspace Admin, or a user with the Channel Manager role may rename it. Others will receive a `not_authorized` error.

## Naming {#naming}

Conversation names can only contain lowercase letters, numbers, hyphens, and underscores, and must be 80 characters or less. We will validate the submitted channel name and modify it to meet the above criteria. When calling this method, we recommend storing the channel's `name` value that is returned in the response.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "channel": {    "id": "C012AB3CD",    "name": "general",    "is_channel": true,    "is_group": false,    "is_im": false,    "created": 1449252889,    "creator": "W012A3BCD",    "is_archived": false,    "is_general": true,    "unlinked": 0,    "name_normalized": "general",    "is_read_only": false,    "is_shared": false,    "is_ext_shared": false,    "is_org_shared": false,    "pending_shared": [],    "is_pending_ext_shared": false,    "is_member": true,    "is_private": false,    "is_mpim": false,    "last_read": "1502126650.228446",    "topic": {      "value": "For public discussion of generalities",      "creator": "W012A3BCD",      "last_set": 1449709364    },    "purpose": {      "value": "This part of the workspace is for fun. Make fun here.",      "creator": "W012A3BCD",      "last_set": 1449709364    },    "previous_names": [      "specifics",      "abstractions",      "etc"    ],    "num_members": 23,    "locale": "en-US"  }}
```

#### Typical error response when the calling user is not a member of the conversation

```
{  "ok": false,  "error": "not_in_channel"}
```

Returns a [channel object](/reference/objects/channel-object).

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

`invalid_name`

Value passed for `name` was invalid.

`invalid_name_maxlength`

Value passed for `name` exceeded max length.

`invalid_name_punctuation`

Value passed for `name` contained only punctuation.

`invalid_name_required`

Value passed for `name` was empty.

`invalid_name_specials`

Value passed for `name` contained unallowed special characters or upper case characters.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`is_archived`

Cannot rename archived channel.

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

`name_taken`

New channel name is taken.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`not_authorized`

Caller cannot rename this channel.

`not_in_channel`

Caller is not a member of the channel.

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