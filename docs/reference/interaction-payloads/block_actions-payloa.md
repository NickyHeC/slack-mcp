Source: https://docs.slack.dev/reference/interaction-payloads/block_actions-payload

# block_actions payload

A `block_actions` payload is received when a user interacts with a [Block Kit interactive component](/reference/block-kit/block-elements).

Read our guide to [handling payloads from user interactions](/interactivity/handling-user-interaction#payloads) to learn how your app should process and respond to these payloads.

* * *

## Timing of payload dispatch {#payload_timing}

Different [interactive components](/reference/block-kit/block-elements) will cause an interaction payload to be sent at different moments:

Component

Payload sent

[`button`](/reference/block-kit/block-elements/button-element)

When the button is clicked.

[`checkboxes`](/reference/block-kit/block-elements/checkboxes-element)

When a checkbox is ticked or unticked.

[`datepicker`](/reference/block-kit/block-elements/date-picker-element)

When a date is chosen and the date picker closes.

[`multi_*_select`](/reference/block-kit/block-elements/multi-select-menu-element)

Each time an item is chosen from the multi-select menu.

[`overflow`](/reference/block-kit/block-elements/overflow-menu-element)

When an item from the overflow menu is clicked.

[`plain_text_input`](/reference/block-kit/block-elements/plain-text-input-element)

Determined by the `dispatch_action_config` field in the element.

[`radio`](/reference/block-kit/block-elements/radio-button-group-element)

When the selected radio in a group of radio buttons is changed.

[`*_select`](/reference/block-kit/block-elements/select-menu-element)

When an item is chosen from the select menu.

[`rich_text_input`](/reference/block-kit/block-elements/rich-text-input-element)

Determined by the `dispatch_action_config` field in the element.

Deselecting the currently selected option of a Block Kit static option will return a `null` value.

For more information about select menu elements, refer to [select menu of static options](/reference/block-kit/block-elements/select-menu-element).

To send this `block_actions` payload for [interactive components](/reference/block-kit/block-elements) used within [input blocks](/reference/block-kit/blocks/input-block), you can set `dispatch_action` to `true` in those input blocks.

They are included in [`view_submission` payloads](/reference/interaction-payloads/view-interactions-payload) as well.

## Properties {#fields}

This is a list of some properties that can be encountered in this type of interaction payload:

Properties received in a `block_actions` event may differ based on the source of the interactive elements.

A check in the column means that property is included in a `block_actions` event sent to a function, a non-function, or both. Functions refer to [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/guides/adding-interactivity).

Property

Functions

Non-Functions

Description

Required?

`type`

✓

✓

Helps identify which type of interactive component sent the payload; An interactive element in a block will have a type of `block_actions`, whereas an interactive element in a [message attachment](/legacy/legacy-messaging/legacy-secondary-message-attachments) will have a type of `interactive_message`.

Required

`trigger_id`

✓

✓

A short-lived ID that can be [used to open modals](/interactivity/handling-user-interaction#modal_responses).

Required

`user`

✓

✓

The user who interacted to trigger this request.

Required

`team`

✓

✓

The workspace the app is installed on. Null if the app is org-installed.

Required

`container`

✓

✓

The container where this block action took place.

Required

`api_app_id`

✓

✓

A string representing the app ID.

Required

`actions.block_id`

✓

✓

Identifies the block within a surface that contained the interactive component that was used. See the [reference guide for the block you're using](/reference/block-kit/blocks) for more info on the `block_id` field.

Required

`actions.action_id`

✓

✓

Identifies the interactive component itself. Some blocks can contain multiple interactive components, so the `block_id` alone may not be specific enough to identify the source component. See the [reference guide for the interactive element you're using](/reference/block-kit/block-elements) for more info on the `action_id` field.

Required

`actions.value`

✓

✓

Set by your app when you composed the blocks, this is the value that was specified in the interactive component when an interaction happened. For example, a select menu will have multiple possible values depending on what the user picks from the menu, and `value` will identify the chosen option. See the [reference guide for the interactive element you're using](/reference/block-kit/block-elements) for more info on the `value` field.

Required

`token`

✓

Represents a deprecated verification token feature. You should validate the request payload, however, and the best way to do so is to [use the signing secret provided to your app](/authentication/verifying-requests-from-slack).

Required

`hash`

✓

✓

A unique value that is optionally accepted in [`views.update`](/reference/methods/views.update) and [`views.publish`](/reference/methods/views.publish) API calls. When provided to those APIs, the `hash` is validated such that only the most recent view can be updated. This should be used to ensure the correct view is being updated when updates are happening asynchronously.

Required

`function_data`

✓

Metadata about the function execution that generated the block where this block action took place.

Required

`interactivity`

✓

An interactivity object generated as a result of the block action.

Required

`bot_access_token`

✓

A workflow (just-in-time) token generated for this block action.

Required

`enterprise`

✓

✓

The enterprise the installed app is part of, if the app is either workspace-installed on an org, or org-installed.

Optional

`channel`

✓

✓

The channel where this block action took place.

Optional

`message`

✓

✓

The message where this block action took place, if the block was contained in a message.

Optional

`view`

✓

✓

The view where this block action took place, if the block was contained in a view.

Optional

`actions`

✓

✓

Contains data from the specific [interactive component](/reference/block-kit/block-elements) that was used. [App surfaces](/surfaces) can contain [blocks](/reference/block-kit/blocks) with multiple interactive components, and each of those components can have multiple values selected by users.

Optional

`state`

✓

✓

A property including all stateful elements, not just input blocks.

Optional

`response_url`

✓

(Deprecated for apps created with the Deno Slack SDK) A short-lived [webhook](/messaging/sending-messages-using-incoming-webhooks) that can be used [to send messages in response to interactions](/interactivity/handling-user-interaction#message_responses).

Optional

If a user doesn't interact with a form field — for example, they don't select a value from a drop-down field on a modal — the value of that field is returned as `None`.

## Examples {#examples}

A payload from an interactive component used in a message:

```
{    "type": "block_actions",    "team": {        "id": "T9TK3CUKW",        "domain": "example"    },    "user": {        "id": "UA8RXUSPL",        "username": "jtorrance",        "team_id": "T9TK3CUKW"    },    "api_app_id": "AABA1ABCD",    "token": "9s8d9as89d8as9d8as989",    "container": {        "type": "message_attachment",        "message_ts": "1548261231.000200",        "attachment_id": 1,        "channel_id": "CBR2V3XEX",        "is_ephemeral": false,        "is_app_unfurl": false    },    "trigger_id": "12321423423.333649436676.d8c1bb837935619ccad0f624c448ffb3",    "channel": {        "id": "CBR2V3XEX",        "name": "review-updates"    },    "message": {        "bot_id": "BAH5CA16Z",        "type": "message",        "text": "This content can't be displayed.",        "user": "UAJ2RU415",        "ts": "1548261231.000200"    },    "response_url": "https://hooks.slack.com/actions/AABA1ABCD/1232321423432/D09sSasdasdAS9091209",    "actions": [        {            "action_id": "WaXA",            "block_id": "=qXel",            "text": {                "type": "plain_text",                "text": "View",                "emoji": true            },            "value": "click_me_123",            "type": "button",            "action_ts": "1548426417.840180"        }    ]}
```

A payload from an interactive component used in a Home tab:

```
{    "type": "block_actions",    "team": {        "id": "T9TK3CUKW",        "domain": "example"    },    "user": {        "id": "UA8RXUSPL",        "username": "jtorrance",        "name": "jtorrance",        "team_id": "T9TK3CUKW"    },    "api_app_id": "AABA1ABCD",    "token": "9s8d9as89d8as9d8as989",    "container": {        "type": "view",        "view_id": "V0PKB1ZFV"    },    "trigger_id": "24571818370.22717085937.b9c7ca14b87be6b44ff5864edba8306f",    "view": {        "id": "V0PKB1ZFV",        "team_id": "T9TK3CUKW",        "type": "home",        "blocks": [            {                "type": "section",                "block_id": "8ZG",                "text": {                    "type": "mrkdwn",                    "text": "A stack of blocks for the sample Block Kit Home tab.",                    "verbatim": false                }            },            {                "type": "actions",                "block_id": "7fhg",                "elements": [                    {                        "type": "button",                        "action_id": "XRX",                        "text": {                            "type": "plain_text",                            "text": "Action A",                            "emoji": true                        }                    },                    {                        "type": "button",                        "action_id": "GFBew",                        "text": {                            "type": "plain_text",                            "text": "Action B",                            "emoji": true                        }                    }                ]            },            {                "type": "section",                "block_id": "6evU",                "text": {                    "type": "mrkdwn",                    "text": "And now it's slightly more complex.",                    "verbatim": false                }            }        ],        "private_metadata": "",        "callback_id": "",        "state": {            "values": {}        },        "hash": "1571318366.2468e46f",        "clear_on_close": false,        "notify_on_close": false,        "close": null,        "submit": null,        "previous_view_id": null,        "root_view_id": "V0PKB1ZFV",        "app_id": "AABA1ABCD",        "external_id": "",        "app_installed_team_id": "T9TK3CUKW",        "bot_id": "B0B00B00"    },    "actions": [        {            "type": "button",            "block_id": "7fhg",            "action_id": "XRX",            "text": {                "type": "plain_text",                "text": "Action A",                "emoji": true            },            "action_ts": "1571318425.267782"        }    ]}
```