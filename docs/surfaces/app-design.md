Source: https://docs.slack.dev/surfaces/app-design

# App design

Hello, fellow developer! We've compiled some best practices for you that dive into the finer details of designing apps.

From understanding your audience to successfully onboarding users, there's one underlying principle we recommend keeping in mind at all times:

**Build with empathy for the end user**. We all want to make our users' work lives more pleasant and productive. Your app is more likely to improve people's lives if you take into account the different ways that people work.

While some social groups use Slack to communicate, most people come to Slack to get work done. How they work may be a bit different. So how will your app help all these people get work done?

* * *

## Designing with intention {#outline_use_cases}

Slack users are people of all ability levels. They may have poor internet connections or only use Slack on mobile. We want them all to have a great experience on Slack, so please be empathetic of your audience while designing your app. Here are a few factors to keep in mind:

*   **Timezones.** Slack is used by people across the world and across timezones. If you're planning to post notifications at a particular time of day, understand that it will be a different time for some people in the workspace.
    
*   **Languages.** Slack is used collaboratively by people of differing languages and regions. Tailor your app's language to create a [localized experience](#localization) for specific users and channels
    
*   **Workspace size.** Not all Slack workspaces are the same size. There are five-person non-profits using Slack, and there are 50,000 person companies using Slack. Some workspaces keep their conversations in a dozen channels, while others create channels for every new project.
    
    To make your app work well for 5 person workspaces and 50,000 person workspaces, take into account how your app uses lists of users and channels. You may need to leave room in your UI for extra channels, or find ways to abbreviate or truncate what you display.
    
