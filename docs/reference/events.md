Source: https://docs.slack.dev/reference/events

# Events

Technical specifications and payload structures for all events sent by the Slack Events API.

| Name | Description |
|------|-------------|
| [accounts_changed](https://docs.slack.dev/reference/events/accounts_changed.md) | The list of accounts a user is signed into has changed |
| [app_mention](https://docs.slack.dev/reference/events/app_mention.md) | Subscribe to only the message events that mention your app or bot |
| [app_deleted](https://docs.slack.dev/reference/events/app_deleted.md) | User has deleted an app |
| [app_home_opened](https://docs.slack.dev/reference/events/app_home_opened.md) | User clicked into your App Home |
| [app_installed](https://docs.slack.dev/reference/events/app_installed.md) | User has installed an app |
| [app_rate_limited](https://docs.slack.dev/reference/events/app_rate_limited.md) | Indicates your app's event subscriptions are being rate limited |
| [app_requested](https://docs.slack.dev/reference/events/app_requested.md) | User requested an app |
| [app_uninstalled](https://docs.slack.dev/reference/events/app_uninstalled.md) | Your Slack app was uninstalled |
| [app_uninstalled_team](https://docs.slack.dev/reference/events/app_uninstalled_team.md) | User has uninstalled an app |
| [assistant_thread_context_changed](https://docs.slack.dev/reference/events/assistant_thread_context_changed.md) | The context changed while an AI assistant thread was visible |
| [assistant_thread_started](https://docs.slack.dev/reference/events/assistant_thread_started.md) | An AI assistant thread was started |
| [bot_added](https://docs.slack.dev/reference/events/bot_added.md) | A bot user was added |
| [bot_changed](https://docs.slack.dev/reference/events/bot_changed.md) | A bot user was changed |
| [call_rejected](https://docs.slack.dev/reference/events/call_rejected.md) | A call was rejected |
| [channel_created](https://docs.slack.dev/reference/events/channel_created.md) | A channel was created |
| [channel_deleted](https://docs.slack.dev/reference/events/channel_deleted.md) | A channel was deleted |
| [channel_history_changed](https://docs.slack.dev/reference/events/channel_history_changed.md) | Bulk updates were made to a channel's history |
| [channel_id_changed](https://docs.slack.dev/reference/events/channel_id_changed.md) | A channel ID changed |
| [channel_joined](https://docs.slack.dev/reference/events/channel_joined.md) | You joined a channel |
| [channel_left](https://docs.slack.dev/reference/events/channel_left.md) | You left a channel |
| [channel_marked](https://docs.slack.dev/reference/events/channel_marked.md) | Your channel read marker was updated |
| [channel_posting_permissions](https://docs.slack.dev/reference/events/channel_posting_permissions.md) | The posting permissions for a channel changed |
| [channel_rename](https://docs.slack.dev/reference/events/channel_rename.md) | A channel was renamed |
| [channel_shared](https://docs.slack.dev/reference/events/channel_shared.md) | A channel has been shared with an external workspace |
| [channel_unshared](https://docs.slack.dev/reference/events/channel_unshared.md) | A channel has been unshared with an external workspace |
| [commands_changed](https://docs.slack.dev/reference/events/commands_changed.md) | A slash command has been added or changed |
| [dnd_updated](https://docs.slack.dev/reference/events/dnd_updated.md) | Do not Disturb settings changed for the current user |
| [dnd_updated_user](https://docs.slack.dev/reference/events/dnd_updated_user.md) | Do not Disturb settings changed for a member |
| [email_domain_changed](https://docs.slack.dev/reference/events/email_domain_changed.md) | The workspace email domain has changed |
| [emoji_changed](https://docs.slack.dev/reference/events/emoji_changed.md) | A custom emoji has been added or changed |
| [entity_details_requested](https://docs.slack.dev/reference/events/entity_details_requested.md) | This event is sent to your app when a user clicks on a Work Object unfurl or refreshes the flexpane |
| [external_org_migration_finished](https://docs.slack.dev/reference/events/external_org_migration_finished.md) | An enterprise org migration has finished on an external workspace |
| [external_org_migration_started](https://docs.slack.dev/reference/events/external_org_migration_started.md) | An enterprise org migration has started on an external workspace |
| [file_change](https://docs.slack.dev/reference/events/file_change.md) | A file was changed |
| [file_comment_added](https://docs.slack.dev/reference/events/file_comment_added.md) | A file comment was added |
| [file_comment_deleted](https://docs.slack.dev/reference/events/file_comment_deleted.md) | A file comment was deleted |
| [file_comment_edited](https://docs.slack.dev/reference/events/file_comment_edited.md) | A file comment was edited |
| [file_created](https://docs.slack.dev/reference/events/file_created.md) | A file was created |
| [file_deleted](https://docs.slack.dev/reference/events/file_deleted.md) | A file was deleted |
| [file_public](https://docs.slack.dev/reference/events/file_public.md) | A file was made public |
| [file_shared](https://docs.slack.dev/reference/events/file_shared.md) | A file was shared |
| [file_unshared](https://docs.slack.dev/reference/events/file_unshared.md) | A file was unshared |
| [function_executed](https://docs.slack.dev/reference/events/function_executed.md) | Your app function is executed as a step in a workflow |
| [goodbye](https://docs.slack.dev/reference/events/goodbye.md) | The server intends to close the connection soon |
| [grid_migration_finished](https://docs.slack.dev/reference/events/grid_migration_finished.md) | An enterprise org migration has finished on this workspace |
| [grid_migration_started](https://docs.slack.dev/reference/events/grid_migration_started.md) | An enterprise org migration has started on this workspace |
| [group_close](https://docs.slack.dev/reference/events/group_close.md) | You closed a private channel |
| [group_deleted](https://docs.slack.dev/reference/events/group_deleted.md) | A private channel was deleted |
| [group_history_changed](https://docs.slack.dev/reference/events/group_history_changed.md) | Bulk updates were made to a private channel's history |
| [group_joined](https://docs.slack.dev/reference/events/group_joined.md) | You joined a private channel |
| [group_left](https://docs.slack.dev/reference/events/group_left.md) | You left a private channel |
| [group_marked](https://docs.slack.dev/reference/events/group_marked.md) | A private channel read marker was updated |
| [group_open](https://docs.slack.dev/reference/events/group_open.md) | You created a group DM |
| [group_rename](https://docs.slack.dev/reference/events/group_rename.md) | A private channel was renamed |
| [hello](https://docs.slack.dev/reference/events/hello.md) | The client has successfully connected to the server |
| [im_close](https://docs.slack.dev/reference/events/im_close.md) | You closed a DM |
| [im_created](https://docs.slack.dev/reference/events/im_created.md) | A DM was created |
| [im_history_changed](https://docs.slack.dev/reference/events/im_history_changed.md) | Bulk updates were made to a DM's history |
| [im_marked](https://docs.slack.dev/reference/events/im_marked.md) | A direct message read marker was updated |
| [im_open](https://docs.slack.dev/reference/events/im_open.md) | You opened a DM |
| [invite_requested](https://docs.slack.dev/reference/events/invite_requested.md) | User requested an invite |
| [link_shared](https://docs.slack.dev/reference/events/link_shared.md) | A message was posted containing one or more links relevant to your application |
| [manual_presence_change](https://docs.slack.dev/reference/events/manual_presence_change.md) | You manually updated your presence |
| [member_joined_channel](https://docs.slack.dev/reference/events/member_joined_channel.md) | A user joined a public channel, private channel or MPDM |
| [member_left_channel](https://docs.slack.dev/reference/events/member_left_channel.md) | A user left a public or private channel |
| [message](https://docs.slack.dev/reference/events/message.md) | A message was sent to a channel |
| [assistant_app_thread](https://docs.slack.dev/reference/events/message/assistant_app_thread.md) | The message sent is an app assistant thread |
| [bot_message](https://docs.slack.dev/reference/events/message/bot_message.md) | A message was posted by an integration |
| [channel_archive](https://docs.slack.dev/reference/events/message/channel_archive.md) | A channel was archived. |
| [channel_convert_to_private](https://docs.slack.dev/reference/events/message/channel_convert_to_private.md) | This channel was made private. Now, it can only be viewed or joined by invitation |
| [channel_convert_to_public](https://docs.slack.dev/reference/events/message/channel_convert_to_public.md) | This channel was made public. Any member in this workspace can see and join it |
| [channel_join](https://docs.slack.dev/reference/events/message/channel_join.md) | A member joined a channel |
| [channel_leave](https://docs.slack.dev/reference/events/message/channel_leave.md) | A member left a channel |
| [channel_name](https://docs.slack.dev/reference/events/message/channel_name.md) | A channel was renamed |
| [channel_posting_permission](https://docs.slack.dev/reference/events/message/channel_posting_permission.md) | The posting permissions for a channel changed |
| [channel_purpose](https://docs.slack.dev/reference/events/message/channel_purpose.md) | A channel purpose was updated |
| [channel_topic](https://docs.slack.dev/reference/events/message/channel_topic.md) | A channel topic was updated |
| [channel_unarchive](https://docs.slack.dev/reference/events/message/channel_unarchive.md) | A channel was unarchived |
| [document_mention](https://docs.slack.dev/reference/events/message/document_mention.md) | A bot is mentioned in the body of a canvas |
| [ekm_access_denied](https://docs.slack.dev/reference/events/message/ekm_access_denied.md) | Message content redacted due to Enterprise Key Management (EKM) |
| [file_comment](https://docs.slack.dev/reference/events/message/file_comment.md) | A comment was added to a file |
| [file_mention](https://docs.slack.dev/reference/events/message/file_mention.md) | A file was mentioned in a channel |
| [file_share](https://docs.slack.dev/reference/events/message/file_share.md) | A file was shared into a channel |
| [group_archive](https://docs.slack.dev/reference/events/message/group_archive.md) | A group was archived |
| [group_join](https://docs.slack.dev/reference/events/message/group_join.md) | A member joined a group |
| [group_leave](https://docs.slack.dev/reference/events/message/group_leave.md) | A member left a group |
| [group_name](https://docs.slack.dev/reference/events/message/group_name.md) | A group was renamed |
| [group_purpose](https://docs.slack.dev/reference/events/message/group_purpose.md) | A group purpose was updated |
| [group_topic](https://docs.slack.dev/reference/events/message/group_topic.md) | A group topic was updated |
| [group_unarchive](https://docs.slack.dev/reference/events/message/group_unarchive.md) | A group was unarchived |
| [me_message](https://docs.slack.dev/reference/events/message/me_message.md) | A /me message was sent |
| [message_changed](https://docs.slack.dev/reference/events/message/message_changed.md) | A message was changed |
| [message_deleted](https://docs.slack.dev/reference/events/message/message_deleted.md) | A message was deleted |
| [message_locked](https://docs.slack.dev/reference/events/message/message_locked.md) | A message thread was locked |
| [message_replied](https://docs.slack.dev/reference/events/message/message_replied.md) | A message thread received a reply |
| [pinned_item](https://docs.slack.dev/reference/events/message/pinned_item.md) | An item was pinned in a channel |
| [reminder_add](https://docs.slack.dev/reference/events/message/reminder_add.md) | A reminder was added to the channel |
| [reply_broadcast](https://docs.slack.dev/reference/events/message/reply_broadcast.md) | (No longer served) A message thread's reply was broadcast to a channel |
| [thread_broadcast](https://docs.slack.dev/reference/events/message/thread_broadcast.md) | A message thread's reply was broadcast to a channel |
| [unpinned_item](https://docs.slack.dev/reference/events/message/unpinned_item.md) | An item was unpinned from a channel |
| [message.app_home](https://docs.slack.dev/reference/events/message.app_home.md) | A user sent a message to your Slack app |
| [message.channels](https://docs.slack.dev/reference/events/message.channels.md) | A message was posted to a channel |
| [message.groups](https://docs.slack.dev/reference/events/message.groups.md) | A message was posted to a private channel |
| [message.im](https://docs.slack.dev/reference/events/message.im.md) | A message was posted in a direct message channel |
| [message.mpim](https://docs.slack.dev/reference/events/message.mpim.md) | A message was posted in a multiparty direct message channel |
| [message_metadata_deleted](https://docs.slack.dev/reference/events/message_metadata_deleted.md) | Message metadata was deleted |
| [message_metadata_posted](https://docs.slack.dev/reference/events/message_metadata_posted.md) | Message metadata was posted |
| [message_metadata_updated](https://docs.slack.dev/reference/events/message_metadata_updated.md) | Message metadata was updated |
| [pin_added](https://docs.slack.dev/reference/events/pin_added.md) | A pin was added to a channel |
| [pin_removed](https://docs.slack.dev/reference/events/pin_removed.md) | A pin was removed from a channel |
| [pref_change](https://docs.slack.dev/reference/events/pref_change.md) | You have updated your preferences |
| [presence_change](https://docs.slack.dev/reference/events/presence_change.md) | A member's presence changed |
| [presence_query](https://docs.slack.dev/reference/events/presence_query.md) | Determine the current presence status for a list of users |
| [presence_sub](https://docs.slack.dev/reference/events/presence_sub.md) | Subscribe to presence events for the specified users |
| [reaction_added](https://docs.slack.dev/reference/events/reaction_added.md) | A member has added an emoji reaction to an item |
| [reaction_removed](https://docs.slack.dev/reference/events/reaction_removed.md) | A member removed an emoji reaction |
| [reconnect_url](https://docs.slack.dev/reference/events/reconnect_url.md) | Experimental |
| [shared_channel_invite_accepted](https://docs.slack.dev/reference/events/shared_channel_invite_accepted.md) | A shared channel invited was accepted |
| [shared_channel_invite_approved](https://docs.slack.dev/reference/events/shared_channel_invite_approved.md) | A shared channel invited was approved |
| [shared_channel_invite_declined](https://docs.slack.dev/reference/events/shared_channel_invite_declined.md) | A shared channel invited was declined |
| [shared_channel_invite_received](https://docs.slack.dev/reference/events/shared_channel_invite_received.md) | A shared channel invited was sent to a Slack user |
| [shared_channel_invite_requested](https://docs.slack.dev/reference/events/shared_channel_invite_requested.md) | A shared channel invited was requested |
| [star_added](https://docs.slack.dev/reference/events/star_added.md) | A member has saved an item for later or starred an item |
| [star_removed](https://docs.slack.dev/reference/events/star_removed.md) | A member has removed an item saved for later or starred an item |
| [subteam_created](https://docs.slack.dev/reference/events/subteam_created.md) | A User Group has been added to the workspace |
| [subteam_members_changed](https://docs.slack.dev/reference/events/subteam_members_changed.md) | The membership of an existing User Group has changed |
| [subteam_self_added](https://docs.slack.dev/reference/events/subteam_self_added.md) | You have been added to a User Group |
| [subteam_self_removed](https://docs.slack.dev/reference/events/subteam_self_removed.md) | You have been removed from a User Group |
| [subteam_updated](https://docs.slack.dev/reference/events/subteam_updated.md) | An existing User Group has been updated or its members changed |
| [team_access_granted](https://docs.slack.dev/reference/events/team_access_granted.md) | Access to a set of teams was granted to your org app |
| [team_access_revoked](https://docs.slack.dev/reference/events/team_access_revoked.md) | Access to a set of teams was revoked from your org app |
| [team_domain_change](https://docs.slack.dev/reference/events/team_domain_change.md) | The workspace domain has changed |
| [team_join](https://docs.slack.dev/reference/events/team_join.md) | A new member has joined |
| [team_migration_started](https://docs.slack.dev/reference/events/team_migration_started.md) | The workspace is being migrated between servers |
| [team_plan_change](https://docs.slack.dev/reference/events/team_plan_change.md) | The account billing plan has changed |
| [team_pref_change](https://docs.slack.dev/reference/events/team_pref_change.md) | A preference has been updated |
| [team_profile_change](https://docs.slack.dev/reference/events/team_profile_change.md) | The workspace profile fields have been updated |
| [team_profile_delete](https://docs.slack.dev/reference/events/team_profile_delete.md) | The workspace profile fields have been deleted |
| [team_profile_reorder](https://docs.slack.dev/reference/events/team_profile_reorder.md) | The workspace profile fields have been reordered |
| [team_rename](https://docs.slack.dev/reference/events/team_rename.md) | The workspace name has changed |
| [tokens_revoked](https://docs.slack.dev/reference/events/tokens_revoked.md) | API tokens for your app were revoked |
| [url_verification](https://docs.slack.dev/reference/events/url_verification.md) | Verifies ownership of an Events API Request URL |
| [user_change](https://docs.slack.dev/reference/events/user_change.md) | A member's data has changed |
| [user_connection](https://docs.slack.dev/reference/events/user_connection.md) | A member's user connection status change requested |
| [user_huddle_changed](https://docs.slack.dev/reference/events/user_huddle_changed.md) | A user's huddle status has changed |
| [user_typing](https://docs.slack.dev/reference/events/user_typing.md) | A channel member is typing a message |