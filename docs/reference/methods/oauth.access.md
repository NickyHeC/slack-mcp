Source: https://docs.slack.dev/reference/methods/oauth.access

# oauth.access method

DocsCall generator

## Facts {#facts}

**Description**Exchanges a temporary OAuth verifier code for an access token.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/oauth.access
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.oauth.access
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.oauth_access
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().oauthAccess
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 4: 100+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Optional arguments

**`client_id`**`string`Optional

Issued when you created your application. If possible, avoid sending `client_id` and `client_secret` as parameters in your request and instead supply the Client ID and Client Secret using the HTTP Basic authentication scheme.

_Example:_ `2141029472.691202649728`

**`client_secret`**`string`Optional

Issued when you created your application. If possible, avoid sending `client_id` and `client_secret` as parameters in your request and instead supply the Client ID and Client Secret using the HTTP Basic authentication scheme.

_Example:_ `e1b9e11dfcd19c1982d5de12921e17e8c`

**`code`**`string`Optional

The `code` param returned via the OAuth callback.

_Example:_ `4724469134.4644010092847.232b4e6d82c333b475fc30f5f5a341d294feb1a94392c2fd791f7ab7731a443d1a`

**`redirect_uri`**`string`Optional

This must match the originally submitted URI (if one was sent).

_Example:_ `http://example.com`

**`single_channel`**`boolean`Optional

Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://docs.slack.dev/changelog/2021-03-workspace-apps-to-retire-in-august-2021).

_Default:_ `false`

_Example:_ `true`

## Usage info {#usage-info}

This is a legacy method only used by classic apps.

Use [oauth.v2.access](/reference/methods/oauth.v2.access) for [granular permissions Slack apps](/app-management/quickstart-app-settings)

This method allows you to exchange a temporary OAuth `code` for an API access token.

This is the third step of the [OAuth authentication flow](/authentication).

We strongly recommend supplying the Client ID and Client Secret using the HTTP Basic authentication scheme, as discussed [in RFC 6749](https://tools.ietf.org/html/rfc6749#section-2.3.1).

If at all possible, avoid sending `client_id` and `client_secret` as parameters in your request.

**Keep your tokens secure**. Do not share tokens with users or anyone else.

When used with a legacy workspace app, this method's response differs significantly.

A potential gotcha: while `redirect_uri` is optional, it is _required_ if your app passed it as a parameter to `oauth/authorization` in the first step of the OAuth flow.

* * *

## Response {#response}

#### Successful user token negotiation for a single scope

```
{  "access_token": "xoxp-XXXXXXXX-XXXXXXXX-XXXXX",  "scope": "groups:write",  "team_name": "Wyld Stallyns LLC",  "team_id": "TXXXXXXXXX",  "enterprise_id": null}
```

#### Success example when asking for multiple scopes, a bot user token, and an incoming webhook

```
{  "access_token": "xoxp-XXXXXXXX-XXXXXXXX-XXXXX",  "scope": "incoming-webhook,commands,bot",  "team_name": "Team Installing Your Hook",  "team_id": "TXXXXXXXXX",  "enterprise_id": null,  "incoming_webhook": {    "url": "https://hooks.slack.com/TXXXXX/BXXXXX/XXXXXXXXXX",    "channel": "#channel-it-will-post-to",    "configuration_url": "https://teamname.slack.com/services/BXXXXX"  },  "bot": {    "bot_user_id": "UTTTTTTTTTTR",    "bot_access_token": "xoxb-XXXXXXXXXXXX-TTTTTTTTTTTTTT"  }}
```

#### Success example using a workspace app produces a very different kind of response

```
{  "ok": true,  "access_token": "xoxa-access-token-string",  "token_type": "app",  "app_id": "A012345678",  "app_user_id": "U0NKHRW57",  "team_name": "Subarachnoid Workspace",  "team_id": "T061EG9R6",  "enterprise_id": null,  "authorizing_user": {    "user_id": "U061F7AUR",    "app_home": "D0PNCRP9N"  },  "installer_user": {    "user_id": "U061F7AUR",    "app_home": "D0PNCRP9N"  },  "scopes": {    "app_home": [      "chat:write",      "im:history",      "im:read"    ],    "team": [],    "channel": [      "channels:history",      "channels:read",      "chat:write"    ],    "group": [      "chat:write"    ],    "mpim": [      "chat:write"    ],    "im": [      "chat:write"    ],    "user": []  }}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_client_id"}
```

The response schema for this step of OAuth differs depending on [the scopes](/reference/scopes) requested and the type of application used. When asking for the `bot` scope, you'll receive the token separately from the user token.

`enterprise_id` will be populated if the installing team is part of an enterprise. Otherwise, it will be `null`.

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

Value passed for `client_secret` was invalid.

`bad_redirect_uri`

Value passed for `redirect_uri` did not match the `redirect_uri` in the original request.

`code_already_used`

Value passed for `code` was already exchanged.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

Something went wrong during app installation.

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

Value passed for `client_id` was invalid.

`invalid_code`

Value passed for `code` was invalid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_token`

Invalid refresh token.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_resource`

Missing permission resource.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`oauth_authorization_url_mismatch`

The OAuth flow was initiated on an incorrect version of the authorization url. The flow must be initiated via /oauth/authorize.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

Too many requests made in succession.

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

`user_email_unverified`

The users email is unverified