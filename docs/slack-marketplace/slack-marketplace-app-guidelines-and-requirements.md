Source: https://docs.slack.dev/slack-marketplace/slack-marketplace-app-guidelines-and-requirements

# Slack Marketplace app guidelines and requirements

Whether you’ve just started building an app, or are ready to submit one to the Slack Marketplace, this guide will help you prepare your app for the Slack Marketplace review.

During the review, we’ll check that your app follows the guidelines below, which you’ll see summarized when you submit your app. Remember that your customers use Slack to communicate, collaborate and streamline processes while they’re at work. Consider how your app’s design and experience will help them do just that, and build a high-quality experience with that in mind.

This guide is subject to change and will reflect updates we make to the review process as we release new features and experiences in Slack. If you have any questions or feedback about this process or guide, we’d love to hear from you.

* * *

## Apps unsuitable for Slack Marketplace {#suitable}

In the Slack Marketplace, our focus is to showcase apps that help our customers get work done more easily. For that reason, not every app may be the right fit for the Slack Marketplace. The list below is not exhaustive-the Slack Marketplace team may use their judgment to deny any app from being listed. Some apps are unsuitable for the Slack Marketplace, including apps that:

*   export or backup message data.
*   do not include functionality in Slack.
*   use legacy/restricted scopes or methods, scopes that provide extensive access to workspace data without a clear use case that requires them, or coded workflow scopes (e.g. `admin.*`, `identity.*`, `search:read`, `workflow.steps:execute`, `triggers:*`).
*   facilitate destructive behavior (e.g., 'self-destructing' messages, bulk file deletion, bulk message deletion).
*   embed Slack into another site.
*   only use [Sign in with Slack](/authentication/sign-in-with-slack/) functionality.
*   replicate Slack client functionality, or are third-party Slack clients.
*   unnecessarily request a large number of scopes when there is a less permissive option.
*   share sensitive personal information, such as financial or health information in Slack.
*   circumvent product restrictions or admin controls in Slack.
*   do not add value to the experience of using Slack.
*   enable remote execution on a server via a downloadable third party script e.g terminal commands from Slack.
*   facilitate the sharing of third party service accounts between multiple users.
*   are installed on less than 5 active workspaces. An active workspace is a workspace that has been used in the past 28 days.
*   are in private beta, still being built, or have not been fully tested.
*   enable financial transactions, including cryptocurrency transactions, or the minting or transfer of NFTs in Slack.
*   use Slack data to train Large Language Models (LLMs).
*   perform sentiment analysis/insight generation, unless the insights/analysis provide very clear value to customers, are limited to an aggregate level, and it is clear how they are determined.

In addition, coded workflows are currently not eligible for listing in the Slack Marketplace.

### Read our terms and policies {#policies}

In addition to the above list of unsuitable use cases, you should also review our terms and policies. By distributing your app through the Slack Marketplace, you agree to abide by the following core policies and terms:

