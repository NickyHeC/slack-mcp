Source: https://docs.slack.dev/reference/methods/admin.usergroups.addTeams

# admin.usergroups.addTeams method

DocsCall generator

## Facts {#facts}

**Description**Associate one or more default workspaces with an organization-wide IDP group.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.usergroups.addTeams
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.usergroups.addTeams
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_usergroups_addTeams
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminUsergroupsAddTeams
```

**Scopes**

User token:

[`admin.teams:write`](/reference/scopes/admin.teams.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`usergroup_id`**`string`Required

An encoded usergroup (IDP Group) ID.

_Example:_ `S12345678`

**`team_ids`**`array`Required

A comma separated list of encoded team (workspace) IDs. Each workspace _MUST_ belong to the organization associated with the token.

_Example:_ `T12345678,T98765432`

### Optional arguments

**`auto_provision`**`boolean`Optional

When `true`, this method automatically creates new workspace accounts for the IDP group members.

_Default:_ `false`

_Example:_ `true`

## Usage info {#usage-info}

Use this method to add workspaces to an organization-wide [IDP Group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-organization). When you link workspaces to an IDP group, you automatically add members of the IDP group to those workspaces.

This method is only available to Enterprise organizations, and only applies to IDP groups (user groups) across the organization.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

If an error occurs on one or more workspaces, an `errors` element will be populated with a list of `team_ID`s that were _not_ successfully linked to the IDP group:

```
    {        "ok": false,        "error": "auto_provision_failure",        "errors": [            "T12345678",            "T98765432"        ]    }
```

Note that some workspaces may successfully be added while others fail:

```
    {        "ok": false,        "error": "auto_provision_failure",        "errors": [            "T98765432"        ]    }
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

`auto_provision_failure`

A failure occurred while assigning IDP group members to a specific workspace; see `errors` element for a list of failed team IDs.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

An unexpected error occurred.

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

`invalid_team_ids`

One or more team IDs provided were invalid; see the `errors` field in the response for the list of invalid team IDs.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`no_team_ids_given`

The `team_ids` parameter was empty.

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

The calling user cannot update the specified usergroup.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_limit_exceeded`

The number of teams associated with the org group would exceed the limit.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`usergroup_not_found`

`usergroup_id` wasn't found.