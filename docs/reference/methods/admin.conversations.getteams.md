Source: https://docs.slack.dev/reference/methods/admin.conversations.getTeams

# admin.conversations.getTeams method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**Get all the workspaces a given public or private channel is connected to within this Enterprise org.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.conversations.getTeams
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.conversations.getTeams
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_conversations_getTeams
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminConversationsGetTeams
```

**Scopes**

User token:

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel_id`**Required

The channel to determine connected workspaces within the organization for.

_Example:_ `C12345`

### Optional arguments

**`cursor`**`string`Optional

Set `cursor` to `next_cursor` returned by the previous call to list items in the next page

_Example:_ `5c3e53d5`

**`limit`**`integer`Optional

The maximum number of items to return. Must be between 1 - 1000 both inclusive.

_Default:_ `100`

_Example:_ `100`

## Usage info {#usage-info}

This [Admin API method](/admins) gets the workspaces connected to a given channel _within the organization_.

Note: this method doesn't list workspaces from other Enterprise organizations that are also connected to the same channel.

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
{  "ok": true,  "team_ids": [    "T1234",    "T5679"  ]}
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

`channel_not_found`

The channel wasn't found or isn't connected to multiple workspaces.

`channel_type_not_supported`

The `channel_id` provided was a DM, MPDM, or the 'general' channel.

`could_not_get_teams`

Could not fetch the workspaces that the channel is shared with in this organization.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_channel_migrating`

The channel is actively being migrated

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

The token provided doesn't have access to this method.

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

`invalid_cursor`

The provided cursor wasn't valid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_limit`

The value passed for `limit` wasn't valid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

A workspace preference prevents the authenticated user from listing the workspaces connected to a channel.

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

`unsupported_team_type`

This endpoint can only called by Enterprise organizations.