Source: https://docs.slack.dev/messaging/creating-interactive-messages

# Creating interactive messages

Transform your Slack app into a powerful workflow partner by making messages interactive.

In this guide we'll walk through how [app interactivity](/interactivity) applies to messages and show you how to build a Slack app capable of interacting with users via message.

* * *

## App interactivity in messages {#interactivity}

Beyond creating [rich message layouts](/messaging/formatting-message-text#rich-layouts), [Block Kit](/block-kit) also contains a subset of [components that enable interactivity](/block-kit#making-things-interactive). These [interactive components](/block-kit#making-things-interactive) can be inserted into messages, converting them from mere information relays into powerful partners for users.

[Work Objects](/messaging/work-objects-overview) allow you to facilitate rich user interactions by implementing [flexpane components](/messaging/work-objects-overview#flexpane), [unfurl cards](/messaging/work-objects-overview#unfurl), and supporting Block Kit actions such as [action buttons](/messaging/work-objects-implementation#actions).

Where once your Slack app might have just pulled in data from external services, interactivity allows your app to manipulate, update, and send back data to that same service, thanks to user action.

* * *

## Getting started with interactive messages {#getting_started}

For this guide, you'll need to have [created a Slack app](/app-management/quickstart-app-settings#creating), though you won't need to have built it out with any features yet.

When you're ready, it's time to get started.

## 1. Compose your interactive message {#compose}

Adding interactive components is no different from adding any other block. Let's add a couple of [buttons](/reference/block-kit/block-elements/button-element) to an [actions](/reference/block-kit/blocks/actions-block) block in a message payload:

```
{  "channel": "C123ABC456",  "text": "New Paid Time Off request from Fred Enriquez",  "blocks": [    {      "type": "header",      "text": {      "type": "plain_text",        "text": "New request",        "emoji": true      }    },    {      "type": "section",      "fields": [        {          "type": "mrkdwn",          "text": "*Type:*\nPaid Time Off"        },        {          "type": "mrkdwn",          "text": "*Created by:*\n<example.com|Fred Enriquez>"        }      ]    },    {      "type": "section",      "fields": [        {          "type": "mrkdwn",          "text": "*When:*\nAug 10 - Aug 13"        }      ]    },    {      "type": "actions",      "elements": [        {          "type": "button",          "text": {            "type": "plain_text",            "emoji": true,            "text": "Approve"          },          "style": "primary",          "value": "click_me_123"        },        {          "type": "button",          "text": {            "type": "plain_text",            "emoji": true,            "text": "Reject"          },            "style": "danger",            "value": "click_me_123"        }      ]    }  ]}
```

[View in Block Kit Builder](https://api.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22New%20request%22,%22emoji%22:true%7D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type:*%5CnPaid%20Time%20Off%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Created%20by:*%5Cn%3Cexample.com%7CFred%20Enriquez%3E%22%7D%5D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*When:*%5CnAug%2010%20-%20Aug%2013%22%7D%5D%7D,%7B%22type%22:%22actions%22,%22elements%22:%5B%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22emoji%22:true,%22text%22:%22Approve%22%7D,%22style%22:%22primary%22,%22value%22:%22click_me_123%22%7D,%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22emoji%22:true,%22text%22:%22Reject%22%7D,%22style%22:%22danger%22,%22value%22:%22click_me_123%22%7D%5D%7D%5D%7D)

You could replace these buttons with any of the [available interactive components](/block-kit#making-things-interactive). You can also add a button as a [`section` block's `accessory` element](/reference/block-kit/blocks/section-block), rather than the `actions` block used above.

Browse the [interactive components](/block-kit#making-things-interactive) to see a full list of what's available, or try the [Block Kit Builder tool](https://api.slack.com/tools/block-kit-builder) to visually prototype a layout with interactive components.

## 2. Publishing an interactive message {#publishing_interactive_messages}

There's nothing special about the process of an app publishing an interactive message, compared to a regular message. Read our [guide to sending messages](/messaging/sending-and-scheduling-messages) to find the best publishing method for your app.

After you've chosen a sending method, try to send the message payload above, substituting a real `channel` ID.

Once you do, your app's message will be sitting in channel, waiting for someone to click the button within. Let's see what happens when they do.

## 3. Prepare your app to receive interaction payloads {#understanding_payloads}

When someone uses an interactive component published by your app, Slack will send an [interaction payload to you](/interactivity/handling-user-interaction#payloads).

An interaction payload is both a way of notifying your app about an interaction, and a bundle of info describing the where and when (and many other Ws) of the interaction. It is vital to the interaction process, so your app has to be able to understand it.

The payload will be sent to your [configured Request URL](/interactivity/handling-user-interaction#payloads) in an HTTP POST. The body of that request will contain a `payload` parameter. Your app should parse this `payload` parameter as JSON.

The entirety of this payload will contain all the contextual info that your app needs to be able to figure out what kind of interaction occurred. Your app can use as much or as little of the info as needed.

For the purposes of this guide, you should grab the `channel` object, and store that channel's `id` for later. You'll also want to grab the `response_url` here too.

Now that your app can receive and understand interaction payloads, it needs to decide what it will do after one of them is sent.

## 4. Respond to the interaction {#responding_to_interactions}

In our [guide to handling user interaction](/interactivity/handling-user-interaction) we explained the different app responses to any interaction.

The most important is the required [acknowledgment response](/interactivity/handling-user-interaction#acknowledgment_response). This response is sent back to the same HTTP POST that [delivered the interaction payload](#understanding_payloads).

In addition to this acknowledgment, your app can also choose to [compose a message response](/interactivity/handling-user-interaction#message_responses), [invoke a modal](/interactivity/handling-user-interaction#modal_responses), or [one of a multitude of asynchronous responses](/interactivity/handling-user-interaction#async_responses).

* * *

## Next steps {#next}

Through this guide you've learned how to add interactive components to messages, prepared your app to handle payloads, and created a simplified interactive flow. From here you can dive into our [reference guides](/reference/block-kit/blocks) to learn more about the different types of blocks you can use, and deepen what your app is capable of doing for users.