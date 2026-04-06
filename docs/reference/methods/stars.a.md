Source: https://docs.slack.dev/reference/methods/stars.add

# stars.add method

DocsCall generator

## Facts {#facts}

**Description**Save an item for later. Formerly known as adding a star.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/stars.add
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.stars.add
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.stars_add
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().starsAdd
```

**Scopes**

User token:

[`stars:write`](/reference/scopes/stars.write)

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

**`channel`**`string`Optional

Channel to add star to, or channel where the message to add star to was posted (used with `timestamp`).

**`file`**`string`Optional

File to add star to.

**`file_comment`**`string`Optional

File comment to add star to.

**`timestamp`**`string`Optional

Timestamp of the message to add star to.

## Usage info {#usage-info}

Stars can still be added via `stars.add` but they can no longer be viewed or interacted with by end-users.

Additionally, the [`star_added`](/reference/events/star_added) event is no longer emitted. We recommend retiring any app functionality that relies on `stars` APIs.

End-users can use the [new Later view](https://slack.com/help/articles/13453851074067-Save-it-for-Later), but Later APIs are not currently available.

See [this changelog](/changelog/2023-07-its-later-already-for-stars-and-reminders) for more information.

This method adds a star to an item (message, file, file comment, channel, private group, or DM) on behalf of the authenticated user. One of `file`, `file_comment`, `channel`, or the combination of `channel` and `timestamp` must be specified.

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

`already_starred`

The specified item has already been starred by the authenticated user.

`bad_timestamp`

Value passed for `timestamp` was invalid.

`channel_not_found`

Channel, private group, or DM specified by `channel` does not exist

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`external_channel_migrating`

Channel is undergoing active migration

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_comment_not_found`

File comment specified by `file_comment` does not exist.

`file_not_found`

File specified by `file` does not exist.

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

`message_not_found`

Message specified by `channel` and `timestamp` does not exist.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_item_specified`

`file`, `file_comment`, `channel` and `timestamp` was not specified.

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