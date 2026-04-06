Source: https://docs.slack.dev/reference/methods/conversations.acceptSharedInvite

# conversations.acceptSharedInvite method

DocsCall generator

## Facts {#facts}

**Description**Accepts an invitation to a Slack Connect channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.acceptSharedInvite
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.acceptSharedInvite
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_acceptSharedInvite
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsAcceptSharedInvite
```

**Scopes**

Bot token:

[`conversations.connect:write`](/reference/scopes/conversations.connect.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel_name`**`string`Required

Name of the channel. If the channel does not exist already in your workspace, this name is the one that the channel will take.

_Example:_ `puppies-r-us`

### Optional arguments

**`is_private`**`boolean`Optional

Whether the channel should be private.

_Example:_ `true`

**`free_trial_accepted`**`boolean`Optional

Whether you'd like to use your workspace's free trial to begin using Slack Connect.

**`invite_id`**Optional

ID of the invite that you’d like to accept. Must provide either `invite_id` or `channel_id`. See the [`shared_channel_invite_received`](/reference/events/shared_channel_invite_received) event payload for more details on how to retrieve the ID of the invitation.

**`channel_id`**Optional

ID of the channel that you'd like to accept. Must provide either `invite_id` or `channel_id`.

**`team_id`**Optional

The ID of the workspace to accept the channel in. If an org-level token is used to call this method, the `team_id` argument is required.

## Usage info {#usage-info}

This [Slack Connect API](/apis/slack-connect/using-slack-connect-api-methods) method accepts an invitation to a Slack Connect channel.

If the channel does not already exist in your app's workspace, this method creates, and names, the Slack Connect channel inside your workspace.

If your app's workspace is not on a paid plan, this API will also start a free trial for your workspace (as long as you qualify and you use the `free_trial_accepted` parameter.

After an invite is accepted by your app, the Slack Connect channel may still need to be [approved](/reference/methods/conversations.approveSharedInvite) by Admins on your workspace or the host organization.

* * *

## Response {#response}

When your app successfully accepts a Slack Connect channel invite:

```
{	"ok": true,	"implicit_approval": true,	"channel_id": "C0001111",	"invite_id": "I00043221"}
```

If your app cannot accept because the workspace on which your app is installed has already had a free trial in the past and is not a paid team currently:

```
{	"ok": false,	"error": "not_paid"}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_conversion_in_progress`

Unable to create a channel connection while a channel conversion is in progress

`connection_limit_exceeded`

This channel has hit the limit of external connections.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`email_does_not_match`

User's email does not match the email in the invite.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`failed_to_start_trial`

Unable to initiate a trial on shared invite acceptance

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`has_already_connected_to_org`

A team on the workspace of the org is already in the channel.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

Invalid API arguments were provided. Either `sig` or `invite_id` must be specified.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_emoji_not_allowed`

The desired name contains emoji.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_host_team`

The host workspace is invalid.

`invalid_link`

We couldn't find an invite associated with the ID provided.

`invalid_name`

The value passed for `channel_name` was invalid.

`invalid_name_maxlength`

The value passed for `channel_name` exceeded the maximum length.

`invalid_name_punctuation`

The value passed for `channel_name` contained only punctuation.

`invalid_name_required`

The value passed for `channel_name` was empty.

`invalid_name_specials`

The value passed for `channel_name` contained unallowed special characters or upper case characters.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_privacy`

An invalid channel privacy was provided.

`invalid_recipient_team`

The accepting team does not match the expected recipient team.

`invalid_target_team`

The target workspace is invalid.

`invite_from_same_org`

You can't accept an invite from the same org or workspace.

`invite_not_found`

We couldn't find a Slack Connect channel invite with the ID provided.

`invite_used`

This invite has already been accepted.

`is_pending_connected_to_org`

A team pending to join the channel is on the org of the team trying to accept.

`legacy_connection_invalid_org`

Teams not previously connected to this legacy channel can't connect.

`legacy_connection_limit_exceeded`

You cannot share a legacy ESC channel with a third team

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`name_taken`

The desired channel name is already taken in your workspace.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_for_grid_workspace`

Acceptance is not allowed for this workspace.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`not_paid`

This workspace doesn't have access to this feature.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

A team preference prevents the authenticated user from creating private channels.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_found`

The team provided in the `team_id` argument does not exits.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`user_cannot_create_channel`

This user is not allowed to create a channel.

`user_is_restricted`

This user is restricted and cannot accept the invite.

`user_not_found`

The user accepting the invite is not a member of the team provided in the `team_id` argument.

`user_required_to_accept_as_private_but_cannot`

This uer cannot accept a private channel invitation.