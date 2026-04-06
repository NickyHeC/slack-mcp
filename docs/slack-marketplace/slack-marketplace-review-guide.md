Source: https://docs.slack.dev/slack-marketplace/slack-marketplace-review-guide

# Slack Marketplace review guide

In the Slack Marketplace, we connect Slack customers with new or existing services and tools they can use in Slack to make their working lives simpler, more pleasant, and more productive.

The apps published are ones that our review team determines to be high-quality, reliable, and useful.

Coded workflows are currently not eligible for listing in the Slack Marketplace.

In this guide, we’ll walk you through what you need to know to ensure your app is submitted correctly to be listed in the Slack Marketplace.

* * *

## Before building your app {#before}

### Ensure your app will be supported for listing {#ensure-support}

We won’t list apps in the Slack Marketplace if they don’t follow our [guidelines](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements) or [policies](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements#policies), so make sure to familiarize yourself with this documentation before getting started.

At a high level, the Slack Marketplace is not the right place for your app if it:

*   Uses scopes that we don’t accept for the Slack Marketplace.
*   Is something that you’re building for fun or that you’re building for your own team internally.
*   Doesn’t yet have any customers or isn’t fully built out.
*   Breaks our policies or Slack’s privacy model.
*   Provides a low quality or confusing experience for customers.
*   Enables financial transactions, including cryptocurrency transactions, or the minting or transfer of NFTs in Slack.

*   Does not include functionality in Slack.

In addition, coded workflows are currently not eligible for listing in the Slack Marketplace.

Read more about the kinds of apps and functionality that we don’t support for listing [here](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements#suitable).

### Communicate with your customers {#communicate}

As you’re planning your app’s features and functionality, and before you start building, make sure that you’re talking to your customers about how they use Slack and what they feel is missing without having your service integrated into their own workflows.

It might be that customers want to be notified of actions that happen in your service, or that they want to be able to search for information right from Slack. Taking time to get to know how your customers use both your service and Slack can help you discover problems and solutions that your customers need help with, even if they wouldn’t explicitly call those problems out for you. This leads to building an app that truly provides value to your customers.

### Understand the review process and timeline {#review-timeline}

In the early phases of your app building process, you should know the timeline for listing your app in the Slack Marketplace, as well as the [review process](/slack-marketplace/slack-marketplace-review-guide#review). You can see the estimated turnaround time for reviews when you go to the submission page in your app settings pages. It's important to account for these in your project planning and timelines, as we will not be able to skip or accelerate the review process in order to coordinate with your launch.

After your submission, we often have feedback during the review process that you will need to address before your app can be listed. The more closely your app follows the [submission guidelines](/slack-marketplace/slack-marketplace-review-guide), the less feedback there should be, but we strongly recommend that the timeline for an app’s launch includes your app’s submission and review as a milestone with at least a few weeks to spare.

**Before moving on, ask yourself:**

*   Is the app I’m planning appropriate for the Slack Marketplace?
*   Will my app provide customers with a high quality experience that makes their working life simpler, more pleasant, and more productive?
*   Have I spoken to my customers to understand how they use Slack and how they imagine my service/app working in their workspace?
*   Have I read through the Slack guidelines and policies listed above?

* * *

## As you're building {#as_you_build}

### Constant feedback {#customer-feedback}

You’ve started building — that’s great! Our biggest piece of advice is to get customer feedback along the way. A helpful way to do this is to put together a beta group of customers who are going to test and use your app once you’ve [distributed it](/app-management/distribution). Learn from their feedback to make it useful, to iterate on the product, and then to run a pilot with them to get real-world feedback. This allows you to understand how your customers use Slack alongside your product and will lead to building a truly high quality experience.

_Think about the experiences you’re building!_

As you're planning your app's functionality, here are a few tips to help you:

*   Think carefully about the [scopes](/reference/scopes) you’ll need. You should be building your apps with the guiding principle of least privilege. Focus on requesting the smallest number of least permissive scopes you can while still providing a good experience.
*   Consider the differences between [bot and user token](/authentication/tokens) scopes and how you can minimize data access while still providing a positive experience for your customers.
*   Build with Enterprise in mind: build an [Org App](/enterprise/organization-ready-apps), understand multi-workspace channels and privacy, and build great onboarding flows.
*   Consider how to make your users feel welcome, and help them use your app with a [great onboarding experience](/surfaces/app-design#onboarding).
*   Think about how you’ll communicate with your customers. Building an [App Home](/surfaces/app-home) is a great way to do this, as it can show content customized to the user including onboarding information, instructions on how to use the app, and updates to functionality.
    *   You cannot send emails to users who install your Slack app without their explicit consent, so be sure to keep this in mind while building your onboarding flow. The **App Home** is a great place to request their consent.
*   Ensure your app doesn’t allow manual mapping of users between your service and a Slack account. Take a look at our [best practices for account binding](/authentication/binding-accounts-across-services).
*   Understand Slack’s privacy model:
    *   Users in Slack can only access content in either public channels or the private channels to which they’ve been added. Slack admins have some powers that other users do not have, but they cannot gain access to private channels or even see the names of those channels unless they are already a member. Your app and any associated web app should only ever grant access to content that users can already access in Slack.
    *   You should also be mindful of guest users (who have access to only a restricted number of channels) and Slack Connect channels (where an external user might be able to access content from your app in a shared channel).
*   Review our [security recommendations](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements#security) to ensure your app does not put your users at risk.

* * *

## Submitting to the Slack Marketplace {#submitting}

You’ve finished building your app, tested it, and implemented user feedback, which means your app is ready to be reviewed by the Slack Marketplace team, hurrah!

In the next section, we’ll walk you through when and how to submit your app to the Slack Marketplace. Be sure to read this carefully, as it contains information that will lead to a successful review. If we don’t have the information we need, or your app is broken, it will be returned to you, which resets your app’s place in the review queue and prolongs the process.

### Prerequisites {#prerequisites}

Before you submit your app for listing in the Slack Marketplace, please ensure:

*   Your app is fully functional, publicly available, and can be installed correctly.
*   You've tested, tested, tested! This means you have thoroughly confirmed your app's installation flow, set-up process, and end-to-end functionality, _including uninstalling it_, on a workspace that is not your development workspace: you should run through installation, onboarding and usage of the app as a brand-new customer might, which is how we’ll approach our review.
*   **Your app has been installed on 5 or more active workspaces** and the service has been tested on those workspaces in accordance with the above bullet. An active workspace is a workspace that has been used in the past 28 days. Please note: apps that do not meet this requirement will be blocked from submitting to the Marketplace.
*   You are prepared to maintain your app and to provide good levels of support to the customers who choose to install it.
*   Your app meets our guidelines in their entirety. There are certain kinds of apps that are not currently accepted for listing. Please [read about those](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements#suitable) before submitting your app.

Please do not submit your app for review if it's in private beta, still being built, or hasn’t been fully tested. Your app should arrive at the review stage as it would in your customers’ hands, which means bug-free and fully functional. _We will return submissions that are not ready for review._

If your app is submitted with bugs, poor user experience, or we repeatedly run into issues of low quality when reviewing, we will return it and ask you to spend more time on it before resubmitting.

### When to submit {#when-to-submit}

Our review turnaround time can vary depending on volume, so please take a look at the estimated time for review listed on the submission page of your app settings to plan your launch timeline.

Currently, the preliminary part of the review takes up to 10 business days to receive feedback, while the functional review takes up to 10 weeks for new submissions and 6 weeks for published apps resubmitting changes.

If you are planning a launch or an update, please note that we’re unable to shorten or skip the review, and depending on the preparedness of your app at submission, we may require multiple rounds of feedback.

Make sure to submit as early as you can before your launch to allow time to action any feedback you receive during the review process. All feedback must be addressed before your app can be listed. Once approved, you can publish your app at the time of your choosing, so submitting with plenty of time before your proposed launch date will give you a buffer to publish on time.

### How to submit {#how-to-submit}

Your app submission (and subsequent updates to your app) happens from the **Submit to the Slack Marketplace** section of your app's configuration page.

As part of the submission process, you will be asked to review your app listing information, your app’s scopes, and to provide us with any supplementary information we need to test your app properly. We recommend that you review your app features separately before submitting to make sure that you haven’t left any test slash commands in by accident.

Before you can submit your app, we will run some automated tests on your app. Once you’ve fixed any issues we detect, you can submit your app.

### Help us review {#help-us-review}

We aim to provide you with as smooth a review experience as we can. To help us do that, we request that your submitted app be in a production-ready state. We also require that you provide us with test account credentials needed to access your service (or any third party service your app connects with) in order to install and fully test your app submission.

This means that if a paid account is required for your service, you’ll need to share login credentials with us for an account with the required level of access. If you choose to provide us with a free trial account, please make the free trial as long as possible, since we might need to test over an extended period of time.

Wherever possible, please provide us with test accounts that include dummy data, particularly if your app connects to another service beyond your own. If a test account is required to connect other services to your app, please provide the login credentials for those 3rd party services in the “Test account details” section of the submission flow.

We can only access any test accounts or email accounts created specifically for testing purposes. We cannot access any Slack workspaces (even created for testing), so please make sure to provide us with a way to install the app ourselves, rather than your test Slack workspace credentials.

#### Demo your submission {#demo}

You can help us review your app more quickly by providing us with a short video demo. For a new submission, it should include a video showing the full installation and OAuth flow, set-up process, and end-to-end functionality, including uninstallation. This will help us greatly when it comes to performing our functional review of your app.

If you’re submitting updates to an already published app, your video should demonstrate the new functionality you’re adding.

* * *

## The review process {#review}

The review itself consists of the Slack Marketplace Team checking your app against our [guidelines](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements).

After preparing your app for submission and addressing issues caught in the automated feedback section of the submission process, your app will move onto the manual review.

There are two main parts of the review:

1.  Preliminary: confirming the app is ready for review
2.  Functional: installation and testing of the app

### The preliminary review {#preliminary}

This section includes a review of your listing information, accompanying documentation and links, and a quick look at the reasons you’re requesting each scope. We’ll also check that we have the information and access required to install your app. We may install your app to check that OAuth is working and that the app is ready to be reviewed, but we won’t begin testing your app at this point.

If we find any failures in this first part of the review, we’ll return your submission with that feedback. This includes issues we run into when trying to access and install your app.

Feedback from this part of the review generally takes up to 10 business days and you'll need to make all of the requested changes before your submission can be moved to the next part of the review. If these changes aren't made, or there is information missing from your submission, this step is repeated until the requirements are met.

During this part of the review, your place in the queue is reset each time you resubmit. This restarts the timeline for the next part of the review, so be sure to take a look at our submission guidelines before you submit. The more closely your app follows these guidelines, the less feedback there should be.

### The functional review {#functional}

Once your app enters this stage of the review, your submission will be assigned to a reviewer and you’ll receive feedback about your app’s functionality and associated scopes. Feedback from this part of the review generally takes up to 10 weeks for new submissions and 6 weeks for published apps resubmitting changes (though we try to handle small changes like copy/URL edits much faster). Once your submission has been assigned to a reviewer, your place in the queue is not reset when you resubmit with changes.

We may run into bugs and issues you may have missed, and we’re always happy to point those out. However, our review is not a replacement for Quality Assurance testing. If we run into frequent bugs that prevent us from fully testing the app’s functionality or that provide a poor user experience when reviewing, we will return your submission and ask you to develop it further before resubmitting.

### How we approach scopes {#scopes}

We can only review and approve scopes and functionality that are already available within your app (that we can test or see comprehensive demos for). _Please do not submit your app with scopes for a feature that you plan to build at some point in future._ In addition, you’ll also need to ensure that your app does not request legacy/restricted scopes, scopes that provide extensive access to workspace data, or coded workflow scopes (e.g. `identity.*`, `workflow.steps:execute`, `read`, `post`, `client`, `admin.*`, `search:read`, `triggers:*`).

With that in mind, we also encourage you to consider how you’ll communicate with your customers through the app when you do have updates that require the app to be reinstalled (such as adding scopes). Using the [context block](/reference/block-kit/blocks/context-block) in a message or sharing the updated OAuth link in your app home are great ways to alert your customers to updated scopes and functionality.

### Feedback {#receiving-feedback}

You’ll receive our feedback from the review within the submission flow in your app settings, as well as email notifications about the status of your submission to the email address you entered during the submission. You can review the feedback, address each point, and then resubmit when ready. At this point, we’ll confirm how you’ve addressed the feedback and either send your submission back with more questions, or finish the review for you to publish your app and changes.

When your app or the updates you’ve made to it have been approved, you’ll be able to publish at your own convenience from the app settings page.

* * *

## Updating your app {#updating}

Once your app is published in the Slack Marketplace, the live version of your app is locked. This means that you will not be able to make any changes to your app’s configuration, features, or scopes without re-submitting the app for review.

Additionally, any updates you make in your app that may be affected by your Slack app configuration (such as scope changes or updated redirect URIs) will not work until you have submitted and published the changes. You will also need to manually update your OAuth urls to include any new scopes after approval. If you try to make changes to your live app, it can break your app's experience for users; e.g., if you update your app’s install link to add new scopes that were not previously reviewed, your app will show customers an error and they will not be able to install it.

![Rich text app error messaging](/assets/images/app-review-error-c4fe6f0211d17f9cd90c17b3512a86fc.png)

When you need to make changes to your app, deploy the updates with a test or staging app that will be identical to your published app so that you (and we!) can test during the review process.

For example, if your app is `cycling_tips`, create a staging app called `cycling_tips-dev` that can be [distributed](/app-management/distribution). Use this staging app to test updates to your app's functionalities such as adding a new feature, scopes, or events. You can create a copy of your app for dev/staging using [your app’s manifest](/app-manifests/configuring-apps-with-app-manifests).

After testing your changes, submit them for review, and tell us about the changes you’ve made in the **Testing Information** section. You should also include a link to your [publicly distributed](/app-management/distribution) staging/test app's OAuth flow so that we’re able to install a version of your app with the changes for testing. The staging version itself does not need to be submitted for review, but we do need a way to install it.

Once your update is reviewed, you’ll be able to choose when to publish the changes to your app, allowing you to coordinate when you deploy your changes.

**Changes that don't require a test app:**

*   Updating Display information (app name, descriptions, icon)
*   Changes to pricing, languages your app supports
*   Adding another instance of an existing functionality

If you're making small changes to your app's long description or app name, a test app isn't necessary, but we may still ask for one.

**Changes that will require a test app or video demo:**

*   Enabling new functionalities for your app
*   Toggling on **Messages** or **App Home** tabs for the first time
*   Adding new scopes to your app

In cases where you've added significant changes to an existing feature (such as a different shortcut or slash command), we may ask for a staging app for testing.

* * *

## Being listed in the Slack Marketplace {#listed}

Now that your app is listed in the Slack Marketplace, make sure you review the [requirements for listed apps](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements) and the possible [enforcement actions](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements#enforcement) if those requirements aren’t met. You can also stay up to date with platform and Slack Marketplace updates by subscribing to our [changelog](/changelog), signing up for our [developer newsletter](https://slack.com/blog/news) or joining the [Slack Community](https://slackcommunity.com/).

### Featured apps {#featured}

Remember that feedback loop you created with your customers when you were building and testing your app? That relationship you’ve built with them will continue to serve you well as you engage them to get feedback on new features. As you grow your app’s functionality, you’ll naturally want to share that with a wider group of customers, and that might include being featured in the Slack Marketplace.

We regularly feature apps in the Slack Marketplace that we believe will meet customer needs. Our goal is to share apps that will make customers’ working lives more pleasant and more productive. As part of our review process, we look for high quality apps, taking into account the way an app uses Slack API features, the value the app provides customers during their workday, and the overall quality of experience.

Do you think your app would be a great fit for us to feature? We'd love to hear from you! Give us feedback and tell us more about the value your app is providing, any recent updates or improvements you've made, or feedback you're hearing from customers. If you're planning a big marketing launch with an update to your app, feel free to include links to blog posts you're using so that we can learn more about the new additions to your app.