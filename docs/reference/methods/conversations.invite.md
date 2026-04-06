Source: https://docs.slack.dev/reference/methods/conversations.invite

# conversations.invite method

DocsCall generator

## Facts {#facts}

**Description**Invites users to a channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.invite
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.invite
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_invite
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsInvite
```

**Scopes**

Bot token:

[`channels:manage`](/reference/scopes/channels.manage)[`channels:write.invites`](/reference/scopes/channels.write.invites)[`groups:write`](/reference/scopes/groups.write)[`groups:write.invites`](/reference/scopes/groups.write.invites)[`im:write`](/reference/scopes/im.write)[`mpim:write`](/reference/scopes/mpim.write)

User token:

[`channels:write`](/reference/scopes/channels.write)[`channels:write.invites`](/reference/scopes/channels.write.invites)[`groups:write`](/reference/scopes/groups.write)[`groups:write.invites`](/reference/scopes/groups.write.invites)[`im:write`](/reference/scopes/im.write)[`mpim:write`](/reference/scopes/mpim.write)

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

The ID of the public or private channel to invite user(s) to.

**`users`**`string`Required

A comma separated list of user IDs. Up to 100 users may be listed.

### Optional arguments

**`force`**`boolean`Optional

When set to `true` and multiple user IDs are provided, continue inviting the valid ones while disregarding invalid IDs. Defaults to `false`.

_Default:_ `false`

_Example:_ `true`

## Usage info {#usage-info}

This [Conversations API](/apis/web-api/using-the-conversations-api) method invites 1-1000 users to a public or private channel. The calling user must be a member of the channel.

### Partially failed calls {#partially-failed-calls}

Users who can be successfully invited and who were not members of the workspace previously will not be invited if _any_ of the user invites fail. Instead, an error response will be returned.

Inviting users who are in a "removed" state (that is, they were once a member of the workspace but have since been removed) will fail “silently”: an error response will be returned via the API, but all other users will be invited except for those in the "removed" state.

* * *

## Response {#response}

#### Typical success response when an invitation is extended

```
{  "ok": true,  "channel": {    "id": "C012AB3CD",    "name": "general",    "is_channel": true,    "is_group": false,    "is_im": false,    "created": 1449252889,    "creator": "W012A3BCD",    "is_archived": false,    "is_general": true,    "unlinked": 0,    "name_normalized": "general",    "is_read_only": false,    "is_shared": false,    "is_ext_shared": false,    "is_org_shared": false,    "pending_shared": [],    "is_pending_ext_shared": false,    "is_member": true,    "is_private": false,    "is_mpim": false,    "last_read": "1502126650.228446",    "topic": {      "value": "For public discussion of generalities",      "creator": "W012A3BCD",      "last_set": 1449709364    },    "purpose": {      "value": "This part of the workspace is for fun. Make fun here.",      "creator": "W012A3BCD",      "last_set": 1449709364    },    "previous_names": [      "specifics",      "abstractions",      "etc"    ]  }}
```

#### Error response when users cannot be invited for differing reasons: one for not being associated with a valid user ID, and one for being the user sending the invite.

```
{  "ok": false,  "error": "user_not_found",  "errors": [    {      "user": "U111111",      "ok": false,      "error": "user_not_found"    },    {      "user": "U222222",      "ok": false,      "error": "cant_invite_self"    }  ]}
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

`already_in_channel`

Invited user is already in the channel.

`cant_invite`

User cannot be invited to this channel.

`cant_invite_self`

Authenticated user cannot invite themselves to a channel.

`channel_not_found`

Value passed for `channel` was invalid.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_channel_migrating`

External channel migrating.

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

`invitee_cant_see_channel`

The Enterprise org multi-workspace channel you are inviting a user to is not shared with any workspaces the user is currently a member of.

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

`no_external_invite_permission`

User does not have permission to invite that external user to the channel

`no_permission`

User does not have permission to invite that specific user to the channel

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`no_user`

No value was passed for `users`.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`not_in_channel`

Authenticated user is not in the channel.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`org_user_not_in_team`

One or more members invited are part of the Enterprise organization but not the specific workspace you're interfacing with.

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

`ura_max_channels`

An invited user is a single-channel guest user ('ultra restricted access') that is already in the maximum number of conversations.

`user_is_restricted`

An invited user is a guest user that is restricted from accessing this conversation.

`user_not_found`

Value passed for `users` was invalid.