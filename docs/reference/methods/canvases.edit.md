Source: https://docs.slack.dev/reference/methods/canvases.edit

# canvases.edit method

DocsCall generator

## Facts {#facts}

**Description**Update an existing canvas

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/canvases.edit
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.canvases.edit
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.canvases_edit
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().canvasesEdit
```

**Scopes**

Bot token:

[`canvases:write`](/reference/scopes/canvases.write)

User token:

[`canvases:write`](/reference/scopes/canvases.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Auth token with which to authenticate the session

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`canvas_id`**Required

Encoded ID of the canvas

_Example:_ `F1234ABCD`

**`changes`**`array`Required

List of changes to apply on the specified canvas

_Example:_ `[{"operation":"insert_before","document_content":{"type":"markdown","markdown":"Example content"},"section_id":"temp:C:AAAAAAAAAAAAAAAAAAAAAAAAAAAA"}]`

## Usage info {#usage}

This method is used to edit an existing canvas that the actor has write access to.

Different `operations` may be used to target different kinds of edits to a canvas. Sections may be deleted or replaced. New content can be added to the beginning or end of a canvas, or inserted relative to an existing section. Only one operation per API call is currently supported.

### Formatting the changes argument {#formatting}

The `changes` argument is an array of objects that provide instructions on how to edit the canvas. Each element in the `changes` array contains two properties: `operation` and either `document_content` or `title_content` (in the case of [renaming the canvas](#title-operations)).

### Content operations {#content-operations}

The `operation` property is a string that can be any of the following:

*   `insert_after`
*   `insert_before`
*   `insert_at_start`
*   `insert_at_end`
*   `replace`
*   `delete`

Using `insert_after` and `insert_before` requires providing a `section_id` and `document_content`. These updates are made relative to a section of the canvas, hence the required `section_id`. For details on how to find a `section_id`, refer to the [`canvases.sections.lookup`](/reference/methods/canvases.sections.lookup) method.

Alternatively, information can be added to the beginning or the end of the canvas using `insert_at_start` or `insert_at_end`, respectively. Using these operations requires providing a `document_content` argument.

Using the `replace` operation also requires providing a `document_content` argument. You can optionally specify a `section_id` or omit it to replace the entire canvas.

Using the `delete` operation requires providing a `section_id`, and you can only delete a section with this method. To delete an entire canvas, use the [`canvases.delete`](/reference/methods/canvases.delete) method instead. Once a canvas is deleted, there is no way to get it back.

#### Document content {#document-content}

You might recognize `document_content` from the [`canvases.create`](/reference/methods/canvases.create) method; it works the same.

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

### Title operations {#title-operations}

The `operation` property can also be used to rename the canvas, using `rename` and `title_content`, shown here:

```
{  "canvas_id": "F1234ABCD",  "changes": [    {      "operation": "rename",      "title_content": {        "type": "markdown",        "markdown": "Project Status :white_check_mark:"      }    }  ]}
```

Renaming the canvas supports markdown format only, including emojis in markdown format (e.g. `:white_check_mark:`). Differing from updating document content, the `rename` operation does not use a `section_id`.

### Examples {#examples}

This example shows inserting grocery items in a list format after providing the `section_id`.

```
{    "canvas_id": "F0166DCSTS7",    "changes": [        {            "operation": "insert_after",            "section_id": "temp:C:VXX8e648e6984e441c6aa8c61173",            "document_content": {                "type": "markdown",                "markdown": "- [ ] asparagus\n- [ ] coffee\n"            }        }    ]}
```

Then, we could update that same grocery list to check an item off. First, we would need to look up the item's ID, using the [`canvases.sections.lookup`](/reference/methods/canvases.sections.lookup) method. Using the ID that is returned with that, we can check off the item like this:

```
{    "canvas_id": "F0166DCSTS7",    "changes": [        {            "operation": "replace",            "section_id": "temp:C:VXX37d27db7718d44e28803566ae",            "document_content": {                "type": "markdown",                "markdown": "- [x] asparagus\n"            }        }    ]}
```

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response for bad content

```
{  "ok": false,  "error": "canvas_editing_failed",  "detail": "'content' error: line 28: Unsupported block type (List) within block quote"}
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

`canvas_disabled_user_team`

Canvas is disabled on user's team

`canvas_editing_failed`

The changes to the canvas failed to be applied.

`canvas_not_found`

The canvas you wish to apply changes to is not available.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`free_teams_cannot_edit_standalone_canvases`

Free teams cannot edit standalone canvases

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