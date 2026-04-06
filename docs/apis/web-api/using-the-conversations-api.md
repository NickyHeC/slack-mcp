Source: https://docs.slack.dev/apis/web-api/using-the-conversations-api

# Using the Conversations API

_Public channels, private channels, DMs... They're all conversations!_

The Slack Conversations API provides you with a unified interface to work with all the channel-like things encountered in Slack: public channels, private channels, direct messages, group direct messages, [shared channels](/apis/slack-connect/), and so on.

Use this [API family](/reference/methods?family=conversations) to [review history](/reference/methods/conversations.history), [create](/reference/methods/conversations.create) or [archive](/reference/methods/conversations.archive) channels, [invite](/reference/methods/conversations.invite) team members, [set conversation topics](/reference/methods/conversations.setTopic) and [purpose](/reference/methods/conversations.setPurpose), and more — no matter what type of conversation you're working with.

The types of channels you interface with in the Conversations API are governed by corresponding [permission scopes](/reference/scopes). For example; to retrieve details about a public channel, you'll need the [`channels:read`](/reference/scopes/channels.read) scope. For details about a private channel, you'll need the [`groups:read`](/reference/scopes/groups.read) scope.

Use `conversations.*` methods to access anything channel-like. For example, the [`conversation.list`](/reference/methods/conversations.list) method returns information on public, private, and direct message channels, when accessed with the appropriate [permission scopes](/reference/scopes).

## Conversations API methods {#conversations-api-methods}

You can [view all the Conversations API methods in the reference](/reference/methods?family=conversations)

## Working with Shared Channels {#shared_channels}

Each channel has a unique-to-the-team ID that begins with a single letter prefix: either `C`, `G`, or `D`.

When a channel is shared across teams (see [Slack Connect: working with channels between organizations](/apis/slack-connect/)), the prefix of the channel ID may be changed, e.g. a private channel with ID `G0987654321` may become ID `C0987654321`.

This is one reason you should use the `conversations` methods instead of the previous API methods! You cannot rely on a private shared channel's unique ID remaining constant during its entire lifetime.

The channel type object tells you additional channel information. If the channel is shared, `is_shared` is set to `true`. If it is a private channel or a group DM channel, the properties `is_private` or `is_mpim` are set to `true`.

### The conversational booleans {#booleans}

Some of the most important fields in [conversation objects](/reference/objects/conversation-object) are the booleans indicating what kind of conversation/channel it is and how private it is. For a list of these booleans, refer to [conversation-related booleans](/reference/objects/conversation-object#booleans).

## Conversation membership {#membership}

Discover who is party to a conversation with [`conversations.members`](/reference/methods/conversations.members), a paginated method allowing you to safely navigate through very large (or tiny) collections of users.

## Permission scopes {#permission_scopes}

Your app's scopes act as a filter. They sort out the conversations you don't have access to, guaranteeing that Conversations API methods only return the conversations your app should see.

### Scopes for classic apps {#classic_app_scopes}

All Conversations API endpoints still accept _multiple_ scopes and filter access to channels based on the provided token's scope. If you have a scope that allowed you to use a deprecated conversation method, that scope will work with the Conversations API equivalent.

For instance, [`conversations.list`](/reference/methods/conversations.list) accepts [`channels:read`](/reference/scopes/channels.read), [`groups:read`](/reference/scopes/groups.read), [`mpim:read`](/reference/scopes/mpim.read), and [`im:read`](/reference/scopes/im.read).

If you only have `channels:read`, then `conversations.list` will only return public channels and all the related methods will only deal with public channels. If you have both `channels:read` and `im:read`, then methods will only return public channels and DMs, and so on.

## Pagination {#pagination}

The Conversations API uses our [cursor-based pagination model](/apis/web-api/pagination), improving the performance of requests over large sets of data.

Just set a `limit` on your first request, include the `next_cursor` found in `response_metadata` in the response as the `cursor` parameter in your next request and you're paginating with ease on the conversational trapeze. Unlike older methods, the Conversations API is paginated _by default_.

### Inconsistent page size is a feature, not a bug {#inconsistent-page-size-is-a-feature-not-a-bug}

Keep in mind that it's possible to receive fewer results than your specified `limit`, even when there are additional results to retrieve. Maybe you'll even receive 0 results but still have a `next_cursor` with 4 more waiting in the wings.

When looking up MPIMs using the `conversations.list`, you are likely to get far fewer results than requested number with a `next_cursor` value, although `next_cursor` will continue to indicate when more results await. For example, when requesting 100 MPIMs, it may return only 5.

## Known issues {#issues}

#### 🚧 Channel IDs can become unstable in certain situations {#-channel-ids-can-become-unstable-in-certain-situations}

There are a few circumstances where channel IDs might change within a workspace. You can use [`conversations.list`](/reference/methods/conversations.list) regularly to monitor change for known `#channel` names if ID stability is important to you.

In the future, we'll mitigate this unexpected transition with appropriate [Events API](/apis/events-api/) events or other solutions.

#### 🚧 MPIM events and channel types {#-mpim-events-and-channel-types}

In a Multiparty Direct Message Channel (MPIM) with a foreign user, events like [`member_joined_channel`](/reference/events/member_joined_channel) and [`member_left_channel`](/reference/events/member_left_channel) may dispatch an incorrect value for `channel_type`.

#### 🚧 IM object format is not yet consistent {#-im-object-format-is-not-yet-consistent}

IM formats may differ from other channel objects. We're working towards making all objects the same format. You may notice `members` lists that aren't meant to be there. These are almost all cleared up!

#### 🚧 Unsharing channels {#-unsharing-channels}

When a channel becomes unshared, [`conversations.history`](/reference/methods/conversations.history) access for the channel may become unreliable.