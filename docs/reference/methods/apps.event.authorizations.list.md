Source: https://docs.slack.dev/reference/methods/apps.event.authorizations.list

# apps.event.authorizations.list method

DocsCall generator

## Facts {#facts}

**Description**Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/apps.event.authorizations.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.apps.event.authorizations.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.apps_event_authorizations_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().appsEventAuthorizationsList
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Special rate limits apply.](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`event_context`**`string`Required

### Optional arguments

**`cursor`**`string`Optional

**`limit`**`integer`Optional

## Usage info {#usage-info}

This method returns a list of authorizations for the given event specified by `event_context`. Each authorization represents an app installation that the event is visible to.

### How do I find an event_context to call this method with? {#context}

You'll receive an `event_context` identifying an event in each [event payload](/apis/events-api/#begin) sent to your app. However, [not all events contain an `event_context`](/changelog/2020-09-15-events-api-truncate-authed-users#full_list).

### What do authorizations signify? {#meaning}

Authorizations are **installations of your app**. If your app has been installed multiple times, you'll probably have multiple authorizations for some events.

### When should I call this method? {#when}

Call this method to see all the installations of your app than an event is visible to. Sometimes, only certain installations have permission to know about an event.

### How do I get permission to call this method {#how}

Calling this method is just like any other [Web API](/apis/web-api/) method. However, since this method lists **multiple installations** of your app, you'll need an [app-level token](/authentication/tokens#app).

You'll obtain the app-level token by going to your [app settings](https://api.slack.com/apps) and scrolling down to the App-Level Tokens section on the **Basic Information** page. CLick `Generate Token and Scopes` to get the token. You'll also request the [`authorizations:read`](/reference/scopes/authorizations.read) scope.

For this method, you will need to pass this token in the HTTP `Authorization` header of your request; passing it as a POST parameter will result in an error.

### What are the rate limiting conditions for this method? {#rate-limits}

Rate limiting conditions for this method include a default rate limit that is sufficient for most apps, with custom overrides determined on a per-team basis. The default limit is 600 requests per minute (per app per team).

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "authorizations": [    {      "enterprise_id": "string",      "team_id": "string",      "user_id": "string",      "is_bot": "string"    },    {      "enterprise_id": "string2",      "team_id": "string2",      "user_id": "string2",      "is_bot": "string2"    }  ]}
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

`auth_mismatch`

The given authorization token is not associated with the app that sent this event.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

An unexpected error occurred while finding authorizations for this event.

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

The `cursor` argument was invalid.

`invalid_event_context`

The given `event_context` didn't match an event.

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