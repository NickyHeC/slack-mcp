Source: https://docs.slack.dev/reference/methods/slackLists.items.info

# slackLists.items.info method

DocsCall generator

## Facts {#facts}

**Description**Get a row from a List.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/slackLists.items.info
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.slackLists.items.info
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.slackLists_items_info
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().slackListsItemsInfo
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

**`list_id`**`string`Required

ID of the List.

_Example:_ `F1234567`

**`id`**`string`Required

ID of the row to get.

_Example:_ `Rec014K005UQJ`

### Optional arguments

**`include_is_subscribed`**`boolean`Optional

Set to `true` to include `is_subscribed` data for the returned List row.

_Default:_ `false`

## Usage info {#usage-info}

Lists are only available to Slack workspaces on a paid plan.

This method allow you to get a row from a List.

## Sample requests data {#sample-requests-data}

### Minimal {#minimal}

```
{  "token": "***",  "list_id": "F1234567",  "id": "Rec1234567"}
```

### Include subscription flag {#subscription-flag}

```
{  "token": "***",  "list_id": "F1234567",  "include_is_subscribed": true,  "id": "Rec1234567"}
```

* * *

## Response {#response}

#### Typical success response: minimal

```
{  "ok": true,  "list": {    "id": "F1234567",    "created": 1758744341,    "timestamp": 1758744341,    "name": "list",    "title": "Sprint Board",    "mimetype": "application/vnd.slack-list",    "filetype": "list",    "pretty_type": "List",    "user": "W0AB1CDE2",    "user_team": "E0AB1CD2E",    "editable": true,    "size": 0,    "mode": "list",    "is_external": false,    "external_type": "",    "is_public": false,    "public_url_shared": false,    "display_as_bot": false,    "username": "",    "list_metadata": {      "schema": [        {          "id": "Col018AL7648J",          "name": "Title",          "key": "title",          "type": "text",          "is_primary_column": true        },        {          "id": "Col018B8C91TM",          "name": "Notes",          "key": "rich_text_notes",          "type": "rich_text",          "is_primary_column": false        },        {          "id": "Col018AL76490",          "name": "Message",          "key": "message_link",          "type": "message",          "is_primary_column": false        },        {          "id": "Col018B8C91U3",          "name": "Estimate",          "key": "estimate",          "type": "number",          "is_primary_column": false,          "options": {            "precision": 2,            "show_member_name": true          }        },        {          "id": "Col018AL7649G",          "name": "Status",          "key": "status",          "type": "select",          "is_primary_column": false,          "options": {            "choices": [              {                "value": "not_started",                "label": "Not Started",                "color": "red"              },              {                "value": "in_progress",                "label": "In Progress",                "color": "yellow"              },              {                "value": "completed",                "label": "Completed",                "color": "green"              }            ],            "format": "single_select",            "show_member_name": true          }        },        {          "id": "Col018B8C91UK",          "name": "Labels",          "key": "labels",          "type": "multi_select",          "is_primary_column": false,          "options": {            "choices": [              {                "value": "p0",                "label": "P0",                "color": "red"              },              {                "value": "p1",                "label": "P1",                "color": "yellow"              },              {                "value": "p2",                "label": "P2",                "color": "green"              }            ],            "format": "multi_select",            "show_member_name": true          }        },        {          "id": "Col018AL764AE",          "name": "Date",          "key": "date",          "type": "date",          "is_primary_column": false        },        {          "id": "Col018B8C91V1",          "name": "Owner",          "key": "owner",          "type": "user",          "is_primary_column": false,          "options": {            "format": "single_entity",            "show_member_name": true          }        },        {          "id": "Col018AL764AW",          "name": "Attachments",          "key": "attachments",          "type": "attachment",          "is_primary_column": false        },        {          "id": "Col018B8C9203",          "name": "Ready?",          "key": "ready",          "type": "checkbox",          "is_primary_column": false        },        {          "id": "Col018AL764BC",          "name": "Email",          "key": "email",          "type": "email",          "is_primary_column": false        },        {          "id": "Col018B8C921H",          "name": "Phone",          "key": "phone",          "type": "phone",          "is_primary_column": false        },        {          "id": "Col018AL764G2",          "name": "Channel",          "key": "channel",          "type": "channel",          "is_primary_column": false        },        {          "id": "Col018B8C9259",          "name": "Rating",          "key": "rating",          "type": "rating",          "is_primary_column": false,          "options": {            "emoji": ":star:",            "max": 5,            "show_member_name": true          }        },        {          "id": "Col018AL77TH8",          "name": "Vote",          "key": "vote",          "type": "vote",          "is_primary_column": false        },        {          "id": "Col018B8D6Q91",          "name": "Assignee",          "key": "assignee",          "type": "assignee",          "is_primary_column": false        },        {          "id": "Col018AL83THQ",          "name": "Due Date",          "key": "due_date",          "type": "due_date",          "is_primary_column": false        },        {          "id": "Col018AL857QS",          "name": "Completed",          "key": "completed",          "type": "completed",          "is_primary_column": false        },        {          "id": "Col018B8D84R1",          "name": "Canvas",          "key": "canvas",          "type": "canvas",          "is_primary_column": false        },        {          "id": "Col018AL9577U",          "name": "Link",          "key": "link",          "type": "link",          "is_primary_column": false        }      ],      "views": [        {          "id": "View018B8E85S7",          "name": "Record",          "type": "record",          "is_locked": false,          "position": "1758744341",          "columns": [            {              "visible": true,              "key": "title",              "id": "Col018AL7648J",              "position": "5000000000"            },            {              "visible": true,              "key": "rich_text_notes",              "id": "Col018B8C91TM",              "position": "5000000001"            },            {              "visible": true,              "key": "message_link",              "id": "Col018AL76490",              "position": "5000000002"            },            {              "visible": true,              "key": "estimate",              "id": "Col018B8C91U3",              "position": "5000000003"            },            {              "visible": true,              "key": "status",              "id": "Col018AL7649G",              "position": "5000000004"            },            {              "visible": true,              "key": "labels",              "id": "Col018B8C91UK",              "position": "5000000005"            },            {              "visible": true,              "key": "date",              "id": "Col018AL764AE",              "position": "5000000006"            },            {              "visible": true,              "key": "owner",              "id": "Col018B8C91V1",              "position": "5000000007"            },            {              "visible": true,              "key": "attachments",              "id": "Col018AL764AW",              "position": "5000000008"            },            {              "visible": true,              "key": "ready",              "id": "Col018B8C9203",              "position": "5000000009"            },            {              "visible": true,              "key": "email",              "id": "Col018AL764BC",              "position": "5000000010"            },            {              "visible": true,              "key": "phone",              "id": "Col018B8C921H",              "position": "5000000011"            },            {              "visible": true,              "key": "channel",              "id": "Col018AL764G2",              "position": "5000000012"            },            {              "visible": true,              "key": "rating",              "id": "Col018B8C9259",              "position": "5000000013"            },            {              "visible": true,              "key": "vote",              "id": "Col018AL77TH8",              "position": "5000000014"            },            {              "visible": true,              "key": "assignee",              "id": "Col018B8D6Q91",              "position": "5000000015"            },            {              "visible": true,              "key": "due_date",              "id": "Col018AL83THQ",              "position": "5000000016"            },            {              "visible": true,              "key": "completed",              "id": "Col018AL857QS",              "position": "5000000017"            },            {              "visible": true,              "key": "canvas",              "id": "Col018B8D84R1",              "position": "5000000018"            },            {              "visible": true,              "key": "link",              "id": "Col018AL9577U",              "position": "5000000019"            }          ],          "date_created": 1758744341,          "created_by": "W0QR1STU2",          "stick_column_left": false,          "is_all_items_view": false        },        {          "id": "View018AL9598S",          "name": "All items",          "type": "table",          "is_locked": false,          "position": "1758744342",          "columns": [            {              "visible": true,              "key": "title",              "id": "Col018AL7648J",              "position": "5000000000"            },            {              "visible": true,              "key": "rich_text_notes",              "id": "Col018B8C91TM",              "position": "5000000001"            },            {              "visible": true,              "key": "message_link",              "id": "Col018AL76490",              "position": "5000000002"            },            {              "visible": true,              "key": "estimate",              "id": "Col018B8C91U3",              "position": "5000000003"            },            {              "visible": true,              "key": "status",              "id": "Col018AL7649G",              "position": "5000000004"            },            {              "visible": true,              "key": "labels",              "id": "Col018B8C91UK",              "position": "5000000005"            },            {              "visible": true,              "key": "date",              "id": "Col018AL764AE",              "position": "5000000006"            },            {              "visible": true,              "key": "owner",              "id": "Col018B8C91V1",              "position": "5000000007"            },            {              "visible": true,              "key": "attachments",              "id": "Col018AL764AW",              "position": "5000000008"            },            {              "visible": true,              "key": "ready",              "id": "Col018B8C9203",              "position": "5000000009"            },            {              "visible": true,              "key": "email",              "id": "Col018AL764BC",              "position": "5000000010"            },            {              "visible": true,              "key": "phone",              "id": "Col018B8C921H",              "position": "5000000011"            },            {              "visible": true,              "key": "channel",              "id": "Col018AL764G2",              "position": "5000000012"            },            {              "visible": true,              "key": "rating",              "id": "Col018B8C9259",              "position": "5000000013"            },            {              "visible": true,              "key": "vote",              "id": "Col018AL77TH8",              "position": "5000000014"            },            {              "visible": true,              "key": "assignee",              "id": "Col018B8D6Q91",              "position": "5000000015"            },            {              "visible": true,              "key": "due_date",              "id": "Col018AL83THQ",              "position": "5000000016"            },            {              "visible": true,              "key": "completed",              "id": "Col018AL857QS",              "position": "5000000017"            },            {              "visible": true,              "key": "canvas",              "id": "Col018B8D84R1",              "position": "5000000018"            },            {              "visible": true,              "key": "link",              "id": "Col018AL9577U",              "position": "5000000019"            }          ],          "date_created": 1758744342,          "created_by": "W0QR1STU2",          "stick_column_left": false,          "is_all_items_view": true,          "default_view_key": "all_items",          "show_completed_items": true        }      ],      "integrations": [],      "icon": "",      "description": "",      "description_blocks": [        {          "type": "rich_text",          "block_id": "XYcTZ",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "Sprint work"                }              ]            }          ]        }      ],      "is_trial": false,      "subtask_schema": [        {          "id": "Col018AL7648J",          "name": "Title",          "key": "title",          "type": "text",          "is_primary_column": true        }      ],      "creation_source": {        "type": "copy_from_list",        "reference_id": "F018AL98L3U"      },      "todo_mode": false,      "default_view": ""    },    "list_limits": {      "over_row_maximum": false,      "row_count_limit": 1000,      "row_count": 7,      "archived_row_count": 0,      "over_column_maximum": false,      "column_count": 20,      "column_count_limit": 30,      "over_view_maximum": false,      "view_count": 2,      "view_count_limit": 50,      "max_attachments_per_cell": 10    },    "url_private": "https://files.com/files-pri/T0AB1CD2E-F1234567/list",    "url_private_download": "https://files.com/files-pri/T0AB1CD2E-F1234567/download/list",    "permalink": "https://someenterpriseorg.slack.com/lists/T0ABCDEFG/F1234567",    "permalink_public": "https://files.com/T0AB1CD2E-F1234567-123ab4cd56",    "last_editor": "W0QR1STU2",    "list_csv_download_url": "https://files.com/files-pri/T0AB1CD2E-F1234567/csv/list",    "updated": 1758744347,    "is_starred": false,    "skipped_shares": true,    "teams_shared_with": [      "E0AB1CD2E"    ],    "is_restricted_sharing_enabled": false,    "has_rich_preview": false,    "file_access": "visible",    "access": "owner",    "org_or_workspace_access": "none",    "is_ai_suggested": false  },  "record": {    "id": "Rec018B8RR603",    "list_id": "F1234567",    "date_created": 1758744346,    "created_by": "W0QR1STU2",    "updated_by": "W0QR1STU2",    "fields": [],    "updated_timestamp": "1758744346"  },  "subtasks": []}
```

