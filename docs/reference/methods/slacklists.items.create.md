Source: https://docs.slack.dev/reference/methods/slackLists.items.create

# slackLists.items.create method

DocsCall generator

## Facts {#facts}

**Description**Add a new item to an existing List.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/slackLists.items.create
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.slackLists.items.create
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.slackLists_items_create
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().slackListsItemsCreate
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

Token with which to authenticate the session.

**`list_id`**Required

ID of the List to add the item to.

### Optional arguments

**`duplicated_item_id`**Optional

ID of the record to make a copy of.

**`parent_item_id`**Optional

ID of the parent record for this subtask.

**`initial_fields`**`array`Optional

Initial item data.

## Usage info {#usage-info}

Lists are only available to Slack workspaces on a paid plan.

This method is used to create a new item, also known as a record, in an existing List.

The item will be created with the field values specified in the `initial_fields` parameter. Each field corresponds to a column in the List and must reference a valid `column_id`.

The response includes the created item with all its field values, plus metadata:

*   `id`: The unique identifier for the created item.
*   `list_id`: The List the item belongs to.
*   `date_created`: Unix timestamp when the item was created.
*   `created_by`: User ID of the user who created the item.
*   `updated_by`: User ID of the user who last updated the item.
*   `updated_timestamp`: String timestamp of last update.
*   `parent_record_id`: Present if this is a subtask.
*   `fields`: Array of all field values with their formatted representations.

## Sample requests data {#sample-requests-data}

### Minimal {#minimal}

```
{  "token": "***",  "list_id": "F1234ABCD"}
```

### With initial field values {#initial-field-values}

Provide field values using the `initial_fields` parameter:

```
{  "token": "***",  "list_id": "F1234ABCD",  "initial_fields": [    {      "column_id": "Col10000000",      "rich_text": [        {          "type": "rich_text",          "elements": [            {              "type": "rich_text_section",               "elements": [                {                  "type": "text",                  "text": "List of favorite shows"                }              ]            }          ]        }      ]    }  ]}
```

### Text column (plain text) {#text-column-plain}

While a bit counterintuitive, you must use `rich_text` blocks in a request that includes plain text. This is because List text fields are always rich text in order to create consistency across Slack's text editing experience. You may see the `text` property appear in a response as a fallback, but it is not accepted in the request payload. Instead, format your request using the Block Kit `rich_text` block as in the example below:

```
{  "token": "***",  "list_id": "F1234ABCD",  "initial_fields": [    {      "column_id": "Col018B8C91TM",      "rich_text": [        {          "type": "rich_text",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "Timestream Defenders Orion"                }              ]            }          ]        }      ]    }  ]}
```

### With initial date, select, and user fields {#date-select-user}

```
{  "token": "***",  "list_id": "F1234ABCD",  "initial_fields": [    {      "column_id": "Col018AL764AE",      "date": ["2025-10-10"]    },    {      "column_id": "Col018AL7649G",      "select": ["completed"]    },    {      "column_id": "Col018B8C91V1",      "user": ["U012A34BCDE"]    }  ]}
```

### Duplicate an item {#duplicate}

Create a copy of an existing item by specifying the `duplicated_item_id`:

```
{  "token": "***",  "list_id": "F1234ABCD",  "duplicated_item_id": "Rec12345678"}
```

### Create a subtask under a parent item {#create-a-subtask-under-a-parent-item}

Create a subtask by specifying the `parent_item_id`:

```
{  "token": "***",  "list_id": "F1234ABCD",  "parent_item_id": "Rec12345678",   "initial_fields": [    {      "column_id": "Col10000000",      "select": ["OptHIGH123"]    }  ]}
```

## Field types {#field-types}

The `initial_fields` parameter supports all column types available in Lists. The supported field formats are listed with examples below.

**Text field (rich\_text)**

```
{  "column_id": "Col123",  "rich_text": [    {      "type": "rich_text",      "elements": [        {          "type": "rich_text_section",          "elements": [            {              "type": "text",              "text": "Worldhoppers"            }          ]        }      ]    }  ]}
```

**User field**

```
{  "column_id": "Col123",  "user": ["U1234567", "U2345678"]}
```

**Date field**

```
{  "column_id": "Col123",   "date": ["2025-10-10"]}
```

**Select field**

```
{  "column_id": "Col123",  "select": ["OptionId123"]}
```

**Checkbox field**

```
{  "column_id": "Col123",  "checkbox": true}
```

**Number field**