*   **User roles and access.** There are [several different user types in Slack](https://slack.com/help/articles/201314026-Roles-and-permissions-in-Slack). Aside from regular users, you should be aware of guest accounts, which are restricted to fewer channels. You may also come across actions performed by other bot users — depending on your app's purpose, it may be appropriate to treat them as regular users.
    
    Some users have permissions that others do not. For example, administrators can only permit certain people to install and manage apps, so prompting a guest user to authenticate their account may lead to a dead end. If you can, test your app using a variety of user types.
    
*   **Slack desktop vs. Slack mobile.** Some people only use Slack on their phones, while others only use it in a web browser. Make sure that you test our your app's interactivity and messages on as many screens as you can.
    
*   **Workspace preferences.** Some Slack workspaces may prevent users from editing or deleting messages. Some Slack workspaces may have a 1-hour message retention, meaning older messages are automatically deleted. Take a look through our [Help Center](https://slack.com/help/) for some example of workspace-level settings.
    
*   **User preferences.** Each individual user may have different settings. For example, they may choose to display username rather than full names, or they may automatically collapse all images and media within a message. Try to familiarize yourself with as many of Slack's user preferences as you can.
    
*   **Familiarity with apps.** Just because somebody installs your app on their Slack workspace, it doesn't mean that everybody else on the workspace knows about it. Some people may not even know that Slack apps exist, and may think that your app is part of Slack's built-in functionality.
    

### Gather feedback {#feedback}

Gather feedback and surveys from a diverse range of people within your organization. We don't prescribe what feedback or ideas to seek, but here are some thought experiments to try:

*   **Are there any regular types of message that are posted manually?** Imagine a manager posting in a channel every Friday afternoon asking for status reports. This could be turned into an app or workflow that posts reminders on the same schedule. The app could also collect the responses in a better format for the manager to consume later.
*   **Ask team members to find one or two automated messages that they’ve received in the past week or so that are critical to their job.** These automated emails can often be turned into messages posted by Slack apps.
*   **Think about the key hurdles that people face when using Slack in your team, and outline them.** Can an app or workflow solve those problems?
*   **Do you regularly use an external service while working?** If the service doesn't already have its own integration in the Slack Marketplace, build an app that integrates that service into Slack using that service's web-based API.

If you need some inspiration, explore the [Slack Marketplace](/slack-marketplace)!

* * *

## Case study: Slackbot {#slackbot}

We've developed our own set of guidelines for using Slackbot in an empathetic way:

![Should we use Slackbot? Flowchart](/assets/images/bp_should_i_use_slackbot-e1815014083632b486c1a39c28cb28f9.png)

Your app has its own special purpose and personality.

Map out your bot's logic and conscience while working through these best practices to help develop consistent and user-friendly experiences that feel at home on Slack.

* * *

## Considering bot design {#considering}

### Bot names {#bot-names}

Pick a name that is representative or your brand and what the bot does, being careful not to violate trademarks and other brand names.

Your bot's username must follow our regular username guidelines: lowercase letters, numbers, underscores, dashes, periods, and less than 22 characters in length.

Some Slack users prefer to see full names rather than usernames. In this case, the bot's "full name" will inherit the name of your app.

To update the name of a bot that has already been installed, navigate to your workspace settings by clicking on your workspace name in Slack, then **Tools & settings**, then **Manage apps**. Once you've navigated to the app management dashboard, you can find **Bot user** and rename it.

### Slash commands {#slash-commands}

Should you choose to create a Bolt app (as opposed to a Deno Slack SDK app) choose a descriptive name for your [slash command](/interactivity/implementing-slash-commands), but make it easy to remember and type.

If your application provides printing services, then `/print` makes sense, but avoid using copyrighted names that you do not own like `/HP` or `/canon` (unless you work there, in which case it's a great idea).

If your service is known by its name, a command with your company's name in it (like `/lyft` and `/uber` to request car sharing service) is an easy way for Slack users to remember how to invoke your slash commands.

When a slash command with the same name is created by another app, it will override pre-existing slash commands with that same name. Try to choose a name that won't override or be overridden by another developer's carefully named command.

Pick a name that is easy to remember and connects directly with a purpose. Users shouldn't have to explore the slash command drop down every time they go to do that thing.

### Colors {#colors}

There are a couple of different places where you can customize colors used in your app.

#### Message attachment bar {#message-attachment-bar}

The first is the set of colorful bars guarding the edge of messages.

Utilize your brand color to complement your app's avatar to more clearly brand your messages.

Your service may already associate specific colors with workflow transition types and objects — prioritize clarity and legibility by using the colors that will most clearly resonate with our common users (e.g. green for confirmation, red for cancelling actions, colors that are legible and not overbright).

![message attachment bar green](data:image/png;base64,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)

![message attachment bar red](data:image/png;base64,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p+YCrnKajF++O/2LaRMRfU1G5cJ/j3Xdu1OPRU9/ONOe1nvuR6VNRPQdA697t7gLuLrutvndvdImIsJ3nNUgMJjfK63VAOJM+quPSpuI6FsG3hDJ/RJLEH5Y+mfSJiL6loE3goE7juNFH5b+mbSJiPAdZzXoyHDPqcvZh6V/3zMlIrZ4iYiIgZeIiIGXiIgYeImIGHiJiBh4iYiIgZeIiIGXiIgYeImIGHiJiAh/zqt/jvhaglWx+4cZQfxz70M8JuZ6t/SCVwIL1hYi+tGBd6qr0ItqYQS5/oiMhEnoR4cFzExWFiLCz+5qyGzA8gEAbgr4Lx8S3m3WECJi4HWzA6MAAAQoSURBVN3rAMm2QeoACD4ovPNdPkTEwLv35AOqC2A0BfSPerO69FhHiIiBdycwkWwAKIAtALhDW3/wsXs9pqOP7nCQpPSbv3CHtj3km9WI6B20r3UaxYVPh3O/jwsFqisfloCYQozWSaHEcEMAnrtQCiXu9YNWqZ1P38xhFEjDEoBIoSUARFEkRZFklhu94kyJiP6UebyZDVjIgMELXG0KmCaS1RjwywVgmgjLdx7B9gG9Nl9CaNU/0txn3SGin/gAhQ5MeyGQAk4C291sukDsQwlhOpuNm8l39zTYgHrosogTmN1er2silKw7RPQTA++LD8SAPsdoCnRegFmGUMcCsOfAS/HuIbepYgLRrkvX0wFzNp3OFCBlPy8R/chHhgMAMAUwB2yMx+OxAKZwgcWv0V2OMDeBxNr1bQDmDADM6g8R0Q96cm1rZWeAMgUKFWFY/bKTKXaIKQZJeYeXrc+cFAsHu6G/bXlNByFCVh4i+omBF1oGWGsAgLl7yqwIpu5gAYQwR5M7tKofF0hjFQAivdbOVVh5iOhHBl4cekzs51pLeOUlRojkLrlbm0nVI2NlSPadDjErDxH96GUhB0Ao6r+YB4sCCO8x6SvaJ2zvjuImAOeTEdHPDryliWTbBO15AETVKsX0HolPisOzctsC2wBmxspDRD868E5NQH/Ue043Tl2M80HP9VRgcJ/UsyrIRgqQ/tL1XzpgTll5iAg/uY93O/lAjQHoBVSEAHSY6Z1S9/LtHIa1k2KqYgroM9YdIvrpr/4JvIEJwC60FRLdBgDfmN+rQV3Y9aOYgz4nkxHRm32RSVFG9Xd6oVnerkPVg9zN3HU78epiIz97Y/pV0lhd+QLBrl8i+lGBFy17V7IPS5+Bl4jAtwwTETHwEhEx8BIREQMvEREDLxERMfASETHwEhERAy8REQMvEREx8BIRMfASETHwEhHRzwu8/gcn5X+50yQiBt7fSiC9X2IpxIelfyZtIqJvGXjt2lvV382E/WHpn0mbiOiY9rVOozj/v6ns3utt6t4KSvxB6bvr07SJiL5li3c1QOneKe6uMVh9UPpueSZtIiJ8y5ddlu4KD4nx3hf7+qm5gPvyIelv0y5Zo4gIf8SrfwBfWdzpSIOXj0t/UPKd70T0xwRewBVh9O7DCDtafVT6V9ImIvqWgZeICBxcIyIiBl4iIgZeIiJi4CUiYuAlImLgJSIiBl4iIgZeIiL63oF33PiLiAhcFvKjpdv1IOOMV4SI2OL9HJE+BsZ6xAtCRERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERERETn/T+adTRxkeXqMAAAAABJRU5ErkJggg==)

When you're not harmonizing with your brand, we suggest using the default light gray. If you're looking for just a little more distinction, consider using optional `color` values `good`, `warning`, or `danger`.

#### App Profile background color {#app-profile-background-color}

The second place where you can choose a custom color is in your app's profile background. If somebody clicks on your app's name, a little profile card with a brief description of your app will be displayed.

The top section containing your app's name and icon will be displayed with your custom background color. It should pair nicely with the colors in your icon, and there should be enough contrast that you can read the white text on top.

### Logo assets {#logo-assets}

*   Pick a compelling logo that will look great, adaptively rendering at 512x512px on desktop, and 36x36px on mobile. Illustrations work better than photos.
*   Don't include lots of text that will be hard to read at a small size
*   Don't round the corners — Slack will do it for you!

![logo examples](/assets/images/bp_logos-fe445403e55d9d4414414665a4559697.png)

* * *

## Messaging with consideration {#messaging}

[Messages](/messaging) that alert users can be incredibly useful. Many Slack apps exist primarily to pipe notifications from external services into relevant channels. Here are some specific considerations that can help ensure the messages your users want don’t turn into noise.

### Be upfront about communication {#comms_onboarding}

When your app is first installed, allow the installer to easily set preferences that relate to communication. Think about settings like the rate of messages, the channel they should be posted to, and if applicable, the type(s) of notifications your app should send.

### Avoid large-group mentions {#mentioning}

There are very few cases where your app should send broad mentions like _@channel_, _@here_, or _@everyone_. One exception might be if your app sends a notification for immediate action when a critical system or service goes down. Even then, you should get explicit permission from the installer before your app uses one of these mentions.

### Pick the right frequency of notifications {#frequency_notifications}

Consider how frequently your messages are generating notifications for a user. When it makes sense, offer the user an option to get a digest of these messages rather than being alerted for individual events. This is especially important when the events are coming from an automatic source like service logs. In extreme cases, sending too many messages can get your token revoked due to rate limits.

When your app generates a lot of notifications, users will notice (and might grow annoyed). This can lead them to remove your app from a channel or even to uninstall the app from the entire workspace. One way to mitigate this is by surfacing messaging preferences often. Make it intuitive for people to use your app how and when they want.

Here's an example of an app that builds a preferences link into the actual messages:

![App message featuring link to change notification settings](/assets/images/interaction_guidelines_notifications-46d8141db24fe0496332bccdf84c57b9.png)

### Match message types and channels {#notifications_channels}

You may already be segmenting or categorizing the types of messages that users can receive. If your service already does this, you can make the Slack notification experience even better by giving people the option to pipe different message types into different channels.

For example, an HR tool might want to pipe messages about a candidate’s background check only into _#hr-team_, but after an offer has been accepted and signed, maybe a _#new-hires_ channel wants to be notified so they can celebrate.

Don’t post to a workspace’s _#general_ channel by default.

You’ll likely be unnecessarily disrupting many users and there is probably a more relevant channel for your app to post in.

### Make messages that notify actionable {#notifications_action}

Some messages are best being only text that alerts a channel that something happened in a third-party system. But oftentimes messages lead to follow-up action.

![App message, featuring buttons for direct interaction](/assets/images/interaction_guidelines_notifications_b-61583ca8755018eb445f92d7bf5a8db8.png)

You can save people work by adding action elements directly into your app’s Slack messages. [Buttons](/reference/block-kit/block-elements/button-element), [select menus](/reference/block-kit/block-elements/select-menu-element), and [modals](/surfaces/modals) let people react in the moment and get work done faster. If your app is considerate with alerts and saves people time, they’ll likely find your app an essential part of their workday.

Your actionable messages don’t need to be complex to be helpful.

Just think about what action the receiver _most likely_ wants to take. For example, if your app sends expense approval messages, the receiver probably wants to approve or deny the expense — interactive buttons are perfect for this.

Learn more about [sending messages in our messaging docs](/messaging).

### Sending direct messages to users {#dms}

First, consider when and whether you should [send direct messages (DMs)](/messaging/sending-and-scheduling-messages#conversations) to specific users. Remember that DMs generate push notifications for mobile users and badges on desktop and mobile. These are useful but also disruptive and can be unexpected, so be cautious with your use of DMs. You should only DM a user when:

*   The user sends you a DM first.
*   The user is the only one you’re providing a service to, rather than the team.
*   Your app is sharing confidential interactions or information.

Users will assume that information shared back and forth with your app in DM is private. Be aware of any sensitive information that’s being shared, and don’t surprise users by announcing results of DM conversations in channel without letting them know first.

By default, apps are set up with a messaging tab that allows the app to broadcast messages only, without needing to anticipate or respond to human interaction.

### Responding to users in channel {#in_channel}

Whatever you post in channel is going to be long-lived and add to the group conversation that people are reading, both in the moment and later when they look back at what was shared.

In response to a user action, an app could [publish an in-channel message](/messaging), or an [ephemeral message](/messaging#ephemeral). In-channel response will be visible to all channel members where the user invoked the action. Ephemeral responses will only be visible to the invoking user.

Remember that a chatty app is not necessarily a good thing, so only pick responses that are important to the entire team when posting in-channel.

If the response only needs to be displayed to the user, it’s a better idea to use an ephemeral message than it is to generate a DM.

![An ephemeral message posted by an app](/assets/images/interaction_guidelines_ephemeral-4c46378f3235b3da3e9c7a47261c8c09.png)

[Read more about ephemeral messages](/messaging#ephemeral) in our [Messages docs](/messaging).

* * *

## Communicating with clarity {#voice_and_tone}

Your app will converse with users frequently, whether via conversational interface or structured interactions. It's vital that the voice and tone of your app's articulation is brief, clear, and human.

Your Slack app is a representation of your brand, and the way your app communicates will become part of your brand voice, especially if you’re building a conversational interface.

This presents a great opportunity: you can thoughtfully define what your brand voice is. The best thing to do is think of this voice as an extension of your own voice.

### Providing personality {#personality}

Your app’s primary purpose is to help users accomplish a task—even if that task is inherently entertaining, like finding just the right cat GIF. It's great if your app sounds clever, just ensure these traits don't obstruct the user's ability to complete the work your app is assisting them with.

Foreground the information necessary to the task at hand, then add voice and tone elements. They should enhance what’s already there.

You want your voice to differentiate yourself from the crowd. Using contractions and conversational cadence is a good way to lightly infuse your app with human personality—“You’ll be able to” rather than “You will” and that sort of thing.

A little goes a long way.

### Be brief {#brief}

Nearly every word your app says should facilitate an interaction (courteous parts of speech, such as greetings, are also useful). Don’t add a joke or aside just to be glib.

**Like this**

![brief example](/assets/images/bp_brief_example-c9225883af11862fb6e0ebdeb055da5f.png)

**Not like this**

![overly wordy example](/assets/images/bp_wordy_example-6979191adeb162b54f86c1cb5726cf9e.png)

The first example still has plenty of distinctive personality, but gets straight to the point, and doesn’t risk users choosing not to wade through unimportant content.

### Be clear {#clear}

Words and copy used in your interactions should be easily understood even by someone who doesn’t speak the same language fluently. That means:

*   Don’t use jargon and slang in the important parts of message text
*   Avoid culturally specific references, like jokes from movies
*   Stick to common, understandable words
*   Button labels should be clear and specific
*   Make buttons active-voice and reflect the user’s outcome (Save, Book Flight, Place Order)
*   Avoid vague, non-actionable text like Click here or Settings
*   Don’t replace words with emoji

If you choose to include puns or wordplay, make sure they focus a user's attention, rather than creating a distraction.

**Like this**

![non-culturally specific example](data:image/png;base64,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)

**Not like this**

![overly culturally specific example](data:image/png;base64,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)

The second example is confusing in two ways: it includes a reference to an obscure film, and the emojis it uses may stall some users as they try to decipher their meanings (“Fire... meat? Fire-meat?”).

The message button copy is also unclear and confusing, potentially preventing users from selecting any response at all. We recommend using standard combinations on buttons (Attend/Decline, Confirm/Cancel) to help your users have a smooth experience with your app.

### Be empathetic {#empathy}

All kinds of people use Slack, and we previously described how important it is to understand that variation in terms of their ability to use your app properly. But that diversity is also important when thinking about the tone you use to communicate with them.

Ensure that your voice and tone express empathy toward every single person who uses your app. Some basic steps to take include:

*   Use gender-neutral pronouns.
*   Use a variety of emoji skin tones.
*   Don’t use sexist, racist, or ableist language.
*   Make an effort to trial your voice and tone with people from a diversity of backgrounds, in different settings (on mobile, with flaky wifi, etc.).
*   Don’t assume any level of technical fluency from your users - keep instructions clear.
*   Writing for a broad audience takes a bit of practice if you’re new to it, and it is usually easier if you have a diverse team of people working on your app from the start.
*   If you decide to give gender to your app (and it’s very easy not to), then be appropriate with the kind of things it says - make sure it doesn't use any stereotypes or generalizations.

A final note: informality is good, but getting too friendly is often seen as grating or culturally insensitive (particularly in a workplace).

## Locali(z/s)ing your Slack apps {#localization}

Slack app localization allows an app to provide specific text written for specific locales by using API methods to automatically detect the `locale` of users and conversations.

Use localization to customize your app's experience. This can include:

*   Changing languages to suit different audiences.
*   Customizing cultural references for a specific region, culture, or language.
*   Tailoring interactivity. For example, a travel booking app can select a default departure airport for a user based on their locale.

You can localize any text that your app publishes directly to users, such as in messages and modals.

You cannot localize pre-configured text in [slash commands](/interactivity/implementing-slash-commands) or [message actions](/interactivity/implementing-shortcuts). Nor can you localize your app's display name.

### Knowing which language to display {#locales}

There are two basic preferences for language that are visible to apps:

*   The chosen language of the [conversation](/messaging#conversations) that the app is currently operating in.
*   The display language of an individual user of the app.

A localized app should use the channel's locale for channel-published content. The app can then optionally use an individual user's locale for content _only visible to that specific user_.

The goal should be to **ensure that the most common language is chosen for the entire audience in each context**.

Imagine a French-speaking user is in a German-speaking public channel. Your app can use French in private interactions with the French user, while using German in the German-speaking public channel.

### Retrieving locale preferences {#locale_apis}

There are multiple locations you may encounter the `locale` field, indicating a preferred language.

*   Retrieve the `locale` of a [conversation](/messaging#conversations) by using the [`conversations.info`](/reference/methods/conversations.info) Web API method and setting the `include_locale` to `true`.
*   Retrieve the `locale` of a user by using the [`users.info`](/reference/methods/users.info) Web API method and setting the `include_locale` parameter to `true`.
*   Receive a `locale` field within any [Events API](/apis/events-api/) [`user_change`](/reference/events/user_change) event object.

Your app should check the conversation or user `locale` every time the app wants to publish or update content.