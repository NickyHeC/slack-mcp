Source: https://docs.slack.dev/reference/methods/files.remote.add

# files.remote.add method

DocsCall generator

## Facts {#facts}

**Description**Adds a file from a remote service

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/files.remote.add
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.files.remote.add
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.files_remote_add
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().filesRemoteAdd
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

**`external_id`**`string`Required

Creator defined GUID for the file.

_Example:_ `123456`

**`external_url`**`string`Required

URL of the remote file.

_Example:_ `http://example.com/my_cloud_service_file/abc123`

**`title`**`string`Required

Title of the file being shared.

_Example:_ `Danger, High Voltage!`

### Optional arguments

**`filetype`**`string`Optional

type of file

_Example:_ `doc`

**`indexable_file_contents`**Optional

A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.

_Example:_ `...`

**`preview_image`**Optional

Preview of the document via `multipart/form-data`.

_Example:_ `...`

## Usage info {#usage-info}

This method adds a remote file to Slack. Adding a file does not share it to a channel. To make your remote file visible, use the [`files.remote.share`](/reference/methods/files.remote.share) API method. This method performs an upsert: if you add a file that has been added previously, the existing file will be updated.

Remote files exist across the entire workspace (or organization, for Enterprise orgs). Because of that, remote files must be added by bots with the [`bot` scope](/reference/scopes/bot), not by an individual user. Dimension requirements for previews are a minimum of `800w x 400h`.

`preview_image` is displayed when your remote file is [shared](/reference/methods/files.remote.share). It's a binary image file.

`external_id` is the unique ID of the remote file, according to the external host of the file.

`indexable_file_contents` is a text file that represents the file for search. When a user searches in Slack, their query will be compared against the contents of this text file for matching. Think of this text file like the `alt` parameter on an HTML `<img>` tag: a textual representation of a non-textual object. The text file can contain a description of the remote file, or it can contain search keywords or anything else text-based.

One tricky bit: in the response, the file object may indicate that `"has_rich_preview"` is `false`, even if you include the `preview_image` parameter. That's because it takes a few seconds for Slack to parse the `preview_image` you pass. If you call `files.remote.add` with the same `external_id` later, you'll see `"has_preview_image": true`.

* * *

## Response {#response}

```
{    "ok": true,    "file": {        "id": "F08EAQ813FW",        "created": 1740062388,        "timestamp": 1740062388,        "name": "Test",        "title": "Test",        "mimetype": "application/vnd.slack-remote",        "filetype": "remote",        "pretty_type": "Remote",        "user": "U123A4BCDE5",        "user_team": "T123A4BC5DE",        "editable": false,        "size": 0,        "mode": "external",        "is_external": true,        "external_type": "app",        "is_public": false,        "public_url_shared": false,        "display_as_bot": false,        "username": "",        "url_private": "https://docs.google.com/document/d/1e8LtkvCSe_NH0UU0RyLgssmUQLT8G_3RMCGzyPWcx58/edit?tab=t.0",        "media_display_type": "unknown",        "permalink": "https://thetestenv.slack.com/files/U123A4BCDE5/F08EAQ813FW/test",        "comments_count": 0,        "is_starred": false,        "shares": {},        "channels": [],        "groups": [],        "ims": [],        "has_more_shares": false,        "external_id": "1234",        "external_url": "https://docs.google.com/document/d/1e8LtkvCSe_NH0UU0RyLgssmUQLT8G_3RMCGzyPWcx58/edit?tab=t.0",        "has_rich_preview": false,        "file_access": "visible"    }}
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

`bad_title`

The title provided is too long.

`bot_user_required`

bot user token is required

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

`invalid_external_id`

The external\_id provided is too long.

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