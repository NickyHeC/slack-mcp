Source: https://docs.slack.dev/reference/methods/slackLists.items.update

# slackLists.items.update method

DocsCall generator

## Facts {#facts}

**Description**Updates cells in a List.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/slackLists.items.update
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.slackLists.items.update
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.slackLists_items_update
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().slackListsItemsUpdate
```

**Scopes**

Bot token:

[`lists:write`](/reference/scopes/lists.write)

User token:

[`lists:write`](/reference/scopes/lists.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

**`list_id`**`string`Required

ID of the List to add or update cells.

_Example:_ `F01ABCDE2FG`

**`cells`**`array`Required

Cells to update.

_Example:_ `[{"row_id":"Rec014K005UQJ","column_id":"Col014K005UQJ","user":["U01284PCR98", "U0137181B5H"]}]`

## Usage info {#usage-info}

Lists are only available to Slack workspaces on a paid plan.

This method is used to update cells in a List.

## Sample requests data {#sample-requests-data}

### Update text (text column) {#update-text}

```
{  "token": "***",  "list_id": "F01ABCDE2FG",  "cells": [    {      "column_id": "Col018B8C91TM",      "rich_text": [        {          "type": "rich_text",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "Updated text"                }              ]            }          ]        }      ],      "row_id": "Rec018B8RR603"    }  ]}
```

### Update select option {#update-select}

```
{  "token": "***",  "list_id": "F01ABCDE2FG",  "cells": [    {      "column_id": "Col018AL7649G",      "select": ["in_progress"],      "row_id": "Rec018B8RR603"    }  ]}
```

### Update user field (multi-user) {#update-user}

```
{  "token": "***",  "list_id": "F01ABCDE2FG",  "cells": [    {      "column_id": "Col018B8C91V1",      "user": ["W0QR1STU2", "U012A34BCDE"],      "row_id": "Rec018B8RR603"    }  ]}
```

### Update date {#update-date}

```
{  "token": "***",  "list_id": "F01ABCDE2FG",  "cells": [    {      "column_id": "Col018AL764AE",      "date": [ "2025-09-20"],      "row_id": "Rec018B8RR603"    }  ]}
```

### Create new row via cells {#create-via-cella}

```
{  "token": "***",  "list_id": "F018B8C91SP",  "cells": [    {      "row_id_to_create": true,      "column_id": "Col018B8C91TM",      "rich_text": [        {          "type": "rich_text",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "New row title"                }              ]            }          ]        }      ],      "row_id": "Rec018B8RR603"    }  ]}
```

### Rich text cell (rich_text_column) {#rich-text}

```
{  "token": "***",  "list_id": "F018B8C91SP",  "cells": [    {      "column_id": "Col018B8C91TM",      "rich_text": [        {          "type": "rich_text",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "Notes"                }              ]            }          ]        }      ],      "row_id": "Rec018B8RR603"    }  ]}
```

* * *

## Response {#response}

#### Typical success response for all scenarios above

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_row_id"}
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

`channel_not_found`

The channel cannot be found.

`column_id_not_provided`

The `column_id` or `column_id_to_create` field must be provided.

`column_not_found`

The column was not found.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_not_found`

Invalid file ID for this List.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_attachment`

Invalid attachment provided.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_blocks`

Rich text payload supplied is invalid.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_column_id`

Invalid column ID for this List.

`invalid_date`

Date supplied is invalid.

`invalid_email`

Email supplied is invalid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_input_type`

Supplied value key or value type is invalid for the given column type.

`invalid_link`

Message archive link supplied is invalid.

`invalid_message`

Invalid message provided.

`invalid_option_id`

Option supplied is invalid.

`invalid_phone_number`

Invalid phone number provided.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_row_id`

Invalid row ID for this List.

`invalid_text_block`

Rich text payload supplied is invalid.

`invalid_vote_value`

Invalid vote value is supplied.

`list_not_found`

The List was not found.

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

`over_cell_fields_limit`

The supplied cell fields are over the cell field maximum.

`permission_denied`

The user does not have permission to perform this action.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`row_id_not_provided`

The `row_id` or `row_id_to_create` field must be provided.

`row_not_found`

The row was not found.

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

`uneditable_column`

The column cannot be updated.

`user_not_found`

The user cannot be found.