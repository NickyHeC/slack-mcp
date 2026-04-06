Source: https://docs.slack.dev/reference/methods/rtm.start

# rtm.start method

DocsCall generator

## Facts {#facts}

**Description**Deprecated: Starts a Real Time Messaging session. Use rtm.connect instead.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
GET https://slack.com/api/rtm.start
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.rtm.start
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.rtm_start
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().rtmStart
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 1: 1+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`simple_latest`**`boolean`Optional

Return timestamp only for latest message object of each channel (improves performance).

**`no_unreads`**`boolean`Optional

Skip unread counts for each channel (improves performance).

**`mpim_aware`**`boolean`Optional

Returns MPIMs to the client in the API response.

**`presence_sub`**`boolean`Optional

Only deliver presence events when requested by subscription. See [presence subscriptions](/apis/web-api/user-presence-and-status#subscriptions).

_Default:_ `true`

**`batch_presence_aware`**`boolean`Optional

Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/apis/web-api/user-presence-and-status#batching).

_Default:_ `false`

_Example:_ `1`

**`no_latest`**`boolean`Optional

Exclude latest timestamps for channels, groups, mpims, and ims. Automatically sets `no_unreads` to `1`

_Default:_ `0`

_Example:_ `1`

**`include_locale`**`boolean`Optional

Set this to `true` to receive the locale for users and channels. Defaults to `false`

## Usage info {#usage-info}

Deprecated

[Learn more about this method's deprecation.](/changelog/2021-10-rtm-start-to-stop)

This method began a Real Time Messaging API session and reserved your application a specific URL with which to connect via websocket.

It's user-centric and team-centric: your app connects _as_ a specific user or bot user on a specific team. Many apps will find the [Events API](/apis/events-api/)'s subscription model more scalable when working against multiple teams.

Please proactively [`rtm.connect`](/reference/methods/rtm.connect) instead. Existing apps still using `rtm.start` after September 27, 2022 now get the response from that method instead.

Consult the [RTM API documentation](/legacy/legacy-rtm-api) for full details on using the RTM API.

[New Slack apps](/quickstart) may not use any Real Time Messaging API method.

For most applications [Socket Mode](/apis/events-api/using-socket-mode) is a better way to communicate with Slack, anyway.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
```

See the [`rtm.connect`](/reference/methods/rtm.connect#response) method documentation for details on this method's response after September 27, 2022.

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

`rtm.start` is deprecated. Please use `rtm.connect` instead of `rtm.start`. Read https://docs.slack.dev/changelog/2021-10-rtm-start-to-stop for more info.

`method_deprecated`

The method has been deprecated.

`migration_in_progress`

Workspace is being migrated between servers. See [the `team_migration_started` event documentation](/reference/events/team_migration_started) for details.

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

`rtm_connect_required`

`rtm.start` is deprecated. Please use `rtm.connect` instead of `rtm.start`. Read https://docs.slack.dev/changelog/2021-10-rtm-start-to-stop for more info.

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