Source: https://docs.slack.dev/admins/admin-oversight-api

# Using the Admin Oversight API

Access Oversight API

An Organization Owner can contact our team at [exports@slack.com](mailto:exports@slack.com) to request access to the Oversight API.

The Admin Oversight API provides near real-time oversight information for customer administrators in an Enterprise org. This API introduces a new collection of API methods for accessing channel info, channel membership, and specific messages.

Org owners can install Admin Oversight API applications via the typical [OAuth process](/authentication/installing-with-oauth).

This API is not intended for bulk message collection. While you may collect messages with these API methods, they're rate-limited to 100 messages per hour, returning many fewer messages than the `conversations.history` and `conversations.replies` Web API methods (which allow 900 messages per hour with 60 calls at 15 messages per call) and equivalent Discovery API methods.

This API is designed to support the admin management use cases such as:

*   Automating channel management
*   Guest management
*   Reporting messages

* * *

## Scopes {#required-scopes}

The Admin Oversight API methods rely on combinations of the following scopes. Read a method's _Facts_ to determine which ones that method specifically requires.

*   [`admin.conversations:read`](/reference/scopes/admin.conversations.read)
*   [`admin.users:read`](/reference/scopes/admin.users.read)
*   [`admin.teams:read`](/reference/scopes/admin.teams.read)
*   [`admin.chat:read`](/reference/scopes/admin.chat.read)
*   [`admin.chat:write`](/reference/scopes/admin.chat.write)

## Methods {#methods}

### Enterprise and users {#users}

Use these methods to gather basic information about the Enterprise organization and its members.

Method

Description

