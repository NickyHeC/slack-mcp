Source: https://docs.slack.dev/reference/methods/canvases.create

# canvases.create method

DocsCall generator

## Facts {#facts}

**Description**Create canvas for a user

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/canvases.create
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.canvases.create
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.canvases_create
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().canvasesCreate
```

**Scopes**

Bot token:

[`canvases:write`](/reference/scopes/canvases.write)

User token:

[`canvases:write`](/reference/scopes/canvases.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Auth token with which to authenticate the session

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`title`**`string`Optional

Title of the newly created canvas

_Example:_ `Your Brilliant Title`

**`document_content`**Optional

Structure describing the type and value of the content to create

_Example:_ `{"type": "markdown", "markdown": "> standalone canvas!"}`

**`channel_id`**`string`Optional

Channel ID of the channel the canvas will be tabbed in. This is a required field for free teams.

## Usage info {#usage-info}

This method is used to create a new standalone canvas owned by the acting user.

The canvas will be created untitled and empty if none of the optional parameters are specified.

The canvas may be created with a `title`. The canvas may also be created with some initial `document_content`. The canvas's ID is returned in the response from the create call.

A canvas can be automatically added to a channel tab with `write` permissions by setting the `channel_id` parameter.

You can update the canvas's channel or user access by calling the [`canvases.access.set`](/reference/methods/canvases.access.set) method.

The following formatting elements are supported in the `document_content` object:

*   bold
*   bulleted lists
*   checklist
*   canvas unfurl
*   code block
*   code span
*   divider (horizontal rule)
*   emojis—standard and custom
*   file unfurls
*   hard line break
*   headings h1-h3
*   italic
*   link (in line)
*   link reference
*   markdown table
*   message unfurl
*   ordered lists
*   paragraph
*   profile unfurl
*   quote block
*   strikethrough
*   website unfurl
*   @ mentions for users and channels

Find more details about formatting the `document_content` object in the [Canvas surface documentation](/surfaces/canvases).

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "canvas_id": "F1234ABCD"}
```

#### Typical error response for bad content

```
{  "ok": false,  "error": "canvas_creation_failed",  "detail": "'content' error: line 28: Unsupported block type (List) within block quote"}
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

`canvas_creation_failed`

Canvas was unable to be created.

`canvas_disabled_user_team`

Canvas is disabled on user's team

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`free_teams_cannot_create_standalone_canvases`

Free teams cannot create standalone canvases

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

`restricted_action`

User does not have permission to perform this action.

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