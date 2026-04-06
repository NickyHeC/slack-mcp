Source: https://docs.slack.dev/reference/methods/admin.functions.list

# admin.functions.list method

DocsCall generator

## Facts {#facts}

**Description**Look up functions by a set of apps.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.functions.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.functions.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_functions_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminFunctionsList
```

**Scopes**

User token:

[`admin.workflows:read`](/reference/scopes/admin.workflows.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`app_ids`**`array`Required

Comma-separated array of app IDs to get functions for; max 50.

_Example:_ `A02,A1234`

### Optional arguments

**`team_id`**Optional

The team context to retrieve functions from.

_Example:_ `T00000001`

**`include_non_distributed_functions`**`boolean`Optional

Whether to also include functions that are not yet distributed to any users in the function count. This is needed for admins that are approving an app request and will only work if the team owns the app.

**`cursor`**`string`Optional

Set `cursor` to `next_cursor` returned by the previous call to list items in the next page.

_Example:_ `dXNlcjpVMDYxTkZUVDI=`

**`limit`**`integer`Optional

The number of results that will be returned by the API on each invocation. Must be between 1 and 1000, both inclusive.

_Default:_ `100`

_Example:_ `20`

## Usage info {#usage-info}

List all functions installed by a set of app IDs; returns an array of function objects.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "functions": [    {      "id": "123ABC456DE",      "callback_id": "sample_function",      "title": "Sample function",      "description": "A sample function.",      "type": "app",      "input_parameters": [        {          "type": "string",          "name": "message",          "description": "Message to be posted.",          "title": "Message",          "is_required": true        },        {          "type": "slack#/reference/objects/user-object_id",          "name": "user",          "description": "The user invoking the workflow.",          "title": "User",          "is_required": false        }      ],      "output_parameters": [        {          "type": "string",          "name": "updatedMsg",          "description": "Updated message to be posted.",          "title": "Updated Msg",          "is_required": true        }      ],      "app_id": "789FGH1011IJ",      "date_created": 1692283027,      "date_updated": 1692725035,      "date_deleted": 0    }  ],  "response_metadata": {    "next_cursor": "aWQ6MTE3MDk1NTIzNDAxOQ=="  }}
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

The user is not allowed to access this API method.

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

The user is not allowed to access this API method.

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