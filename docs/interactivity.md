Source: https://docs.slack.dev/interactivity

# Interactivity overview

Both Bolt apps and apps created using the Deno Slack SDK can be invoked automatically (like a scheduled message) or by a user (like by clicking a shortcut). All Slack apps can also use interactive features to achieve much more than just one-way communication.

An injection of interactivity invites and inspires action (and reaction). Best of all, users never have to depart from the comfort of Slack to get things done.

The interactive flow between Slack apps and users is a two-step process:

1.  Something happens that [**invokes**](#triggers) the app or interaction.
2.  The app [**responds**](#responses) to the interaction.

There are multiple ways to invoke apps and interactions, and apps have multiple ways to respond.

* * *

## Invoking apps {#triggers}

There are several potential ways that app invocations are triggered. They can be divided into two categories:

*   [**Automatic invocations**](#automatic). Apps choose to invoke the interaction.
*   [**User invocations**](#user). Users choose to invoke the interaction.

### Automatic invocations {#automatic}

Your app can be invoked without any direct user input. Let users focus while your app handles what it needs to on its own.

#### Scheduled interactions {#scheduled-interactions}

The interaction is invoked at a specific time with a specific cadence.

For example, on every Friday at 3pm an app could post a reminder.

➡️ To achieve this with an app created with the Deno Slack SDK, check out the guide to [scheduled triggers](/tools/deno-slack-sdk/guides/creating-scheduled-triggers).

➡️ To achieve this with a Bolt app, check out the [Send or schedule a message](/messaging/sending-and-scheduling-messages) guide.

#### Interactions initiated by external services {#interactions-initiated-by-external-services}

Connections you've built with external services can trigger app interactions at any time. This provides seamless integration from those services into Slack.

For example, an account update on a CRM platform could cause a Slack app to post a Slack message.

➡️ To achieve this with an app created with the Deno Slack SDK, check out the guide to [webhook triggers](/tools/deno-slack-sdk/guides/creating-webhook-triggers).

➡️ To achieve this with a Bolt app, check out the [Sending messages using incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) page.

#### Interactions initiated by the Events API {#interactions-initiated-by-the-events-api}

The [Events API](/apis/events-api/) can send a push to Slack apps whenever a specific event occur in Slack. The receipt of one of these event pushes can trigger some interaction response by an app.

For example, the [`app_mention`](/reference/events/app_mention) event sends a push when an app is mentioned by someone in a conversation. The app could then respond with a message.

➡️ To achieve this with an app created with the Deno Slack SDK, check out the guide to [event triggers](/tools/deno-slack-sdk/guides/creating-event-triggers).

➡️ To achieve this with a Slack app, check out the guide to the [Events API](/apis/events-api/).

* * *

### User invocations {#user}

Users can directly invoke your app via _entry points_—a set of app features that serve as launching points for interactions. Most user invocations will send data payloads to an app containing contextual information about the interaction. These types of actions can further be used to interact with the app beyond the initial invocation, achieving a sort of back-and-forth interaction between the user and the app.

Enable these configurable features to provide users a way to invoke and interact with apps from the comfort of familiar Slack client elements.

#### Shortcuts {#shortcuts}

Shortcuts let users quickly trigger workflows from various prominent UI locations in Slack.

➡️ Refer to [Link triggers](/tools/deno-slack-sdk/guides/creating-link-triggers) for more info on using shortcuts, or rather, link triggers, with an app created with the Deno Slack SDK.

➡️ Refer to [Shortcuts](/interactivity/implementing-shortcuts) for more info for using shortcuts with a Slack app.

![](/assets/images/global_shortcuts-e647f5c4f57d1b4213590241b991235a.svg)

#### Slash commands {#slash commands}

Let users trigger an interaction with your app by typing a command into the message composer box in any Slack conversation.

➡️ Slash commands in apps created with the Deno Slack SDK are used simply as another entry point. Read more about it [here](/faq#slashcommands).

➡️ Refer to [Slash commands](/interactivity/implementing-slash-commands) for more info on using this invocation as well as the many other uses of slash commands in a Slack app.

#### Block Kit interactive components {#block-kit-interactive-components}

Interactive components are a subset of [Block Kit](/block-kit), our UI framework of visual components for Slack apps. They can be placed into [app surfaces](/surfaces) like [messages](/messaging), [modals](/surfaces/modals), or [App Home](/surfaces/app-home). Each component provides its own trigger for a possible interaction.

➡️ Refer to [Building with Block Kit](/block-kit) for more info.

![](/assets/images/bk_landing_bkb-e64c290c97543b50e0b09c0b291c7c78.png)

* * *

## Responding to interactions {#responses}

An app's reaction to an interaction can take on many forms, ranging from doing nothing at all, to performing one of the many [API functions](/apis) available to Slack apps.

Some possibilities:

*   [Send messages](/messaging) using [Web APIs](/apis/web-api/) with a Slack app or using [built-in Slack functions](/tools/deno-slack-sdk/guides/creating-slack-functions) with an app created with the Deno Slack SDK.
    
*   Create, archive, and manage conversations using [conversation-specific Web APIs](/apis/web-api/using-the-conversations-api).
    
*   Open [modals](/surfaces/modals) to collect info and provide a space for displaying dynamic details. Check out [our tutorial on using them with the Bolt for Python framework](/tools/bolt-python/tutorial/modals) or using them in [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/guides/creating-an-interactive-modal).
    

Read our [guide to designing your Slack app](/surfaces/app-design) for some interactivity inspiration.

All interactivity payloads can be found in the [Reference: interaction payloads](/reference/interaction-payloads) documentation.

## Implementing infinite interactions {#chaining}

Responses to interactions can themselves be invocations of further interaction.

Some examples:

*   An [interactive message](/messaging) could be published in response to a schedule, and a button within that message could be clicked to continue a workflow.
    
*   A [shortcut](/interactivity/implementing-shortcuts) could trigger a [modal](/surfaces/modals) that, once completed, could trigger an update of the app's [Home tab](/surfaces/app-home).
    

Chaining interactions together creates workflows that can accomplish complex tasks.

Ready to add interactivity to your app? Next stop is [Handling user interaction in your Slack apps](/interactivity/handling-user-interaction) for Slack apps or start with [Creating a form](/tools/deno-slack-sdk/guides/creating-a-form) for apps created with the Deno Slack SDK.