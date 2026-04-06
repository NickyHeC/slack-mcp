Source: https://docs.slack.dev/admins/managing-channels

# Managing channels

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

The APIs for channel management allow your app to create and control channels within your Enterprise organization. You can achieve anything with your app that could be done with a [Slack Admin's channel management tools](https://slack.com/help/articles/360047512554-Use-channel-management-tools).

That includes:

*   creating and deleting channels,
*   archiving and unarchiving channels,
*   connecting and disconnecting additional workspaces,
*   and setting posting preferences.

With the help of these APIs, you can streamline and automate the task of channel management, saving your admins time and making their lives more pleasant and productive.

## Set up with scopes {#scopes}

Two [scopes](/app-management/quickstart-app-settings#scopes) enable an app to manage channels across an Enterprise org:

*   The [`admin.conversations:read`](/reference/scopes/admin.conversations.read) scope allows the app to get information about channels.
*   The [`admin.conversations:write`](/reference/scopes/admin.conversations.write) scope allows the app to create and change channels.

All `admin.*` scopes are obtained using the normal [OAuth flow](/authentication), but there are a few extra requirements. The OAuth installation must:

*   be initiated by an Enterprise org admin or owner.
*   take place on the Enterprise org, not on an individual workspace, using the workspace switcher during the install flow.

![Installing the app on a workspace](/assets/images/workspace-v-org-audit-10f163aac79dc5f2c15e3ebe8267dbf4.png)

Check out the [scope documentation for more detail](/reference/scopes/admin.conversations.read).

## Manage channels {#basics}

Here are the methods for some of the most common things you'll want to do with channels:

Action

Method

Create a channel

[`admin.conversations.create`](/reference/methods/admin.conversations.create)

Delete a channel

[`admin.conversations.delete`](/reference/methods/admin.conversations.delete)

Invite some users

[`admin.conversations.invite`](/reference/methods/admin.conversations.invite)

Archive a channel

[`admin.conversations.archive`](/reference/methods/admin.conversations.archive)

Unarchive a channel

[`admin.conversations.unarchive`](/reference/methods/admin.conversations.unarchive)

Rename a channel

[`admin.conversations.rename`](/reference/methods/admin.conversations.rename)

Search for a channel

[`admin.conversations.search`](/reference/methods/admin.conversations.search)

Convert a public channel to private

[`admin.conversations.convertToPrivate`](/reference/methods/admin.conversations.convertToPrivate)

Convert a private channel to public

[`admin.conversations.convertToPublic`](/reference/methods/admin.conversations.convertToPublic)

The reference pages linked above are your best source of info for how to call these methods and what to expect in response.

If you have your channels up and running, you might want to make some modifications to who has permission to post messages and to respond in threads. If so, [read on](#prefs).

## Set and get posting preferences {#prefs}

You can decide exactly who can post messages in your channel, and who can respond inside threads with the following methods:

Action

Method

Set permissions

[`admin.conversations.setConversationPrefs`](/reference/methods/admin.conversations.setConversationPrefs)

Retrieve already set permissions

[`admin.conversations.getConversationPrefs`](/reference/methods/admin.conversations.getConversationPrefs)

Here's a quick primer on the [`admin.conversations.setConversationPrefs`](/reference/methods/admin.conversations.setConversationPrefs) method:

To set either who can post or who can respond in threads, you'll use the `prefs` argument with some stringified JSON. "Stringified JSON" means JSON with white space removed and fields marked by single quotations. Since this argument won't contain more complex characters, you don't need to do further encoding.

For example, to set who can post messages, use the `who_can_post` field inside your `prefs` argument:

```
"prefs": "{'who_can_post':'type:admin,user:U1234'}"
```

Inside your stringified JSON for `who_can_post`, you can specify who the permission applies to in a few different ways:

*   by `type`: you can include all `admin` users, or just all `user`s in general.
*   by `user`: you can specifically list users: `user:U123ABC456`.

The `can_thread` field works exactly the same inside the `prefs` object, only it determines who can respond in threads. You can pass both `who_can_post` and `can_thread` to the `prefs` argument in this method at the same time.

For example:

```
"prefs": "{'who_can_post':'type:admin,user:U1234','can_thread':'type:user'}"
```

## Connect and disconnect other workspaces {#connect}

You can handle connected workspaces for a channel with the following methods:

Action

Method

Set the connected workspaces for a channel. Any previously-connected workspaces you do not include will be disconnected.

[`admin.conversations.setTeams`](/reference/methods/admin.conversations.setTeams)

Retrieve the list of workspaces that have already been connected to a channel

[`admin.conversations.getTeams`](/reference/methods/admin.conversations.getTeams)

Disconnect a workspace from a channel

[`admin.conversation.disconnectShared`](/reference/methods/admin.conversations.disconnectShared)

The reference pages linked above are the best way to determine exactly how to call these methods and what to expect in response.

You can connect workspaces to a channel using the [`admin.conversations.setTeams`](/reference/methods/admin.conversations.setTeams) method.

But you can _also_ set a channel to be available across an entire Enterprise organization with the same method, just by setting the `org_channel` parameter to `true`.

[Check out the rest of our documentation](/admins) to see other ways that your app can aid Admins in managing Slack.