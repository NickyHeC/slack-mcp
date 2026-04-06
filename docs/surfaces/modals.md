Source: https://docs.slack.dev/surfaces/modals

# Modals

A modal is the Slack app equivalent of an alert box, pop-up, or dialog box. Modals capture and maintain focus within Slack until the user submits or dismisses the modal. This makes them a powerful piece of app functionality for engaging with users. Modals are available for both Bolt apps and Deno Slack SDK apps.

You can use modals with other app surfaces such as [messages](/messaging) and [Home tabs](/surfaces/app-home).

For example, you could have an app present a task dashboard that resides in the app's Home tab. A user clicks a [button](/reference/block-kit/block-elements/button-element) to add a task, and is presented with a modal to [input](/reference/block-kit/blocks/input-block) some [plain text](/reference/block-kit/block-elements/plain-text-input-element) and [select from a list of categories](/reference/block-kit/block-elements/select-menu-element). Upon submitting, a [message](/messaging) is sent to a triage channel in the Slack workspace, where another user can click a button to claim the task.

![](/assets/images/modal-abstract-f84c7b1e74a116b1376d94dd07121db0.png)

Each modal consists of some standardized UI elements — a title, an _x_ button to dismiss the modal, a _cancel_ button — that wrap around a focused space, known as the modal's **view**.