*   [App Developer Policy](/developer-policy)
*   [Slack Marketplace Agreement](/slack-marketplace/marketplace-terms-conditions/slack-marketplace-agreement)
*   [Security Review](/slack-marketplace/marketplace-terms-conditions/slack-security-review)
*   [API Terms of Service](https://slack.com/terms-of-service/api)
*   [Brand Guidelines](https://slack.com/brand-guidelines)

Apps that do not follow these terms will not be accepted in the Slack Marketplace.

Phew - if you've read through the above and still think your app is suitable for the Slack Marketplace, keep reading to find out more about what we look for.

* * *

## Your Slack Marketplace listing {#listing}

If your app/service is a house, then your Slack Marketplace listing is the front door. People visiting your listing should be able to easily understand the problems your app solves, how it integrates with your service, and what the next steps are for getting started.

### Name {#name}

A great name can help people understand what your app is all about. Choose a name that's unique, easy to remember, read, search for, and spell.

If your Slack app integrates with another service, include the name of that service in your app name. If you do not own the service, make sure to not infringe on any trademarks or copyright (e.g., _“Task notifications for Slack”_ rather than _“Slack task notifications”_).

### Short description {#short_description}

The short description should be used to sum up your app’s value. An app's short description is visible in Slack Marketplace search results and on app profile cards in Slack. This description should concisely state the value of your app and be attention-grabbing. Make sure to **keep it short and sweet at 10 words (or fewer)** so that it doesn’t get cut off anywhere. Please note: short descriptions do not support Slack [message formatting](https://slack.com/help/articles/202288908-format-your-messages).

![Example of how a short description appears in search results](/assets/images/google_calendar_short_description-afd4de7baf3049c9f6391e64fbc739e5.png)

### Long description {#long_description}

In a long description, you can go into more detail about what your app can do. Your long description will help customers browsing the Slack Marketplace better understand the value of your app. While there is some flexibility in how you choose to describe your app, below are some points you should cover:

*   If your app integrates with another service, include a brief overview of that service for those who may not be familiar.
*   Clearly state the problem your app solves. Framing your app in this way helps people understand how they could use it.
*   Provide a clear indication of how your app works in Slack. This helps people to understand what they can expect in Slack after installing your app.
*   Use Slack [message formatting](https://slack.com/help/articles/202288908-format-your-messages) to make the long description easier to read.
*   Emoji can be added to your long description using the `:emoji-code:` notation and will render in your Slack Marketplace listing, however be sure only to use standard [emoji codes](https://www.webfx.com/tools/emoji-cheat-sheet/) as custom emojis will not work.
*   Please don’t try to boost searchability by filling your long description with keywords that aren’t directly relevant to your app.

![Example of how a long description appears in Slack Marketplace](/assets/images/hiretron_long_description-8fe51ba7a39b5f43bcb55819fe8fb1ce.png)

### Icon {#icon}

Your app icon should catch people's eye when they're scrolling through the Slack Marketplace. Make it unique, distinctive, and understandable. It should also be of high quality and resolution so that it doesn’t result in a blurry image in the Slack Marketplace.

![A icon we like](data:image/png;base64,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) ![An icon we think is bad. Don&#39;t try this at home](data:image/png;base64,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)

### Images and screenshots {#images}

Your Slack Marketplace listing allows you to upload app images and screenshots. This is a great way to highlight key app features and give customers a clear idea of how your app works in Slack. Here are some things to keep in mind:

*   Use high quality images.
*   Use a 1600px by 1000px size (8:5 ratio).
*   Show your app/service in the context of Slack, not other tools your service may integrate with.
*   Use a .jpg, .jpeg, or .png file format, and make sure the size is under 21mb.

When showing an image of your app in Slack, adding text can help provide context. This is a good way to show your customer at a glance how your app will help them get their work done more seamlessly.

![Helpdesk example screenshot](/assets/images/example_screenshot-1db7c4fa7fb5f72cdb22274a67b00bda.png)

### Video {#video}

A high-quality video is an efficient way to show people what your app can do and help your potential customers get excited about how it might help them with their work. We strongly recommend you consider adding a video and offer these suggestions:

*   Keep your video length between 30-90 seconds.
*   Make sure your video is publicly-accessible YouTube link, not a link to a channel or playlist.
*   Turn on closed captioning and turn off ads in YouTube's settings before submitting your link.
*   Make sure your video shows how your app works in Slack.
*   For screencasts, use a real-life Slack environment (e.g., realistic member names, profile pictures, and channel names). Make sure to show your production app in action, not the app you use to test during development.

### Pricing {#pricing}

Slack allows you to charge users for your app. If you do so, you should handle payments securely and provide transparent information on your billing policy. You can select one of the following pricing models to be displayed on your app's listing page.

*   **Paid:** users pay to use your app.
    
*   **Paid with free trial:** users pay to use your app, but there's a free trial available.
    
*   **Free and paid plans available:** users don't need to pay to use your app, but there are paid features available.
    
*   **Free:** your app is free!
    
*   **Included with service subscription:** the app is free so long as users have a paid plan with your service.
    

### Language Support {#languages}

Supporting multiple languages with your Slack app is great. Before adding this information to your app settings, it’s important to understand what it means to fully support a language:

*   People can select to use your Slack app and any related service in this language entirely.
*   All messages and interactive components sent by your app in Slack, as well as any other interfaces related to your service, are available in this language.

As this relates to the language used in your Slack Marketplace listing, this is entirely up to you! The only thing we ask is that the experience is consistent i.e. the language used for your descriptions, images, videos, and pages associated with your listing is consistent.

### Direct Install {#direct_install}

Enabling direct install can be a great way to shorten the distance between discovering your app and installing it. With this enabled, instead of people having to visit your landing page to install your app:

![Direct install screenshot](data:image/png;base64,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)

They can install your app directly from your Slack Marketplace listing:

![Direct install screenshot](data:image/png;base64,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)

To configure this link on your [app's settings dashboard](https://api.slack.com/apps):

1.  Open the _Basic Information_ page
2.  Scroll down to _Installing Your App_
3.  Select and enable _Install from Slack Marketplace_

Things to note when enabling direct install:

*   The URL you provide must HTTP 302 redirect to a fully qualified `slack.com/oauth/v2/authorize` URL, as per the [first step of the OAuth flow](/authentication/installing-with-oauth).
*   As installation of your Slack app will be accessible to anyone with a Slack workspace who views your Slack Marketplace listing, your onboarding flow needs to account for this. For instance, in the case of a Slack app that requires an account with a third party service to function, it is possible that people will install your Slack app without first having an account. Your Slack app’s onboarding flow should account for this and guide people to either create a new account or connect an existing account.

* * *

## Pages associated with your app {#pages}

### Your landing page {#landing}

Your landing page is the place for you to provide your potential customers with all the information they need to get started with your Slack app. There are some things that you should make sure to include:

*   A clear overview of your Slack app, any associated services, and the problem your app solves.
*   A detailed explanation of how your app works in Slack. Screenshots and GIFs are a good way to show people what they can expect in Slack after installing your app.
*   A clear path to installing your Slack app, whether that is an Add to Slack button on your landing page or instructions for accessing your Add to Slack button.
*   A clear path to using your app. Once people install your app to their workspace, they should be redirected to a page that confirms the installation was successful and provides clear next steps for getting started with your app.
*   A clear link to your privacy policy.
*   In addition your landing page needs to be publicly accessible (i.e. not behind a login) and should be an actual web page created specifically for your Slack app - not a link to a PDF, document or code repository.

![Google calendar landing page](/assets/images/google_calendar_landing_page-2f61d636261d6bcb9f6e2630e94e0902.png)

### Your support page {#support}

We expect all Slack Marketplace developers to provide accessible and responsive support for their apps. You know your app best, which means you’re the expert when it comes to providing customers with a great support experience when they have questions or encounter issues. Please make sure your support follows these guidelines:

*   There is a clear way to get in touch with your support if someone needs help, such as an email address or contact form.
*   Getting support doesn’t require signing up for any additional accounts. While using GitHub issues or Twitter as support channels is completely reasonable, you must also provide support that does not require an additional account.
*   Your support experience is responsive. We expect support requests to receive a response within **2 business days**.
*   Your support page needs to be publicly accessible i.e. not behind a login.

### Your privacy policy page {#privacy}

All Slack Marketplace apps must include a clear privacy policy that details how third-party data is handled and this page should be accessible on your app’s landing page. At a minimum it should include:

*   What data is collected.
*   How the data that is collected is used.
*   How long data is kept.
*   How an individual can request to access, transfer, or delete their data
    *   For deletion, this can be either a generalized statement regarding how someone can request deletion of their data, or language specific to applicable privacy law e.g GDPR/CCPA.
*   Information on how to contact the service for making a request related to their data.
    *   At a minimum should be an email address or a webform.
    *   A physical address alone is not sufficient.

It’s important to think about how third-party data passes through your app. While your app may not make use of data as a feature of your product, it is possible that data is received by your service when your app is used (e.g., IDs from slash command payloads, data from system logging, etc.). If your app receives data but never uses it, this must be stated in your privacy policy.

* * *

## User experience {#ux}

It goes without saying (but we’ll say it anyway): people should have a good experience using your Slack app! This encompasses everything from making sure an app meets basic utility requirements, all the way to the finer details of how your app interacts with people in Slack. As part of reviewing your submission to the Slack Marketplace we will install and test your Slack app to assess the user experience; below are some of the things we will be looking for.

### UI/UX Fundamentals {#ux-fundamentals}

The Slack platform provides an extensive array of options for developers to choose from when building an app. However, the same general considerations someone makes when designing a website/desktop app/mobile app/any-kind-of-software-with-an-interface still apply. You should always look to create interfaces and experiences in your app that adhere to common best practices i.e what people expect from modern software. Some things to think about:

*   ✅ **DO** provide clear visual feedback when a user takes an action e.g buttons appear ‘clicked’, information submitted is confirmed as submitted, loading gifs etc
*   ✅ **DO** provide explicit user guidance where needed e.g input hints
*   ✅ **DO** provide meaningful & actionable error messages e.g “You need to invite our app to the channel before you can use this command. Type /invite @bestapp and try again” rather than “Oops! something went wrong!”.
*   ✅ **DO** actively onboard first time users - help them get started!
*   ✅ **DO** make help and support easily accessible as part of using the app e.g include support information in your app “Home” tab by default
*   ✅ **DO** make it clear what the output will be for any given input e.g no “I didn’t realize it would post that in channel!” moments for users
*   ✅ **DO** clearly attribute app actions to a user where there could be confusion e.g no “who let this app post in this channel!?” moments for users
*   🚫 **DON’T** lead users through one-way doors e.g users should always have an easy way to go back when completing an action with an app
*   🚫 **DON’T** lead users to dead ends e.g no “well what do I do now?” moments for users

The above list is by no means exhaustive but you get the picture: give the folks using your app everything they need to make the most of it.

### Organization-ready deployment {#org-ready-deployment}

Enabling [organization-ready deployment](/enterprise/organization-ready-apps) for your app allows people to deploy your app across multiple workspaces within an Enterprise organization. Since this is a powerful feature, it requires some thoughtful planning. In particular your app needs to be prepared to function in [Slack Connect](/apis/slack-connect/) channels where Slack users from another workspace in the organization will be able to interact with your app. Having a clear understanding how your app’s features work in this environment is a requirement for any app in the Slack Marketplace with organization-wide deployment enabled. To find out more about preparing your app head [here](/enterprise/organization-ready-apps).

### Onboarding {#onboarding}

Good onboarding is transparent, directed, and designed to welcome a new customer to a product by setting them up for success! Onboarding is a broad topic and there are as many ways to do it as there are ways to build a Slack app, however here are some common things we think underpin a good experience (and a few that don’t):

*   ✅ **DO** be transparent about where a user is within the onboarding flow e.g provides goals and clear progress markers
*   ✅ **DO** provide clear next steps
*   ✅ **DO** close the gap between installation and usage - get to the value! e.g. have people try out app features as part of onboarding
*   ✅ **DO** request explicit consent to send emails (if you intend to send messages to emails collected via the Slack API)
*   ✅ **DO** clearly surface ways to get support throughout the process
*   ✅ **DO** remember to think about onboarding in terms of both the installing user and first time users - both need to be guided!
*   ✅ **DO** provide a clear and easy way for users to connect their Slack account with your service’s account if required e.g a ‘connect account’ step that asks people to authorize the app.
*   🚫 **DON’T** ask people to manually map external service accounts to Slack accounts (invites potential for human error/impersonation).
*   🚫 **DON’T** leave users stranded e.g no “Hello? What do I do now?” moments for users
*   🚫 **DON’T** make people think!

The above list is not exhaustive but should provide a fair idea of what we will be looking for when reviewing your app.

### Notifications and sending messages {#notifications}

For many apps, notifications are the core of their service, and for many customers, notifications are what they think of when they think of Slack apps. A well timed, actionable notification has the potential to genuinely make someone’s working life _simpler, more pleasant, and more productive_. But with great power comes great responsibility! Poorly timed, persistent, uninformative notifications have the potential to ruin someone’s experience of using Slack. Here are some of the things we hope (and don’t hope) for from Slack Marketplace apps:

*   ✅ **DO** provide a way for customers to configure notification type and frequency
*   ✅ **DO** make notifications relevant and actionable e.g message buttons!
*   ✅ **DO** try to batch-send high volume notifications or create digests
*   ✅ **DO** attribute notifications in shared spaces to the person who configured them e.g if notifications have been configured for a public channel, send an intro message into the channel to inform channel members of this fact and who configured them
*   ✅ **DO** double (triple) check notification copy for spelling and grammar
*   ✅ **DO** use [Block Kit](/block-kit) to create beautifully formatted, easily parsable notifications that deliver their message clearly and succinctly
*   🚫 **DON’T** send notifications to people who would not expect to receive them
*   🚫 **DON’T** spam people with high volume notifications
*   🚫 **DON’T** impersonate a user on a workspace when sending messages
*   🚫 **DON’T** send notifications to a user’s Slackbot channel. Use the app home Messages tab instead.
*   🚫 **DON’T** use @channel, @everyone unless there is a supremely relevant and unavoidable reason (nearly never)
*   🚫 **DON’T** post to a workspace’s #general channel by default.

### Home Tab {#home}

The “Home” tab is one of the most powerful tools in your toolbox when it comes to building a robust user experience right in the heart of Slack. The highly customizable layout will allow you to provide an experience closer to using full-fledged standalone software. Here are some of our top tips on how to maximize the space:

*   ✅ **DO** load relevant and useful content for any user on a workspace who views the tab regardless of whether they have authorized your app or not
*   ✅ **DO** adhere to standard UI best practices e.g. pagination for long lists, auto update view when changes are made by user etc
*   ✅ **DO** make support information clearly visible and surface any pricing plan information (if applicable)
*   ✅ **DO** use it as a place to surface app settings
*   ✅ **DO** allow people to customize how things are organized/presented (more relevant to apps who make heavy use of the “Home” tab)
*   ✅ **DO** understand who is viewing the tab and only show information they should have access to
*   ✅ **DO** think about the hierarchy of information and functionality being displayed e.g customers shouldn’t have to think too hard to do common tasks or find information
*   🚫 **DON’T** enable the tab if the app does not use it. This doesn’t only include cases where it doesn’t load content, but also cases where the content is detracting from the experience of the app e.g a tab displaying only “\[APP NAME\] is installed on your workspace”.

### Messages Tab {#messages}

The "Messages" tab is part of the App Home and is the equivalent of a direct message conversation between a user and your app. It is a great place for notifications along with more complex, conversation-like interactions.

*   ✅ **DO** respond to users’ direct messages if the message input is enabled
*   🚫 **DON’T** have this tab enabled if your app is not actively using it

### Shortcuts {#shortcuts}

Shortcuts come in two flavors:

_Global shortcuts_: a great way to provide people with access to your app’s functionality anywhere in Slack via the quick switcher or by clicking on the plus icon to the left of the message field in Slack.

_Message shortcuts_: perfect for in-context use of your app and turning messages into action! Accessible via the ‘More actions’ menu on selected messages.

When working with shortcuts the following guidelines apply:

*   ✅ **DO** start your shortcut name with a verb
*   ✅ **DO** acknowledge the request with a 200 OK response in 3000ms to avoid a timeout error
*   ✅ **DO** open a modal when the shortcut is used, send appropriate confirmation and error messages
*   ✅ **DO** understand that your shortcut is accessible to anyone on a workspace where your app is installed, so you should handle unrecognized users with grace and clarity.
*   🚫 **DON’T** expose private channel metadata (e.g channel name, members) if sharing a message from a private channel using a message shortcut

### Slash Commands {#slash}

Slash commands are a long lived stalwart of the Slack platform (and messaging software generally). Used by entering a forward slash and the given command in the message field or by clicking on the plus icon to the left of the message field in Slack. When working with slash commands:

*   ✅ **DO** try to use a unique name for your slash commands in order to maximize discoverability and minimize the potential for name collisions e.g instead of `/help` use `/[your_app_name]-help`
*   ✅ **DO** respond with usage instructions when someone adds “help” or unknown input after the slash command
*   ✅ **DO** respond with a helpful and appropriate error message if something goes wrong
*   ✅ **DO** consider whether to respond with an ephemeral or in-channel message — it’s usually always best to use an ephemeral response to minimize disruption for others and allow your slash command to be used anywhere.
*   ✅ **DO** understand that your slash command is accessible to anyone on a workspace where your app is installed, so you should handle unrecognized users with grace and clarity.
*   ✅ **DO** use the [response\_url](/interactivity/handling-user-interaction#message_responses) included in the slash command payload to respond to users
*   ✅ **DO** include a clear and useful hint and short description text for your slash command.
*   🚫 **DON'T** overload a slash command with too many arguments. Whittle things down to key workflows and explore things like [message buttons](/reference/block-kit/block-elements/button-element) as ways for people to navigate your slash command functionality

### Work Objects {#work-objects}

[Work objects](/messaging/work-objects-overview) add a whole new dimension to standard unfurls, making it possible to represent external content (e.g files, tasks, incidents, pull requests) in a structured way in Slack.

*   ✅ **DO** respond with an error in the flexpane if authentication is required and a user is not authenticated to view an item or perform an action
*   ✅ **DO** respond with an error in the flexpane if a user _is_ authenticated but does not have access to the resource
*   ✅ **DO** send the user an ephemeral message or DM with a helpful error message for non-authentication related errors
*   ✅ **DO** use Slack [message formatting](/messaging/formatting-message-text#basic-formatting) to ensure any markdown content is easy to read
*   ✅ **DO** ensure that blocks render cleanly with no broken images, cut off text, etc.
*   ✅ **DO** handle each entity type correctly and respond with appropriate content if multiple entity types are enabled

### Scope & Data access {#data}

When developing your app for Slack, one of the most important things to bear in mind is the level of access it needs to work: the less access your app requests, the more comfortable users will feel about installing your app. From the customers’ perspective, they must give your app access for it to function and they may be reluctant to install apps that request a lot of access to their Slack data (particularly sensitive data like their message history).

*   ✅ **DO** adhere to the ‘principle of least privilege’ when thinking about the scopes your app will use
*   ✅ **DO** provide clear reasons for each of the scopes you include in your submitted app. Don’t just tell us what the scope does (we know that already) but rather tell us how your app uses it
*   🚫 **DON’T** include scopes in your submitted app intended for future functionality. We will only approve scopes related to functionality we can test
*   🚫 **DON’T** request legacy/restricted scopes. See [here](#suitable) for more details

In addition to the above guidance there are some additional caveats worth thinking about before submitting:

*   We are unlikely to approve broad access to workspace message/file data (e.g. user token \*:history scopes) without a clear use case that requires them, such as [Real-time Search](/apis/web-api/real-time-search-api/) or [MCP server](/ai/slack-mcp-server/developing/) functionality
*   We are unlikely to approve use of admin\* scopes by apps submitting to the Slack Marketplace who are not part of our [partner program](https://slack.com/intl/en-au/partners)
*   Use of user token scopes should only be used when your app is acting as your authenticating user and action needs to be performed from the user's perspective: for example, reading or starting group DMs for a specific user. We will return submissions where user token scopes are being used unnecessarily. To find out more about access tokens and how they work check out this [doc](/authentication/tokens).
*   Be aware of unintentionally circumventing Slack's product limitations as they relate to access to data. In particular, for workspaces using Slack's free tier, message and file history is limited to 90 days. Your app shouldn't make it possible for people to access message and file data beyond this period.

If you have questions about the above or are unsure as to whether your app would be impacted please drop us a line at [feedback@slack.com](mailto:feedback@slack.com) before submitting and we can chat it through.

### Optional scopes {#optional-scopes}

Optional scopes allow users to choose which additional permissions to grant your app at install time. Scopes marked as required are always included; scopes marked as optional can be accepted or declined by the user without blocking installation. When using optional scopes, keep the following in mind:

*   ✅ **DO** ensure that your required scopes cover everything needed for your app's core functionality. Your app should be fully usable with only its required scopes — optional scopes should enhance the core experience, not complete it
*   ✅ **DO** support a reinstallation flow that allows users to grant optional scopes at a later date. A user who initially declines an optional scope should be able to change their mind and easily re-authorize with the additional scopes
*   ✅ **DO** clearly communicate to users what functionality is unlocked by each optional scope on your app's landing page. Users should understand what they're gaining or missing
*   🚫 **DON’T** place scopes required for core functionality into the optional category to make your app's install prompt appear lighter. If your app can't deliver its primary value without a scope, that scope must be required

The same rules that apply to required scopes also apply to optional scopes: they must relate to functionality we can test, and you should provide a clear reason for each one. Optional scopes intended for future, unimplemented functionality will not be approved.

### AI components {#ai-components}

If your app allows Slack users to interact with generative AI technologies, here are some things to keep in mind when submitting:

*   ✅ **DO** be transparent about the actions the app will take once added to a workspace.
*   ✅ **DO** add a disclaimer to your landing page and long description to let users know of the app's potential to generate inaccurate responses, summaries or other outputs if it uses a LLM.
*   ✅ **DO** disclose the following AI-related information in the relevant fields in the Security & Compliance section of your submission:
    *   Model used if your app exposes Slack users to a LLM
    *   How long users' data is retained and how it is being used by the LLM
    *   LLM data tenancy
    *   LLM data residency
*   🚫 **DON'T** use Slack data to train LLMs.
*   🚫 **DON'T** perform unexpected actions, e.g. apps should not join all public channels by default after installation.

In addition to the above, if you’re requesting scopes that provide extensive access to workspace data or allow the bot to add itself to private conversations, your submission will be subject to an enhanced review, to reduce the risk of unexpected behavior. These scopes include:

*   `*:history`, `files:read`, and `canvases:read`
*   user token `groups:write`, `groups:write.invites`, `mpim:write`
*   `conversations.connect:write`
*   `admin.*`

### Agent or Assistant UI {#ai-agent-or-assistant}

If your app has the Agent or Assistant messaging experience enabled, here are some things to keep in mind:

*   ✅ **DO** add a disclaimer to your landing page and long description to let users know that a paid Slack plan is required to access the AI agent in the app container. You can also let users know that other features will still work on free Slack plans.
*   ✅ **DO** ensure that your app functions as expected on workspaces that are not on a Slack paid plan and don't have access to the AI agent in the app container.
*   ✅ **DO** limit the Assistant Overview to 25 words or less. This should concisely summarize the functionality of the AI agent.
*   ✅ **DO** respond with usage instructions when someone sends help in the “Chat” tab or in the AI agent container view.
*   ✅ **DO** respond with relevant and helpful error messages if something goes wrong. It will be useful if the error messages help guide users in drafting prompts which the app can provide contextually appropriate responses to.
*   ✅ **DO** ensure that a thread status is set after someone sends a message, so they know the app is formulating a response.
*   🚫 **DON'T** store any Slack data you obtain. Store metadata instead and pull in data in real time if needed, i.e. zero-copy.
*   🚫 **DON'T** perform unexpected actions, e.g. apps should not join all public channels by default after installation.

### The privacy model {#privacy-model}

It is very important to understand Slack’s privacy model to ensure that your app doesn’t unintentionally circumvent or undermine how data is managed in Slack. In short: an app should not give people access to information/abilities that they would not otherwise have access to in Slack. Some examples:

*   An app should not expose private channel information (e.g channel name) to anyone who is not a member of the channel in Slack
*   An app should not expose messages/files to anyone who would not have access to them in Slack
*   An app should not allow people to exercise restricted actions they would not normally have access to e.g create channels in a workspace where channel creation has been restricted

It is also worth making sure you understand how to comply with the above in shared channels where you may be dealing with external companies. Check out [this doc](/apis/slack-connect/) to find out more.

These sorts of things can be tricky and the above list of examples is not exhaustive, so if you have questions about the above or are unsure as to whether your app would be impacted please drop us a line at [feedback@slack.com](mailto:feedback@slack.com) before submitting and we can chat it through.

### User emails {#emails}

If your app makes use of email addresses obtained via the Slack API for any reason, you must take special care. If you do need to contact users by email, make sure you get _explicit consent_ from each customer to use any email addresses before contacting them. You can do this as part of the installation process (with an explicit opt-in option before installation), or as part of your app’s onboarding flow.

* * *

## Use case specific guidelines {#use-case}

### Automation platform apps {#automation-platform-apps}

If your app connects Slack to an automation platform (i.e a platform that allows people to build workflows, connecting different services together), here are some things to keep in mind before submitting:

*   ✅ **DO** ensure that your app adheres to Slack’s [privacy model](#privacy-model) especially when it comes to passing restricted information (e.g private channel names) between different services via a workflow.
*   🚫 **DON’T** expose the API token for your Slack app to end users.
*   🚫 **DON’T** request user token `*:history` and `files:read` scopes for the collection of message and file data.
*   🚫 **DON’T** allow your Slack app’s authorization to be shared between users of your service when user token scopes have been requested.
*   🚫 **DON’T** facilitate the creation of workflows/automations that allow users of your service to circumvent Slack Marketplace requirements or any of Slack’s terms of service e.g export/backup of Slack message data, bulk deletion of Slack messages/files, direct access to the Slack API using your Slack app’s authorization.

In addition to the above, while one of the key benefits of automation platforms is their flexibility, it can also allow for the easy circumvention of free product restrictions. Because of this we require that you limit the installation of your app to Slack workspaces on our paid plans. To enable this you will need to request the `team.billing:read` bot token scope, which will enable you to check the workspace plan post-authorization and revoke it if needed.

* * *

## Security {#security}

When using Slack’s API, you should follow our [best practices for security](/security). In addition, we’ve detailed other security requirements for distribution in the Slack Marketplace below. Our team may also perform an advanced [security review](/slack-marketplace/marketplace-terms-conditions/slack-security-review) at any point after an app is submitted to the Slack Marketplace. Please note that your app may be blocked or removed from the Slack Marketplace if it doesn’t meet our security requirements.

### OAuth and tokens {#oauth}

When building for the Slack Marketplace, you'll be working with credentials from Slack and API tokens granted through an OAuth flow. It’s important that you [handle these with care](/security).

Your app must store API tokens securely. They should never be logged, stored in client-side code and public repositories, or made accessible to end-users. When your app is no longer supported, these API tokens need to be invalidated by deleting your app from your app settings page.

To prevent [forgery attacks](https://tools.ietf.org/html/rfc6749#section-10.12), your app must use the `state parameter` when requesting access to customer data during the [OAuth flow](/authentication/installing-with-oauth).

### TLS {#tls}

Your app needs Transport Layer Security (TLS) to encrypt all traffic between clients and servers. As of [February 19, 2020](/changelog/2019-07-deprecate-early-tls-versions), your app must use TLS version 1.2 or greater to continue using Slack endpoints.

### Authenticating requests {#requests}

Your app may have configured endpoints for certain interactions, including slash commands, actions, interactive messages, menus, and the Events API.

Before your server responds to a request, you must verify that any requests received at these endpoints are authentic by using [signed secrets or mutual TLS](/authentication/verifying-requests-from-slack). These methods should be used instead of verification tokens, an older form of request authentication which is now deprecated.

The signing secret should be protected like a password. If accidentally exposed, you can regenerate it from your app settings.

### Security incidents {#incidents}

If you have any reason to believe that your app security has been compromised, contact our team at [feedback@slack.com](mailto:feedback@slack.com) as soon as possible.

* * *

## Post-approval requirements {#post}

Your app being approved is only the beginning! As a member of the Slack Marketplace there are certain ongoing requirements that you must meet to maintain a good experience for our shared customers.

### Maintaining your published app {#maintain}

To provide everyone with the highest quality experience when using apps from the Slack Marketplace we have some expectations around your app's performance, maintenance, support, and security standards:

*   **Your app's listing is kept up to date.** Any changes to functionality, pricing, visual appearance, or any other updates should be accurately reflected in your app's listing.
*   **You provide timely support to customers.** If we hear from customers that they’ve not received responses from their support requests, we will reach out to you. If we do not receive a prompt reply to our own messages to you, we may de-list your app.
*   **You regularly update your app to ensure that it makes use of our newest platform security features.** We regularly add new security features to our API, so please make sure you’re using those that are applicable to your app. Stay up to date with those new features by subscribing to our [changelog](/changelog).
*   You keep your app contact details up to date and are responsive to messages from us. We will occasionally need to get in touch with you with questions about your app, to resolve any issues, or in the case where your app is subject to security testing. Please make sure the developer and support contact details in your app submission are kept up to date so that we can contact you easily. Otherwise, you may miss important notices from us.
*   **You must add a collaborator to your app.** Adding app collaborators ensures that multiple people can access your app’s configuration, in the event that the app creator leaves the [associated workspace](/app-management/distribution). Edit your app's collaborator list by going to your [app's settings dashboard](https://api.slack.com/apps) and clicking into the Collaborators page.
*   **You must resubmit your app for review when you make [substantial changes or updates](/slack-marketplace/distributing-your-app-in-the-slack-marketplace#updating) to the features, purpose or functionality of your app.**
*   **Your app is being actively used.** We want the Slack Marketplace to provide people with a choice of useful and used apps to help make their work days more productive. If your app is published in the Slack Marketplace but it is not being used, we will reach out to you to learn more about your plans for the app. If you do not plan to update your app, or people continue not to use your app, we will delist your app after communication with you.
*   **Your app's functionality and customer experience matches or exceeds the quality of experience at submission, and you maintain your app’s performance.**

### Possible enforcement actions {#enforcement}

In order to maintain the health of the Slack Marketplace and provide everyone with the best possible experience, there are circumstances in which we will contact you and possibly delist or take further action on your app.

We may contact you for response when:

*   our [expectations for published apps](#maintain) are not being met;
*   we hear about issues from our mutual users, including but not limited to: spammy app behavior, broken or unexpected functionality, poor support experiences, lack of responses to support requests;
*   we see increased instances of your app being uninstalled;
*   we see large numbers of errors for your app;
*   the support page or privacy policy page links for the app are broken.

If we do not hear back from you after reaching out to you for any reason, we will reach out again while simultaneously delisting your app to protect users. If we hear back from you, and confirm that issues are resolved, we'll be able to re-list your app.

We may delist your app without prior notice (other than to inform you of that action) when:

*   your app's landing page or installation flow are broken
*   your app appears to be unmaintained or abandoned
*   your app's functionality changes substantially without notice and without the app being resubmitted for review.

We reserve the right to revoke access and tokens for your app if we receive no response from you about security-related issues.

### Discontinuing your published app {#discontinue}

All good things come to an end. If your app is no longer being actively maintained or developed, you should ensure you adequately sunset your app. This means:

*   Removing it from the Slack Marketplace. You can remove your published app from the Slack Marketplace in the **Published app** settings section of your app's settings dashboard.
*   Contacting the Slack Marketplace team
*   Contacting your customers where appropriate
*   Deleting and revoking any tokens your app generated

* * *

To find out more about the nuts and bolts of the Slack Marketplace submission and review process check out this [guide](/slack-marketplace/slack-marketplace-review-guide).