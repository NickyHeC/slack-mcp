Source: https://docs.slack.dev/reference/methods/admin.workflows.triggers.types.permissions.set

# admin.workflows.triggers.types.permissions.set method

Set the permissions for using a trigger type.

DocsCall generator

## Facts {#facts}

**Description**Set the permissions for using a trigger type

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.workflows.triggers.types.permissions.set
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.workflows.triggers.types.permissions.set
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_workflows_triggers_types_permissions_set
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminWorkflowsTriggersTypesPermissionsSet
```

**Scopes**

User token:

[`client`](/reference/scopes/client)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`id`**Required

The trigger type ID for which to set the permissions

_Example:_ `['FTT01', 'FTT02', 'FTT03']`

### Optional arguments

**`visibility`**`string`Optional

The function visibility

_Acceptable values:_ `everyone` `named_entities` `no_one`

**`user_ids`**`array`Optional

List of user IDs to allow for named\_entities visibility

_Example:_ `['U00000001', 'U00000002', 'U00000003']`

**`permissions`**`object`Optional

## Usage Info {#usage-info}

The following arguments are always required:

*   `token` (string): Authentication token (session or cookie)
*   `id` (string): The trigger type ID for which to set the permissions
    *   Example: `['FTT01', 'FTT02', 'FTT03']`

### Permissions configuration {#permissions-configuration}

After providing the required arguments above, you must use either top-level visibility or a permissions array to configure permissions:

#### Top-Level visibility {#top-level-visibility}

Set permissions using the top-level `visibility` property:

**Public or no access**

When `visibility` is set to `"everyone"` or `"no_one"`, no additional properties are required.

**Example (everyone):**

```
{  "token": "session_token",  "id": "FTT01",  "visibility": "everyone"}
```

**Example (no one):**

```
{  "token": "session_token",  "id": "FTT01",  "visibility": "no_one"}
```

**Named entities**

When `visibility` is set to `"named_entities"`, you must provide at least one of the following:

*   `user_ids` (array): List of user IDs to allow access (max 50 items)
    *   Example: `['U00000001', 'U00000002', 'U00000003']`
*   `team_ids` (array): List of workspace IDs to allow access (max 50 items)
    *   Example: `['T00000001', 'T00000002', 'T00000003']`
*   `org_ids` (array): List of enterprise IDs to allow access
    *   Example: `['E00000001', 'E00000002', 'E00000003']`

**Example:**

```
{  "token": "session_token",  "id": "FTT01",  "visibility": "named_entities",  "user_ids": ["U00000001", "U00000002"],  "team_ids": ["T00000001"]}
```

#### Permissions array {#permissions-array}

Set multiple permission types using the `permissions` array. Each permission object in the array must specify:

*   `type` (string, required): The type of permission
    *   `"trigger_type"`
    *   `"private_channel_access"`
    *   `"private_channel_message_access"`
*   `visibility` (string, required): Who has access
    *   `"everyone"`, `"named_entities"`, or `"no_one"`

**Public or no access**

When `visibility` is `"everyone"` or `"no_one"`, no additional properties are required in the permission object.

**Example:**

```
{  "token": "session_token",  "id": "FTT01",  "permissions": [    {      "type": "trigger_type",      "visibility": "everyone"    },    {      "type": "private_channel_access",      "visibility": "no_one"    }  ]}
```

**Named entities**

When `visibility` is `"named_entities"`, you must provide at least one of the following within each permission object:

*   `user_ids` (array): List of user IDs (max 50 items)
*   `team_ids` (array): List of workspace IDs (max 50 items)
*   `org_ids` (array): List of enterprise IDs

**Example:**

```
{  "token": "session_token",  "id": "FTT01",  "permissions": [    {      "type": "trigger_type",      "visibility": "named_entities",      "user_ids": ["U00000001", "U00000002"]    },    {      "type": "private_channel_access",      "visibility": "named_entities",      "team_ids": ["T00000001"]    }  ]}
```

### Notes {#notes}

*   All ID arrays support `uniqueItems: true`, meaning duplicate values are not allowed.
*   The `user_ids` and `team_ids` properties have a maximum of 50 items.
*   You cannot mix both options - use either top-level visibility OR the permissions array, but not both.
*   When using the `named_entities` visibility, at least one ID array must be non-empty.

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

`invalid_named_entities`

Named entities visibility requires a valid set of named entities to be specified

`invalid_permission_set`

This permission set is invalid.

`invalid_permission_type`

This permission type is invalid.

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

`required_visibility`

Visibility is required on this resource.

`restricted_action`

This actor does not have access to the permissions on this resource.

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

The referenced trigger type ID does not exist.

`two_factor_setup_required`

Two factor setup is required.

`visibility_is_not_named_entities`

The visibility should be named entities when the user\_ids, team\_ids, or org\_ids args are set