[View in Block Kit Builder](https://api.slack.com/block-kit-builder?blocks=%5B%7B"type"%3A"input"%2C"element"%3A%7B"type"%3A"plain_text_input"%2C"action_id"%3A"sl_input"%2C"placeholder"%3A%7B"type"%3A"plain_text"%2C"text"%3A"Placeholder%20text%20for%20single-line%20input"%7D%7D%2C"label"%3A%7B"type"%3A"plain_text"%2C"text"%3A"Label"%7D%2C"hint"%3A%7B"type"%3A"plain_text"%2C"text"%3A"Hint%20text"%7D%7D%2C%7B"type"%3A"input"%2C"element"%3A%7B"type"%3A"plain_text_input"%2C"action_id"%3A"ml_input"%2C"multiline"%3Atrue%2C"placeholder"%3A%7B"type"%3A"plain_text"%2C"text"%3A"Placeholder%20text%20for%20multi-line%20input"%7D%7D%2C"label"%3A%7B"type"%3A"plain_text"%2C"text"%3A"Label"%7D%2C"hint"%3A%7B"type"%3A"plain_text"%2C"text"%3A"Hint%20text"%7D%7D%5D&mode=modal)

![](/assets/images/modal-inputs-10132556d29246e382b001ee15266946.png)

To generate a modal, an app will compose an initial view. Apps can compose view layouts and add interactivity to views using [Block Kit](/block-kit).

A modal can hold up to 3 views at a time in a **view stack**. There is only ever a single view visible at a given moment, but the view stack can retain previous views, returning to them with their prior state still intact. An app can push new views onto a modal's view stack, or update an existing view within that stack — including the currently visible view.

If you've used our outmoded dialogs in your apps, check out our [guide to upgrading dialogs to modals](/block-kit/upgrading-outmoded-dialogs-to-modals).

* * *

## Understanding the lifecycle of a modal {#lifecycle}

In the beginning, there was a user interaction.

Interactions happen with one of an app's [entry points](/interactivity). As a result, the app is sent an [interaction payload](/reference/interaction-payloads) containing a special [`trigger_id`](/interactivity/handling-user-interaction#modal_responses). The app then composes an initial view (view A in the diagram below).

![A diagram explaining the view stack through the lifecycle of a modal](/assets/images/modal-view-stack-0a9f18c577268e2c8ad9f62f3ac7b3cf.png)

The user [interacts](/interactivity) with an [interactive component](/block-kit#making-things-interactive) in view A. This sends another [interaction payload](/reference/interaction-payloads) to the app. The app uses the context from this new payload to [update the currently visible view A](#updating_views) with additional content.

The user interacts with another interactive component in view A, and another interaction payload is sent to the app. The app uses the context from the new payload to [push a new view (view B) on to the modal's view stack](#adding_views), causing it to appear to the user immediately. View A remains in the view stack, but is no longer visible or active. The user enters some values into [input blocks](#gathering_user_input) in view B, and clicks the view's submit button. This sends a [different type of interaction payload](#interactions) to the app.

The app [handles the view submission and responds](#interactions) by [clearing the view stack](#close_all_views).

As described above, the view stack can be manipulated in a few ways over the course of a modal's lifetime:

*   [**Updating a view**](#updating_views). This can happen at any time while the modal is open. Updates can change the contents and layout of the view. A view update should normally only happen in response to the use of interactive components or [inputs](#gathering_input) gathered in the view.
*   [**Adding a new view.**](#adding_views) Apps can [push a new view onto the modal's view stack](#adding_views). This causes the new view to immediately become visible. Three views can exist in the view stack at any one time. Again, pushing a new view should normally only happen in response to the use of interactive components or [inputs](#gathering_input) gathered in one of the previous views.
*   [**Closing a view.**](#closing_views) When a view contains [inputs](#gathering_input), users can submit the modal when that view is visible. The app can then either [close that specific view](#closing_views) or [all views in the view stack](#close_all_views). Closing a single view removes it from the view stack and causes the next view in the stack to appear again. Closing all views will close the modal entirely.

### Gathering user input {#gathering_input}

In order to capture user input, a special type of [Block Kit component](/block-kit) is available called an [**input block**](/reference/block-kit/blocks/input-block). An input block can hold a [plain-text input](/reference/block-kit/block-elements/plain-text-input-element), a [select menu](/reference/block-kit/block-elements/select-menu-element), or a [multi-select menu](/reference/block-kit/block-elements/multi-select-menu-element). Plain-text inputs can be set to accept single or multi-line text. See the full input block definition in the [input block reference](/reference/block-kit/blocks/input-block).

If you're using any [input blocks](/reference/block-kit/blocks/input-block), you must include the [`submit` field when defining your view](#composing_views).

## Preparing your app {#preparing_for_modals}

Before we begin, if you don't already have a Slack app, click the following button to create one:

[Create an app](https://api.slack.com/apps?new_app=1)

You'll also need an [access token](/authentication/tokens) — read our [guide to app distribution](/app-management/distribution) to see how you can generate one. And, you'll need to enable _Interactive Components_ in your app's management dashboard. We explain all about how to enable these settings, what interaction payloads and request URLs are, and how to handle interactivity in our [guide to handling user interaction](/interactivity/handling-user-interaction).

Alternatively, you could create a workflow with the [quickstart guide](/tools/deno-slack-sdk/guides/getting-started).

## Composing modal views {#composing_views}

Before opening a modal, you'll need to define a view object to structure the layout of the initial view. The view object is a JSON object that defines the content populating this initial view and some version of metadata about the modal itself.

### Defining modal view objects {#defining-view-objects}

Modal view objects are used within the following [Web API](/apis/web-api/) methods:

*   [`views.open`](/reference/methods/views.open)
*   [`views.update`](/reference/methods/views.update)
*   [`views.push`](/reference/methods/views.push)

#### Modal view object fields {#view-object-fields}

Field

Type

Description

`type`

String

Required. The type of view. Set to `modal` for modals.

`title`

Object

Required. The title that appears in the top-left of the modal. Must be a [`plain_text` text element](/reference/block-kit/composition-objects/text-object) with a max length of 24 characters.

`blocks`

Array

Required. An array of [blocks](/reference/block-kit/blocks) that defines the content of the view. Max of 100 blocks.

`close`

Object

An optional [`plain_text` element](/reference/block-kit/composition-objects/text-object) that defines the text displayed in the close button at the bottom-right of the view. Max length of 24 characters.

`submit`

Object

An optional [`plain_text` element](/reference/block-kit/composition-objects/text-object) that defines the text displayed in the submit button at the bottom-right of the view. `submit` is required when an `input` block is within the `blocks` array. Max length of 24 characters.

`private_metadata`

String

An optional string that will be sent to your app in `view_submission` and `block_actions` events. Max length of 3000 characters.

`callback_id`

String

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Max length of 255 characters.

`clear_on_close`

Boolean

When set to `true`, clicking on the `close` button will clear all views in a modal and close it. Defaults to `false`.

`notify_on_close`

Boolean

Indicates whether Slack will send your request URL a `view_closed` event when a user clicks the `close` button. Defaults to `false`.

`external_id`

String

A custom identifier that must be unique for all views on a per-team basis.

`submit_disabled`

Boolean

When set to `true`, disables the `submit` button until the user has completed one or more inputs. _This property is for [configuration modals](/changelog/2023-08-workflow-steps-from-apps-step-back)._

If you use non-standard characters (including characters with diacritics), please be aware that these are converted and sent in unicode format when you receive the view callback payloads.

Preserving `input` entry in views

Data entered or selected in `input` blocks can be preserved while updating views. The new `view` that you use with `views.update` should contain the same input blocks and elements with identical `block_id` and `action_id` values.

#### Example {#example}

Below is a full modal view example. We'll construct this piece by piece in the following sections.

```
{  "type": "modal",  "title": {    "type": "plain_text",    "text": "Modal title"  },  "blocks": [    {      "type": "section",      "text": {        "type": "mrkdwn",        "text": "It's Block Kit...but _in a modal_"      },      "block_id": "section1",      "accessory": {        "type": "button",        "text": {          "type": "plain_text",          "text": "Click me"        },        "action_id": "button_abc",        "value": "Button value",        "style": "danger"      }    },    {      "type": "input",      "label": {        "type": "plain_text",        "text": "Input label"      },      "element": {        "type": "plain_text_input",        "action_id": "input1",        "placeholder": {          "type": "plain_text",          "text": "Type in here"        },        "multiline": false      },      "optional": false    }  ],  "close": {    "type": "plain_text",    "text": "Cancel"  },  "submit": {    "type": "plain_text",    "text": "Save"  },  "private_metadata": "Shh",  "callback_id": "view_identifier_12"}
```

The layout of a view is composed using [Block Kit](/block-kit)'s visual and interactive components — including special input blocks to gather user input.

![An example of a modal across iOS, Web, and Android](/assets/images/modal-clients-09930b306c03153dab796b6583c3dcc1.png)

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Modal%20title%22%7D,%22submit%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Submit%22%7D,%22type%22:%22modal%22,%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22It's%20Block%20Kit...but%20_in%20a%20modal_%22%7D,%22block_id%22:%22section1%22%7D%5D,%22private_metadata%22:%22Shhhhhhhh%22,%22callback_id%22:%22view_identifier_12%22%7D)

These visual components are all contained within the `blocks` field in your view object. Read our [comprehensive guide to composing layouts with Block Kit](/block-kit) to see how the `blocks` array should be formed.

When creating a view, set a unique `block_id` for each block and a unique `action_id` for each block element. This will make it much easier to track the possible values of those block elements when they are [returned in `view_submission` payloads](/reference/interaction-payloads/view-interactions-payload#view_submission).

If you're using any [input blocks](/reference/block-kit/blocks/input-block), you must include a `submit` field in your view object.

Once you've created your `blocks` layout, you need to add it to your `view` object payload. Here's an example `view` that we'll use:

```
{  "type": "modal",  "callback_id": "modal-identifier",  "title": {    "type": "plain_text",    "text": "Just a modal"  },  "blocks": [    {      "type": "section",      "block_id": "section-identifier",      "text": {        "type": "mrkdwn",        "text": "*Welcome* to ~my~ Block Kit _modal_!"      },      "accessory": {        "type": "button",        "text": {          "type": "plain_text",          "text": "Just a button",        },        "action_id": "button-identifier",      }    }  ],}
```

Your modal's initial view is now ready for use.

## Opening modals {#opening_modals}

To open a new modal, your app _must_ possess a valid, unexpired `trigger_id`, obtained from an [interaction payload](/interactivity/handling-user-interaction#payloads). Your app will receive one of these payloads, and therefore a `trigger_id`, after a user invokes one of the [app's entry points](/interactivity). If your app doesn't have one of these [entry point features](/interactivity) enabled, the app will not be able to open a modal. The `trigger_id` requirement ensures that modals only appear when apps have the express permission of a user.

A `trigger_id` will expire 3 seconds after it's sent to your app, so you’ll want to use it quickly.

Once in possession of a `trigger_id`, your app can call [`views.open`](/reference/methods/views.open) with the `view` payload you [created above](#composing_views):

```
POST https://slack.com/api/views.openContent-type: application/jsonAuthorization: Bearer YOUR_ACCESS_TOKEN_HERE{  "trigger_id": "156772938.1827394",  "view": {    "type": "modal",    "callback_id": "modal-identifier",    "title": {      "type": "plain_text",      "text": "Just a modal"    },    "blocks": [      {        "type": "section",        "block_id": "section-identifier",        "text": {          "type": "mrkdwn",          "text": "*Welcome* to ~my~ Block Kit _modal_!"        },        "accessory": {          "type": "button",          "text": {            "type": "plain_text",            "text": "Just a button"          },          "action_id": "button-identifier"        }      }    ]  }}
```

This will open a new modal, and display the view you composed within it. If the view was opened successfully, your app will [receive a response](/reference/methods/views.open#response) containing an `ok` value set to `true`, along with the view object that was displayed to the user. There's an example response in the [`views.open`](/reference/methods/views.open#response) reference.

When you receive this success response, you'll want to store the `view.id` from it for safekeeping. This will allow you to [update the contents of that view](#updating_views) later on.

* * *

## Handling and responding to interactions {#interactions}

Depending on how [your modal's initial view was composed](#composing_views), there are a few different interactions that could happen:

*   **`block_actions` payloads.** When someone uses an [interactive component](/reference/block-kit/block-elements) in your app's views, the app receives a [`block_actions`](/reference/interaction-payloads/block_actions-payload) payload. This **does not** apply to components included in an [`input`](/reference/block-kit/blocks/input-block) block (see below for details about those). Once processed, the information in the `block_actions` payload can be used to respond to the interaction.
*   **`view_submission` payloads.** When a view is submitted, you'll receive a [`view_submission` payload](/reference/interaction-payloads/view-interactions-payload#view_submission). This payload will contain a `state` object with the values and contents of any stateful blocks that were in the submitted view. Refer to the info on [`view.state.values`](/reference/interaction-payloads/view-interactions-payload#view_submission_fields) of the `view_submission` payload to understand the structure of this `state` object. As with `block_actions` payloads, the information in `view_submission` payloads can be used to respond.
*   **`view_closed` payloads.** Your app can optionally receive [`view_closed`](/reference/interaction-payloads/view-interactions-payload#view_closed) payloads whenever a user clicks on the _Cancel_ or _x_ buttons. These buttons are standard in all app modals. To receive the `view_closed` payload when this happens, set `notify_on_close` to `true` when creating a view with [`views.open`](/reference/methods/views.open), pushing a new view with [`views.push`](/reference/methods/views.push), or in your response to the action.

If a user closes a specific view in a modal using the _Cancel_ button, you will receive a `view_closed` event with the corresponding view's `id`.

That being said, if the user exits the modal with the _x_ button in the top-right corner, you'll receive a `view_closed` event with the initial modal view's `id` and the `is_cleared` flag set to `true`.

Upon receiving either of the interaction payloads described above, your app can choose from a [multitude of responses](/interactivity/handling-user-interaction#responses). In every case, apps must [return a required acknowledgment response](/interactivity/handling-user-interaction#acknowledgment_response) back to the HTTP request that sent the payload.

It's likely you'll also want your app to modify the modal itself in some way. If so, you have a few options depending on the type of interaction that occurred:

*   If you want to modify a modal in response to a `block_actions` interaction, your app must [send the acknowledgment response](/interactivity/handling-user-interaction#acknowledgment_response). Then the app can use the `view.*` API endpoints [explained below](#modifying) to make desired modifications.
*   If you want to modify a modal in response to a `view_submission` interaction, your app can include a valid `response_action` with the [acknowledgment response](/interactivity/handling-user-interaction#acknowledgment_response). We'll explain how to do that [below](#modifying).

* * *

## Updating modal views {#updating_views}

A view can be updated to change the layout or its underlying state. This update can occur whether or not the view is currently visible within the modal's view stack. There are two ways to update a view in a modal:

*   [via `response_action`](#updating_response)
*   [via API](#updating_apis)

### Update a view via response_action {#updating_response}

If your app just received a [`view_submission`](#handling_submissions) payload, you have **3 seconds** to respond and update the source view. Respond to the HTTP request app with a `response_action` field of value `update`, along with a newly composed [`view`](#composing_views) as in the following example:

```
{  "response_action": "update",  "view": {    "type": "modal",    "title": {      "type": "plain_text",      "text": "Updated view"    },    "blocks": [      {        "type": "section",        "text": {          "type": "plain_text",          "text": "I've changed and I'll never be the same. You must believe me."        }      }    ]  }}
```

This method only works in response to a user clicking the `submit` button in a view; therefore it can only be used to update the currently visible view.

### Update a view via API {#updating_apis}

Remember the `view.id` [included in the success response](#success_response) when you used `views.open` [earlier](#opening_modals)? Hopefully you have that `id` handy, because you can now use it to update the view.

You may update a modal view by calling [`views.update`](/reference/methods/views.update). Include a newly-composed `view` and the `id` of the view that should be updated. This new view will replace the contents of the existing view.

Preserving `input` entry

Data entered or selected in `input` blocks can be preserved while updating views. The new `view` object that you use with `views.update` should contain the same input blocks and elements with identical `block_id` and `action_id` values.

Here's an example of a `views.update` call:

```
POST https://slack.com/api/views.updateContent-type: application/jsonAuthorization: Bearer YOUR_TOKEN_HERE{  "view_id": "VIEW ID FROM VIEWS.OPEN RESPONSE",  "hash": "156772938.1827394",  "view": {    "type": "modal",    "callback_id": "view-helpdesk",    "title": {      "type": "plain_text",      "text": "Submit an issue"    },    "submit": {        "type": "plain_text",         "text": "Submit"    },    "blocks": [      {        "type": "input",        "block_id": "ticket-title",        "label": {          "type": "plain_text",          "text": "Ticket title"        },        "element": {          "type": "plain_text_input",          "action_id": "ticket-title-value"        }      },      {        "type": "input",        "block_id": "ticket-desc",        "label": {          "type": "plain_text",          "text": "Ticket description"        },        "element": {          "type": "plain_text_input",          "multiline": true,          "action_id": "ticket-desc-value"        }      }    ]  }}
```

#### Avoiding race conditions when using views.update {#handling_race_conditions}

Race conditions can potentially occur when updating views using `views.update`, but luckily there's a solution built-in.

Let's digress for an example:

*   Suppose there is a view with a list of tasks that can be marked as complete using a button. When the task is completed, the UI shows the timestamp when the task was completed.
*   If the user clicks the complete button for task A, the app will mark the task as completed in the app's database, query the same database for an up-to-date list of tasks, then make a call to `views.update` with a new `view`. In this case, the modal will correctly display task A as complete, and task B as incomplete.
*   If, while the above processing is happening, the user clicks the complete button for task B, the app will go through the same process as above. All being well, the view will correctly display both task A and task B as complete.
*   However, it's possible that the `views.update` call from completing task A could take longer to complete than the same API call from completing task B. Perhaps it took longer to query for the list of tasks after marking task A as complete, or perhaps temporary network conditions slowed down the API call to `views.update` for task A.
*   In this case, the user would initially see the correct task list display after the `views.update` call from task B.
*   The modal would then update again after the `views.update` call from task A, and the user would see task A as complete, but task B as incomplete.
*   The outdated `views.update` call from after completing task A has overwritten the up-to-date `views.update` call from after completing task B.

Okay, digression over. So, how can your app solve this problem?

To prevent these kinds of conditions, there is a `hash` value included in all [`block_actions`](/reference/interaction-payloads/block_actions-payload) payloads. You can pass `hash` when calling [`views.update`](/reference/methods/views.update). If the `hash` is outdated, the API call will be rejected. This provides an automated assurance that you will never accidentally update a view with outdated data. We highly recommend your apps take advantage of this `hash` value.

## Adding a new view {#adding_views}

Within a modal's view stack, 3 views can exist at any one time. If there is still space remaining, you can push a new view onto the view stack. The newly-pushed view will immediately become visible to the user. When the user closes or submits this new view, they'll return to the next one down in the stack.

There are two ways to add a view to a modal's view stack:

*   [via `response_action`](#pushing_response)
*   [via API](#pushing_api)

### Add a new view via response_action {#add_response}

If your app has received a [`view_submission`](#handling_submissions) payload, you have **3 seconds** to respond and push a new view. Respond to the HTTP request app with a `response_action` field of value `push`, along with a [newly composed `view`](#composing_views) as in the following example:

```
{  "response_action": "push",  "view": {    "type": "modal",    "title": {      "type": "plain_text",      "text": "Updated view"    },    "blocks": [      {        "type": "image",        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/plants.png",        "alt_text": "Plants"      },      {        "type": "context",        "elements": [          {            "type": "mrkdwn",            "text": "_Two of the author's cats sit aloof from the austere challenges of modern society_"          }        ]      }    ]  }}
```

The view immediately becomes visible on top of the submitted view, adding it to the top of the modal's view stack. When a user submits or cancels the current view, they’ll return to the previous view on the stack.

If you need to get the `id` of the newly-pushed view (rather than the `id` of the submitted view, which is what `view.id` will return) in response to a `view_submission` payload, you can pass an [`external_id`](/reference/methods/views.update#arg_external_id) to update the modal after the new view is pushed.\]

You can then use the `external_id` to track your new view and update it using [`views.update`](/reference/methods/views.update).

### Add a new view via API {#add_api}

The [`views.push`](/reference/methods/views.push) method will add a new view to the top of the current stack of views in a modal, requires a `trigger_id` (similar to `views.open`), and can only be called when a modal is already open. Therefore, the only possible way to acquire a `trigger_id` to use here is from the use of an interactive component in the modal.

A `trigger_id` will expire 3 seconds after you receive it, so you need to make your call to `views.push` in that 3 second window.

```
POST https://slack.com/api/views.pushContent-type: application/jsonAuthorization: Bearer YOUR_TOKEN_HERE{  "trigger_id": "YOUR TRIGGER ID",  "view": {    "type": "modal",    "callback_id": "edit-task",    "title": {      "type": "plain_text",      "text": "Edit task details"    },    "submit": {    	"type": "plain_text",        "text": "Create"    },    "blocks": [      {        "type": "input",        "block_id": "edit-task-title",        "label": {          "type": "plain_text",          "text": "Task title"        },        "element": {          "type": "plain_text_input",          "action_id": "task-title-value",          "initial_value": "Block Kit documentation"        },      },      {        "type": "input",        "block_id": "edit-ticket-desc",        "label": {          "type": "plain_text",          "text": "Ticket description"        },        "element": {          "type": "plain_text_input",          "multiline": true,          "action_id": "ticket-desc-value",          "initial_value": "Update Block Kit documentation to include Block Kit in new surface areas (like modals)."        }      }    ]  }}
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22title%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Modal%20title%22%7D,%22submit%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Save%22%7D,%22type%22:%22modal%22,%22blocks%22:%5B%7B%22type%22:%22input%22,%22block_id%22:%22edit-task-title%22,%22label%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Task%20title%22%7D,%22element%22:%7B%22type%22:%22plain_text_input%22,%22action_id%22:%22task-title-value%22,%22initial_value%22:%22Block%20Kit%20documentation%22%7D%7D,%7B%22type%22:%22input%22,%22block_id%22:%22edit-ticket-desc%22,%22label%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Ticket%20description%22%7D,%22element%22:%7B%22type%22:%22plain_text_input%22,%22multiline%22:true,%22action_id%22:%22ticket-desc-value%22,%22initial_value%22:%22Update%20Block%20Kit%20documentation%20to%20include%20Block%20Kit%20in%20new%20surface%20areas%20\(like%20modals\).%22%7D%7D%5D,%22close%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Cancel%22%7D,%22private_metadata%22:%22Shhhhhhhh%22,%22callback_id%22:%22view_identifier_12%22%7D)

The view immediately becomes visible on top of the submitted view, adding it to the top of the modal's view stack. When a user submits or cancels the current view, they’ll return to the previous view on the stack.

A successful response from [`views.push`](/reference/methods/views.push) will include an `id` for the newly pushed view. This `id` is useful if you need to update the view using `views.update`.

## Closing views {#closing_views}

Apps have the ability to close views within a modal. This can happen only in response to the user clicking a submit button in the modal, sending the [`view_submission`](#handling_submissions) payload. After receiving this payload, your app has **3 seconds** to respond and close the submitted view, or close all views.

*   [Close the current view](#close_current_view)
*   [Close all view](#close_all_views)

Your app cannot use any other method to close views. A _user_ may choose to cancel a view, or close the entire modal by clicking on the _cancel_ or _x_ buttons, and your app [can optionally receive a notification if that happens](#modal_cancellations).

### Close the current view {#close_current_view}

If your app responds to a `view_submission` event with a basic [acknowledgment response](/interactivity/handling-user-interaction#acknowledgment_response) — an HTTP 200 response — this will immediately close the submitted view and remove it from the view stack. Your HTTP 200 response must be empty for this step to complete successfully.

If there are no more views left in the stack, the modal will close. Otherwise, the modal will display the next view down in the stack.

### Close all views {#close_all_views}

To close all views, set the `response_action` to `clear`. Regardless of the number of views in the stack, it will be emptied, and the modal will close:

```
{  "response_action": "clear"}
```

### Display errors in views {#displaying_errors}

Upon receiving a `view_submission` event, your app may want to validate any [inputs](#gathering_input) from the submitted view.

If your app detects any validation errors, say an invalid email or an empty required field, the app can respond to the payload with a `response_action` of `errors` and an `errors` object providing error messages:

```
{  "response_action": "errors",  "errors": {    "ticket-due-date": "You may not select a due date in the past"  }}
```

Within the `errors` object, you supply a key that is the `block_id` of the erroneous input block, and a value - the plain text error message to be displayed to the user.

The above JSON object would highlight the error within the modal around the `ticket-due-date` block, displaying the chosen error message. The user can then edit their input and resubmit the view.

Your app is responsible for setting and tracking `block_id`s when [composing views](#composing_views).

![A modal that is rendering errors supplied by the developer](/assets/images/modal-errors-33e61a7c021c14a6f24f451787f1b5ff.png)

### Carry data between views {#private_metadata}

Because views within a modal are usually connected in purpose, your app may want a way to send data from one view into the other, and then back again once a view is submitted.

To do this, we provide an optional `private_metadata` parameter that can be supplied in a `view` payload when your app [opens a modal with an initial view](#opening_modals), or [updates an existing view](#updating_views).

This `private_metadata` string is not shown to users, but is returned to your app in `view_submission` and `block_actions` events. Refer to `private_metadata` in `view` payloads for more detail.

Try it with AI

Modals are a great way to collect structured data, especially when you're looking for AI to complete a task with that given data, and your app expects the same data every time. Cut out the conversation and send all necessary inputs to an LLM by collecting it in a modal. Consider the following example of a slash command invoking a modal, then sending the collected data to an LLM and posting the answer to the user after. These examples use [Bolt for JavaScript](/tools/bolt-js) and [Bolt for Python](/tools/bolt-python).

Click to expand code

*   JavaScript
*   Python

app.js

```
// This is the listener for the slash command named 'generate-product-description'// The sole purpose of this is to collect product information in a formapp.command('/generate-product-description', async ({ ack, body, client, logger }) => {  try {    // Acknowledge the command request    await ack();    // Call views.open with the built-in client    const result = await client.views.open({      // Pass a valid trigger_id within 3 seconds of receiving it      trigger_id: body.trigger_id,      // View payload      view: {        type: 'modal',        // View identifier        callback_id: 'view_1',        title: {          type: 'plain_text',          text: 'Describe your product'        },        // Blocks comprise a view - get a preview of how they look at api.slack.com/block-kit-builder        blocks: [          {            type: 'section',            text: {              type: 'mrkdwn',              text: 'Enter the details for your product and AI will generate a description.'            },          },          {            type: 'input',            block_id: 'input_c',            label: {              type: 'plain_text',              text: 'Product name'            },            element: {              type: 'plain_text_input',              action_id: 'product_name',              multiline: true            }          },          {            type: 'section',            block_id: 'target_audience_block',            text: {              type: 'plain_text',              text: 'Target audience',            },            accessory: {              type: 'radio_buttons',              action_id: 'target_audience',              initial_option: {                value: 'Builders',                text: {                  type: 'plain_text',                  text: 'Builders'                }              },              options: [                {                  value: 'Builders',                  text: {                    type: 'plain_text',                    text: 'Builders',                  }                },                {                  value: 'Developers',                  text: {                    type: 'plain_text',                    text: 'Developers',                  }                },                 {                  value: 'Admins',                  text: {                    type: 'plain_text',                    text: 'Admins',                   }                }              ]            }          },          {            type: 'input',            block_id: 'key_features_block',            label: {              type: 'plain_text',              text: 'Key features'            },            element: {              type: 'plain_text_input',              action_id: 'key_features',              multiline: true            }          }        ],        submit: {          type: 'plain_text',          text: 'Submit'        }      }    });    logger.info(result);  }  catch (error) {    logger.error(error);  }});// This listener defines what happens once the submit button is clickedapp.view('view_1', async ({ ack, body, view, client, logger }) => {  // Acknowledge the view submission and close the modal.  await ack({    response_action: 'clear'  });  try {  // Extract submitted data from the view payload  const values = view.state.values;  const productName = values.input_c.product_name.value;  const targetAudience = values.target_audience_block.target_audience.selected_option.value;  const keyFeatures = values.key_features_block.key_features.value;  // The user who submitted the modal  const userId = body.user.id;  const defaultInstruction= 'You are a product marketing specialist tasked with drafting a product description for a website. Given the user input of product name, target audience, and key features, write a product description for the product.'  const commandText = `Product name: ${productName}\nTarget audience: ${targetAudience}\nKey features: ${keyFeatures}`;  // Prepare the messages to send to the LLM  const messages = [{ role: 'system', content: defaultInstruction }, {role: 'user', content: commandText}];  // A Hugging Face client is used here, but this could be substituted for any LLM  const llmResponse = await hfClient.chatCompletion({    model: 'Qwen/QwQ-32B',    messages,    max_tokens: 2000,  });  await client.chat.postMessage({    channel: userId, // Posts a message directly to the user who submitted the modal    text: llmResponse.choices[0].message.content,  });  } catch (error) {    logger.error(error);  }});
```

app.py

```
# This is the listener for the slash command named "generate-product-description"# The sole purpose of this is to collect product information in a form@app.command("/generate-product-description")def handle_slash_command(ack, body, client, logger):    # Acknowledge the command request    ack()    try:        # Define the modal view payload        modal_view = {            "type": "modal",            "callback_id": "view_1",            "title": {                "type": "plain_text",                "text": "Describe your product"            },            "blocks": [                {                    "type": "section",                    "text": {                        "type": "mrkdwn",                        "text": "Enter the details for your product and AI will generate a description."                    },                },                {                    "type": "input",                    "block_id": "input_c",                    "label": {                        "type": "plain_text",                        "text": "Product name"                    },                    "element": {                        "type": "plain_text_input",                        "action_id": "product_name",                        "multiline": True                    }                },                {                    "type": "section",                    "block_id": "target_audience_block",                    "text": {                        "type": "plain_text",                        "text": "Target audience",                    },                    "accessory": {                        "type": "radio_buttons",                        "action_id": "target_audience",                        "initial_option": {                            "value": "Builders",                            "text": {                                "type": "plain_text",                                "text": "Builders"                            }                        },                        "options": [                            {                                "value": "Builders",                                "text": {                                    "type": "plain_text",                                    "text": "Builders",                                }                            },                            {                                "value": "Developers",                                "text": {                                    "type": "plain_text",                                    "text": "Developers",                                }                            },                             {                                "value": "Admins",                                "text": {                                    "type": "plain_text",                                    "text": "Admins",                                 }                            }                        ]                    }                },                {                    "type": "input",                    "block_id": "key_features_block",                    "label": {                        "type": "plain_text",                        "text": "Key features"                    },                    "element": {                        "type": "plain_text_input",                        "action_id": "key_features",                        "multiline": True                    }                }            ],            "submit": {                "type": "plain_text",                "text": "Submit"            }        }        # Open the modal        result = client.views_open(            trigger_id=body["trigger_id"],            view=modal_view        )        logger.info(result)    except Exception as e:        logger.error(f"Error opening modal: {e}")@app.view("view_1")def handle_view_submission(ack, body, view, client, logger):    # Acknowledge the view submission and close the modal.    ack(response_action="clear")    try:        # Extract submitted data from the view payload        values = view["state"]["values"]        product_name = values["input_c"]["product_name"]["value"]        target_audience = values["target_audience_block"]["target_audience"]["selected_option"]["value"]        key_features = values["key_features_block"]["key_features"]["value"]        # The user who submitted the modal        user_id = body["user"]["id"]        hf_client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))        default_instruction = "You are a product marketing specialist tasked with drafting a product description for a website. Given the user input of product name, target audience, and key features, write a product description for the product."        command_text = f"Product name: {product_name}\nTarget audience: {target_audience}\nKey features: {key_features}"        # Prepare the messages to send to the LLM        messages = [            {"role": "system", "content": default_instruction},            {"role": "user", "content": command_text}        ]        # Use the Hugging Face client to get a response        llm_response = hf_client.chat_completion(            model="Qwen/QwQ-32B",            messages=messages,            max_tokens=2000,        )        # Post a message directly to the user who submitted the modal        client.chat_postMessage(            channel=user_id,            text=llm_response.choices[0].message.content,        )    except Exception as e:        logger.error(f"Error handling view submission: {e}")
```

## Publishing messages after modals are submitted {#modal_response_url}

You may want to publish a message to a Slack channel after your modal is submitted by doing one of the following:

*   Request necessary permissions and use the [Web API](/messaging/sending-and-scheduling-messages#publishing)
*   Generate and [use a webhook](/messaging/sending-messages-using-incoming-webhooks)
*   Include specific blocks and a special parameter in your modal

Unless your app is already configured to do one of the first two things, you'll want to include specific blocks and a special parameter in your modal.This method provides a straightforward route to message publishing for certain apps that use modals, such as those also using [shortcuts](/interactivity/implementing-shortcuts). Here's how:

1.  [Compose a modal view](#composing_views) with a `blocks` array that contains either a [`conversations_select`](/reference/block-kit/block-elements/select-menu-element#conversations_select) or [`channels_select`](/reference/block-kit/block-elements/select-menu-element#channels_select) element.
2.  Set the `response_url_enabled` parameter in the select menu to `true`. **This field only works with menus in [input blocks](/reference/block-kit/blocks/input-block) in modals.**
3.  Open and handle your modal as described in the guide above.

Here's an example view object containing this special configuration:

```
{    "type": "modal",    ...    "blocks": [      ...      {        "block_id": "my_block_id",        "type": "input",        "optional": true,        "label": {          "type": "plain_text",          "text": "Select a channel to post the result on",        },        "element": {          "action_id": "my_action_id",          "type": "conversations_select",          "response_url_enabled": true,        },      },    ],  };}
```

When a user opens the modal, they can choose a conversation to which they'd like a message posted. If you supply the [`default_to_current_conversation`](/reference/block-kit/block-elements/select-menu-element#conversations_select) parameter for the `conversation_select` element, you can even pre-populate the conversation they're currently viewing.

Once they submit the view, you'll receive a [`view_submission`](#handling_submissions) payload that will now include `response_urls`. You can use the values in `response_urls` to publish message responses. Refer to [our guide to handling interactions](/interactivity/handling-user-interaction#message_responses).

We recommend keeping these best practices in mind while using this technique:

*   Ensure you provide clear instruction to the user that a message will be posted to the conversation they choose.
*   Consider setting `optional` to `true` to allow the user to decline selecting a conversation.
*   If the user declines to select a conversation, or if they cancel the modal, handle this as appropriate.

* * *

## Designing modals {#designing}

Modals are intended for short-term interaction. Their popup, attention-grabbing nature makes them a mighty weapon that should be wielded only at truly appropriate moments.

![An example of modals in desktop and mobile clients](/assets/images/modal_clients-d79d08d7df9d2411b41fb231e45a3b47.svg)

Your app can't [invoke a modal](/surfaces/modals) without a `trigger_id` from a user interaction, which creates a certain amount of intentional usage. That being said, make sure to not surprise your users - they should understand that a modal will open based on their action.

Once invoked, a user can cancel a modal at any time. [Handle these cancellations](/surfaces/modals#modal_cancellations) with grace. Don't try to force the user to proceed through the same process again.

### Keep modals glanceable {#keep-modals-glanceable}

Whatever the modal's content, the end-user shouldn’t need to spend excessive time on a single view within a modal. Rather than overloading a view, your app should use inputs sparingly, and implement pagination as necessary — generally when there are upwards of six inputs or blocks of information.

### Indicate outcome {#indicate-outcome}

Your app should indicate what happens upon a modal submission. For example, if a message will be posted into a channel on the users behalf, it should be evident.

### Show progress {#show-progress}

If your app needs to perform resource-intensive data fetching, you should implement a temporary loading screen so the user better understands what's happening. This is especially important to consider as your app is installed on workspaces for larger teams with even larger collections of data.

### Don’t prompt for login information {#dont-prompt-for-login-information}

Users should **not** be prompted for confidential information like passwords within modals (or any app surface area, for that matter). When your app needs access to a user’s credentials, you should direct them to your login and store any necessary information on your app’s backend.

#### Use cases {#use-cases}

*   Collecting input from users
*   Displaying lists or results
*   Confirming a user’s action
*   Onboarding a user to your app