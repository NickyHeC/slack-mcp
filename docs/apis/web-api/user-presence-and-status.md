Source: https://docs.slack.dev/apis/web-api/user-presence-and-status

# User presence and status

Slack users can toggle whether they are marked active or away. They can also set their own custom status, informing their workspace not only that they are _at lunch_, but exactly what they are eating.

## Custom status {#custom-status}

![A set custom status as it appears within a conversation](/assets/images/custom_status_in_message-51386d118b32dd816a7c5f36effabd76.png)

Users can declare their status by selecting a custom emoji icon and string of text to represent their "current status" — maybe they're in another office, on the good old telephone, sailing, vacationing in the sticks, or possibly eaten by a grue.

Some users want to fly the freak flag and use this space to wax poetic while others won't touch the stuff, or only in the most perfunctory way.

We encourage developers to embrace all the ways users and workspaces enjoy utilizing custom status. Slack is where workplay happens.

Custom status is part of a user's profile and setting status requires the `users.profile:write` scope. At this time, bot users do not have a user profile and do not have a status.

Admins on paid teams may also set a user's status by passing the `user` parameter to the [`users.profile.set`](/reference/methods/users.profile.set) method.

### Reading statuses {#reading-statuses}

Determine a user's currently set custom status by consulting their profile. You'll find profiles attached to user objects returned by [`users.list`](/reference/methods/users.list) and [`users.info`](/reference/methods/users.info). Both methods require the `users:read` OAuth scope.

More directly retrieve status for a specific user with [`users.profile.get`](/reference/methods/users.profile.get) with the `users.profile:read` scope.

A user's custom status is represented by the `status_text`, `status_emoji`, and `status_expiration` profile attributes.

*   `status_text` - a string of no more than 100 characters; does not support markup or other formatting, like user mentions. May contain `:emoji:` references.
*   `status_emoji` - a string corresponding to an emoji installed on the workspace. Animated emoji will appear frozen. When clearing the attribute, a default emoji (currently `💬` / `:speech_balloon:`) will be selected for the user.
*   `status_expiration` - an integer specifying seconds since the epoch, more commonly known as "UNIX time". When it becomes this time, the status will be reset. When `0` or omitted, the status does not expire.

To be notified when status and other profile fields change, subscribe to [`user_change`](/reference/events/user_change) events in the [Events API](/apis/events-api/) or use the [RTM API](/legacy/legacy-rtm-api) to stream and monitor.

### Writing custom statuses {#writing-custom-statuses}

Set a user's custom status by using their access token with [`users.profile.set`](/reference/methods/users.profile.set) and the `users.profile:write` scope.

You'll need to provide the `profile` parameter a URL-encoded JSON string containing at least the `status_text` attribute.

For example, to set a non-expiring custom status of `riding a train` with an emoji set to this idyllic scene: `🚞`, build a JSON payload like this:

```
{    "status_text": "riding a train",    "status_emoji": ":mountain_railway:",    "status_expiration": 0}
```

Next, place the custom status fields within the user's `profile` and use [`users.profile.set`](/reference/methods/users.profile.set). In this example, we're posting with JSON and using a user token :

```
POST /api/users.profile.setHost: slack.comContent-type: application/json; charset=utf-8Authorization: Bearer xoxp_secret_token{    "profile": {        "status_text": "riding a train",        "status_emoji": ":mountain_railway:",        "status_expiration": 0    }}
```

As with other profile fields, these fields may be set on their own or while updating multiple profile fields.

To unset a user's custom status, set both `status_text` and `status_emoji` to empty strings: `""`.

When sending a `application/x-www-form-urlencoded`\-based HTTP POST instead, you must provide the `profile` parameter as a URL-encoded string of JSON. We recommend using `application/json` to avoid any encoding errors.

### Expiring custom statuses {#expiration}

Automatically expire a custom status by setting `status_expiration` to an integer-based Unix timestamp, like `1532627506`.

For example, to set a custom status of `🚞 riding the train home` and have it expire on July 26th, 2018 at 17:51:46 UTC, construct this JSON payload:

```
{    "status_text": "riding the train home",    "status_emoji": ":mountain_railway:",    "status_expiration": 1532627506}
```

That's how to sync status with calendars, cubicles, conference calls, and bathroom stalls.

* * *

## User presence {#user-presence}

A user can have one of two possible presence values, `active` or `away`. A user is active if they have at least one client connected to Slack, and they are not marked as "away". There are two ways a user can be marked as away: automatic and manual.

### Automatic away {#automatic-away}

