Source: https://docs.slack.dev/reference/methods/files.completeUploadExternal

# files.completeUploadExternal method

DocsCall generator

## Facts {#facts}

**Description**Finishes an upload started with files.getUploadURLExternal

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/files.completeUploadExternal
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.files.completeUploadExternal
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.files_completeUploadExternal
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().filesCompleteUploadExternal
```

**Scopes**

Bot token:

[`files:write`](/reference/scopes/files.write)

User token:

[`files:write`](/reference/scopes/files.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 4: 100+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`files`**`array`Required

Array of file ids and their corresponding (optional) titles.

_Example:_ `[{"id":"F044GKUHN9Z", "title":"slack-test"}]`

### Optional arguments

**`channel_id`**Optional

Channel ID where the file will be shared. If not specified the file will be private.

_Example:_ `C0NF841BK`

**`thread_ts`**`string`Optional

Provide another message's `ts` value to upload this file as a reply. Never use a reply's `ts` value; use its parent instead. Also make sure to provide only one channel when using 'thread\_ts'

_Example:_ `1524523204.000192`

**`channels`**`string`Optional

Comma-separated string of channel IDs or user IDs where the file will be shared.

_Example:_ `C0NF841BK,C2AW648GH`

**`initial_comment`**`string`Optional

The message text introducing the file in specified channels.

**`blocks`**`string`Optional

A JSON-based array of structured rich text blocks, presented as a URL-encoded string. If the `initial_comment` field is provided, the `blocks` field is ignored

_Example:_ `[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]`

## Usage info {#usage-info}

This method finalizes a file upload started with [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal).

After uploading the file to the URL obtained from [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal), call this endpoint to share the uploaded file in Slack. In most cases, callers will supply a channel where the file will be shared. If the `channel_id` is not specified, the file will remain private.

If this method is not called, the uploaded file and associated metadata will be discarded.

This method can only be called once.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "files": [    {      "id": "F123ABC456",      "title": "slack-test"    }  ]}
```

#### Typical error response for an invalid token

```
{  "ok": false,  "error": "invalid_auth"}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

User is not the owner of the file.

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_not_found`

Value passed for `channel_id` was invalid.

`channels_limit_exceeded`

Exceeded the channel limit. A maximum of 100 channels is allowed per request.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_not_found`

Could not find the file from the upload ticket.

`file_update_failed`

Failure occurred when attempting to update the file.

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

Provided blocks are in the incorrect format.

`invalid_channel`

Channel could not be found or channel specified is invalid.

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

No authentication token provided.

`not_in_channel`

User/bot membership is required for the specified channel.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`posting_to_channel_denied`

User is not authorized to post to channel.

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