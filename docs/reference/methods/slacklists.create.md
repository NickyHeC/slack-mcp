Source: https://docs.slack.dev/reference/methods/slackLists.create

# slackLists.create method

DocsCall generator

## Facts {#facts}

**Description**Create a List.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/slackLists.create
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.slackLists.create
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.slackLists_create
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().slackListsCreate
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

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`name`**`string`Required

Name of the List.

_Example:_ `My List`

### Optional arguments

**`description_blocks`**`array`Optional

A rich text description of the List.

_Example:_ `[{"type":"rich_text","elements":[{"type":"rich_text_section","elements":[{"type":"text","text":"List to keep track of tasks!"}]}]}]`

**`schema`**`array`Optional

Column definition for the List.

_Example:_ `[{ "key": "task_name", "name": "Task Name", "type": "text", "is_primary_column": true }, { "key": "due_date", "name": "Due Date", "type": "date" }, { "key": "status", "name": "Status", "type": "select", "options": { "choices": [ { "value": "not_started", "label": "Not Started", "color": "red" }, { "value": "in_progress", "label": "In Progress", "color": "yellow" }, { "value": "completed", "label": "Completed", "color": "green" } ] } }, { "key": "assignee", "name": "Assignee", "type": "user" }]`

**`copy_from_list_id`**`string`Optional

ID of the List to copy.

_Example:_ `F1234567`

**`include_copied_list_records`**`boolean`Optional

Boolean indicating whether to include records when a List is copied.

_Example:_ `false`

**`todo_mode`**`boolean`Optional

Boolean indicating whether the List should be used to track todo tasks.

_Example:_ `true`

## Usage info {#usage-info}

Lists are only available to Slack workspaces on a paid plan.

This method is used to create a new standalone List owned by the acting user. The List will be created with only one text column if none of the optional parameters are specified.

When `todo_mode` is set to true, the list will be create with 3 additional fields used for task tracking:

*   Completed: a boolean column (column type `todo_completed`) for tracking whether or not an item is completed.
*   Assignee: a people column (column type `todo_assignee`) for storing who the assignee is for a given List item.
*   Due date: a date column (column type `todo_due_date`) for storing when the List item is due.

### Schema definition {#schema-definition}

The `schema` is defined with the following structure, with `?` denoting whether the field is optional:

```
[  {    "key": <string>, // Key of the column.    "name": <string>, // Name of the column to be displayed in the List.    "type": <string>, // Type of the column.    ?"is_primary_column": <boolean>, // Whether the column is the primary column.     // Only one column in the List can be the primary column, and it must be a text column.    // In addition, you cannot reassign a different column to be the new primary column, even     // if the new column is also a text column. If you want a new text column to be the primary     // one, it is recommended to export the List to CSV, modify the order, and then create a     // new List from the new CSV with the columns reordered.    ?"options": { // Column options.      ?"choices": [ // Used by select columns to specify options.        {          "value": <string>, // Value for the option.          "label": <string>, // Label of the option to be displayed in the List.          "color": <string> // Color type.        }      ],      ?"format": <string>, // Used by some columns (such as the select column) to specify       // some options/formatting.      ?"precision": <integer>, // Used by numeric columns to specify number of decimal places.      ?"date_format": <string>, // Used by date columns to specify the format of the date.      ?"emoji": <string>, // The emoji to be displayed e.g., ":smile:". Used by rating and       // vote columns.      ?"emoji_team_id": <string>, // The team ID the emoji belongs to. Used by rating columns.      ?"max": <integer>, // Used by rating columns to specify the maximum rate value.      ?"default_value_typed": { // Default value for some columns.        ?"user": [ <string> ], // Default user values (encoded user ids) for the people column.        ?"channel": [ <string> ], // Default channel values (encoded channel ids) for the         // channel column.        ?"select": [ <string> ] // Default select values for the select column.         // These values should be the same ones used in the choices value.        // When defining a select column, you can add up to 100 options.         // However, you can only add up to 50 for a single cell.      },      ?"show_member_name": boolean, // Used by people, channel, and canvas columns to specify       // whether the entity name should be shown. Default is true.      ?"notify_users": boolean // Used by people columns to specify whether the users should be       // notified  when the column is updated.    }  }]
```

### Schema-specific values {#schema-specific-values}

When the `schema` argument is provided, the following are some of the arguments that require specific values:

#### schema.type {#schematype}

*   text
*   message
*   number
*   select
*   date
*   user
*   attachment
*   checkbox
*   email
*   phone
*   channel
*   rating
*   created\_by
*   last\_edited\_by
*   created\_time
*   last\_edited\_time
*   vote
*   canvas
*   reference
*   link

