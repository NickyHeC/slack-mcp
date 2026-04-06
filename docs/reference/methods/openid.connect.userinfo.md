Source: https://docs.slack.dev/reference/methods/openid.connect.userInfo

# openid.connect.userInfo method

DocsCall generator

## Facts {#facts}

**Description**Get the identity of a user who has authorized Sign in with Slack.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/openid.connect.userInfo
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.openid.connect.userInfo
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.openid_connect_userInfo
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().openidConnectUserInfo
```

**Scopes**

User token:

[`openid`](/reference/scopes/openid)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

## Usage info {#usage-info}

This special method is part of implementing [Sign in with Slack](/authentication/sign-in-with-slack/).

As part of [Sign in with Slack](/authentication/sign-in-with-slack/), this method allows your app to receive information about a user who signs into your service with their Slack profile.

* * *

## Response {#response}

#### Successful user info request during the Sign in with Slack flow

```
{  "ok": true,  "sub": "U0R7JM",  "https://slack.com/user_id": "U0R7JM",  "https://slack.com/team_id": "T0R7GR",  "email": "krane@slack-corp.com",  "email_verified": true,  "date_email_verified": 1622128723,  "name": "krane",  "picture": "https://secure.gravatar.com/....png",  "given_name": "Bront",  "family_name": "Labradoodle",  "locale": "en-US",  "https://slack.com/team_name": "kraneflannel",  "https://slack.com/team_domain": "kraneflannel",  "https://slack.com/user_image_24": "...",  "https://slack.com/user_image_32": "...",  "https://slack.com/user_image_48": "...",  "https://slack.com/user_image_72": "...",  "https://slack.com/user_image_192": "...",  "https://slack.com/user_image_512": "...",  "https://slack.com/team_image_34": "...",  "https://slack.com/team_image_44": "...",  "https://slack.com/team_image_68": "...",  "https://slack.com/team_image_88": "...",  "https://slack.com/team_image_102": "...",  "https://slack.com/team_image_132": "...",  "https://slack.com/team_image_230": "...",  "https://slack.com/team_image_default": true}
```

This method retrieves user info for a user who has previously authenticated to your service with [Sign in with Slack](/authentication/sign-in-with-slack/).

Some of the fields in the response to this method are preceded with `https://slack.com/`—these fields are Slack-specific, and they're from the perspective of Slack. For example, `https://slack.com/user_id` indicates the user's ID on Slack, not on your service.

`team_image_default` indicates whether the image is a default one (`true`), or someone uploaded their own (`false`).

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