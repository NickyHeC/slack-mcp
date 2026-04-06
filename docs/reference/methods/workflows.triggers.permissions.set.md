Source: https://docs.slack.dev/reference/methods/workflows.triggers.permissions.set

# workflows.triggers.permissions.set method

DocsCall generator

## Facts {#facts}

**Description**Set the permission type for who can run a trigger

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/workflows.triggers.permissions.set
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.workflows.triggers.permissions.set
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.workflows_triggers_permissions_set
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().workflowsTriggersPermissionsSet
```

**Scopes**

Bot token:

[`triggers:write`](/reference/scopes/triggers.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`trigger_id`**`string`Required

Encoded ID of the trigger

_Example:_ `Ft0000000001`

**`permission_type`**`string`Required

The type of permission that defines who can run a trigger

_Acceptable values:_ `everyone` `app_collaborators` `named_entities`

### Optional arguments

**`user_ids`**`array`Optional

List of encoded user IDs

_Example:_ `U0000000001,U0000000002`

**`channel_ids`**`array`Optional

List of encoded channel IDs

_Example:_ `C0000000001,C0000000002`

**`team_ids`**`array`Optional

List of encoded workspace IDs

_Example:_ `T0000000001,T0000000002`

**`org_ids`**`array`Optional

List of encoded organization IDs

_Example:_ `E00000001,E00000002`

## Usage info {#usage-info}

Grant users permission to run your workflow via the [trigger](/tools/deno-slack-sdk/guides/creating-link-triggers) identified by `trigger_id`. You can specify individual encoded user IDs or grant access to everyone in a particular channel, workspace or org.

### Required scopes {#required-scopes}

This method is used for [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/) and authorization should be done using the [CLI](/tools/slack-cli/guides/authorizing-the-slack-cli). The required user token scope listed above cannot be added in the [app settings](https://api.slack.com/apps).

* * *

## Response {#response}

#### If successful, the command returns the trigger's permission type and if applicable, the list of entities with access

```
{  "ok": true,  "permission_type": "named_entities",  "user_ids": [    "U01565LTEBD"  ]}
```

#### Typical error response when permission_type is set to named_entities` but no entities are provided

```
{  "ok": false,  "error": "named_entities_cannot_be_empty"}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

This actor does not have access to the permissions on this resource.

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`channel_not_found`

One or more of the listed channels could not be found.

`connected_org_denied`

The workspace admin does not allow connected organizations to be named\_entities.

`connected_team_denied`

The workspace admin does not allow connected teams to be named\_entities.

`connected_user_denied`

The workspace admin does not allow connected users to be named\_entities.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_workspace_denied`

The channel selected is not on the workflow team.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

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

`invalid_permission_type`

This function requires permission\_type to be set as named\_entities before adding users.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`named_entities_cannot_be_empty`

Must pass at least one valid named entity.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`no_valid_named_entities`

None of the provided named entities were valid

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`org_not_connected`

One of more of the listed organizations were not connected.

`org_not_found`

One or more of the listed organizations could not be found.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`shared_channel_denied`

The workspace admin does not allow shared channels to be named\_entities.

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_not_connected`

One of more of the listed teams were not connected by org.

`team_not_found`

One or more of the listed teams could not be found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_named_entities`

Too many named\_entities passed into the trigger permissions setting.

`trigger_not_found`

This trigger does not exist.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

This method does not exist.

`user_not_found`

One or more of the listed users could not be found.