#### schema.options.format {#schemaoptionsformat}

*   single\_select: format used by select columns to select a single option
*   multi\_select: format used by select columns to allow multiple selections
*   single\_entity: format used by user and channel columns to allow only one entity in the cell
*   multi\_entity: format used by user and channel columns to allow multiple entities in the cell

#### schema.options.date_format {#schemaoptionsdate_format}

*   default
*   DD/MM/YYYY
*   MM/DD/YYYY
*   YYYY/MM/DD
*   MMMM DD, YYYY
*   DD MMMM YYYY

#### schema.options.choices.color {#schemaoptionschoicescolor}

*   indigo
*   blue
*   cyan
*   pink
*   yellow
*   green
*   gray
*   red
*   purple
*   orange
*   brown

## Sample requests data {#sample-requests-data}

### Minimal {#minimal}

```
{  "token": "***",  "name": "My List"}
```

### With rich text description {#rich-text}

```
{  "token": "***",  "name": "My List",  "description_blocks": [    {      "type": "rich_text",      "elements": [        {          "type": "rich_text_section",          "elements": [            {              "type": "text",              "text": "List of favorite shows"            }          ]        }      ]    }  ]}
```

### With schema (all supported column types) {#schema-columns}

```
{  "token": "***",  "name": "All Column Types",  "schema": [    {      "key": "title",      "name": "Title",      "type": "text",      "is_primary_column": true    },    {      "key": "rich_text_notes",      "name": "Notes",      "type": "rich_text"    },    {      "key": "message_link",      "name": "Message",      "type": "message"    },    {      "key": "ranking",      "name": "Ranking",      "type": "number",      "options": {        "precision": 2      }    },    {      "key": "status",      "name": "Status",      "type": "select",      "options": {        "format": "single_select",        "choices": [          {            "value": "not_started",            "label": "Not Started",            "color": "red"          },          {            "value": "in_progress",            "label": "In Progress",            "color": "yellow"          },          {            "value": "completed",            "label": "Completed",            "color": "green"          }        ]      }    },    {      "key": "labels",      "name": "Labels",      "type": "multi_select",      "options": {        "format": "multi_select",        "choices": [          {            "value": "p0",            "label": "P0",            "color": "red"          },          {            "value": "p1",            "label": "P1",            "color": "yellow"          },          {            "value": "p2",            "label": "P2",            "color": "green"          }        ]      }    },    {      "key": "date",      "name": "Date",      "type": "date"    },    {      "key": "owner",      "name": "Owner",      "type": "user",      "options": {        "format": "single_entity"      }    },    {      "key": "attachments",      "name": "Attachments",      "type": "attachment"    },    {      "key": "ready",      "name": "Ready?",      "type": "checkbox"    },    {      "key": "email",      "name": "Email",      "type": "email"    },    {      "key": "phone",      "name": "Phone",      "type": "phone"    },    {      "key": "channel",      "name": "Channel",      "type": "channel"    },    {      "key": "rating",      "name": "Rating",      "type": "rating",      "options": {        "emoji": ":star:",        "max": 5      }    },    {      "key": "vote",      "name": "Vote",      "type": "vote"    },    {      "key": "assignee",      "name": "Assignee",      "type": "assignee"    },    {      "key": "due_date",      "name": "Due Date",      "type": "due_date"    },    {      "key": "completed",      "name": "Completed",      "type": "completed"    },    {      "key": "canvas",      "name": "Canvas",      "type": "canvas"    },    {      "key": "link",      "name": "Link",      "type": "link"    }  ]}
```

### Copy from an existing List (no records) {#copy-no-records}

```
{  "token": "***",  "name": "Copied List Without Records",  "include_copied_list_records": false,  "copy_from_list_id": "F012ABCD3EF"}
```

### Copy from an existing List (include records) {#copy-with-records}

```
{  "token": "***",  "name": "Copied List with Records",  "include_copied_list_records": true,  "copy_from_list_id": "F012ABCD3EF"}
```

### Todo mode {#todo-mode}

```
{  "token": "***",  "name": "My Todos",  "todo_mode": true}
```

### Description and schema {#desc-schema}

```
{  "token": "***",  "name": "Favorite Shows",  "description_blocks": [    {      "type": "rich_text",      "elements": [        {          "type": "rich_text_section",          "elements": [            {              "type": "text",              "text": "The Rise and Fall of Sanctuary Moon"            }          ]        }      ]    }  ],  "schema": [    {      "key": "title",      "name": "Title",      "type": "text",      "is_primary_column": true    }  ]}
```

### Schema and todo mode {#schema-todo-mode}

