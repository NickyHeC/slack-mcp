Source: https://docs.slack.dev/reference/methods/admin.analytics.messages.metadata

# admin.analytics.messages.metadata method

DocsCall generator

## Facts {#facts}

**Description**Retrieves metadata for a list of messages from a given channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
GET https://slack.com/api/admin.analytics.messages.metadata
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.analytics.messages.metadata
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_analytics_messages_metadata
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminAnalyticsMessagesMetadata
```

**Scopes**

User token:

[`admin.analytics:read`](/reference/scopes/admin.analytics.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[1200 requests per minute with a burst allowance of 2000.](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

Channel ID for channel containing the messages to query.

### Optional arguments

**`oldest_ts`**`string`Optional

Oldest timestamp to include in the results

**`latest_ts`**`string`Optional

Most recent timestamp to include in the results. If not passed, defaults to current time.

**`cursor`**`string`Optional

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](#pagination) for more details.

_Example:_ `abcd...`

## Usage info {#usage-info}

This Web API method allows org owners and admins to retrieve message metadata from channels within their organization. It returns structural information about messages without the actual message content, including character counts, reactions, file attachments, and threading information.

### Pagination {#pagination}

Results are paginated. When more results exist, the response includes a `response_metadata.next_cursor` field. Pass this value as the `cursor` parameter in subsequent requests to fetch the next page.

```
cursor = Noneall_messages = []while True:    response = client.admin_analytics_messages_metadata(        channel="C0123456789",        limit=1000,        cursor=cursor    )    all_messages.extend(response["messages"])        cursor = response.get("response_metadata", {}).get("next_cursor")    if not cursor:        break
```

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "messages": [    {      "type": "message",      "ts": "1234567890.123456",      "user_id": "U123ABC456",      "text_character_count": 42,      "subtype": "bot_message",      "thread_ts": "1234567890.123456",      "reactions": [        {          "name": "thumbsup",          "count": 5        }      ],      "files": [        {          "id": "F123ABC456",          "created": 1234567890,          "timestamp": 1234567890,          "mimetype": "image/png",          "filetype": "png",          "pretty_type": "PNG"        }      ]    }  ],  "response_metadata": {    "next_cursor": "abcd..."  }}
```

### Message object fields {#message-object-fields}

Field

Type

Description

Required

`type`

`string`

Message type

Required

`ts`

`string`

Timestamp of the message

Required

`user_id`

`string`

Encoded ID of user who authored the message

Optional

`subtype`

`string`

Message subtype (e.g., `bot_message`, `channel_join`)

Optional

`thread_ts`

`string`

Timestamp of the root message if this is a threaded reply

Optional

`display_as_bot`

`boolean`

Whether the message displays as a bot

Optional

`client_msg_id`

`string`

Client-generated message ID

Optional

`text_character_count`

`integer`

Number of characters in the message text

Optional

`reactions`

`array`

Array of reaction counts

Optional

`files`

`array`

Array of file metadata

Optional

### Reaction object fields {#reaction-object-fields}

Field

Type

Description

Required

`name`

`string`

Name of the reaction emoji

Required

`count`

`integer`

Number of times this reaction was used

Required

### File object fields {#file-object-fields}

Field

Type

Description

Required

`id`

`string`

Encoded file ID

Required

`created`

`integer`

Unix timestamp when file was created

Required

`timestamp`

`integer`

Unix timestamp of the file

Required

`mimetype`

`string`

MIME type of the file

Optional

`filetype`

`string`

File type extension

Optional

`subtype`

`string`

File subtype

Optional

`pretty_type`

`string`

Human-readable file type

Optional

`is_external`

`boolean`

Whether the file is external

Optional

`external_type`

`string`

Type of external file

Optional

`is_public`

`boolean`

Whether the file is public

Optional

`public_url_shared`

`boolean`

Whether the public URL is shared

Optional

`display_as_bot`

`boolean`

Whether to display as bot

Optional

`duration_ms`

`integer`

Duration in milliseconds for media files

Optional

`media_display_type`

`string`

Display type for media files

Optional

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

`admin_analytics_disabled`

We're having issues returning your analytics. Please wait and try again.

`analytics_unavailable`

We were unable to find analytics for you.

`channel_not_found`

The specified channel was not found

`deprecated_endpoint`

The endpoint has been deprecated.

`different_team_owns_message_metadata_for_channel`

Message metadata must be accessed by an actor from the same team that owns the channel. This may be the org or a specific enterprise workspace.

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

Required arguments either were not provided or contain invalid values.

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

The user token does not belong to an enterprise.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_plan_level`

This feature is not available for your current product plan.

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