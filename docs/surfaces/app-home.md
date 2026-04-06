Source: https://docs.slack.dev/surfaces/app-home

# App Home

The App Home is a private, one-to-one space in Slack shared by a user and an app. It is only available in granular permission Slack apps, not [slack apps created with the Deno Slack SDK](/tools/deno-slack-sdk/). Each App Home can contain three tabbed views:

*   **[The Home tab](#home-tab)** — a fully customizable space enriched with [Block Kit](/block-kit) layouts and interactivity.
    
*   **[The Messages tab](#messages-tab)** — the app-user conversation, taking advantage of all the typical Slack [messaging features](/messaging).
    
*   **[The About tab](#about-tab)** — the descriptive info about the app.
    

![](/assets/images/app_home_abstract-f4c341508b05b02d5fb0aac5a7ad61ba.png)

This guide details how to utilize all three tabs of App Home. Jump to whichever tab you want to focus on, or read through everything App Home.

Regardless, you'll need a Slack app before you can begin. If you don't already have one, click the button below:

[Create an app](https://api.slack.com/apps?new_app=1)

* * *

## Using the Home tab {#home-tab}

An app's Home tab can be published and updated at the app's whim. You can publish a single table design to all the app's users, or provide personalized dynamic tabs that updates upon interaction.

This combination of a _fixed location_ for a _persistent interface_ with _dynamic contents_ enables a huge range of use cases for Slack apps.

Some ways you can make use of the Home tab:

*   Onboard users to your app
*   Display dashboards and other personalized user data
*   Surface app settings
*   Authenticate users to 3rd party apps
*   Alert users of app updates

As you design your Home tab, consider the following:

*   **Present users information that is _most relevant for them_.**
    
    For example, if you’re building a ticketing app, users will likely want to see open tickets assigned to them. Think about how to organize information for users in a customized, accessible way.
    
*   **The most important content should shine at the top of your Home tab.**
    
    This includes entry points to invoke your app’s core functionality alongside useful information that users will want to access most often. Employ the use content dividers when considering what actions and information is important to the user, versus what could be expressed as secondary, or hidden behind a modal.
    
*   **Show app settings**
    
    A good rule of thumb is to present app settings in your Home tab [behind a button](/reference/block-kit/block-elements/button-element). Settings are specific to your app, and different users may have specialized settings — for example, admins may be able to control workspace-wide settings whereas standard users should not have access to this.
    
    Block Kit Builder's [calendar template](https://api.slack.com/tools/block-kit-builder?template=calendar) is an exceptional example of exposing settings in your app's Home tab.
    
*   **Curate call-to-actions**
    
    To avoid bombarding a user with too many call-to-actions, consider limiting the amount of actions a user can take in your Home tab. If actions are essential to your app’s experience, look into overflow menus to help hide the less-essential actions and focus on what the majority of your users will want to accomplish within your Home tab. This section will take you through the steps necessary to publish and update an app's Home tab for a user at any time.
    

### 1. Preparing your app to use Home tab {#enabling}

To start using your app's Home tab, you'll need to set up a few things in app management.

#### Request necessary permissions {#permissions_setup}

Your app needs at least one permission scope to enable the Home tab. It doesn't matter _which_ scope, but if you want your app to also use the [Messages tab](#messages-tab) you'll need to add the [`chat:write`](/reference/scopes/chat.write) anyway.

To add a scope:

1.  Go to your [app's management dashboard](https://api.slack.com/apps).
2.  Click _OAuth & Permissions_ in the sidebar.
3.  Select a scope under _Bot token scopes_.

#### Enable Home tab {#tab_setup}

With a scope added, you can now enable the Home tab.

To enable the Home tab:

1.  Go to your [app's management dashboard](https://api.slack.com/apps).
2.  Click on _App Home_ in the sidebar.
3.  Under _Show Tab_, switch on the _Home tab_ toggle.

This page is also where you can choose to disable the Messages tab, if you wish.

#### Install your app {#install}

Now you'll need to install your app. For [Single workspace apps](/app-management/distribution):

1.  Click on _Install App_ in the sidebar.
2.  Click _Install to Workspace_. If you have previously installed it, click _Reinstall to Workspace_.
3.  Click _Allow_ to grant the app access to your workspace.

Once your app is installed, grab the [_Bot User OAuth Access Token_](/authentication/tokens#granular_bot). You can find it on the _OAuth & Permissions_ page. You'll need to use it later.

Your app's Home tab will now appear within your [App Home](/surfaces/app-home#where), but it will be empty. Let's change that.

### 2. Composing a view {#composing}

The Home tab is composed of a single [**view**](/reference/views) that can contain up to 100 [**blocks**](/block-kit).

That view object is a JSON object that contains a `blocks` array that defines the layout composition, alongside other fields.

#### Home tab view object fields {#view-fields}

Field

Type

Description

`type`

String

Required. The type of view. Set to `home` for Home tabs.

`blocks`

Array

Required. An array of [blocks](/reference/block-kit/blocks) that defines the content of the view. Max of 100 blocks.

`private_metadata`

String

An optional string that will be sent to your app in `view_submission` and `block_actions` events. Max length of 3000 characters.

`callback_id`

String

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Max length of 255 characters.

`external_id`

String

A custom identifier that must be unique for all views on a per-team basis.

If you use non-standard characters (including characters with diacritics), please be aware that these are converted and sent in unicode format when you receive the view callback payloads.

In our example below, we're creating a view containing text and an image.

```
{  "type": "home",  "blocks": [    {      "type": "section",      "text": {        "type": "mrkdwn",        "text": "This is a Block Kit example"      },      "accessory": {        "type": "image",        "image_url": "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",        "alt_text": "calendar thumbnail"      }    }  ]}
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder/#%7B"type":"home","blocks":%5B%7B"type":"section","text":%7B"type":"mrkdwn","text":"This%20is%20a%20Block%20Kit%20example"%7D,"accessory":%7B"type":"image","image_url":"https://api.slack.com/img/blocks/bkb_template_images/notifications.png","alt_text":"calendar%20thumbnail"%7D%7D%5D%7D)

### 3. Publishing a view to your Home tab {#publishing}

After designing the view object, use the [`views.publish`](/reference/methods/views.publish) method to publish the content to the Home tab.

There are three required arguments. Here's how to use them for our example:

*   `token` - This is the [bot token](/authentication/tokens#granular_bot) we asked you to make note of [earlier](#install).
*   `user_id` - For this example, this is _your_ user ID. You can find this within Slack by opening your profile, clicking on the ":" button and choosing "Copy member ID". Beyond this example, apps can get a user's ID programmatically by subscribing to the [`app_home_opened`](/reference/events/app_home_opened) event, from [interaction payloads](/interactivity/handling-user-interaction) or from the many other places you can encounter a `user_id`.
*   `views` - This is the view object JSON object [created in the previous step](#composing).

Now make the call to `views.publish` with the above values:

```
POST https://slack.com/api/views.publishContent-type: application/jsonAuthorization: Bearer YOUR_TOKEN_HERE{  "user_id": "YOUR_USER_ID",  "view": {    "type": "home",    "blocks": [      {        "type": "section",        "text": {          "type": "mrkdwn",          "text": "This is a Block Kit example"        },        "accessory": {          "type": "image",          "image_url": "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",          "alt_text": "calendar thumbnail"        }      }    ]  }}
```

If your API call was a success, you'll get a success response containing `ok: true`.

Navigate to your App Home within Slack, click on the Home tab, and you'll see your newly created layout.

### 4. Updating your Home tab {#updating}

Updating a Home tab also uses the [`views.publish`](/reference/methods/views.publish) method. Providing a new `blocks` array will update the view accordingly.

In this example, we've added a new [block element](/reference/block-kit/block-elements): a button. A button is a Block Kit _interactive component_.

```
POST https://slack.com/api/views.publishContent-type: application/jsonAuthorization: Bearer YOUR_TOKEN_HERE{  "user_id": "YOUR_USER_ID",  "view": {    "type": "home",    "blocks": [      {        "type": "section",        "text": {          "type": "mrkdwn",          "text": "This is a Block Kit example"        },        "accessory": {          "type": "image",          "image_url": "https://api.slack.com/img/blocks/bkb_template_images/notifications.png",          "alt_text": "calendar thumbnail"        }      },      {        "type": "actions",        "elements": [          {            "type": "button",            "text": {              "type": "plain_text",              "text": "Click Me",              "emoji": true            },            "value": "click_me_123",            "action_id": "actionId-0"          }        ]      }    ]  }}
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder/#%7B"type":"home","blocks":%5B%7B"type":"section","text":%7B"type":"mrkdwn","text":"This%20is%20a%20Block%20Kit%20example"%7D,"accessory":%7B"type":"image","image_url":"https://api.slack.com/img/blocks/bkb_template_images/notifications.png","alt_text":"calendar%20thumbnail"%7D%7D,%7B"type":"actions","elements":%5B%7B"type":"button","text":%7B"type":"plain_text","text":"Click%20Me","emoji":true%7D,"value":"click_me_123","action_id":"actionId-0"%7D%5D%7D%5D%7D)

Make this API call, and your Home tab will update automatically to reflect the new content.

In a real world context, apps will likely need to store the `user_id` of the Home tab user, along with any relevant customizations for individual users. This is because Home tab updates can happen when a user isn't interacting with Slack or the app — for example if a Home tab update was triggered by an external service.

### Next steps: adding interactivity {#interactivity}

If you try clicking on the button in the created example Home tab, you'll see that they don't do anything other than display an error icon. That's because even though you can publish Block Kit interactive components without enabling interactivity, users won't be able to use them. See the [user interactivity guide](/interactivity/handling-user-interaction) for instructions.

Take a deeper dive into [Block Kit](/block-kit) and find out about the full range of [blocks](/reference/block-kit/blocks) and [block elements](/reference/block-kit/block-elements) available to use in Home tabs.

You can also browse [onboarding templates](https://api.slack.com/tools/block-kit-builder?template=1) in Block Kit Builder.

* * *

## Using the Messages tab {#messages-tab}

The _Messages_ tab in an App Home provides a space for the app and user to converse.

### Request necessary permissions {#permissions_setup}

Your app needs the [`chat:write`](/reference/scopes/chat.write) [permission scope](/authentication/installing-with-oauth) to use the Messages tab, and the [`im:history`](/reference/scopes/im.history) scope to respond to messages.

To add the scope:

1.  Go to your [app's management dashboard](https://api.slack.com/apps).
2.  Click _OAuth & Permissions_ in the sidebar.
3.  Select a scope under _Bot token scopes_.
4.  Add _chat:write_.
5.  Add _im.history_ (Optional).

### Enable Messages tab {#enable-messages}

Then you can enable the Messages tab. To do so:

1.  Go to your [app's management dashboard](https://api.slack.com/apps).
2.  Click on _App Home_ in the sidebar.
3.  Under _Show Tab_, switch on the _Messages tab_ toggle.

AI-enabled apps

If you choose to use the **Agents & AI Apps** feature toggle (found in your [app settings](https://api.slack.com/apps), the Messages tab will be replaced with Chat and History tabs.)

### Subscribe to message.im events {#subscribe-messages}

Your app must also subscribe to the [`message.im`](/reference/events/message.im) event so it can respond to messages.

To do so:

1.  Go to your [app's management dashboard](https://api.slack.com/apps).
2.  Click on _Event Subscriptions_.
3.  Make sure _Enable Events_ is toggled on.
4.  Under _Subscribe to bot events_, click _Add Bot User Event_.
5.  Add _message.im_.
6.  Click _Save Changes_.

You'll then receive an [Events API](/apis/events-api/) notification for every message sent to your app via the Messages tab.

Your app can then choose to respond to those messages in whatever way you see fit. Some ideas:

*   The `user` and `channel` IDs found in the `app_home_opened` event can be used as the `channel` parameter when calling the [`chat.postMessage`](/reference/methods/chat.postMessage) method to publish a message.
*   An [incoming webhook](/messaging/sending-messages-using-incoming-webhooks) can be created for the Messages tab conversation.
*   [Message responses](/interactivity/handling-user-interaction#message_responses) can be created when a valid [`request_url`](/interactivity/handling-user-interaction#message_responses) is received.

### Next steps: customizing messages {#next-steps-messages}

Read our [guides to messaging for Slack apps](/messaging) for more details on how to enrich your app's messages with rich layouts and interactivity.

* * *

## Using the About tab {#about-tab}

The About tab displays basic information about your app. Here, users can view:

*   The app name
*   The app icon
*   A short description about the app
*   And a few other specific details about the app

To tweak the About tab for your app:

1.  Go to your [app's management dashboard](https://api.slack.com/apps).
2.  Click _Basic Information_ in the sidebar.
3.  Go to _Display Information_.
4.  Make any desired changes.
5.  Click _Save Changes_.

* * *

## Detecting App Home visitors {#opened}

The [`app_home_opened`](/reference/events/app_home_opened) event is accurately named — it tells your app when the user has opened the App Home. Your app can listen for this event and respond accordingly.

A payload will be delivered to your app via the [Events API](/apis/events-api/), containing actionable and contextual information about the event. This information will include the user that opened the App Home, the workspace that the event happened in, and more. Here's an example:

```
{    "type": "app_home_opened",    "user": "U123ABC456",    "channel": "D123ABC456",    "event_ts": "1515449522000016",    "tab": "home",    "view": {        ...    }}
```

Your app can use this contextual information in its response to the user.

For example, the `event_ts` field is a timestamp dated that identifies within a few seconds when the user opened the window. Your app might store this, along with the `user` and `channel` IDs, so you can keep track of when, if ever, your app last interacted with a user in your App Home.

If you need more information about the user and have the appropriate scopes, use [`users.info`](/reference/methods/users.info). If you need more information about the conversation that forms the App Home **Messages** tab, use [`conversations.info`](/reference/methods/conversations.info).

### Responding to an App Home visit {#respond}

A user opening your App Home represents clear intent or interest in your app. There are many options for responding to such an event. Here are some examples:

*   **Onboarding new users**. Use the event to trigger a [helpful and informative onboarding flow](/surfaces/app-design#onboarding). Read [Rolling out the Red Carpet](https://medium.com/slack-developer-blog/rolling-out-the-red-carpet-447f0509fe97) and learn about building great onboarding experiences on Slack.
    
*   **Boost user familiarity with regular tips**. Display them to a user at varying cadences when they open the App Home. Give users control of how often these reminders come.
    
*   **Re-engage visitors**. If a user hasn't interacted with your app in a while, _and_ you receive a `app_home_opened` event, send them a message that welcomes them back and shows actionable next steps.
    
*   **Provide updates on your app**. Keep your users informed of the latest app improvements, new functionality or features released. But don't just market to them.
    
*   **Prompt for configuration**. Messages and Home tabs are buses for all kinds of interactivity — help users configure your app in a safe place, away from public channels.
    

* * *

## Deep linking to App Home {#deep_linking}

You can use a special [deep-linking syntax](/interactivity/deep-linking) to directly navigate users to different parts of Slack. This syntax can create links to open conversations, share files, and can even link a user right into your App Home:

```
slack://app?team={TEAM_ID}&id={APP_ID}
```

The link opens the App Home belonging to the app specified by the `APP_ID` in the `id` field, like `A123ABC456`. You should specify `team` with a `TEAM_ID`, using the ID of your Slack workspace.

You can also deep-link directly to a specific tab within an App Home:

```
slack://app?team={TEAM_ID}&id={APP_ID}&tab=home
```

The value of `tab` should be one of:

*   `home` - opens the Home tab of the app specified by `id` within the Slack workspace specified by `team`.
*   `about` - opens the About tab of the app specified by `id` within the Slack workspace specified by `team`.
*   `messages` - opens the Messages tab of the app specified by `id` within the Slack workspace specified by `team`.

* * *

## Onward: pairing with modals {#modals}

[Modals](/surfaces/modals) are a type of app surface ideal for requesting and collecting data from users. Interactive components within Home tabs can [trigger modals](/surfaces/modals#lifecycle), allowing apps to take input in a more focused space and respond accordingly. See [Modals](/surfaces/modals) for instruction.