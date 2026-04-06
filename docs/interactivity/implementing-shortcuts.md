Source: https://docs.slack.dev/interactivity/implementing-shortcuts

# Implementing shortcuts

**Shortcuts** let users quickly trigger workflows from various prominent locations within Slack.

Shortcuts can trigger [modals](/surfaces/modals) and other [app interactions](/interactivity#responses). When someone uses one of your shortcuts, your app will receive some context about what happened in an [interaction payload](#request_payload). They are gateways to powerful, productive workflows.

Apps can create **global shortcuts** that are available from anywhere in Slack, and **message shortcuts** that are shown only in message context menus.

#### Use cases {#use-cases}

*   Surface your app's core functionality globally within Slack
*   Enable users to take action on a message
*   Improve discoverability of your app

* * *

## Shortcut types {#shortcut-types}

### Global shortcuts {#global}

Global shortcuts are available to users via the shortcuts button in the message composer, and when using search in Slack.

These type of shortcuts are intended to trigger workflows that can operate without the context of a channel or message.

For example, users might trigger a global shortcut to create a calendar event or view their upcoming on-call shifts.

![](/assets/images/2021-nov-shortcuts-execution-b86dc2795872f75a7998ad044bb8c745.png)

### Message shortcuts {#messages}

Message shortcuts are shown to users in the context menus of non-ephemeral messages within Slack.

Message shortcuts will retain the context of the source message from which they were initiated. This makes them ideal when you have a workflow that relies on that context to work.

For example, users might quickly generate tasks from a posted message, or send messages to external services.

![](/assets/images/message_shortcuts-354f3adde554ab79fc9aa5ea86f6ae9a.svg)

Think about what app invocation points belong in a global context versus which belong in a message context.

For example, pretend you're building a task management app. An example of a shortcut that makes sense in a global context would be `Create a task`, whereas a shortcut that belongs in a message context would be `Attach to a task`, which could attach the specific message to an existing task.

* * *

## Getting started with shortcuts {#getting_started}

If you don't have a Slack app yet, [follow our quick guide to create one](/app-management/quickstart-app-settings#creating).

In order to start using shortcuts with your app, there are a few preparation steps you'll need to go through.

### Preparing for payloads {#enabling_components}

Ensure your app is ready to receive interaction payloads by providing a **Request URL**, as described in our [guide to handling user interactions](/interactivity/handling-user-interaction#setup).

### Adding the right permissions {#scope_permissions}

To make shortcuts available in Slack, your app must have the `commands` permission scope. You can either [request this scope during the OAuth flow](/authentication/installing-with-oauth#asking) or add it to your app OAuth settings:

1.  From your [app's dashboard](https://api.slack.com/apps), click the menu item **OAuth & Permissions**.
    
2.  Under _Scopes_, type `commands` into the text field, select the correct permission to add it, then click **Save Changes**.
    

If your app isn't already requesting `commands` at installation, it will need to be reinstalled before shortcuts can be used. If your app is published in the Slack Marketplace, the changes will be reflected only after the app is reviewed and approved.

* * *

## Creating a shortcut {#creating_shortcut}

Now that your app is ready, it's time to create some potential interaction energy:

1.  Open your [app's dashboard](https://api.slack.com/apps)
    
2.  Click on _Interactivity & Shortcuts_ in the sidebar
    
3.  Click the _Create New Shortcut_ button under _Shortcuts_
    
4.  Select from the _Global_ and _On messages_ options, depending on [which type of shortcut you want](#shortcut_types) and click _Next_
    
5.  Fill in the following:
    

*   _Name_: a short, catchy call to action. Start the name with a verb, and use sentence case (eg. “Create a ticket”).
*   _Short Description_: describe what the shortcut does for the benefit of a potential user.
*   _Callback ID_: a string that will be sent to your Request URL in an interaction payload — we'll talk about this more [later on](#request_payload).

6.  Click the green **Create** button, and you'll be sent back to the _Interactivity & Shortcuts_ page.
    
7.  On that page you'll need to click the **Save Changes** button.
    

That's it—you've created your first shortcut! You can create some more—each app can have up to 5 global shortcuts, and separately, 5 message shortcuts. Shortcuts will appear in shortcuts menus in the order in which they were created.

Now let's make sure you are ready to receive interaction payloads and do something in response.

* * *

## Handling the use of shortcuts in your app {#implementation}

You've created a shortcut, and at some point it will be used by someone in Slack. Your app has to handle that eventuality.

We explain the process in-depth in our [guide to handling user interactions in apps](/interactivity/handling-user-interaction#flow), including how to prepare your app with a request URL. In short, your app will receive an interaction payload after someone uses one of your shortcuts. Your app must process that payload and then send a response.

First, let's learn more about that interaction payload.

Take a shortcut to a solution with Bolt

Our Bolt framework, available in [JavaScript](/tools/bolt-js), [Python](/tools/bolt-python), and [Java](/tools/java-slack-sdk) allows you to rapidly build logic to handle shortcuts. [Learn more about Bolt](/tools).

### Processing the interaction payload {#request_payload}

When a shortcut is invoked, a request will be sent to the app's configured _Request URL_. The request body will contain a `payload` parameter that your app should parse for JSON.

Inside you'll discover an interaction payload containing lots of useful context — consult our [reference guide](/reference/interaction-payloads/shortcuts-interaction-payload) to see the full structure of the fields included.

Payloads for global shortcuts will contain different info from payloads for message shortcuts. For example, a payload for a message shortcut will include channel and message context, and a `response_url` for publishing message responses. If you want to publish a message in response to a global shortcut, [use our alternative approach](#global_response_url).

### Responding to shortcuts {#shortcut_response}

There are a few things to consider about responding to interaction payloads:

*   **Always send an [acknowledgment response](/interactivity/handling-user-interaction#acknowledgment_response)**.
    
    As soon as your app receives the interaction payload, a countdown begins, because this message will self-destruct in 3 seconds. If your app doesn't respond with an HTTP status `200 OK` within 3000ms of receiving the payload, the person who used the shortcut will see a generic error message letting them know that something went wrong.
    
*   **Your app must [follow up with a modal](/interactivity/handling-user-interaction#modal_responses) to confirm any action that will occur**.
    
    This will allow the user to feel much more confident using _any_ shortcut, as they can trust that they won't immediately publish a message or modify data.
    

Specify the [`default_to_current_conversation`](/reference/block-kit/block-elements/select-menu-element) parameter in block kit elements so users can send messages to the same channel your shortcut was invoked in.

*   **Beyond these essential actions, your app also has a range of more complex responses to take.**
    
    You can [use a field supplied in the interaction payload to publish messages](/interactivity/handling-user-interaction#message_responses), or [another payload field to pop a modal that can collect or present more info](/interactivity/handling-user-interaction#modal_responses). Shortcuts can also be a trigger for your app to [make calls to APIs or external services](/interactivity/handling-user-interaction#async_responses).
    

Global shortcuts and sending messages

If you're using global shortcuts, and want to publish messages as a response, you can do so by [triggering a modal containing a special conversation selector](/surfaces/modals#modal_response_url).

Apps should use this approach to ensure that users know that they can use _any_ shortcut without an unexpected message being published on their behalf.

Some recommendations related to shortcuts:

*   **Include user confirmation of results**
    
    Whenever a user completes an action with your app (even when it isn't associated with shortcuts), provide confirmation and details about what they just did. And for a third-party service, include relevant links out to the service.
    
    As an example, if the user performed an action like creating a new helpdesk ticket in a third-party service, include a link to where they can view more information about that ticket.
    
*   **Be clear when using paid-feature shortcuts**
    
    If your app’s core features are paid-only and you plan to expose them via shortcuts, you should make it apparent for non-paying users that the reason they can’t use the shortcut is because they must have a paid plan for your app. Rather than silently failing, we recommend opening an explanatory modal (or posting an ephemeral message) that explains why they can't use the shortcut.
    

Try it with AI

How often is a question posed in Slack that no one knows the answer to? Check out this example of a [message shortcut listener](/tools/bolt-js/concepts/shortcuts) that asks an AI Code Assistant app the question posed in the message where the user invoked the shortcut. These examples show [Bolt for JavaScript](/tools/bolt-js) and [Bolt for Python](/tools/bolt-python).

Click to expand code

*   JavaScript
*   Python

app.js

```
app.shortcut('ask_code_assistant', async ({ shortcut, ack, say, logger }) => {  try {    await ack();    const channelId = shortcut.channel.id;    const threadTs = shortcut.message_ts;    const message = shortcut.message.text;    const defaultInstruction = 'You are an AI code assistant app who helps users with their coding questions. Any markdown content you display in Slack mrkdwn.';    // Prepare the messages to send to the LLM    const messages = [{ role: 'system', content: defaultInstruction }, {role: 'user', content: message}];    // A Hugging Face client is used here, but this could be substituted for any LLM    const llmResponse = await hfClient.chatCompletion({        model: 'Qwen/QwQ-32B',        messages,        max_tokens: 2000,        });    // Reply in thread with the app's answer    await say({      text: llmResponse.choices[0].message.content,      channel: channelId,      thread_ts: threadTs,    });      } catch (error) {    logger.error(error);  }});
```

app.py

```
@app.shortcut('ask_code_assistant')def ask_code_assistant(ack, shortcut, say):    try:        ack()        default_instruction = 'You are an AI code assistant app who helps users with their coding questions. Any markdown content you display in Slack mrkdwn.'        # A Hugging Face client is used here, but this could be substituted for any LLM        hf_client = InferenceClient(token=os.getenv("HUGGINGFACE_API_KEY"))        channel_id = shortcut['channel']['id']        thread_ts = shortcut['message_ts']        message = shortcut['message']['text']        # Prepare the messages to send to the LLM        messages = [            {'role': 'system', 'content': default_instruction},            {'role': 'user', 'content': message}        ]                response = hf_client.chat.completions.create(            model="Qwen/QwQ-32B",            messages=messages,            max_tokens=2000,        )        # Reply in thread with the app's answer        say(            text=response.choices[0].message.content,            channel=channel_id,            thread_ts=thread_ts        )    except Exception as e:        print(f"Error: {e}")
```

* * *

## Limitations {#limitations}

*   Global shortcuts are not visible (and therefore usable) for all types of guest user. Please see our [Help Center](https://slack.com/intl/en-ie/help/articles/202518103-Multi-Channel-and-Single-Channel-Guests#guest-permissions) for an up-to-date breakdown of the [availability of shortcuts for these users](https://slack.com/intl/en-ie/help/articles/202518103-Multi-Channel-and-Single-Channel-Guests#guest-permissions).
    
*   When an app is submitted (or re-submitted) to the Slack Marketplace, the confirmation modal does not indicate any changes regarding global shortcuts. Despite the discrepancy, global shortcut changes _will_ be submitted upon confirmation.
    
*   An app responding to a shortcut initiated from a threaded message cannot currently publish a message back to that thread. They _can_ publish back to the parent conversation. We are working on a comprehensive solution that will make this possible.
    

* * *

## Next steps {#next}

You've now learned how to create a shortcut, and what your app has to do to handle their use. That's a great start!

Read our [guide to responding to interactions](/interactivity/handling-user-interaction#responses) to understand the vast range of possibilities open to your app at this point.

* * *

## Related references {#reference}

### Interaction payloads {#interaction-payloads-reference}

*   [Interaction payload reference for shortcuts](/reference/interaction-payloads/shortcuts-interaction-payload)

### Modal and messages {#modal-messages-reference}

*   [Web API: `views.open`](/reference/methods/views.open)
*   [Block Kit: Select menu with conversations list](/reference/block-kit/block-elements/select-menu-element#conversations_select)
*   [Block Kit: Select menu with channels list](/reference/block-kit/block-elements/select-menu-element#channels_select)