```
{  "token": "***",  "name": "Shows",  "todo_mode": true,  "schema": [    {      "key": "title",      "name": "Title",      "type": "text",      "is_primary_column": true    }  ]}
```

* * *

## Response {#response}

#### Typical success response: minimal

```
{  "ok": true,  "list_id": "F1234ABCD"}
```

#### Typical success response: with rich text description

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "name",        "name": "Name",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      }    ],    "subtask_schema": [      {        "key": "name",        "name": "Name",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      }    ]  }}
```

#### Typical success response: with schema (all supported column types)

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "rich_text_notes",        "name": "Notes",        "is_primary_column": false,        "type": "rich_text",        "id": "Col056A7BCDE8"      },      {        "key": "message_link",        "name": "Message",        "is_primary_column": false,        "type": "message",        "id": "Col090A1BCDE2"      },      {        "key": "ranking",        "name": "Ranking",        "is_primary_column": false,        "type": "number",        "options": {          "precision": 2,          "show_member_name": true        },        "id": "Col034A5BCDE6"      },      {        "key": "status",        "name": "Status",        "is_primary_column": false,        "type": "select",        "options": {          "choices": [            {              "value": "not_started",              "label": "Not Started",              "color": "red"            },            {              "value": "in_progress",              "label": "In Progress",              "color": "yellow"            },            {              "value": "completed",              "label": "Completed",              "color": "green"            }          ],          "format": "single_select",          "show_member_name": true        },        "id": "Col078A9BCDE0"      },      {        "key": "labels",        "name": "Labels",        "is_primary_column": false,        "type": "multi_select",        "options": {          "choices": [            {              "value": "p0",              "label": "P0",              "color": "red"            },            {              "value": "p1",              "label": "P1",              "color": "yellow"            },            {              "value": "p2",              "label": "P2",              "color": "green"            }          ],          "format": "multi_select",          "show_member_name": true        },        "id": "Col112A2BCDE3"      },      {        "key": "date",        "name": "Date",        "is_primary_column": false,        "type": "date",        "id": "Col223A3BCDE4"      },      {        "key": "owner",        "name": "Owner",        "is_primary_column": false,        "type": "user",        "options": {          "format": "single_entity",          "show_member_name": true        },        "id": "Col334A4BCDE5"      },      {        "key": "attachments",        "name": "Attachments",        "is_primary_column": false,        "type": "attachment",        "id": "Col556A6BCDE7"      },      {        "key": "ready",        "name": "Ready?",        "is_primary_column": false,        "type": "checkbox",        "id": "Col778A8BCDE9"      },      {        "key": "email",        "name": "Email",        "is_primary_column": false,        "type": "email",        "id": "Col990A0BCDE1"      },      {        "key": "phone",        "name": "Phone",        "is_primary_column": false,        "type": "phone",        "id": "Col111A1BCDE1"      },      {        "key": "channel",        "name": "Channel",        "is_primary_column": false,        "type": "channel",        "id": "Col222A2BCDE2"      },      {        "key": "rating",        "name": "Rating",        "is_primary_column": false,        "type": "rating",        "options": {          "emoji": ":star:",          "max": 5,          "show_member_name": true        },        "id": "Col333A3BCDE3"      },      {        "key": "vote",        "name": "Vote",        "is_primary_column": false,        "type": "vote",        "id": "Co444A4BCDE4"      },      {        "key": "assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "assignee",        "id": "Col555A5BCDE5"      },      {        "key": "due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "due_date",        "id": "Col666A6BCDE6"      },      {        "key": "completed",        "name": "Completed",        "is_primary_column": false,        "type": "completed",        "id": "Col777A7BCDE7"      },      {        "key": "canvas",        "name": "Canvas",        "is_primary_column": false,        "type": "canvas",        "id": "Col888A8BCDE8"      },      {        "key": "link",        "name": "Link",        "is_primary_column": false,        "type": "link",        "id": "Col999A9BCDE9"      }    ],    "subtask_schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col000A0BCDE0"      }    ]  }}
```