#### Typical success response: include subscription flag

```
{  "ok": true,  "list": {    "id": "F1234567",    "created": 1758744341,    "timestamp": 1758744341,    "name": "list",    "title": "Sprint Board",    "mimetype": "application/vnd.slack-list",    "filetype": "list",    "pretty_type": "List",    "user": "W0AB1CDE2",    "user_team": "E0AB1CD2E",    "editable": true,    "size": 0,    "mode": "list",    "is_external": false,    "external_type": "",    "is_public": false,    "public_url_shared": false,    "display_as_bot": false,    "username": "",    "list_metadata": {      "schema": [        {          "id": "Col018AL7648J",          "name": "Title",          "key": "title",          "type": "text",          "is_primary_column": true        },        {          "id": "Col018B8C91TM",          "name": "Notes",          "key": "rich_text_notes",          "type": "rich_text",          "is_primary_column": false        },        {          "id": "Col018AL76490",          "name": "Message",          "key": "message_link",          "type": "message",          "is_primary_column": false        },        {          "id": "Col018B8C91U3",          "name": "Estimate",          "key": "estimate",          "type": "number",          "is_primary_column": false,          "options": {            "precision": 2,            "show_member_name": true          }        },        {          "id": "Col018AL7649G",          "name": "Status",          "key": "status",          "type": "select",          "is_primary_column": false,          "options": {            "choices": [              {                "value": "not_started",                "label": "Not Started",                "color": "red"              },              {                "value": "in_progress",                "label": "In Progress",                "color": "yellow"              },              {                "value": "completed",                "label": "Completed",                "color": "green"              }            ],            "format": "single_select",            "show_member_name": true          }        },        {          "id": "Col018B8C91UK",          "name": "Labels",          "key": "labels",          "type": "multi_select",          "is_primary_column": false,          "options": {            "choices": [              {                "value": "p0",                "label": "P0",                "color": "red"              },              {                "value": "p1",                "label": "P1",                "color": "yellow"              },              {                "value": "p2",                "label": "P2",                "color": "green"              }            ],            "format": "multi_select",            "show_member_name": true          }        },        {          "id": "Col018AL764AE",          "name": "Date",          "key": "date",          "type": "date",          "is_primary_column": false        },        {          "id": "Col018B8C91V1",          "name": "Owner",          "key": "owner",          "type": "user",          "is_primary_column": false,          "options": {            "format": "single_entity",            "show_member_name": true          }        },        {          "id": "Col018AL764AW",          "name": "Attachments",          "key": "attachments",          "type": "attachment",          "is_primary_column": false        },        {          "id": "Col018B8C9203",          "name": "Ready?",          "key": "ready",          "type": "checkbox",          "is_primary_column": false        },        {          "id": "Col018AL764BC",          "name": "Email",          "key": "email",          "type": "email",          "is_primary_column": false        },        {          "id": "Col018B8C921H",          "name": "Phone",          "key": "phone",          "type": "phone",          "is_primary_column": false        },        {          "id": "Col018AL764G2",          "name": "Channel",          "key": "channel",          "type": "channel",          "is_primary_column": false        },        {          "id": "Col018B8C9259",          "name": "Rating",          "key": "rating",          "type": "rating",          "is_primary_column": false,          "options": {            "emoji": ":star:",            "max": 5,            "show_member_name": true          }        },        {          "id": "Col018AL77TH8",          "name": "Vote",          "key": "vote",          "type": "vote",          "is_primary_column": false        },        {          "id": "Col018B8D6Q91",          "name": "Assignee",          "key": "assignee",          "type": "assignee",          "is_primary_column": false        },        {          "id": "Col018AL83THQ",          "name": "Due Date",          "key": "due_date",          "type": "due_date",          "is_primary_column": false        },        {          "id": "Col018AL857QS",          "name": "Completed",          "key": "completed",          "type": "completed",          "is_primary_column": false        },        {          "id": "Col018B8D84R1",          "name": "Canvas",          "key": "canvas",          "type": "canvas",          "is_primary_column": false        },        {          "id": "Col018AL9577U",          "name": "Link",          "key": "link",          "type": "link",          "is_primary_column": false        }      ],      "views": [        {          "id": "View018B8E85S7",          "name": "Record",          "type": "record",          "is_locked": false,          "position": "1758744341",          "columns": [            {              "visible": true,              "key": "title",              "id": "Col018AL7648J",              "position": "5000000000"            },            {              "visible": true,              "key": "rich_text_notes",              "id": "Col018B8C91TM",              "position": "5000000001"            },            {              "visible": true,              "key": "message_link",              "id": "Col018AL76490",              "position": "5000000002"            },            {              "visible": true,              "key": "estimate",              "id": "Col018B8C91U3",              "position": "5000000003"            },            {              "visible": true,              "key": "status",              "id": "Col018AL7649G",              "position": "5000000004"            },            {              "visible": true,              "key": "labels",              "id": "Col018B8C91UK",              "position": "5000000005"            },            {              "visible": true,              "key": "date",              "id": "Col018AL764AE",              "position": "5000000006"            },            {              "visible": true,              "key": "owner",              "id": "Col018B8C91V1",              "position": "5000000007"            },            {              "visible": true,              "key": "attachments",              "id": "Col018AL764AW",              "position": "5000000008"            },            {              "visible": true,              "key": "ready",              "id": "Col018B8C9203",              "position": "5000000009"            },            {              "visible": true,              "key": "email",              "id": "Col018AL764BC",              "position": "5000000010"            },            {              "visible": true,              "key": "phone",              "id": "Col018B8C921H",              "position": "5000000011"            },            {              "visible": true,              "key": "channel",              "id": "Col018AL764G2",              "position": "5000000012"            },            {              "visible": true,              "key": "rating",              "id": "Col018B8C9259",              "position": "5000000013"            },            {              "visible": true,              "key": "vote",              "id": "Col018AL77TH8",              "position": "5000000014"            },            {              "visible": true,              "key": "assignee",              "id": "Col018B8D6Q91",              "position": "5000000015"            },            {              "visible": true,              "key": "due_date",              "id": "Col018AL83THQ",              "position": "5000000016"            },            {              "visible": true,              "key": "completed",              "id": "Col018AL857QS",              "position": "5000000017"            },            {              "visible": true,              "key": "canvas",              "id": "Col018B8D84R1",              "position": "5000000018"            },            {              "visible": true,              "key": "link",              "id": "Col018AL9577U",              "position": "5000000019"            }          ],          "date_created": 1758744341,          "created_by": "W0QR1STU2",          "stick_column_left": false,          "is_all_items_view": false        },        {          "id": "View018AL9598S",          "name": "All items",          "type": "table",          "is_locked": false,          "position": "1758744342",          "columns": [            {              "visible": true,              "key": "title",              "id": "Col018AL7648J",              "position": "5000000000"            },            {              "visible": true,              "key": "rich_text_notes",              "id": "Col018B8C91TM",              "position": "5000000001"            },            {              "visible": true,              "key": "message_link",              "id": "Col018AL76490",              "position": "5000000002"            },            {              "visible": true,              "key": "estimate",              "id": "Col018B8C91U3",              "position": "5000000003"            },            {              "visible": true,              "key": "status",              "id": "Col018AL7649G",              "position": "5000000004"            },            {              "visible": true,              "key": "labels",              "id": "Col018B8C91UK",              "position": "5000000005"            },            {              "visible": true,              "key": "date",              "id": "Col018AL764AE",              "position": "5000000006"            },            {              "visible": true,              "key": "owner",              "id": "Col018B8C91V1",              "position": "5000000007"            },            {              "visible": true,              "key": "attachments",              "id": "Col018AL764AW",              "position": "5000000008"            },            {              "visible": true,              "key": "ready",              "id": "Col018B8C9203",              "position": "5000000009"            },            {              "visible": true,              "key": "email",              "id": "Col018AL764BC",              "position": "5000000010"            },            {              "visible": true,              "key": "phone",              "id": "Col018B8C921H",              "position": "5000000011"            },            {              "visible": true,              "key": "channel",              "id": "Col018AL764G2",              "position": "5000000012"            },            {              "visible": true,              "key": "rating",              "id": "Col018B8C9259",              "position": "5000000013"            },            {              "visible": true,              "key": "vote",              "id": "Col018AL77TH8",              "position": "5000000014"            },            {              "visible": true,              "key": "assignee",              "id": "Col018B8D6Q91",              "position": "5000000015"            },            {              "visible": true,              "key": "due_date",              "id": "Col018AL83THQ",              "position": "5000000016"            },            {              "visible": true,              "key": "completed",              "id": "Col018AL857QS",              "position": "5000000017"            },            {              "visible": true,              "key": "canvas",              "id": "Col018B8D84R1",              "position": "5000000018"            },            {              "visible": true,              "key": "link",              "id": "Col018AL9577U",              "position": "5000000019"            }          ],          "date_created": 1758744342,          "created_by": "W0QR1STU2",          "stick_column_left": false,          "is_all_items_view": true,          "default_view_key": "all_items",          "show_completed_items": true        }      ],      "integrations": [],      "icon": "",      "description": "",      "description_blocks": [        {          "type": "rich_text",          "block_id": "XYcTZ",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "Sprint work"                }              ]            }          ]        }      ],      "is_trial": false,      "subtask_schema": [        {          "id": "Col018AL7648J",          "name": "Title",          "key": "title",          "type": "text",          "is_primary_column": true        }      ],      "creation_source": {        "type": "copy_from_list",        "reference_id": "F018AL98L3U"      },      "todo_mode": false,      "default_view": ""    },    "list_limits": {      "over_row_maximum": false,      "row_count_limit": 1000,      "row_count": 7,      "archived_row_count": 0,      "over_column_maximum": false,      "column_count": 20,      "column_count_limit": 30,      "over_view_maximum": false,      "view_count": 2,      "view_count_limit": 50,      "max_attachments_per_cell": 10    },    "url_private": "https://files.com/files-pri/T0AB1CD2E-F1234567/list",    "url_private_download": "https://files.com/files-pri/T0AB1CD2E-F1234567/download/list",    "permalink": "https://someenterpriseorg.slack.com/lists/T0RTANENP/F1234567",    "permalink_public": "https://files.com/T0AB1CD2E-F1234567-490eb8da78",    "last_editor": "W0QR1STU2",    "list_csv_download_url": "https://files.com/files-pri/T0AB1CD2E-F1234567/csv/list",    "updated": 1758744347,    "is_starred": false,    "skipped_shares": true,    "teams_shared_with": [      "E0AB1CD2E"    ],    "is_restricted_sharing_enabled": false,    "has_rich_preview": false,    "file_access": "visible",    "access": "owner",    "org_or_workspace_access": "none",    "is_ai_suggested": false  },  "record": {    "id": "Rec018B8RR603",    "list_id": "F1234567",    "date_created": 1758744346,    "created_by": "W0QR1STU2",    "updated_by": "W0QR1STU2",    "fields": [],    "updated_timestamp": "1758744346",    "is_subscribed": false  },  "subtasks": []}
```

#### Typical error response

```
{  "ok": false,  "error": "record_not_found"}
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

`record_deleted`

The record has been deleted.

`record_not_found`

The record was not found in the List.

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