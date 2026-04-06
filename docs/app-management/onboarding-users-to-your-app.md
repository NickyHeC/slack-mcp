Source: https://docs.slack.dev/app-management/onboarding-users-to-your-app

# Onboarding users to your app

Your app only has one chance to make a first impression with users, so it's worth the time to make your onboarding experience a great one. Your app should provide a great experience for everybody in a potentially diverse audience.

When people first interact with your app inside of Slack, they may have varying context about your app and what it does:

*   They may have used it before
*   They may be familiar with your app on another platform, but using it in Slack for the first time
*   They may have seen others on their team using the app, but have not used it themselves
*   They may know nothing about your app at all

Your onboarding should equip people to get something done as quickly as possible, no matter what context they have. Determine the key tasks you need a user to accomplish in the first 30 seconds of interacting with your app, and design your onboarding to help them get it done.

## When to start onboarding {#start}

Since we don't recommend DMing users out of the blue, your app will need to cue off events to begin onboarding. One such nifty notification is the `app_home_opened` event. It lets you know that a user has clicked on a DM with your app, entering the [**App Home**](/surfaces/app-home) space. It's the perfect time to begin on an onboarding flow.

Many events can trigger onboarding, though, so it's important to make sure that you're looking out for more than just `app_home_opened`.

For example, if a user invokes one of your app's slash commands, their onboarding should start then, rather than waiting for the `app_home_opened` event. Relatedly, this user's onboarding would take a slightly different form, because using a slash command indicates a different level of expertise than clicking on your app to interact with it.

## Say hello 👋 {#hello}

It's a good idea to have an app announce its presence and teach people how to interact with it. There is, however, a fine line between being informative and being spammy. Here's how to do it right:

**Have an informative, concise welcome message** When someone installs your app, it's a good idea to DM that person with a welcome message. A welcome message should be concise, and clearly state what your app does, while including instructions on how to use it.

![welcome message from donut](/assets/images/donut-welcome-message-optimized-f86f40a19113078886c21102311ad8dc.png)

🧠 **Thought Starter:** What is the call to action for the user installing your app? Should they add your app to a specific channel? Should they (or their admin) link a 3rd party account?

Make the _call to action_ clear and actionable from your welcome message. Without a clear call to action, it's likely that the installing user won't configure your app properly and won't get the full value from it.

**Introducing yourself to the team** _Do not DM the entire team_, as unexpected messages from an app can prompt uninstallation. Only the installing user should receive a direct message from your app.

If your app has a bot user, it should say hello when it's added to a new channel. In addition to explaining the app's purpose, the bot user should give a quick explanation of how to use your app and what configurations have been set (if any). For example, if your app is going to post a daily update at 10am, that's helpful to know.

💡 **Design Tip:** If your app has help documentation hosted on your website or if people can DM your app for help, now's a great time to let them know.

![DM from taskbot with field prompting users to DM taskbot back](/assets/images/taskbot-intro-message-optimized-067959b2911e3156d0d28dce288d0c1b.png)

**Make deeper dives opt-in** Your welcome message should contain enough information to help someone complete a task for the first time. That said, you may want to help people use your app beyond the first quick-win scenario. Let people choose to have an extended walkthrough for more complex tasks, especially if your app allows users to do more than one thing.

🧠 **Thought Starter:** Any non-essential onboarding past an app's welcome message should be skippable. Some users who appear new may have used your app before on other Slack teams. Others will find your app intuitive enough that they'd prefer not to be helped. Design with user optionality in mind --- in other words, let users choose when to skip non-essential onboarding.

## Offer help {#help}

Onboarding is really about proactively helping people use your app. That said, even after a well-designed onboarding experience, users may still have questions about your app or may come back later and forget the onboarding you led them through.

**Provide a help action** When slash commands are a central part of your app's experience, it's common practice to provide a help action, e.g. `/myapp help`, that will offer the user assistance. Perhaps provide more information about your app and listing your app's commands.

If your app is more conversational, then reply in your app's DM when a user asks for help or your app doesn't understand something a user says to you.

![Doodle Bot offering list of helpful tips with embedded video](/assets/images/doodle-offer-help-optimized-3d8f82ad153c137604ddc351368bb730.png)

💡 **Design Tip:** If you're designing an app with more than one workflow, it can be helpful to offer a select menu in your help message that gives users the option to kick off any of your app's workflows to see what they are and how they work.

**Respond when your app is @mentioned** When your app is **@mentioned**, a user probably wants to use your app or doesn't know how to use your app but wants to learn. This is another good moment to surface help to the user and allow them to start using your app as quickly as possible.

⚙️ **Development Tip:** Listening to `app_mention` event in the Events API will send you a payload every time someone directly @mentions your bot user.

**Help and feedback sometimes look alike** People don't just want to reach you when they're critically stuck. Sometimes, they'll want to give feedback on things like the ease of going through a particular workflow, or whether a bot successfully understood their intent. If you have a place to route feedback requests, provide a way for people to get there inside Slack. _Only offer a feedback channel if you plan to collect and review feedback._

## Make your app visible {#visibility}

There are a few things you can do before your app is event installed to help potential users discover and install your app.

**App suggestions** If a user posts a link from your website into channel, there's a good chance they might want to install your app. As part of the Slack Marketplace, your app can suggest users install your Slack app when links associated with your domain are posted in a channel. This helps users less familiar with the Slack Marketplace (or with Slack apps in general) find your app in the first place.

![user posting taskbot link, response from slackbot to install taskbot](/assets/images/taskbot-install-prompt-optimized-6d6074ed1fbf265acb4132784e867ced.png)

You can find HTML code to embed on your website on your app management page. Learn more about app suggestions in [our Slack Marketplace guide](/slack-marketplace/distributing-your-app-in-the-slack-marketplace#suggestions).

**Install directly from the Slack Marketplace** Direct install creates less friction for people thinking about installing your app. Instead of redirecting them from the Slack Marketplace to your site to install the app, you can provide a Direct Install URL, which redirects the current user to Slack's OAuth authorize step directly.

[Learn more about Direct Install](/slack-marketplace/distributing-your-app-in-the-slack-marketplace#direct_install) in our Slack Marketplace guide.