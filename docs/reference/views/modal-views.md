Source: https://docs.slack.dev/reference/views/modal-views

# Modal views

Modal view objects are used within the following [Web API](/apis/web-api/) methods:

*   [`views.open`](/reference/methods/views.open)
*   [`views.update`](/reference/methods/views.update)
*   [`views.push`](/reference/methods/views.push)

Non-standard characters (including characters with diacritics) within view objects are converted and sent in unicode format when you receive the view callback payloads.

Preserving `input` entry in views

Data entered or selected in `input` blocks can be preserved while updating views. The new `view` that you use with `views.update` should contain the same input blocks and elements with identical `block_id` and `action_id` values.

## Modal view object fields {#modal-fields}

Field

Type

Description

Required?

`type`

String

The type of view. Set to `modal` for modals.

Required

`title`

Object

The title that appears in the top-left of the modal. Must be a [`plain_text` text element](/reference/block-kit/composition-objects/text-object) with a max length of 24 characters.

Required

`blocks`

Array

An array of [blocks](/reference/block-kit/blocks) that defines the content of the view. Max of 100 blocks.

Required

`close`

Object

A [`plain_text` element](/reference/block-kit/composition-objects/text-object) that defines the text displayed in the close button at the bottom-right of the view. Max length of 24 characters.

Optional

`submit`

Object

A [`plain_text` element](/reference/block-kit/composition-objects/text-object) that defines the text displayed in the submit button at the bottom-right of the view. `submit` is required when an `input` block is within the `blocks` array. Max length of 24 characters.

Optional

`private_metadata`

String

A string that will be sent to your app in `view_submission` and `block_actions` events. Max length of 3000 characters.

Optional

`callback_id`

String

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Max length of 255 characters.

Optional

`clear_on_close`

Boolean

When set to `true`, clicking on the `close` button will clear all views in a modal and close it. Defaults to `false`.

Optional

`notify_on_close`

Boolean

Indicates whether Slack will send your request URL a `view_closed` event when a user clicks the `close` button. Defaults to `false`.

Optional

`external_id`

String

A custom identifier that must be unique for all views on a per-team basis.

Optional

`submit_disabled`

Boolean

When set to `true`, disables the `submit` button until the user has completed one or more inputs. _This property is for [configuration modals](/changelog/2023-08-workflow-steps-from-apps-step-back)._

## Modal view example {#modal-view-example}

```
{    "type": "modal",    "title": {        "type": "plain_text",        "text": "Modal title"    },    "blocks": [        {            "type": "section",            "text": {                "type": "mrkdwn",                "text": "It's Block Kit...but _in a modal_"            },            "block_id": "section1",            "accessory": {                "type": "button",                "text": {                    "type": "plain_text",                    "text": "Click me"                },                "action_id": "button_abc",                "value": "Button value",                "style": "danger"            }        },        {            "type": "input",            "label": {                "type": "plain_text",                "text": "Input label"            },            "element": {                "type": "plain_text_input",                "action_id": "input1",                "placeholder": {                    "type": "plain_text",                    "text": "Type in here"                },                "multiline": false            },            "optional": false        }    ],    "close": {        "type": "plain_text",        "text": "Cancel"    },    "submit": {        "type": "plain_text",        "text": "Save"    },    "private_metadata": "Shhhhhhhh",    "callback_id": "view_identifier_12"}
```