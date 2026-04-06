Source: https://docs.slack.dev/authentication/using-token-rotation

# Using token rotation

This guide covers [token rotation](https://datatracker.ietf.org/doc/html/rfc6819#section-5.2.2.3) for Slack apps, which use [granular permissions](/authentication/installing-with-oauth). You'll learn how to exchange your access token for a refresh token and an expiring access token.

With token rotation, you'll provide an extra layer of security for your access tokens.

## Overview {#overview}

An [access token](/authentication/tokens) represents an installation of your Slack app. Without token rotation, the access token never expires. With token rotation, it expires every 12 hours.

An OAuth flow with token rotation involves exchanging one expiring access token for a new one, using an additional token: the refresh token. The refresh token is then revoked, and a new refresh token is used to exchange the new expiring access token when it expires.

New access and refresh tokens need to be _rotated_ in throughout the lifespan of the app for it to continue to function.

Access token types

For Slack apps, the [access token types](/authentication/tokens) that may be refreshed are granular [bot](/authentication/tokens#granular_bot) or [user](/authentication/tokens#user) tokens.

## Before you begin {#start}

If you don't have a Slack app already, that's okay! Click on the button below to begin the process of creating one:

[Create an app](https://api.slack.com/apps?new_app=1)

Fill out your **App Name** and select the Development Workspace where you'll play around and build your app. Don't fuss too much over either field—no matter what workspace you select, you'll still be able to [distribute your app](/app-management/distribution) to other workspaces if you choose.

If you've just made your app, or if your Slack app isn't set up with our new OAuth V2, head over to our guide on [Installing with OAuth](/authentication/installing-with-oauth). We'll wait right here for you.

### Consider the Bolt framework {#consider}

If you use [Bolt](/tools#bolt) to develop your app, your job will be a whole lot easier. Token rotation is automatically handled in the Bolt framework for building Slack apps. All flavors of Bolt have versions that support token rotation.

Framework

Setup with token supported version

Bolt for Java

`implementation("com.slack.api:bolt-jetty:1.9.+")`

Bolt for JavaScript

`npm i @slack/bolt@3.5`

Bolt for Python

`pip install "slack-bolt>=1.7"`

Whether you're using an SDK or not, continue to turn on token rotation.

## Turn on token rotation {#turn}

Token rotation may not be turned off once it's turned on

You'll want to be sure you're prepared to refresh any newly issued or migrated tokens within 12 hours. Test your existing app in a development environment before enabling token rotation in production.

Before you turn on token rotation, consider how you're going to test your implementation. You don't want all your access tokens to expire before you've successfully figured out how to refresh them.

If your app _is not_ published in the Slack Marketplace, token rotation is enabled via the **OAuth & Permissions** section of your [app settings](https://api.slack.com/apps).

If your app _is_ published in the Slack Marketplace, now is a good time to follow the advice in our [guide to testing Slack Marketplace apps](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements). Apps published in the Slack Marketplace can have token rotation enabled via the **Published App Settings** section of your [app settings](https://api.slack.com/apps).

And if you're using a Bolt app, this is your stop! You're all good to go. If not, keep reading. The [next section](#exchange) is just for you.

## Exchange the long-lived access token {#exchange}

A Slack app implemented with OAuth will already have a long-lived access token. You need to call the [`oauth.v2.exchange`](/reference/methods/oauth.v2.exchange) method to exchange that long-lived access token for a refresh token and an expiring access token.

You'll need your app's `client_id` and `client_secret` as well, which can be found under "App Credentials" within the specific app's "Basic Information" [page](https://api.slack.com/apps).

Here's a sample call:

```
POST /api/oauth.v2.exchangeHOST slack.comContent-Type: application/x-www-form-urlencodedclient_id=60503450.61416client_secret=8bc5fc53901afc11ctoken=xoxb-1234-...
```

Either a granular [bot token](/authentication/tokens#user) or [user token](/authentication/tokens#user) may be exchanged for a refresh token and expiring access token. You won't be able to exchange the same access token for a refresh token more than once.

After you refresh your short-lived credentials for the first time, we'll expire your original long-lived access token. Please don't try to revoke it yourself using [`auth.revoke`](/reference/methods/auth.revoke), or you'll end up making the user redo the whole OAuth installation process (_yikes!_). Instead, just call [`auth.test`](/reference/methods/auth.test) to make sure the original token won't work anymore. Keep in mind that this applies to **both user** and **bot** tokens, so make sure to repeat the OAuth process to get your hands on fresh credentials.

Here's a sample response from `oauth.v2.exchange` when exchanging a bot token:

```
{    "ok": true,    "access_token": "xoxe.xoxb-1-...", // New access token    "expires_in": 43200, // 12 hours    "refresh_token": "xoxe-1-...", // New refresh token    "token_type": "bot",    "scope": "commands,incoming-webhook",    "bot_user_id": "U123456",    "app_id": "A123456",    "team": {        "name": "Slack Softball Team",        "id": "T123456"    },    "enterprise": {        "name": "slack-sports",        "id": "E12345678"    },}
```

Notice that your `access_token` now has a new `xoxe.` prefix. The access token's lifespan is based on the `expires_in` field. This field defines the number of seconds until the access token you've received expires. It will always expire in 43,200 seconds, which is 12 hours.

The response will also have a `refresh_token`.

You now have your first set of rotatable tokens!

## Refresh a token {#refresh}

Any time you implement OAuth with your Slack app, whether token rotation is enabled or not, the last step of the flow requires you to call the [`oauth.v2.access`](/reference/methods/oauth.v2.access) method. The only difference with token rotation is that you'll be calling the method throughout your app's life to get new tokens.

In order to refresh a token, make a call to `oauth.v2.access`, setting the new `grant_type` parameter to your refresh token:

```
POST /api/oauth.v2.accessHOST slack.comContent-Type: application/x-www-form-urlencodedclient_id=60503450.61416client_secret=8bc5fc53901afc11cgrant_type=refresh_tokenrefresh_token=xoxe-1-...
```

Note that `client_id` and `client_secret` are still required for this call as well.

When you have turned on the token rotation toggle, your app will receive additional data from `oauth.v2.access`. Expect a response that contains the following new fields [mentioned earlier](#exchange):

```
    ...    "expires_in": 43200, // 12 hours    "refresh_token": "xoxe-1-...",    ...
```

You can receive refresh tokens for both user tokens and bot tokens in the same `oauth.v2.access` response (only applies to the initial `oauth.v2.access` response **before** token rotation is enabled).

If you make use of a [user token](/authentication/tokens#user), expect those two new fields along with your access token in the response:

```
    "id": "U1234",    "scope": "chat:write",    "access_token": "xoxe.xoxp-1-1234-...",    "expires_in": 43200, // 12 hours    "refresh_token": "xoxe-1-..."    "token_type": "user"
```

Use the new `refresh_token` when you need to refresh the tokens once again. Schedule a task to refresh your access token _before_ the `expires_in` time. If you don't refresh your access token in time, you'll receive an error when you make an API call with the expired access token.

Store the refresh token as you would an access token, in a database or secure datastore (not in code). Refresh tokens are designed to be used once. After calling `oauth.v2.access`, the refresh token you used is revoked after a short grace period.

Calling `oauth.v2.access` will not immediately invalidate your existing access token. If you need to immediately revoke an access token, you can call [`auth.revoke`](/reference/methods/auth.revoke).

2 active token limit

If you refresh your credentials repeatedly before expiration (e.g. by calling `oauth.v2.access` multiple times for the same token within a 12 hour period), we will enforce a limit of 2 active tokens. If more than 2 tokens exist after the refresh, the oldest additional token will be revoked.

Once you've successfully refreshed an access token, congratulations! You're now developing with a more secure app that makes use of token rotation.

* * *

## App manifests and token rotation {#manifests}

You may **also** create a new app that makes use of token rotation using [app manifests](/app-manifests/configuring-apps-with-app-manifests).

Add the following to your app manifest YAML to enable token rotation:

```
settings:  token_rotation_enabled: true
```

* * *

## Uninstalling apps {#uninstall}

Slack APIs provide multiple ways to undo Slack installations. With [`apps.uninstall`](/reference/methods/apps.uninstall), behavior is the same regardless of whether the app uses token rotation. The app is uninstalled and all tokens associated with the installation are revoked.

[`auth.revoke`](/reference/methods/auth.revoke) is used to revoke a single token of an installation. When used on an app **without** token rotation, it usually revokes the authorization associated with it, meaning that the user or team that had the app installed needs to reinstall it.

For apps _with_ token rotation, `auth.revoke` will revoke a single token (a refresh token, a bot access token that expires, or a user access token that expires) without changing the underlying installation. Events will still be delivered and new tokens may still be generated in the UI.