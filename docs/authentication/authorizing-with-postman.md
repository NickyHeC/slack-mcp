Source: https://docs.slack.dev/authentication/authorizing-with-postman

# Authorizing with Postman

This guide will walk you through setting up a Slack app. Then, we'll introduce you to the Slack [OAuth authorization flow](/authentication) using [Postman](https://www.postman.com/).

This is good way to get a token if you only want to get a token once or just want to play around with the API. Note that this guide is mainly centered around getting a _bot token_, but we'll also go over how to obtain a user token at the [end](#get_user_token).

## Prerequisites {#prerequisites}

*   A [Slack workspace](https://slack.com/) with privileges to install apps. You may need to get in contact with an Admin or Owner on your workspace to do this.
*   [Postman](https://www.getpostman.com/) to authorize and test.

## Getting a bot token in Postman {#steps}

### 1. Create a Slack App {#create_app}

[Create an app](https://api.slack.com/apps?new_app=1)

Create an app by using the button above. Choose _From Scratch_ and give your app a name and workspace to live on.

### 2. Obtain the Client ID and Client Secret {#get_client_secret}

On the **Basic Information** page, scroll down and note the **Client ID** and **Client Secret**, which you can find under the **App Credentials** section. We'll need these values for later, so keep them in a safe place.

![client ID and client secret](/assets/images/basic_info-3cbdb5917ca619ff0cb4d5313b8600b1.png)

### 3. Add the Postman OAuth callback URL to your Redirect URLs {#add_callback_url}

In the left navigation, click **OAuth & Permissions** and scroll down to **Redirect URLs**. Here, add the following URL to your list of Redirect URLs:

`https://oauth.pstmn.io/v1/browser-callback`

This is the URL that Slack will redirect back to as part of the OAuth flow with a temporary value of `code`. Postman will do the heavy lifting by exchanging it for a token for us. If you want to learn more about this, take a look at our [OAuth docs](/authentication/installing-with-oauth#exchanging).

### 4. Add at least one scope to your app {#4-add-at-least-one-scope-to-your-app}

In order to have a bot user added to your app, you must specify at least one bot scope within your app's settings page. If you're requesting more scopes, you're welcome to add them as well, but you will need at least one. To do this, scroll down within the **OAuth & Permissions** page to **Scopes** and add the scopes that you want to request. As an example here, we're adding the `chat:write` scope.

### 5. Configure the OAuth settings {#oauth_settings}

Now that we have a Slack App to authorize against, we will setup an OAuth 2.0 client. In Postman's [Authorization menu](https://learning.postman.com/docs/sending-requests/authorization/), select **OAuth 2.0** for the type. It's best if you're using a Collection, as the token details will be reused for all methods found within that Collection, but you can also do this per method as well. Configure the OAuth client by filling out the form as below:

Item

Value

Comments

**Add auth data to**

Request headers

This means that the token will be added to the headers of your requests. This is a requirement of the Slack API, as you cannot send your token within the body.

**Token Name**

A name of your choice

Choose a name that you can use to keep track of your token.

**Grant Type**

Authorization code

The Slack API relies on issuing you a `code` value to exchange for your token. This tells Postman that we are using this paradigm.

**Callback URL**

`https://oauth.pstmn.io/v1/browser-callback`

If you toggle the `Authorize Using Browser` checkbox, this will automatically populate.

**Auth URL**

`https://slack.com/oauth/v2/authorize`

The first step of the OAuth flow requires that you direct users to this URL. Setting this here tells Postman to do this for you.

**Access Token URL**

`https://slack.com/api/oauth.v2.access`

The last step requires you to provide the `code` from the previous step and call this method. Setting this here tells Postman to call this URL with the proper values.

**Client ID**

The value of **Client ID**

Used in conjunction with the value of `code` to send to the `oauth.v2.access` method.

**Client Secret**

The value of **Client Secret**

Used in conjunction with the value of `code` to send to the `oauth.v2.access` method.

**Scope**

For example, `chat:write`

A comma-separated list of OAuth scopes. For a complete list of scopes see here.

**Client Authentication**

Send client credentials in the body

If you've filled everything out correctly, it'll look something like this:

![Oauth configuration in Postman](/assets/images/oauth_configuration-e34e35cd60dbdbf0e4697f0519f03353.png)

### 6. Click Get New Access Token and 🎉 {#obtain_bot_token}

Click **Get New Access Token** and a new browser window will open, prompting you for permissions to your workspace. If you accept the scopes requested, you should be automatically redirected back to Postman, and your token will have been issued. It will start with `xoxb-` and will be followed by a series of letters and numbers.

* * *

## Extras: How to get a user or Enterprise org-level token {#get_user_token}

If you're looking specifically to get a user token or Enterprise org-level scope— for example, anything starting with `admin.*` or `auditlogs:read`—you'll need to follow these steps since Postman doesn't work with multiple tokens being issued from the OAuth flow.

### 1. Publicly distribute your app (only if Enterprise org-level scopes are requested) {#distribute}

This step can be skipped if you aren't requesting Enterprise org-level scopes. How do you know if a scope is Enterprise org-level? Take a look at the [scopes page](/reference/scopes?filter=user), and if you see anything that starts with `admin.*` or `auditlogs:read`, that's an Enterprise org-level scope.

In order to use Enterprise org-level scopes, your app must be able to be installed on more than one workspace. This is what publicly distributing your app means. For more on information on this, refer to [public distribution](/app-management/distribution).

To publicly distribute your app, head to the **Manage Distribution** page by following the left-hand navigation on your app's settings page. Next, head to **Share Your App with Other Workspaces** and ensure you follow the steps to get green checks on all of these sections. Then, click **Activate Public Distribution**.

### 2. Add in the user scopes that you need {#add_user_scopes}

Follow the steps above, as these are the same for requesting a user token. Once you get to the step where you configure your OAuth settings, make sure all the values are the same except for the **Auth URL**. You'll need to append `?user_scope=` followed by a comma-separated list with all the User scopes that you'd like to request. As an example, if you want to request the scopes `chat:write` and `admin`, you'd use the following Auth URL:

`https://slack.com/oauth/v2/authorize?user_scope=chat:write,admin`

### 3. Obtain your token and use it as a Bearer token {#obtain_user_token}

Following the same steps as before, you’ll need to click **Get New Access Token** and follow the same steps to go through the OAuth process. The difference here is that you'll need to look at the payload from Slack that shows up within Postman's **Manage Access Tokens** modal. Within the payload, look for the `authed_user` object, and within this object you'll see an `access_token` property that starts with the characters `xoxp-`. Copy this value.

![client ID and client secret](/assets/images/user_token-346e1ac74ec6ead0ca894c716fd1217e.png)

Since Postman only allows for one token to be used at one time (if you have a bot token, it will be used by default), you'll need to paste your user token into the **Access Token** field within Postman.

![Adding user token to Postman](/assets/images/user_token_config-06bc78c1b042cdb7311e1be57bae28a6.png)

Now you are ready to make any calls to the API using your user token instead of a bot token! 🎉