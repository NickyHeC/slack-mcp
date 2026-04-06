Source: https://docs.slack.dev/reference/methods/files.getUploadURLExternal

# files.getUploadURLExternal method

DocsCall generator

## Facts {#facts}

**Description**Gets a URL for an edge external file upload

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/files.getUploadURLExternal
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.files.getUploadURLExternal
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.files_getUploadURLExternal
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().filesGetUploadURLExternal
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

**`length`**`integer`Required

Size in bytes of the file being uploaded.

_Example:_ `53072`

**`filename`**`string`Required

Name of the file being uploaded.

_Example:_ `laughingoutloudcat.jpg`

### Optional arguments

**`snippet_type`**`string`Optional

Syntax type of the snippet being uploaded.

_Example:_ `python`

**`alt_txt`**`string`Optional

Description of image for screen-reader.

_Example:_ `Aerial view of the Bixby Bridge and coastline of the Big Sur area in California`

## Usage info {#usage-info}

This method gets a URL that can be used for uploading a file to share within channels. The URL allows clients to send file data to Slack's file upload service.

The workflow is as follows:

1.  Call `files.getUploadURLExternal`, which returns an upload URL and a file ID.
2.  Upload a file by making a POST request to the upload URL. Include the filename (e.g., `-F filename="@text.txt"`). Files are processed asynchronously via a job handler.
    *   Files can be sent as raw bytes or can be multipart form encoded. Slack will return HTTP 200 if the upload is successful; a non-200 response indicates a failure.
3.  Call [`files.completeUploadExternal`](/reference/methods/files.completeUploadExternal) to finalize the upload.
    *   There is no need to wait for files to be processed by the job handler; the `files.completeUploadExternal` method will return with no action until both processes have completed. If `files.completeUploadExternal` is not called, the upload will be aborted and clients will receive an error.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "upload_url": "https://files.slack.com/upload/v1/ABC123...",  "file_id": "F123ABC456"}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
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

`alt_txt_too_large`

Description for the image is longer than the limit of 1000 character

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_upload_size_restricted`

The size of provided file is too large, as the team has restricted uploads of large files.

`file_uploads_disabled`

Team has disabled all file uploads.

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

`method_deprecated`

The method has been deprecated.

`missing_argument`

A required argument was not provided. Typically only occurs when the `length` provided is 0.

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

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`snippet_too_large`

The provided `length` is too large to create a snippet, which are limited to 1MB.

`storage_limit_reached`

File storage limit has been reached. This occurs when free teams have uploaded 5GB of files.

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

`unknown_snippet_type`

The provided `snippet_type` is not a supported type.

`unknown_subtype`

The provided `subtype` is not a supported type.