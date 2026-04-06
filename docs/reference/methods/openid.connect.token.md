Source: https://docs.slack.dev/reference/methods/openid.connect.token

# openid.connect.token method

DocsCall generator

## Facts {#facts}

**Description**Exchanges a temporary OAuth verifier code for an access token for Sign in with Slack.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/openid.connect.token
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.openid.connect.token
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.openid_connect_token
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().openidConnectToken
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 4: 100+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Optional arguments

**`client_id`**`string`Optional

Issued when you created your application.

_Example:_ `2141029472.691202649728`

**`client_secret`**`string`Optional

Issued when you created your application.

_Example:_ `e1b9e11dfcd19c1982d5de12921e17e8c`

**`code`**`string`Optional

The `code` param returned via the OAuth callback.

_Example:_ `4724469134.4644010092847.232b4e6d82c333b475fc30f5f5a341d294feb1a94392c2fd791f7ab7731a443d1a`

**`redirect_uri`**`string`Optional

This must match the originally submitted URI (if one was sent).

_Example:_ `http://example.com`

**`grant_type`**`string`Optional

The `grant_type` param as described in the OAuth spec.

_Acceptable values:_ `authorization_code` `refresh_token`

_Example:_ `authorization_code`

**`refresh_token`**`string`Optional

The `refresh_token` param as described in the OAuth spec.

_Example:_ `xoxe-1-abcdefg`

## Usage info {#usage-info}

This special method is part of implementing [Sign in with Slack](/authentication/sign-in-with-slack/).

As part of [Sign in with Slack](/authentication/sign-in-with-slack/), this method allows your app to receive information about a user who signs into your service with their Slack profile.

A potential gotcha: while `redirect_uri` is optional, it is _required_ if your app passed it as a parameter to `/openid/connect/authorize` in the first step of the Sign in with Slack flow.

* * *

## Response {#response}

#### Successful token request during the Sign in with Slack flow

```
{  "ok": true,  "access_token": "xoxp-1234",  "token_type": "Bearer",  "id_token": "eyJhbGcMjY5OTA2MzcWNrLmNvbVwvdGVhbV9p..."}
```

The `id_token` in the response is a [standard](https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse) JSON Web Token (JWT). . When it's decoded, you'll see a payload like:

```
  "iss": "https://slack.com",  "sub": "U0R7MFMJM",  "aud": "25259531569.11152291",  "exp": 1626874955,  "iat": 1626874655,  "auth_time": 1626874655,  "nonce": "abcd",  "at_hash": "tUbyWGBHe0V32FJEupkgVQ",  "https://slack.com/team_id": "T0RR",  "https://slack.com/user_id": "U0JM",  "email": "bront@slack-corp.com",  "email_verified": true,  "date_email_verified": 1622128723,  "locale": "en-US",  "name": "brent",  "given_name": "",  "family_name": "",  "https://slack.com/user_image_24": "https://secure.gravatar.com/avatar/bc.png",  "https://slack.com/user_image_32": "...",  "https://slack.com/user_image_48": "...",  "https://slack.com/user_image_72": "...",  "https://slack.com/user_image_192": "...",  "https://slack.com/user_image_512": "...",  "https://slack.com/team_image_34": "...",  "https://slack.com/team_image_44": "...",  "https://slack.com/team_image_68": "...",  "https://slack.com/team_image_88": "...",  "https://slack.com/team_image_102": "...",  "https://slack.com/team_image_132": "...",  "https://slack.com/team_image_230": "...",  "https://slack.com/team_image_default": true
```

`iss`, `sub`, `aud`, `exp`, `iat`, `auth_time`, `nonce`, and `at_hash` are each defined by the [OpenID standard](https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse), but here's an overview:

*   `iss` signifies the issuer of the token.
*   `sub` signifies the subject of the token.
*   `aud` signifies the intended audience of the token, the client ID of the OpenID Relying Party.
*   `exp` signifies the expiration time of the request, meaning that it shouldn't be trusted if it's not received by the expiration time.
*   `iat` signifies the time when the token was issued.
*   `auth_time` signifies the time when the end-user authenticated.
*   `nonce` is a state variable that you pass to the `/openid/connect/authorize` endpoint at the beginning of Sign in with Slack, and that Slack then returns to you at the end of the flow here. Verify that it matches the `nonce` you passed to `/authorize`.

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

`bad_client_secret`

The value passed for `client_secret` was invalid.

`bad_redirect_uri`

The value passed for `redirect_uri` did not match the `redirect_uri` in the original request.

`cannot_install_an_org_installed_app`

An org-installed app cannot be installed on a workspace.

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

`invalid_client_id`

The value passed for `client_id` was invalid.

`invalid_code`

The value passed for `code` was invalid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_grant_type`

The value passed for `grant_type` was invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_refresh_token`

The given refresh token is invalid.

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

`oauth_authorization_url_mismatch`

The OAuth flow was initiated on an incorrect version of the authorization URL. The flow must be initiated via /openid/connect/authorize .

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`preview_feature_not_available`

The API method is not yet available on the team.

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