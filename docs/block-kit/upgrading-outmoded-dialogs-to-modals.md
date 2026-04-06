Source: https://docs.slack.dev/block-kit/upgrading-outmoded-dialogs-to-modals

# Upgrading outmoded dialogs to modals

In late 2019 we released a new app surface for collecting rich user input and displaying dynamic information using [Block Kit](/block-kit) — [**modals**](/surfaces/modals). Modals are the replacement for [dialogs](/legacy/legacy-dialogs), an outmoded feature that allowed apps to collect static input.

Modals have the ability to use Block Kit interactive components like [datepickers](/messaging/creating-interactive-messages#datepickers) and [multi-select menus](/messaging/creating-interactive-messages#multi_select_menus), as well as the standard input options available to dialogs. Modals can also be updated dynamically, and chained together to form deep workflows.

Dialogs will continue to work for the time being, but apps using them cannot avail any of these new modal features.

This guide is intended for developers of existing Slack apps that use dialogs. It will provide information on how to migrate your dialogs to modals and introduce you to new capabilities and components that modals provide.

* * *

## Planning your upgrade {#planning}

Mapping dialogs to modals is fairly straight-forward if you plan to keep the same layout and user flow. However, it’s **highly recommended** you take the opportunity to explore the new Block Kit components and [additional functionality](#new_methods) available to your app within modals.

### Using blocks to collect richer user input {#using_blocks}

Modals are built with [blocks](/reference/block-kit/blocks) that can be mixed and stacked to design surface areas customized to your app. Modals can use Block Kit components that map directly to dialog elements. Blocks such as [`input`](/reference/block-kit/blocks/input-block) and elements like [`select` menus](/reference/block-kit/block-elements/select-menu-element) replicate fields that could be added to dialogs.

There are also additional blocks that your app can use to improve the user experience and simplify the payload your app receives on submission:

[**Date pickers**](/reference/block-kit/block-elements/date-picker-element) allow your app to collect dates through a calendar interface. This provides a better user experience than text fields, and it standardizes date formats that your app may receive.

[**Multi-select menus**](/reference/block-kit/block-elements/multi-select-menu-element) are new dropdown menus similar to select menus. You probably guessed by the name, but they allow users to make multiple selections rather than being limited to just one.

You also have access to the entire suite of blocks, like `section` and `image` blocks that allow you to display static content, or `divider` and `context` blocks that help you organize information.

To get started with blocks read our [building with blocks guide](/block-kit), or to see all available blocks check out our [layout block reference](/reference/block-kit/blocks).

### Creating a modal {#creating}

Similar to [`dialog.open`](/reference/methods/dialog.open), with modals you call [`views.open`](/reference/methods/views.open) to open a modal and populate it with a [view object](/reference/views).

The response will be similar to dialogs, though it will also include a view ID which you can use to [update an existing modal](#new_methods). Read our [documentation on creating modals](/surfaces/modals) to learn more and see an example.

### Updating and pushing views in modals {#new_methods}

Modals are containers that can hold a stack of one to three views. Each view is generated using [a payload](/reference/views) that defines a Block Kit layout, view functionality, and some state variables to track within the view.

Within an individual modal, views can be created and [pushed onto the stack](/reference/methods/views.push), or [updated while in the stack](/reference/methods/views.update). Complete [our guide to using modals](/surfaces/modals) to learn how to manipulate views and modals.

### Prototyping with Block Kit Builder {#builder}

[Block Kit Builder](https://api.slack.com/tools/block-kit-builder) is a prototyping tool that allows you (or a designer on your team) to quickly design surface areas for your app. There’s a [dedicated mode to design modals](https://api.slack.com/tools/block-kit-builder?&mode=modal) which reveals blocks exclusive to modals, like the [`input`](/reference/block-kit/blocks/input-block) block.

The Builder also provides [templates with common workflows](https://api.slack.com/tools/block-kit-builder?template=1) to get started, editable JSON to plug into your app, and example interactive payloads to examine what your app will receive.

## Upgrading to modals {#upgrading}

You've read about the details of new modals functionality that apps have access to. Now let's get into the specific differences to account for in your app when you replace dialogs with modals.

### Discovering equivalents for dialog elements {#elements}

The content of a view is composed using a `blocks` array rather than the `elements` equivalent in dialogs. The `blocks` array contains a collection of [blocks from the Block Kit framework](/reference/block-kit/blocks). Although dialogs could only contain 10 elements, modals can contain up to 100 blocks.

Each dialog element has an equivalent that you can use to define and design the views within your modals:

[`input`](/reference/block-kit/blocks/input-block) blocks replace the dialog's text element and textarea. The `input` block has an optional `multiline` flag that determines whether it should be one line (the text element equivalent) or multiple lines (the textarea equivalent).

An important difference with `input` blocks in a view is that when _any_ `input` blocks are in your `blocks[]` array, you **must** pass a [`submit` element](/reference/views). When you pass a `submit` element, you will receive the input's values when a user submits the view. This is discussed more in the [accessing input values in modals](#accessing_input) section.

[`select` menus](/reference/block-kit/block-elements/select-menu-element) and [`multi-select` menus](/reference/block-kit/block-elements/multi-select-menu-element) replace the dialog's select element. Select menus can be within [`actions` blocks](/reference/block-kit/blocks/actions-block), [`input` blocks](/reference/block-kit/blocks/input-block), or as accessories in [`section` blocks](/reference/block-kit/blocks/section-block).

To see all available blocks, see our [layout block reference](/reference/block-kit/blocks).

### Identifying blocks with block_id and action_id {#identifying}

While [view objects](/reference/views) are still identified using a `callback_id`, interactive components within a view use `block_id`s and `action_id`s. These are sent when interactive components are used in a view, or when a view is submitted (described [below](#accessing_input)).

The `block_id` is specified in blocks. It can be used to identify the parent block of the source interactive component used in a `block_actions` or `view_submission` interaction. If you don’t specify a `block_id`, one will be automatically generated for the block.

The `action_id` is specified in the interactive component. It can be used to identify the parent block of the source interactive component used in a `block_actions` or `view_submission` interaction. If you don’t specify an `action_id`, one will be automatically generated for the element.

### Accessing input values in modals {#accessing_input}

For elements within `input` blocks, the values will be contained in a `view_submission` payload that will be sent to your app’s Request URL when a user clicks a submit button.

Within the `view_submission` payload, there will be a `state` object that contains the values for all `input` blocks, stored using their `block_id` and `action_id`.

To learn more about view submissions, read the section on [handling `view_submission` events](/surfaces/modals#handling_submissions).

### Handling interactions in modals {#interactions}

If you have `select` menus or other interactive components within an [`actions`](/reference/block-kit/blocks/actions-block) or [`section`](/reference/block-kit/blocks/section-block) block, the values will **not** be contained in the `view_submission` payload. You’ll handle these events in the same way as all Block Kit interactive components.

For more information on handling non-input interactions in modals, [read the modals documentation](/surfaces/modals#handling_modal_interactions).

### Responding to view_submission events {#submissions}

Within dialogs, you respond to `dialog_submission` events with either a **200 OK** or an array of errors. With modals, your app will receive a `view_submission` event. After receiving this event, you have 3 seconds to respond with a valid [`response_action`](/surfaces/modals#handling_submissions).

Similar to dialogs, `response_action`s allow your app to close the modal or display errors. If you just want to close the modal, nothing will change — you’ll just respond with a **200 OK**. For other options, you’ll respond with the `response_action` corresponding to the action you want to take.

With modals, you also have the option to use a `response_action` to update a view, push a new view, or close all views. To learn more about using `response_action`s [read the handling submission section of the documentation](/surfaces/modals#handling_submissions).

### Passing state in modals {#state}

When opening or updating a view, you may optionally use the `private_metadata` string to pass additional data. This is equivalent to the `state` string in dialogs, and has the same 3000 character limit.

The `private_metadata` string will never be sent to clients. It is only returned in `view_submission` and `block_actions` events.

### Don't rely on response_url {#responding}

When a dialog is submitted, your app receives an HTTP request. `dialog_submission` events contained a `response_url` that allowed you to post a message tied to the channel the dialog was initiated from. However, **modals don't rely on a channel context**. This means that the `view_submission` event will not contain a `response_url`.

If you want to send a message into the channel the modal was opened from, you can pass the channel ID in the [`private_metadata` string](#state). This will be included in `view_submission` events, and you can access this value to send a message to channel using [`chat.postMessage`](/reference/methods/chat.postMessage). Another option is to DM the user verifying that the modal they filled out was successfully submitted.

Note that to call [`chat.postMessage`](/reference/methods/chat.postMessage), you’ll need to add the `chat:write` scope to your app if you aren’t using a bot user.

### Include text in objects rather than as fields {#text}

Instead of defining text as a flat field, Block Kit uses text objects. Using text objects you can define the actual text content, as well as the formatting method (mrkdwn or plain\_text) in the same place. Read the [reference guide for text objects](/reference/block-kit/composition-objects/text-object) to see an example and full details.

Note that in view objects, most text objects _only_ accept `plain_text` objects. Read the [reference guide for view objects](/reference/views) for more information.

### Handling closed modals {#closing}

When creating a view object, you can pass a `notify_on_close` flag that indicates that Slack will send you a `view_closed` event. This is equivalent to the `notify_on_cancel` flag in dialogs.

Read the [reference guide for view objects](/reference/views) for more information and examples.

## Next steps {#next}

Congratulations! 🎉 If you made it to this point, hopefully you were successfully able to migrate your app’s dialogs to modals. If you want to level-up your app’s user experience, here are some next steps:

*   If you haven’t migrated your messages to use Block Kit, read our [migration guide for messages](/messaging/migrating-outmoded-message-compositions-to-blocks#text_objects).
    
*   Explore all of the [available Blocks and elements in Block Kit](/block-kit). Discover new interactive components and static elements that will allow you to create cleaner and more compelling workflows.
    
*   Use the [Block Kit Builder](https://api.slack.com/tools/block-kit-builder) to quickly play with blocks, or use [templates](https://api.slack.com/tools/block-kit-builder?template=1) as a starting point for common design patterns in Slack apps.
    
*   If you’re rewriting your app from scratch, check out Bolt, a development framework built to make building Slack apps faster and easier, available in [JavaScript](/tools/bolt-js) and [Java](/tools/java-slack-sdk/guides/getting-started-with-bolt).