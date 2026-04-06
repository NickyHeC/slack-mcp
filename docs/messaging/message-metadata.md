Source: https://docs.slack.dev/messaging/message-metadata

# Using message metadata

Messages are how people communicate with people, **message metadata** is how apps communicate with apps.

Slack can be a busy place, with millions of messages and numerous notifications. Many of those messages correspond to app events - whether that be from Slack apps or external apps such as project management or calendar software.

Message metadata gives apps a way to correspond with other apps by passing along the event information they need within messages.

* * *

## Understanding message metadata {#overview}

With message metadata, your app can become an event-driven vehicle, delivering information across the Slack platform in a structured way.

Let's look at an example. If we wanted to add metadata about a customer to a message that alerts a channel whenever a new customer is created, we can start with the message object:

```
{    "channel": "A12345",    "text": "A new customer record has been created."}
```

Then, we can attach some metadata to it:

```
{    "channel": "A12345",    "text": "A new customer record has been created.",    "metadata": {        "event_type": "customer_created",        "event_payload": {            "crm_id": "123456ABCD",            "external_id": "QWERTY12",            "nurture_step": "new_account"        }    }}
```

After your message is sent and becomes part of a channel's timeline, your app or another developer's app can respond, react, or do something completely unexpected (but reasonable) in its own way to your message metadata.

Maybe your CRM will perform some nurturing automations based on this new customer being created. Maybe the folks handling accounts payable use an app to automatically update their systems based on some external ID.

Whatever the case may be, you determine the unique `event_type` for your automations as well as the structure of the `event_payload`, giving you the opportunity to customize exactly how your apps and external systems communicate with each other.

* * *

## Defining metadata {#defining}

Message metadata consists of _structured payloads_ defined by you that contain additional information beyond a message's visible contents.

While the structure used for metadata is very close to the JSON schema standard, we have a few conventions and native types that differ. Using the recommended schema will allow your metadata events to be more easily accepted by other Slack apps.

Our [design guidelines](/messaging/message-metadata/designing-metadata-event-schema) are a helpful resource for creating message metadata event schemas.

* * *

## Sending metadata {#sending_metadata}

Once you have planned out a payload structure to link between messages that your app sends and some outside event, your app can _send_ that metadata any time that it sends messages.

In order to send metadata with a message, include a `metadata` parameter. You'll use two keys, `event_type` and `event_payload`, inside `metadata`.

One way you can send metadata is by using the [`chat.postMessage`](/reference/methods/chat.postMessage) method with the `metadata` argument. We recommend using the method with a HTTP POST and an `application/json` body. Below are a few examples doing so.

Example: Task created

This example shows a message sent when a new task is created. It include metadata about the task for project management tools to pull in:

```
POST /api/chat.postMessageHost: slack.comAuthorization: Bearer xoxb-6050345600-60510457-…Content-type: application/json; charset=utf-8{    "channel": "C123ABC456",    "text": "New task Added by @sam - Redesign homepage",    "metadata": {        "event_type": "task_created",        "event_payload": {            "id": "TK-2132",            "summary": "New issue with the display of mobile element",            "description": "An end user has found a problem with the new mobile container for data entry. It was reproduced in the current version of IOS.",            "priority": "HIGH",            "resource_type": "TASK"        }    }}
```

Example: New member added

This example shows a message that is part of an onboarding app. The message is sent when a new person is added to a team channel or user group within Slack. This app sends along a `new_teammate` event with corresponding metadata:

```
POST /api/chat.postMessageHost: slack.comAuthorization: Bearer xoxb-6050345600-60510457-…Content-type: application/json; charset=utf-8{    "channel": "C123ABC456",    "text": "New teammate @Billy just joined",    "metadata": {        "event_type": "new_teammate",        "event_payload": {            "id": "TK-2132",            "summary": "New teammate has been added to the channel",            "description": "@Billy is a new teammate and needs to be added to the necessary channels",            "priority": "HIGH",            "resource_ type": "TASK"        }    }}
```

You can then have a Slack app that performs other actions, such as:

*   adds @Billy to other team channels
*   Sends a direct message containing the `description` field contents
*   Sends a direct message to people in channel reminding them to post a welcome message
*   Send an ephemeral message to @Billy with suggested channels to join

Example: External feedback received via webhook

This example shows how you can use message metadata from an external source using [webhooks](/messaging/sending-messages-using-incoming-webhooks). Your app can listen for posts from a website where users can post feedback. When a post does occur, your app posts a message in #feedback-channel with metadata attached:

```
POST /api/chat.postMessageHost: slack.comAuthorization: Bearer xoxb-6050345600-60510457-…Content-type: application/json; charset=utf-8{    "channel": "C123ABC456",    "text": "New feedback received",    "metadata": {        "event_type": "feedback_received",        "event_payload": {            "id": "TK-2132",            "summary": "User submitted feedback",            "description": "Someone submitted feedback on this page",            "feedback_message":"This page is awesome, thanks for writing it!",            "page_url": "http://docs.slack.dev",            "priority": "LOW",            "page_owner": "@haile",            "resource_ type": "TASK"        }    }}
```

You can then have a Slack app that performs other actions, such as:

*   reacts to the feedback submissions
*   assigns the task to a user in the channel.
*   sends direct messages to the `page_owner` found in the `event_payload`

The number of actions being triggered is up to you and your app's utilization of message metadata.

* * *

## Receiving metadata {#receiving_metadata}

Your app may also _receive_ metadata. This can be done with either the Web API or the Events API.

### Receive metadata with the Web API {#direct}

Message metadata is received via any way that apps send messages, such as [`conversations.history`](/reference/methods/conversations.history), or [response urls](/interactivity/handling-user-interaction#setup).

If you receive a message by directly calling an API method and passing `include_all_metadata=true`, you will find a new `metadata` parameter in the message object with two keys: `event_type` and `event_payload`. If you do not pass `include_all_metadata=true`, you will receive the `event_type` field only.

Field

Type

Description

`event_type`

string

The type of the event triggered in your system. For example, `task_added`.

`event_payload`

object

This payload contains the **custom properties** that you've already defined in your `.yaml` file for your app.

Make a call with the [`conversations.history`](/reference/methods/conversations.history) method to read metadata when you fetch a conversation's history:

```
GET /api/conversations.history?channel=C1234224&include_all_metadata=trueHOST: slack.comAuthorization: Bearer xoxb-12501860787-17163110960-...
```

The response will include metadata within the message object:

```
{    "ok": true,    "messages": [        {            "type": "message",            "user": "U123ABC456",            "text": "New task Added by @sam - Redesign homepage",            "app_id": "A01234",            "metadata": {                "event_type": "task_added",                "event_payload": {                    "id": "11223",                    "title": "Redesign homepage",                    "creator": "sam@acme-corp.com",                    "created_at": "1610561787",                    "priority": "high",                    "status": "triage"                }            },            "ts": "1512085950.000216"        },        {            "type": "message",            "user": "U123ABC456",            "text": "I'm going to start working on :point_up: task",            "ts": "1512104434.000490"        }    ],    "has_more": true,    "pin_count": 0,    "response_metadata": {        "next_cursor": "bmV4dF90czoxNTEyMDg1ODYxMDAwNTQz"    }}
```

### Receive metadata with the Events API {#events}

You can also receive metadata by obtaining messages in an event-driven way. Along with `metadata`, you'll see an `app_id` in the message payload so that you can identify which app sent the metadata. There are two ways to consume these message objects:

#### Subscribe to all message events {#message_events}

You can receive message metadata when you subscribe to the [`messages.*`](/reference/events/message) events. If a message has metadata, it will be available in the event payload.

```
{    "event": {        "type": "message",        "channel": "C123ABC456",        "user": "U123ABC456",        "text": "New task Added by @sam - Redesign homepage",        "app_id": "A123ABC456",        "metadata": {            "event_type": "task_added",            "event_payload": {                "id": "11223",                "title": "Redesign homepage",                "creator": "sam@acme-corp.com",                "created_at": "1610561787",                "priority": "high",                "status": "triage"            }        },        "ts": "1355517523.000005",        "event_ts": "1355517523.000005",        "channel_type": "channel"    }}
```

#### Subscribe specifically to metadata via the Events API {#specific_events}

Finally, you can subscribe _specifically_ to a set of events that tell you when metadata has been posted, updated, or deleted, without consuming an entire firehose of messages. This requires three steps:

1.  Configure your Slack app to request the [`message_metadata:read`](/reference/scopes/metadata.message.read) scope.
    
2.  Subscribe to the following events, as needed:
    

Event

Description

[`message_metadata_deleted`](/reference/events/message_metadata_deleted)

Message metadata was deleted

[`message_metadata_posted`](/reference/events/message_metadata_posted)

Message metadata was posted

[`message_metadata_updated`](/reference/events/message_metadata_updated)

Message metadata was updated

3.  Within your app's manifest file under `settings`, add in your `metadata_subscriptions` under `event_subscriptions`. Each entry requires an `app_id` and `event_type` pair where either (but not both) can be a wildcard `'*'`. Due note that it's best practice to not use the wildcard unless you really need to!

```
settings:  event_subscriptions:    request_url: https://example.ngrok.io/slack/events    bot_events:      - message_metadata_posted    metadata_subscriptions:      - app_id: '*'        event_type: <your-event-name>      - app_id: A1234        event_type: <your-event-name>
```

These events allow you to be updated on the goings on of the message metadata being consumed by your app.