#### Typical success response: copy from an existing List (no records)

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "rich_text_notes",        "name": "Notes",        "is_primary_column": false,        "type": "rich_text",        "id": "Col056A7BCDE8"      },      {        "key": "message_link",        "name": "Message",        "is_primary_column": false,        "type": "message",        "id": "Col090A1BCDE2"      },      {        "key": "estimate",        "name": "Estimate",        "is_primary_column": false,        "type": "number",        "options": {          "precision": 2,          "show_member_name": true        },        "id": "Col034A5BCDE6"      },      {        "key": "status",        "name": "Status",        "is_primary_column": false,        "type": "select",        "options": {          "choices": [            {              "value": "not_started",              "label": "Not Started",              "color": "red"            },            {              "value": "in_progress",              "label": "In Progress",              "color": "yellow"            },            {              "value": "completed",              "label": "Completed",              "color": "green"            }          ],          "format": "single_select",          "show_member_name": true        },        "id": "Col078A9BCDE0"      },      {        "key": "labels",        "name": "Labels",        "is_primary_column": false,        "type": "multi_select",        "options": {          "choices": [            {              "value": "p0",              "label": "P0",              "color": "red"            },            {              "value": "p1",              "label": "P1",              "color": "yellow"            },            {              "value": "p2",              "label": "P2",              "color": "green"            }          ],          "format": "multi_select",          "show_member_name": true        },        "id": "Col112A2BCDE3"      },      {        "key": "date",        "name": "Date",        "is_primary_column": false,        "type": "date",        "id": "Col223A3BCDE4"      },      {        "key": "owner",        "name": "Owner",        "is_primary_column": false,        "type": "user",        "options": {          "format": "single_entity",          "show_member_name": true        },        "id": "Col334A4BCDE5"      },      {        "key": "attachments",        "name": "Attachments",        "is_primary_column": false,        "type": "attachment",        "id": "Col556A6BCDE7"      },      {        "key": "ready",        "name": "Ready?",        "is_primary_column": false,        "type": "checkbox",        "id": "Col778A8BCDE9"      },      {        "key": "email",        "name": "Email",        "is_primary_column": false,        "type": "email",        "id": "Col990A0BCDE1"      },      {        "key": "phone",        "name": "Phone",        "is_primary_column": false,        "type": "phone",        "id": "Col987A6BCDE5"      },      {        "key": "channel",        "name": "Channel",        "is_primary_column": false,        "type": "channel",        "id": "Col111A1BCDE1"      },      {        "key": "rating",        "name": "Rating",        "is_primary_column": false,        "type": "rating",        "options": {          "emoji": ":star:",          "max": 5,          "show_member_name": true        },        "id": "Col333A3BCDE3"      },      {        "key": "vote",        "name": "Vote",        "is_primary_column": false,        "type": "vote",        "id": "Co444A4BCDE4"      },      {        "key": "assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "assignee",        "id": "Col555A5BCDE5"      },      {        "key": "due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "due_date",        "id": "Col777A7BCDE7"      },      {        "key": "completed",        "name": "Completed",        "is_primary_column": false,        "type": "completed",        "id": "Col888A8BCDE8"      },      {        "key": "canvas",        "name": "Canvas",        "is_primary_column": false,        "type": "canvas",        "id": "Col999A9BCDE9"      },      {        "key": "link",        "name": "Link",        "is_primary_column": false,        "type": "link",        "id": "Col000A0BCDE0"      }    ],    "subtask_schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col543A2BCDE1"      }    ]  }}
```

#### Typical success response: copy from an existing List (include records)

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "rich_text_notes",        "name": "Notes",        "is_primary_column": false,        "type": "rich_text",        "id": "Col056A7BCDE8"      },      {        "key": "message_link",        "name": "Message",        "is_primary_column": false,        "type": "message",        "id": "Col090A1BCDE2"      },      {        "key": "estimate",        "name": "Estimate",        "is_primary_column": false,        "type": "number",        "options": {          "precision": 2,          "show_member_name": true        },        "id": "Col034A5BCDE6"      },      {        "key": "status",        "name": "Status",        "is_primary_column": false,        "type": "select",        "options": {          "choices": [            {              "value": "not_started",              "label": "Not Started",              "color": "red"            },            {              "value": "in_progress",              "label": "In Progress",              "color": "yellow"            },            {              "value": "completed",              "label": "Completed",              "color": "green"            }          ],          "format": "single_select",          "show_member_name": true        },        "id": "Col078A9BCDE0"      },      {        "key": "labels",        "name": "Labels",        "is_primary_column": false,        "type": "multi_select",        "options": {          "choices": [            {              "value": "p0",              "label": "P0",              "color": "red"            },            {              "value": "p1",              "label": "P1",              "color": "yellow"            },            {              "value": "p2",              "label": "P2",              "color": "green"            }          ],          "format": "multi_select",          "show_member_name": true        },        "id": "Col112A2BCDE3"      },      {        "key": "date",        "name": "Date",        "is_primary_column": false,        "type": "date",        "id": "Col223A3BCDE4"      },      {        "key": "owner",        "name": "Owner",        "is_primary_column": false,        "type": "user",        "options": {          "format": "single_entity",          "show_member_name": true        },        "id": "Col334A4BCDE5"      },      {        "key": "attachments",        "name": "Attachments",        "is_primary_column": false,        "type": "attachment",        "id": "Col556A6BCDE7"      },      {        "key": "ready",        "name": "Ready?",        "is_primary_column": false,        "type": "checkbox",        "id": "Col778A8BCDE9"      },      {        "key": "email",        "name": "Email",        "is_primary_column": false,        "type": "email",        "id": "Col990A0BCDE1"      },      {        "key": "phone",        "name": "Phone",        "is_primary_column": false,        "type": "phone",        "id": "Col111A1BCDE1"      },      {        "key": "channel",        "name": "Channel",        "is_primary_column": false,        "type": "channel",        "id": "Col333A3BCDE3"      },      {        "key": "rating",        "name": "Rating",        "is_primary_column": false,        "type": "rating",        "options": {          "emoji": ":star:",          "max": 5,          "show_member_name": true        },        "id": "Co444A4BCDE4"      },      {        "key": "vote",        "name": "Vote",        "is_primary_column": false,        "type": "vote",        "id": "Col555A5BCDE5"      },      {        "key": "assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "assignee",        "id": "Col777A7BCDE7"      },      {        "key": "due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "due_date",        "id": "Col888A8BCDE8"      },      {        "key": "completed",        "name": "Completed",        "is_primary_column": false,        "type": "completed",        "id": "Col999A9BCDE9"      },      {        "key": "canvas",        "name": "Canvas",        "is_primary_column": false,        "type": "canvas",        "id": "Col000A0BCDE0"      },      {        "key": "link",        "name": "Link",        "is_primary_column": false,        "type": "link",        "id": "Col543A2BCDE1"      }    ],    "subtask_schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col654A3BCDE2"      }    ]  }}
```

