Source: https://docs.slack.dev/admins/managing-users

# Managing users

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

A Slack app can create a new [workspace](https://slack.com/help/articles/115004071768#your-slack-workspace) populated with the right users and admins using a collection of API methods.

* * *

## Getting started {#start}

You'll need three scopes to allow your app to create workspaces and manage users:

*   [`admin.teams:write`](/reference/scopes/admin.teams.write) allows your app to create a workspace.
*   [`admin.teams:read`](/reference/scopes/admin.teams.read) allows your app to list owners or admins for a workspace.
*   [`admin.users:write`](/reference/scopes/admin.users.write) allows your app to assign, invite, and remove users in a workspace. It also allows your app to designate a user as an admin, owner, or regular user.

All `admin.*` scopes are obtained using the normal [OAuth flow](/authentication), but there are a few extra requirements. The OAuth installation **must be initiated by an Enterprise org admin or owner**. Also, the install must take place **on the Enterprise org, not on an individual workspace** using the workspace switcher during the install flow.

![Installing the app on a workspace](/assets/images/workspace-v-org-audit-10f163aac79dc5f2c15e3ebe8267dbf4.png)

* * *

## Creating a workspace {#creating}

Create your workspace with the [`admin.teams.create`](/reference/methods/admin.teams.create) method.

* * *

## Managing users in a workspace {#managing}

The real fun of a workspace starts with conversation, and conversations need users. You can [invite](#inviting) new Enterprise org users and [assign](#assigning) existing Enterprise org users to a workspace.

### Inviting a user {#inviting}

Inviting a user is a polite first move. You'll invite users via email, just like you would using the [Slack user invitation UI](https://slack.com/help/articles/201330256-invite-new-members-to-your-workspace). The user doesn't have to be a member of your Enterprise organization yet.

Use the [`admin.users.invite`](/reference/methods/admin.users.invite) method to invite a new user. You can specify channels that you'd like the user to join using the `channel_ids` parameter, and can also designate the user as a single-channel or multi-channel guest by using the `is_restricted` and `is_ultra_restricted` parameters respectively.

### Assigning a user {#assigning}

Assign an existing Enterprise org user to a workspace if you want to skip the polite dance of invitation. If the user has previously been removed or left the workspace, they'll still be reinstated as a member.

Use the [`admin.users.assign`](/reference/methods/admin.users.assign) method to assign a user to a workspace.

Again, you have the option to designate the user as a single-channel or multi-channel guest by using the `is_restricted` and `is_ultra_restricted` parameters respectively.

### Removing a user {#removing}

All good things must come to an end, even membership in the most memorable workspace. To remove a user, use the [`admin.users.remove`](/reference/methods/admin.users.remove) method.

### Designating a user as an admin, owner, or regular user {#promoting}

You can fine-tune the flavor of your workspace by designating users as an admin, owner or regular user. The user's current designation doesn't matter; all three methods can promote and demote users. Use the corresponding method to set a user to that specific user type:

*   Set a user as an admin with the [`admin.users.setAdmin`](/reference/methods/admin.users.setAdmin) method
*   Set a user as an owner with the [`admin.users.setOwner`](/reference/methods/admin.users.setOwner) method
*   Set a user as a regular old user with the [`admin.users.setRegular`](/reference/methods/admin.users.setRegular) method

#### Looking up admins, owners, and regular users {#listing}

You can check which users are admins, workspace owners, and regular users by making use of three API methods, one for each type:

*   Return the list of workspace owners with the [`admin.teams.owners.list`](/reference/methods/admin.teams.owners.list) method
*   Return the list of admins with the [`admin.teams.admins.list`](/reference/methods/admin.teams.admins.list) method
*   Return the list of regular users with the [`admin.users.list`](/reference/methods/admin.users.list) method

### Designating a user's role {#roles}

Adding a role assignment to a user grants them the permission scopes that are assigned to that role. You can control role assignments with three methods:

*   Add a role assignment to a user with the [`admin.roles.addAssignments`](/reference/methods/admin.roles.addAssignments) method
*   remove a role assignment from a user with the [`admin.roles.removeAssignments`](/reference/methods/admin.roles.removeAssignments) method
*   See all existing role assignments in your organization with the [`admin.roles.listAssignments`](/reference/methods/admin.roles.listAssignments) method.

### Resetting sessions {#reset}

When you suspect a device-mobile, web, or either-has been swiped, take immediate action. Wipe a user's login session [using our session reset APIs](/reference/methods/admin.users.session.reset).

* * *

## Setting allowlists for private channels {#allowlists}

Typically, any member of a private channel can invite anyone else belonging to their workspace into the channel.

However, you may need to restrict access to private channels due to sensitive or confidential information. The Private Channel Management API methods allow you to create a membership “allowlist” for both private, single-workspace channels _and_ private, cross-workspace shared channels.

These API methods may only be used for private channels, not for public channels or channels that are shared externally to different Enterprise organizations.

*   Add a private channel allowlist with the [`admin.conversations.restrictAccess.addGroup`](/reference/methods/admin.conversations.restrictAccess.addGroup) method
*   Remove a private channel allowlist with the [`admin.conversations.restrictAccess.removeGroup`](/reference/methods/admin.conversations.restrictAccess.removeGroup) method
*   List private channel allowlists with the [`admin.conversations.restrictAccess.listGroups`](/reference/methods/admin.conversations.restrictAccess.listGroups) method

An [IDP group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-organization) represents a group of users synced from your identity provider (IDP). Here's a brief overview of what to expect when you create a allowlist for a private channel by linking an IDP group:

When a linked IDP group is **added** to a channel's allowlist:

*   If the added IDP group is the **first** group linked to this channel, any user who is not a member of that group is removed from the channel.
*   Members of the linked IDP group are not immediately added to the channel. They must be manually invited by a channel member.
*   Users who are _not_ in one of the IDP groups linked to a channel cannot be invited to the channel.
*   Multiple IDP groups _can_ be linked to a channel, but each API call must be made separately.

When a linked IDP group is **removed** from a channel’s allowlist:

*   Members will be removed from the channel unless they remain on the channel allowlist through membership in another IDP group.
*   When a user is removed from an IDP group, they will be removed from any channels linked to that IDP group (unless they have access to the channel through membership in another IDP group).
*   If a channel is linked to a single group, the group must be disconnected from the channel _before_ the group can be deleted.
*   If a channel is unlinked from all groups, it becomes a regular private channel—anyone can be invited.
*   If you send a SCIM request to remove over 1,000 users from a group that is linked to a channel, all in one request, the API call will fail.

## Define default channels for IDP groups {#idp-group}

You can add, remove, and list default channels for an IDP group with the `admin.usergroups.*` methods.

*   The [`admin.usergroups.addChannels`](/reference/methods/admin.usergroups.addChannels) method adds up to one hundred default channels to an IDP group.
*   The [`admin.usergroups.removeChannels`](/reference/methods/admin.usergroups.removeChannels) method removes one or more default channels from an org-level IDP group (user group).
*   The [`admin.usergroups.listChannels`](/reference/methods/admin.usergroups.listChannels) method lists the channels linked to an org-level IDP group (user group).

You can also add a _workspace_ to an IDP group using the [`admin.usergroups.addTeams`](/reference/methods/admin.usergroups.addTeams) method. When you link a workspace to an IDP group, members of the IDP group automatically join the workspace.

## Onward {#parting}

When time is pressing and the number of workspaces mounts, the API methods for creating workspaces and managing users can help. Combine with our [other APIs for help in administering and managing workspaces](/enterprise) to soothe the wounded souls of admins.