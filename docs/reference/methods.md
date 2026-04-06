Source: https://docs.slack.dev/reference/methods

# Methods

An API reference for all available Slack Web API methods and their parameters.

| Name | Description |
|------|-------------|
| [admin.analytics.getFile](https://docs.slack.dev/reference/methods/admin.analytics.getfile.md) | Retrieve analytics data for a given date, presented as a compressed JSON file |
| [admin.analytics.messages.activity](https://docs.slack.dev/reference/methods/admin.analytics.messages.activity.md) | Retrieves activity metrics for messages from a given channel. |
| [admin.analytics.messages.metadata](https://docs.slack.dev/reference/methods/admin.analytics.messages.metadata.md) | Retrieves metadata for a list of messages from a given channel. |
| [admin.apps.activities.list](https://docs.slack.dev/reference/methods/admin.apps.activities.list.md) | Get logs for a specified team/org |
| [admin.apps.approve](https://docs.slack.dev/reference/methods/admin.apps.approve.md) | Approve an app for installation on a workspace. |
| [admin.apps.approved.list](https://docs.slack.dev/reference/methods/admin.apps.approved.list.md) | List approved apps for an org or workspace. |
| [admin.apps.clearResolution](https://docs.slack.dev/reference/methods/admin.apps.clearresolution.md) | Clear an app resolution |
| [admin.apps.config.lookup](https://docs.slack.dev/reference/methods/admin.apps.config.lookup.md) | Look up the app config for connectors by their IDs |
| [admin.apps.config.set](https://docs.slack.dev/reference/methods/admin.apps.config.set.md) | Set the app config for a connector |
| [admin.apps.requests.cancel](https://docs.slack.dev/reference/methods/admin.apps.requests.cancel.md) | Cancel app request for team |
| [admin.apps.requests.list](https://docs.slack.dev/reference/methods/admin.apps.requests.list.md) | List app requests for a team/workspace. |
| [admin.apps.restrict](https://docs.slack.dev/reference/methods/admin.apps.restrict.md) | Restrict an app for installation on a workspace. |
| [admin.apps.restricted.list](https://docs.slack.dev/reference/methods/admin.apps.restricted.list.md) | List restricted apps for an org or workspace. |
| [admin.apps.uninstall](https://docs.slack.dev/reference/methods/admin.apps.uninstall.md) | Uninstall an app from one or many workspaces, or an entire enterprise organization. |
| [admin.audit.anomaly.allow.getItem](https://docs.slack.dev/reference/methods/admin.audit.anomaly.allow.getitem.md) | API to allow Enterprise org admins to read the allow list of IP blocks and ASNs from the enterprise configuration. |
| [admin.audit.anomaly.allow.updateItem](https://docs.slack.dev/reference/methods/admin.audit.anomaly.allow.updateitem.md) | API to allow Enterprise org admins to write/overwrite the allow list of IP blocks and ASNs from the enterprise configuration. |
| [admin.auth.policy.assignEntities](https://docs.slack.dev/reference/methods/admin.auth.policy.assignentities.md) | Assign entities to a particular authentication policy. |
| [admin.auth.policy.getEntities](https://docs.slack.dev/reference/methods/admin.auth.policy.getentities.md) | Fetch all the entities assigned to a particular authentication policy by name. |
| [admin.auth.policy.removeEntities](https://docs.slack.dev/reference/methods/admin.auth.policy.removeentities.md) | Remove specified entities from a specified authentication policy. |
| [admin.barriers.create](https://docs.slack.dev/reference/methods/admin.barriers.create.md) | Create an Information Barrier |
| [admin.barriers.delete](https://docs.slack.dev/reference/methods/admin.barriers.delete.md) | Delete an existing Information Barrier |
| [admin.barriers.list](https://docs.slack.dev/reference/methods/admin.barriers.list.md) | Get all Information Barriers for your organization |
| [admin.barriers.update](https://docs.slack.dev/reference/methods/admin.barriers.update.md) | Update an existing Information Barrier |
| [admin.conversations.archive](https://docs.slack.dev/reference/methods/admin.conversations.archive.md) | Archive a public or private channel. |
| [admin.conversations.bulkArchive](https://docs.slack.dev/reference/methods/admin.conversations.bulkarchive.md) | Archive public or private channels in bulk. |
| [admin.conversations.bulkDelete](https://docs.slack.dev/reference/methods/admin.conversations.bulkdelete.md) | Delete public or private channels in bulk |
| [admin.conversations.bulkMove](https://docs.slack.dev/reference/methods/admin.conversations.bulkmove.md) | Move public or private channels in bulk. |
| [admin.conversations.bulkSetExcludeFromSlackAi](https://docs.slack.dev/reference/methods/admin.conversations.bulksetexcludefromslackai.md) | Exclude channels from Slack AI in bulk |
| [admin.conversations.convertToPrivate](https://docs.slack.dev/reference/methods/admin.conversations.converttoprivate.md) | Convert a public channel to a private channel. |
| [admin.conversations.convertToPublic](https://docs.slack.dev/reference/methods/admin.conversations.converttopublic.md) | Convert a private channel to a public channel. |
| [admin.conversations.create](https://docs.slack.dev/reference/methods/admin.conversations.create.md) | Create a public or private channel-based conversation. |
| [admin.conversations.createForObjects](https://docs.slack.dev/reference/methods/admin.conversations.createforobjects.md) | Create a Salesforce channel for the corresponding object provided. |
| [admin.conversations.delete](https://docs.slack.dev/reference/methods/admin.conversations.delete.md) | Delete a public or private channel. |
| [admin.conversations.disconnectShared](https://docs.slack.dev/reference/methods/admin.conversations.disconnectshared.md) | Disconnect a connected channel from one or more workspaces. |
| [admin.conversations.ekm.listOriginalConnectedChannelInfo](https://docs.slack.dev/reference/methods/admin.conversations.ekm.listoriginalconnectedchannelinfo.md) | List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM. |
| [admin.conversations.getConversationPrefs](https://docs.slack.dev/reference/methods/admin.conversations.getconversationprefs.md) | Get conversation preferences for a public or private channel. |
| [admin.conversations.getCustomRetention](https://docs.slack.dev/reference/methods/admin.conversations.getcustomretention.md) | This API endpoint can be used by any admin to get a conversation's retention policy. |
| [admin.conversations.getTeams](https://docs.slack.dev/reference/methods/admin.conversations.getteams.md) | Get all the workspaces a given public or private channel is connected to within this Enterprise org. |
| [admin.conversations.invite](https://docs.slack.dev/reference/methods/admin.conversations.invite.md) | Invite a user to a public or private channel. |
| [admin.conversations.linkObjects](https://docs.slack.dev/reference/methods/admin.conversations.linkobjects.md) | Link a Salesforce record to a channel |
| [admin.conversations.lookup](https://docs.slack.dev/reference/methods/admin.conversations.lookup.md) | Returns channels on the given team using the filters. |
| [admin.conversations.removeCustomRetention](https://docs.slack.dev/reference/methods/admin.conversations.removecustomretention.md) | This API endpoint can be used by any admin to remove a conversation's retention policy. |
| [admin.conversations.rename](https://docs.slack.dev/reference/methods/admin.conversations.rename.md) | Rename a public or private channel. |
| [admin.conversations.restrictAccess.addGroup](https://docs.slack.dev/reference/methods/admin.conversations.restrictaccess.addgroup.md) | Add an allowlist of IDP groups for accessing a channel |
| [admin.conversations.restrictAccess.listGroups](https://docs.slack.dev/reference/methods/admin.conversations.restrictaccess.listgroups.md) | List all IDP Groups linked to a channel |
| [admin.conversations.restrictAccess.removeGroup](https://docs.slack.dev/reference/methods/admin.conversations.restrictaccess.removegroup.md) | Remove a linked IDP group linked from a private channel |
| [admin.conversations.search](https://docs.slack.dev/reference/methods/admin.conversations.search.md) | Search for public or private channels in an Enterprise organization. |
| [admin.conversations.setConversationPrefs](https://docs.slack.dev/reference/methods/admin.conversations.setconversationprefs.md) | Set the posting permissions for a public or private channel. |
| [admin.conversations.setCustomRetention](https://docs.slack.dev/reference/methods/admin.conversations.setcustomretention.md) | This API endpoint can be used by any admin to set a conversation's retention policy. |
| [admin.conversations.setTeams](https://docs.slack.dev/reference/methods/admin.conversations.setteams.md) | Set the workspaces in an Enterprise org that connect to a public or private channel. |
| [admin.conversations.unarchive](https://docs.slack.dev/reference/methods/admin.conversations.unarchive.md) | Unarchive a public or private channel. |
| [admin.conversations.unlinkObjects](https://docs.slack.dev/reference/methods/admin.conversations.unlinkobjects.md) | Unlink a Salesforce record from a channel |
| [admin.emoji.add](https://docs.slack.dev/reference/methods/admin.emoji.add.md) | Add an emoji. |
| [admin.emoji.addAlias](https://docs.slack.dev/reference/methods/admin.emoji.addalias.md) | Add an emoji alias. |
| [admin.emoji.list](https://docs.slack.dev/reference/methods/admin.emoji.list.md) | List emoji for an Enterprise organization. |
| [admin.emoji.remove](https://docs.slack.dev/reference/methods/admin.emoji.remove.md) | Remove an emoji across an Enterprise organization |
| [admin.emoji.rename](https://docs.slack.dev/reference/methods/admin.emoji.rename.md) | Rename an emoji. |
| [admin.functions.list](https://docs.slack.dev/reference/methods/admin.functions.list.md) | Look up functions by a set of apps. |
| [admin.functions.permissions.lookup](https://docs.slack.dev/reference/methods/admin.functions.permissions.lookup.md) | Lookup the visibility of multiple Slack functions and include the users if it is limited to particular named entities. |
| [admin.functions.permissions.set](https://docs.slack.dev/reference/methods/admin.functions.permissions.set.md) | Set the visibility of a Slack function and define the users or workspaces if it is set to named_entities. |
| [admin.inviteRequests.approve](https://docs.slack.dev/reference/methods/admin.inviterequests.approve.md) | Approve a workspace invite request. |
| [admin.inviteRequests.approved.list](https://docs.slack.dev/reference/methods/admin.inviterequests.approved.list.md) | List all approved workspace invite requests. |
| [admin.inviteRequests.denied.list](https://docs.slack.dev/reference/methods/admin.inviterequests.denied.list.md) | List all denied workspace invite requests. |
| [admin.inviteRequests.deny](https://docs.slack.dev/reference/methods/admin.inviterequests.deny.md) | Deny a workspace invite request. |
| [admin.inviteRequests.list](https://docs.slack.dev/reference/methods/admin.inviterequests.list.md) | List all pending workspace invite requests. |
| [admin.roles.addAssignments](https://docs.slack.dev/reference/methods/admin.roles.addassignments.md) | Adds members to the specified role with the specified scopes |
| [admin.roles.listAssignments](https://docs.slack.dev/reference/methods/admin.roles.listassignments.md) | Lists assignments for all roles across entities. Options to scope results by any combination of roles or entities |
| [admin.roles.removeAssignments](https://docs.slack.dev/reference/methods/admin.roles.removeassignments.md) | Removes a set of users from a role for the given scopes and entities |
| [admin.teams.admins.list](https://docs.slack.dev/reference/methods/admin.teams.admins.list.md) | List all of the admins on a given workspace. |
| [admin.teams.create](https://docs.slack.dev/reference/methods/admin.teams.create.md) | Create an Enterprise team. |
| [admin.teams.list](https://docs.slack.dev/reference/methods/admin.teams.list.md) | List all teams in an Enterprise organization |
| [admin.teams.owners.list](https://docs.slack.dev/reference/methods/admin.teams.owners.list.md) | List all of the owners on a given workspace. |
| [admin.teams.settings.info](https://docs.slack.dev/reference/methods/admin.teams.settings.info.md) | Fetch information about settings in a workspace |
| [admin.teams.settings.setDefaultChannels](https://docs.slack.dev/reference/methods/admin.teams.settings.setdefaultchannels.md) | Set the default channels of a workspace. |
| [admin.teams.settings.setDescription](https://docs.slack.dev/reference/methods/admin.teams.settings.setdescription.md) | Set the description of a given workspace. |
| [admin.teams.settings.setDiscoverability](https://docs.slack.dev/reference/methods/admin.teams.settings.setdiscoverability.md) | An API method that allows admins to set the discoverability of a given workspace |
| [admin.teams.settings.setIcon](https://docs.slack.dev/reference/methods/admin.teams.settings.seticon.md) | Sets the icon of a workspace. |
| [admin.teams.settings.setName](https://docs.slack.dev/reference/methods/admin.teams.settings.setname.md) | Set the name of a given workspace. |
| [admin.usergroups.addChannels](https://docs.slack.dev/reference/methods/admin.usergroups.addchannels.md) | Add up to one hundred default channels to an IDP group. |
| [admin.usergroups.addTeams](https://docs.slack.dev/reference/methods/admin.usergroups.addteams.md) | Associate one or more default workspaces with an organization-wide IDP group. |
| [admin.usergroups.listChannels](https://docs.slack.dev/reference/methods/admin.usergroups.listchannels.md) | List the channels linked to an org-level IDP group (user group). |
| [admin.usergroups.removeChannels](https://docs.slack.dev/reference/methods/admin.usergroups.removechannels.md) | Remove one or more default channels from an org-level IDP group (user group). |
| [admin.users.assign](https://docs.slack.dev/reference/methods/admin.users.assign.md) | Add an Enterprise user to a workspace. |
| [admin.users.getExpiration](https://docs.slack.dev/reference/methods/admin.users.getexpiration.md) | Fetches the expiration timestamp for a guest |
| [admin.users.invite](https://docs.slack.dev/reference/methods/admin.users.invite.md) | Invite a user to a workspace. |
| [admin.users.list](https://docs.slack.dev/reference/methods/admin.users.list.md) | List users on a workspace |
| [admin.users.remove](https://docs.slack.dev/reference/methods/admin.users.remove.md) | Remove a user from a workspace. |
| [admin.users.session.clearSettings](https://docs.slack.dev/reference/methods/admin.users.session.clearsettings.md) | Clear user-specific session settings—the session duration and what happens when the client closes—for a list of users. |
| [admin.users.session.getSettings](https://docs.slack.dev/reference/methods/admin.users.session.getsettings.md) | Get user-specific session settings—the session duration and what happens when the client closes—given a list of users. |
| [admin.users.session.invalidate](https://docs.slack.dev/reference/methods/admin.users.session.invalidate.md) | Revoke a single session for a user. The user will be forced to login to Slack. |
| [admin.users.session.list](https://docs.slack.dev/reference/methods/admin.users.session.list.md) | List active user sessions for an organization |
| [admin.users.session.reset](https://docs.slack.dev/reference/methods/admin.users.session.reset.md) | Wipes all valid sessions on all devices for a given user |
| [admin.users.session.resetBulk](https://docs.slack.dev/reference/methods/admin.users.session.resetbulk.md) | Enqueues an asynchronous job to wipe all valid sessions on all devices for a given list of users |
| [admin.users.session.setSettings](https://docs.slack.dev/reference/methods/admin.users.session.setsettings.md) | Configure the user-level session settings—the session duration and what happens when the client closes—for one or more users. |
| [admin.users.setAdmin](https://docs.slack.dev/reference/methods/admin.users.setadmin.md) | Set an existing regular user or owner to be a workspace or org admin. |
| [admin.users.setExpiration](https://docs.slack.dev/reference/methods/admin.users.setexpiration.md) | Set an expiration for a guest user |
| [admin.users.setOwner](https://docs.slack.dev/reference/methods/admin.users.setowner.md) | Set an existing regular user or admin to be a workspace or org owner. |
| [admin.users.setRegular](https://docs.slack.dev/reference/methods/admin.users.setregular.md) | Set an existing guest user, admin user, or owner to be a regular user. |
| [admin.users.unsupportedVersions.export](https://docs.slack.dev/reference/methods/admin.users.unsupportedversions.export.md) | Ask Slackbot to send you an export listing all workspace members using unsupported software, presented as a zipped CSV file. |
| [admin.workflows.collaborators.add](https://docs.slack.dev/reference/methods/admin.workflows.collaborators.add.md) | Add collaborators to workflows within the team or enterprise |
| [admin.workflows.collaborators.remove](https://docs.slack.dev/reference/methods/admin.workflows.collaborators.remove.md) | Remove collaborators from workflows within the team or enterprise |
| [admin.workflows.permissions.lookup](https://docs.slack.dev/reference/methods/admin.workflows.permissions.lookup.md) | Look up the permissions for a set of workflows |
| [admin.workflows.search](https://docs.slack.dev/reference/methods/admin.workflows.search.md) | Search workflows within the team or enterprise |
| [admin.workflows.triggers.types.permissions.lookup](https://docs.slack.dev/reference/methods/admin.workflows.triggers.types.permissions.lookup.md) | List the permissions for using each trigger type. |
| [admin.workflows.triggers.types.permissions.set](https://docs.slack.dev/reference/methods/admin.workflows.triggers.types.permissions.set.md) | Set the permissions for using a trigger type |
| [admin.workflows.unpublish](https://docs.slack.dev/reference/methods/admin.workflows.unpublish.md) | Unpublish workflows within the team or enterprise |
| [api.test](https://docs.slack.dev/reference/methods/api.test.md) | Checks API calling code. |
| [apps.activities.list](https://docs.slack.dev/reference/methods/apps.activities.list.md) | Get logs for a specified app |
| [apps.auth.external.delete](https://docs.slack.dev/reference/methods/apps.auth.external.delete.md) | Delete external auth tokens only on the Slack side |
| [apps.auth.external.get](https://docs.slack.dev/reference/methods/apps.auth.external.get.md) | Get the access token for the provided token ID |
| [apps.connections.open](https://docs.slack.dev/reference/methods/apps.connections.open.md) | Generate a temporary Socket Mode WebSocket URL that your app can connect to in order to receive events and interactive payloads over. |
| [apps.datastore.bulkDelete](https://docs.slack.dev/reference/methods/apps.datastore.bulkdelete.md) | Delete items from a datastore in bulk |
| [apps.datastore.bulkGet](https://docs.slack.dev/reference/methods/apps.datastore.bulkget.md) | Get items from a datastore in bulk |
| [apps.datastore.bulkPut](https://docs.slack.dev/reference/methods/apps.datastore.bulkput.md) | Creates or replaces existing items in bulk |
| [apps.datastore.count](https://docs.slack.dev/reference/methods/apps.datastore.count.md) | Count the number of items in a datastore that match a query |
| [apps.datastore.delete](https://docs.slack.dev/reference/methods/apps.datastore.delete.md) | Delete an item from a datastore |
| [apps.datastore.get](https://docs.slack.dev/reference/methods/apps.datastore.get.md) | Get an item from a datastore |
| [apps.datastore.put](https://docs.slack.dev/reference/methods/apps.datastore.put.md) | Creates a new item, or replaces an old item with a new item. |
| [apps.datastore.query](https://docs.slack.dev/reference/methods/apps.datastore.query.md) | Query a datastore for items |
| [apps.datastore.update](https://docs.slack.dev/reference/methods/apps.datastore.update.md) | Edits an existing item's attributes, or adds a new item if it does not already exist. |
| [apps.event.authorizations.list](https://docs.slack.dev/reference/methods/apps.event.authorizations.list.md) | Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to. |
| [apps.manifest.create](https://docs.slack.dev/reference/methods/apps.manifest.create.md) | Create an app from an app manifest. |
| [apps.manifest.delete](https://docs.slack.dev/reference/methods/apps.manifest.delete.md) | Permanently deletes an app created through app manifests |
| [apps.manifest.export](https://docs.slack.dev/reference/methods/apps.manifest.export.md) | Export an app manifest from an existing app |
| [apps.manifest.update](https://docs.slack.dev/reference/methods/apps.manifest.update.md) | Update an app from an app manifest |
| [apps.manifest.validate](https://docs.slack.dev/reference/methods/apps.manifest.validate.md) | Validate an app manifest |
| [apps.uninstall](https://docs.slack.dev/reference/methods/apps.uninstall.md) | Uninstalls your app from a workspace. |
| [apps.user.connection.update](https://docs.slack.dev/reference/methods/apps.user.connection.update.md) | Updates the connection status between a user and an app. |
| [assistant.search.context](https://docs.slack.dev/reference/methods/assistant.search.context.md) | Searches messages, files, channels and users across your Slack organization. |
| [assistant.search.info](https://docs.slack.dev/reference/methods/assistant.search.info.md) | Returns search capabilities on a given team. |
| [assistant.threads.setStatus](https://docs.slack.dev/reference/methods/assistant.threads.setstatus.md) | Set the status for an AI assistant thread. |
| [assistant.threads.setSuggestedPrompts](https://docs.slack.dev/reference/methods/assistant.threads.setsuggestedprompts.md) | Set suggested prompts for the given assistant thread |
| [assistant.threads.setTitle](https://docs.slack.dev/reference/methods/assistant.threads.settitle.md) | Set the title for the given assistant thread |
| [auth.revoke](https://docs.slack.dev/reference/methods/auth.revoke.md) | Revokes a token. |
| [auth.teams.list](https://docs.slack.dev/reference/methods/auth.teams.list.md) | Obtain a full list of workspaces your org-wide app has been approved for. |
| [auth.test](https://docs.slack.dev/reference/methods/auth.test.md) | Checks authentication & identity. |
| [bookmarks.add](https://docs.slack.dev/reference/methods/bookmarks.add.md) | Add bookmark to a channel. |
| [bookmarks.edit](https://docs.slack.dev/reference/methods/bookmarks.edit.md) | Edit bookmark. |
| [bookmarks.list](https://docs.slack.dev/reference/methods/bookmarks.list.md) | List bookmark for the channel. |
| [bookmarks.remove](https://docs.slack.dev/reference/methods/bookmarks.remove.md) | Remove bookmark from the channel. |
| [bots.info](https://docs.slack.dev/reference/methods/bots.info.md) | Gets information about a bot user. |
| [calls.add](https://docs.slack.dev/reference/methods/calls.add.md) | Registers a new Call. |
| [calls.end](https://docs.slack.dev/reference/methods/calls.end.md) | Ends a Call. |
| [calls.info](https://docs.slack.dev/reference/methods/calls.info.md) | Returns information about a Call. |
| [calls.participants.add](https://docs.slack.dev/reference/methods/calls.participants.add.md) | Registers new participants added to a Call. |
| [calls.participants.remove](https://docs.slack.dev/reference/methods/calls.participants.remove.md) | Registers participants removed from a Call. |
| [calls.update](https://docs.slack.dev/reference/methods/calls.update.md) | Updates information about a Call. |
| [canvases.access.delete](https://docs.slack.dev/reference/methods/canvases.access.delete.md) | Remove access to a canvas for specified entities |
| [canvases.access.set](https://docs.slack.dev/reference/methods/canvases.access.set.md) | Sets the access level to a canvas for specified entities |
| [canvases.create](https://docs.slack.dev/reference/methods/canvases.create.md) | Create canvas for a user |
| [canvases.delete](https://docs.slack.dev/reference/methods/canvases.delete.md) | Deletes a canvas |
| [canvases.edit](https://docs.slack.dev/reference/methods/canvases.edit.md) | Update an existing canvas |
| [canvases.sections.lookup](https://docs.slack.dev/reference/methods/canvases.sections.lookup.md) | Find sections matching the provided criteria |
| [chat.appendStream](https://docs.slack.dev/reference/methods/chat.appendstream.md) | Appends text to an existing streaming conversation. |
| [chat.delete](https://docs.slack.dev/reference/methods/chat.delete.md) | Deletes a message. |
| [chat.deleteScheduledMessage](https://docs.slack.dev/reference/methods/chat.deletescheduledmessage.md) | Deletes a pending scheduled message from the queue. |
| [chat.getPermalink](https://docs.slack.dev/reference/methods/chat.getpermalink.md) | Retrieve a permalink URL for a specific extant message |
| [chat.meMessage](https://docs.slack.dev/reference/methods/chat.memessage.md) | Share a me message into a channel. |
| [chat.postEphemeral](https://docs.slack.dev/reference/methods/chat.postephemeral.md) | Sends an ephemeral message to a user in a channel. |
| [chat.postMessage](https://docs.slack.dev/reference/methods/chat.postmessage.md) | Sends a message to a channel. |
| [chat.scheduledMessages.list](https://docs.slack.dev/reference/methods/chat.scheduledmessages.list.md) | Returns a list of scheduled messages. |
| [chat.scheduleMessage](https://docs.slack.dev/reference/methods/chat.schedulemessage.md) | Schedules a message to be sent to a channel. |
| [chat.startStream](https://docs.slack.dev/reference/methods/chat.startstream.md) | Starts a new streaming conversation. |
| [chat.stopStream](https://docs.slack.dev/reference/methods/chat.stopstream.md) | Stops a streaming conversation. |
| [chat.unfurl](https://docs.slack.dev/reference/methods/chat.unfurl.md) | Provide custom unfurl behavior for user-posted URLs |
| [chat.update](https://docs.slack.dev/reference/methods/chat.update.md) | Updates a message. |
| [conversations.acceptSharedInvite](https://docs.slack.dev/reference/methods/conversations.acceptsharedinvite.md) | Accepts an invitation to a Slack Connect channel. |
| [conversations.approveSharedInvite](https://docs.slack.dev/reference/methods/conversations.approvesharedinvite.md) | Approves an invitation to a Slack Connect channel |
| [conversations.archive](https://docs.slack.dev/reference/methods/conversations.archive.md) | Archives a conversation. |
| [conversations.canvases.create](https://docs.slack.dev/reference/methods/conversations.canvases.create.md) | Create a channel canvas for a channel |
| [conversations.close](https://docs.slack.dev/reference/methods/conversations.close.md) | Closes a direct message or multi-person direct message. |
| [conversations.create](https://docs.slack.dev/reference/methods/conversations.create.md) | Initiates a public or private channel-based conversation |
| [conversations.declineSharedInvite](https://docs.slack.dev/reference/methods/conversations.declinesharedinvite.md) | Declines a Slack Connect channel invite. |
| [conversations.externalInvitePermissions.set](https://docs.slack.dev/reference/methods/conversations.externalinvitepermissions.set.md) | Upgrade or downgrade Slack Connect channel permissions between 'can post only' and 'can post and invite'. |
| [conversations.history](https://docs.slack.dev/reference/methods/conversations.history.md) | Fetches a conversation's history of messages and events. |
| [conversations.info](https://docs.slack.dev/reference/methods/conversations.info.md) | Retrieve information about a conversation. |
| [conversations.invite](https://docs.slack.dev/reference/methods/conversations.invite.md) | Invites users to a channel. |
| [conversations.inviteShared](https://docs.slack.dev/reference/methods/conversations.inviteshared.md) | Sends an invitation to a Slack Connect channel |
| [conversations.join](https://docs.slack.dev/reference/methods/conversations.join.md) | Joins an existing conversation. |
| [conversations.kick](https://docs.slack.dev/reference/methods/conversations.kick.md) | Removes a user from a conversation. |
| [conversations.leave](https://docs.slack.dev/reference/methods/conversations.leave.md) | Leaves a conversation. |
| [conversations.list](https://docs.slack.dev/reference/methods/conversations.list.md) | Lists all channels in a Slack team. |
| [conversations.listConnectInvites](https://docs.slack.dev/reference/methods/conversations.listconnectinvites.md) | Lists shared channel invites that have been generated or received but have not been approved by all parties |
| [conversations.mark](https://docs.slack.dev/reference/methods/conversations.mark.md) | Sets the read cursor in a channel. |
| [conversations.members](https://docs.slack.dev/reference/methods/conversations.members.md) | Retrieve members of a conversation. |
| [conversations.open](https://docs.slack.dev/reference/methods/conversations.open.md) | Opens or resumes a direct message or multi-person direct message. |
| [conversations.rename](https://docs.slack.dev/reference/methods/conversations.rename.md) | Renames a conversation. |
| [conversations.replies](https://docs.slack.dev/reference/methods/conversations.replies.md) | Retrieve a thread of messages posted to a conversation |
| [conversations.requestSharedInvite.approve](https://docs.slack.dev/reference/methods/conversations.requestsharedinvite.approve.md) | Approves a request to add an external user to a channel and sends them a Slack Connect invite |
| [conversations.requestSharedInvite.deny](https://docs.slack.dev/reference/methods/conversations.requestsharedinvite.deny.md) | Denies a request to invite an external user to a channel |
| [conversations.requestSharedInvite.list](https://docs.slack.dev/reference/methods/conversations.requestsharedinvite.list.md) | Lists requests to add external users to channels with ability to filter. |
| [conversations.setPurpose](https://docs.slack.dev/reference/methods/conversations.setpurpose.md) | Sets the channel description. |
| [conversations.setTopic](https://docs.slack.dev/reference/methods/conversations.settopic.md) | Sets the topic for a conversation. |
| [conversations.unarchive](https://docs.slack.dev/reference/methods/conversations.unarchive.md) | Reverses conversation archival. |
| [dialog.open](https://docs.slack.dev/reference/methods/dialog.open.md) | Open a dialog with a user |
| [dnd.endDnd](https://docs.slack.dev/reference/methods/dnd.enddnd.md) | Ends the current user's Do Not Disturb session immediately. |
| [dnd.endSnooze](https://docs.slack.dev/reference/methods/dnd.endsnooze.md) | Ends the current user's snooze mode immediately. |
| [dnd.info](https://docs.slack.dev/reference/methods/dnd.info.md) | Retrieves a user's current Do Not Disturb status. |
| [dnd.setSnooze](https://docs.slack.dev/reference/methods/dnd.setsnooze.md) | Turns on Do Not Disturb mode for the current user, or changes its duration. |
| [dnd.teamInfo](https://docs.slack.dev/reference/methods/dnd.teaminfo.md) | Retrieves the Do Not Disturb status for up to 50 users on a team. |
| [emoji.list](https://docs.slack.dev/reference/methods/emoji.list.md) | Lists custom emoji for a team. |
| [entity.presentDetails](https://docs.slack.dev/reference/methods/entity.presentdetails.md) | Provide custom flexpane behavior for Work Objects. Apps call this endpoint to send per-user flexpane metadata to the client. |
| [files.comments.delete](https://docs.slack.dev/reference/methods/files.comments.delete.md) | Deletes an existing comment on a file. |
| [files.completeUploadExternal](https://docs.slack.dev/reference/methods/files.completeuploadexternal.md) | Finishes an upload started with files.getUploadURLExternal |
| [files.delete](https://docs.slack.dev/reference/methods/files.delete.md) | Deletes a file. |
| [files.getUploadURLExternal](https://docs.slack.dev/reference/methods/files.getuploadurlexternal.md) | Gets a URL for an edge external file upload |
| [files.info](https://docs.slack.dev/reference/methods/files.info.md) | Gets information about a file. |
| [files.list](https://docs.slack.dev/reference/methods/files.list.md) | List files for a team, in a channel, or from a user with applied filters. |
| [files.remote.add](https://docs.slack.dev/reference/methods/files.remote.add.md) | Adds a file from a remote service |
| [files.remote.info](https://docs.slack.dev/reference/methods/files.remote.info.md) | Retrieve information about a remote file added to Slack |
| [files.remote.list](https://docs.slack.dev/reference/methods/files.remote.list.md) | Retrieve information about a remote file added to Slack |
| [files.remote.remove](https://docs.slack.dev/reference/methods/files.remote.remove.md) | Remove a remote file. |
| [files.remote.share](https://docs.slack.dev/reference/methods/files.remote.share.md) | Share a remote file into a channel. |
| [files.remote.update](https://docs.slack.dev/reference/methods/files.remote.update.md) | Updates an existing remote file. |
| [files.revokePublicURL](https://docs.slack.dev/reference/methods/files.revokepublicurl.md) | Revokes public/external sharing access for a file |
| [files.sharedPublicURL](https://docs.slack.dev/reference/methods/files.sharedpublicurl.md) | Enables a file for public/external sharing. |
| [files.upload](https://docs.slack.dev/reference/methods/files.upload.md) | Uploads or creates a file. |
| [functions.completeError](https://docs.slack.dev/reference/methods/functions.completeerror.md) | Signal that a function failed to complete |
| [functions.completeSuccess](https://docs.slack.dev/reference/methods/functions.completesuccess.md) | Signal the successful completion of a function |
| [functions.distributions.permissions.add](https://docs.slack.dev/reference/methods/functions.distributions.permissions.add.md) | Grant users access to a custom slack function if its permission_type is set to named_entities |
| [functions.distributions.permissions.list](https://docs.slack.dev/reference/methods/functions.distributions.permissions.list.md) | List the access type of a custom slack function and include the users, team or org ids with access if its permission_type is set to named_entities |
| [functions.distributions.permissions.remove](https://docs.slack.dev/reference/methods/functions.distributions.permissions.remove.md) | Revoke user access to a custom slack function if permission_type set to named_entities |
| [functions.distributions.permissions.set](https://docs.slack.dev/reference/methods/functions.distributions.permissions.set.md) | Set the access type of a custom slack function and define the users, team or org ids to be granted access if permission_type is set to named_entities |
| [functions.workflows.steps.list](https://docs.slack.dev/reference/methods/functions.workflows.steps.list.md) | List the steps of a specific function of a workflow's versions |
| [functions.workflows.steps.responses.export](https://docs.slack.dev/reference/methods/functions.workflows.steps.responses.export.md) | Download form responses of a workflow |
| [slackLists.access.delete](https://docs.slack.dev/reference/methods/slacklists.access.delete.md) | Revoke access to a List for specified entities. |
| [slackLists.access.set](https://docs.slack.dev/reference/methods/slacklists.access.set.md) | Set the access level to a List for specified entities. |
| [slackLists.create](https://docs.slack.dev/reference/methods/slacklists.create.md) | Create a List. |
| [slackLists.download.get](https://docs.slack.dev/reference/methods/slacklists.download.get.md) | Retrieve List download URL from an export job to download List contents. |
| [slackLists.download.start](https://docs.slack.dev/reference/methods/slacklists.download.start.md) | Initiate a job to export List contents. |
| [slackLists.items.create](https://docs.slack.dev/reference/methods/slacklists.items.create.md) | Add a new item to an existing List. |
| [slackLists.items.delete](https://docs.slack.dev/reference/methods/slacklists.items.delete.md) | Deletes an item from an existing List. |
| [slackLists.items.deleteMultiple](https://docs.slack.dev/reference/methods/slacklists.items.deletemultiple.md) | Deletes multiple items from an existing List. |
| [slackLists.items.info](https://docs.slack.dev/reference/methods/slacklists.items.info.md) | Get a row from a List. |
| [slackLists.items.list](https://docs.slack.dev/reference/methods/slacklists.items.list.md) | Get records from a List. |
| [slackLists.items.update](https://docs.slack.dev/reference/methods/slacklists.items.update.md) | Updates cells in a List. |
| [slackLists.update](https://docs.slack.dev/reference/methods/slacklists.update.md) | Update a List. |
| [migration.exchange](https://docs.slack.dev/reference/methods/migration.exchange.md) | For Enterprise organization workspaces, map local user IDs to global user IDs |
| [oauth.access](https://docs.slack.dev/reference/methods/oauth.access.md) | Exchanges a temporary OAuth verifier code for an access token. |
| [oauth.v2.access](https://docs.slack.dev/reference/methods/oauth.v2.access.md) | Exchanges a temporary OAuth verifier code for an access token. |
| [oauth.v2.exchange](https://docs.slack.dev/reference/methods/oauth.v2.exchange.md) | Exchanges a legacy access token for a new expiring access token and refresh token |
| [oauth.v2.user.access](https://docs.slack.dev/reference/methods/oauth.v2.user.access.md) | Exchanges a temporary OAuth verifier code for a user access token. |
| [openid.connect.token](https://docs.slack.dev/reference/methods/openid.connect.token.md) | Exchanges a temporary OAuth verifier code for an access token for Sign in with Slack. |
| [openid.connect.userInfo](https://docs.slack.dev/reference/methods/openid.connect.userinfo.md) | Get the identity of a user who has authorized Sign in with Slack. |
| [pins.add](https://docs.slack.dev/reference/methods/pins.add.md) | Pins an item to a channel. |
| [pins.list](https://docs.slack.dev/reference/methods/pins.list.md) | Lists items pinned to a channel. |
| [pins.remove](https://docs.slack.dev/reference/methods/pins.remove.md) | Un-pins an item from a channel. |
| [reactions.add](https://docs.slack.dev/reference/methods/reactions.add.md) | Adds a reaction to an item. |
| [reactions.get](https://docs.slack.dev/reference/methods/reactions.get.md) | Gets reactions for an item. |
| [reactions.list](https://docs.slack.dev/reference/methods/reactions.list.md) | Lists reactions made by a user. |
| [reactions.remove](https://docs.slack.dev/reference/methods/reactions.remove.md) | Removes a reaction from an item. |
| [reminders.add](https://docs.slack.dev/reference/methods/reminders.add.md) | Creates a reminder. |
| [reminders.complete](https://docs.slack.dev/reference/methods/reminders.complete.md) | Marks a reminder as complete. |
| [reminders.delete](https://docs.slack.dev/reference/methods/reminders.delete.md) | Deletes a reminder. |
| [reminders.info](https://docs.slack.dev/reference/methods/reminders.info.md) | Gets information about a reminder. |
| [reminders.list](https://docs.slack.dev/reference/methods/reminders.list.md) | Lists all reminders created by or for a given user. |
| [rtm.connect](https://docs.slack.dev/reference/methods/rtm.connect.md) | Starts a Real Time Messaging session. |
| [rtm.start](https://docs.slack.dev/reference/methods/rtm.start.md) | Deprecated: Starts a Real Time Messaging session. Use rtm.connect instead. |
| [search.all](https://docs.slack.dev/reference/methods/search.all.md) | Searches for messages and files matching a query. |
| [search.files](https://docs.slack.dev/reference/methods/search.files.md) | Searches for files matching a query. |
| [search.messages](https://docs.slack.dev/reference/methods/search.messages.md) | Searches for messages matching a query. |
| [stars.add](https://docs.slack.dev/reference/methods/stars.add.md) | Save an item for later. Formerly known as adding a star. |
| [stars.list](https://docs.slack.dev/reference/methods/stars.list.md) | Listed a user's saved items, formerly known as stars. |
| [stars.remove](https://docs.slack.dev/reference/methods/stars.remove.md) | Removes a saved item (star) from an item. |
| [team.accessLogs](https://docs.slack.dev/reference/methods/team.accesslogs.md) | Gets the access logs for the current team. |
| [team.billableInfo](https://docs.slack.dev/reference/methods/team.billableinfo.md) | Gets billable users information for the current team. |
| [team.billing.info](https://docs.slack.dev/reference/methods/team.billing.info.md) | Reads a workspace's billing plan information. |
| [team.externalTeams.disconnect](https://docs.slack.dev/reference/methods/team.externalteams.disconnect.md) | Disconnect an external organization. |
| [team.externalTeams.list](https://docs.slack.dev/reference/methods/team.externalteams.list.md) | Returns a list of all the external teams connected and details about the connection. |
| [team.info](https://docs.slack.dev/reference/methods/team.info.md) | Gets information about the current team. |
| [team.integrationLogs](https://docs.slack.dev/reference/methods/team.integrationlogs.md) | Gets the integration logs for the current team. |
| [team.preferences.list](https://docs.slack.dev/reference/methods/team.preferences.list.md) | Retrieve a list of a workspace's team preferences. |
| [team.profile.get](https://docs.slack.dev/reference/methods/team.profile.get.md) | Retrieve a team's profile. |
| [tooling.tokens.rotate](https://docs.slack.dev/reference/methods/tooling.tokens.rotate.md) | Exchanges a refresh token for a new app configuration token. |
| [usergroups.create](https://docs.slack.dev/reference/methods/usergroups.create.md) | Create a User Group. |
| [usergroups.disable](https://docs.slack.dev/reference/methods/usergroups.disable.md) | Disable an existing User Group. |
| [usergroups.enable](https://docs.slack.dev/reference/methods/usergroups.enable.md) | Enable a User Group. |
| [usergroups.list](https://docs.slack.dev/reference/methods/usergroups.list.md) | List all User Groups for a team. |
| [usergroups.update](https://docs.slack.dev/reference/methods/usergroups.update.md) | Update an existing User Group. |
| [usergroups.users.list](https://docs.slack.dev/reference/methods/usergroups.users.list.md) | List all users in a User Group. |
| [usergroups.users.update](https://docs.slack.dev/reference/methods/usergroups.users.update.md) | Update the list of users for a user group. |
| [users.conversations](https://docs.slack.dev/reference/methods/users.conversations.md) | List conversations the calling user is a member of. |
| [users.deletePhoto](https://docs.slack.dev/reference/methods/users.deletephoto.md) | Delete the user profile photo |
| [users.discoverableContacts.lookup](https://docs.slack.dev/reference/methods/users.discoverablecontacts.lookup.md) | Look up an email address to see if someone is discoverable on Slack |
| [users.getPresence](https://docs.slack.dev/reference/methods/users.getpresence.md) | Gets user presence information. |
| [users.identity](https://docs.slack.dev/reference/methods/users.identity.md) | Get a user's identity. |
| [users.info](https://docs.slack.dev/reference/methods/users.info.md) | Gets information about a user. |
| [users.list](https://docs.slack.dev/reference/methods/users.list.md) | Lists all users in a Slack team. |
| [users.lookupByEmail](https://docs.slack.dev/reference/methods/users.lookupbyemail.md) | Find a user with an email address. |
| [users.profile.get](https://docs.slack.dev/reference/methods/users.profile.get.md) | Retrieve a user's profile information, including their custom status. |
| [users.profile.set](https://docs.slack.dev/reference/methods/users.profile.set.md) | Set a user's profile information, including custom status. |
| [users.setActive](https://docs.slack.dev/reference/methods/users.setactive.md) | Marked a user as active. Deprecated and non-functional. |
| [users.setPhoto](https://docs.slack.dev/reference/methods/users.setphoto.md) | Set the user profile photo |
| [users.setPresence](https://docs.slack.dev/reference/methods/users.setpresence.md) | Manually sets user presence. |
| [views.open](https://docs.slack.dev/reference/methods/views.open.md) | Open a view for a user. |
| [views.publish](https://docs.slack.dev/reference/methods/views.publish.md) | Publish a static view for a User. |
| [views.push](https://docs.slack.dev/reference/methods/views.push.md) | Push a view onto the stack of a root view. |
| [views.update](https://docs.slack.dev/reference/methods/views.update.md) | Update an existing view. |
| [workflows.featured.add](https://docs.slack.dev/reference/methods/workflows.featured.add.md) | Add featured workflows to a channel. |
| [workflows.featured.list](https://docs.slack.dev/reference/methods/workflows.featured.list.md) | List the featured workflows for specified channels. |
| [workflows.featured.remove](https://docs.slack.dev/reference/methods/workflows.featured.remove.md) | Remove featured workflows from a channel. |
| [workflows.featured.set](https://docs.slack.dev/reference/methods/workflows.featured.set.md) | Set featured workflows for a channel. |
| [workflows.triggers.permissions.add](https://docs.slack.dev/reference/methods/workflows.triggers.permissions.add.md) | Allows users to run a trigger that has its permission type set to named_entities |
| [workflows.triggers.permissions.list](https://docs.slack.dev/reference/methods/workflows.triggers.permissions.list.md) | Returns the permission type of a trigger and if applicable, includes the entities that have been granted access |
| [workflows.triggers.permissions.remove](https://docs.slack.dev/reference/methods/workflows.triggers.permissions.remove.md) | Revoke an entity's access to a trigger that has its permission type set to named_entities |
| [workflows.triggers.permissions.set](https://docs.slack.dev/reference/methods/workflows.triggers.permissions.set.md) | Set the permission type for who can run a trigger |