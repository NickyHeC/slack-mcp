Source: https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload

# View interaction payloads

There are different types of payloads that can be received when users interact with [modal views](/surfaces/modals#views):

*   [`view_submission`](#view_submission)
*   [`view_closed`](#view_closed)

## view_submission payloads {#view_submission}

Sent to an app's [configured Request URL](/interactivity/handling-user-interaction#setup) when a user submits a [view in a modal](/surfaces/modals#views).

Read [our guide to using modals](/surfaces/modals#handling_submissions) to learn how your app should process and respond to these payloads.

If you're using our Bolt framework, we have additional guidance on how to utilize the `view_submission` payload:

*   [Bolt JS](/tools/bolt-js/concepts/view-submissions)
*   [Bolt Python](/tools/bolt-python/concepts/view-submissions)
*   [Bolt Java](/tools/java-slack-sdk/guides/modals)

* * *

### Properties {#view_submission_fields}

This is a list of some properties that can be encountered in this type of interaction payload:

Properties received in a `view_submission` event may differ based on the source of the interactive elements.

A check in the column means that property is included in a `view_submission` event sent to a function, a non-function, or both. Functions refer to [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/guides/adding-interactivity).

Property

Functions

Non-Functions

Description

Required?

`type`

✓

✓

Identifies the source of the payload. The `type` for this interaction is `view_submission`.

Required

`team`

✓

✓

The [workspace](/reference/methods/team.info) where the view was submitted from. Null if the app is org-installed.

Required

`user`

✓

✓

The user who interacted to trigger this request.

Required

`view`

✓

✓

The source [view](/surfaces/modals#views) of the modal the user submitted.

Required

`enterprise`

✓

✓

The enterprise that the installed app is a part of, if the app is either workspace-installed on an org, or org-installed.

Required

`api_app_id`

✓

✓

A string representing the app ID.

Required

`function_data`

✓

Metadata about the function execution that generated the view where this view submission took place.

Required

`interactivity`

✓

An interactivity object generated as a result of the view submission.

Required

`bot_access_token`

✓

A workflow (just-in-time) token generated for this view submission.

Required

`view.state.values`

✓

✓

A dictionary of objects. Each object represents a block in the source view that contained [stateful, interactive components](/messaging). Objects are keyed by the `block_id` of those blocks. These objects each contain a child object. The child object is keyed by the `action_id` of the interactive element in the block. This final child object will contain the `type` and submitted `value` of the input block element.

Optional

`hash`

✓

✓

A unique value that is optionally accepted in [`views.update`](/reference/methods/views.update) and [`views.publish`](/reference/methods/views.publish) API calls. When provided to those APIs, the `hash` is validated such that only the most recent view can be updated. This should be used to ensure the correct view is being updated when updates are happening asynchronously.

Optional

`response_urls`

✓

(Deprecated for apps created with the Deno Slack SDK) An array of objects that contain `response_url` values, used to [send message responses](/interactivity/handling-user-interaction#message_responses). Each object will also contain `block_id` and `action_id` values to identify the source of the interaction. Also included is a `channel_id` which identifies where the `response_url` will publish to. `response_urls` is available only when the view contained block elements configured to generate a [response\_url](/surfaces/modals#modal_response_url).

Optional

* * *

### Example {#view_submission_example}

This is an example `view_submission` payload:

```
{    "type": "view_submission",    "team": {        "id": "T1234567",        "domain": "example-domain"    },    "user": {        "id": "U1234567",        "username": "example-user"    },    "view": {        "id": "VNHU13V36",        "type": "modal",        "title": {            "type": "plain_text",            "text": "Modal Title"        },        "submit": {            "type": "plain_text",            "text": "Submit"        },        "blocks": [],        "private_metadata": "shhh-its-secret",        "callback_id": "modal-with-inputs",        "state": {            "values": {                "multiline": {                    "mlvalue": {                        "type": "plain_text_input",                        "value": "This is my example inputted value"                    }                },                "target_channel": {                    "target_select": {                        "type": "conversations_select",                        "selected_conversation": "C123B12DE"                    }                }            }        },        "hash": "156663117.cd33ad1f",        "response_urls": [            {                "block_id": "target_channel",                "action_id": "target_select",                "channel_id": "C123B12DE",                "response_url": "https://hooks.slack.com/app/ABC12312/1234567890/A100B100C100d100"            }        ]    }}
```

This was generated from the submission of this example view:

```
{    "view": {        "type": "modal",        "callback_id": "modal-with-inputs",        "title": {            "type": "plain_text",            "text": "Modal with inputs"        },        "blocks": [            {                "type": "input",                "block_id": "multiline",                "label": {                    "type": "plain_text",                    "text": "Enter your value"                },                "element": {                    "type": "plain_text_input",                    "multiline": true,                    "action_id": "mlvalue"                }            },            {                "block_id": "target_channel",                "type": "input",                "optional": true,                "label": {                    "type": "plain_text",                    "text": "Select a channel to post the result on"                },                "element": {                    "action_id": "target_select",                    "type": "conversations_select",                    "response_url_enabled": true                }            }        ],        "submit": {            "type": "plain_text",            "text": "Submit"        }    }}
```

* * *

## view_closed payloads {#view_closed}

Optionally sent to an app's [configured Request URL](/interactivity/handling-user-interaction#setup) when a user dismisses a [modal](/surfaces/modals). To receive these payloads, the modal view must [have been created](/surfaces/modals#composing_views) with the [`notify_on_close` argument set to `true`](/reference/views#reference-guide-defining-view-objects__fields).

Read [our guide to using modals](/surfaces/modals#modal_cancellations) to learn how your app should process and respond to these payloads.

### Fields {#fields}

Field

Description

`type`

Helps identify the source of the payload. The `type` for this interaction is `view_closed`.

`team`

The [workspace](/reference/methods/team.info) that the interaction happened in.

`user`

The user who dismissed a modal to trigger this request.

`view`

The source [modal view](/surfaces/modals#views) that the user dismissed. This will include the full state of the view, excluding any [input blocks](/reference/block-kit/blocks/input-block) in the modal.

`is_cleared`

A boolean that represents whether or not a whole [view stack](/surfaces/modals#view_stack) was cleared.

### Example {#example}

```
{    "type": "view_closed",    "team": {        "id": "TXXXXXX",        "domain": "coverbands"    },    "user": {        "id": "UXXXXXX",        "name": "dreamweaver"    },    "view": {        "id": "VXXXXXX",        "type": "modal",        "title": {            "type": "plain_text",            "text": "Modal Title"        },        "blocks": []    },    "api_app_id": "AXXXXXX",    "is_cleared": false}
```