Source: https://docs.slack.dev/ai/developing-agents

# Developing agents

Slack offers a unique messaging experience for agents, including a side-by-side window within the Slack client, an app launch point accessible from the top bar in Slack, special loading states, suggested prompts, and app threads. Slack does not provide an LLM; rather, it gives you the tools and interface to best integrate an LLM of your choice for use in Slack.

Developing and using some AI features require a paid plan, despite being visible in the app settings on any plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

This guide takes you through the response loop of developing an agent. The response loop is the cycle of receive input → reason → call tools → stream/render output → repeat if needed. It's the core interaction engine of any agent app.

## Getting started {#getting-started}

To set up your app for agent capabilities, first [create an app](https://api.slack.com/apps?new_app=1), then find the **Agents & AI Apps** feature in the sidebar, and enable it.

![Feature toggle in app settings](/assets/images/agents_ai_apps_toggle-7f161ea91cdb314613abf727cbe0932b.png)

By toggling on this feature, your app will live in the top bar app [entry point](/agent-entry-and-interaction) in Slack and will be available for interaction in the split pane. The [`assistant:write`](/reference/scopes/assistant.write) scope is automatically added to your app (verifiable in the app manifest) when you toggle on this feature. The `assistant:write` scope is needed for the top bar entry point and split pane view, as well as suggested prompts and setting thread titles.

You will also want to subscribe to the [`assistant_thread_started`](/reference/events/assistant_thread_started), [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed), and [`message.im`](/reference/events/message.im) events.

Remember to provide an agent overview in the setup too!

Apart from the entry point and side pane, the rest of the AI-related app features need to be implemented. Use this guide to do so both with and without the use of the Bolt frameworks.

## Initial user interaction {#initial-interaction}

When the user first opens the container, Slack sends the [`assistant_thread_started`](/reference/events/assistant_thread_started) event along with the `context` object. The `context` object is shown below:

```
    "context": {       "channel_id": "C123ABC456",       "team_id": "T123ABC456",       "enterprise_id": "E123ABC456"    }
```

Some applications have no use for the `context` object. Perhaps your app does, though! If so, first call the [`conversations.info`](/reference/methods/conversations.info) method to see if your app has access to the channel, then proceed from there.

The [`assistant_thread_context_changed`](/reference/events/assistant_thread_context_changed) event is sent when a user opens a new channel while the container is open. This can be used to track the active context of a user in Slack.

### Onboarding and welcome message {#onboarding}

Send a call to action or suggest next steps when a user interacts with an agent for the very first time. Once this requirement is completed, optimize for repeat use and avoid repetitive prompts and 'getting started' types of messaging. This is important especially when it is necessary for the user to sign in, connect an account, agree to terms of service, or review a code of conduct.

Implementing user onboarding

We recommend using an [interactive element](/messaging/creating-interactive-messages) or [link](/messaging/formatting-message-text#linking-urls) if an action is needed or the user needs to visit a document or external URL.

For an app that requires the user complete a login flow to access all of the features, a first message could include a block that looks something like this:

```
{    "type": "rich_text",    "block_id": "Vrzsu",    "elements": [        {            "type": "rich_text_quote",            "elements": [                {                    "type": "text",                    "text": "It looks like you're not logged into the TeamworkDreamwork app.\n Sign in now to use this feature."                }            ]        }    ]},{    "type": "actions",    "block_id": "actionblock789",    "elements": [        {            "type": "button",            "style": "primary",            "text": {                "type": "plain_text",                "text": "Sign in"            },            "value": "sign_in_123"        },        {            "type": "button",            "style": "danger",            "text": {                "type": "plain_text",                "text": "Ignore"            }        }    ]}
```

View this example in [Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22block_id%22:%22Vrzsu%22,%22elements%22:%5B%7B%22type%22:%22rich_text_quote%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22It%20looks%20like%20you're%20not%20logged%20into%20the%20TeamworkDreamwork%20app.%5Cn%20Sign%20in%20now%20to%20use%20this%20feature.%22%7D%5D%7D%5D%7D,%7B%22type%22:%22actions%22,%22block_id%22:%22actionblock789%22,%22elements%22:%5B%7B%22type%22:%22button%22,%22style%22:%22primary%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Sign%20in%22%7D,%22value%22:%22sign_in_123%22%7D,%7B%22type%22:%22button%22,%22style%22:%22danger%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Ignore%22%7D%7D%5D%7D%5D%7D).

## Respond to the assistant_thread_started event {#thread-started}

Present the user with suggested prompts using the [`assistant.threads.setSuggestedPrompts`](/reference/methods/assistant.threads.setSuggestedPrompts) API method. We recommend using the Bolt framework to handle the details for you.

![suggested prompts](/img/guides/ai_container/suggestedprompts.png)

*   API call
*   Bolt for Python
*   Bolt for JS

Here is a sample request for the API without using the Bolt framework. Refer to the [method docs](/reference/methods/assistant.threads.setSuggestedPrompts) or [app flow section below](#app-flow) for more implementation details.

```
{   "channel_id": "D123ABC456",   "thread_ts": "1724264405.531769",   "title": "Welcome. What can I do for you?",   "prompts": [         {            "title": "Generate ideas",            "message": "Pretend you are a marketing associate and you need new ideas for an enterprise productivity feature. Generate 10 ideas for a new feature launch.",          },          {            "title": "Explain what Slack stands for",            "message": "What does Slack stand for?",          },          {            "title": "Describe how AI works",            "message": "How does artificial intelligence work?",          },   ]}
```

Use the Bolt for Python utility to set predetermined suggested prompts for the user to choose from. Refer to the [Bolt for Python docs](/tools/bolt-python/concepts/ai-apps#handling-user-response) for more details.

```
assistant = Assistant()@assistant.thread_starteddef start_assistant_thread(    say: Say,    get_thread_context: GetThreadContext,    set_suggested_prompts: SetSuggestedPrompts,    logger: logging.Logger,):    try:        say("How can I help you?")        prompts: List[Dict[str, str]] = [            {                "title": "Suggest names for my Slack app",                "message": "Can you suggest a few names for my Slack app? The app helps my teammates better organize information and plan priorities and action items.",            },        ]        thread_context = get_thread_context()        if thread_context is not None and thread_context.channel_id is not None:            summarize_channel = {                "title": "Summarize the referred channel",                "message": "Can you generate a brief summary of the referred channel?",            }            prompts.append(summarize_channel)        set_suggested_prompts(prompts=prompts)    except Exception as e:        logger.exception(f"Failed to handle an assistant_thread_started event: {e}", e)        say(f":warning: Something went wrong! ({e})")
```

Use the Bolt for JavaScript utility to set predetermined suggested prompts for the user to choose from. Refer to the [Bolt for JavaScript docs](/tools/bolt-js/concepts/ai-apps#handling-new-thread) for more details.

```
...threadStarted: async ({ event, logger, say, setSuggestedPrompts, saveThreadContext }) => {    const { context } = event.assistant_thread;    try {      await say('Hi, how can I help?');      await saveThreadContext();      /**       * Provide the user up to 4 optional, preset prompts to choose from.       *       * The first `title` prop is an optional label above the prompts that       * defaults to 'Try these prompts:' if not provided.       */      if (!context.channel_id) {        await setSuggestedPrompts({          title: 'Start with this suggested prompt:',          prompts: [            {              title: 'This is a suggested prompt',              message:                'When a user clicks a prompt, the resulting prompt message text ' +                'can be passed directly to your LLM for processing.\n\n' +                'Assistant, please create some helpful prompts I can provide to ' +                'my users.',            },          ],        });      }      if (context.channel_id) {        await setSuggestedPrompts({          title: 'Perform an action based on the channel',          prompts: [            {              title: 'Summarize channel',              message: 'Assistant, please summarize the activity in this channel!',            },          ],        });      }    } catch (e) {      logger.error(e);    }  },...
```

## Listen for the message.im event {#message-im}

The user then will type a message or click on a prompt which triggers a [`message.im`](/reference/events/message.im) event. The event is the same whether the user clicked the suggested prompt or typed it manually. Users can message your app via the container or through your app's Chat tab.

Your app can respond to the user directly or it can pass back the `thread_ts` parameter to continue in the same thread. In most situations, you will want to call the [`chat.postMessage`](/reference/methods/chat.postMessage) method with the `thread_ts` parameter.

When your app receives the `thread_ts` parameter, you can retrieve the conversation by using `thread_ts` as the unique identifier. This is useful if your app stores the long-lived context or the state of a thread.

You can also fetch previous thread messages using the [`conversations.replies`](/reference/methods/conversations.replies) method and choose which other messages from the conversation to include in the LLM prompt or your app logic.

_Note: @-mentions in channels can happen like they do today; whether you support this or not is up to you. You can engage with the user or ask them to use the container to converse with your app._

## Provide a loading state {#loading-state}

Your app should then call the [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus) method to display the status indicator in the container. We recommend doing so immediately for the user's benefit.

Loading states indicate to your user that the app is working on a response.

![loading state](/img/guides/ai_container/loadingstates.png)

We recommend using the Bolt framework to handle the details for you.

*   API call
*   Bolt for Python
*   Bolt for JS

Here is a sample request for the API without using the Bolt framework. Refer to the [method docs](/reference/methods/assistant.threads.setStatus) or [app flow section below](#app-flow) for more implementation details.

```
{   "status": "is working on your request...",   "channel_id": "D324567865",   "thread_ts": "1724264405.531769"}
```

Use the Bolt for Python `setStatus` utility to cycle through strings passed into a `loading_messages` array. Refer to the [Bolt for Python docs](/tools/bolt-python/concepts/ai-apps#handling-user-response) for more details.

```
# This listener is invoked when the human user sends a reply in the assistant thread@assistant.user_messagedef respond_in_assistant_thread(    client: WebClient,    context: BoltContext,    get_thread_context: GetThreadContext,    logger: logging.Logger,    payload: dict,    say: Say,    set_status: SetStatus,):    try:        channel_id = payload["channel"]        team_id = payload["team"]        thread_ts = payload["thread_ts"]        user_id = payload["user"]        user_message = payload["text"]	# Set your desired statuses here        set_status(            status="thinking...",            loading_messages=[                "Untangling the internet cables…",                "Consulting the office goldfish…",                "Convincing the AI to stop overthinking…",            ],        )...
```

Use the Bolt for JavaScript `setStatus` utility to cycle through strings passed into a `loading_messages` array. Refer to the [Bolt for JavaScript docs](/tools/bolt-js/concepts/ai-apps#handling-user-response) for more details.

```
...const assistant = new Assistant({  ...  userMessage: async ({ client, context, logger, message, getThreadContext, say, setTitle, setStatus }) => {    if (!('text' in message) || !('thread_ts' in message) || !message.text || !message.thread_ts) {      return;    }    const { channel, thread_ts } = message;    const { userId, teamId } = context;    try {      await setTitle(message.text);      /**       * Set the status of the Assistant to give the appearance of active processing.       */      await setStatus({        status: 'thinking...',        loading_messages: [          'Teaching the hamsters to type faster…',          'Untangling the internet cables…',          'Consulting the office goldfish…',          'Polishing up the response just for you…',          'Convincing the AI to stop overthinking…',        ],      });...
```

## Respond to the user {#respond}

Your app can send a message back to the user, automatically clearing the status indicator in the Slack client. The status can also be cleared by again calling the `assistant.threads.setStatus` method with an empty string in the `status` field.

Formulate and send a response, using [text streaming](/ai/developing-agents#streaming). Three Web API methods work together to provide users a text streaming experience:

*   The [`chat.startStream`](/reference/methods/chat.startStream) method starts the text stream,
*   the [`chat.appendStream`](/reference/methods/chat.appendStream) method appends the text stream, and
*   the [`chat.stopStream`](/reference/methods/chat.stopStream) method stops it.

If you're a Python or JavaScript fan, our Bolt frameworks and SDKs in those languages have a streamer utility to allow you to quickly implement the functionality of these API methods into your apps.

### Text streaming {#streaming}

Text streaming is handled by three different API methods: [`chat.startStream`](/reference/methods/chat.startStream), [`chat.appendStream`](/reference/methods/chat.appendStream), and [`chat.stopStream`](/reference/methods/chat.stopStream). These allow the user to see the response from the LLM as a text stream, rather than a single block of text sent all at once. This provides closer alignment with expected behavior from other major LLM tools. The Bolt framework, available for [Python](/tools/bolt-python/concepts/message-sending/) and [JavaScript](/tools/bolt-js/concepts/message-sending), makes this process simpler.

When using text streaming, there are a couple of caveats to keep in mind. [Blocks](/block-kit) may be used in the `chat.stopStream` method, but not the `chat.startStream` or `chat.appendStream` method, in order to prevent having them broken up. Also, unfurling is disabled in streaming messages.

*   API call
*   Bolt for Python
*   Bolt for JS

Below is a sample of these API method requests. Refer to the method docs linked above for more implementation details.

Initiate a new streaming method with the [`chat.startStream`](/reference/methods/chat.startStream) API method. Use `task_display_mode` to control how tasks appear:

```
{  "channel": "D12345678",  "thread_ts": "1503435956.000248",  "task_display_mode": "plan",  "chunks": [    {      "type": "markdown_text",      "markdown_text": "Let me help you with that!"    }  ]}
```

Append chunks progressively to an existing streaming message with the [`chat.appendStream`](/reference/methods/chat.appendStream) API method:

```
{  "channel": "D12345678",  "message_ts": "1503435956.000247",  "thread_ts": "1503435956.000248",  "chunks": [    {      "type": "markdown_text",      "markdown_text": "Here's what I found..."    },    {      "type": "task_update",      "task": {        "task_id": "task_1",        "title": "Fetching weather data",        "status": "complete",        "output": {          "type": "rich_text",          "elements": [            {              "type": "rich_text_section",              "elements": [                {                  "type": "text",                  "text": "Found weather data from 1 source"                }              ]            }          ]        },        "sources": [          {            "type": "url",            "url": "https://weather.com/",            "text": "weather.com"          }        ]      }    }  ]}
```

Close the stream with the [`chat.stopStream`](/reference/methods/chat.stopStream) API method:

```
{  "channel": "D12345678",  "message_ts": "1503435956.000247",  "thread_ts": "1503435956.000248",  "chunks": [    {      "type": "markdown_text",      "markdown_text": "Hope this helps!"    }  ]}
```

Use the Bolt for Python `chat_stream()` utility to streamline (pun intended) all three API methods for streaming your app's messages. Refer to the [Bolt for Python docs](/tools/bolt-python/concepts/ai-apps/#text-streaming) for more details.

This code snippet is from the [AI Agent App Template](https://github.com/slack-samples/bolt-python-assistant-template).

listeners/assistant/message.py

```
import timefrom logging import Loggerfrom openai.types.responses import ResponseInputParamfrom slack_bolt import BoltContext, Say, SetStatusfrom slack_sdk import WebClientfrom slack_sdk.models.messages.chunk import (    MarkdownTextChunk,    PlanUpdateChunk,    TaskUpdateChunk,)from agent.llm_caller import call_llmfrom listeners.views.feedback_block import create_feedback_blockdef message(    client: WebClient,    context: BoltContext,    logger: Logger,    message: dict,    payload: dict,    say: Say,    set_status: SetStatus,):    """    Handles when users send messages or select a prompt in an assistant thread and generate AI responses:    Args:        client: Slack WebClient for making API calls        context: Bolt context containing channel and thread information        logger: Logger instance for error tracking        payload: Event payload with message details (channel, user, text, etc.)        say: Function to send messages to the thread        set_status: Function to update the assistant's status    """    try:        channel_id = payload["channel"]        team_id = context.team_id        thread_ts = payload["thread_ts"]        user_id = context.user_id        # The first example shows a message with thinking steps that has different        # chunks to construct and update a plan alongside text outputs.        if message["text"] == "Wonder a few deep thoughts.":            set_status(                status="thinking...",                loading_messages=[                    "Teaching the hamsters to type faster…",                    "Untangling the internet cables…",                    "Consulting the office goldfish…",                    "Polishing up the response just for you…",                    "Convincing the AI to stop overthinking…",                ],            )            time.sleep(4)            streamer = client.chat_stream(                channel=channel_id,                recipient_team_id=team_id,                recipient_user_id=user_id,                thread_ts=thread_ts,                task_display_mode="plan",            )            streamer.append(                chunks=[                    MarkdownTextChunk(                        text="Hello.\nI have received the task. ",                    ),                    MarkdownTextChunk(                        text="This task appears manageable.\nThat is good.",                    ),                    TaskUpdateChunk(                        id="001",                        title="Understanding the task...",                        status="in_progress",                        details="- Identifying the goal\n- Identifying constraints",                    ),                    TaskUpdateChunk(                        id="002",                        title="Performing acrobatics...",                        status="pending",                    ),                ],            )            time.sleep(4)            streamer.append(                chunks=[                    PlanUpdateChunk(                        title="Adding the final pieces...",                    ),                    TaskUpdateChunk(                        id="001",                        title="Understanding the task...",                        status="complete",                        details="\n- Pretending this was obvious",                        output="We'll continue to ramble now",                    ),                    TaskUpdateChunk(                        id="002",                        title="Performing acrobatics...",                        status="in_progress",                    ),                ],            )            time.sleep(4)            feedback_block = create_feedback_block()            streamer.stop(                chunks=[                    PlanUpdateChunk(                        title="Decided to put on a show",                    ),                    TaskUpdateChunk(                        id="002",                        title="Performing acrobatics...",                        status="complete",                        details="- Jumped atop ropes\n- Juggled bowling pins\n- Rode a single wheel too",                    ),                    MarkdownTextChunk(                        text="The crowd appears to be astounded and applauds :popcorn:"                    ),                ],                blocks=feedback_block,            )    except Exception as e:        logger.exception(f"Failed to handle a user message event: {e}")        say(f":warning: Something went wrong! ({e})")
```

Use the Bolt for JavaScript `chat_stream()` utility to streamline all three API methods for streaming your app's messages. Refer to the [Bolt for JavaScript docs](/tools/bolt-js/concepts/ai-apps/#text-streaming) for more details.

This code snippet is from the [AI Agent App Template](https://github.com/slack-samples/bolt-js-assistant-template).

listeners/assistant/message.js

```
import { callLLM } from '../../agent/llm-caller.js';import { feedbackBlock } from '../views/feedback_block.js';const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));/** * Handles when users send messages or select a prompt in an assistant thread * and generate AI responses. * * @param {Object} params * @param {import("@slack/web-api").WebClient} params.client - Slack web client. * @param {import("@slack/bolt").Context} params.context - Event context. * @param {import("@slack/logger").Logger} params.logger - Logger instance. * @param {import("@slack/types").MessageEvent} params.message - The incoming message. * @param {import("@slack/bolt").SayFn} params.say - Function to send messages. * @param {Function} params.setStatus - Function to set assistant status. * * @see {@link https://docs.slack.dev/reference/events/message} */export const message = async ({ client, context, logger, message, say, setStatus }) => {  /**   * Messages sent to the Assistant can have a specific message subtype.   *   * Here we check that the message has "text" and was sent to a thread to   * skip unexpected message subtypes.   *   * @see {@link https://docs.slack.dev/reference/events/message#subtypes}   */  if (!('text' in message) || !('thread_ts' in message) || !message.text || !message.thread_ts) {    return;  }  try {    const { channel, thread_ts } = message;    const { userId, teamId } = context;    // The first example shows a message with thinking steps that has different chunks to construct and update a plan alongside text outputs.    if (message.text === 'Wonder a few deep thoughts.') {      await setStatus({        status: 'thinking...',        loading_messages: [          'Teaching the hamsters to type faster…',          'Untangling the internet cables…',          'Consulting the office goldfish…',          'Polishing up the response just for you…',          'Convincing the AI to stop overthinking…',        ],      });      await sleep(4000);      const streamer = client.chatStream({        channel: channel,        recipient_team_id: teamId,        recipient_user_id: userId,        thread_ts: thread_ts,        task_display_mode: 'plan',      });      await streamer.append({        chunks: [          {            type: 'markdown_text',            text: 'Hello.\nI have received the task. ',          },          {            type: 'markdown_text',            text: 'This task appears manageable.\nThat is good.',          },          {            type: 'task_update',            id: '001',            title: 'Understanding the task...',            status: 'in_progress',            details: '- Identifying the goal\n- Identifying constraints',          },          {            type: 'task_update',            id: '002',            title: 'Performing acrobatics...',            status: 'pending',          },        ],      });      await sleep(4000);      await streamer.append({        chunks: [          {            type: 'plan_update',            title: 'Adding the final pieces...',          },          {            type: 'task_update',            id: '001',            title: 'Understanding the task...',            status: 'complete',            details: '\n- Pretending this was obvious',            output: "We'll continue to ramble now",          },          {            type: 'task_update',            id: '002',            title: 'Performing acrobatics...',            status: 'in_progress',          },        ],      });      await sleep(4000);      await streamer.stop({        chunks: [          {            type: 'plan_update',            title: 'Decided to put on a show',          },          {            type: 'task_update',            id: '002',            title: 'Performing acrobatics...',            status: 'complete',            details: '- Jumped atop ropes\n- Juggled bowling pins\n- Rode a single wheel too',          },          {            type: 'markdown_text',            text: 'The crowd appears to be astounded and applauds :popcorn:',          },        ],        blocks: [feedbackBlock],      });    }  } catch (e) {    logger.error(`Failed to handle a user message event: ${e}`);    await say(`:warning: Something went wrong! (${e})`);  }};
```

#### Display modes for streaming text {#display-modes-for-streaming-text}

Use blocks from Block Kit to help visualize the response. Tasks can then be displayed using [task card](/reference/block-kit/blocks/task-card-block) blocks along with the comprehensive [plan](/reference/block-kit/blocks/plan-block) display. Task cards display individual steps your agent is taking; a plan groups those tasks together.

Apps can display a [task update](/reference/methods/chat.appendStream#task_update-chunks) view for users to better understand what the app is doing. The task update display mode is best suited for short tasks with narration text. It can be in one of three different states: `in_progress`, `completed`, and `error`.

![Task update display mode](/img/guides/timeline.png)

The plan display mode uses the [plan block](/reference/block-kit/blocks/plan-block/) to present a list of tasks all together. It can be in one of four different states: `pending`, `in_progress`, `completed`, and `error`.

![Plan display mode](https://a.slack-edge.com/bf0a72a/img/api/partner_docs/thinking_steps/combined_plan.png)

### Feedback {#feedback}

With every message, provide an opportunity for feedback on the accuracy and helpfulness of the response with [interactive elements](/messaging/creating-interactive-messages), the [context actions block](/reference/block-kit/blocks/context-actions-block/), [icon button block](/reference/block-kit/block-elements/icon-button-element/), and [feedback button block](/reference/block-kit/block-elements/feedback-buttons-element/). You can also subscribe to [`reaction_added`](/reference/events/reaction_added) events so that when a user reacts to a message with an unfavorable reaction, you can collect feedback on it.

![Image of context block](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG0AAAAmCAMAAAD5ueXLAAAAD1BMVEX///9qaWq4uLjc3NySkZJWgBFNAAAACXBIWXMAAAsTAAALEwEAmpwYAAABQUlEQVR42u1VwZLFIAhLwP//4kL20J231Yrdmb6jOdWiICEgsLGxsfEeHH+0AMBcn3JGvcUFpEMAYzQNa0sHKdc6nKHc0hIAJQCiqY7m/JhJahErRcztlpTLSZKEWlbRTLi6MJVUUa7iNoRgYkiSZNlR0C7f6mrRUFTGEwkh/yOLZCeM1jN0QfhcAEhYQJQjnsN5uWrD6YpJC7hAiROlEIBdaM4qt8OkP7psdnMmGg4AtOS9fSYH5FEweZKVMD5xFMiVji4bOzHZaJZqCh+qMhrv1vZmECnn3XgyzCA8usLZ90ehFEg/RwR6Hb3JzcRZRU95ewiMHNN+g1JMhxPhvJM8dr8BFvWEfEjtU9LwyWU4UMOPNGchWxD6lWKs36UGSVq+b+z6eFoqgICFA1o2pefEB6sGitfq9C/42NjY2JjgB7Pii0Q9wJPWAAAAAElFTkSuQmCC)

A simple thumbs up/down reaction emoji will work, but consider opening a modal to collect more information when the response was graded poorly so that you can learn more about what the issue was.

*   API call
*   Bolt for Python
*   Bolt for JS

Here is an example of using the `context_actions` and `feedback_buttons` blocks to create a thumbs up/thumbs down section you can include in your app messages. To take action on the feedback, you will have to define what you'd like to happen when the button is clicked using a [`block_actions` payload](/reference/interaction-payloads/block_actions-payload).

```
{  "blocks": [    {      "type": "context_actions",      "elements": [        {          "type": "feedback_buttons",          "action_id": "feedback_buttons_1",          "positive_button": {            "text": {              "type": "plain_text",              "text": "👍"            },            "value": "positive_feedback"          },          "negative_button": {            "text": {              "type": "plain_text",              "text": "👎"            },            "value": "negative_feedback"          }        },      ]    }  ]}
```

View this in Block Kit Builder [here](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22context_actions%22,%22elements%22:%5B%7B%22type%22:%22feedback_buttons%22,%22action_id%22:%22feedback_buttons_1%22,%22positive_button%22:%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22%F0%9F%91%8D%22%7D,%22value%22:%22positive_feedback%22%7D,%22negative_button%22:%7B%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22%F0%9F%91%8E%22%7D,%22value%22:%22negative_feedback%22%7D%7D%5D%7D%5D%7D).

Additionally, you could include the icon button in messages to allow for deleting them. That block looks like this:

```
{  "blocks": [    {      "type": "context_actions",      "elements": [        {          "type": "icon_button",          "icon": "trash",          "text": {            "type": "plain_text",            "text": "Delete"          },          "action_id": "delete_button",          "value": "delete_item"        }      ]    }  ]}
```

View this in Block Kit Builder [here](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22context_actions%22,%22elements%22:%5B%7B%22type%22:%22icon_button%22,%22icon%22:%22trash%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Delete%22%7D,%22action_id%22:%22delete_button%22,%22value%22:%22delete_item%22%7D%5D%7D%5D%7D).

Use the Bolt for Python `blocks` utility to handle feedback interactions. Refer to the [Bolt for Python docs](/tools/bolt-python/concepts/ai-apps/#adding-and-handling-feedback) for more details.

```
from typing import Listfrom slack_sdk.models.blocks import Block, ContextActionsBlock, FeedbackButtonsElement, FeedbackButtonObjectdef create_feedback_block() -> List[Block]:    """    Create feedback block with thumbs up/down buttons    Returns:        Block Kit context_actions block    """    blocks: List[Block] = [        ContextActionsBlock(            elements=[                FeedbackButtonsElement(                    action_id="feedback",                    positive_button=FeedbackButtonObject(                        text="Good Response",                        accessibility_label="Submit positive feedback on this response",                        value="good-feedback",                    ),                    negative_button=FeedbackButtonObject(                        text="Bad Response",                        accessibility_label="Submit negative feedback on this response",                        value="bad-feedback",                    ),                )            ]        )    ]    return blocks
```

Refer to the [full docs](/tools/bolt-python/concepts/ai-apps/#adding-and-handling-feedback) to see the `chat_stream` and `handle_feedback` utilities carry out the full feedback flow.

Use the Bolt for JavaScript `blocks` utility to handle feedback interactions. Refer to the [Bolt for JavaScript docs](/tools/bolt-js/concepts/ai-apps/#adding-and-handling-feedback) for more details.

```
const feedbackBlock = {  type: 'context_actions',  elements: [    {      type: 'feedback_buttons',      action_id: 'feedback',      positive_button: {        text: { type: 'plain_text', text: 'Good Response' },        accessibility_label: 'Submit positive feedback on this response',        value: 'good-feedback',      },      negative_button: {        text: { type: 'plain_text', text: 'Bad Response' },        accessibility_label: 'Submit negative feedback on this response',        value: 'bad-feedback',      },    },  ],};
```

Refer to the [full docs](/tools/bolt-js/concepts/ai-apps/#adding-and-handling-feedback) to see the `chatStream` and `feedback` utilities carry out the full feedback flow.

### App threads {#threads}

By enabling the **Agents & AI Apps** feature in the [app settings](https://api.slack.com/apps), Slack will automatically group your app conversations into threads. You can set the title of these threads using the [`assistant.threads.setTitle`](/reference/methods/assistant.threads.setTitle) API method, or use the Bolt framework utility to handle the details.

*   API call
*   Bolt for Python
*   Bolt for JS

Here is a sample request for the API without using the Bolt framework. Refer to the [method docs](/reference/methods/assistant.threads.setTitle) for more implementation details.

```
{   "title": "Holidays this year",   "channel_id": "D123ABC456",   "thread_ts": "1786543.345678"}
```

Use the Bolt for Python `setTitle` utility to set the title of the app thread. Refer to the [Bolt for Python docs](/tools/bolt-python/concepts/ai-apps#handling-user-response) for more details.

```
assistant = Assistant()@assistant.thread_starteddef start_assistant_thread(    say: Say,    get_thread_context: GetThreadContext,    set_suggested_prompts: SetSuggestedPrompts,    logger: logging.Logger,):    try:        say("How can I help you?")        prompts: List[Dict[str, str]] = [            {                # Set the thread title here                "title": "Suggest names for my Slack app",                "message": "Can you suggest a few names for my Slack app? The app helps my teammates better organize information and plan action items.",            },        ]        thread_context = get_thread_context()        if thread_context is not None and thread_context.channel_id is not None:            summarize_channel = {                # Set the thread title here                "title": "Summarize the referred channel",                "message": "Can you generate a brief summary of the referred channel?",            }            prompts.append(summarize_channel)        set_suggested_prompts(prompts=prompts)    except Exception as e:        logger.exception(f"Failed to handle an assistant_thread_started event: {e}", e)        say(f":warning: Something went wrong! ({e})")
```

Use the Bolt for JavaScript `setTitle` utility to set the title of the app thread. Refer to the [Bolt for JavaScript docs](/tools/bolt-js/concepts/ai-apps#handling-user-response) for more details.

```
...threadStarted: async ({ event, logger, say, setSuggestedPrompts, saveThreadContext }) => {    const { context } = event.assistant_thread;    try {      await say('Hi, how can I help?');      await saveThreadContext();      if (!context.channel_id) {        await setSuggestedPrompts({          // Set the thread title here          title: 'Start with this suggested prompt:',          prompts: [            {              title: 'This is a suggested prompt',              message:                'When a user clicks a prompt, the resulting prompt message text ' +                'can be passed directly to your LLM for processing.\n\n' +                'Assistant, please create some helpful prompts I can provide to ' +                'my users.',            },          ],        });      }      if (context.channel_id) {        await setSuggestedPrompts({          // Set the thread title here          title: 'Perform an action based on the channel',          prompts: [            {              title: 'Summarize channel',              message: 'Assistant, please summarize the activity in this channel!',            },          ],        });      }    } catch (e) {      logger.error(e);    }  },...
```

### Messaging guidelines {#messaging-guidelines}

#### Block Kit and interactivity {#block-kit-and-interactivity}

Provide interactive [Block Kit](/block-kit) elements, such as drop-down menus and buttons, to allow your user to interact with the app. Block Kit is not required, however; you can forgo interactivity and message the user via plain text and Slack markdown.

When updating longer messages sent to a user, only call the [`chat.update`](/reference/methods/chat.update) method once every 3 seconds with new content, otherwise your calls may hit the rate limit.

You can also set a [section block element's](/reference/block-kit/blocks/section-block) `expand` property to `true` to allow your app to post long messages without the user needing to click 'see more' to see the full text of the message.

When not using Block Kit, use [Slack `mrkdwn`](/messaging/formatting-message-text#basic-formatting) for sending rich text. The formatting system of Slack is different from the common markup language used elsewhere on the web. It is typical for LLMs to default to use this common markdown syntax unless prompted otherwise, which will not render correctly when posted in Slack. Using the [Markdown Block](/reference/block-kit/blocks/markdown-block) with standard markdown entered as the `text` input will ensure Slack translates the formatting correctly.

#### Content disclaimers {#content-disclaimers}

Add a disclaimer at the footer of app messages indicating that the response was generated by an LLM (large language model) and provide any disclaimers that may be appropriate or applicable to communicate with the user. An example of this might sound something like:

> This content was generated by an LLM. Check generated content for vulnerabilities, and do not use to generate code that is visible outside of Slack. Review carefully before acting on the response; it may contain bias or hallucinations.

Implementing a content disclaimer

You can implement a disclaimer like this to each message by using a [context block](/reference/block-kit/blocks/context-block). Here is an example:

```
{    "type": "context",    "elements": [        {            "type": "mrkdwn",            "text": "This tool uses AI to generate responses, so some information may be inaccurate."        }    ]}
```

View this example in [Block Kit Builder](https://app.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22context%22,%22elements%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22This%20tool%20uses%20AI%20to%20generate%20responses,%20so%20some%20information%20may%20be%20inaccurate.%22%7D%5D%7D%5D%7D).

#### Media support {#media-support}

Where applicable, build apps that can handle a wide array of media types to provide the best user experience. Make it clear which media the app supports and gracefully fail when necessary. Refer to [working with files](/messaging/working-with-files) for this guidance.

For example, if a user sends an image file and your app does not support receiving images, reply with a message like this:

> It looks like the image didn't come through! 📸 Feel free to describe what you need help with, and I'll do my best to assist you. 😊

#### Sending notifications {#sending-notifications}

When your app has the Agents & AI Apps feature toggled on, every DM with the user is a thread.

When sending a notification to a user outside of an existing thread:

1.  Use the [`chat.postMessage`](/reference/methods/chat.postMessage) method as normal, but look for the `ts` parameter in the response.
2.  Call the [`assistant.threads.setTitle`](/reference/methods/assistant.threads.setTitle) method, sending the new `ts` parameter as the `thread_ts` parameter to set the title of the thread. This allows a user to see the new notification with a titled thread when they view the app's DM.

When a user navigates to your app, two tabs are available. The **History** tab is all of the past threads (in which the user has sent a message); this is where they will see new notifications. The **Chat** tab is the last active thread between the user and your app.

Slack has the **Activity** side rail tab to show new activity in a workspace. This area is optimized for users to quickly see and respond to notifications from your app.

#### References, citations, and annotations {#references-citations-and-annotations}

Sources and attribution should be used and displayed consistently. There should be a concise way to reference internal messages and files from external sources. We recommend including these in each response that cited a source or used knowledge from a message or document to generate the output. Doing so builds trust with your app's users.

Implementing references

Use [link formatting](/messaging/formatting-message-text#linking-urls) to cite sources inline and a [context block](/reference/block-kit/blocks/context-block) to list references at the end of the message. To avoid clutter in the response, you may want to [suppress unfurls](/reference/methods/chat.postMessage#unfurling) if there are several sources.

Here is an example of citing a source in a context block that you could include at the end of a message:

```
{    "type": "context",    "elements": [        {            "type": "mrkdwn",            "text": "Slack stands for 'Searchable Log of All Conversation and Knowledge.' <https://app.slack.com/slackhelp/en-US/115004071768|[1 Help Center]>"        }    ]}
```

View this example in [Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22context%22,%22elements%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22Slack%20stands%20for%20'Searchable%20Log%20of%20All%20Conversation%20and%20Knowledge.'%20%3Chttps://app.slack.com/slackhelp/en-US/115004071768%7C%5B1%20Help%20Center%5D%3E%22%7D%5D%7D%5D%7D).

#### Graceful errors {#graceful-errors}

Graceful failure means the agent treats its own partial progress as something worth preserving.

Agents make mistakes, they make things up, they omit important details and get stuck in endless loops of thinking. These situations can happen fairly often, and designing for them is a critical part of building a good agent experience.

When an agent experiences an error, it should:

*   Save what it's accomplished
*   Explain where it got stuck and why
*   Give the user a clear set of options, including:
    *   provide the missing information
    *   skip the blocked step
    *   or take over manually from a known state.

As a last resort, clear the status so the app is not stuck 'thinking' indefinitely. It's important for the user to know when there are errors beyond their control and they need to try again or report a bug.

Something as simple as sending a message like this can go a long way for a user understanding why something isn't working:

> Ope sorry! TeamworkDreamwork App isn't enabled for you.

Implementing graceful error handling

This will vary based on the types of errors you handle, but you can clear a status by calling the [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus) method and sending an empty string in the `status` field.

## Full example {#full-example}

Here is a full code example of the response loop.

Complete pattern example

```
app.event('app_mention', async ({ event, client }) => {  const channel = event.channel;  const threadTs = event.thread_ts ?? event.ts;  const userQuery = (event.text || '').trim();  // 1. Set status immediately for instant feedback  await client.assistant.threads.setStatus({    channel_id: channel,    thread_ts: threadTs,    status: 'Searching...'  });  // 2. Open stream with plan mode  const stream = await client.chat.startStream({    channel,    thread_ts: threadTs,    task_display_mode: 'plan'  });  // 3. Send plan to user  await client.chat.appendStream({    channel,    ts: stream.ts,    chunks: [      { type: 'task', id: 'search', text: 'Search workspace', status: 'in_progress' },      { type: 'task', id: 'build', text: 'Build context', status: 'pending' },      { type: 'task', id: 'compose', text: 'Compose response', status: 'pending' }    ]  });  // 4. Search workspace for relevant context  const searchResult = await client.assistant.search.context({    query: userQuery,    action_token: event.action_token,    content_types: ['messages', 'files', 'channels'],    channel_types: ['public_channel', 'private_channel'],    include_context_messages: true,    limit: 20  });  // 5. Update plan state for human in the loop  await client.chat.appendStream({    channel,    ts: stream.ts,    chunks: [      { type: 'task', id: 'search', text: 'Search workspace', status: 'complete' },      { type: 'task', id: 'build', text: 'Build context', status: 'in_progress' }    ]  });  // 6. Optionally drill into the top result's thread for full context  const topMatch = searchResult.results?.messages?.[0];  let threadReplies = [];  if (topMatch) {    const repliesResult = await client.conversations.replies({      channel: topMatch.channel_id,      ts: topMatch.message_ts,      limit: 100    });    threadReplies = repliesResult.messages || [];  }  // 7. Build structured state  const state = {    goal: userQuery,    constraints: '',    decisions: [],    artifacts: [],    sources: (searchResult.results?.messages || []).map((m) => ({      text: m.content,      link: m.permalink    }))  };  // 8. Update plan for human in the loop  await client.chat.appendStream({    channel,    ts: stream.ts,    chunks: [      { type: 'task', id: 'build', text: 'Build context', status: 'complete' },      { type: 'task', id: 'compose', text: 'Compose response', status: 'in_progress' }    ]  });  // 9. Build context block and call LLM  const sourceContext = state.sources.map((s) => `• ${s.text} (${s.link})`).join('\n');  const threadContext = threadReplies.length > 0    ? `\nFull thread:\n${threadReplies.map((m) => m.text).join('\n')}`    : '';  const contextBlock = sourceContext + threadContext;  const completion = await llm.responses.create({    model: 'gpt-4.1-mini',    input: `Goal: ${state.goal}\n\nRelevant context:\n${contextBlock}\n\nRespond with JSON only: { "summary": "one sentence", "findings": ["string"], "decisions": ["string"], "next_actions": ["string"] }`  });  const parsed = JSON.parse(completion.output_text);  state.decisions = parsed.decisions || [];  state.artifacts.push({ type: 'summary', text: parsed.summary });  // 10. Map structured response to Block Kit  const listSection = (label, items) => ({    type: 'section',    text: { type: 'mrkdwn', text: `*${label}*\n${items.map((i) => `• ${i}`).join('\n')}` }  });  const actions = [    { type: 'button', text: { type: 'plain_text', text: 'Run again' }, action_id: 'run_again' },    { type: 'button', text: { type: 'plain_text', text: 'Refine search' }, action_id: 'refine_search' },    { type: 'button', text: { type: 'plain_text', text: 'Share summary' }, action_id: 'share_summary', style: 'primary' }  ];  const blocks = [{ type: 'header', text: { type: 'plain_text', text: parsed.summary } }];  if (parsed.findings?.length > 0) blocks.push(listSection('Findings', parsed.findings));  if (parsed.decisions?.length > 0) blocks.push(listSection('Decisions', parsed.decisions));  if (parsed.next_actions?.length > 0) blocks.push(listSection('Next actions', parsed.next_actions));  blocks.push({ type: 'divider' });  if (state.sources.length > 0) {    blocks.push({      type: 'context',      elements: state.sources.slice(0, 3).map((s) => ({ type: 'mrkdwn', text: `<${s.link}|Source>` }))    });  }  blocks.push({ type: 'actions', elements: actions });  await client.chat.stopStream({ channel, ts: stream.ts, text: parsed.summary, blocks });  await client.assistant.threads.setStatus({    channel_id: channel,    thread_ts: threadTs,    status: ''  });});
```

On follow-up turns, pass the existing `state` object to the LLM and update individual fields as the conversation evolves — do not call `assistant.search.context` again unless the goal has changed.

## Additional guidelines {#guidelines}

### Data retention {#data-retention}

Do not store any Slack data you obtain. Instead, store metadata and pull in data in real time if needed.

### Members only {#members-only}

Workspace guests are not permitted to access apps with the Agents & AI Apps feature enabled.

## More ways to add AI to your app {#more-ai}

Can't get enough AI in the agent experience? Any user input can be used as input for an LLM query, and the answer can be posted back in Slack. Take these three examples:

*   Ask an LLM a question that was reacted to with a reacji. Learn how to do this in the [Events API docs](/apis/events-api#try-it-with-ai)
*   Initiate asking an LLM a question posed in a message from a [message shortcut](/interactivity/implementing-shortcuts#try-it-with-ai)
*   Start off an LLM query with a [slash command](/interactivity/implementing-slash-commands#try-it-with-ai)
*   Collect structured data in a [modal](/surfaces/modals#try-it-with-ai), then use it in a query to an LLM

Remember to enable the Agents & AI Apps feature toggle to gain access to the [`assistant:write`](/reference/scopes/assistant.write) scope, which is required for calling assistant-related methods like [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus).

AI-enabled apps and prompt injection

Integrating with AI carries an inherent risk of prompt injection. Read more about the risk of data exfiltration and how to prevent it in the [security](/security#prompt-injection) docs.

## Next steps {#next-steps}

✨ Integrate the [Slack MCP server](/ai/slack-mcp-server) to access Slack data and perform user-authorized actions in your app.

✨ Get started with an agent template in [Bolt for Python](https://github.com/slack-samples/bolt-python-assistant-template) or [Bolt for JavaScript](https://github.com/slack-samples/bolt-js-assistant-template).

✨ Build an AI-fueled Code Assistant app using Bolt for JavaScript with [this tutorial](/tools/bolt-js/tutorials/code-assistant).