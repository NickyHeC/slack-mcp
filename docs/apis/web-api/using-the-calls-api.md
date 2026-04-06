Source: https://docs.slack.dev/apis/web-api/using-the-calls-api

# Using the Calls API

You can integrate your calls with Slack so that they're more interactive, less intrusive, and easier for users to join.

Your call app will appear in the Slack client natively, under the Call icon, if you choose.

Whenever someone starts or shares a call, it appears in Slack with all the bells and whistles: a list of participants, a join button, and information about the call.

## Overview {#overview}

The Calls API provides a way for your call app to tell Slack about the calls you're making between users.

It's important to know that Slack doesn't make the call. The API allows you to do your work and include your call, pleasantly and productively, within the Slack client. In exchange, Slack allows users to start, end, and enter your Calls from inside Slack.

To make things clearer, when we refer to your app's 3rd-party call, we'll use a lowercase "c". The full Call inside Slack will be capitalized.

Slack also shows off your call natively, with lists of participants, a join button, and metadata.

Slack also shows off your call natively, with lists of participants, a join button, and metadata.

![Image of a call object generated from a link](/assets/images/calls_link_shared-1020977528ab258e5cfff54fc921cf5f.png)

There are two ways for your app to integrate with Slack so that users can initiate and deal with Calls within Slack.

One way for a user to initiate your app is via a slash command, for example, by typing `/mycallapp` into the message composer. The other way for a user to initiate your app is directly via the Call icon.

