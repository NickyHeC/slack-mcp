Source: https://docs.slack.dev/ai/agent-entry-and-interaction

# Entry points and interaction surfaces

An entry point is where a user’s action invokes your agent. At that moment, responsibility for acting on the user’s intent passes from the user to your app. Slack offers several surfaces where users can access and interact with your agent.

## Entry points {#entry-points}

Some entry points require you to enable the **Agents & AI Apps** setting in your [app settings](https://api.slack.com/apps) to become available in the Slack UI:

*   Top bar entry point for launching the agent in a split pane
*   Chat and History tabs in the app UI

Entry points that do not require that setting are:

*   @-channel mentions
*   Direct messages

### Agent container {#assistant-container-entry}

When the **Agents & AI Apps** feature is enabled in your [app settings](https://api.slack.com/apps), the top nav entry point and agent container are available.

![Image of an entry point](/img/guides/ai_container/entrypoint.png)

The [Bolt](/tools#bolt) `Assistant` class wraps three API events into handler callbacks, providing a single lifecycle for the agent container:

*   The `threadStarted` callback wraps the [`assistant_thread_started`](/reference/events/assistant_thread_started) event: user opens the container. Set suggested prompts and initialize state here.
*   The `threadContextChanged` callback wraps the [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed) event: user navigates to a different channel while the container is open. Use to keep responses grounded in the user's current context.
*   The `userMessage` callback wraps the [`message.im`](/reference/events/message.im) event: user sends a message. This is the app's core response loop: set status, call LLM, respond.

```
const assistant = new Assistant({  threadStarted: async ({ say, setSuggestedPrompts }) => {    await say({ text: 'Hi! How can I help?' });    await setSuggestedPrompts({      prompts: [        { title: 'Summarize a channel', message: 'Summarize the last week of #general' },        { title: 'Draft a message', message: 'Help me write a project update' }      ]    });  },  threadContextChanged: async ({ assistantThread }) => {    // assistantThread.context.channel_id is the newly active channel    // update thread state if context-grounded responses are needed  },  userMessage: async ({ message, say, setStatus }) => {    await setStatus({ status: 'Thinking...' });    // call LLM with message.text, then:    await say({ text: 'Here is your answer.' });  }});app.use(assistant);
```

### Channel mentions {#channel-mentions}

The [`app_mention`](/reference/events/app_mention) event fires when a user @-mentions your bot in a channel or thread. Always reply in-thread using `thread_ts ?? event.ts`. This uses the `thread_ts` if it exists; otherwise, fall back to `event.ts`.

```
app.event('app_mention', async ({ event, client }) => {  const channel = event.channel;  const threadTs = event.thread_ts ?? event.ts;  await client.chat.postMessage({ channel, thread_ts: threadTs, text: 'On it!' });});
```

### Direct messages {#direct-messages}

Listen for the [`message.im`](/reference/events/message.im) event for when a user messages your agent outside of the assistant container. Filter on `channel_type: im` to distinguish from group DMs.

```
app.message(async ({ message, say }) => {  if (message.channel_type !== 'im') return;  await say({ text: 'Got your message!' });});
```

## Interaction surfaces {#interaction-surfaces}

Interaction surfaces are where users engage with your agent. These include the agent container, conversations (channels, threads, messages), App Home, modals, slash commands, shortcuts, and unfurls.

### Agent container {#agent-container}

The native AI assistant panel (split pane in the Slack client), accessible from the top bar. Use for conversational agent interactions: back-and-forth dialogue, multi-turn reasoning, and contextual responses. Interactions here are implemented using the Bolt `Assistant` class.

![Image of split view pane](/img/guides/ai_container/splitview.png)

We recommend setting dynamic prompts based on context clues from the interaction: the channel, user profile, connected company data, etc. Seeing the same prompts at every interaction may suggest that the app is less connected to the workspace and not optimized for repeat usage. Read more about setting suggested prompts in [Developing agents](/ai/developing-agents#respond-to-the-assistant_thread_started-event).

### Conversations {#conversations}

Conversations include channels, threads, and messages.

#### Channels {#channels}

Be clear with users about where and how the app works. Does it work in channels? Does it support @-mentions? Or is it solely used in the split view? Meet users where they work, whether that is in a dedicated split view container for 1:1 interaction or within channels where one or more users are asking questions.

Implementing channel support

Communicating where and how the app is available can be done in the [App Home](#app-home) or during user onboarding. To support your app's use in channels, be sure to implement a listener and respond to the [`app_mention`](/reference/events/app_mention) event. Check out how this is done in our Bolt for Python [AI Chatbot](https://github.com/slack-samples/bolt-python-ai-chatbot/blob/main/listeners/events/app_mentioned.py) sample app.

#### App threads {#app-threads}

App threads are designed to organize conversations and feature a single thread in the conversational experience. Slack automatically starts new threads when appropriate.

We recommend [keeping chat titles updated](/ai/developing-agents#threads). The thread title is set automatically after the user sends their first message. Update the title to keep it accurate according to the conversation it describes.

Set the title initially to capture the first question from the user. Update it when necessary. This makes it easier to find a conversation when browsing the **History** tab.

![Image of ai app threads](/img/guides/ai_container/assistantthreads.png)

#### Messages {#messages}

Responses posted in-thread keep agent work anchored to the message that triggered it without flooding the channel. Always reply using `thread_ts ?? event.ts` to use `thread_ts` when available and `event.ts` as a fallback. This is triggered via the [`app_mention`](/reference/events/app_mention) event.

_Ephemeral messages_

These are temporary messages visible only to the triggering user. Use them for command acknowledgments, inline errors, confirmations, and "here's what I'm about to do" prompts that shouldn't be broadcast to the whole channel. They are the recommended default for slash command responses and shortcut acknowledgments. The channel and user fields vary by context. Use:

*   `event.channel` / `event.user` in event handlers
    
*   `command.channel_id` / `command.user_id` in slash command handlers
    
*   `body.channel.id` / `body.user.id` in action/shortcut handlers
    
    ```
    await client.chat.postEphemeral({channel: event.channel,  // command.channel_id in slash commands, body.channel.id in actionsuser: event.user,        // command.user_id in slash commands, body.user.id in actionstext: 'Got it — working on your request now.'});
    ```
    

### App Home {#app-home}

The App Home is the user's personal space with your app, accessible from the app's page in Slack. Use the App Home as the persistent surface for workflow visibility and orchestration controls. Show running workflows, recent completions, and blocked items in one place. Expose pause/resume/stop/retry/redirect actions so users can intervene without reconstructing thread history. Use Block Kit in the App Home for configurable status views, settings, and recovery paths. Publish on [`app_home_opened`](/reference/events/app_home_opened):

```
app.event('app_home_opened', async ({ event, client }) => {  await client.views.publish({    user_id: event.user,    view: { type: 'home', blocks: [] }  });});
```

Implementing the App Home

First go to your [app settings](https://api.slack.com/apps), select your app, and navigate to **App Home** under **Features** in the left navigation. This menu allows you to configure which tabs are available in your app, along with a few other configurations. Ensure your app is set to use the Home Tab. Then refer to the [App Home](/surfaces/app-home#home-tab) guide for how to customize this surface.

### Modals {#modals}

Modals are temporary overlays for structured, focused input. Use for multi-step flows, form collection, confirmation dialogs, and any interaction requiring the user's full attention before the agent proceeds. Open with the [`views.open`](/reference/methods/views.open) API method and handle submission with a `view` listener:

```
// Openawait client.views.open({  trigger_id,  view: {    type: 'modal',    callback_id: 'my_modal',    title: { type: 'plain_text', text: 'Title' },    submit: { type: 'plain_text', text: 'Submit' },    blocks: []  }});// Handle submissionapp.view('my_modal', async ({ view, ack }) => {  await ack();  const values = view.state.values;});
```

Implementing modals

Pre-filling a modal with the approximate information will allow the user to review the information rather than needing to fill it out manually before submitting.

[Gather user input](/surfaces/modals#gathering_input) and take advantage of the `initial_value` / `initial_options` property to prefill the modal. For example, if an app is used for gathering information for submitting an issue, the app could send a message with a button that, when clicked, opens a modal for data collection. In that modal, you can use the [plain-text input](/reference/block-kit/block-elements/plain-text-input-element) for fields and pre-populate them with user-provided data using the `initial_value` field.

### Slash commands {#slash-commands}

Slash commands are text-invoked workflows with inline arguments. Use when users need to trigger a task explicitly with parameters (`/summarize #channel last 7 days`) rather than starting a conversation. Always `ack()` immediately:

```
app.command('/myapp', async ({ command, ack, client }) => {  await ack();  const [subcommand] = command.text.trim().split(/\s+/);  // route by subcommand or respond inline});
```

Slash commands are not supported in the split view container because all messages in the container or in conversation with the app take place in message threads; slash commands do not work in threads in general. They do work in messages.

### Shortcuts {#shortcuts}

Message shortcuts are triggered from the message context menu. The agent receives the full message payload, making this the recommended pattern for "act on this message" interactions, including summarize, create a ticket, draft a reply, or any action where the message content is the input:

```
app.shortcut({ callback_id: 'my_action', type: 'message_action' }, async ({ shortcut, ack, client }) => {  await ack();  await client.views.open({ trigger_id: shortcut.trigger_id, view: { /* modal */ } });});
```

Global shortcuts are triggered from the shortcut button (`+`) in the compose box toolbar in Slack. Use these as a quick-launch entry point for agent workflows that don't start from a particular message:

```
app.shortcut({ callback_id: 'my_shortcut', type: 'shortcut' }, async ({ shortcut, ack, client }) => {  await ack();  await client.views.open({ trigger_id: shortcut.trigger_id, view: { /* modal */ } });});
```

### Unfurls {#unfurls}

Unfurls are rich previews for shared links. Subscribe to the [`link_shared`](/reference/events/link_shared) event and call the [`chat.unfurl`](/reference/methods/chat.unfurl) API method to replace a plain URL with structured Block Kit content. This is useful when your agent surfaces data that users will frequently share as links:

```
app.event('link_shared', async ({ event, client }) => {  await client.chat.unfurl({    channel: event.channel,    ts: event.message_ts,    unfurls: {      [event.links[0].url]: { blocks: [] }    }  });});
```

## Next steps {#next-steps}

✨ Develop the entire response loop of your agent with guidance from [Developing agents](/ai/developing-agents).

✨ Learn the best way to [manage context](/ai/agent-context-management) in agents.