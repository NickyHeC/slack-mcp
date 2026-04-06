Source: https://docs.slack.dev/reference/methods/admin.workflows.search

# admin.workflows.search method

DocsCall generator

## Facts {#facts}

**Description**Search workflows within the team or enterprise

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.workflows.search
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.workflows.search
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_workflows_search
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminWorkflowsSearch
```

**Scopes**

User token:

[`admin.workflows:read`](/reference/scopes/admin.workflows.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`query`**`string`Optional

A search query to filter for workflow name or description

_Example:_ `Time off`

**`app_id`**Optional

The parent app ID for which to return workflows

_Example:_ `A12345`

**`cursor`**`string`Optional

Set `cursor` to `next_cursor` returned by the previous call to list items in the next page

_Example:_ `dXNlcjpVMDYxTkZUVDI=`

**`limit`**`integer`Optional

The number of results that will be returned by the API on each invocation

_Default:_ `20`

_Example:_ `20`

**`no_collaborators`**`boolean`Optional

Only include workflows with no collaborators in the result; default is false

**`collaborator_ids`**`array`Optional

Only include workflows where all of the provided user IDs are a manager/collaborator of that workflow

**`num_trigger_ids`**`integer`Optional

Number of trigger IDs to fetch for each workflow; default is 10

_Default:_ `10`

**`is_sales_elevate`**`boolean`Optional

Filter workflows by their Sales Elevate status

**`source`**`string`Optional

Source of workflow creation, either from code or workflow builder

_Acceptable values:_ `code` `workflow_builder` `sales_home` `agent`

**`sort`**`string`Optional

The field used to sort the returned workflows

_Default:_ `name`

_Acceptable values:_ `name`

**`sort_dir`**`string`Optional

Sort direction. Possible values are `asc` for ascending order like (1, 2, 3) or (a, b, c), and `desc` for descending order like (3, 2, 1) or (c, b, a)

_Default:_ `desc`

_Acceptable values:_ `asc` `desc`

**`trigger_type_id`**`string`Optional

Only include workflows with this trigger type

**`publish_status`**`string`Optional

Filter workflows by their published status

_Default:_ `published`

_Acceptable values:_ `all` `published` `unpublished`

**`step_function_ids`**`array`Optional

Only include workflows that use all of the provided step function ids

## Usage info {#usage-info}

This method allows searching accross all workflows in the top-level team of the caller. It returns an array of all workflows in the org, letting you filter by app ID, name, etc.

Since workflows can have an unlimited number of triggers, there may be some cases where we may not be able to accurately report trigger information in the response. For example, if a workflow has hundreds of triggers, we are only able to populate response fields such as `trigger_types` or `trigger_ids` for a subset of those triggers. We provide the `num_trigger_ids` parameter to allow fetching more triggers but this is limited to a maxiumum value for performance reasons.

This method requires the caller having the permission to manage apps for the workspace or enterprise.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "total_found": 2,  "workflows": [    {      "id": "Wf014FQ97ZT5",      "workflow_function_id": "Fn014EPW7SBU",      "callback_id": "untitled_workflow",      "title": "Hello there",      "description": "A brand new workflow",      "input_parameters": {        "Ft014FQ980RZ__user_id": {          "type": "slack#/reference/objects/user-object_id",          "name": "Ft014FQ980RZ__user_id",          "description": "User who reacted to the message",          "title": "User who reacted to the message",          "is_required": false        },        "Ft014FQ980RZ__message_context": {          "type": "slack#/types/message_context",          "name": "Ft014FQ980RZ__message_context",          "description": "Reference to the message that was reacted to",          "title": "Reference to the message that was reacted to",          "is_required": true        }      },      "steps": [        {          "id": "a1468ed7-82a2-4d3a-8598-d67194a10148",          "function_id": "Fn010P",          "inputs": {            "message": {              "value": [                {                  "type": "rich_text",                  "elements": [                    {                      "type": "rich_text_section",                      "elements": [                        {                          "text": "Hello ",                          "type": "text"                        },                        {                          "id": "{{inputs.Ft014FQ980RZ__user_id}}",                          "type": "workflowtoken",                          "property": "",                          "data_type": "slack#/reference/objects/user-object_id"                        }                      ]                    }                  ]                }              ],              "locked": false            },            "message_context": {              "value": "{{inputs.Ft014FQ980RZ__message_context}}",              "locked": false            },            "reply_broadcast": {              "value": "false",              "locked": false            }          }        }      ],      "collaborators": [        "U014FM2DQF5"      ],      "icons": {        "image_96": "https://slack-pantry.dev.slack.com/11d89af/img/apps/workflows_96.png",        "image_192": "https://slack-pantry.dev.slack.com/11d89af/img/apps/workflows_192.png"      },      "is_published": true,      "last_updated_by": "U014FM2DQF5",      "unpublished_change_count": 0,      "app_id": "A014EPW7S3U",      "source": "workflow_builder",      "billing_type": "simple",      "date_updated": 1715661162,      "is_billable": false,      "creation_source_type": 1,      "creation_source_id": "Wt06DWT50W57",      "last_published_version_id": "Wfv014FQ9NHCK",      "last_published_date": "1674675746",      "trigger_ids": [        "Ft050QQ638NS"      ],      "is_sales_home_workflow": false,      "is_sales_elevate": false,      "trigger_types": [        {          "id": "Ftt0102",          "type": "event",          "subtype": "slack#/events/reaction_added"        }      ]    },    {      "id": "Wf014HH0GN9G",      "workflow_function_id": "Fn014HH0GN82",      "callback_id": "give_kudos_workflow",      "title": "Give kudos",      "description": "Acknowledge the impact someone had on you",      "input_parameters": {        "interactivity": {          "type": "slack#/types/interactivity",          "name": "interactivity",          "title": "Interactivity",          "is_required": true        }      },      "steps": [        {          "id": "0",          "function_id": "Fn010N",          "inputs": {            "title": {              "value": "Give someone kudos",              "locked": false            },            "fields": {              "value": {                "elements": [                  {                    "name": "doer_of_good_deeds",                    "type": "slack#/reference/objects/user-object_id",                    "title": "Whose deeds are deemed worthy of a kudo?",                    "description": "Recognizing such deeds is dazzlingly desirable of you!"                  },                  {                    "name": "kudo_channel",                    "type": "slack#/reference/objects/channel-object_id",                    "title": "Where should this message be shared?"                  },                  {                    "long": true,                    "name": "kudo_message",                    "type": "string",                    "title": "What would you like to say?"                  },                  {                    "enum": [                      "Appreciation for someone 🫂",                      "Celebrating a victory 🏆",                      "Thankful for great teamwork ⚽️",                      "Amazed at awesome work ☄️",                      "Excited for the future 🎉",                      "No vibes, just plants 🪴"                    ],                    "name": "kudo_vibe",                    "type": "string",                    "title": "What is this kudo's \"vibe\"?",                    "description": "What sorts of energy is given off?"                  }                ],                "required": [                  "doer_of_good_deeds",                  "kudo_channel",                  "kudo_message"                ]              },              "locked": false            },            "description": {              "value": "Continue the positive energy through your written word",              "locked": false            },            "submit_label": {              "value": "Share",              "locked": false            },            "interactivity": {              "value": "{{inputs.interactivity}}",              "locked": false            }          }        },        {          "id": "1",          "function_id": "Fn014JHDUP3M",          "inputs": {            "vibe": {              "value": "{{steps.0.fields.kudo_vibe}}",              "locked": false            }          }        },        {          "id": "2",          "function_id": "Fn0102",          "inputs": {            "message": {              "value": "*Hey <@{{steps.0.fields.doer_of_good_deeds}}>!* Someone wanted to share some kind words with you :otter:\n> {{steps.0.fields.kudo_message}}\n{{steps.1.URL}}",              "locked": false            },            "channel_id": {              "value": "{{steps.0.fields.kudo_channel}}",              "locked": false            }          }        }      ],      "collaborators": [        "U014ELP4Z9Q"      ],      "icons": {        "image_96": "https://example.com/avatars/2023-03-01/1153578567186_dd65b1ee58919c5d8665_96.png",        "image_192": "https://example.com/avatars/2023-03-01/1153578567186_dd65b1ee58919c5d8665_192.png"      },      "is_published": true,      "last_updated_by": "U014ELP4Z9Q",      "unpublished_change_count": 0,      "app_id": "A014HH0GN7L",      "source": "app",      "billing_type": "complex",      "date_updated": 1715661162,      "is_billable": true,      "creation_source_type": 1,      "creation_source_id": "Wt06DWT50W57",      "last_published_version_id": "Wfv014JHDUP4K",      "last_published_date": "1677682235",      "trigger_ids": [        "Ft0481M8V85R"      ],      "is_sales_home_workflow": false,      "is_sales_elevate": false,      "trigger_types": [        {          "id": "Ftt0101",          "type": "shortcut"        }      ]    }  ],  "response_metadata": {    "next_cursor": "aWQ6MTE1MzU3ODU2NjMyMg=="  }}
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

`invalid_cursor`

Value passed for `cursor` was not valid or is no longer valid.

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

The user is not allowed to access this API method.

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

`two_factor_setup_required`

Two factor setup is required.