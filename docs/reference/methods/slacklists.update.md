Source: https://docs.slack.dev/reference/methods/slackLists.update

# slackLists.update method

DocsCall generator

## Facts {#facts}

**Description**Update a List.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/slackLists.update
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.slackLists.update
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.slackLists_update
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().slackListsUpdate
```

**Scopes**

Bot token:

[`lists:write`](/reference/scopes/lists.write)

User token:

[`lists:write`](/reference/scopes/lists.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

**`id`**Required

The ID of the List to update.

### Optional arguments

**`name`**`string`Optional

The updated name of the List.

_Example:_ `My List`

**`description_blocks`**`array`Optional

A rich text description of the List.

_Example:_ `[{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"text","text":"My list description!"}]}]}]`

**`todo_mode`**`boolean`Optional

Boolean indicating whether the List should be in todo mode.

_Example:_ `true`

## Usage info {#usage-info}

Lists are only available to Slack workspaces on a paid plan.

This method allow you to update a List name, description, and TODO mode. TODO mode is used by clients to hide task tracking fields when `todo_mode` is set false, or to unhide or create task tracking fields when `todo_mode` is set true.

Task tracking fields are as follows:

*   Completed: a boolean column (column type `todo_completed`) for tracking when an item is completed or not.
*   Assignee: a people column (column type `todo_assignee`) for storing who the assignee is for a given List item.
*   Due date: a date column (column type `todo_due_date`) for storing when the List item is due.

## Sample requests data {#sample-requests-data}

### Rename only {#rename-only}

```
{  "token": "***",  "name": "Updated Name",  "id": "F012ABCD3EF"}
```

### Update description only {#desc-only}

```
{  "token": "***",  "description_blocks": [    {      "type": "rich_text",      "elements": [        {          "type": "rich_text_section",          "elements": [            {              "type": "text",              "text": "My List description"            }          ]        }      ]    }  ],  "id": "F012ABCD3EF"}
```

### Toggle todo mode on {#todo-mode}

```
{  "token": "***",  "todo_mode": true,  "id": "F012ABCD3EF"}
```

### Name, description, and todo mode {#name-desc-todo}

```
{  "token": "***",  "name": "Sprint Board",  "todo_mode": false,  "description_blocks": [    {      "type": "rich_text",      "elements": [        {          "type": "rich_text_section",          "elements": [            {              "type": "text",              "text": "Work for this sprint"            }          ]        }      ]    }  ],  "id": "F012ABCD3EF"}
```

* * *

## Response {#response}

#### Typical success response for all scenarios above

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "list_not_found"}
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

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_channel_rename_error`

Failed to rename file channel based on file title.

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

`list_editor_upsert_error`

Failed to upsert List editor.

`list_edits_update_error`

Failed to update List metadata.

`list_not_found`

The List was not found.

`method_deprecated`

The method has been deprecated.

`missing_arguments`

No arguments were provided to update the List.

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

`over_title_length_maximum`

Title can not exceed defined length.

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

The team cannot be found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unexpected_description_blocks_arg`

Unexpected description blocks argument.

`user_not_found`

The user cannot be found.