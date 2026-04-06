Source: https://docs.slack.dev/reference/methods/admin.apps.approved.list

# admin.apps.approved.list method

DocsCall generator

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Facts {#facts}

**Description**List approved apps for an org or workspace.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
GET https://slack.com/api/admin.apps.approved.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.apps.approved.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_apps_approved_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminAppsApprovedList
```

**Scopes**

User token:

[`admin.apps:read`](/reference/scopes/admin.apps.read)

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

**`limit`**`integer`Optional

The maximum number of items to return. Must be between 1 - 1000 both inclusive.

_Default:_ `100`

_Example:_ `100`

**`cursor`**`string`Optional

Set `cursor` to `next_cursor` returned by the previous call to list items in the next page

_Example:_ `5c3e53d5`

**`team_id`**Optional

_Example:_ `T0HFE6EBT`

**`enterprise_id`**Optional

_Example:_ `E0AS553RN`

**`certified`**`boolean`Optional

Limit the results to only include certified apps. When false, no certified apps will appear in the result

_Default:_ `false`

## Usage info {#usage-info}

Managing app approval

When used in an admin app to approve or restrict other app installs across an entire Enterprise organization, the UI-based process is disabled and the admin app solely manages apps.

This [App Management API](/admins/managing-app-approvals) method lists apps approved for installation for a workspace.

This method requires an `admin.*` scope. It's obtained through the normal [OAuth process](/authentication), but there are a few additional requirements. The scope must be requested by an Enterprise org admin or owner, and the OAuth install must take place on the entire Enterprise org, not an individual workspace. See the [`admin.apps:read`](/reference/scopes/admin.apps.read) method for more detailed instructions.

`enterprise_id` and `team_id` cannot be used together.

*   Passing `enterprise_id` will return the list of org-wide approved apps.
*   Passing `team_id` will return the apps approved for that specific workspace.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "approved_apps": [    {      "app": {        "id": "A0W7UKG8E",        "name": "My Test App",        "description": "test app",        "help_url": "https://www.slack.com",        "privacy_policy_url": "https://www.slack.com",        "app_homepage_url": "https://www.slack.com",        "app_directory_url": "https://myteam.enterprise.slack.com/apps/A0W7UKG8E-my-test-app",        "is_app_directory_approved": false,        "is_internal": false,        "developer_type": "third_party",        "socket_mode_enabled": false,        "icons": {          "image_32": "https://302674312496446w_2bd4ea1ad1f89a23c242_32.png",          "image_36": "https://302674312496446w_2bd4ea1ad1f89a23c242_36.png",          "image_48": "https://302674312496446w_2bd4ea1ad1f89a23c242_48.png",          "image_64": "https://302674312496446w_2bd4ea1ad1f89a23c242_64.png",          "image_72": "https://302674312496446w_2bd4ea1ad1f89a23c242_72.png",          "image_96": "https://302674312496446w_2bd4ea1ad1f89a23c242_96.png",          "image_128": "https://30267341249446w6_2bd4ea1ad1f89a23c242_128.png",          "image_192": "https://30267431249446w6_2bd4ea1ad1f89a23c242_192.png",          "image_512": "https://30267431249446w6_2bd4ea1ad1f89a23c242_512.png",          "image_1024": "https://3026743124446w96_2bd4ea1ad1f89a23c242_1024.png",          "image_original": "https://302674446w12496_2bd4ea1ad1f89a23c242_original.png"        },        "additional_info": ""      },      "scopes": [        {          "name": "bot",          "description": "Add the ability for people to direct message or mention @my_test_app",          "is_sensitive": true,          "token_type": "bot"        }      ],      "date_updated": 1574296707,      "last_resolved_by": {        "actor_id": "W0G82F4FD",        "actor_type": "user"      }    }  ],  "response_metadata": {    "next_cursor": ""  }}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
```

The `developer_type` in each app helpfully describes its origin.

*   `internal`: the app was developed as part of this Enterprise organization or workspace.
*   `third_party`: the app was developed by a third party, such as (but not limited to) those found in the Slack Marketplace.
*   `slack`: the app was built with love by Slack. Hello!

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

`app_management_app_not_installed_on_org`

The app management app must be installed on the org.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

Returned when the Admin APIs feature is not enabled for this team

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_actor`

The provided actor\_id is not a valid user or application

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

Value passed for `cursor` was not valid or is no longer valid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

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

`not_allowed`

The user is not allowed to access this API method

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

This method is only accessible by org/workspace owners and admins

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

User does not have permission to access method

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_found`

Returned when team id is not found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_teams_provided`

Please provide only `team_id` OR `enterprise_id`.

`two_factor_setup_required`

Two factor setup is required.