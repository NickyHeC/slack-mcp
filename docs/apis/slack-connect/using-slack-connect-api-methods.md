Source: https://docs.slack.dev/apis/slack-connect/using-slack-connect-api-methods

# Using Slack Connect API methods

[Slack Connect](/apis/slack-connect/) allows users between different workspaces and organizations to work together on Slack.

Slack Connect API methods offer capabilities for managing and automating your Slack Connect processes. Here's some of the ways these API methods can empower you:

✨ Invite users from external organizations to new channels and accept Slack Connect channel invitations when installed on the target workspace.

✨ Integrate Slack Connect management into your onboarding and offboarding processes. Automatically invite new partners and collaborators, or disconnect from those who are leaving.

✨ Schedule regular audits and maintenance tasks to keep your Slack Connect connections current and secure. Automate the disconnection of outdated or unnecessary connections.

Read on for more details and use cases.

* * *

## Creating an app to interact with Slack Connect {#create}

You can use Slack Connect API methods within both apps created with the Deno Slack SDK and Bolt apps. They are set up differently, however.

To create an app with the Deno Slack SDK, head to the [Deno Slack SDK quickstart](/tools/deno-slack-sdk/guides/getting-started). We also recommend reading our [Governing Slack Connect invites](/tools/deno-slack-sdk/tutorials/governing-slack-connect-invites) guide for an example on using Slack Connect API methods, scopes, and events with the Deno Slack SDK and the Slack CLI.

Scopes are given to apps within the [App manifest](/tools/deno-slack-sdk/guides/using-the-app-manifest). Apps created with the Deno Slack SDK can't subscribe to events, but can have an [event trigger](/tools/deno-slack-sdk/guides/creating-event-triggers) for some events. All the events listed on this page have corresponding event triggers.

