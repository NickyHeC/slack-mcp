Source: https://docs.slack.dev/interactivity/implementing-slash-commands

# Implementing slash commands

![An example slash command](data:image/png;base64,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)

Slash commands allow users to invoke your app by typing a string into the message composer box. By enabling slash commands, your app can be summoned by users from any conversation in Slack. Slash commands created by developers cannot, however, be invoked in message threads.

A submitted slash command will cause a payload of data to be sent from Slack to the associated app. The app can then respond in whatever way it wants using the context provided by that payload.

When part of an app, they can be installed for your workspace as a [single workspace app](/app-management/distribution) or [distributed to other workspaces](/app-management/distribution) via the [Slack Marketplace](/slack-marketplace/distributing-your-app-in-the-slack-marketplace).

Built-in slash commands

There is a set of [built-in slash commands](https://slack.com/help/articles/360057554553-Use-shortcuts-to-take-actions-in-Slack#built-in-shortcuts). These include slash commands such as `/topic` and `/remind`.

Built-in slash commands are unique commands with unique additional features. They, along with [Giphy app](https://slack.com/help/articles/204714258-Giphy-for-Slack) slash commands, are the only slash commands that can be invoked in message threads.

## Understanding the structure of slash commands {#command_structure}

Slash commands require a particular invocation structure that makes them less universally usable compared to [other app entry points](/interactivity). Ensure you [understand your app's audience](/surfaces/app-design) before implementation.

Let's look at an example slash command for an app that stores a list of to-do tasks:

`/todo ask @crushermd to bake a birthday cake for @worf in #d-social`

Here's the structure:

*   `/todo` - This is the `command`, the part that tells Slack to treat it as a slash command and where to route it. You'll define yours [below](#creating_commands).
*   `ask @crushermd to bake a birthday cake for @worf in #d-social` - This is the `text` portion, it includes everything after the first space following the command. It is treated as a single parameter that is passed to the app that owns the command (we'll discuss this [more below](#app_command_handling)).

We want to make sure that birthday cake gets baked, so read on to find out how to set up commands for your apps as well as how to handle and respond to them.

* * *

## Getting started with slash commands {#getting_started}

In order to get slash commands up and running with your app, you'll have to create the command itself, then prepare your app to be able to handle the interaction flow. We'll describe that flow in more detail in the steps below, but the basic pattern is:

*   A Slack user types in the message box with the command and submits it.
*   A payload is sent via an HTTP POST request to your app.
*   Your app responds.

Let's look closer at the recipe for making a great slash command.

### 1. Creating a slash command {#creating_commands}

You need two things to create a command:

*   A Slack app,
*   The name of your new command.

If you don't already have a Slack app, click below to create one:

[Create an app](https://api.slack.com/apps?new_app=1)

Now let's get to actually creating that command. First, head to your [App Management](https://api.slack.com/apps) dashboard, select the app you wish to work with, then select **Slash Commands** under **Features** in the navigation menu. You'll be presented with a button called **Create New Command**, and when you click it, you'll see a screen prompting you to define your new slash command:

#### Defining slash commands {#defining_slash_command}

*   **Command**: The name of the command, which is the actual string that users will type to trigger a world of magic. Bear in mind our [naming advice below](#naming_your_command) when you pick this.
    
*   **Request URL**: The URL we'll send a payload to when the command is invoked by a user. You'll want to use a URL that you can set up to receive these payloads as we'll describe [later in this doc](#app_command_handling). If [public distribution](/app-management/distribution) is active for your app, this needs to be an HTTPS URL (and self-signed certificates are not allowed). If you're building an app [solely for your own workspace](/app-management/distribution), it should also be HTTPS.
    
*   **Short Description**: A short description of what your command does.
    
*   **Usage Hint**: Displayed to users when they try to invoke the command, so if you have any parameters that can be used with your command, we recommend showing them here. You'll see a preview of the autocomplete entry where this hint is displayed, so make sure you're keeping this hint brief enough not to get truncated.
    
*   **Escape channels, users, and links sent to your app**: Turning this on will modify the parameters sent with a command by a user. It will wrap URLs in angle brackets and it will translate channel or user mentions into their correlated IDs. Private channels will only include the channel ID (`<C987654321|>`) while public channels will display the channel ID _and name_ (`<C123456789|public-channel-01>`). So, if a user invoked your command like this:
    
    ```
    /todo ask @crushermd to bake a birthday cake for @worf in #d-social
    ```
    
    You'll receive the following in the sent data payload:
    
    ```
    ask <@U012ABCDEF> to bake a birthday cake for <@U345GHIJKL> in <#C012ABCDE>
    ```
    
    If disabled, the payload will repeat the plain text:
    
    ```
    ask @crushermd to bake a birthday cake for @worf in #d-social
    ```
    
    While your eyes might take less offense to the second example, in that case you'd have to resolve those plain-text names yourself using [`users.list`](/reference/methods/users.list) or [`conversations.list`](/reference/methods/conversations.list) if you planned to use any Slack API in your response to the command.
    
    We recommend that you enable this feature if you expect to receive user or channel mentions in the command text.
    

#### Naming your slash command {#naming_your_command}

Consider your command's name carefully. Slash commands are not namespaced. This means multiple commands may occupy the same name. If this happens and a user tries to invoke the command, Slack will always invoke the one that was installed most recently. It's an important thing to consider, especially if you're planning to distribute your app.

When you're picking a command name, you'll want to avoid terms that are generic and therefore likely to be duplicated. On the other hand, you don't want the command to be too complicated for users to easily remember.

In essence, a great command is descriptive and understandable but also unique. Naming it after your service is often a good idea.

Once you've created your command, any channel or workspace where your app is installed will immediately be able to start using it, so let's learn what to do when a user types one of your app's commands.

### 2. Preparing your app to receive commands {#app_command_handling}

When a slash command is invoked, Slack sends an HTTP POST to the Request URL [you specified above](#creating_commands). This request contains a data payload describing the source command and who invoked it, like a really detailed knock at the door.

For example, imagine a workspace at example.slack.com installed an app with a command called `/weather`. If someone on that workspace types `/weather 94070` in their `#test` channel and submits it, the following payload would be sent to the app:

#### Payload example {#payload_example}

```
token=gIkuvaNzQIHg97ATvDxqgjtO&team_id=T0001&team_domain=example&enterprise_id=E0001&enterprise_name=Globular%20Construct%20Inc&channel_id=C2147483705&channel_name=test&user_id=U2147483697&user_name=Steve&command=/weather&text=94070&response_url=https://hooks.slack.com/commands/1234/5678&trigger_id=13345224609.738474920.8088930838d88f008e0&api_app_id=A123456
```

This data will be sent with a `Content-type` header set as `application/x-www-form-urlencoded`. Here are details of some of the important fields you might see in this payload:

##### Command payload info {#command_payload_descriptions}

Parameter

Description

`token`

(Deprecated) This is a verification token, a deprecated feature that you shouldn't use any more. It was used to verify that requests were legitimately being sent by Slack to your app, but you should use the [signed secrets functionality](/authentication/verifying-requests-from-slack) to do this instead.

`command`

The command that was entered to trigger this request. This value can be useful if you want to use a single Request URL to service multiple slash commands, as it allows you to tell them apart.

`text`

This is the part of the slash command _after_ the command itself, and it can contain absolutely anything the user might decide to type. It is common to use this text parameter to provide extra context for the command. You can prompt users to adhere to a particular format by showing them in the [_Usage Hint_ field when creating a command](#creating_commands).

`response_url`

A temporary [webhook URL](/messaging/sending-messages-using-incoming-webhooks) that you can use to [generate message responses](/interactivity/handling-user-interaction#message_responses).

`trigger_id`

A short-lived ID that will allow your app to open [a modal](/surfaces/modals).

`user_id`

The ID of the user who triggered the command.

`user_name`

(Deprecated) The plain text name of the user who triggered the command. Do not rely on this field as it has been [phased out](/changelog/2017-09-the-one-about-usernames). Use the `user_id` instead.

`team_id`, `enterprise_id`, `channel_id`, etc.

These IDs provide context about where the user was in Slack when they triggered your app's command (e.g. the workspace, Enterprise organization, or channel). You may need these IDs for your command response. The various accompanying `*_name` values provide you with the plain text names for these IDs, but as always you should only rely on the IDs as the names might change arbitrarily. We'll include `enterprise_id` and `enterprise_name` parameters on command invocations when the executing workspace is part of an Enterprise organization.

`api_app_id`

Your Slack app's unique identifier. Use this in conjunction with [request signing](/authentication/verifying-requests-from-slack) to verify context for inbound requests.

If [public distribution](/app-management/distribution) is active for your app, Slack will occasionally send your command's request URL a POST request to verify the server's SSL certificate.

These requests will include a parameter `ssl_check` set to `1` and a `token` parameter. See [Verifying requests from Slack](/authentication/verifying-requests-from-slack) for more information. Mostly, you may ignore these requests, but please do [confirm receipt as below](#responding_basic_receipt).

This payload is like getting all the ingredients to bake a really nice cake, so let's take a look at the recipe.

### 3. Responding to commands {#responding_to_commands}

There are three main ingredients in the response cake:

1.  Acknowledge your receipt of the payload.
2.  Do something useful in response right away.
3.  Do something useful in response later.

The first is like the cake itself, a required minimum, but the other two are like optional icing and toppings. We'll examine this more closely.

#### Confirming receipt {#responding_basic_receipt}

This is the step which lets Slack, and therefore the user, know that the command was successfully received by the app, regardless of what the app intends to do. Your app can do this by sending back an empty HTTP 200 response to the original request.

If you don't do this, the user will be shown an error message that indicates that the slash command didn't work — not a great experience for the user, so you should always acknowledge receipt (unless you didn't receive the command, but then you wouldn't know not to respond, and now we've fallen into a logical paradox).

This confirmation _must be_ received by Slack within 3000 milliseconds of the original request being sent, otherwise an `operation_timeout` error will be displayed to the user. If you couldn't [verify the request payload](/authentication/verifying-requests-from-slack), your app should return an error instead and ignore the request. The HTTP 200 response _doesn't have to be empty_ however, it can contain other useful stuff — a plain cake isn't all that tasty, so maybe we should add some icing.

#### Sending an immediate response {#responding_immediate_response}

As mentioned, you can include more substantive info in the body of your HTTP 200 response. In fact, you can use any of the complex [formatting](/messaging/formatting-message-text) or [Block Kit layout options](/messaging#complex_layouts) that are available when sending _any_ [message](/messaging/sending-and-scheduling-messages).

You can include this message either as plain text in the response body:

```
It's 80 degrees right now.
```

Or as a JSON payload in the response body, with a `Content-type` header of `application/json`:

```
{    "blocks": [    {      "type": "section",      "text": {        "type": "mrkdwn",        "text": "*It's 80 degrees right now.*"      }    },    {      "type": "section",      "text": {        "type": "mrkdwn",        "text": "Partly cloudy today and tomorrow"      }    }  ]}
```

These message responses can even include interactive elements like buttons or menus to allow users to interact more and keep the workflow active. Read our [guide to composing messages](/messaging) to explore the full range of possibilities.

**Message Visibility**

There's one special feature to response messages. When responding with a JSON payload you can directly control whether the message will be visible only to the user who triggered the command (we call these ephemeral messages), or to all members of the channel where the command was triggered.

The `response_type` parameter in the JSON payload controls this visibility; by default it is set to `ephemeral`, but you can specify a value of `in_channel` to post the response into the channel, like this:

```
{    "response_type": "in_channel",    "text": "It's 80 degrees right now."}
```

When the `response_type` is `in_channel`, both the response message and the initial slash command entered by the user will be shared in the channel. For the most clarity, we recommend always declaring your intended `response_type`, even if you wish to use the default `ephemeral` value.

![Example of a command in channel response](data:image/png;base64,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)

#### Enterprise Grid considerations {#enterprise-grid}

For Enterprise Grid organizations where apps are installed on multiple workspaces within the Grid, users will be prompted to select the workspace they want to run their slash command in when run from within a multi-workspace channel or a DM:

![Example of a slash command in Enterprise Grid](/assets/images/slash-command-enterprise-grid-09848c947aaea844b06a1ba4eb12fc74.png)

#### Other responses {#responding_response_url}

If you need to respond outside of the 3-second window provided by the request responses above, you still have plenty of options for keeping the workflow alive.

Read our [guide to responding to user interactions](/interactivity/handling-user-interaction#responses). There, we'll explain how you can use fields such as `response_url` or `trigger_id` from your [slash command payload](#command_payload_descriptions) to open modals and send messages.

When you're reading our [guide to responding to user interactions](/interactivity/handling-user-interaction#responses), you'll encounter fields called `replace_original` and `delete_original`, which can be used in conjunction with your `response_url` to modify previously-posted app messages in that interactive chain.

It's important to note that these fields _cannot_ modify the original user-posted message that was used to invoke the slash command.

We also explain [all the multitude of other ways](/interactivity/handling-user-interaction#async_responses) you can top this cake.

Try it with AI

Do you ever have a question that's top of mind you wish you could ask AI without disrupting your flow? Consider this [listener](/tools/bolt-js/concepts/commands) example that allows users to ask an AI Code Assistant app a question using a slash command. These examples show [Bolt for JavaScript](/tools/bolt-js) and [Bolt for Python](/tools/bolt-python).

Click to expand code

*   JavaScript
*   Python

app.js

```
app.command('/ask-code-assistant', async ({ command, ack, say, logger }) => {  try {    await ack();    const userId = command.user_id;    const channelId = command.channel_id;    const commandText = command.text;    const defaultInstruction = 'You are an AI code assistant app who helps users with their coding questions. Any markdown content you display in Slack mrkdwn.';    // Use the `say` method to post a public confirmation of the user's question in the channel    const firstMessage = await say(`Hello <@${userId}>! Your question: "${commandText}"`);        // Prepare the messages to send to the LLM    const messages = [{ role: 'system', content: defaultInstruction }, {role: 'user', content: commandText}];    // A Hugging Face client is used here, but this could be substituted for any LLM    const llmResponse = await hfClient.chatCompletion({        model: 'Qwen/QwQ-32B',        messages,        max_tokens: 2000,    });    // Reply in thread with the app's answer    await say({      text: llmResponse.choices[0].message.content,      channel: channelId,      thread_ts: firstMessage.ts,    });  } catch (error) {    logger.error('Error handling slash command:', error);  }});
```

app.py

```
@app.command("/ask-code-assistant")def handle_slash_command(ack, say, command, logger):    try:        # Acknowledge the command within 3 seconds        ack()        user_id = command["user_id"]        channel_id = command["channel_id"]        command_text = command["text"]        hf_client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))        default_instruction = "You are an AI code assistant app who helps users with their coding questions. Any markdown content you display in Slack mrkdwn."        # Use the `say` method to post a public confirmation of the user's question in the channel        first_message = say(f"Hello <@{user_id}>! Your question: \"{command_text}\"")                # Prepare the messages to send to the LLM        messages = [            {"role": "system", "content": default_instruction},            {"role": "user", "content": command_text}        ]        # A Hugging Face client is used here, but this could be substituted for any LLM        llm_response = hf_client.chat_completion(            model="Qwen/QwQ-32B",            messages=messages,            max_tokens=2000,        )        # Reply in thread with the app's answer        say(            text=llm_response.choices[0].message.content,            channel=channel_id,            thread_ts=first_message["ts"],        )    except Exception as e:        logger.error(f"Error handling slash command: {e}")
```

### Sending error responses {#responding_with_errors}

There are going to be times when you need to let the user know that something went wrong — perhaps the user supplied an incorrect text parameter alongside the command, or maybe there was a failure in an API being used to generate the command response.

It would be tempting in this case to return an HTTP 500 response to the initial command, but this isn't the right approach. The status code returned as a response to the command should only be used to indicate whether or not the request URL successfully received the data payload — while an error might have occurred in processing and responding to that payload, the communication itself was still successful.

Instead, you should continue to follow the above instructions to send either a response [back via the HTTP request](#responding_immediate_response) or using the `request_url` in a [message response](/interactivity/handling-user-interaction#message_responses). In that response message, communicate the error back to the user:

```
{  "response_type": "ephemeral",  "text": "Sorry, slash commando, that didn't work. Please try again."}
```

* * *

## Best practices {#best-practices}

*   If you're not ready to respond to an incoming command but still want to acknowledge the user's action by having their slash command displayed within the channel, respond to your URL's invocation with a simplified JSON response containing only the `response_type` field set to `in_channel`: `{"response_type": "in_channel"}`.
*   If your command doesn't need to post anything back (either privately or publicly), respond with an empty HTTP 200 response. Only do so if you are absolutely sure no response is necessary or desired. Even a short "Got it!" ephemeral response is better than nothing.
*   Help your users understand how to use your command. **Provide a help action that explains your command's usage**. If your slash command was `/please`, you should provide a response to `/please help` that lists the other actions available.
*   Always [validate](/authentication/verifying-requests-from-slack) an incoming slash command request that has been issued to you by Slack.
*   Turn on [escaping for usernames, channels, and links](#creating_commands) by flipping the toggle in your slash command's configuration dialog. Always work with user IDs and channel IDs.
*   [Give your command a descriptive and unique name](#naming_your_command) to avoid conflicts with other apps.
*   Using multiple commands with multiple apps or development environments? Look for `api_app_id` to differentiate which app is intended for the slash command invocation.