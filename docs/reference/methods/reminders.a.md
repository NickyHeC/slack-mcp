Source: https://docs.slack.dev/reference/methods/reminders.add

# reminders.add method

DocsCall generator

## Facts {#facts}

**Description**Creates a reminder.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/reminders.add
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.reminders.add
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.reminders_add
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().remindersAdd
```

**Scopes**

User token:

[`reminders:write`](/reference/scopes/reminders.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`text`**`string`Required

The content of the reminder

_Example:_ `eat a banana`

**`time`**`string`Required

Can also take a type of integer. When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. "in 15 minutes," or "every Thursday")

_Example:_ `1602288000`

### Optional arguments

**`user`**`string`Optional

No longer supported - reminders cannot be set for other users. Previously, was the user who would receive the reminder.

_Example:_ `U18888888`

**`team_id`**`string`Optional

Encoded team id, required if org token is used

**`recurrence`**`object`Optional

Specify the repeating behavior of a reminder. Available options: `daily`, `weekly`, `monthly`, or `yearly`. If `weekly`, may further specify the days of the week.

_Example:_ `{ "frequency": "weekly", "weekdays": ["monday", "wednesday", "friday"] }`

## Usage info {#usage-info}

Retirement of API methods for interfacing with reminders began March 2023, and as such have become degraded or useless.

See [this changelog](/changelog/2023-07-its-later-already-for-stars-and-reminders) for more information.

This method creates a reminder.

Setting reminders for other users with `reminders.add` can now only be done with a bot token. As an alternative, you can use apps created with the [Deno Slack SDK](/tools/deno-slack-sdk/) to add reminders via [scheduled triggers](/tools/deno-slack-sdk/guides/creating-scheduled-triggers).

* * *

## Response {#response}

#### Only non-recurring reminders will have time and complete_ts fields.

```
{  "ok": true,  "reminder": {    "id": "Rm12345678",    "creator": "U123ABC456",    "user": "U123ABC456",    "text": "eat a banana",    "recurring": false,    "time": 1602288000,    "complete_ts": 0  }}
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

`cannot_add_bot`

Reminders can't be sent to bots.

`cannot_add_others`

Guests can't set reminders for other team members.

`cannot_add_others_recurring`

Recurring reminders can't be set for other team members.

`cannot_add_profile_only_user`

Reminders can't be sent to profile only users.

`cannot_add_slackbot`

Reminders can't be sent to Slackbot.

`cannot_parse`

The phrasing of the timing for this reminder is unclear. You must include a complete time description. Some examples that work: `1458678068`, `20`, `in 5 minutes`, `tomorrow`, `at 3:30pm`, `on Tuesday`, or `next week`.

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

`missing_argument`

An argument is missing.

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

That user can't be found.