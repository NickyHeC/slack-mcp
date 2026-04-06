Source: https://docs.slack.dev/ai/slack-mcp-server/developing

# Developing a sample app with the Slack MCP Server

MCP clients integrate with Slack by sending standard JSON-RPC 2.0 requests as defined by the MCP specification. Since Slack hosts and manages the MCP Server, handling the tool logic on your behalf, implementing the connection is simple.

The following instructions use the Bolt for JavaScript [Slack MCP Server Template app](https://github.com/slack-samples/bolt-js-slack-mcp-server) to show how to connect a Slack app to the Slack MCP server. While creating a new app is not necessary to start using the MCP server, we show creating a new app for the sake of example here.

Free sandbox

Join the Slack [Developer Program](https://api.slack.com/developer-program) for access to a free sandbox where you can build and experiment with apps outside of a production environment.

### Create an app {#new-app}

The first step to using the Slack MCP server in your Slack app is to create an app in the [app settings](https://api.slack.com/apps?new_app=1), then select **From a manifest**. Select a workspace where your app can live, then replace the JSON manifest with that of the [`manifest.json`](https://github.com/slack-samples/bolt-js-slack-mcp-server/blob/main/manifest.json) file from the sample app, also shown here:

`manifest.json`

```
{  "display_information": {      "name": "Slack MCP Sample"  },  "features": {      "app_home": {          "home_tab_enabled": false,          "messages_tab_enabled": true,          "messages_tab_read_only_enabled": false      },      "bot_user": {          "display_name": "Slack MCP Sample",          "always_online": true      },      "assistant_view": {          "assistant_description": "Sample that demonstrates the use of Slack's MCP server",          "suggested_prompts": []      }  },  "oauth_config": {      "redirect_urls": [          "https://example.ngrok-free.app/slack/oauth_redirect"      ],      "scopes": {          "user": [              "chat:write",              "canvases:write"          ],          "bot": [              "assistant:write",              "channels:history",              "chat:write",              "groups:history",              "im:history",              "mpim:history"          ]      }  },  "settings": {      "event_subscriptions": {          "request_url": "https://example.ngrok-free.app/slack/events",          "bot_events": [              "assistant_thread_context_changed",              "assistant_thread_started",              "message.im"          ]      },      "interactivity": {          "is_enabled": true,          "request_url": "https://example.ngrok-free.app/slack/events"      },      "org_deploy_enabled": true,      "socket_mode_enabled": false,      "token_rotation_enabled": false  }}
```

Enable the app for MCP by navigating to the **Agents & AI Apps** sidebar section and toggling **On** the **Model Context Protocol** feature.

![MCP setting](/assets/images/mcp_feature-bfe8c78372d2b7d24e1ff8d1721625dd.png)

### Add scopes {#add-scopes}

After following the prompts to create the app, you land on the **Basic Information** page of the app settings. Select **OAuth & Permissions** from the left sidebar and scroll down to the **Scopes** section. Which scopes your app requires depends on what actions you'd like it to take. You can see on this page which scopes the template has added.

The scopes listed below are the scopes related to MCP server tools. Add them to the user token.

MCP tool

User scope needed

Search messages/channels

[`search:read.public`](/reference/scopes/search.read.public), [`search:read.private`](/reference/scopes/search.read.private), [`search:read.mpim`](/reference/scopes/search.read.mpim), [`search:read.im`](/reference/scopes/search.read.im)

Search files

[`search:read.files`](/reference/scopes/search.read.files)

Search users

[`search:read.users`](/reference/scopes/search.read.users)

Send a message

[`chat:write`](/reference/scopes/chat.write)

Read a channel/thread

[`channels:history`](/reference/scopes/channels.history), [`groups:history`](/reference/scopes/groups.history), [`mpim:history`](/reference/scopes/mpim.history), [`im:history`](/reference/scopes/im.history)

Create/update a canvas

[`canvases:read`](/reference/scopes/canvases.read), [`canvases:write`](/reference/scopes/canvases.write)

Read user profile/email

[`users:read`](/reference/scopes/users.read), [`users:read.email`](/reference/scopes/users.read.email)

### Add a redirect URL {#add-redirect-url}

After adding the scopes, scroll back up on the page to **Redirect URLs**. Add a redirect URL and save it.

Tip

If you do not have a redirect URL available for testing, we recommend using [ngrok](https://ngrok.com/docs/what-is-ngrok#getting-started-expose).

Using ngrok, the format of the URL might look something like this:

```
https:///b21a03fd701b.ngrok-free.app/slack/oauth_redirect
```

Enabling the app for OAuth is needed in order to utilize user tokens in the app, and therefore allow the app to take action on the user's behalf.

### Install and run {#install}

Once your URL is saved, click to **Install** the app and follow the prompts.

Next, clone the sample app repo with the following command in your terminal:

```
# Clone this project onto your machinegit clone https://github.com/slack-samples/bolt-js-slack-mcp-server.git
```

Then, navigate to the directory and open it in VSCode.

```
cd bolt-js-slack-mcp-servercode .
```

Rename the `.env.sample` file to `.env` and copy and paste your environment variable values there. Go back to the app settings and navigate to the **Basic Information** page for these values. For the `SLACK_INSTALL_URL`, use the same base redirect link you used earlier, with `install` appended. Following the prior example, it would look like this:

```
https://b21a03fd701b.ngrok-free.app/slack/install
```

The install link is needed for each user to install the app so that the MCP server can query Slack on behalf of the invoking user.

The OpenAI key must be obtained by creating an OpenAI account and [creating a new key](https://platform.openai.com/api-keys). Once these keys are saved, go back to your terminal and install, then start the app:

```
# Install dependenciesnpm install# Run Bolt servernpm start
```

### Update event subscriptions {#event-subscriptions}

With your app running, there is one more update to make in the app settings. Navigate to **Event Subscriptions** and update the URL to the base of the redirect URL, with `/events` appended, so that it looks something like:

```
https://b21a03fd701b.ngrok-free.app/slack/events
```

Slack will verify the URL, then you should be good to test the app!

Make sure you install the app using the install link, then create a new chat with the app to test its functionality. Upon creation of the new chat, the user is prompted with two static options that demonstrate either sending a message to #general, or creating a new canvas – both as and on behalf of the user! You can see the code behind this in the app's [`user-message.js`](https://github.com/slack-samples/bolt-js-slack-mcp-server/blob/main/listeners/assistant/user-message.js) file.

### The MCP call {#mcp-call}

The MCP server is used as a tool that is provided alongside an API call to an LLM. Each LLM has a different way of formatting requests including an MCP server, so verify with their documentation for how to format it in your code. Here are a couple of examples.

In the sample app we created above, for example, the call to OpenAI using the Slack MCP server as a tool looks like this:

```
    const llmResponse = await openai.responses.create({        model: 'gpt-4o-mini',        input: `System: ${DEFAULT_SYSTEM_CONTENT}\n\n${parsedThreadHistory}\nUser: ${message.text}`,        tools: [            {                type: 'mcp',                server_label: 'slack',                server_url: 'https://mcp.slack.com/mcp',                headers: {                    Authorization: `Bearer ${context.userToken}`,                },                require_approval: 'never',            },        ],        stream: true,    });
```

For a call to Anthropic, it may look like this:

```
    const response = await client.beta.messages.create({        model: "claude-sonnet-4-20250514",        max_tokens: 1000,        system: DEFAULT_SYSTEM_CONTENT,        messages: [            ...parsedThreadHistory,            { role: "user", content: message.text }        ],        mcp_servers: [            {                type: 'url',                url: `https://mcp.slack.com/mcp`,                 name: 'slack',            }        ],        // The Anthropic SDK's structure for beta features might vary.     });
```

Check out the full code for the MCP sample app [here](https://github.com/slack-samples/bolt-js-slack-mcp-server).