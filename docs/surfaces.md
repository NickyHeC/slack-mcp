Source: https://docs.slack.dev/surfaces

# Surfaces

Create welcoming spaces for people to use your Slack app on a variety of surfaces. **Surfaces** are places where your app can express itself through communication or interaction with your users.

Most surfaces can be built using [Block Kit](/block-kit) layout blocks and elements. Our [guide to building block layouts](/block-kit) will help you learn how. Canvases, on the other hand, use [markdown](/messaging/formatting-message-text#basic-formatting) for content formatting.

* * *

## App Home {#app-home}

The App Home is a private, one-to-one space in Slack shared by a user and an app. The Home tab, a specific App Home view, is an optional ever-present space, retaining its content and state until the app chooses to update it.

Present each of your users with a unique Home tab just for them, always found in the same place.

Although not every app needs to have a Home tab, the 'always-on' nature of the space makes it an important surface for many Slack apps.

The App Home is not available for apps created with the Deno Slack SDK.

![](/assets/images/app_home_abstract-f4c341508b05b02d5fb0aac5a7ad61ba.png)

➡️ **To get started with App Home**, read our [App Home guide](/surfaces/app-home).

* * *

## Canvases {#canvases}

Canvases are built-in documents in Slack, existing either tied to a channel or as a standalone space.

Use canvases to store channel guidelines or instructions, welcome new team members with an onboarding flow, or present project updates with canvases. Add links to team resources, helpful videos, and even kick off a workflow from a canvas.

![](/assets/images/canvas-5260e8e383df4e487e8bfca3c8883b24.png)

➡️ **To get started with canvases**, read our [Canvas guide](/surfaces/canvases).

* * *

## Lists {#lists}

Lists help you organize and collaborate on work happening in Slack.

Use Lists to manage tasks, check the status of project work, and more.

![](/assets/images/lists-bc547b497580bd64f82e996a24d2bcfc.png)

➡️ **To get started with Lists**, read our [Lists guide](/surfaces/lists).

* * *

## Messages {#messages}

App-published messages are dynamic yet transient spaces. They allow users to complete workflows as Slack conversations.

Apps can [send messages](/messaging) whenever they want to, as long as they have the relevant permissions and access. Our [guide to formatting text for app surfaces](/messaging/formatting-message-text) will show you what formatting is possible.

When an app is invoked, it can respond with a message. Further action can flow from that message, forming a conversational interface connected to any of Slack's features.

![](/assets/images/message-abstract-06be210d128e91ff97e3ca6d791ef7d9.png)

➡️ **To get started with messages**, read our [Messages guide](/messaging).

✨ **To level up your messages with interactive components such as buttons and select menus**, read our Creating interactive messages guide for traditional [Slack apps](/messaging/creating-interactive-messages) or [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/guides/creating-an-interactive-message).

* * *

## Modals {#modals}

Modals are prominent and pervasive spaces ideal for requesting and collecting data from users, or temporarily displaying dynamic and interactive information.

Modals appear in front of any other interface element in Slack. As a result, they are short-lived and invoked only when a specific task is to be completed. Apps can _only_ create modals in response to [user invocation](/interactivity#user), such as a [shortcut](/interactivity/implementing-shortcuts).

Modals contain one to three [**views**](/surfaces/modals#lifecycle) that can be chained together to create complex, non-linear workflows.

![](/assets/images/modal-abstract-f84c7b1e74a116b1376d94dd07121db0.png)

➡️ **To get started with modals**, read our [Modals guide](/surfaces/modals).

* * *

## Split view {#split-view}

The split view surface enables an AI chat experience. Along with the side-by-side view within Slack, the feature set that enables the split view also replaces the typical Messages tab for a Chat and History tab. This view is enabled with the Agents & AI Apps feature toggle found in [app settings](https://api.slack.com/apps).

![Image of split view](/img/guides/ai_container/splitview.png)

➡️ **To get started with split view**, read our [Split view guide](/surfaces/split-view).

* * *

## Using app surfaces together {#next}

App surfaces can also be used together to create a rich interactive experience for your users. For example, imagine the following Task App, which presents a task dashboard that resides in the app's [Home tab](/surfaces/app-home):

1.  A user can click a [button](/reference/block-kit/block-elements/button-element) to add a task.
2.  The user is then presented with a [modal](/surfaces/modals) to [enter](/reference/block-kit/blocks/input-block) some [plain text](/reference/block-kit/block-elements/plain-text-input-element) and [select from a list of categories](/reference/block-kit/block-elements/select-menu-element).
3.  Upon submitting, a [message](/messaging) is sent to a triage channel elsewhere in Slack.
4.  Finally, a different user in the triage channel can click a [button](/reference/block-kit/block-elements/button-element) to claim that task.

Explore all the possibilities and get some tips and inspiration by reading our [guides to planning Slack apps](/surfaces/app-design).