Source: https://docs.slack.dev/app-management/quickstart-app-settings

# Creating an app from app settings

In the following guide, you'll create a basic Slack app that can send messages using webhooks.

Want a step-by-step guide using the Slack CLI and Bolt framework? Head over to this [Quickstart](/quickstart) guide.

## 1. Creating an app {#creating}

Create a Slack app via the apps page by selecting the following button:

[Create an app](https://api.slack.com/apps?new_app=1)

1.  Select **From scratch**.
2.  Enter your **App Name**. For this example, enter "Grocery Reminders".
3.  Select the **Workspace** where you'll be developing your app. You'll be able to [distribute your app](/app-management/distribution) to other workspaces later if you choose.
4.  Select **Create App**.

If you need to update the name of your app later, you can do so from your app's [**Home tab**](/surfaces/app-home#home-tab). Changing the _app name_ entry under **Basic Information** will update the bot name rather than the app name — this is the name that appears when the app performs actions such as posting in a channel or sending a direct message.

## 2. Requesting scopes {#scopes}

Next, you'll need to request [**scopes**](/reference/scopes) for your app. Scopes give your app permission to perform actions, such as posting messages in your workspace.

Slack apps can't post to any public channel by default; they gain that ability by asking for permission explicitly with the use of scopes. Request the [`chat:write.public`](/reference/scopes/chat.write.public) scope to gain the ability to post in all public channels without joining. Otherwise, you'll need to use the [`conversations.join`](/reference/methods/conversations.join) scope, or have your app invited into a channel by a user before it can post.

1.  Within **OAuth & Permissions**, scroll down to **Scopes**.
2.  Under **Bot Token Scopes**, select **Add an OAuth Scope**.
3.  To allow your app to post messages, add the [`chat:write`](/reference/scopes/chat.write) scope.
4.  To allow your app to access public Slack channels, add the [`channels:read`](/reference/scopes/channels.read) scope.

In general, you'll add scopes to your bot token, not your user token. A notable exception is if you need to act as a specific user (for example, posting messages on behalf of a user, or setting a user's status).

Slack apps cannot access the [Real Time Messaging (RTM) API](/legacy/legacy-rtm-api)

The [Events API](/apis/events-api/) allows your app to listen to Slack events in a structured, safe way. If you require access to RTM (for example, because you're building your app behind a corporate firewall), you'll need to create a legacy Slack app and use its bot token to call [`rtm.connect`](/reference/methods/rtm.connect). For more information, refer to [Legacy: Real Time Message API](/legacy/legacy-rtm-api).

## 3. Installing and authorizing the app {#installing}

1.  Scroll back to the top of the **OAuth & Permissions** page.
2.  Install your app by selecting the **Install to Workspace** button.
3.  You'll now be sent through the Slack OAuth flow. Select **Allow** on the following screen.

When you follow this flow, you're playing the part of the _installing user_, not the app. If you were adding your app to a different workspace besides your own, this flow would be completed by a user _from that workspace_ instead of you.

After installation, navigate back to the **OAuth & Permissions** page. You'll see an **access token** under **OAuth Tokens**.

Access tokens represent the permissions delegated to your app by the installing user. Keep it secret. Keep it safe. At a minimum, avoid checking them into public version control. Instead, access them via an environment variable.

Your access token allows you to call the methods described by the scopes you requested. For example, your [`chat:write`](/reference/scopes/chat.write) scope allows your app to post messages.

Your app isn't a member of any channels yet, so pick a channel to add some test messages in and `/invite` your app as in the following example slash command:

```
/invite @Grocery Reminders
```

You'll see a message posted in the channel confirming that your app was added.

## 4. Configuring the app for event listening {#listening}

Slack apps listen and respond to events. We've already touched on one way an app can respond: by calling [`chat.postMessage`](/reference/methods/chat.postMessage) to post a message. Apps can also respond to events such as mentions in a channel, menu selections, or users sending the app a direct message. Apps listen with the [Events API](/apis/events-api/). Let's subscribe to the [`app_mention`](/reference/events/app_mention) event.

1.  Select **Event Subscriptions** and toggle **Enable Events** to ON.
2.  Within **Subscribe to bot events**, select **Add Bot User Event**, then search for `app_mention`. As with scopes, always subscribe to events with a _bot user_.
3.  If your app will be using HTTP Request URLs, set the **Request URL** to a URL where your app's server listens to the incoming HTTP requests. Slack will send an HTTP request there when your app is mentioned, allowing your app to determine how it will respond. Note that you'll need to implement your own server for this step, as well as to send messages with webhooks. You may want to explore the [Bolt family of SDKs](/tools), which can allow you to implement a server that listens for events automatically. Also note that this step is not required if your app is set up to use Socket Mode; refer to [comparing HTTP & Socket Mode](/apis/events-api/comparing-http-socket-mode/) for more details.

You'll notice that the `app_mention` event requires the [`app_mentions:read`](/reference/scopes/app_mentions.read) scope. Events are like API methods: they allow your app access to information in Slack, so you'll need permissions for them. Reinstall your app to the workspace with this new scope. Now you'll be notified when your app is mentioned, and can determine how your app will respond.

## 5. Sending a message with a webhook {#webhooks}

1.  Select **Incoming Webhooks** from the left sidebar and toggle **Activate Incoming Webhooks** to ON.
2.  Select **Add New Webhook to Workspace** to start the webhook flow. Select the channel you previously invited your app to and then **Allow** on the following screen.
3.  Reinstall your app to the workspace with this new feature by selecting the **Reinstall to Workspace** button within the **Install App** page in the left sidebar.
4.  Navigate back to **Incoming Webhooks** and view the new entry listed under **WebHook URLs for Your Workspace**. Copy your webhook.
5.  Create a new HTTP POST request with the webhook as follows:

```
POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXXContent-type: application/json{    "text": "Gotta get the bread and milk!"}
```

Navigate to the channel your app was installed in to see the message posted by your app:

![Bot avatar](/assets/images/oslo-b2272998a620e09f3081347b23f939cc.png)

Oslo

Gotta get the bread and milk!

## Onward {#onward}

Congratulations on creating your very own Slack app! Keep learning about all the things your app can do by checking out the following:

*   [Sending messages using Incoming Webhooks](/messaging/sending-messages-using-incoming-webhooks)
*   [Designing Slack apps](/surfaces/app-design)
*   [App interactivity overview](/interactivity)
*   [Building with Block Kit](/block-kit)