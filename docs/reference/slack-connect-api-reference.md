Source: https://docs.slack.dev/reference/slack-connect-api-reference

# Slack Connect API reference

[Slack Connect](/apis/slack-connect/) allows users between different workspaces and organizations to work together on Slack.

Below is a list of Slack Connect-related scopes, methods and events. For information on how to use these components together to address common use cases, see our [Using Slack Connect API methods](/apis/slack-connect/using-slack-connect-api-methods) guide.

## Scopes {#scopes}

Scope

Description

[`conversations.connect:read`](/reference/scopes/conversations.connect.read)

Receive Slack Connect invite events sent to the channels your slack app is in.

[`conversations.connect:write`](/reference/scopes/conversations.connect.write)

Create Slack Connect invitations for channels that your slack app has been added to, and accept invitations sent to your slack app.

[`conversations.connect:manage`](/reference/scopes/conversations.connect.manage)

Allows your slack app to manage Slack Connect channels, and approve, decline, and list Slack Connect invitations. Since approval requires more authority than accepting invitations, apps with this feature can only be installed by a workspace owner or admin.

## Methods {#methods}

Method

Description

[`admin.conversations.disconnectShared`](/reference/methods/admin.conversations.disconnectShared)

Disconnect a connected channel from one or more workspaces.

[`conversations.acceptSharedInvite`](/reference/methods/conversations.acceptSharedInvite)

Accepts an invitation to a Slack Connect channel.

[`conversations.approveSharedInvite`](/reference/methods/conversations.approveSharedInvite)

Approves an invitation to a Slack Connect channel

[`conversations.declineSharedInvite`](/reference/methods/conversations.declineSharedInvite)

Declines a Slack Connect channel invite.

[`conversations.externalInvitePermissions.set`](/reference/methods/conversations.externalInvitePermissions.set)

Upgrade or downgrade Slack Connect channel permissions between "can post only" and "can post and invite".

[`conversations.inviteShared`](/reference/methods/conversations.inviteShared)

Sends an invitation to a Slack Connect channel.

[`conversations.listConnectInvites`](/reference/methods/conversations.listConnectInvites)

Lists shared channel invites that have been generated or received but have not been approved by all parties.

[`conversations.requestSharedInvite.approve`](/reference/methods/conversations.requestSharedInvite.approve)

 Approves a request to add an external user to a channel and sends them a Slack Connect invite.

[`conversations.requestSharedInvite.deny`](/reference/methods/conversations.requestSharedInvite.deny)

Denies a request to invite an external user to a channel.

[`conversations.requestSharedInvite.list`](/reference/methods/conversations.requestSharedInvite.list)

Lists requests to add external users to channels with ability to filter.

[`team.externalTeams.disconnect`](/reference/methods/team.externalTeams.disconnect)

Disconnects all Slack Connect channels and direct messages (DMs) from an external organization.

[`team.externalTeams.list`](/reference/methods/team.externalTeams.list)

Returns a list of all the external teams connected and details about the connection.

[`users.discoverableContacts.lookup`](/reference/methods/users.discoverableContacts.lookup)

Look up an email address to see if someone is [discoverable](https://slack.com/help/articles/5535749574803-Manage-Slack-Connect-discoverability-for-your-organization) on Slack.

## Events {#events}

Method

Description

[`shared_channel_invite_accepted`](/reference/events/shared_channel_invite_accepted)

A shared channel invite was accepted.

[`shared_channel_invite_approved`](/reference/events/shared_channel_invite_approved)

A shared channel invite was approved.

[`shared_channel_invite_declined`](/reference/events/shared_channel_invite_declined)

A shared channel invite was declined.

[`shared_channel_invite_received`](/reference/events/shared_channel_invite_received)

A shared channel invite was sent to a Slack user.

[`shared_channel_invite_requested`](/reference/events/shared_channel_invite_requested)

A shared channel invite was sent to a Slack user.