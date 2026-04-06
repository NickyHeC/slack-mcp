Source: https://docs.slack.dev/authentication/installing-with-oauth

# Installing with OAuth

Slack apps are installed with a v2 OAuth 2.0 flow. We're sorry about all the "2s": OAuth 2.0 refers to the [2.0 version of the OAuth spec](https://oauth.net/2/), and this is our second version of OAuth 2.0. For the rest of this guide, we'll just refer to it as "OAuth".

For posterity, this OAuth flow works the same as the OAuth flow for legacy Slack apps. Only a few details have changed; URL and method names have gained a `v2`, and the shape of the OAuth access response now puts bot access tokens first. We created a version 2 of the OAuth flow because it provides more granular Slack scopes, especially for bot users. Your app can act with its own identity, instead of acting on behalf of users — all without requesting excessive permissions that could cause installations to be rejected.

* * *

## How it works: a high-level overview {#how}

OAuth allows a user in any Slack workspace to install your app. At the end of the OAuth flow, your app gains an access token. Your app's access token opens the door to [Slack API methods](/apis/web-api/), [events](/apis/events-api/), and [other features](/interactivity). During the OAuth flow, you specify which [scopes](/reference/scopes) your app needs. Those scopes determine exactly which doors your app can open.

Implementing an OAuth flow can feel hard because there are a lot of steps, but your app really only has to worry about three steps to make OAuth work: [requesting](#asking) scopes, [waiting](#waiting) for a user to give their approval, and [exchanging](#exchanging) a temporary authorization code for an access token. Redirecting a user to Slack can be done with a single link. For example:

```
[Add to Slack](https://slack.com/oauth/v2/authorize?scope=incoming-webhook&client_id=33336676.569200954261)
```

Replace the `client_id` with your app's client ID, and add the scopes you'd like. Bot scopes should be added as `scope=<bot_scope>`, and user scopes should be added as `user_scope=<user_scope>`.

For example, if your app only has one bot scope and it is `incoming-webhook`, the redirect would look like that shown above. If your app has a user scope, it might look like this instead:

```
https://slack.com/oauth/v2/authorize?user_scope=search%3Aread&client_id=33336676.569200954261
```

If your app has both a bot and a user scope, it might look like this:

```
https://slack.com/oauth/v2/authorize?scope=incoming-webhook&user_scope=search%3Aread&client_id=33336676.569200954261
```

* * *

## Obtaining access tokens with OAuth {#obtaining}

Your app obtains an access token in three steps:

1.  [Requesting scopes](#asking).
2.  [Waiting for a user to approve your requested scopes](#waiting).
3.  [Exchanging a temporary authorization code for an access token](#exchanging).

Why is there a third exchanging step in OAuth at all? Why doesn't Slack send your app an access token directly after the user okays your app? The reason is _two-factor authentication_. You have to prove both that you have the right temporary authorization code, _and_ that you have your app's client secret.

### Requesting scopes {#asking}

While developing your app, you'll determine a minimum list of [scopes](/reference/scopes) that your app requires to work. When a user installs your app in their workspace, you'll request those scopes.

To request scopes, redirect Slack users to `https://slack.com/oauth/v2/authorize`. If you're developing a [GovSlack](/govslack) app for use by public sector customers, redirect users to `https://slack-gov.com/oauth/v2/authorize`.

A scope conflict occurs when attempting to combine [Sign in with Slack (SIWS)](/authentication/sign-in-with-slack/) user scopes with non-Sign in with Slack scopes in the same OAuth flow

Each set of scopes must be requested in a separate OAuth flow.

Include both your app's client ID, which is found in the [**App Management**](https://api.slack.com/apps) page, and a comma-separated list of scopes, such as: `scope=incoming-webhook,commands`. The full redirect URL will look something like this:

```
https://slack.com/oauth/v2/authorize?scope=incoming-webhook,commands&client_id=3336676.569200954261
```

The `scope` list requests scopes for your app's bot user. If you have specific need for a user token (for example, so that you can act on behalf of a user), provide a `user_scope` parameter with requested user scopes instead of, or in addition to, the `scope` parameter.

Also note that each installation can result in additive scopes. For example, if a user installs your app in a workspace where you request `channels:history` and then installs your app again where you request `channels:read`, both `channels:history` and `channels:read` will be assigned to the token. There is no way to remove scopes from an existing token without revoking it entirely.

When requesting scopes, you also need to tell Slack where to send your temporary authorization code afterward. Include a `redirect_uri` parameter in the URL above. The `redirect_uri` is where Slack will send the user back to, along with the temporary authorization code, once the user okays your app. The `redirect_uri` must use HTTPS. Alternatively, you can configure a Redirect URL in the **App Management** page under **OAuth & Permissions**. A Redirect URL must also use HTTPS.

When there are multiple Redirect URL values configured, the `redirect_url` parameter must be sent in both the **Authorize** and **Access** steps described below, and the parameter value must be the same for both steps — otherwise, you will encounter a `bad_redirect_uri` error:

1.  **Authorize**: You direct the user to the corresponding /oauth/v2/authorize path (this can be done with a link or button, for example). Send the `redirect_uri` in this step.
2.  **Redirect**: Slack redirects the user to what was specified as the `redirect_uri` in the previous step, and adds a verification code to that URL.
3.  **Access**: Your server retrieves the verification code from the previous step and sends it to the [`oauth.v2.access`](/reference/methods/oauth.v2.access) API endpoint to exchange that code for an access token.  If you sent a `redirect_uri` field in the first step, you must send that same field with the same value in this step.

If there are multiple Redirect URL values configured, but no `redirect_uri` parameter is sent, the OAuth flow will use the first Redirect URL listed on the **App Management** page. You can use the `redirect_uri` parameter in your `oauth/v2/authorize` redirect as mentioned above and configure a Redirect URL in the **App Management** page. Your `redirect_uri` must match or be a subdirectory of a Redirect URL configured under **App Management**. A Redirect URL can _not_ contain an anchor (`#`).

```
REDIRECT_URL: https://example.com/pathGOOD redirect_uri: https://example.com/pathGOOD: https://example.com/path/subdir/otherBAD:  http://example.com/barBAD:  http://example.com/BAD:  http://example.com:8080/pathBAD:  http://oauth.example.com:8080/pathBAD:  http://example.org
```

#### The team parameter {#team}

When a valid team ID is passed to `team` and the authenticating user is already signed in to that workspace, passing this parameter ensures the user will auth against that workspace.

If the user is not signed in yet, the user will be asked to specify a workspace to sign in to. That workspace will then be used as they complete the authorization flow, regardless of any `team` parameter you provided when the flow began.

If you omit the optional `team` parameter, the user will be allowed to choose which workspace they are authenticating against.

#### Optional scopes {#optional-scopes}

Optional scopes allow you to mark certain permissions as optional during app configuration, giving users more control over what data your app can access while reducing installation abandonment.

You can designate scopes as optional in two ways: via the [app settings](https://api.slack.com/apps) or the app manifest.

*   **App settings**: In the app settings, uncheck the checkbox next to any scope you want to mark as optional. ![optional scopes](/assets/images/optional_scopes-d8eb7bc28e26a2ae3300ee07ce69e4bd.png)
    
*   **App manifest**: Add optional scopes to the `bot_optional` or `user_optional` [fields](/reference/app-manifest#oauth) within the `oauth_config.scopes` object. Optional scopes must also be listed in the corresponding bot or user fields.
    
    ```
    "oauth_config": {    "scopes": {        "bot": [            "commands",            "chat:write",            "chat:write.public",            "metadata.message:read",            "links:read",            "assistant:write",            "im:history",            "reactions:write"        ],        "bot_optional": [            "chat:write"        ],        "user": [            "channels:history",            "reactions:read",            "reactions:write"        ],        "user_optional": [            "reactions:write"        ]},    "redirect_urls": [        "https://example.com/slack/auth"    ],    "token_management_enabled": true},
    ```
    

### Waiting for a user to approve your requested scopes {#waiting}

Good news! Your app doesn't really have to do _anything_.

Prepare for the return of a user by listening for HTTP requests at whatever Redirect URL you specified.

[Optional scopes](#optional-scopes) give end users visibility and control over what data an app can access from their account. During installation, users are presented with the optional scopes the admin has pre-approved and can choose which ones to grant. Apps should respect users' scope selections and handle the absence of ungranted scopes gracefully. Refer to the [Handling optional scopes in your app](#handling-optional-scopes) section below for guidance.

### Exchanging a temporary authorization code for an access token {#exchanging}

If all goes well, a user goes through the Slack app installation and okays your app with all the scopes it requests. Then, Slack redirects the user back to your specified Redirect URL.

Parse the HTTP request that lands at your Redirect URL for a `code` field. That's your temporary authorization code, which expires after ten minutes. Check the `state` parameter if you sent one along with your initial user redirect. If it doesn't match what you sent, consider the authorization a forgery.

Now, you just need to exchange the code for an access token. You'll do this by calling the [`oauth.v2.access`](/reference/methods/oauth.v2.access) method as follows:

```
curl -F code=1234 -F client_id=3336676.569200954261 -F client_secret=ABCDEFGH https://slack.com/api/oauth.v2.access
```

Once you complete your access call, Slack sends you an HTTP request response containing an access token. It looks something like this:

```
{    "ok": true,    "access_token": "xoxb-17653672481-19874698323-pdFZKVeTuE8sk7oOcBrzbqgy",    "token_type": "bot",    "scope": "commands,incoming-webhook",    "bot_user_id": "U0KRQLJ9H",    "app_id": "A0KRD7HC3",    "team": {        "name": "Slack Pickleball Team",        "id": "T9TK3CUKW"    },    "enterprise": {        "name": "slack-pickleball",        "id": "E12345678"    },    "authed_user": {        "id": "U1234",        "scope": "chat:write",        "access_token": "xoxp-1234",        "token_type": "user"    }}
```

If you requested scopes for a user token, you'll find them with a user access token under the `authed_user` property.

One more suggestion: show the user a nice message once they are redirected and you successfully gain an access token — or, if there's been an error, report that error to the user. The reason the user is redirected back to your app at the end of OAuth is for transparency purposes: the user deserves to know the end of the story, whether your app was installed successfully or not.

#### Handling optional scopes in your app {#handling-optional-scopes}

Apps must demonstrate usage of all scopes (both required and optional) and handle the absence of optional scopes gracefully. When a user doesn't grant an optional scope, your app should still function for features that don't require it.

*   **Graceful degradation**: Handle `missing_scope` API errors when optional scopes aren't granted.
*   **Token scope storage**: Store the granted scopes from the `oauth.v2.access` response to proactively show or hide features based on what the user has authorized.
*   **Feature gating**: Check token scopes before displaying functionality that requires optional permissions.

## The user-centric flow: the oauth.v2.user.access method {#v2-user-access}

In addition to the standard workspace installation flow, Slack provides a dedicated flow for obtaining user-specific access tokens. To initiate a user-specific flow, redirect users to the `v2_user` authorization endpoint:

```
https://slack.com/oauth/v2_user/authorize?client_id=YOUR_CLIENT_ID&scope=chat:write,channels:history
```

Unlike the the standard `v2/authorize` endpoint, this flow focuses exclusively on the user's identity and personal permissions. After approval, Slack redirects back to your `redirect_uri` with a temporary `code`, just like the standard flow.

### Exchanging the code with oauth.v2.user.access {#exchanging-the-code-with-oauthv2useraccess}

Once you have the temporary authorization code, you must exchange it using the [`oauth.v2.user.access`](/reference/methods/oauth.v2.user.access) API method. This method is compliant to the OAuth 2.0 RFC.

### Comparing oauth.v2.access and oauth.v2.user.access endpoints {#comparing-oauthv2access-and-oauthv2useraccess-endpoints}

The [`oauth.v2.access`](/reference/methods/oauth.v2.access) API method supports generating either a bot token or user token or both.

The [`oauth.v2.user.access`](/reference/methods/oauth.v2.user.access) API method generates a user token by default following the standard OAuth spec and works out-of-the-box with [MCP](/ai/slack-mcp-server) authorization flows.

The `oauth.v2.user.access` endpoint should be used in scenarios where:

*   You only need user tokens, not bot tokens
*   You're building [MCP integrations](/ai/slack-mcp-server) with desktop IDE clients like Cursor or Claude Code

Use the `oauth.v2.access` API method unless your client cannot support passing `scope` and `scope_user` in the same request.

## Appending scopes {#appending_scopes}

When you initially send a user through the OAuth flow, you receive a token that has the set of scopes you requested. Any subsequent time(s) you send that same user through the OAuth flow, any new scopes you request will be added to that initial set.

For example, if you initially request `channels:read` and `channels:write` from a user, the initial token will only be scoped to `channels:read channels:write` (plus `identify`, which is automatically included in any OAuth grant for a classic app). If you send that same user through a second OAuth flow, this time requesting `files:write`, the resulting token will have the new scope added to the previous set: `channels:read channels:write files:write identify`.

This process can be repeated any number of times, and each scope you request is **additive** to the scopes you've already been awarded. It is not possible to downgrade an access token's scopes.

As you make [Web API](/apis/web-api/) requests, a `x-oauth-scopes` HTTP header will be returned with every response indicating which scopes the calling token currently has:

```
x-oauth-scopes: identity.basic,reactions:read
```

* * *

## More about tokens {#tokens}

### Using tokens {#using}

The best way to communicate your access tokens — also known as bearer tokens — to Slack is by presenting them in a request's `Authorization` HTTP header where the full value, including "Bearer", is case-sensitive. This approach is required when using `application/json` with a write method.

```
GET /api/conversations.list?limit=50Authorization: Bearer xoxb-1234-abcdefgh
```

Alternatively, you may send the token as a POST body attribute of the `application/x-www-form-urlencoded` variety.

POST body:

```
POST /api/conversations.listContent-type: application/x-www-form-urlencodedtoken=xoxb-1234-abcdefgh&limit=50
```

### Revoking tokens {#revoking}

OAuth tokens do not expire. If they are no longer needed, they can be revoked. Revocation of an OAuth token happens if a workspace owner fully uninstalls the app, a user individually removes their configurations, or the account of the user who initially authenticated the Slack app is deactivated.

API access tokens are revoked via the [`auth.revoke`](/reference/methods/auth.revoke) method. After that happens:

*   The bot token no longer works.
*   The bot user is removed from the workspace.
*   Slash commands associated with the bot token will be removed from the workspace if no user tokens for the same app exist and carry the `commands` scope.
*   Incoming webhooks that were installed and associated with the bot token will be removed.
*   If no user tokens for the same app exist, the app will appear to be uninstalled from the workspace.

Additionally, for Slack apps using granular permissions, you can exchange your access token for a refresh token and an expiring access token with [token rotation](/authentication/using-token-rotation).

### Storing tokens securely {#storing}

Store your application's credentials and user tokens with care. Restrict Web API access to only IP addresses you trust by allowlisting specific IP addresses. Read up on [best practices for security](/security).

## Errors {#errors}

Below are some errors you may encounter and reasons for encountering them:

*   `bad_redirect_uri`: Occurs when there are multiple `redirect_url` parameter values configured and they do not match.
*   `invalid_scope`: Occurs if requesting a non-existent scope or requesting a set of scopes that are in conflict with each other (e.g. SIWS user scopes cannot be combined with non-SIWS user scopes).
*   `invalid_team_for_non_distributed_app`: Occurs when attempting to install/authorize an undistributed Slack API app on a team where the app was not created.
*   `scope_not_allowed_on_enterprise`: Occurs when attempting to install an app in an Enterprise org containing scopes that are not org-compatible. See below for more details.
*   `unapproved_scope`: Occurs if attempting to install a published app for which the requested scopes aren't approved either because they're still in review for that app, or they weren't yet submitted for review by the app developer.

### Non-Enterprise scopes {#non-enterprise-scopes}

The following is a list of scopes that are not org-compatible:

*   [bot](/reference/scopes/bot/)
*   [apps.requests.write](/reference/scopes/apps.requests.write/)