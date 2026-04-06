Source: https://docs.slack.dev/reference/methods/slackLists.items.list

# slackLists.items.list method

DocsCall generator

## Facts {#facts}

**Description**Get records from a List.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/slackLists.items.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.slackLists.items.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.slackLists_items_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().slackListsItemsList
```

**Scopes**

Bot token:

[`lists:read`](/reference/scopes/lists.read)

User token:

[`lists:read`](/reference/scopes/lists.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Token with which to authenticate the session.

**`list_id`**`string`Required

ID of the List.

_Example:_ `F12345678`

### Optional arguments

**`limit`**`integer`Optional

The maximum number of records to return.

_Example:_ `100`

**`cursor`**`string`Optional

Next cursor for pagination.

_Example:_ `bGlzdF9pZDoxMjIxNzk3NzMyNDgzO2lkOjEyNzAxMjMxNTEzOTQ7ZGF0ZV9jcmVhdGVkOjE3NTE1NTkyMTU=`

**`archived`**`boolean`Optional

Boolean indicating whether archived items or normal items should be returned.

_Example:_ `true`

## Usage info {#usage-info}

Lists are only available to Slack workspaces on a paid plan.

This method is used to retrieve many items from one List. The example successful JSON response below shows the information that will be returned, with `?` denoting whether the field may be present in the response.

## Request template {#request-template}

```
{    "ok": true,    "items": [                         // array of rows/items for a given List        {            "id": <string>,            // the encoded ID of the item            "list_id": <string>,       // the encoded List ID of the item            "date_created": <integer>, // the date the item was created            "fields": [                // data for each cell                 {                    "key": <string>,                             // an identifier for the column. It can either be an encoded column ID or any text. This will be deprecated in favor of `column_id`                    "value": <boolean | string | number | null>, // the value of the cell. This will also be deprecated eventually in favor of typed values defined in their own field below                    ?"column_id": <string>,                    ?"text": <string>,                           // plain text fallback of the cell value, similar to normal Slack messages                    ?"rich_text": [<rich text>],                 // Block Kit-formatted message. Only the rich text variant is supported at this time                    ?"message": [                        {                            "value": <string>,                   // the message URL                            "channel_id": <string>,              // the encoded channel ID                            "ts": <string>,                      // the timestamp the message was sent                            "thread_ts": <string>                // the timestamp the message in thread was sent                        }                    ],                    ?"number": [ <number> ],                     // an array of numbers (integer or rational numbers)                    ?"select": [ <string> ],                     // an array of List encoded option IDs                    ?"date": [ <string> ],                       // an array of date strings in the format YYYY-MM-DD                    ?"user": [ <string> ],                       // an array of encoded user IDs                    ?"channel": [ <string> ],                    // an array of encoded channel IDs                    ?"attachment": [ <string> ],                 // an array of encoded file IDs                    ?"checkbox": [ boolean ],                    // boolean value indicating whether or not the checkbox is enabled                    ?"email": [ <string> ],                      // an array of emails                    ?"phone": [ <string> ],                      // an array of phone numbers                    ?"rating": [ <integer> ],                    // an integer representing the number of emoji for a given rating (the array will have one value)                    ?"timestamp": [ <integer> ],                 // an array of unix timestamps                    ?"link": [                        {                            "originalUrl": <string>,             // the link URL                            ?"attachment": <object | null>,      // metadata information retrieved from the link URL                            ?"displayAsUrl": <boolean>,          // if true, the link URL will be displayed in the cell instead of website name retrieved from URL metadata                            ?"displayName": <displayName>        // the name to display in the cell                        }                    ],                    "reference": [                       // a field referencing another entity, such as another List or a canvas                        {                            ?"message": {                    // reference to a message                                "channel_id": <string>,      // encoded channel ID                                "ts": <string>,              // timestamp the message was sent                                ?"thread_ts": <string>       // timestamp the thread message was sent                            },                            ?"list_record": {                // reference to a List item                                "list_id": <string>,         // the encoded List ID                                "row_id": <string>           // the encoded row/item ID                            },                            ?"file": {                       // reference to a file                                "file_id": <string>          // the encoded file ID                            },                            ?"canvas_section": {             // reference to a canvas section                                "file_id": <string>,         // the encoded canvas ID                                "section_id": <string>       // the section ID of the canvas                            }                        }                    ]                }            ],            ?"created_by": <string>,        // the encoded user ID of the user who created the item            ?"updated_timestamp": <string>, // the date the item was last updated            ?"updated_by": <string>,        // the encoded user ID of the user who performed the update on the item            ?"parent_record_id": <string>,  // the encoded item ID of the parent item in case this is a subtask            ?"archived": <boolean>,         // indicates whether this item is archived or not            ?"is_subscribed": <boolean>,    // indicates whether the user sending the request is subscribed to the item            ?"saved": {                     // reminder information for item                "is_archived": <boolean>,       // indicates whether the reminder is archived or not                ?"date_due": <integer>,         // the date the reminder is due                ?"date_completed": <integer>,   // the date the reminder was marked as completed                "state": <string>               // The state of the reminder. Values allowed are `archived`, `in_progress` and `completed`            },            ?"saved_fields": {              // reminder information for specific cells                "Col1234ABCD": {                // the encoded column ID for the reminder of the item                    "is_archived": <boolean>,       // indicates whether the reminder is archived or not                    ?"date_due": <integer>,         // the date the reminder is due                    ?"date_completed": <integer>,   // the date the reminder was marked as completed                    "state": <string>               // The state of the reminder. Values allowed are `archived`, `in_progress`, and `completed`                }            }        }    ],    "response_metadata": {             // response metadata with cursor information        "next_cursor": <string>        // cursor information for the next set of items    }}
```

## Sample requests data {#sample-requests-data}

### Minimal {#minimal}

```
{  "token": "***",  "list_id": "F1234567"}
```

### With limit {#limit}

```
{  "token": "***",  "list_id": "F1234567",  "limit": 100}
```

### Return archived items {#archived}

```
{  "token": "***",  "list_id": "F1234567",  "archived": true}
```

* * *

## Response {#response}

#### Typical success response: minimal

```
{  "ok": true,  "items": [    {      "id": "Rec018B8X2B3M",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "rich_text_notes",          "value": "[{\"type\":\"rich_text\",\"block_id\":\"08jc0\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Onboard new hire\"}]}]}]",          "text": "Onboard new hire",          "rich_text": [            {              "type": "rich_text",              "block_id": "08jc0",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "text": "Onboard new hire",                      "type": "text"                    }                  ]                }              ]            }          ],          "column_id": "Col018B8C91TM"        },        {          "key": "estimate",          "value": 3,          "number": [            3          ],          "column_id": "Col018B8C91U3"        }      ],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018B8RR603",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018ALFLP2N",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018ALA7RPU",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "status",          "value": "completed",          "select": [            "completed"          ],          "column_id": "Col018AL7649G"        },        {          "key": "date",          "value": "2025-09-19",          "date": [            "2025-09-19"          ],          "timestamp": [            -1          ],          "column_id": "Col018AL764AE"        },        {          "key": "owner",          "value": "U014W31KQMR",          "user": [            "U014W31KQMR"          ],          "column_id": "Col018B8C91V1"        }      ],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018B8LPLG3",      "list_id": "F1234567",      "date_created": 1758744345,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "rich_text_notes",          "value": "[{\"type\":\"rich_text\",\"block_id\":\"UXkfa\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Onboard new hire \"},{\"type\":\"text\",\"text\":\"(week 1)\",\"style\":{\"bold\":true}}]}]}]",          "text": "Onboard new hire *(week 1)*",          "rich_text": [            {              "type": "rich_text",              "block_id": "UXkfa",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "text": "Onboard new hire ",                      "type": "text"                    },                    {                      "text": "(week 1)",                      "type": "text",                      "style": {                        "bold": true                      }                    }                  ]                }              ]            }          ],          "column_id": "Col018B8C91TM"        }      ],      "updated_timestamp": "1758744345"    },    {      "id": "Rec018ALFLNTU",      "list_id": "F1234567",      "date_created": 1758744345,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "rich_text_notes",          "value": "[{\"type\":\"rich_text\",\"block_id\":\"k0zIi\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Fix bug\"}]}]}]",          "text": "Fix bug",          "rich_text": [            {              "type": "rich_text",              "block_id": "k0zIi",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "text": "Fix bug",                      "type": "text"                    }                  ]                }              ]            }          ],          "column_id": "Col018B8C91TM"        }      ],      "updated_timestamp": "1758744345"    },    {      "id": "Rec018ALE9718",      "list_id": "F1234567",      "date_created": 1758744345,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [],      "updated_timestamp": "1758744345"    }  ],  "response_metadata": {    "next_cursor": ""  }}
```

#### Typical success response: with limit

```
{  "ok": true,  "items": [    {      "id": "Rec018B8X2B3M",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "rich_text_notes",          "value": "[{\"type\":\"rich_text\",\"block_id\":\"08jc0\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Onboard new hire\"}]}]}]",          "text": "Onboard new hire",          "rich_text": [            {              "type": "rich_text",              "block_id": "08jc0",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "text": "Onboard new hire",                      "type": "text"                    }                  ]                }              ]            }          ],          "column_id": "Col018B8C91TM"        },        {          "key": "estimate",          "value": 3,          "number": [            3          ],          "column_id": "Col018B8C91U3"        }      ],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018B8RR603",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018ALFLP2N",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018ALA7RPU",      "list_id": "F1234567",      "date_created": 1758744346,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "status",          "value": "completed",          "select": [            "completed"          ],          "column_id": "Col018AL7649G"        },        {          "key": "date",          "value": "2025-09-19",          "date": [            "2025-09-19"          ],          "timestamp": [            -1          ],          "column_id": "Col018AL764AE"        },        {          "key": "owner",          "value": "U014W31KQMR",          "user": [            "U014W31KQMR"          ],          "column_id": "Col018B8C91V1"        }      ],      "updated_timestamp": "1758744346"    },    {      "id": "Rec018B8LPLG3",      "list_id": "F1234567",      "date_created": 1758744345,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "rich_text_notes",          "value": "[{\"type\":\"rich_text\",\"block_id\":\"UXkfa\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Onboard new hire \"},{\"type\":\"text\",\"text\":\"(week 1)\",\"style\":{\"bold\":true}}]}]}]",          "text": "Onboard new hire *(week 1)*",          "rich_text": [            {              "type": "rich_text",              "block_id": "UXkfa",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "text": "Onboard new hire ",                      "type": "text"                    },                    {                      "text": "(week 1)",                      "type": "text",                      "style": {                        "bold": true                      }                    }                  ]                }              ]            }          ],          "column_id": "Col018B8C91TM"        }      ],      "updated_timestamp": "1758744345"    },    {      "id": "Rec018ALFLNTU",      "list_id": "F1234567",      "date_created": 1758744345,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [        {          "key": "rich_text_notes",          "value": "[{\"type\":\"rich_text\",\"block_id\":\"k0zIi\",\"elements\":[{\"type\":\"rich_text_section\",\"elements\":[{\"type\":\"text\",\"text\":\"Fix bug\"}]}]}]",          "text": "Fix bug",          "rich_text": [            {              "type": "rich_text",              "block_id": "k0zIi",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "text": "Fix bug",                      "type": "text"                    }                  ]                }              ]            }          ],          "column_id": "Col018B8C91TM"        }      ],      "updated_timestamp": "1758744345"    },    {      "id": "Rec018ALE9718",      "list_id": "F1234567",      "date_created": 1758744345,      "created_by": "W0AB1CDE2",      "updated_by": "W0AB1CDE2",      "fields": [],      "updated_timestamp": "1758744345"    }  ],  "response_metadata": {    "next_cursor": ""  }}
```

#### Typical success response: return archived items

```
{  "ok": true,  "items": [],  "response_metadata": {    "next_cursor": ""  }}
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

`archive_not_supported`

Archiving is not supported.

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

`invalid_cursor`

Value passed for `cursor` was not valid or is no longer valid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

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

`user_not_found`

The user cannot be found.