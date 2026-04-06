Source: https://docs.slack.dev/messaging/migrating-outmoded-message-compositions-to-blocks

# Migrating outmoded message compositions to blocks

In early 2019 we introduced a new way of composing messages, by [using blocks to create rich and interactive layouts](/messaging/creating-interactive-messages). Slack apps designed and built before then may have used features such as [attachments](/legacy/legacy-messaging/legacy-secondary-message-attachments) which are now considered outmoded.

These older features will continue to work, but apps using them will miss out on the [new layout](/messaging#complex_layouts) and [interactivity features](/messaging/creating-interactive-messages) blocks provide.

This guide is intended for developers of existing Slack apps that are using outmoded composition features. It will provide information on the best ways to transform your messages to block layouts and introduce new ways of thinking about message composition in the era of blocks. We will also show you the newer blocks and elements that can be used to directly replace outmoded visual components such as attachments.

* * *

## Planning your upgrade {#planning}

In many cases, message layouts directly map to an [exact block equivalent](#switching_to_blocks). If your app sends messages with text and some buttons, this strategy may work best for your app:

![A message from an app called Lunch Train showing a lunch invite and buttons to accept or decline](/assets/images/lunch_train_example_1-7175c6e31ebe6bbbd83be5cd0a7fbd26.png)

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22Chew%20choo!%20%40scott%20started%20a%20train%20to%20Deli%20Board%20at%2011%3A30.%20Will%20you%20join%3F%22%0A%09%09%7D%0A%09%7D%2C%0A%09%7B%0A%09%09%22type%22%3A%20%22actions%22%2C%0A%09%09%22elements%22%3A%20%5B%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22button%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22plain_text%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%22Yes%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22emoji%22%3A%20true%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22button%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22plain_text%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%22No%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22emoji%22%3A%20true%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%09%09%09%7D%0A%09%09%5D%0A%09%7D%0A%5D)

This case may not warrant any more work after you [switch to blocks](#switching_to_blocks).

We **strongly recommend**, however, that all developers of Slack apps use this opportunity to completely rethink their message compositions, and take advantage of the exciting new features and possibilities that have been introduced.

Consider these basic guidelines when migrating to block-based message composition:

### Use new elements to simplify messages {#new_elements}

New [block elements](/reference/block-kit/block-elements) such as [overflow menus](/reference/block-kit/block-elements/overflow-menu-element) or [date pickers](/reference/block-kit/block-elements/date-picker-element) offer the opportunity to clean up message complexity. Keep the focus of a message on what users are trying to do right there and then, and de-emphasize interactive actions that are less important.

Here's an example message that might have been directly ported from an older, [attachment](/legacy/legacy-messaging/legacy-secondary-message-attachments)\-based version:

![An interactive message showing an approval request with a row of 6 buttons](/assets/images/keep_flow_bad-21f859c61ed884391e11346b660c0361.png)

With the help of the new [overflow menu](/reference/block-kit/block-elements/overflow-menu-element), this message could instead be simplified and focused:

![An interactive message showing an approval request with approve/reject buttons and an overflow menu](/assets/images/keep_flow_good-7fb5c9aa27b4b09b7696b1e551248a7a.png)

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22*Approval%20Request*%5CnYour%20approval%20is%20requested%20to%20make%20an%20offer%20to%20%3Chttp%3A%2F%2Fexample.com%7CFlorence%20Tran%3E.%22%0A%09%09%7D%0A%09%7D%2C%0A%09%7B%0A%09%09%22type%22%3A%20%22context%22%2C%0A%09%09%22elements%22%3A%20%5B%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%09%22text%22%3A%20%22%3Chttp%3A%2F%2Fexample.com%7CView%20applicant%3E%22%0A%09%09%09%7D%0A%09%09%5D%0A%09%7D%2C%0A%09%7B%0A%09%09%22type%22%3A%20%22actions%22%2C%0A%09%09%22elements%22%3A%20%5B%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22button%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22plain_text%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%22Approve%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22emoji%22%3A%20true%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22button%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22type%22%3A%20%22plain_text%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22text%22%3A%20%22Reject%22%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%22emoji%22%3A%20true%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%09%09%09%7D%2C%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22overflow%22%2C%0A%09%09%09%09%22options%22%3A%20%5B%0A%09%09%09%09%09%7B%0A%09%09%09%09%09%09%22text%22%3A%20%7B%0A%09%09%09%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%09%09%09%22text%22%3A%20%22Follow%22%2C%0A%09%09%09%09%09%09%09%22emoji%22%3A%20true%0A%09%09%09%09%09%09%7D%2C%0A%09%09%09%09%09%09%22value%22%3A%20%22value-0%22%0A%09%09%09%09%09%7D%2C%0A%09%09%09%09%09%7B%0A%09%09%09%09%09%09%22text%22%3A%20%7B%0A%09%09%09%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%09%09%09%22text%22%3A%20%22Activity%20feed%22%2C%0A%09%09%09%09%09%09%09%22emoji%22%3A%20true%0A%09%09%09%09%09%09%7D%2C%0A%09%09%09%09%09%09%22value%22%3A%20%22value-1%22%0A%09%09%09%09%09%7D%2C%0A%09%09%09%09%09%7B%0A%09%09%09%09%09%09%22text%22%3A%20%7B%0A%09%09%09%09%09%09%09%22type%22%3A%20%22plain_text%22%2C%0A%09%09%09%09%09%09%09%22text%22%3A%20%22Details%22%2C%0A%09%09%09%09%09%09%09%22emoji%22%3A%20true%0A%09%09%09%09%09%09%7D%2C%0A%09%09%09%09%09%09%22value%22%3A%20%22value-3%22%0A%09%09%09%09%09%7D%0A%09%09%09%09%5D%0A%09%09%09%7D%0A%09%09%5D%0A%09%7D%0A%5D)

### Use new elements to add functionality {#new_functions}

While switching to blocks can let you hide previously visible and messy elements from view, you can also use new features like the [overflow menu](/reference/block-kit/block-elements/overflow-menu-element) to introduce brand new functionality to your app's messages.

Where before you might have cautiously avoided cluttering your messages with secondary actions that were nevertheless useful, now you can add them while keeping things clean.

### Consider mobile layouts of blocks and elements {#consider_mobile}

The replacement block for your outmoded visual element might create an identical layout on desktop clients, but make sure the mobile view still looks good. Some blocks can have very different layouts on desktop clients compared to mobile:

![An interactive message showing two buttons in a desktop client layout compared to the mobile layout](/assets/images/desktop_vs_mobile-89052b9a1339b0296d1a7df21776aeb7.png)

### Free your messages from layout constraints {#free_layouts}

If you've used [attachments](/legacy/legacy-messaging/legacy-secondary-message-attachments), you'll know that they conform to a very strict order of visual elements. You can't change where the `author_name` field renders in a message, for example. This leaves designers of Slack apps constrained in terms of the range of possibilities for message layouts.

Apps that switch to using layout blocks can choose from any of the [available blocks](/reference/block-kit/blocks) and [elements](/reference/block-kit/block-elements), stacking them in whatever order is desired. Blocks can also be repeated within the same message, giving a designer a huge amount more composition flexibility. For example, that `author_name` field mentioned above becomes [a context block](/reference/block-kit/blocks/context-block) that could be placed anywhere in the message, and contain more than just an author name.

### Prototype with Block Kit Builder {#builder}

Seeing is believing. [Block Kit Builder](https://api.slack.com/tools/block-kit-builder) is a visual prototyping tool that lets you preview message composition without writing any code.

[Use it](https://api.slack.com/tools/block-kit-builder) to prototype your new message designs, to check the validity of the blocks JSON that you're publishing, and to examine sample interaction payloads.

* * *

## Switching to block layouts {#switching_to_blocks}

Now that you've [planned your app's transition to using blocks](#planned), you probably have some questions about the nitty gritty. Following is a list of important information to understand the changing paradigms compared to the older ways of composing messages.

### Finding equivalents for older visual elements {#direct_equivalents}

Nearly every older visual element has a direct equivalent in blocks or block elements. If you were using attachments, you can find a list of block alternatives for each visual component in our [attachment fields reference guide](/legacy/legacy-messaging/legacy-secondary-message-attachments#legacy_fields).

There is one exception, and that's the [`color` parameter](/legacy/legacy-messaging/legacy-secondary-message-attachments#fields), which currently does not have a block alternative. If you are strongly _attached_ (🎺) to the `color` bar, use the [`blocks` parameter](/legacy/legacy-messaging/legacy-secondary-message-attachments#fields) within an attachment.

This will let you place newer blocks inside of an attachment, but bear in mind the [advice above](#planning) and use the opportunity to rethink your message composition. Users will increasingly associate attachments with less-important secondary content because they have a lower visual hierarchy compared to blocks.

There are a few more things to watch out for if you're an old hand at pre-block message composition.

### Include text in objects rather than as fields {#text_objects}

Instead of the older, awkward way of defining `text` - as a flat field with a separate `mrkdwn_in` array to determine the formatting method - within blocks there is a new, saner way to structure text.

Using [text objects](/reference/block-kit/composition-objects/text-object) you can define the actual text content, as well as the formatting method (`mrkdwn` or `plain_text`) in the same place. Read the [reference guide for text objects](/reference/block-kit/composition-objects/text-object) to see an example and full details.

### Watch out for changes to field limits {#field_limits}

A lot of limits - for things like the maximum length of text fields, or the number of elements that can be included in a block - will be different from what you may be used to. Check out the [block reference guides](/reference/block-kit/blocks) for full details of any limits applied to particular fields.

### Prepare for the new structure of interaction payloads {#new_payloads}

If you were using any of the outmoded versions of [interactive components](/reference/block-kit/block-elements), such as buttons or menus, your app will be built to handle the specific interaction payload from those outmoded components.

While the structure of the interaction payload is largely the same for the [newer interactive components](/reference/block-kit/block-elements), you should prepare your app for the new structure, accommodating small changes like the new `type` of `block_actions` that will be included. Our [reference guide](/reference/interaction-payloads/block_actions-payload) contains an outline of this new interaction payload structure.

This payload will also include new `block_id` and `action_id` fields, [as described below](#callback_id_replacement).

### Use block_id and action_id instead of callback_id {#callback_id_replacement}

In the past, including a `callback_id` when publishing a message would allow you to pass a unique identifier for a group of buttons in an interactive message attachment. This `callback_id` was sent with the interaction payload when someone clicked one of the buttons.

With [interactive components](/reference/block-kit/block-elements) in blocks, there are _two_ new fields that can replicate this same functionality, `block_id` and `action_id`. Both (or one or none) of these fields can be specified [when you're composing a message](/messaging#complex_layouts), and they'll be included with the [interaction payload](/interactivity/handling-user-interaction#payloads) sent to your app.

`block_id` is specified [in blocks](/reference/block-kit/blocks). It can be used to identify the parent block of the source [interactive component](/reference/block-kit/block-elements) used in an interaction. If you don't specify a `block_id`, one will be automatically generated for the block, and included in [interaction payloads](/interactivity/handling-user-interaction#payloads).

`action_id` is specified [in interactive components](/reference/block-kit/block-elements). It can be used to identify the source interactive component used in an interaction. If you don't specify an `action_id`, one will be automatically generated for the element, and included in [interaction payloads](/interactivity/handling-user-interaction#payloads).

In addition, the `value` field for [options](/reference/block-kit/composition-objects/option-object) will continue to identify which item _within_ an interactive component was chosen (for example the chosen option within a [select menu](/reference/block-kit/block-elements/select-menu-element)).

### Specify fallback text for message notifications {#fallback_text}

Unless you're sending messages that only contain plain text, you'll need to provide fallback text when publishing a message. This fallback text will specify what should appear in any notifications prompted by the publishing of the message.

Previously there was a [`fallback` field defined within the attachment object](/legacy/legacy-messaging/legacy-secondary-message-attachments#legacy_fields) to define this fallback text.

When you're using [blocks](/reference/block-kit/blocks) in a message, however, you specify fallback text by using the [top-level `text` field within the payload](/messaging#payloads) your app is sending to publish the message. The `text` field won't render in messages in Slack clients as long as `blocks` is also provided, but it will show up as the fallback text in notifications.

If you're not including the `blocks` field, the [top-level `text` field](/messaging#payloads) will continue to render in messages as normal.

### Use only response_url to publish messages in response to interactions {#response_message}

When an interaction occurs, apps receive an interaction payload in an HTTP request.

In the past, apps could respond directly to this HTTP request to publish a new message. The `response_url` from the interaction payload could then be used to publish any subsequent messages.

With blocks, it is not possible to publish a new message by responding directly to the HTTP request. You will **always** need to use the `response_url` for this purpose. The HTTP response may now only be used to send an HTTP 200 acknowledgement response.

Read our [guide to responding to interactions](/interactivity/handling-user-interaction#responses) to find out more information about acknowledgement responses, and how to use the `response_url` to publish, delete, and update messages.