To create a granular bot app, head to the [quickstart](/app-management/quickstart-app-settings) guide and [create a new app](https://api.slack.com/apps?new_app=1). Scopes are given to granular bot apps within the _App Settings_. Granular bots can subscribe to events within the _Events API_ section of the _App Settings_ page.

* * *

## Managing your app's Slack Connect invitations {#managing-app-invitations}

Your app can be invited to a Slack Connect Channel. Use the [`shared_channel_invite_received`](/reference/events/shared_channel_invite_received) event to be notified when suitors call.

The `shared_channel_invite_received` event is fired when a shared channel invite was sent. This event will fire **only** if the [`conversations.inviteShared`](/reference/methods/conversations.inviteShared) API method is called to invite an app to a Slack Connect channel.

### Accept invitations {#accept}

In order for your app to _act_ upon the invite, it'll need to have the proper scopes:

*   [`conversations.connect:read`](/reference/scopes/conversations.connect.read) — This scope allows your app to handle events when your app is invited to a Slack Connect channel.
*   [`conversations.connect:write`](/reference/scopes/conversations.connect.write) — This scope allows your app to send and accept invitations to Slack Connect and receive events when invitations are accepted.

Use the [`conversations.acceptSharedInvite`](/reference/methods/conversations.acceptSharedInvite) method to accept an invite to a Slack Connect channel. You'll have the option to name the channel if the channel hasn't already been created yet by passing the `channel_name` parameter. Provide the invitation ID from the [`shared_channel_invite_received`](/reference/events/shared_channel_invite_received) event response.

You can also use the `free_trial_accepted` parameter to start a free trial for your workspace in order to use Slack Connect, as long as you're eligible.

* * *

## Inviting users to Slack Connect channels {#invite-users}

Your app can invite users from external organizations to a channel, turning the channel into a Slack Connect channel in the process.

It'll need the proper scope:

*   [`conversations.connect:write`](/reference/scopes/conversations.connect.write) — This scope allows your app to send and accept invitations to Slack Connect and receive events when invitations are accepted.

Then use the [`conversations.inviteShared`](/reference/methods/conversations.inviteShared) method to invite users via email or via user ID.

If your app is already installed on the target organization, you can invite it directly and therefore automate both inviting and accepting invitations in order to connect two or more organizations.

Your app does **not** need to handle approval of Slack Connect in order to invite users. You can invite users and then wait for manual approval by Admins if that approval is necessary on your workspace or the target workspace.

Many workspaces require **approval** by an Admin for Slack Connect channels (in addition to a user accepting an invitation). Alternatively, you can manage approval of the channel invitations.

* * *

## Managing workspace invitations {#manage-workspace-invitations}

Since many workspaces require Admin approval for the creation of Slack Connect channels, your app can manage that task, with the help of an installing user who grants your app a user token. If the installing user has the authority to manage Slack Connect approval, you're good to go — your app can make use of that authority in the user's stead.

The following events help you stay on top of workspace invitations.

*   [`shared_channel_invite_accepted`](/reference/events/shared_channel_invite_accepted) — This event notifies your app when an invite sent by your workspace or organization has been accepted.
*   [`shared_channel_invite_approved`](/reference/events/shared_channel_invite_approved) — This event notifies your app when an invitation has been approved.
*   [`shared_channel_invite_declined`](/reference/events/shared_channel_invite_declined) — This event notifies your app when an invitation has been declined.

In order for your app to _act_ upon the the invitations, it'll need to have the proper scope:

*   [`conversations.connect:manage`](/reference/scopes/conversations.connect.manage) — This scope allows your app to approve, decline, or list Slack Connect invitations. Since approval requires more authority than accepting invitations, apps with this feature can only be installed by a workspace owner or admin.

### Approve invitations {#approve-invitations}

With the `conversations.connect:manage` scope, your app can call the [`conversations.approveSharedInvite`](/reference/methods/conversations.approveSharedInvite) method to approve a pending invitation. Provide the invitation ID from the [`shared_channel_invite_accepted`](/reference/events/shared_channel_invite_accepted) event response.

You can approve from the perspective of the originating organization _or_ the target organization, depending on where your app is installed.

### Decline invitations {#decline-invitations}

You can also decline pending invitations with the [`conversations.declineSharedInvite`](/reference/methods/conversations.declineSharedInvite) method. Provide the invitation ID from the [`shared_channel_invite_accepted`](/reference/events/shared_channel_invite_accepted) event response.

### List invitations {#list-invitations}

To list shared channel invites that have been generated or received but have not been approved by all parties, use the [`conversations.listConnectInvites`](/reference/methods/conversations.listConnectInvites) method. If your app is installed at the organization level, you'll be able to list all the pending invitations in all workspaces, but you can also specify a particular channel.

### Governing invitations {#govern-invitations}

You can choose to add an approval step to the Slack Connect process before invitations are sent to external people.

We have a dedicated guide on automating the governing of Slack Connect invitations!

Visit the [Governing Slack Connect invites](/tools/deno-slack-sdk/tutorials/governing-slack-connect-invites) page for all the details.

If you choose to apply automation rules before channel invitations are sent, you can listen for the [`shared_channel_invite_requested`](/reference/events/shared_channel_invite_requested) event. You can also list all the requests needing approval before being sent with the [`conversations.requestSharedInvite.list`](/reference/methods/conversations.requestSharedInvite.list) method.

When enabled, external user invitations will not be sent until they are approved to send. To approve an invitation to be sent, use the [`conversations.requestSharedInvite.approve`](/reference/methods/conversations.requestSharedInvite.approve) API method. To deny an invitation to be sent use the [`conversations.requestSharedInvite.deny`](/reference/methods/conversations.requestSharedInvite.deny) API method.

* * *

## Viewing connected organizations and users {#view-connected}

You can use Slack Connect API methods to find information on connected organizations and users. The relevant methods will require a Slack Connect specific scope: the [`conversations.connect:manage`](/reference/scopes/conversations.connect.manage) scope.

To view details about external teams connected via Slack Connect, use the [`team.externalTeams.list`](/reference/methods/team.externalTeams.list) method.

To look up if a specific user is on Slack (and is also [discoverable](https://slack.com/help/articles/5535749574803-Manage-Slack-Connect-discoverability-for-your-organization)), use the [`users.discoverableContacts.lookup`](/reference/methods/users.discoverableContacts.lookup) method.

* * *

## Setting Slack Connect channels posting permissions {#set-permissions}

Slack Connect channels have two types of posting permissions:

*   _Permission only to post_
*   _Permission to post, invite, and more_

You can pick the permission level using the [`conversations.externalInvitePermissions.set`](/reference/methods/conversations.externalInvitePermissions.set) method. Be sure to provide your app the [`conversations.connect:manage`](/reference/scopes/conversations.connect.manage) scope.

* * *

## Disconnecting a Slack Connect channel {#disconnect}

Your app can disconnect Slack Connect channels. It'll need the proper _Admin_ scope:

*   [`admin.conversations:write`](/reference/scopes/admin.conversations.write) — This scopes allows your app to start new conversations, modify conversations and modify channel details.

Then use the [`admin.conversations.disconnectShared`](/reference/methods/admin.conversations.disconnectShared) method to disconnect the Slack Connect channel.

### Disconnect all Slack Connect channels from another organization {#disconnect-all}

To sever all ties with another organization, you can disconnect all Slack Connect channels and direct messages (DMs) from that organization.

You'll need the proper `write` scopes for all relevant message types, alongside the [`conversations.connect:manage`](/reference/scopes/conversations.connect.manage) scope.

Then use the [`team.externalTeams.disconnect`](/reference/methods/team.externalTeams.disconnect) method and say goodbye.

Gone, but not forgotten.

Disconnecting from an organization ends all communication, but depending on permissions, still allows access to conversation history. Refer to [this help center article](https://slack.com/help/articles/360063030933-Slack-Connect--Disconnect-from-an-organization-) for the expected behavior of disconnecting conversations.