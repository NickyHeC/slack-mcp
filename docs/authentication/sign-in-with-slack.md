Source: https://docs.slack.dev/authentication/sign-in-with-slack

# Using Sign in with Slack

Sign in with Slack helps users log into your service using their Slack profile.

The Sign in with Slack flow will redirect users to the right Slack URL. Slack will send users back to your service, along with the information your service needs.

The flow is based on the [OpenID Connect standard](https://openid.net/specs/openid-connect-core-1_0.html), built on top of [OAuth 2.0](/authentication/installing-with-oauth). The modern Sign in with Slack flow works with any package that successfully implements this standard. OpenID maintains a list of [certified implementations of the OpenID Connect standard](https://openid.net/developers/certified/). We recommend you make use of one of these packages to take care of the boilerplate surrounding OAuth.

If you already have an existing Sign in with Slack app that uses `identity.*` scopes, you can find [legacy Sign in with Slack documentation here](/legacy/legacy-authentication/legacy-sign-in-with-slack).

Check out [Sign in with Slack links](/authentication/sign-in-with-slack/setting-up-sign-in-with-slack-links), which allows users to share their Slack profile with you when they click a link from your service.

* * *

## Getting started {#implementation}

Implementation of the Sign in with Slack flow follows the flow of [our OAuth V2 process](/authentication/installing-with-oauth). If you're not familiar with that, you'll want to review these steps.

The key differences between **Sign in with Slack** and a typical OAuth flow for a Slack app are as follows:

*   You redirect users to a special OpenID endpoint, `/openid/connect/authorize`, rather than `/oauth/v2/authorize`.
*   You request the OpenID scopes—[`openid`](/reference/scopes/openid), [`email`](/reference/scopes/email), and [`profile`](/reference/scopes/profile). (With legacy Sign in with Slack, you requested legacy `identity.*` scopes.)
*   You exchange your access code for an access token using an OpenID method, [`/openid.connect.token`](/reference/methods/openid.connect.token), rather than `oauth.v2.access`.
*   You receive the [standard OpenID response](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest) sent to your redirect URI with the expected fields encoded in the `id_token`.
*   You use the [`openid.connect.userInfo`](/reference/methods/openid.connect.userInfo) method to retrieve updated user information. (With legacy Sign in with Slack, you used [`users.identity`](/reference/methods/users.identity).)

We'll step through the flow in more detail below.

### App setup {#setup}

First, create a Slack app:

[Create an app](https://api.slack.com/apps?new_app=1)

Enter your **App Name** and select the Development Workspace where you'll play around and build your app. Don't fuss too much over either field—no matter what workspace you select, you'll still be able to [distribute your app](/app-management/distribution) to other workspaces if you choose.

Navigate to the **OAuth & Permissions** section and configure a **Redirect URL** to match your service. The Redirect URL signifies where Slack should redirect users when they complete the OAuth flow. If you're using `ngrok`, use the ngrok public forwarding host as the root.

### Discover information on Slack OpenID endpoints {#discover}

Slack provides a discovery endpoint so that your OpenID Connect Relying Party can discover which endpoints to call. Our Well Known endpoint is accessible at:

```
https://slack.com/.well-known/openid-configuration
```

The response follows the [OpenID standard](https://openid.net/specs/openid-connect-discovery-1_0.html), as in the following example:

```
{    "issuer": "https://slack.com",    "authorization_endpoint": "https://slack.com/openid/connect/authorize",    "token_endpoint": "https://slack.com/api/openid.connect.token",    "userinfo_endpoint": "https://slack.com/api/openid.connect.userInfo",    "jwks_uri": "https://slack.com/openid/connect/keys",    "scopes_supported": ["openid","profile","email"],    "response_types_supported": ["code"],    "response_modes_supported": ["form_post"],    "grant_types_supported": ["authorization_code"],    "subject_types_supported": ["public"],    "id_token_signing_alg_values_supported": ["RS256"],    "claims_supported": ["sub","auth_time","iss"],    "claims_parameter_supported": false,    "request_parameter_supported": false,    "request_uri_parameter_supported": true,    "token_endpoint_auth_methods_supported": ["client_secret_post","client_secret_basic"]}
```

### Request with scopes {#request}

Send users into the Sign in with Slack authorization flow with a button or other redirect. If you're unsure of what that should look like, check out our [design guidelines](#design) for tips on how to make the experience as pleasant as possible for your users.

A scope conflict occurs when attempting to combine Sign in with Slack user scopes with non-Sign in with Slack scopes in the same OAuth flow

Each set of scopes must be requested in separate OAuth flows.

You should redirect users to the following URL:

```
https://slack.com/openid/connect/authorize
```

Your request should have the [standard OpenID Connect form](https://openid.net/specs/openid-connect-core-1_0.html#AuthorizationEndpoint), which is why it pays to use a pre-implemented package.

Here's an example:

```
  GET /openid/connect/authorize?    response_type=code    &scope=openid%20profile%20email    &client_id=s6BhdRkqt3    &state=af0ifjsldkj    &team=T1234    &nonce=abcd    &redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb HTTP/1.1  Host: https://slack.com
```

Here's a quick explanation of the parameters:

Parameter

Description

`response_type`

Set equal to `code`. This indicates you're asking for a temporary access code to then exchange for an access token.

`scope`

Which permissions you want the user to grant you. Your app will request `openid`, the base scope you always need to request in any Sign in with Slack flow. You may request `email` and `profile` as well.

`client_id`

Your app's client ID. You can find it in your [app settings](https://api.slack.com/apps) under **Basic Information**.

`state`

Used to avoid forgery attacks. Pass in a value that's unique to the user you're authenticating, and check it when you receive a temporary authorization code.

`nonce`

Used to verify that the entire flow has completed with no forgery. You can verify the `nonce` in the [response](#response) you receive from the final token exchange to ensure it's the same as what you pass here.

`redirect_uri`

Where Slack will send the user, along with the temporary authorization code, once the user okays your app. You can specify a more _specific_ `redirect_uri` than the one in your [app settings](https://api.slack.com/apps) here, but it must be either an exact match or a subdirectory of one of the redirect URLs in your app settings.

`team`

The workspace the user is intending to authenticate. If that workspace has been previously authenticated, the user will be signed in directly, bypassing the consent screen.

### Exchange {#exchange}

After the user successfully grants your app permission to access their Slack profile, they'll be redirected back to your service along with the typical `code` that signifies a temporary access code. Exchange that `code` for a real access token using the [`/openid.connect.token`](/reference/methods/openid.connect.token) method.

You can check that method's documentation for a full list of parameters to pass. As an overview, you'll pass:

*   `code`
*   your app's `client_secret`
*   your app's `client_id`
*   your app's `redirect_uri`

### Response {#response}

After calling the [`openid.connect.token`](/reference/methods/openid.connect.token) method, you'll receive a standard OpenID response:

```
{  "ok": true,  "access_token": "xoxp-...-...-...-123",  "token_type": "Bearer",  "id_token": "123abc...456"}
```

The `id_token` parameter is a [standard](https://openid.net/specs/openid-connect-core-1_0.html#TokenResponse) JSON Web Token (JWT). You can decode it with off-the-shelf libraries in any programming language, and most packages that handle OpenID will handle JWT decoding.

If you've requested the `openid` `email`. and `profile` scopes, the token response decodes into an object as in the following example:

```
{  "iss": "https://slack.com",  "sub": "U123ABC456",  "aud": "25259531569.1115258246291",  "exp": 1626874955,  "iat": 1626874655,  "auth_time": 1626874655,  "nonce": "abcd",  "at_hash": "abc...123",  "https://slack.com/team_id": "T0123ABC456",  "https://slack.com/user_id": "U123ABC456",  "email": "alice@example.com",  "email_verified": true,  "date_email_verified": 1622128723,  "locale": "en-US",  "name": "Alice",  "given_name": "",  "family_name": "",  "https://slack.com/team_image_230": "https://secure.gravatar.com/avatar/bc.png",  "https://slack.com/team_image_default": true}
```

Some additional fields may be included in the payload. Make sure to verify that the `nonce` returned in the JWT payload is the same as the `nonce` you supplied to [`authorize`](#request).

Your Sign in with Slack flow has officially completed. Now you can [obtain updated user info whenever you want for that authenticated user](#user_info).

### Get updated user info {#user_info}

Once you've obtained a user access token from the Sign in with Slack flow, you can use the [`openid.connect.userInfo`](/reference/methods/openid.connect.userInfo) method to get updated user information, such as their profile image and team image. Read up on that documentation for more details on the exact response to expect.

### Token rotation {#rotation}

[Token rotation](/authentication/using-token-rotation) is supported with Sign in with Slack. It works exactly like regular token rotation, except with the Sign in Slack token exchange endpoint. You'll pass a `grant_type=refresh_token` and use a `refresh_token` parameter to obtain a new access token from [`openid.connect.token`](/reference/methods/openid.connect.token).

* * *

## Button generator {#generator}

You can use the Sign in with Slack button generator [here](https://api.slack.com/sign-in-with-slack-button-generator).

* * *

## Migrate a legacy Sign in with Slack app {#migrate}

If you have a [legacy Sign in with Slack app](/authentication/sign-in-with-slack/), there are only a few steps needed to migrate to the current flow. Request the [new OpenID scopes](#setup), reconfigure your authorization URL, parse the new response from `openid.connect.token`, and you're good to go.

Here's a map of what legacy Sign in with Slack feature corresponds to what modern feature:

*   The authorization endpoint becomes `/openid/connect/authorize`, rather than `/oauth/v2/authorize`.
*   You exchange your access code for an access token using an OpenID endpoint, [`openid.connect.token`](/reference/methods/openid.connect.token).
*   The `identity.basic` becomes the [`openid`](/reference/scopes/openid) scope.
*   The `identity.email` becomes the [`email`](/reference/scopes/email) scope.
*   The `identity.avatar` is contained in the [`profile`](/reference/scopes/profile) scope.
*   The `identity.team` is also contained in the [`profile`](/reference/scopes/profile) scope.
*   The `users.info` method becomes the [`openid.connect.userInfo`](/reference/methods/openid.connect.userInfo) method.

Enjoy your modern Sign in with Slack app! If you want to get even more nitty gritty details on how best to present a pleasant experience to users, read on for some [design guidelines](#design).

* * *

## Button design guidelines {#design}

You should [use our button generator](#generator) to create a Sign in with Slack button. But if you need to modify that button or create your own, here are some basic design guidelines you should follow:

*   Show the button prominently.
*   The Slack logo should always be present.
*   The text should always say Sign in with Slack, with ‘S’ capitalized.
*   Use the same size as other sign in options.
*   Make it visible and keep it above the fold.

### Sizing {#button_sizing}

![Image showing dimensions guidelines as explained below in text](/assets/images/siws_button_dimensions-b6b1ce7858d9a508d51585ec5fb49c29.png)

A max size button should be:

*   296px (width) x 56px (height)
*   18px font Lato bold
*   Logo : 24px x 24px

A minimum size button should be:

*   224px (width) x 44px (height)
*   14px font Lato bold
*   Logo : 16px x 16px

A default size button should be:

*   256px (width) x 48px (height)
*   16px font Lato bold
*   Logo : 20px x 20px

### Spacing {#button_spacing}

![Image showing spacing guidelines as explained below in text](data:image/png;base64,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)

For a center-aligned logo, use:

*   Margin-between: 12px

For a border-aligned logo, use:

*   Margin-left: 16px

### Corners {#button_corners}

![Image showing guidelines as explained below in text](data:image/png;base64,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)

Use a border-radius of:

*   Min: 4px
*   Max: height of the button

### Color themes {#button_themes}

![Image showing theme guidelines as explained below in text](data:image/png;base64,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)

For a default theme, use:

*   Background color : #FFFFFF
*   Font color : #000000
*   Border color : #DDDDDD

For a dark theme, recommended only for spaces with sufficient contrast, use:

*   Background color : #4A154B
*   Font color : #FFFFFF
*   Border : none

### Icon sizing {#icon_sizing}

You can also use an icon button consisting only of the Slack logo.

![Image showing guidelines as explained below in text](data:image/png;base64,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)

Dimensions of a max size button:

*   56px (width) x 56px (height)
*   Logo: 28px x 28px

Min size:

*   36px (width) x 36px (height)
*   Logo: 18px x 18px

Default size:

*   48px (width) x 48px (height)
*   Logo: 24px x 24px

### Icon corners {#icon_corners}

![Image showing guidelines as explained below in text](data:image/png;base64,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)

Use a border-radius of:

*   Min: 4px
*   Max: height of the button

### Icon color themes {#icon_themes}

![Image showing guidelines as explained below in text](data:image/png;base64,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)

Color guidelines for icon buttons are [the same as text buttons above](#button_themes).

### Assets {#assets}

If you can't use our [button generator](#generator), you can use the following static image assets instead. This HTML snippet references our CDN-hosted buttons:

```
<img src="https://platform.slack-edge.com/img/sign_in_with_slack.png" srcset="https://platform.slack-edge.com/img/sign_in_with_slack.png 1x, https://platform.slack-edge.com/img/sign_in_with_slack.png 2x" />
```

If you want to host the assets yourself, you can download these images:

[Download PNG (170px by 40px)](https://platform.slack-edge.com/img/sign_in_with_slack.png) [Download PNG (Retina, 344px by 80px)](https://platform.slack-edge.com/img/sign_in_with_slack.png)