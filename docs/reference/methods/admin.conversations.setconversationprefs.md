Source: https://docs.slack.dev/reference/methods/admin.conversations.setConversationPrefs

# admin.conversations.setConversationPrefs method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**Set the posting permissions for a public or private channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.conversations.setConversationPrefs
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.conversations.setConversationPrefs
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_conversations_setConversationPrefs
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminConversationsSetConversationPrefs
```

**Scopes**

User token:

[`admin.conversations:write`](/reference/scopes/admin.conversations.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel_id`**`string`Required

The channel to set the prefs for

_Example:_ `C1234`

**`prefs`**`string`Required

The prefs for this channel in a stringified JSON format.

_Example:_ `{'who_can_post':'type:admin,user:U1234'}`

## Usage info {#usage-info}

This [Admin API method](/admins) sets the posting permissions for a channel.

This method allows you to adjust several conversation settings. To set any of these permissions, you'll use the `prefs` argument with some stringified JSON. Stringified JSON means JSON with white space removed and fields marked by single quotations. Since this argument won't contain more complex characters, you don't need to do further encoding.

Calling this method requires that you — the user associated with your app's token — have permission to change conversation preferences.

You can see or change the users who have permission in your Org’s Channel Management settings dashboard.

### Posting permissions {#posting-permissions}

To adjust who's allowed to post in a channel, use the `who_can_post` field inside your `prefs` argument:

```
"prefs": "{'who_can_post':'type:admin,user:U1234'}"
```

Inside your stringified JSON for `who_can_post`, you can specify who the permission applies to in a couple different ways:

*   By `type`: you can set posting permissions to include all `admin` users, or just any `user` in general. The `user` type is only honored when `admin` or `org_admin` is also provided.
    
*   By list of specific users who have the permission: `user:U1234` for a single user or `user:U1234,user:U5678` for multiple users. If you're specifying specific people, you can select up to 100 per channel. If you exceed that maximum, you may receive the `could_not_set_channel_pref` error.
    

`org_admin` can only be used if the channel is an Org-Wide Channel, otherwise you may receive the `invalid_value` error.

The `can_thread` field works exactly the same inside the `prefs` object, except that it determines who can respond in threads. You can pass both `who_can_post` and `can_thread` to the `prefs` argument in this method at the same time.

Example:

```
"prefs": "{'who_can_post':'type:admin,user:U1234','can_thread':'type:user'}"
```

In addition, while you cannot return to the original "empty" state of each of these fields when the channel is first created, you can always reset the channel to allow everyone to post by using the value `ra`:

```
"prefs": "{'who_can_post':'type:ra','can_thread':'type:ra'}"
```

#### Slack Connect {#slack-connect}

In [Slack Connect channels](/apis/slack-connect/), the same fields and values are used by the channel owner (home workspace) to control who can post in a given channel, but they have slightly different meanings:

*   `type:ra` means that all home and away workspace members and guests can post.
*   `type:regular` means that only home workspace members can post, but away workspace members and home/away workspace guests cannot.
*   `type:admin` means that only home admins can post, but home/away workspace members or guests cannot.
*   `type:org_admin` means that only home org admins can post, but home/away workspace members or guests cannot.

When listing individual users who can post in the channel, you are free to include user IDs of both home and away users.

### Huddles {#huddles}

The `can_huddle` field determines if a huddle can be started in the channel.

For example:

```
"prefs": "{'can_huddle':'false'}"
```

### Channel mentions {#channel-mentions}

Channel mention restriction prefs `enable_at_channel` and `enable_at_here` can be used to place channel, here, and everyone mention restrictions in a channel.

The `enable_at_channel` field determines if channel mentions can be used in a channel. The `enable_at_here` field determines if here mentions can be used in a channel. If these channel prefs have never been set before for a channel, then the relevant mention can be used in a channel. We require that both of these prefs remain synced so if you would like to set one of these prefs, you must also update the other pref, and they must be the same value. We do this because the everyone mention restriction in general channels is also controlled by these prefs.

For example:

```
"prefs": "{'enable_at_channel':'false', 'enable_at_here':'false'}"
```

This admin scope is obtained through version two of the OAuth V2 flow, but there are a few additional requirements. The app requesting this scope must be installed by an admin or Owner of an Enterprise organization. Also, the app must be installed on the entire org, not on an individual workspace. See below for more details.

If the app is installed by an Org Admin or Owner, ensure the Channel Management settings provide the appropriate permissions. The Org Admin or Owner installing the app must have the **Channel Management** role, and must also be granted access to **Public channels** and **Private channels** within this role. If these criteria aren't met, the Org Admin or Owner will receive a `not_allowed` error when attempting to install an app.

Admin API endpoints reach across **an entire Enterprise organization**, not individual workspaces.

For a token to be imbued with Admin scopes, it must be obtained from installing an app on the **entire Enterprise org**, not just a workspace within the organization.

To configure and install an app supporting Admin API endpoints on your Enterprise organization:

1.  [Create a new Slack app](https://api.slack.com/apps). Your app will need to be able to handle a standard [OAuth 2 flow](/authentication/installing-with-oauth).
2.  In the app's settings, select **OAuth & Permissions** from the left navigation. Scroll down to the section titled **Scopes** and add the `admin.*` scope you want. Click the **Save Changes** button.
3.  In the app's settings, select **Manage Distribution** from the left navigation. Under the section titled **Share Your App with Other Workspaces**, make sure all four sections have the green check. Then click the green **Activate Public Distribution** button.
4.  Under the **Share Your App with Your Workspace** section, copy the **Sharable URL** and paste it into a browser to initiate the OAuth handshake that will install the app on your organization. You must be logged in as an **admin or Owner** of your Enterprise organization to install the app.
5.  Check the dropdown in the upper right of the installation screen to make sure you are installing the app on the organization, not an individual workspace within the organization. See the image below for a visual.
6.  Once your app completes the OAuth flow, you will be granted an OAuth token that can be used for calling Admin API methods for your organization.

![](/img/guides/admin/workspace-v-org-audit.png)

_When installing an app to use an Admin API endpoint, be sure to install it on your Enterprise organization, not a workspace within the organization._

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
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

`channel_mention_sync_required`

If setting channel mention restriction prefs, both mention prefs must be passed and they must be the same value.

`channel_not_found`

Value passed for `channel` was invalid.

`channel_type_not_supported`

Value given for `channel_id` was a #general channel.

`could_not_set_channel_pref`

Setting the preference or permission failed.

`default_org_wide_channel`

Returned when you try to modify a default org wide channel.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

The Admin APIs feature is not enabled for this team.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_value`

Value passed for the preferences are invalid

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The calling token is not granted the necessary scopes to complete this operation.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

The token provided is not associated with an org admin.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

A workspace preference prevents the authenticated user from archiving.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.