These two interaction patterns work the same for your app. Once you decide on one or the other, only the [app setup](#setup) is different. The payloads you receive are the same, and the way that you use the API methods to inform Slack about your calls remains the same as well.

## App setup {#setup}

Users of non-partnered apps will need to initiate Calls using a [slash command](/interactivity/implementing-slash-commands).

To get started, [create your Slack app](https://api.slack.com/apps). Under the **Add features and functionality** header, select the **Slash Commands** button and then **Create a New Command**. Setting up your slash command app here is exactly the same as documented in the [slash command documentation](/interactivity/implementing-slash-commands).

Don't worry too much about the Request URL (the URL where Slack will send information about users interacting with calls to your app). You can change that later. You can also change the name of the command later.

You'll need two scopes for interacting with calls:

*   [`calls:read`](/reference/scopes/calls.read)
*   [`calls:write`](/reference/scopes/calls.write)

Request these two scopes under the **OAuth & Permissions** sidebar (scroll down to the **Scopes** section). Then click the **Install App to Workspace** button. You're all ready to work with Calls.

## Call functions: dialing to hanging up and everything in between {#functions}

If you want to give users a smartphone for their calling needs, there are several different features you'll want to provide. Initiating and rejecting a Call are the starting point, but far more can happen.

The five main actions that a smart Call app has to handle are: [initiation of a Call](#initiation), [unfurling a link to a Call](#unfurling), [responding to a rejected Call](#rejection), [updating Call info and adding/removing participants](#updating), and finally [hanging up a Call](#ending).

Next, we'll go through each in a bit more detail, starting with [Call initiation](#initiation).

### Responding to a Call initiation {#initiation}

When a user initiates a call with your app, either by using a slash command or the Call icon, Slack sends a payload to your app.

For example, if the call is initiated with the Call icon, your app might receive the following in an HTTP POST request:

```
{    "token": "<verification token>",    "team_id": "T123ABC456",    "team_domain": "my-team",    "channel_id": "C123ABC456",    "channel_name": "test",    "user_id" : "U123ABC456",    "user_name": "mattjones",    "response_url":"https://slack.com/callback/123xyz",    "type": "video"}
```

If the call is initiated with a slash command (e.g., `/mycall`), expect a normal [slash command payload](/interactivity/implementing-slash-commands#app_command_handling) sent to your app instead.

In turn, your app makes two responses—maybe three, if you include posting the Call to a channel afterward.

Note that in the payload, the `token` property is deprecated and can be ignored. Slack now uses [signed secrets](/authentication/verifying-requests-from-slack) for verification.

#### 1. Immediate response {#immediate_response}

First up is an immediate, synchronous response within 3 seconds. This quick acknowledgement tells Slack where to send the calling user, and only applies when a user starts a call from a Call button—not a slash command.

Post your response to the `response_url` indicated in the payload you receive. If you're implementing a calls slash command, the `response_url` isn't needed: see the [register the call with Slack](#register_call) and [post the Call to channel](#post_to_channel) steps.

In reference to the example above, you'd therefore respond by pinging `https://slack.com/callback/123xyz` with:

```
{    "response_type":"call",    "call_initiation_url":"https://join.call.com/123456",    "desktop_protocol_call_initiation_url": "call://join&room_id=123456"}
```

The specified `call_initiation_url` will be automatically opened for the initiating user in a separate window.

Sometimes, you might prefer to use a custom URL scheme to launch your app in desktop directly. If you wish, include the `desktop_protocol_call_initiation_url` optional field, representing the URL that will be used to launch your calls app directly. If you don't include it, Slack will fallback by launching `call_initiation_url` in a new browser window.

You'll always need to include the regular `call_initiation_url` in case a user doesn't have, or doesn't want, your app to be launched in desktop.

A `type` might be included in the payload sent to your app to indicate whether the call should be `audio` or `video`. For `video`, you don't need to do anything special except make sure your initiation URL begins a video. For `audio`, you'll receive a `phone_number`, and you'll want to make use of that in your response to Slack.

Example response:

```
{    "response_type": "audio",    "call_initiation_url": "https://your_company_url/...",    "desktop_protocol_call_initiation_url": "your_call_app_url://+1-202-555-0145"}
```

#### 2. Register the call with Slack {#register_call}

After you've made your quick response to Slack with a redirect `call_initiation_url`, you'll want to actually register the details of the call with Slack. Use the [`calls.add`](/reference/methods/calls.add) method to add the Call to Slack.

You'll receive an `id` from Slack in the response. Make sure you store the Call's `id`, since you'll need it to reference the call if you want to [update](#updating) or [end](#ending) the Call.

#### 3. Post the Call to channel {#post_to_channel}

As a courtesy, post the Call to channel so the people in it know about the Call. Use the [`chat.postMessage`](/reference/methods/chat.postMessage) method with a `call` block:

```
"blocks": [    {        "type": "call",        "call_id": "R123",    }]
```

Your app might not have permission to post to private channels, multi-party direct messages, or direct messages in order to post a call block via the usual [chat.postMessage](/reference/methods/chat.postMessage) method. In that case, use the `in_channel` slash command response type. This posts a message directly to the channel the slash command request originated from, and can include a `call` block:

```
{    "response_type": "in_channel",    "text": "A new call was started by <name of call provider>",    "blocks": [{        "type": "call",        "call_id": "R123",    }]}
```

#### The users parameter {#users}

When you register a Call with the [`calls.add`](/reference/methods/calls.add) method, add participants with the [`calls.participants.add`](/reference/methods/calls.participants.add) method, or remove them with the [`calls.participants.remove`](/reference/methods/calls.participants.remove) method, you'll notice a `users` parameter.

Each method requires `user` objects to include either a `slack_id` or `external_id`, or both.

A `slack_id` is the `id` of the user in Slack—you might receive this when interacting with any Slack API method, such as the [`conversations.members`](/reference/methods/conversations.members) method. An `external_id` may be used if you don't know the `slack_id` for your users. In this case, `external_id` is a unique id created by your app for your users.

Here's an example `users` array containing two users identified in those two distinct ways:

```
[    {        "slack_id": "U123ABC456",    },    {        "external_id": "54321678",        "display_name": "Kim Possible",        "avatar_url": "https://callmebeepme.com/users/avatar1234.jpg"    }]
```

If you aren't using the `application/json` Content-type, remember to encode `users` appropriately for the Content-type you send.

### Unfurling a link to a Call {#unfurling}

Subscribe to the [`link_shared`](/reference/events/link_shared) and [`call_rejected`](/reference/events/call_rejected) events in your [app settings page](https://api.slack.com/apps) under **Event Subscriptions**, if you haven't already. Reinstall your app afterward.

Slack notifies your app with a `link_shared` event whenever a link from a specified domain (i.e., your app's domain representing calls) is shared.

Similar to [Call initiation](#initiation), your app should respond to the `link_shared` event with the [`calls.add`](/reference/methods/calls.add) method to register the call. You'll receive an `id` from Slack in the response. Make sure you store the Call's `id`, since you'll need it to reference the call here and elsewhere.

In this case, you'll then invoke the [`chat.unfurl`](/reference/methods/chat.unfurl) method. That way, you unfurl a Call in channel, already populated with the Call's duration and participants.

Here's an example call to `chat.unfurl`, supplying a `call_id` received from `calls.add`:

```
{    "token": "xxxx-xxxxxxxxx-xxxx",    "channel": "C123ABC456",    "ts": "12345.6789",    "unfurls": {        "https:\/\/url.to\/your\/call": {            "blocks": [{                "type": "call",                "call_id": "Rxxx"            }]        }    }}
```

### Responding to a rejected Call {#rejection}

Slack notifies your app with a `call_rejected` event whenever a Call is rejected by an invited user. Here's an example payload your app might receive:

```
{    "token": "12345FVmRUzNDOAuy4BiWh",    "team_id": "T123ABC456",    "api_app_id": "B123ABC456",    "event": {        "type": "call_rejected",        "call_id": "RL731AVEF",        "user_id": "U123ABC456",        "channel_id": "D123ABC456",        "external_unique_id": "123-456-7890"    },    "type": "event_callback",    "event_id": "Ev123ABC456",    "event_time": 1563448153,    "authorizations": [        {            "user_id": "U123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],}
```

Your app can then choose to handle the rejected call according to its own logic.

### Updating a Call and its participants {#updating}

Use the [`calls.update` method](/reference/methods/calls.update) to update a Call's `title`, `join_url`, or `desktop_app_join_url`.

Use the [`calls.participants.add`](/reference/methods/calls.participants.add) method and the [`calls.participants.remove`](/reference/methods/calls.participants.remove) method to add or remove participants.

The Call object in channel will update automatically with any of these changes.

### Hanging up a Call {#ending}

When a call ends, update the Call object in Slack by calling the [`calls.end`](/reference/methods/calls.end) method.

![Image of a call that has ended](/assets/images/calls_end-f463e562daf9003677a75c0ad5b31a04.png)