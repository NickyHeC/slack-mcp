Source: https://docs.slack.dev/reference/views/home-tab-views

# Home tab views

The Home tab is available only for Bolt apps, not [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/). Home tab view objects are used within the [`views.publish`](/reference/methods/views.publish) [Web API](/apis/web-api/) method.

Non-standard characters (including characters with diacritics) within view objects are converted and sent in unicode format when you receive the view callback payloads.

Preserving `input` entry in views

Data entered or selected in `input` blocks can be preserved while updating views. The new `view` that you use with `views.update` should contain the same input blocks and elements with identical `block_id` and `action_id` values.

## Home tab view object fields {#home-fields}

Field

Type

Description

Required?

`type`

String

The type of view. Set to `home` for Home tabs.

Required

`blocks`

Array

An array of [blocks](/reference/block-kit/blocks) that defines the content of the view. Max of 100 blocks.

Required

`private_metadata`

String

A string that will be sent to your app in `view_submission` and `block_actions` events. Max length of 3000 characters.

Optional

`callback_id`

String

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Max length of 255 characters.

Optional

`external_id`

String

A custom identifier that must be unique for all views on a per-team basis.

Optional

## Home tab view example {#home-example}

```
{    "type": "home",    "blocks": [        {            "type": "section",            "text": {                "type": "mrkdwn",                "text": "A stack of blocks for the sample Block Kit Home tab."            }        },        {            "type": "actions",            "elements": [                {                    "type": "button",                    "text": {                        "type": "plain_text",                        "text": "Action A",                        "emoji": true                    }                },                {                    "type": "button",                    "text": {                        "type": "plain_text",                        "text": "Action B",                        "emoji": true                    }                }            ]        }    ]}
```