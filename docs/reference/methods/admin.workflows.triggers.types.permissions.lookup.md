Source: https://docs.slack.dev/reference/methods/admin.workflows.triggers.types.permissions.lookup

# admin.workflows.triggers.types.permissions.lookup method

This API method lists the permissions for using each trigger type. The response structure varies based on a toggle.

DocsCall generator

## Facts {#facts}

**Description**List the permissions for using each trigger type.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.workflows.triggers.types.permissions.lookup
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.workflows.triggers.types.permissions.lookup
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_workflows_triggers_types_permissions_lookup
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminWorkflowsTriggersTypesPermissionsLookup
```

**Scopes**

User token:

[`client`](/reference/scopes/client)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`trigger_type_ids`**`array`Required

The trigger type IDs for which to get the permissions.

_Example:_ `['FTT01', 'FTT02', 'FTT03']`

## Usage info {#usage-info}

The `output.properties.permissions` structure returns different property sets depending on the toggle state:

### Toggle OFF (default legacy behavior) {#toggle-off-default-legacy-behavior}

When the toggle is **OFF**, each trigger type object contains:

*   `permission` (required): String enum of `"everyone"`, `"named_entities"`, or `"no_one"`
*   `user_ids` (conditional): Array of user IDs
*   `team_ids` (conditional): Array of team/workspace IDs
*   `org_ids` (conditional): Array of enterprise IDs

**Validation Rule**: If `permission` is set to `"named_entities"`, then at least one of `user_ids`, `team_ids`, or `org_ids` must be present and non-empty.

**Example Response**:

```
{  "permissions": {    "Ftt01": {      "permission": "named_entities",      "user_ids": ["U00000001", "U00000002"],      "team_ids": ["T00000001"]    }  },  "metadata": { ... }}
```

### Toggle ON (granular permissions) {#toggle-on-granular-permissions}

When the toggle is **ON**, each trigger type object contains:

*   `permissions` (required): Array of permission objects

Each permission object in the array contains:

*   `type` (required): String enum specifying the permission type:
    *   `"trigger_type"`: Trigger access permission
    *   `"private_channel_access"`: Access to private channels
    *   `"private_channel_message_access"`: Access to text from messages in private channels
*   `permission` (required): String enum of `"everyone"`, `"named_entities"`, or `"no_one"`
*   `user_ids` (conditional): Array of user IDs
*   `team_ids` (conditional): Array of team/workspace IDs
*   `org_ids` (conditional): Array of enterprise IDs

**Validation Rule**: If `permission` is set to `"named_entities"` within any array item, then at least one of `user_ids`, `team_ids`, or `org_ids` must be present and non-empty for that item.

**Example Response**:

```
{  "permissions": {    "Ftt01": {      "permissions": [        {          "type": "trigger_type",          "permission": "everyone"        },        {          "type": "private_channel_access",          "permission": "named_entities",          "team_ids": ["T00000001"]        },        {          "type": "private_channel_message_access",          "permission": "no_one"        }      ]    }  },  "metadata": { ... }}
```

## Notes {#notes}

*   The toggle controls which response structure is returned.
*   Check for the presence of the `permissions` array to determine which format is being used.
*   The toggle ON format provides more granular control over different permission types.
*   Both formats maintain the same validation logic for `named_entities` requiring at least one entity ID list.

* * *

## Response {#response}

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

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

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

This actor does not have access to view the permissions on this resource

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

`trigger_type_id_not_found`

The given trigger type ID(s) do not map to valid trigger types

`two_factor_setup_required`

Two factor setup is required.