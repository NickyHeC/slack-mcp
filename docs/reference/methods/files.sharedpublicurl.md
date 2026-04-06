Source: https://docs.slack.dev/reference/methods/files.sharedPublicURL

# files.sharedPublicURL method

DocsCall generator

## Facts {#facts}

**Description**Enables a file for public/external sharing.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/files.sharedPublicURL
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.files.sharedPublicURL
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.files_sharedPublicURL
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().filesSharedPublicURL
```

**Scopes**

User token:

[`files:write`](/reference/scopes/files.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`file`**`string`Required

File to share

## Usage info {#usage-info}

This method enables public/external sharing for a file.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
```

The response contains a [file object](/reference/objects/file-object), including the `permalink_public` url.

```
    {        "ok": true,        "file": {            "id" : "F2147483862",            "timestamp" : 1356032811,            "name" : "file.htm",            "title" : "My HTML file",            "mimetype" : "text\/plain",            "filetype" : "text",            "pretty_type": "Text",            "user" : "U2147483697",            "mode" : "hosted",            "editable" : true,            "is_external": false,            "external_type": "",            "size" : 12345,            "url_private": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/1.png",            "url_private_download": "https:\/\/slack.com\/files-pri\/T024BE7LD-F024BERPE\/download\/1.png",            "thumb_64": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_64.png",            "thumb_80": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_80.png",            "thumb_360": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.png",            "thumb_360_gif": "https:\/\/slack-files.com\/files-tmb\/T024BE7LD-F024BERPE-c66246\/1_360.gif",            "thumb_360_w": 100,            "thumb_360_h": 100,            "permalink": "https:\/\/coolkids.slack.com\/files\/cal\/F024BERPE\/1.png",            "permalink_public": "https:\/\/slack-files.com\/T024BE7LD-F024BERPE-8004f909b1",            "edit_link": "https:\/\/coolkids.slack.com\/files\/cal\/F024BERPE\/1.png/edit",            "preview": "&lt;!DOCTYPE html&gt;\n&lt;html&gt;\n&lt;meta charset='utf-8'&gt;",            "preview_highlight": "&lt;div class=\"sssh-code\"&gt;&lt;div class=\"sssh-line\"&gt;&lt;pre&gt;&lt;!DOCTYPE html...",            "lines" : 123,            "lines_more": 118,            "is_public": true,            "public_url_shared": false,            "channels": ["C024BE7LT", ...],            "groups": ["G12345", ...],            "initial_comment": {...},            "num_stars": 7,            "is_starred": true        },        "comments": [            {                "id": "Fc027BN9L9",                "timestamp": 1356032811,                "user": "U2147483697",                "comment": "This is a comment"            },            ...        ],        "paging": {            "count": 100,            "total": 2,            "page": 1,            "pages": 0        }    }
```

The [file object](/reference/objects/file-object) contains information about the uploaded file.

Only the original creator of the file can use the `files.sharedPublicURL` method unless the file is shared into a public channel.

Each comment object in the comments array contains details about a single comment. Comments are returned oldest first.

The paging information contains the `count` of comments returned, the `total` number of comments, the `page` of results returned in this response and the total number of `pages` available. Please note that the max `count` value is `1000` and the max `page` value is `100`.

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

`file_not_found`

Value passed for `file` was invalid

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

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed`

Public sharing has been disabled for this team. You may see this error if you are creating an external link from a free or trial workspace. You can either upgrade to a [Paid Plan](https://app.slack.com/plans) or use `file.list` to get a `url_private_download` link, download the file with an application, and re-upload it somewhere it can be shared with users who are not members of your workspace. Be sure to pass the Slack [Bot token](/authentication/tokens#bot) to the request on the headers file when calling `url_private_download`.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`public_file_type_not_allowed`

Public sharing has been restricted for this file type.

`public_video_not_allowed`

Public sharing of videos is not available. A `Free` instance of Slack may encounter this error because free teams don't have the ability to share video files publicly.

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