#### Typical success response: todo mode

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "name",        "name": "Name",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "todo_completed",        "name": "Completed",        "is_primary_column": false,        "type": "todo_completed",        "id": "Col00"      },      {        "key": "todo_assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "todo_assignee",        "options": {          "format": "multi_entity",          "default_value": null,          "show_member_name": true        },        "id": "Col01"      },      {        "key": "todo_due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "todo_due_date",        "id": "Col02"      }    ],    "subtask_schema": [      {        "key": "name",        "name": "Name",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "todo_completed",        "name": "Completed",        "is_primary_column": false,        "type": "todo_completed",        "id": "Col00"      },      {        "key": "todo_assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "todo_assignee",        "options": {          "format": "multi_entity",          "default_value": null,          "show_member_name": true        },        "id": "Col01"      },      {        "key": "todo_due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "todo_due_date",        "id": "Col02"      }    ]  }}
```

#### Typical success response: description and schema

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      }    ],    "subtask_schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      }    ]  }}
```

#### Typical success response: schema and todo mode

```
{  "ok": true,  "list_id": "F1234ABCD",  "list_metadata": {    "schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "todo_completed",        "name": "Completed",        "is_primary_column": false,        "type": "todo_completed",        "id": "Col00"      },      {        "key": "todo_assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "todo_assignee",        "options": {          "format": "multi_entity",          "default_value": null,          "show_member_name": true        },        "id": "Col01"      },      {        "key": "todo_due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "todo_due_date",        "id": "Col02"      }    ],    "subtask_schema": [      {        "key": "title",        "name": "Title",        "is_primary_column": true,        "type": "text",        "id": "Col012A3BCDE4"      },      {        "key": "todo_completed",        "name": "Completed",        "is_primary_column": false,        "type": "todo_completed",        "id": "Col00"      },      {        "key": "todo_assignee",        "name": "Assignee",        "is_primary_column": false,        "type": "todo_assignee",        "options": {          "format": "multi_entity",          "default_value": null,          "show_member_name": true        },        "id": "Col01"      },      {        "key": "todo_due_date",        "name": "Due Date",        "is_primary_column": false,        "type": "todo_due_date",        "id": "Col02"      }    ]  }}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_schema"}
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

`invalid_column_type`

Column type not allowed.

`invalid_copy_and_schema_args`

Cannot provide both `copy_from_list_id` and `schema`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_primary_column`

Missing or more than one primary column.

`invalid_schema`

The schema was invalid.

`method_deprecated`

The method has been deprecated.

`missing_arg_copy_from_list_id`

Missing argument `copy_from_list_id`.

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

`over_column_maximum`

Cannot create List with more than allowed column count.

`over_list_file_maximum`

Cannot create any more List files.

`over_title_length_maximum`

Title can not exceed defined length.

`permission_denied`

The user does not have permission to perform this action.

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