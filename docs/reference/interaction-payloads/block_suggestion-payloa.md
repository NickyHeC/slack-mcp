Source: https://docs.slack.dev/reference/interaction-payloads/block_suggestion-payload

# block_suggestion payloads

A `block_suggestion` payload is received when a user interacts with a [select menu of external data source](/reference/block-kit/block-elements/select-menu-element) element. Users may return a maximum of 100 options or option groups when handling the `block_suggestion` payload.

Read our guide to [handling payloads from user interactions](/interactivity/handling-user-interaction#payloads) to learn how your app should process and respond to these payloads.

## Properties {#properties}

This is a list of the properties that can be encountered in this type of interaction payload:

Properties received in a `block_suggestion` event may differ based on the source of the interactive elements—a modal view, message, or home tab surface.

A check in the column means that property is included in a `block_suggestion` event sent to a function, a non-function, or both. Functions refer to apps created with the Deno Slack SDK; refer to [Interactivity overview](/tools/deno-slack-sdk/guides/adding-interactivity) for more information.

Property

Functions

Non-Functions

Description

Required?

`user`

✓

✓

Details for the user that initiated the block suggestion interaction. The `user.team_id` will report an enterprise organization ID (which starts with an `E`) instead of team ID (which starts with a `T`), when using an Enterprise organization.

Required

`team`

✓

✓

The workspace, or team, details the Block Kit interaction originated from. In the case of an Enterprise organization, `team` can also have the properties `enterprise_id` and `enterprise_name`, which represent the ID and the name of the org, respectively.

Required

`api_app_id`

✓

✓

The encoded application ID the event was dispatched to, e.g. A123456.

Required

`block_id`

✓

✓

Identifies the block within a surface that contained the interactive component that was used. See the [reference guide for the block you're using](/reference/block-kit/blocks) for more info on the `block_id` field.

Required

`action_id`

✓

✓

Identifies the interactive component itself. Some blocks can contain multiple interactive components, so the `block_id` alone may not be specific enough to identify the source component. See the [reference guide for the interactive element you're using](/reference/block-kit/block-elements) for more info on the `action_id` field.

Required

`function_data`

✓

Metadata about the function execution that generated the block where this block suggestion took place.

Required

`bot_access_token`

✓

A workflow (just-in-time) token generated for this block suggestion.

Required

`enterprise`

✓

✓

The enterprise the installed app is part of, if the app is either workspace-installed on an org, or org-installed.

Optional

`channel`

✓

✓

The channel the block suggestion interaction originated from.

Optional

`message`

✓

✓

The message where this block suggestion took place, if the block was contained in a message.

Optional

`view`

✓

✓

The view where this block suggestion took place, if the block was contained in a view.

Optional

`value`

✓

✓

The value the user entered into the select menu.

Required

## Examples {#examples}

A payload from a block suggestion component used in a modal view:

```
{    "type": "block_suggestion",    "team": {        "id": "ABC123DEF45",        "domain": "workspace"    },    "enterprise": null,    "user": {        "id": "EXAMPLE1234",        "name": "sallyslack",        "team_id": "ABC123DEF45"    },    "view": {        "id": "DEFGHIJ89101",        "team_id": "ABC123DEF45",        "app_id": "APPID6789101",        "app_installed_team_id": "ABC123DEF45",        "bot_id": "BOTSRCOOL12",        "title": {            "type": "plain_text",            "text": "Deny Request",            "emoji": true        },        "type": "modal",        "blocks": [            /* ... your view blocks here */        ],        "close": null,        "submit": {            "type": "plain_text",            "text": "Next",            "emoji": true        },        "state": {            "values": {}        },        "hash": "1695235327.610lSjjQ",        "private_metadata": "{\"messageTS\":\"1695235212.424669\"}",        "callback_id": "deny_modal_main",        "root_view_id": "DEFGHIJ89101",        "previous_view_id": null,        "clear_on_close": false,        "notify_on_close": true,        "external_id": ""    },    "container": {        "type": "view",        "view_id": "DEFGHIJ89101"    },    "api_app_id": "APPID6789101",    "action_id": "ext_select_input",    "block_id": "ext_select_block",    "value": "tech",    "function_data": {        "execution_id": "EXECUTEF9101",        "function": {            "callback_id": "review_approval"        },        "inputs": {            "details": "test",            "subject": "test",            "requester_id": "EXAMPLE1234",            "approval_channel_id": "APPROVE1234"        }    },    "bot_access_token": "xwfp-2335208212870-2354592155553-5925491402867-c2a66a8fb377b19e0d8f6c8d24af530d"}
```

A payload from suggestion component used in a message from a workspace using an Enterprise organization:

```
{    "type": "block_suggestion",    "user": {        "id": "ABCDE6789",        "username": "harry-potter",        "name": "harry-potter",        "team_id": "ENT4567"    },    "container": {        "type": "message",        "message_ts": "1628851405.000300",        "channel_id": "CHAN56789",        "is_ephemeral": false    },    "api_app_id": "APP876543",    "token": "XAg1RqiO8jaSczkIQpxq7Z4o",    "action_id": "location_select-action",    "block_id": "bK6",    "value": "test",    "team": {        "id": "ENT4567",        "domain": "my-workspace",        "enterprise_id": "ENT123789",        "enterprise_name": "my-enterprise"    },    "enterprise": {        "id": "ENT123789",        "name": "my-enterprise"    },    "is_enterprise_install": false,    "channel": {        "id": "CHAN56789",        "name": "channel-team-01"    },    "message": {        "bot_id": "B0T123456",        "type": "message",        "text": "Text+here+for+notifications",        "user": "ABCDE6789",        "ts": "1628851405.000300",        "blocks": [            {                "type": "input",                "block_id": "bK6",                "label": {                    "type": "plain_text",                    "text": "Select+Location",                    "emoji": true                },                "optional": false,                "dispatch_action": false,                "element": {                    "type": "external_select",                    "action_id": "location_select-action",                    "placeholder": {                        "type": "plain_text",                        "text": "Select+location",                        "emoji": true                    }                }            }        ],        "team": "ENT4567"    }}
```