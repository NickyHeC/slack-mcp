Source: https://docs.slack.dev/reference/methods/calls.add

# calls.add method

DocsCall generator

## Facts {#facts}

**Description**Registers a new Call.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/calls.add
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.calls.add
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.calls_add
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().callsAdd
```

**Scopes**

Bot token:

[`calls:write`](/reference/scopes/calls.write)

User token:

[`calls:write`](/reference/scopes/calls.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`external_unique_id`**`string`Required

An ID supplied by the 3rd-party Call provider. It must be unique across all Calls from that service.

_Example:_ `025169F6-E37A-4E62-BB54-7F93A0FC4C1F`

**`join_url`**`string`Required

The URL required for a client to join the Call.

_Example:_ `https://example.com/calls/1234567890`

### Optional arguments

**`external_display_id`**`string`Optional

An optional, human-readable ID supplied by the 3rd-party Call provider. If supplied, this ID will be displayed in the Call object.

_Example:_ `705-292-868`

**`desktop_app_join_url`**`string`Optional

When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.

_Example:_ `callapp://join/1234567890`

**`date_start`**`integer`Optional

Unix timestamp of the call start time

_Example:_ `1562002086`

**`title`**`string`Optional

The name of the Call.

_Example:_ `Kimpossible sync up`

**`created_by`**`string`Optional

The valid Slack user ID of the user who created this Call. When this method is called with a user token, the `created_by` field is optional and defaults to the authed user of the token. Otherwise, the field is required.

_Example:_ `U1H77`

**`users`**`array`Optional

The list of users to register as participants in the Call. [Read more on how to specify users here](/apis/web-api/using-the-calls-api#users).

_Example:_ `[{"slack_id": "U1H77"}, {"external_id": "54321678", "display_name": "External User", "avatar_url": "https://example.com/users/avatar1234.jpg"}]`

## Usage info {#usage-info}

This method is part of our [Calls API](/apis/web-api/using-the-calls-api).

For more information on how to specify `users`, read our [additional documentation in the usage guide](/apis/web-api/using-the-calls-api#users).

* * *

## Response {#response}

```
{	"ok": true,	"call": {		"id": "R0E69JAIF",		"date_start": 1562002086,		"external_unique_id": "025169F6-E37A-4E62-BB54-7F93A0FC4C1F",		"join_url": "https://example.com/calls/1234567890",		"desktop_app_join_url": "callapp://join/1234567890",		"external_display_id": "705-292-868",		"title": "Kimpossible sync up",		"users": [			{				"slack_id": "U0MQG83FD"			},			{				"external_id": "54321678",				"display_name": "Kim Possible",				"avatar_url": "https://callmebeepme.com/users/avatar1234.jpg"			}		]	}}
```

Note that the success response includes an `id` associated with the Call. This ID can be used to post the Call to a channel by using the [`chat.postMessage`](/reference/methods/chat.postMessage) method with the following block:

```
{	"blocks": [		{			"type": "call",			"call_id": "R0E69JAIF"		}	]}
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

An unexpected error has occurred while trying to register the Call.

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

`invalid_created_by`

The `created_by` user ID is invalid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_start_time`

The start time is invalid.

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

`not_authorized`

The specified user is not authorized to create a Call in this channel.

`not_implemented`

This method is not available.

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

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`user_not_found`

A specified user wasn't found.