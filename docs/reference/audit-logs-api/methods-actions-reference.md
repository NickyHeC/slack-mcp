Source: https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference

# Audit Logs API methods & actions

This feature is only available to Slack workspaces on an Enterprise plan

The Audit Logs API is RESTful and, being read-only, uses a single HTTP verb — `GET` — to query and retrieve information. These methods will also return standard HTTP status codes to indicate success or failure.

The base URL for accessing the Audit Logs API methods is:

```
https://api.slack.com/audit/v1/
```

All [endpoints](#endpoints) branch from this base URL.

Header

Value

Description

`Host`

`api.slack.com`

`Accept`

`application/json`

`Authorization`

`Bearer xoxp-...`

The token must be a Slack user token (beginning with `xoxp`) associated with an Enterprise organization owner (Enterprise organization administrator tokens are not currently supported) and the token must be granted the `auditlogs:read` OAuth scope. If you are having trouble generating this token, please [contact our support team](mailto:support@slack.com).

Below is an example of a call:

```
   GET /audit/v1/logs HTTP/1.1   Host: api.slack.com   Accept: application/json   Authorization: Bearer xoxp-1234567890-0987654321-1234567890-0987654321
```

## Rate limits {#rate-limits}

The Audit Logs API methods conform to Slack's [rate limits](/apis/web-api/rate-limits), and all methods are rated Tier 3. This allows for up to 50 calls per minute, with an allowance for sporadic bursts. Unlike the Web API rate limits however, which are calculated on a per-app basis, the Audit Logs API rate limits are calculated according to an organization-wide limit.

## Endpoints {#endpoints}

Use the following RESTful endpoints to access the methods of the Audit Logs API.

Endpoint

Description

**GET /schemas**

Returns information about the kind of objects which the Audit Logs API returns as a list of all objects and a short description. Authentication not required.

**GET /actions**

Returns information about the kind of actions that the Audit Logs API returns as a list of all actions and a short description of each. Authentication not required.

**GET /logs**

Retrieves audit events from your organization. It will return a list of actions that have occurred on the installed workspace or Enterprise organization. Authentication required.

### Filters {#filters}

The following filters can be applied to narrow the range of actions returned. Filters are added as query string parameters and can be combined together. Multiple filter parameters are additive (a boolean AND) and are separated with an ampersand (`&`) in the query string. Filtering is entirely optional.

Filter key

Type

Description

`latest`

Integer

Unix timestamp of the most recent audit event to include (inclusive).

`oldest`

Integer

Unix timestamp of the least recent audit event to include (inclusive). Data is not available prior to March 2018.

`limit`

Integer

Number of results to _optimistically_ return, maximum `9999`.

`action`

String

Name of the action or actions (separated by commas) to filter on, maximum `30`.

`actor`

String

User ID who initiated the action. Will be `USLACKSECURITY` if customer credentials were reset by Slack Security.

`entity`

String

ID of the target entity of the action (such as a channel, workspace, organization, file).

For example, a call to the Audit Logs API that returns all of the audit events for a specific user (`W123AB456`) who logged in (`user_login`) since March 16, 2018 would look like:

```
https://api.slack.com/audit/v1/logs?oldest=1521214343&action=user_login&actor=W123AB456
```

To return logs for multiple actions, separate the actions in the query string by commas:

```
https://api.slack.com/audit/v1/logs?oldest=1521214343&action=file_uploaded,public_channel_created,emoji_added
```

Slack will return a maximum of 9,999 audit events per API request, with the default ordering being descending (most to least recent). Use [cursor-based pagination](/apis/web-api/pagination#cursors) to programmatically access more audit events.

You may receive more than the passed `limit` results from a given request if there are multiple logs that were recorded at the exact same time.

## Actions {#actions}

The following tables outline the currently supported list of actions, organized by entity. This list will grow over time — if you don't see an action you are interested in keeping an eye on, [please let us know](mailto:devsupport@slack.com).

### AI in Slack {#slack-ai}

Additional logging for Slackbot

When Slackbot takes an action on behalf of a user (for example, executing `file_opened` or `canvas_edited`), Slack provides additional context in the audit log. Here is an example of additional information provided with a `canvas_edited` action:

```
action: canvas_edited...acting_agent: Slackbotagent_message:  channel_id: D0123ABC456  message_ts: "1772835937.732289"  thread_ts: "1772828335.812309"
```

Action

Description

`huddle_transcription_cancelled`

Huddle transcription was cancelled.

`huddle_transcription_paused`

Huddle transcription was paused.

`huddle_transcription_resumed`

Huddle transcription was resumed.

`huddle_transcription_started`

Huddle transcription was started.

`huddle_transcription_start_notification`

A user was notified that huddle transcription started.

`slack_ai_canvas_content_generated`

AI-generated content was created for a canvas.

`slack_ai_file_summary_deleted`

An AI file summary was deleted.

`slack_ai_file_summary_generated`

An AI file summary was generated and stored.

`slack_ai_file_summary_translation_generated`

A translation was generated for a file summary.

`slack_ai_huddle_notes_generated`

AI notes were generated for a huddle.

`slack_ai_message_explanation_generated`

An AI explanation was generated for a message.

`slack_ai_message_translation_generated`

A translation was generated for a message.

`slack_ai_permissions_reset`

AI feature permissions were reset to the default.

`slack_ai_summary_requested`

A user requested an AI summary.

### App {#app}

Action

Description

`agentforce_agent_actions_updated`

Actions were updated for an Agentforce agent.

`agentforce_agent_activated`

An Agentforce agent was activated.

`agentforce_agent_deactivated`

An Agentforce agent was deactivated.

`agentforce_agent_metadata_updated`

Metadata was updated for an Agentforce agent.

`agentforce_agent_slack_connection_added`

A Slack connection was added to an Agentforce agent.

`agentforce_agent_slack_connection_removed`

A Slack connection was removed from an Agentforce agent.

`agentforce_agent_slack_deleted`

An Agentforce agent was deleted from Slack.

`app_agentforce_session_created_from_prompt_link`

A user began talking to an agent via a prompt link.

`app_agentforce_shareable_prompt_created`

A user created an Agentforce prompt link.

`app_approved`

On workspaces that have [admin approved apps](https://slack.com/help/articles/222386767-Manage-apps-for-your-workspace) enabled, an app has been approved but not yet installed.

`app_deleted`

An app has been deleted.

`app_deployed`

An app has been deployed to Slack.

`app_installed`

An app has been installed. If a custom integration had been disabled, this event will also be triggered if it is re-enabled.

`app_manifest_created`

An app manifest was created. This occurs prior to the app being installed and made available to users.

`app_manifest_updated`

An app manifest was updated. This occurs prior to the app being installed and made available to users. Please see the additional action `app_scopes_expanded`, which occurs when an update results in additional access to resources.

`app_removed_from_whitelist`

An app was removed from the allowed list.

`app_resources_added`

[Workspace apps](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021) have the ability to request access to a [specific resource on a workspace](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021#resources), such as a channel or a DM, including wildcard resources (such as all public channels). This event is triggered when access has been granted.

`app_resources_granted`

An app resource was granted.

`app_restricted`

On workspaces that have [admin approved apps](https://slack.com/help/articles/222386767-Manage-apps-for-your-workspace) enabled, an app has been restricted and cannot be installed.

`app_scopes_expanded`

An app has been granted additional access to resources on a workspace or organization, via OAuth scopes. For most apps, this requires a re-install.

`app_token_preserved`

An app's token was preserved instead of revoked, usually due to an app owner or installer being removed from an organization.

`app_uninstalled`

A Slack app was uninstalled.

`app_variable_added`

An environment variable was added to the app or the value was updated.

`app_variable_removed`

An environment variable was removed from the app.

`bot_token_downgraded`

A bot app's token was downgraded to non-granular permissions.

`bot_token_upgraded`

A bot app's token was upgraded with granular permissions.

`org_app_future_workspace_install_disabled`

Disabled auto install of organization installed apps to future workspaces.

`org_app_future_workspace_install_enabled`

Enabled auto install of organization installed apps to future workspaces.

`org_app_upgraded_to_org_install`

An app was granted access to all workspaces that previously had the app installed.

`org_app_workspace_added`

An App was added on a workspace.

`org_app_workspace_removed`

An App was removed from a workspace.

### Canvas {#canvas}

Action

Description

`canvas_access_added`

Canvas access granted to a user or channel.

`canvas_access_downgraded`

Canvas access was downgraded for a channel.

`canvas_access_revoked`

Canvas access revoked from a user or channel.

`canvas_access_upgraded`

Canvas access was upgraded for a channel.

`canvas_converted_to_standalone`

A channel canvas was converted to a standalone canvas. This action is taken on our side, not by a user.

`canvas_converted_to_template`

A canvas was converted to a template.

`canvas_created`

A canvas was created.

`canvas_deleted`

A canvas was deleted.

`canvas_downloaded`

A canvas was downloaded via a private download link.

`canvas_edited`

A canvas was edited.

`canvas_linksharing_disabled`

Canvas link sharing was set to restricted.

`canvas_linksharing_enabled`

Canvas link sharing was set to view or edit.

`canvas_merged`

A canvas was merged from another canvas.

`canvas_opened`

A canvas was opened.

`canvas_ownership_transferred`

Canvas ownership was transferred to another user.

`canvas_restored`

A canvas was restored.

`canvas_shared`

A canvas was shared in a channel, direct message, or multi-party direct message.

`canvas_tombstoned`

A canvas was tombstoned.

`canvas_unshared`

A canvas was unshared from a channel, direct message, or multi-party direct message.

`canvas_template_reverted`

A canvas template was reverted back to a canvas.

`canvas_template_used`

A canvas template was used.

### Channel {#channel}

Action

Description

`channel_can_huddle_pref_changed_from_org_level`

Channel huddle permission updated through channel management tool.

`channel_email_address_created`

An email forwarding address was created for a channel.

`channel_email_address_deleted`

An email forwarding address was deleted from channel.

`channel_enable_at_channel_pref_changed_from_org_level`

Channel mention posting permission updated for channel through the channel management tool.

`channel_enable_at_here_pref_changed_from_org_level`

Here mention posting permission updated for channel through the channel management tool.

`channel_huddle_properties_updated`

Channel huddle properties updated through the channel management tool.

`channel_membership_limit_changed_from_org_level`

Channel membership limit updated through the channel management tool.

`channel_moved`

A channel has been moved to a different workspace.

`channel_posting_permissions_updated`

Posting permissions updated for a channel through the channel posting permissions modal.

`channel_posting_pref_changed_from_org_level`

Channel posting permission updated through the channel management tool.

`channel_renamed`

A channel has been renamed.

`channel_retention_changed`

Message retention policy was changed for a channel.

`channel_tab_added`

Channel tab was added for a channel.

`channel_tab_removed`

Channel tab was removed for a channel.

`channel_workspaces_updated`

The scope of a multi-workspace channel was updated.

`dm_user_added`

A user was added to an existing DM conversation.

`featured_workflow_added`

A Featured workflow was added to the channel.

`featured_workflow_removed`

A Featured workflow was removed from the channel.

`group_converted_to_channel`

Group has been converted to channel.

`guest_channel_join`

A guest user has joined a channel. This action contains a `team` identifier so that you can see which team the joining guest comes from (useful for externally shared channels).

`guest_channel_leave`

A guest user has left a channel. This action contains a `team` identifier so that you can see which team the departing guest comes from (useful for externally shared channels).

`guest_created`

A guest was invited to a channel. This action contains a `team` identifier so that you can see which team the inviting user comes from.

`mpim_converted_to_private`

A multi-party direct message was converted to a private channel.

`private_channel_archive`

A private channel was archived.

`private_channel_converted_to_public`

A channel which was once private is now public.

`private_channel_created`

A private channel was created.

`private_channel_deleted`

A private channel was deleted.

`private_channel_unarchive`

A private channel was unarchived.

`private_message_forwarded`

A message from a DM or private channel was forwarded or shared via link.

`public_channel_archive`

A public channel was archived.

`public_channel_converted_to_private`

A channel which was once public is now private.

`public_channel_created`

A public channel was created.

`public_channel_deleted`

A public channel was deleted.

`public_channel_preview`

Conversations of a public channel are viewed by a user who is not a member of the channel.

`public_channel_unarchive`

A public channel was unarchived.

`service_owner_transferred`

Service owner has been transferred on request from primary owner.

`user_channel_join`

A user has joined a channel. The actor parameter describes the `user` who joined the channel and the `entity` describes the channel. If the user was invited to the channel, the inviter will appear in the `details` parameter and the `context` parameter will be that of the `inviter`. The `user` field in this action contains a `team` identifier so that you can see which team the joining user comes from (useful for externally shared channels).

`user_channel_leave`

A user has left a channel. This action contains a `team` identifier so that you can see which team the departing user comes from (useful for externally shared channels).

### Enterprise Key Management (EKM) {#ekm}

Action

Description

`ekm_clear_cache_set`

A revocation event has triggered a new TTL for cached date in this workspace.

`ekm_enrolled`

The workspace is now enrolled/managed by EKM.

`ekm_key_added`

An EKM key was added for the workspace.

`ekm_key_removed`

An EKM key was removed for the workspace.

`ekm_logging_config_set`

Logging settings for this workspace's EKM configuration have changed.

`ekm_slackbot_enroll_notification_sent`

Slack sent notifications about this workspace being enrolled in EKM.

`ekm_slackbot_logging_notification_sent`

Slack sent notifications about logging changes to EKM in this workspace.

`ekm_slackbot_rekey_notification_sent`

Slack sent notifications about this workspace's EKM configuration being rekeyed.

`ekm_slackbot_unenroll_notification_sent`

Slack sent notifications about this workspace no longer being enrolled in EKM.

`ekm_unenrolled`

The workspace is no longer enrolled or managed by EKM.

### Huddles {#huddles}

Action

Description

`huddle_ended`

A huddle has ended.

`huddle_knock_accepted`

Someone asked to join a huddle and was accepted.

`huddle_participant_dropped`

Someone was dropped from a huddle.

`huddle_participant_joined`

Someone has joined a huddle.

`huddle_participant_left`

Someone has left a huddle.

`huddle_started`

A huddle has started.

`huddle_screenshare_on`

Someone started sharing their screen in a huddle.

`huddle_screenshare_off`

Someone stopped sharing their screen in a huddle.

### File {#file}

Action

Description

`file_deleted`

A file was deleted.

`file_download_blocked`

A file was blocked from being downloaded.

`file_downloaded`

A file was downloaded or viewed within Slack.

`file_malicious_content_detected`

Malware scanning found malicious content in the file.

`file_public_link_created`

A public link was created for a file. This action contains a `team` identifier so that you can see which team the creating user comes from (useful for externally shared channels).

`file_public_link_revoked`

A public link was revoked from a file. This action contains a `team` identifier so that you can see which team the revoking user comes from (useful for externally shared channels).

`file_shared`

A file was shared in another channel. This action contains a `team` identifier so that you can see which team the uploading user comes from (useful for externally shared channels).

`file_uploaded`

A file was uploaded.

### Function {#function}

Action

Description

`function_distribution_permission_added`

A [function](/tools/deno-slack-sdk/guides/controlling-access-to-custom-functions) permission has been added.

`function_distribution_permission_removed`

A [function](/tools/deno-slack-sdk/guides/controlling-access-to-custom-functions) permission has been removed.

`function_distribution_permission_set`

A [function](/tools/deno-slack-sdk/guides/controlling-access-to-custom-functions) permission has been set.

### Legal holds {#legal-holds}

Action

Description

`legal_hold_policy_created`

A legal hold was created.

`legal_hold_policy_entities_added`

Entities added to legal hold policy.

`legal_hold_policy_entities_deleted`

Entities deleted from legal hold policy.

`legal_hold_policy_exclusion_added`

Exclusion added to legal hold policy.

`legal_hold_policy_exclusion_deleted`

Exclusion deleted from legal hold policy.

`legal_hold_policy_reactivated`

A legal hold was reactivated.

`legal_hold_policy_released`

A legal hold was released.

`legal_hold_policy_updated`

A legal hold was updated.

### List {#list}

Action

Description

`list_access_added`

List access was granted to a user or channel.

`list_access_downgraded`

List access was downgraded for a user or channel.

`list_access_revoked`

List access was revoked from a user or channel.

`list_access_upgraded`

List access was upgraded for a user or channel.

`list_cell_updated`

A list cell was edited.

`list_column_created`

A list column was edited.

`list_column_deleted`

A list column was deleted.

`list_column_reverted`

A list column change was reverted.

`list_column_updated`

A list column was renamed or edited; for example, by changing a single-select column to a multi-select column.

`list_converted_to_template`

A list was converted to a template.

`list_created`

A list was created.

`list_deleted`

A list was deleted.

`list_description_updated`

A list description was changed.

`list_downloaded`

A list was downloaded via a private download link.

`list_icon_updated`

The title emoji of a list was changed.

`list_linksharing_enabled`

List link sharing was set to view or edited.

`list_linksharing_disabled`

List link sharing was set to restricted.

`list_opened`

A list was opened.

`list_ownership_transferred`

List ownership transferred to another user.

`list_shared`

A list was shared in a channel, direct message, or multi-party direct message.

`list_restored`

A list was restored.

`list_row_created`

A list row was added or duplicated.

`list_row_deleted`

A list row was deleted.

`list_rows_deleted`

Multiple list rows were deleted.

`list_row_updated`

A list row was dragged and dropped to change its position.

`list_template_reverted`

A list template was reverted back to a list.

`list_title_updated`

A list title was changed.

`list_tombstoned`

A list was tombstoned.

`list_view_created`

A list view was created.

`list_view_deleted`

A list view was deleted.

`list_view_updated`

A list view had a filter, sort, or grouping applied, was renamed, was dragged and dropped to change its order, or a column within the list view was dragged and dropped to change its order.

### Native Data Loss Prevention (DLP) {#native-dlp}

Action

Description

`native_dlp_rule_action_applied`

Data Loss Prevention Rule triggered.

`native_dlp_rule_created`

Data Loss Prevention Rule created.

`native_dlp_rule_deactivated`

Data Loss Prevention Rule deactivated.

`native_dlp_rule_reactivated`

Data Loss Prevention Rule reactivated.

`native_dlp_violation_deleted`

Data Loss Prevention Rule deleted.

### Salesforce {#sales_elevate}

Action

Description

`sales_elevate_members_added`

A Slack user has been granted Sales Elevate access to a Salesforce organization.

`sales_elevate_members_removed`

A Slack user's Sales Elevate access to a Salesforce organization has been revoked.

`sales_elevate_notifications_settings_updated`

A Sales Elevate notifications setting of a Salesforce organization has been updated.

`sales_elevate_object_mappings_set`

The object mappings for a Salesforce organization has been set.

`sales_elevate_object_mappings_updated`

The object mappings for a Salesforce organization has been updated.

`sales_elevate_opportunity_list_settings_updated`

The opportunity list setting for a Salesforce organization has been updated.

`sales_elevate_org_connection_added`

A new Salesforce organization connection has been added.

`sales_elevate_org_connection_removed`

A Salesforce organization connection has been removed.

`sales_elevate_sales_admin_activity_config_changed`

The configurations related to activities for a Salesforce organization has been updated.

`sales_elevate_workflow_updated`

A Sales Elevate notification workflow config has been updated.

`salesforce_record_transferred`

A Salesforce record was transferred to another user.

### Seamless Auth {#seamless_auth}

Action

Description

`salesforce_org_deleted`

The connection between Slack and a Salesforce org was deleted.

`salesforce_org_upserted`

A Salesforce org was either inserted or updated into the database.

`salesforce_access_granted`

A user was given access to a Salesforce org.

`salesforce_access_removed`

A user's access to a Salesforce org was removed.

`salesforce_permissions_synced`

Permissions from Salesforce were synced over to Slack.

### Shared channels {#shared_channels}

Action

Description

`connect_dm_invite_accepted`

An invitation to start a Slack Connect DM was accepted.

`connect_dm_invite_generated`

An invitation to start a Slack Connect DM was sent.

`connect_dm_invite_ignored`

Slack Connect DM link was ignored.

`connect_dm_invite_revoked`

An invitation to start a Slack Connect DM was revoked.

`external_shared_channel_access_upgraded`

A channel was upgraded to a Slack Connect channel.

`external_shared_channel_connected`

A shared channel with another workspace has been connected with this one.

`external_shared_channel_disconnect_and_archived`

A shared channel was disconnected and archived.

`external_shared_channel_disconnected`

A shared channel or DM with another workspace is no longer connected with this one.

`external_shared_channel_invite_accepted`

An invitation to join a shared channel was accepted! Nice.

`external_shared_channel_invite_approved`

An invitation to join a shared channel was approved by an admin.

`external_shared_channel_invite_auto_revoked`

An invitation to join a shared channel was automatically revoked.

`external_shared_channel_invite_created`

An invitation url to join a shared channel was created.

`external_shared_channel_invite_declined`

An invitation to join a shared channel was declined.

`external_shared_channel_invite_expired`

An invitation to join a shared channel expired.

`external_shared_channel_invite_revoked`

An invitation to join a shared channel was revoked.

`external_shared_channel_reconnected`

A previously connected and then disconnected shared channel or DM with another workspace is once again shared with this one.

### Slack Model Context Protocol (MCP) Server {#mcp-server}

Action

Description

`mcp_slack_create_canvas_tool_called`

An AI app created a Canvas on behalf of a user in your organization.

`mcp_slack_read_canvas_tool_called`

An AI app read the contents of a Canvas on behalf of a user in your organization.

`mcp_slack_read_channel_tool_called`

An AI app read the contents of a channel on behalf of a user in your organization.

`mcp_slack_read_thread_tool_called`

An AI app read the contents of a message thread on behalf of a user in your organization.

`mcp_slack_read_user_profile_tool_called`

An AI app read a user profile on behalf of a user in your organization.

`mcp_slack_search_channels_tool_called`

An AI app searched channel content on behalf of a user in your organization.

`mcp_slack_search_public_and_private_tool_called`

An AI app searched public and private content on behalf of a user in your organization.

`mcp_slack_search_public_tool_called`

An AI app searched public content on behalf of a user in your organization.

`mcp_slack_search_users_tool_called`

An AI app searched users on behalf of a user in your organization.

`mcp_slack_send_message_tool_called`

An AI app sent a message on behalf of a user in your organization.

`mcp_slack_update_canvas_tool_called`

An AI app updated the contents of a Canvas on behalf of a user in your organization.

### Workflows {#workflows}

Action

Description

`workflow_app_token_preserved`

A workflows app token was preserved.

`workflow_created`

A workflow has been created.

`workflow_deleted`

A workflow has been deleted.

`workflow_published`

A workflow has been published.

`workflow_responses_csv_download`

A user downloaded a workflow’s responses as a CSV file.

`workflow_unpublished`

A workflow has been unpublished.

### Workflows v2 {#workflowsv2}

Action

Description

`external_auth_oauth2_token_fetched`

An external token was fetched. Refer to [token rotation](/authentication/using-token-rotation) for more details.

`external_auth_oauth2_token_refreshed`

An external token was refreshed. Refer to [token rotation](/authentication/using-token-rotation) for more details.

`external_auth_oauth2_token_deleted`

An external token was deleted. Refer to [token rotation](/authentication/using-token-rotation) for more details.

`workflow_trigger_permission_added`

One or more entities have been allowed access to a [workflow](/tools/deno-slack-sdk/guides/creating-workflows) [trigger](/tools/deno-slack-sdk/guides/managing-triggers#manage).

`workflow_trigger_permission_removed`

One or more entities have had their access to a [workflow](/tools/deno-slack-sdk/guides/creating-workflows) [trigger](/tools/deno-slack-sdk/guides/managing-triggers#manage) revoked.

`workflow_trigger_permission_set`

The permission type of a [workflow](/tools/deno-slack-sdk/guides/creating-workflows) [trigger](/tools/deno-slack-sdk/guides/managing-triggers#manage) has been set.

`workflow_trigger_suspicious_keyword`

A suspicious keyword was added to the `MessagePosted` event trigger configuration.

`workflow_v2_published`

A [workflow](/tools/deno-slack-sdk/guides/creating-workflows) has been published.

### User {#user}

Action

Description

`anomaly`

An anomalous user behavior was detected.

`custom_tos_accepted`

A team member accepted a custom terms of service agreement.

`custom_tos_link_clicked`

A team member viewed a custom terms of service agreement.

`guest_created`

A guest was created.

`guest_deactivated`

A guest was deactivated.

`guest_expiration_cleared`

A guest had an expiration time cleared (before this time arrived).

`guest_expiration_set`

A guest had an account expiration time set.

`guest_expired`

A guest was deactivated when the expiration time was reached.

`guest_joined_workspace`

A guest joined a workspace.

`guest_reactivated`

A guest was reactivated after having been deactivated.

`owner_transferred`

An owner was transferred.

`permissions_assigned`

A team member was assigned a permission.

`permissions_removed`

A team member was unassigned a permission.

`role_assigned`

A team member was assigned a role.

`role_change_to_admin`

A team member was made an admin.

`role_change_to_guest`

A team member was changed to a Multi-Channel Guest (MCG) or Single-Channel Guest (SCG).

`role_change_to_owner`

A team member was made an owner.

`role_change_to_user`

A team member was made a regular user.

`role_removed`

A team member was unassigned a role.

`user_created`

A team member was created.

`user_deactivated`

A team member was deactivated.

`user_email_updated`

A team member's email was updated.

`user_force_upgrade_non_compliant_mobile_app_version`

A team member was forced to upgrade due to a non-compliant mobile app version.

`user_joined_workspace`

A team member joined a workspace.

`user_login_failed`

A team member failed to login.

`user_login`

A team member logged in.

`user_logout_compromised`

A team member was logged out due to a compromised device.

`user_logout_non_compliant_mobile_app_version`

A team member was logged out due to a non-compliant mobile app version.

`user_logout`

A team member logged out.

`user_password_reset_requested`

A user requested to reset password.

`user_password_reset_slack_security`

A Slack security agent has reset the user's password. The actor will be `USLACKSECURITY`.

`user_profile_updated`

A user's profile has been updated. This action will only be recorded when `real_name`, `display_name`, `first_name`, `last_name`, `pronouns`, `title` or the profile image is updated.

`user_profile_deleted`

A user's profile information has been deleted.

`user_reactivated`

A team member was reactivated after having been deactivated.

`user_session_invalidated`

A team member's session was invalidated.

`user_session_reset_by_admin`

A team member's session was reset by an admin.

`user_sessions_reset_by_anomaly_event_response`

A team member's sessions were reset by the [anomaly event response](https://slack.com/help/articles/37193054707603) feature.

`user_session_settings_changed`

A team member's session settings were changed.

`app_agentforce_execute_slack_action`

A team member directed an Agent to execute a Slack Action.

`app_flows_execute_slack_action`

A Salesforce Flow executed a Slack Action.

### User groups {#user_groups}

Action

Description

`default_channel_added_to_usergroup`

A default channel was added to a user group.

`default_channel_removed_from_usergroup`

A default channel was removed from a user group.

`role_added_to_usergroup`

A role was added to a user group.

`role_modified_on_usergroup`

A user group role was updated.

`role_removed_from_usergroup`

A role was removed from a user group.

`user_added_to_usergroup`

A user was added to a user group.

`user_removed_from_usergroup`

A user was removed from a user group.

`usergroup_add_to_team_enqueued`

The request to add a user group to a team was enqueued.

`usergroup_added_to_team`

A user group was added to a team.

`usergroup_remove_from_team_enqueued`

The request to remove a user group from a team was enqueued.

`usergroup_removed_from_team`

A user group was removed from a team.

`usergroup_update_enqueued`

The request to update a user group was enqueued.

`usergroup_updated`

A user group was updated.

### Workspace or organization {#workspace_org}

Action

Description

`approved_orgs_added`

An organization was added to the approved organizations list.

`approved_orgs_removed`

An organization was removed from the approved organizations list.

`barrier_created`

An information barrier was created.

`barrier_deleted`

An information barrier was deleted.

`barrier_updated`

An information barrier was updated.

`billing_address_added`

A billing address was added. Includes a `details` parameter noting the timestamp the TOS was accepted.

`channels_export_completed`

A channel export is complete.

`channels_export_deleted`

A channel export was deleted.

`channels_export_downloaded`

A channel export was downloaded.

`channels_export_started`

A channel export has begun.

`cli_login`

A user has logged in with the Slack CLI to the workspace or organization.

`corporate_exports_approved`

The corporate export feature has been approved for use on a workspace.

`corporate_exports_enabled`

The corporate export feature has been enabled for a workspace.

`domain_created`

A domain was created.

`domain_deleted`

A domain was deleted.

`domain_verified`

A domain was verified.

`emoji_added`

An emoji was added. Includes a `details` parameter with the name of the emoji.

`emoji_aliased`

An emoji was given an alias. Includes a `details` parameter with the name of the alias.

`emoji_removed`

An emoji was removed. Includes a `details` parameter with the name of the emoji.

`emoji_renamed`

An emoji was renamed. Includes a `details` parameter with the previous and new names of the emoji.

`idp_configuration_added`

IdP configuration added.

`idp_configuration_deleted`

IdP configuration deleted.

`idp_prod_configuration_updated`

IdP Production configuration updated.

`idp_test_configuration_updated`

IdP Testing configuration updated.

`manual_export_completed`

A standard or corporate export has finished.

`manual_export_deleted`

A standard or corporate export was deleted.

`manual_export_downloaded`

A standard or corporate export was downloaded.

`manual_export_started`

An admin or owner has started a standard or corporate export.

`manual_user_export_completed`

A manual user export has finished.

`manual_user_export_deleted`

A manual user export was deleted.

`manual_user_export_downloaded`

A manual user export was downloaded.

`manual_user_export_started`

A manual user export has started.

`message_flagged`

A message was flagged.

`message_moderated`

A message was moderated.

`message_restored`

A message was restored.

`message_tombstoned`

A message was tombstoned.

`migration_completed`

A migration was completed.

`migration_dms_mpdms_completed`

A migration of DMs and MPDMs completed.

`migration_scheduled`

A migration was scheduled.

`organization_accepted_migration`

The Org Owner accepted a workspace invitation to join their organization.

`organization_created`

An Enterprise organization was created.

`organization_declined_migration`

The Org Owner declined a workspace invitation to join their organization.

`organization_deleted`

An Enterprise organization was deleted.

`organization_domain_changed`

An Enterprise organization's domain was changed.

`organization_public_url_updated`

Your organization’s public URL has been changed.

`organization_renamed`

An Enterprise organization was renamed.

`organization_unverified`

Slack has flagged a change in your organization’s identity and has unverified it. The organization will no longer be denoted with a verified badge.

`organization_verified`

Slack has confirmed the identity of your organization. The organization will now be denoted with a verified badge.

`scheduled_export_completed`

A scheduled export has finished.

`scheduled_export_deleted`

A scheduled export was deleted.

`scheduled_export_downloaded`

A scheduled export was downloaded.

`scheduled_export_started`

A scheduled export has started.

`team_authorized_ip_range_set`

The authorized IP ranges has been set for desktop block file download feature.

`team_unsupported_versions_job_end`

An Unsupported Versions report job has completed.

`team_unsupported_versions_job_start`

An Unsupported Versions report job has started.

`team_unsupported_versions_start_failure`

A request to generate the Unsupported Versions report has failed.

`team_unsupported_versions_start_success`

A request to generate the Unsupported Versions report has been scheduled successfully.

`thread_replies_disabled`

Thread replies have been disabled.

`thread_replies_enabled`

Thread replies have been enabled.

`workspace_accepted_migration`

An administrator on a workspace has accepted an invitation to migrate to an Enterprise organization.

`workspace_created`

A workspace in an organization was created.

`workspace_declined_migration`

An administrator on a workspace has declined an invitation to migrate to an Enterprise organization.

`workspace_deleted`

A workspace in an organization was deleted.

`audit_logs_records_searched`

A user searched for audit logs from the Audit Logs screen on organization dashboard.

`audit_logs_export_csv_started`

A user started a CSV export of audit logs from the Audit Logs screen on organization dashboard.

`audit_logs_export_json_started`

A user started a JSON export of audit logs from the Audit Logs screen on organization dashboard.

### Workspace or organization preferences {#workspace_org_preferences}

Action

Description

`auth_policy_created`

Auth policy created.

`auth_policy_entity_assigned`

Entity has been assigned to auth policy.

`auth_policy_entity_removed`

Entity has been removed from auth policy.

`bulk_session_reset_by_admin`

Admin has bulk reset user sessions.

`intune_disabled`

Microsoft Intune Enterprise MDM disabled.

`intune_enabled`

Microsoft Intune Enterprise MDM enabled.

`pref.agentforce_workspaces_settings_changed`

The workspaces settings for Agentforce, including the blocked workspaces and default workspaces to grant access to.

`pref.allow_calls`

A preference indicating whether Slack Calls can be used in this workspace has changed.

`pref.allow_canvas_version_history_changed`

The ability for editors of a canvas to access history and restore prior versions has been enabled or disabled.

`pref.allow_huddles_transcriptions_changed`

The setting for allowing huddles transcriptions has been changed.

`pref.allow_message_deletion`

Someone altered this workspace's settings around whether messages can be deleted or not.

`pref.allow_native_gif_picker`

Someone altered this workspace's settings around whether the gif picker can be accessed or not.

`pref.allow_slack_ai_changed`

The setting controlling access to all Slack AI features for the organization has been changed. This is a global toggle for all AI functionality.

`pref.anomaly_event_response_changed`

Someone modified which [anomaly events](/reference/audit-logs-api/anomalous-events-reference) automatically end all user sessions, or which admins are notified. Includes a `details` parameter noting the previous and new values.

`pref.app_dir_only`

Whether only Slack Marketplace apps can be installed or not in this workspace has changed.

`pref.app_whitelist_enabled`

Someone has carefully carved or culled the list of apps this workspace allows.

`pref.block_download_and_copy_on_untrusted_mobile`

The setting of blocking file download and copy on untrusted mobile device.

`pref.block_file_download_for_unapproved_ip`

The setting of blocking file download on desktop client with unauthorized IP ranges.

`pref.can_receive_shared_channels_invites`

Whether this workspace can receive invites to share channels with other workspaces has changed.

`pref.canvas_retention_changed`

The canvas retention setting changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.commands_only_regular`

The setting determining whether restricted users are restricted from using slash commands was changed.

`pref.custom_tos`

This workspace's settings on having a custom terms of service have changed.

`pref.disallow_public_file_urls`

This workspace has modified their public file URL settings for files uploaded within it.

`pref.dm_retention_changed`

The direct message (DM) retention setting changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.dnd_enabled`

_Do not disturb_ settings have been enabled for a workspace.

`pref.dnd_end_hour`

The exact ending hour for workspace _do not disturb_ settings has been set. Work hard and go home.

`pref.dnd_start_hour`

The exact starting hour for workspace _do not disturb_ settings has been set. Hopefully everyone is awake and ready to work by then.

`pref.emoji_only_admins`

Someone modified the list of emoji-administrating admins.

`pref.enterprise_default_channels`

Someone modified the list of default channels across the Enterprise organization.

`pref.enterprise_mobile_device_check`

Check to see if the user is attempting to log in on a mobile device.

`pref.enterprise_search_connectors_changed`

The list of enterprise search connectors enabled or their permissions have changed.

`pref.enterprise_search_connectors_config_changed`

The list of enterprise search connectors enabled or their configurations have changed.

`pref.enterprise_search_enabled_changed`

The setting to enable enterprise search across your organization has changed.

`pref.enterprise_team_creation_request`

Someone has requested that your organization allow a new workspace to be created.

`pref.file_retention_changed`

The file retention setting changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.invites_only_admins`

Settings determining whether or not invites need admin approval to be sent out changed.

`pref.invite_requests_approval_channel`

The channel where invite requests get sent to admins got changed.

`pre.max_guest_duration`

A max guest duration (in days) was set. This preference can only be set at the Enterprise level from the Org dashboard.

`pref.member_analytics_disabled`

Someone changed whether to allow user with analytics access to view member analytics.

`pref.ml_opt_out`

The organization's ML opt out preference was changed.

`pref.mobile_session_duration_changed`

The organization's mobile session duration was changed.

`pref.msg_edit_window_mins`

Someone edited the edit messaging window for a workspace.

`pref.private_channel_analytics_disabled`

Someone changed whether to allow user with analytics access to view private channel analytics.

`pref.private_channel_retention_changed`

The group (private channel) retention setting changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.private_record_channel_retention_changed`

The private Salesforce record channel retention setting changed. Includes a `details` parameter noting the previous and new values.

`pref.private_record_channel_retention_duration_changed`

The private Salesforce record channel retention duration changed. Includes a `details` parameter noting the previous and new values.

`pref.private_record_channel_redaction_duration_changed`

The private Salesforce record channel redaction duration changed. Includes a `details` parameter noting the previous and new values.

`pref.public_channel_retention_changed`

The channel retention setting type changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.public_record_channel_retention_changed`

The public Salesforce record channel retention setting changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.public_record_channel_retention_duration_changed`

The public Salesforce record channel retention duration changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.public_record_channel_redaction_duration_changed`

The public Salesforce record channel redaction duration changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.retention_override_changed`

The retention override setting, allowing workspace members to set their own retention period for private channels and DMs, changed. Includes a `details` parameter noting the previous and new values. Values are as follows: `RETAIN_ALL` (keep all messages and track edit history), `RETAIN_MSGS` (keep all messages but don’t track edit history), `EXPIRE_ALL` (delete all messages and edit history), `EXPIRE_MSGS` (delete all messages and edit history after a set number of days). A `null` value defaults to `EXPIRE_MSGS`.

`pref.session_duration_changed`

The organizations session duration was changed.

`pref.session_duration_type_changed`

The organization's session type has has changed.

`pref.sign_in_with_slack_disabled`

This workspace changed their preference around allowing [Sign in with Slack](/authentication/sign-in-with-slack).

`pref.slack_ai_allowed_search_files_changed`

The setting controlling the types of files that can be included in AI search answers was changed.

`pref.slack_ai_allowed_workspaces_changed`

The list of workspaces where Slack AI features are permitted was modified.

`pref.slack_ai_allow_detailed_feedback_changed`

The setting allowing users to send detailed feedback (including summary text and free-form comments) about Slack AI features was changed.

`pref.slack_ai_allow_feedback_changed`

The setting allowing users to provide any feedback about Slack AI features (including simple thumbs up/down ratings) was changed.

`pref.slack_ai_allow_file_summaries_changed`

The setting allowing Slack AI file summaries was changed.

`pref.slack_ai_allow_huddle_notes_changed`

The setting allowing Slack AI huddle notes was changed.

`pref.slack_ai_allow_translations_changed`

The setting allowing Slack AI translations was changed.

`pref.slack_ai_allow_recap_changed`

The setting allowing Slack AI recap was changed.

`pref.slack_ai_allow_workflow_builder_changed`

The setting allowing Slack AI workflow builder was changed.

`pref.slackbot_responses_disabled`

The settings around whether Slackbot's witty responses are enabled or disabled changed.

`pref.slackbot_responses_only_admins`

There's a secret cabal of admins for those witty Slackbot responses and that list was changed.

`pref.sso_setting_changed`

The Single Sign On (SSO) restriction changed. Includes a `details` parameter noting the previous and new values.

`pref.stats_only_admins`

The list of admins that can work with workspace statistics _only_ has changed.

`pref.two_factor_auth_changed`

The two-factor authentication requirement changed. Includes a `details` parameter noting the previous and new values.

`pref.two_factor_prevent_sms_changed`

Allowed usage of SMS for two-factor authentication has changed. Includes a `details` parameter noting the previous and new values.

`pref.uneditable_user_profile_fields`

A list of read-only user profile fields.

`pref.username_policy`

A workspace's username policy preference changed.

`pref.who_can_archive_channels`

The list of who is allowed to archive channels changed.

`pref.who_can_create_delete_user_groups`

The list of who can create or delete user groups changed.

`pref.who_can_create_private_channels`

The list of who can create private channels changed.

`pref.who_can_create_public_channels`

The same as above, but for public channels.

`pref.who_can_edit_user_groups`

The list of who can edit user groups changed.

`pref.who_can_manage_channel_posting_prefs`

The list of who can manage channel posting preferences changed.

`pref.who_can_manage_ext_shared_channels`

The list of who can manage externally shared channels has changed.

`pref.who_can_manage_guests`

The list of who can manage guests has changed.

`pref.who_can_manage_shared_channels`

Settings around _who can remove users from **shared** channels_ has changed for a workspace.

`pref.who_can_remove_from_private_channels`

Settings around _who can remove users from **private** channels_ has changed for a workspace.

`prefs_setting_changed`

Preference settings was updated.

`slack_connect_guidelines_changed`

Slack Connect guidelines have been changed.

`slack_connect_invite_routing_disabled`

Slack Connect invite routing has been disabled.

`slack_connect_invite_routing_enabled`

Slack Connect invite routing has been enabled.

`slack_connect_pref_migrated`

Slack Connect preference has been migrated.

`slack_connect_pref_removed`

Slack Connect preference has been removed.

`slack_connect_pref_set`

Slack Connect preference has been set.

## Errors {#errors}

Occasionally, interacting with Slack APIs will result in an error instead of, well, a result. Slack will make every attempt to respond with a descriptive error message that will help you figure out what went wrong and how to fix it.

Error

Description

`bad_endpoint`

The endpoint URL does not exist.

`feature_not_enabled`

Audit Logs are not available on your workspace, probably because it is not part of an Enterprise organization.

`invalid_action`

The action is not supported.

`invalid_authentication`

The authentication token is not valid. Check that the token is associated with an Enterprise organization owner and that it has the `auditlogs:read` scope.

`invalid_cursor`

The [pagination](/apis/web-api/pagination#cursors) cursor is invalid. Check that it matches the cursor that was returned by the previous request.

`invalid_range`

The range specified in the filter is not valid. This may indicate a date from before the feature was enabled or at some point in the future.

`invalid_workspace`

The Audit Logs API can not be used with this workspace, most likely because it not a part of an Enterprise organization.

`method_not_allowed`

This method is not allowed on the workspace or with the token used.

`missing_authentication`

The OAuth token is either missing from the header of the request or malformed.

`rate_limited`

The app is calling the API too often. Please slow down.

`team_not_authorized`

The app is installed on a Slack workspace but needs to be installed in an Enterprise organization.

`user_not_authorized`

The user who installed the app is not an Enterprise organization owner — they must be an Enterprise organization owner.