```
{  "column_id": "Col123",  "number": [5000]}
```

**Email field**

```
{  "column_id": "Col123",  "email": ["perihelion@univmiharanewtideland.com"]}
```

**Phone field**

```
{  "column_id": "Col123",   "phone": ["+1-555-123-4567"]}
```

**Attachment field**

```
{  "column_id": "Col123",  "attachment": ["F1234567890"]}
```

**Link field**

```
{  "column_id": "Col123",  "link": [    {      "original_url": "https://docs.slack.dev/",      "display_as_url": false,      "display_name": "Slack Developer Docs"    }  ]}
```

**Message field**

```
{  "column_id": "Col123",  "message": ["https://yourteam.slack.com/archives/C1234567890/p1234567890123456"]}
```

**Rating field**

```
{  "column_id": "Col123",  "rating": [4]}
```

**Timestamp field**

```
{  "column_id": "Col123",  "timestamp": [1704067200]}
```

**Channel field**

```
{  "column_id": "Col123",  "channel": ["C1234567890"]}
```

**Reference field**

```
{  "column_id": "Col123",  "reference": [    {      "file": {        "file_id": "F1234567890"      }    }  ]}
```

* * *

## Response {#response}

#### Typical success response: minimal

```
{  "ok": true,  "item": {    "id": "Rec018ALE9718",    "list_id": "F1234567",    "date_created": 1758744345,    "created_by": "W0AB1CDE2",    "updated_by": "W0AB1CDE2",    "fields": [],    "updated_timestamp": "1758744345"  }}
```

#### Typical success response: text column (plain text)

```
{  "ok": true,  "item": {    "id": "Rec018ALFLNTU",    "list_id": "F1234567",    "date_created": 1758744345,    "created_by": "W0AB1CDE2",    "updated_by": "W0AB1CDE2",    "fields": [      {        "key": "rich_text_notes",        "value": "[{\"type\":\"rich_text\",\"block_id\":\"k0zIi\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Fix bug\"}]}]}]",        "text": "Fix bug",        "rich_text": [          {            "type": "rich_text",            "block_id": "k0zIi",            "elements": [              {                "type": "rich_text_section",                "elements": [                  {                    "text": "Fix bug",                    "type": "text"                  }                ]              }            ]          }        ],        "column_id": "Col018B8C91TM"      }    ],    "updated_timestamp": "1758744345"  }}
```

#### Typical success response: with initial date, select, and user fields

```
{  "ok": true,  "item": {    "id": "Rec018ALA7RPU",    "list_id": "F1234567",    "date_created": 1758744346,    "created_by": "W0AB1CDE2",    "updated_by": "W0AB1CDE2",    "fields": [      {        "key": "status",        "value": "completed",        "select": [          "completed"        ],        "column_id": "Col018AL7649G"      },      {        "key": "date",        "value": "2025-09-19",        "date": [          "2025-09-19"        ],        "timestamp": [          -1        ],        "column_id": "Col018AL764AE"      },      {        "key": "owner",        "value": "U012A34BCDE",        "user": [          "U012A34BCDE"        ],        "column_id": "Col018B8C91V1"      }    ],    "updated_timestamp": "1758744346"  }}
```

#### Typical success response: with initial date, select, and user fields

```
{  "ok": true,  "item": {    "id": "Rec018ALFLP2N",    "list_id": "F1234567",    "date_created": 1758744346,    "created_by": "W0AB1CDE2",    "updated_by": "W0AB1CDE2",    "fields": [],    "updated_timestamp": "1758744346"  }}
```

#### Typical success response: create a subtask under a parent item

```
{  "ok": true,  "item": {    "id": "Rec018B8RR603",    "list_id": "F1234567",    "date_created": 1758744346,    "created_by": "W0AB1CDE2",    "updated_by": "W0AB1CDE2",    "fields": [],    "updated_timestamp": "1758744346"  }}
```

#### Error when the specified List doesn't exist

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

`duplicated_item_not_found`

The item to duplicate cannot be found.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_not_found`

The attachment file could not be found.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_args`

The provided arguments are invalid.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_column_id`

The column ID provided does not exist in the List.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_input_type`

The field value type does not match the column type.

`invalid_option_id`

Option ID provided does not match column definition.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_vote_value`

Invalid value provided for a vote column.

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

Too many values provided for a single field.

`over_row_maximum`

Cannot create more items over the maximum.

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

`uneditable_column`

Initial values provided for an uneditable column.

`user_not_found`

The user cannot be found.