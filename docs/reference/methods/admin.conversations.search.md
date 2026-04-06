Source: https://docs.slack.dev/reference/methods/admin.conversations.search

# admin.conversations.search method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**Search for public or private channels in an Enterprise organization.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.conversations.search
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.conversations.search
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_conversations_search
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminConversationsSearch
```

**Scopes**

User token:

[`admin.conversations:read`](/reference/scopes/admin.conversations.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`team_ids`**`array`Optional

Comma separated string of team IDs, signifying the internal workspaces to search through.

_Example:_ `T00000000,T00000001`

**`connected_team_ids`**`array`Optional

Array of encoded team IDs, signifying the external orgs to search through.

_Example:_ `['T00000000','T00000001']`

**`query`**`string`Optional

Name of the the channel to query by.

_Example:_ `announcement`

**`limit`**`integer`Optional

Maximum number of items to be returned. Must be between 1 - 20 both inclusive. Default is 10.

_Default:_ `10`

_Example:_ `20`

**`cursor`**`string`Optional

Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.

_Example:_ `dXNlcjpVMEc5V0ZYTlo=`

**`search_channel_types`**`array`Optional

The type of channel to include or exclude in the search. For example `private` will search private channels, while `private_exclude` will exclude them. For a full list of types, check the [Types section](#types).

_Example:_ `private,archived`

**`sort`**`string`Optional

Possible values are `relevant` (search ranking based on what we think is closest), `name` (alphabetical), `member_count` (number of users in the channel), and `created` (date channel was created). You can optionally pair this with the `sort_dir` arg to change how it is sorted

_Default:_ `member_count`

_Example:_ `name`

**`sort_dir`**`string`Optional

Sort direction. Possible values are `asc` for ascending order like (1, 2, 3) or (a, b, c), and `desc` for descending order like (3, 2, 1) or (c, b, a)

_Default:_ `desc`

_Example:_ `asc`

**`total_count_only`**`boolean`Optional

Only return the total\_count of channels. Omits channel data and allows access for admins without channel manager permissions.

## Usage info {#usage-info}

This [Admin API method](/admins) searches for channels across an organization given a search query.

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

### More on channel types {#types}

The `search_channel_types` allows an array of types to be passed, each of which filters the channels that the search returns. If you pass multiple types, the search occurs in channels that satisfy **any** of the types. You can pass the following values in your list of `search_channel_types`:

*   `private`
*   `private_exclude`
*   `archived`
*   `exclude_archived`
*   `private_exclude_archived`
*   `multi_workspace`
*   `org_wide`
*   `external_shared_exclude`
*   `external_shared`
*   `external_shared_private`
*   `external_shared_archived`
*   `exclude_org_shared`

`private` will search private channels, and `private_exclude` will exclude them from the search. The other names follow the same patterns for channels connected to other organizations and archived channels.

Searching private channels with this method will only work if the user associated with the user token being used has permission to manage private channels on the org. By default, only the [primary owner of the org has that level of permission](https://slack.com/help/articles/360052445454-Manage-permissions-for-channel-management-tools#h_01J6FQ9ATH7WVCZCZCHKG9P64Z). Missing this permission is a cause of the `not_allowed` error.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "conversations": [    {      "id": "GSEV0B5PY",      "name": "privacy-channel",      "purpose": "Group messaging with: @rita @nwhere @meanie",      "member_count": -1,      "created": 1578423973,      "creator_id": "WPQ65MVKK",      "is_private": true,      "is_archived": true,      "is_general": false,      "last_activity_ts": 1583198954000200,      "is_ext_shared": false,      "is_global_shared": true,      "is_org_default": false,      "is_org_mandatory": false,      "is_org_shared": true,      "is_frozen": false,      "connected_team_ids": [],      "internal_team_ids_count": 4,      "internal_team_ids_sample_team": "T013F30DBAB",      "pending_connected_team_ids": [],      "is_pending_ext_shared": false    },    {      "id": "C013JDPD6CR",      "name": "proj-decomposed-monolith",      "purpose": "",      "member_count": 1,      "created": 1588786531,      "creator_id": "WPQ65MVKK",      "is_private": false,      "is_archived": false,      "is_general": false,      "last_activity_ts": 1589854024000200,      "is_ext_shared": false,      "is_global_shared": false,      "is_org_default": false,      "is_org_mandatory": false,      "is_org_shared": true,      "is_frozen": false,      "connected_team_ids": [],      "internal_team_ids_count": 1,      "internal_team_ids_sample_team": "TPQ67R81F",      "pending_connected_team_ids": [],      "is_pending_ext_shared": false    }  ],  "next_cursor": "aWQ6Mw==",  "total_count": 14823}
```

The `member_count` field will return `-1` when the channel is archived. Counts of `0` and above indicate current membership.

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

`connected_team_passed_in_is_not_top_level_team`

One of the orgs provided in the external connected teams filter is not a top level team.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_team_not_connected_to_this_org`

One of the teams provided in the external connected teams filter is not connected to the org.

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

The token provided does not belong to an Enterprise organization, or a specified workspace wasn't part of this Enterprise.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_cursor`

The provided cursor is not valid, often due to not urlencoding query parameters.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_search_channel_type`

An invalid `search_channel_types` arg was passed. Make sure there are no spaces between your args and that each is one of the enumerated options listed above.

`invalid_sort`

The provided `sort` argument wasn't valid.

`invalid_sort_dir`

The provided `sort_dir` argument wasn't valid.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed`

The authenticated user does not have the permission to call this method.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

The token provided is not associated with an Org Admin or Owner.

`not_an_enterprise`

This endpoint can only be called by an Enterprise organization.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_found`

One of the workspaces provided in the list wasn't found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.