The Slack message servers will automatically detect activity in the client. After 10 minutes with no activity, the user is automatically marked as `away`. There is some additional nuance to that dependent on the client, explained in detail in our [Help Center](https://slack.com/help/articles/201864558#desktop-3).

These auto-away rules do not apply to [Bot Users](/authentication/tokens#bot).

### Manual away {#manual-away}

An application can call [`users.setPresence`](/reference/methods/users.setPresence) to manually mark a user as `away` or `auto`. A manual status set using this method will persist between connections.

A manual `away` status set using this method overrides the automatic presence determined by the message server.

Setting presence back to `auto` indicates that the automatic status should be used instead. There's no way to force a user status to `active`.

## Bot presence {#bot-presence}

[Bot users](/authentication/tokens#bot) have their own form of being present on Slack.

When marked `away`, bots will have a grey circle next to their name. Many users interpret this demarcation to mean your bot is not currently available.

And when they are `active`, bots will have a green dot there. Users have been known to consider your green dot a badge of conversational readiness.

It's either/or. `away` or `active`. Grey or green (or maybe grey and orange — the color of the active dot may vary when [different Slack client themes](https://slack.com/intl/en-ie/help/articles/205166337-Change-your-Slack-theme) are used).

Please don't use presence to telegraph Morse code or teach your bot to speak the binary language of moisture vaporators. Use [`chat.postMessage`](/reference/methods/chat.postMessage) for that.

### Events API bots {#events-api-bots}

If your bot user runs on the [Events API](/apis/events-api/), you can only toggle your bot's `active` or `away` status by [managing your app](https://api.slack.com/apps) and its _Bot Users_ panel, or for apps published in the Slack Marketplace, on the _Live App Settings_ panel.

![Toggling bot user presence for the events API](data:image/png;base64,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)

When set to _Off_, your bot user is only marked as online if it's connected to the RTM API.

When set to _On_, your bot user will be marked as _active_ and present. That green dot is all yours. Just toggle back _Off_ again to be marked _away_.

Your bot user's [profile](/reference/methods/users.profile.get) will include a `always_active` field set to `true`. Counter-intuitively, your bot's `presence` field will remain `away`. That's the bad news.

The good news is that `always_active` will be interpreted by Slack clients as if the bot user's presence were `active`. Yes, you're awarded that green dot.

### RTM bots {#rtm-bots}

If your bot user runs on the [RTM API](/legacy/legacy-rtm-api), your bot will be marked `active` to users whenever connected to the RTM API.

Bots cannot set their presence to `active` with [`users.setPresence`](/reference/methods/users.setPresence). RTM bots _can_ use it to set it to `away`. Or you can always automatically mark your bot as `away` by disconnecting from your websocket.

## Determining user presence {#determining-user-presence}

RTM API Presence is now only available via subscription

As of January 2018, [`presence_change`](/reference/events/presence_change) events are not dispatched without [_presence subscriptions_](/apis/web-api/user-presence-and-status) established with [`presence_sub`](/reference/events/presence_sub). Relatedly, current user presence status is no longer communicated in [`rtm.start`](/reference/methods/rtm.start). [Learn more](/changelog/2018-01-presence-present-and-future).

### Presence subscriptions over RTM {#subscriptions}

Presence subscriptions are required to track `presence_change` events over RTM.

Subscribe to `presence_change` events for specific users by sending a [`presence_sub`](/reference/events/presence_sub) event into the websocket.

For instance, to subscribe to `presence_change` events for users `U123456` and `W123456`, write the following JSON blob into an established websocket:

```
{    "type": "presence_sub",    "ids": [        "U123456",        "W123456"    ]}
```

The message server will respond with `presence_change` events indicating the current presence state of any users added to the presence subscription.

Here's what you need to know about presence subscriptions:

*   You must declare your entire list of user IDs to subscribe to in _**each**_ request.
    *   Add users by appending them to your array of `ids`.
    *   Remove users by removing them from your array of `ids`.
*   Subscribing to all user's presence events requires specifying every user's ID. This is not recommended, especially on large workspaces.
    *   For best results, limit subscriptions to only those users you absolutely need presence information for. 500 users is a good maximum.
*   Presence subscriptions work best with [batched](#batching) `presence_change` events.
*   Upon connecting, your app will have no presence subscriptions.
*   Presence subscriptions only last the duration of a websocket session. Disconnecting means needing to subscribe again.
*   By specifying an [Enterprise org](/enterprise) user ID belonging to a user on another workspace within the same Enterprise organization, your app can subscribe to cross-workspace `presence_change` events.

Presence subscriptions are now effectively required, as of January 2018. [Learn more](/changelog/2018-01-presence-present-and-future).

`presence_sub` is rate limited and there are upper bounds to the amount of data posted in a single event.

### Presence querying with the RTM API {#presence-querying-rtm}

Writing a [`presence_query`](/reference/events/presence_query) event to the WebSocket will perform a query operation for a list of up to 500 user IDs.

To look up users `U123456` and `W123456`, send a query like:

```
{    "type": "presence_query",    "ids": [        "U123456",        "W123456"    ]}
```

In response, you'll receive [`presence_change`](/reference/events/presence_change) events for the matching users.

`presence_query` is rate limited and there are upper bounds to the amount of data posted in a single event.

### Presence querying with the Web API {#presence-querying-web}

When using our [Web API](/apis/web-api/), you can call the [`users.getPresence`](/reference/methods/users.getPresence) method to get the user's current presence value.

### Presence subscriptions over Events API {#presence-querying-events}

Presence-related events cannot be tracked using the [Events API](/apis/events-api/) at this time.

### Batched presence events {#batching}

Traditionally, using the [Real Time Messaging API](/legacy/legacy-rtm-api) the initial call to [`rtm.start`](/reference/methods/rtm.start) or [`rtm.connect`](/reference/methods/rtm.connect) would include the current presence value for every member of your workspace. If their presence value changes after that, a [`presence_change`](/reference/events/presence_change) event would be sent.

Now presence events must be batched together into a special version of the `presence_change` event that includes a `users` array instead of a singular `user` field. You must enable this new behavior by passing the `batch_presence_aware=1` parameter to `rtm.start` or `rtm.connect`. `presence_change` events will otherwise no longer dispatch after November 15, 2017.

Initial presence state is no longer described when connecting to [`rtm.start`](/reference/methods/rtm.start).