[`oversight.enterprise.info`](#enterprise_info)

Returns basic information about an Enterprise org

[`oversight.user.conversations`](#user_conversations)

Returns list IDs for all conversations a user is in

[`oversight.user.info`](#user_info)

Returns information on a single user

[`oversight.users.list`](#users_list)

Returns list of all users

### Conversations (channels, groups, and DMs) {#conversations}

Use these methods to gather information about and message data from public channels (`channels`), private channels (`channels?private=true`), multiparty DMs (`groups`), and direct messages (`dms`).

Method

Description

[`oversight.conversations.info`](#conversations_info)

Returns overview of a single channel

[`oversight.conversations.list`](#conversations_list)

Returns a list of all conversations

[`oversight.conversations.members`](#conversations_members)

Returns list of everyone in a conversation

### Individual messages {#ims}

Use this method to collect a complete history for a single message.

Method

Description

[`oversight.chat.info`](#chat_info)

Returns a single message

### Tombstone and Deleting Messages {#messages}

Method

Description

[`oversight.chat.delete`](#chat_delete)

Deletes a message

[`oversight.chat.tombstone`](#chat_tombstone)

Tombstones a message

[`oversight.chat.restore`](#chat_restore)

Restores a message

[`oversight.chat.update`](#chat_update)

Updates a message

* * *

## oversight.enterprise.info {#enterprise_info}

This method returns basic information about the Enterprise organization where the app is installed, including all workspaces (`teams`).

The `teams` array is paged at 1000 items by default, but this can also be shortened with the `limit` parameter.

DocsCall generator

## Facts {#facts}

**Description**Returns basic information about the Enterprise organization where the app is installed, including all workspaces (teams).

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.enterprise.info
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.enterprise.info
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_enterprise_info
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightEnterpriseInfo
```

**Scopes**

User token:

[`admin.teams:read`](/reference/scopes/admin.teams.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`cursor`**`string`Optional

Paginate through collections of data by setting the cursor parameter to a next\_cursor attribute returned by a previous request

_Example:_ `dXNlcjpVMDYxTkZUVDI=`

**`limit`**`integer`Optional

The maximum number of items to return

_Example:_ `20`

### Example request {#oversight-enterprise-info-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "limit": 1,  "cursor": "cGFnZToz"}
```

### Example response {#oversight-enterprise-info-example-response}

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

`invalid_cursor`

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`not_an_enterprise`

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

* * *

## oversight.users.list {#users_list}

This method returns a list of all users.

Very similar to the original `users.list` API method. Includes an array of workspace IDs that the user belongs to in an Enterprise organization (`teams`).

DocsCall generator

## Facts {#facts-1}

**Description**Returns a list of all users in an Enterprise organization

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.users.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.users.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_users_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightUsersList
```

**Scopes**

User token:

[`admin.users:read`](/reference/scopes/admin.users.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-1}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`include_deleted`**`boolean`Optional

Include deleted users in the list

_Example:_

**`limit`**`integer`Optional

Limit the number of users returned (less than 1000)

_Example:_ `100`

**`cursor`**`string`Optional

Offset to fetch the next page of records

_Example:_ `W0123ABC456`

### Example request {#oversight-users-list-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "include_deleted": true,  "offset": "W0123ABC456"}
```

### Example response {#oversight-users-list-example-response}

## Errors {#errors-1}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_not_found`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.user.info {#user_info}

This method returns information on a single user in an Enterprise org.

DocsCall generator

## Facts {#facts-2}

**Description**Returns information on a single user in an Enterprise organization

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.user.info
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.user.info
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_user_info
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightUserInfo
```

**Scopes**

User token:

[`admin.users:read`](/reference/scopes/admin.users.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-2}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`user`**`string`Optional

ID of user to get information about

_Example:_ `W0123ABC456`

**`email`**`string`Optional

Email address of the user to get information about

_Example:_ `name@domain.com`

### Users {#users}

The response will include an array of workspace IDs that the user belongs to in an Enterprise organization (`teams`). You may search by either user ID (`user`) or email address (`email`), but you must include one of those.

### Example request {#oversight-user-info-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "user": "W0123ABC456",  "email": "name@domain.com"}
```

### Example response {#oversight-user-info-example-response}

## Errors {#errors-2}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

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

`invalid_args`

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_email`

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_channel`

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`missing_team`

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

`unknown_method`

`user_not_found`

* * *

## oversight.user.conversations {#user_conversations}

This method lists IDs for all conversations (channels and DMs, including public, private, organization-wide, and shared) a user is in, based upon the scopes that your app currently has.

With the optional `include_historical` argument, it will also return any conversation this user was in at some point and left.

Slack only stores and returns the most recent date and time that the user joined or left a conversation.

This method can also be filtered by conversation type: public, private, DM, MPDM. These filters are exclusive and can only be used one at a time.

Since channels like DMs and MPDMs are org-shared channels and are accessible globally within an Enterprise org, the `team_id` field will return the ID associated with the Enterprise ID instead of an individual team.

DocsCall generator

## Facts {#facts-3}

**Description**Lists IDs for all conversations a user is in, based on the app's current scopes

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.user.conversations
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.user.conversations
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_user_conversations
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightUserConversations
```

**Scopes**

User token:

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-3}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`user`**`string`Required

Encoded user ID for the user whose channels you want to retrieve

_Example:_ `W0MLS084A`

### Optional arguments

**`include_historical`**`boolean`Optional

Include conversations the user was in at some point and left

**`limit`**`integer`Optional

Limit the number of channels returned (less than 1000)

_Example:_ `500`

**`only_im`**`boolean`Optional

Return only direct messages

**`only_mpim`**`boolean`Optional

Return only multi-party direct messages

**`only_private`**`boolean`Optional

Return only private channels

**`only_public`**`boolean`Optional

Return only public channels

### Example default request {#example-default-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "user": "W0123ABC456"}
```

### Example default response {#example-default-response}

## Errors {#errors-3}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

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

`invalid_args`

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`unknown_method`

`user_not_found`

* * *

## oversight.conversations.list {#conversations_list}

This method provides a paginated list of all conversations, depending on the token scopes, and the team ID. The endpoint provides a truncated version of the channel metadata.

### DMs and MPDMs {#dms-and-mpdms}

Because both direct messages and multi-party direct messages are automatically organization-wide in an Enterprise org, they will only be returned when an Enterprise ID is passed as the `team` parameter, or is omitted entirely.

### Channels {#channels}

Org-shared and multi-workspace channels will also only be returned when the Enterprise ID is passed as the `team` parameter, or is omitted entirely. Channels that belong to a single workspace will only be returned when that workspace ID is passed into the `team` parameter.

### Conversation names {#conversation-names}

Channel names are included in this method to make it easier to build a browsable list of conversations. Depending on the conversation type, you can expect a different name format. The `name` field will return the channel name for channels, the channel ID for DMs, and a string of participants prefixed by `mpdm` for MPDMs. Please see the Example response for more information.

DocsCall generator

## Facts {#facts-4}

**Description**Provides a paginated list of all conversations, depending on the token scopes and team ID

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.conversations.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.conversations.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_conversations_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightConversationsList
```

**Scopes**

User token:

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-4}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`limit`**`integer`Optional

Limit the number of conversations returned (less than 1000)

_Example:_ `500`

**`cursor`**`string`Optional

Paginate through collections of data

_Example:_ `dXNlcjpVMDYxTkZUVDI=`

**`only_ext_shared`**`boolean`Optional

Return only externally-shared channels

**`only_im`**`boolean`Optional

Return only direct messages

**`only_mpim`**`boolean`Optional

Return only multi-party direct messages

**`only_private`**`boolean`Optional

Return only private channels

**`only_public`**`boolean`Optional

Return only public channels

**`team`**`string`Optional

Team or Enterprise ID to filter conversations

_Example:_ `T0123ABC456`

### Example request {#oversight-conversations-list-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "team": "T0123ABC456",  "offset": "G0QPJB83S"}
```

### Example response {#oversight-conversations-list-example-response}

## Errors {#errors-4}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

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

`invalid_args`

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.conversations.info {#conversations_info}

This method provides a comprehensive overview of a single channel's metadata.

The response includes details about channel retention. The `retention` object includes the `type` and `duration`. Retention type is either `custom` or `default`. Retention `duration` is the period of time content is retained in a channel in days.

Deleted channels take about 24 hours to be expunged from our databases. If a channel is deleted but has not yet been pruned, the `is_deleted` field will return `true`. When the channel has been fully removed from the databases, you should expect to see a `channel_not_found` error.

DocsCall generator

## Facts {#facts-5}

**Description**Provides a comprehensive overview of a single channel's metadata

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.conversations.info
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.conversations.info
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_conversations_info
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightConversationsInfo
```

**Scopes**

User token:

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-5}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The channel to retrieve

_Example:_ `G0123ABC456`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T0123ABC456`

### Example request {#oversight-conversations-info-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "channel": "G0123ABC456",  "team": "T0123ABC456"}
```

### Example response {#oversight-conversations-info-example-response}

## Errors {#errors-5}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_not_found`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.conversations.members {#conversations_members}

This method provides a list of everyone in a given channel, private channel, MDPM, or DM.

Like our other `.list` API methods, its payload is purposely small so that the list itself can be pulled quickly, which is especially important on very large orgs with multiple default channels.

If you want to include members that have left the channel, set the `include_member_left` argument to `true`. Otherwise, only members currently in the conversation are returned in the response (for these users, the `date_left` property is set to `0`). Slack does not store every instance of a user joining or leaving a channel, so those records will only reflect the most recent activity. If someone leaves a channel and then rejoins, we update the `date_joined` field and set the `date_left` field back to `0`.

DocsCall generator

## Facts {#facts-6}

**Description**Provides a list of everyone in a given channel, private channel, MPDM, or DM

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.conversations.members
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.conversations.members
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_conversations_members
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightConversationsMembers
```

**Scopes**

User token:

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-6}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The channel or DM to get membership for

_Example:_ `C123ABC456`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T123ABC456`

**`include_member_left`**`boolean`Optional

Include members that have left the channel

**`limit`**`integer`Optional

Limit the number of members returned

_Example:_ `1000`

**`cursor`**`string`Optional

Paginate through collections of data

_Example:_ `dXNlcjpVMDYxTkZUVDI=`

### Example request {#oversight-conversations-members-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "channel": "G0123ABC456",  "team": "T0123ABC456",  "limit": 4,  "offset": "W123ABC456",  "include_member_left": true}
```

### Example response {#oversight-conversations-members-example-response}

## Errors {#errors-6}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_not_found`

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

`invalid_args`

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

`user_not_found`

* * *

## oversight.chat.info {#chat_info}

This method returns a single message. This endpoint will be limited to 100 requests per hour.

If the message has been edited (or deleted), this method returns the current edited (or deleted) message. If an Enterprise org customer has their retention set to keep edits and deletes, it will also return all of those edits or the deletion. See below for examples.

DocsCall generator

## Facts {#facts-7}

**Description**Returns a single message, including edit and deletion history

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.chat.info
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.chat.info
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_chat_info
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightChatInfo
```

**Scopes**

User token:

[`admin.chat:read`](/reference/scopes/admin.chat.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Limited to 100 requests per hour](/apis/web-api/rate-limits)

## Arguments {#arguments-7}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The ID of the channel or DM where the message was posted

_Example:_ `C0123ABC456`

**`ts`**`string`Required

The entire timestamp of the message

_Example:_ `1569520591.000500`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T123ABC456`

### Example request {#oversight-chat-info-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "ts": "1569520591.000500",  "channel": "C0123ABC456",  "team": "T123ABC456"}
```

### Example responses {#example-responses}

#### Unedited message {#unedited-message}

If a message has not been edited, the `"edits"` array will exist, but it will be empty.

```
{    "ok": true,    "message": {        "client_msg_id": "6b6239f9-9a22-4759-ac01-7e9c48658092",        "type": "message",        "text": "Can we reschedule today's meeting?",        "user": "W123ABC456",        "ts": "1569520591.000500",        "team": "T123ABC456"    },    "edits": []}
```

#### Edited message {#edited-message}

For an edited message, the root `message` object is identical to the one in the relevant `.history` call: The `text` field shows the current message content as seen in the client, and the `edited` object shows who made the most recent edit and when they made it.

The `edits` array will list each edit as a separate object in ascending order. Each object will contain a `text` field that shows the message content after the edit was made, as well as a `previous` object that shows what the message content was immediately prior to this edit.

**Original message with a single edit**

```
{    "ok": true,    "message": {        "client_msg_id": "6b6239f9-9a22-4759-ac01-7e9c48658092",        "type": "message",        "text": "Can we reschedule today's meeting? I have a conflict.",        "user": "W123ABC456",        "ts": "1569520591.000500",        "team": "T123ABC456",        "edited": {            "user": "W123ABC456",            "ts": "1569521123.000000"        }    },    "edits": [        {            "type": "message",            "user": "W123ABC456",            "upload": false,            "ts": "1569521123.000000",            "text": "Can we reschedule today's meeting? I have a conflict.",            "previous": {                "text": "Can we reschedule today's meeting?"            },            "original_ts": "1569520591.000500",            "subtype": "message_changed",            "editor_id": "W123ABC456"        }    ]}
```

**Same message edited a second time**

```
{    "ok": true,    "message": {        "client_msg_id": "6b6239f9-9a22-4759-ac01-7e9c48658092",        "type": "message",        "text": "Never mind, I was able to move my other meeting. See you soon.",        "user": "W123ABC456",        "ts": "1569520591.000500",        "team": "T123ABC456",        "edited": {            "user": "W123ABC456",            "ts": "1569521616.000000"        }    },    "edits": [        {            "type": "message",            "user": "W123ABC456",            "upload": false,            "ts": "1569521123.000000",            "text": "Can we reschedule today's meeting? I have a conflict.",            "previous": {                "text": "Can we reschedule today's meeting?"            },            "original_ts": "1569520591.000500",            "subtype": "message_changed",            "editor_id": "W123ABC456"        },        {            "type": "message",            "user": "W123ABC456",            "upload": false,            "ts": "1569521616.000000",            "text": "Never mind, I was able to move my other meeting. See you soon.",            "previous": {                "text": "Can we reschedule today's meeting? I have a conflict."            },            "original_ts": "1569520591.000500",            "subtype": "message_changed",            "editor_id": "W123ABC456"        }    ]}
```

#### Deleted message {#deleted-message}

When a message has been deleted, the root `message` object will only show `"type": "deleted"`, not any version of the message content. The message content at the time of deletion can be found in the `edits` array in a message object with a subtype of `message_deleted`. It will be the last item in the list. If you would like to see the original message content as it was first posted, it can be found in the `previous` object of the message's earliest edit.

```
{    "ok": true,    "message": {        "type": "deleted"    },    "edits": [        {            "type": "message",            "user": "W123ABC456",            "upload": false,            "ts": "1569521123.000000",            "text": "Can we reschedule today's meeting? I have a conflict.",            "previous": {                "text": "Can we reschedule today's meeting?"            },            "original_ts": "1569520591.000500",            "subtype": "message_changed",            "editor_id": "W123ABC456"        },        {            "type": "message",            "user": "W123ABC456",            "upload": false,            "ts": "1569521616.000000",            "text": "Never mind, I was able to move my other meeting. See you soon.",            "previous": {                "text": "Can we reschedule today's meeting? I have a conflict."            },            "original_ts": "1569520591.000500",            "subtype": "message_changed",            "editor_id": "W123ABC456"        },        {            "type": "message",            "user": "W123ABC456",            "upload": false,            "ts": "1569521860.000000",            "text": "",            "previous": {                "text": "Never mind, I was able to move my other meeting. See you soon."            },            "original_ts": "1569520591.000500",            "subtype": "message_deleted",            "editor_id": "W123ABC456"        }    ]}
```

## Errors {#errors-7}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_not_found`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`message_not_found`

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.chat.delete {#chat_delete}

This method deletes a single message.

DocsCall generator

## Facts {#facts-8}

**Description**Deletes a single message

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.chat.delete
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.chat.delete
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_chat_delete
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightChatDelete
```

**Scopes**

User token:

[`admin.chat:write`](/reference/scopes/admin.chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-8}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The ID of the channel or DM where the message was posted

_Example:_ `C0123ABC456`

**`ts`**`string`Required

The entire timestamp of the message

_Example:_ `1569520591.000500`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T123ABC456`

### Example request {#oversight-chat-delete-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "ts": "1569520591.000500",  "channel": "C0123ABC456",  "team": "T123ABC456"}
```

### Example response {#oversight-chat-delete-example-response}

## Errors {#errors-8}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_update_not_allowed`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`message_not_found`

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.chat.tombstone {#chat_tombstone}

This method tombstones a single message, removing the message content but preserving the message's existence. The tombstone message can be customized with the `content` argument.

DocsCall generator

## Facts {#facts-9}

**Description**Tombstones a single message, removing the message content but preserving the message's existence

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.chat.tombstone
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.chat.tombstone
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_chat_tombstone
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightChatTombstone
```

**Scopes**

User token:

[`export:read`](/reference/scopes/export.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-9}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The ID of the channel or DM where the message was posted

_Example:_ `C0123ABC456`

**`ts`**`string`Required

The entire timestamp of the message

_Example:_ `1569520591.000500`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T123ABC456`

**`content`**`string`Optional

Tombstone message surfaced in the UI to the end user

_Example:_ `This message is currently being reviewed by XYZ company`

### Example request {#oversight-chat-tombstone-example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "ts": "1569520591.000500",  "channel": "C0123ABC456",  "team": "T123ABC456",  "content": "This message is currently being reviewed by XYZ Company"}
```

### Example response {#oversight-chat-tombstone-example-response}

## Errors {#errors-9}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_update_not_allowed`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`message_not_found`

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.chat.restore {#chat_restore}

This method restores a tombstone message.

DocsCall generator

## Facts {#facts-10}

**Description**Restores a tombstoned message

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.chat.restore
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.chat.restore
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_chat_restore
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightChatRestore
```

**Scopes**

User token:

[`admin.chat:write`](/reference/scopes/admin.chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-10}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The ID of the channel or DM where the message was posted

_Example:_ `C0123ABC456`

**`ts`**`string`Required

The entire timestamp of the message

_Example:_ `1569520591.000500`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T123ABC456`

### Example request {#oversight-chat-restore-example-request}

```
{  "ts": "1569520591.000500",  "channel": "C0123ABC456",  "team": "T123ABC456",}
```

### Example response {#oversight-chat-restore-example-response}

## Errors {#errors-10}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_update_not_allowed`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`message_not_found`

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`non_tombstoned_message_not_allowed`

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *

## oversight.chat.update {#chat_update}

This method allows a message to be updated. This method specifies text or attachments that should be included in place of the message. Parse mode: full. Use this method for quarantine and restoration. Present your key/value pairs according to [RFC-3986](https://datatracker.ietf.org/doc/html/rfc3986).

DocsCall generator

## Facts {#facts-11}

**Description**Updates a message, used for quarantine and restoration with full parse mode

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oversight.chat.update
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oversight.chat.update
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oversight_chat_update
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oversightChatUpdate
```

**Scopes**

User token:

[`admin.chat:write`](/reference/scopes/admin.chat.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute. Contributes to org-wide rate limit of ~30 requests per second](/apis/web-api/rate-limits)

## Arguments {#arguments-11}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

The ID of the channel or DM where the message was posted

_Example:_ `C0123ABC456`

**`ts`**`string`Required

The entire timestamp of the message

_Example:_ `1569520591.000500`

**`text`**`string`Required

Replacement text for the message

_Example:_ `This message has been quarantined per DLP Policy 2.1.1`

### Optional arguments

**`team`**`string`Optional

Team or Enterprise ID for the channel

_Example:_ `T123ABC456`

### Example request {#oversight-chat-update-example-request}

```
{  "ts": "1569520591.000500",  "channel": "C0123ABC456",  "team": "T123ABC456",  "Text": "This message has been quarantined per DLP Policy 2.1.1"}
```

### Example response {#oversight-chat-update-example-response}

## Errors {#errors-11}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_update_not_allowed`

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

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`message_not_found`

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`non_tombstoned_message_not_allowed`

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

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

`team_not_found`

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

* * *