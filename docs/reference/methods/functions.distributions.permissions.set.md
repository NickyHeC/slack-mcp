Source: https://docs.slack.dev/reference/methods/functions.distributions.permissions.set

# functions.distributions.permissions.set method

DocsCall generator

## Facts {#facts}

**Description**Set the access type of a custom slack function and define the users, team or org ids to be granted access if permission\_type is set to named\_entities

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/functions.distributions.permissions.set
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.functions.distributions.permissions.set
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.functions_distributions_permissions_set
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().functionsDistributionsPermissionsSet
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`function_id`**`string`Optional

The encoded ID of the function

_Example:_ `Fn12345`

**`function_callback_id`**`string`Optional

The callback ID defined in the function's definition file

_Example:_ `my_function`

**`function_app_id`**`string`Optional

The encoded ID of the app

_Example:_ `A12345`

**`permission_type`**`string`Optional

The type of permission that defines how the function can be distributed

_Acceptable values:_ `everyone` `app_collaborators` `named_entities` `system`

**`user_ids`**`array`Optional

List of encoded user IDs

_Example:_ `U1234,U2345,U3456`

**`team_ids`**`array`Optional

List of team IDs to allow for named\_entities permission

_Example:_ `T00000001,T00000002,T00000003`

**`org_ids`**`array`Optional

List of org IDs to allow for named\_entities permission

_Example:_ `E00000001,E00000002,E00000003`

## Usage info {#usage-info}

Set the `permission_type` to define how your custom function can be [distributed](/tools/deno-slack-sdk/guides/controlling-access-to-custom-functions) for use in other workflows. Supply a list of user IDs to grant access to if distributing to a specific group of users.

Identify your function by supplying its callback ID and your app ID. The encoded ID of the function can also be used instead.

* * *

## Response {#response}

#### If successful, the command returns the permission type and if applicable, the list of users with access

```
{  "ok": true,  "permission_type": "app_collaborators",  "users": [    {      "user_id": "U01565LTEBD",      "username": "joe_smith",      "email": "joesmith@salesforce.com"    }  ]}
```

#### Typical error response when an invalid user ID is supplied in user_ids

```
{  "ok": false,  "error": "user_not_found"}
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

`app_not_found`

This app does not exist.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`function_not_found`

This function does not exist.

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

One or more of the named entities was not found

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

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`permission_type_required`

`permission_type` is a required input.

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

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

This method does not exist.

`user_not_found`

One or more of the named entities was not found.