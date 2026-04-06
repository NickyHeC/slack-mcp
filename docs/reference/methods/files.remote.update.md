Source: https://docs.slack.dev/reference/methods/files.remote.update

# files.remote.update method

DocsCall generator

## Facts {#facts}

**Description**Updates an existing remote file.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/files.remote.update
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.files.remote.update
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.files_remote_update
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().filesRemoteUpdate
```

**Scopes**

Bot token:

[`remote_files:write`](/reference/scopes/remote_files.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`external_id`**`string`Optional

Creator defined GUID for the file.

_Example:_ `123456`

**`external_url`**`string`Optional

URL of the remote file.

_Example:_ `http://example.com/my_cloud_service_file/abc123`

**`file`**`string`Optional

Specify a file by providing its ID.

_Example:_ `F2147483862`

**`filetype`**`string`Optional

type of file

_Example:_ `doc`

**`indexable_file_contents`**Optional

File containing contents that can be used to improve searchability for the remote file.

_Example:_ `...`

**`preview_image`**Optional

Preview of the document via `multipart/form-data`.

_Example:_ `...`

**`title`**`string`Optional

Title of the file being shared.

_Example:_ `Danger, High Voltage!`

## Usage info {#usage-info}

This method updates a remote file.

You cannot update the `external_id` or `file_id` of a remote file. If you need to update those fields, you'll need to [remove](/reference/methods/files.remote.remove) the file and then [add](/reference/methods/files.remote.add) it back.

* * *

## Response {#response}

```
{"url": "","description": "Typical success response","example": {    "ok": true,    "file": {        "id": "F08EAQ813FW",        "created": 1740066121,        "timestamp": 1740066121,        "name": "Test",        "title": "Test",        "mimetype": "application/msword",        "filetype": "doc",        "pretty_type": "Word Document",        "user": "U123A4BCDE5",        "user_team": "T123A4BC5DE",        "editable": false,        "size": 0,        "mode": "external",        "is_external": true,        "external_type": "app",        "is_public": true,        "public_url_shared": false,        "display_as_bot": false,        "username": "",        "url_private": "https://docs.google.com/document/d/1e8LtkvCSe_NH0UU0RyLgssmUQLT8G_3RMCGzyPWcx58/edit?tab=t.0",        "media_display_type": "unknown",        "permalink": "https://thetestenv.slack.com/files/U123A4BCDE5/F08EAQ813FW/test",        "comments_count": 0,        "is_starred": false,        "shares": {            "public": {                "C03QJUTKS4C": [                    {                        "reply_users": [],                        "reply_users_count": 0,                        "reply_count": 0,                        "ts": "1740066131.886799",                        "channel_name": "the-test-channel",                        "team_id": "T123A4BC5DE",                        "share_user_id": "U123A4BCDE5",                        "source": "UNKNOWN"                    }                ],                "C04567YFDK6": [                    {                        "reply_users": [],                        "reply_users_count": 0,                        "reply_count": 0,                        "ts": "1740066131.650279",                        "channel_name": "dev-test",                        "team_id": "T123A4BC5DE",                        "share_user_id": "U123A4BCDE5",                        "source": "UNKNOWN"                    }                ]            }        },        "channels": ["C12ABCDEF3G", "C12345ABCD6"],        "groups": [],        "ims": [],        "has_more_shares": false,        "external_id": "1234",        "external_url": "https://docs.google.com/document/d/1e8LtkvCSe_NH0UU0RyLgssmUQLT8G_3RMCGzyPWcx58/edit?tab=t.0",        "has_rich_preview": false,        "file_access": "visible"    }}
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

`bad_image`

The uploaded image could not be processed - try passing a JPG or PNG

`bot_user_required`

bot user token is required

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`failed_to_unshare`

The file was either not found or it has been unshared already.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_not_found`

Could not find the file to update.

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

`invalid_title`

invalid title provided

`invalid_type`

invalid type provided

`invalid_url`

invalid url provided

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

`too_large`

The uploaded image had excessive dimensions

`two_factor_setup_required`

Two factor setup is required.