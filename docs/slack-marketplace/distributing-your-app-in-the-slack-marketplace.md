Source: https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace

# Distributing your app in the Slack Marketplace

The Slack Marketplace helps users discover apps. The apps published are ones that our review team determine to be high-quality, reliable, and useful.

In order to commercially distribute your app, you must submit it to the Marketplace.

In this guide, we'll help you prepare your app for submission to the Slack Marketplace and outline that submission and review process. We'll also show you how you should maintain your listing after a successful review.

* * *

## Preparing your app for submission {#preparing}

The process for getting apps published in the Slack Marketplace involves a manual review by our Slack Marketplace team. They will ensure that your app meets the quality and utility standards of Slack Marketplace apps.

There are a number of steps to follow before submitting your apps, so let's walk through them.

### Check your app is suitable {#types_not_listing}

Before we go further, it's important to note that there are some types of apps that we aren't currently accepting in the Slack Marketplace. This includes apps that:

*   export or backup message data.
*   do not include functionality in Slack.
*   use legacy/restricted scopes or methods, scopes that provide extensive access to workspace data, or coded workflow scopes (e.g. `admin.*`, `identity.*`, `search:read`, `workflow.steps:execute`, `triggers:*`).
*   facilitate destructive behavior e.g., 'self-destructing' messages, bulk file deletion, bulk message deletion.
*   embed Slack into another site.
*   only use [Sign in with Slack](/authentication/sign-in-with-slack/) functionality.
*   replicate Slack client functionality, or are third-party Slack clients.
*   unnecessarily request a large number of scopes when there is a less permissive option.
*   share sensitive personal information, such as financial or health information, in Slack.
*   circumvent product restrictions or admin controls in Slack.
*   do not add value to the experience of using Slack.
*   enable remote execution on a server via a downloadable third party script e.g., terminal commands from Slack.
*   facilitate the sharing of third party service accounts between multiple users.
*   are installed on less than 5 active workspaces. An active workspace is a workspace that has been used in the past 28 days.
*   are in private beta, still being built, or have not been fully tested.
*   enable financial transactions, including cryptocurrency transactions, or the minting or transfer of NFTs in Slack.
*   use Slack data to train Large Language Models (LLMs).
*   perform sentiment analysis/insight generation (unless the insights/analysis provide very clear value to customers, are limited to an aggregate level, and it is clear how they are determined).

In addition, coded workflows are currently not eligible for listing in the Slack Marketplace.

This list is not exhaustive-the Slack Marketplace team may use their judgment to deny any app from being listed-but it's useful to know upfront when your app is not suitable.

If you think your app _is_ suitable, keep reading to see the kinds of policies that listings in the Slack Marketplace are subject to, and how to prepare your app for review.

* * *

### Prepare your app for public distribution {#distribution}

If you haven't enabled public distribution for your app, follow [our guide to distributing apps publicly](/app-management/distribution). This is a pre-requisite for submitting your app for Slack Marketplace review—you and your app won't make it far without doing this!

* * *

### Read our terms and policies {#policies}

By distributing your app through the Slack Marketplace, you agree to abide by the following core policies and terms:

*   [App Developer Policy](/developer-policy)
*   [Slack Marketplace Agreement](/slack-marketplace/marketplace-terms-conditions/slack-marketplace-agreement)
*   [Security Review](/slack-marketplace/marketplace-terms-conditions/slack-security-review)
*   [API Terms of Service](https://slack.com/terms-of-service/api)
*   [Brand Guidelines](https://slack.com/brand-guidelines)

Apps that do not follow these terms will not be accepted in the Slack Marketplace.

* * *

### Security and Compliance {#security}

You'll add **Security & Compliance** information during the Slack Marketplace submission process. [Read our Slack Marketplace Guidelines for more information](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements#security).

### Providing a great experience {#experience}

Beyond the strict policies and terms mentioned above, the Slack Marketplace team will generally ensure that your apps provide a great experience for users.

There are some resources that can help your app reach this point:

*   Our [design guidelines](/surfaces/app-design) provide tips for making your app as pleasant and productive as possible.
*   Our [guidelines for the Slack Marketplace](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements) outline how to raise your app's descriptive info to the Slack Marketplace listing standard.

### Make installation more direct {#direct_install}

Typically, Slack Marketplace apps must present users with a web page containing a link to Slack's [OAuth](/authentication) installation flow. As users browse apps in the Slack Marketplace or a Slack client and encounter an app they want to install, they first must visit this page to initiate installation:

![Install from your landing page](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAdwAAADsCAMAAADpcOfeAAAANlBMVEUAAADo8u7r6+spqXkCAgICAgIAAAAAAAAAAAAAAAD5+fnd3d3///9RuZKW1b15yavM69+x4M6fSd+5AAAACnRSTlMB/p3/GhQiBQ4JOGeghQAAAAlwSFlzAAALEwAACxMBAJqcGAAADQpJREFUeNrtXeuarKYSXaB9TKvT57z/UybT6oTdDZwf3lDRvszsRHBV8s1u5SKyrKIoigIgkUgkEom0L8peuLuDhs1SsufbOmbLsrAhE5uvqSZvp5ABUBlU5lwpdDeGbNMuGS7H+yqb55n1/JBhkXOea8g3b+aiHZ7WrNTd3va0GyqDgq9Jaw1W/qaorS+trWL61PXM74CbbXYraU+kMvUCuEQ1DoDFI1ksDeRBO8zI/VdrnMFIPQHuiCsZIohP0KyNv2IF2imwFhAW3Z/HSpp9Kqew27naxI0sQ5OcPN3PSdlF0wWsr7aHD3z4Wm3Fk0x9pdslp6ne9nmeJWb8q7bBzSbQWvJFKLMdL7w+0SslAGtth63G8K/W/Y/+/+5Wl0sPl2NB7dbRJWjo7r7WWrt1tDe6asf7elpB3xDdlXAeoTXQVa8nlThZMGu31tqtZdLisXj/zm4fLF9R6/ExTnbt6RPtJDnv49xz63fewrm2HU5SPtSWsx5v66nUT4n+3qeX6GkdifbVuPKURG+1oE3YKuo+87sv8nIvdfecpDeakIwwmgXrii1of+v7kn7qo0k6IM1cMs/B7bHVji5F2ul4O2hUHbxzdMUKttqe37BXRkABfsziK5kwr1pi5WCr9R/vGaMJ7r9EfyfJAK6aD8jdgCsAC23vZxwW3DAp/SUkICCERaoXUyHVXlgA+szeCo3OWg9SJ1uAm/W/Nf5gX4VHf6BFV3qMGNk44nD+EyQ5tg2PDbkVyhoUyuFqgnbT/Kg5sw111O1kroNoGv404N+kL+Q741/Rrsm7nJuNiBPh56EVeb7nGbpcSGXS09jm2J1SNYGU3hYRYbvFuZZSOWhsLaAn+ElK5Tdpl3ybeDiXvqxv6MnYpSWjxTRzwFUEKwbGtbONCHI2E+KQi3g2dg2ca9gjiMQMaRZjriTTIhJnVzkVy4+cXUkBkFwRy6SXqdldi8xCa5Kc5sbIuRTC+OYK2443mHjG3ISYhSyXHbGcUSx/j3Wb3ZqoPGKZTqsxoLsCrqVYjgxd6a4bUCy/iK7dN7zpo1g4pG14g5kcUSxHPPOlWI4YXHIuOZcUrEGSRHBJoYBLH6qIweU8NxZKlg5y1JYRr4MciQoVCfvfX895buxjLjmXYplE2zJph2NuyjEXMcXEwCq4pFf3X+fhuNmQgo+bsNSWaVqOPyYGKS5sCS6iionBMTfimBgecBXnuTEyLm3LOMrCAQnxLhxQLIOuraS9i2W13MJJzkXwe6/hd7NhqKIoxTK3cCKWmBh+2zIjyEUhl/1jLudEUeyrT1ZdW6lQBY+u5ph7pJgYXM+NJiZGsnCz4apQNDExdMJVIRzPtswxF7GsCmU0P8ZLamF+JOdyyY8E2pZJ/65U5jw3ToUqm3MuFaooxbKiQsX9uSSCSyK4JO6sJ+ElI4agbRkRH9RIzuV2EhJ3HJCw44An3fEkCdFFfNFsMnJutNFsqFBFHM2GY+4BotmQcxnNhgTsNSgG57mHimZDOkA0GxK45Eei+ZFEziX9A+AK9gZiiWaj5q6tjGaDGLeTcAsnYolmo1djYlChiivK2Mu25YaQBRIR4w3OPYPSdsfoJiv7c/Gydx1idh0ME13/zvrnI8jZaCVzY4OPZjMh0eMsYQENC8lzpMKku4FovdKNTyxTW+YRqySE5JTOrfWI17bMEHJcFSIxVBEJO1oVorbMzdekEEMV9doyOTeaMTcj5x4isCd3+cW/s56cy2DaJMbEING1lfRPgGs55kYz5tJCFb0RYxLN5jn6+ojU0SZPVYyhijIAEM95EH2VNWJ1a82rc7Rj7lNURuy53JRfh17PzaL2Sm8+Dr0qdAfouBwr53I7SRCU0UIVr21ZEVwwJgYJoRkxFBcO4qWM4MaOLsHFIc7PpScGdxyQgnGz+f5m3BKohotcwjSlxOckSyFttVXDPD9eW8t5uXT5iUvV/Y1NW05+lHOF1sVwUWktoW+3YtKX5q7zjUinQ/6NSKjrSdXsac8ULQoL2KKwB9pOgjetsYO9OS8As4pDYS+bIJzX+/piVwEsHugKZ5sDRxPLPxWHqjKQ5SjkT00jTTqBqToZ2Wx8SF1++Z49PzHpPfC4yL/L+3Ey5r53rlBqet+6/AbcgXq+mfuzvfFrBb4uv31vLara3jou9dEPjfqW+dEC97zpOrKWQN4truTSCtOgv5HbMakdi20bGadLlgY52vShZJ9TI+mLlhaTtK400CAXQ6id0kJUXZtkV3ReklOhx9SkvVvsJ3ABkFibA/mH1UbbS47c2qodUW92VJuLszbGmrLL/2HvgLVWDiWLcTDWwM3aBECRaeOmAam1OZBanRtrTJtSZtoYbQpczjdAWyuAy1kbo6uc4L6lUuWFG86quiM9pbg50humrv87qNAwpxSDwipqAHVdA7m+Iz3VMIP6VbdFBVAYiTQFzIdH/hZ1CpgCyLU06akuJExXq8DHDSatUWjuz31Zpcp7dcpRnE/Xz6tIujvN9QRkUl5HF/jk8yqS3tvuU9aAlLJCJZFcP6XEreOyRqZAKuUnSoNaXK+ixr1cNONLyKsEroAATtdPmWhUMgVKKSvoVKqrlJDFwcbcVnEWb8/6UoMEwJ/FVPGxwLpnw1/FiuNDbnH6BFCfl3sgBHCpgKa0nv0RZQPUmSy+kJhO1Vq4WNjYbaxLC5X65hbO+ow7ULbqVN+ZZ9zNZV1/+d8N9mI8FiJh0c6Hb0scfslW7jfnNf35qwBgAO2t+2Axw+WPvHUKFBCtOuV8Q4W2H2sKzL0Gbtp4heT9drvdbp4WyZ4DzeYEtkqBmz7PTCblxZwtY2K8M3W+5vdpdNBKnAzQGR59LsJJChSm9KSdREvXd9tzTVIAN1frKjN9K+r0uEaM92dDmSxEN1a6o1z5Wcg1fbwB8vQ2atPuZsM1YV4XyJt2XDabposKudT99BsAci3rsjmYReOHfKhS4O6xI1WXTWnffKZe3VutidyPbkYtHwe9a6rTXBVrDrzkJ74xINVnSFedAvAh7g3sdNvvn6XoTUiFtBXyO/6j5suHqZHVxUDc0U+jIACZC9tYI01hIfS2c3wpbIX8z6KWgABEaWsBWCBP7rGL5eQ37M9NMVWnUN5v1mQGaeWwZGFN/wxz15mxrrT4ALTWOeoUhbbWyLFxFXC3JkFzAoy1BpBbbCju+mxsgUsrjYw2pQFMZuxfBofzoVI/MZCbScdVSY1CGukoRafaySROkAVSMYJUn7qP5JrUAIxMxslM0hWtxAkAUrG501CfDAqkSQW04iQ1TVJDnk/l6Uhj7iRSusbjSOnqpWNIm60bi2Q4CtB60fyZPR/uCkVX4KlyAQewXUZK/63ghuvxGyy4CSBg6JR+MKd0urZGHIeKe4V4gAUJdEon7QFcnl8R8ZirePRMxGMuWTdeziW2EY+5r5kUo6Y8yqlQZ7vCc8ZoHMJJPyIjhn3KiHGNmnVzFeU899kJ7zlmn/28OrgYOuvLPdKQvOJ6PvwYoyJVrzXO0azQ0/yIGI0YlucKgUt+pFiW/Hj0TNSxHymWY1Gosh/cCEbCzmK9M/Yjg2mTEIUnBrXlGD0x2Cn0fiTx/FzSTpb6JkYMznPjEMsG4DyXTumkiI41N+wUxBdMm2I5bDIrnMuJLiJfOOCSX0QeNt7tJEQ4Ivk8iGXqUTydhIQQTMuZRyzTRBXJuKsW2jLH27j0KUcsmz7HF7spCmgHcJUjl8nAQdLXfNnAp1AJ6lhBkhSLMH/Sw9l/s6fCo789wlkudWkhKZjDG3GlGKWyWoJr2sN+AKHIu6Hxreqgw+MtnPLX0Q7yCFqVEtIvbIUb51MCXexyS+sVQrIkC/SMa+AVy45gbjE3hgbnveNqNrAdwVUzdFuWNsYYg+/9B+eXczHc7P54EpfX4yzOl25gYL7b1KHu4WK+2OK0e62dnpecgLJ8LyyuVwqMl6aFVogR21W7Rr93aDxVgsNuKHapXtpOGHeCtoPu6N28P4AFv7k5dn5sHW05U5PeSzp4RRBWVBx+mU9gKc+F/zAay51hgSG75Ns5FzhrvHZ2zlR/1JROAOik+wfOGVRtpnnSkH9yMatpcst9zLwJ0wx9of53X830avE0zB7W33Nu9FdjjWOBMRXTR/YJXXOc7P4XnjYXzl2n+e47zvt3AqJZujoK78ErkgpVYAOv8R0MNPO90DoFANsWEUKIvrRYrVj40oRok8V3x03xVDmxuBAbDZy9knipSeIbMIh5JcLbaVhprpiWFaKdBcEIL7aLujLuNAnWF1098R26sf+k+S0Ym51/ODtq30ZTzKOj2pbgZgrIFIOnI0Bf1idGkEyB+AaO6+rAqto/Sik1L6yeqLQ/62Q480TNK1ePKlFugtp6AeW9MzThYTG1PJxFzX+o7Rd+UHqlrFrPpRadoFxc3J5WSr0bQzcw3s0iPV5z45WyWA8e5bBBIpFIpKDo//x0pNsr9joHAAAAAElFTkSuQmCC)

Save users a step by providing a **Direct Install URL**—a location on your site that redirects to the authorize step directly:

![Install from Slack Marketplace](data:image/png;base64,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)

When your app is published in the Slack Marketplace, you can utilize this direct install flow.

Configure this link on your [app's settings dashboard](https://api.slack.com/apps):

*   Open the _Basic Information_ page;
*   Scroll down to _Installing Your App_;
*   Select and enable _Install from Slack Marketplace_.

When you input and save your Direct Install URL, Slack will attempt to send an HTTP GET request to your declared URL.

That URL must then HTTP 302 redirect to a fully qualified `slack.com/oauth/v2/authorize` URL, as per the [first step of the OAuth flow](/authentication/installing-with-oauth). You'll receive an error letting you know if the redirect wasn't successful.

If you ever need to revert to installation via your landing page, just configure your app again to use _Install from your landing page_ in the [dashboard](https://api.slack.com/apps).

### Boost app discovery using App Suggestions {#suggestions}

Once you get published in the Slack Marketplace, Slack can suggest your app to new users. This will happen when links containing the domain name associated with your app are mentioned in conversation:

![An example app suggestion for an app called Paraglider.](/assets/images/app-suggestion-incidents-929e717fbc6ff1adbb50db6e90687166.png)

#### Enabling app suggestions {#enabling-app-suggestions}

While [managing your Slack app](https://api.slack.com/apps) settings, you'll find a snippet of HTML customized for your app under _Manage Distribution_. It's a `META` tag declaring your Slack app's ID, which typically begins with `A`. If you already know the ID, you can build one of these tags yourself.

The snippet looks something like this:

```
<meta name="slack-app-id" content="YOUR_APP_ID_HERE">
```

Place this brief piece of HTML in your website template's `HEAD` section, beside other metadata rubble you've accumulated, like so:

```
<html lang="en">    <head>        <meta charset="utf-8">        <meta name="slack-app-id" content="YOUR_APP_ID_HERE">        <title>Beforebot highlights bots before it</title>    </head></html>
```

With this HTML in place-and once your app is listed in the Slack Marketplace-Slack is ready to suggest your app to new users on workspaces it isn't yet installed on.

#### How app suggestions are triggered {#how-app-suggestions-are-triggered}

Let's take a hypothetical example. `@beforebot` is an app in the Slack Marketplace that has placed its app ID meta tag in the template of all pages on `https://before.bot/`.

On a workspace where `@beforebot` is not installed, `@seo` posts a message talking about the link `https://before.bot/movies/flight-of-the-navigator/trimaxion`.

Within moments of posting, Slack crawls the URL and extracts the app ID, correlating it to the `@beforebot` app. Slackbot then posts an ephemeral message only `@seo` can see:

![An example app suggestion for a bot called @beforebot.](/assets/images/app-suggestions-beforebot-c0651892d832659b333a5e57f9b32bef.png)

This message contains the app's icon and short description, along with a link back to the Slack Marketplace. It also contains three decisive links:

*   **Yes please** takes `@seo` to the Slack Marketplace
*   **Not now** will dismiss the ephemeral message but possibly suggest to `@seo` again when posting links to `before.bot`
*   **No thanks** will dismiss the ephemeral message and won't prompt `@seo` to install again

App suggestions are a great way for users and workspaces that are curious about, or already using your product or service to discover your Slack app.

Once installed, your app can [attach custom unfurling behavior](/messaging/unfurling-links-in-messages) to relevant links shared in messages, among all the other nifty things bots and apps can do.

* * *

## Submitting your app for review {#submitting}

When you're done with the preparation of your app, and have [gone through our guidelines](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements), you're ready to send your app for review.

1.  Go to your [app's settings dashboard](https://api.slack.com/apps).
2.  Click into the _Review and Submit_ page in the _Submit to Slack Marketplace_ section.
3.  Review the resources on the _How to prepare and submit your app_ page.
4.  Go through the submission flow and click the _Submit App for Review_ button.
5.  In the _Preview Your App Submission_ modal, verify everything is correct, and click the _Submit App_ button.

Once you’ve submitted, we’ll start the review process which is split into two parts:

**The preliminary review** This makes sure that the listing information and associated pages meet our guidelines, and that we have everything we need to install and test the app. Feedback from this part of the review generally takes up to 10 business days and you'll need to make all of the changes outlined before the submission can be moved to the next part of the review. If these changes aren't made or there is missing information, this step is repeated until the requirements are met. Your place in the queue is reset each time you resubmit and restarts the timeline for the next part of the review.

**The functional review** Once you've satisfied the requirements for the preliminary review, the submission will be moved to the functional part of the review. At this point, the submission is assigned to a reviewer who will install and test the app to assess the user experience. Feedback from this part of the review generally takes up to 10 weeks and once your submission has been assigned to a reviewer and you receive your first set of feedback, your place in the queue is not reset when you resubmit with changes.

After you address our feedback and everything is passed, we’ll approve your app and you can make it live in the Slack Marketplace straight away by returning to the [app's settings dashboard](https://api.slack.com/apps).

Congratulations! You're now listed in the Slack Marketplace. Flocks of admiring visitors are now on their way to experience your wonderful app. You'll want to keep the place looking neat and tidy—keep reading to find out about our expectations for developers maintaining their apps in the Slack Marketplace.

* * *

## Maintaining your published app {#maintaining}

The Slack Marketplace helps users find high-quality, dependable apps to aid in getting work done in Slack. This means that the process of getting published to the Slack Marketplace is not just about the initial submission and review.

In order to provide everyone with the highest quality experience when using apps from the Slack Marketplace we have some expectations around your app's performance, maintenance, support, and security standards.

### Expectations for published apps {#expectations}

1.  **Your app's listing is kept up to date**.
    
    Any changes to functionality, pricing, visual appearance, or any other updates should be accurately reflected in your app's listing.
    
2.  **Your app's functionality and customer experience matches or exceeds the quality of experience at submission, and you maintain your app’s performance.**
    
3.  **You provide timely support to customers.**
    
    If we hear from customers that they’ve not received responses from their support requests, we will reach out to you. If we do not receive a prompt reply to our own messages to you, we may de-list your app.
    
4.  **You regularly update your app to ensure that it makes use of our newest platform security features.**
    
    We regularly add new security features to our API, so please make sure you’re using those that are applicable to your app. Stay up to date with those new features by subscribing to our [changelog](/changelog).
    
5.  **You keep your app contact details up to date and are responsive to messages from us.**
    
    We will occasionally need to get in touch with you with questions about your app or to resolve any issues.
    
    Please make sure the developer and support contact details in your app submission are kept up to date so that we can contact you easily. Otherwise, you may miss important notices from us.
    
6.  **You must add a collaborator to your app.**
    
    Adding app collaborators ensures that multiple people can access your app’s configuration, in the event that the app creator leaves the [associated workspace](/app-management/distribution).
    
    Edit your app's collaborator list by going to [your app's settings dashboard](https://api.slack.com/apps) and clicking into the _Collaborators_ page.
    
7.  **You must resubmit your app for review when you [make substantial changes or updates](#updating) to the features, purpose or functionality of your app.**
    
8.  **Your app is being actively used.**
    
    We want the Slack Marketplace to provide people with a choice of useful and _used_ apps to help make their work days more productive. If your app is published in the Slack Marketplace but it is not being used, we will reach out to you to learn more about your plans for the app.
    
    If you do not plan to update your app, or people continue not to use your app, we will delist your app after communication with you.
    

### Possible enforcement actions {#enforcement}

In order to do maintain the health of the Slack Marketplace and provide everyone with the best possible experience, there are circumstances in which we will contact you and possibly delist or take further action on your app.

**We may contact you for response when**:

*   our [expectations for published apps](#expectations) are not being met;
*   we hear about issues from our mutual users, including but not limited to: spammy app behavior, broken or unexpected functionality, poor support experiences, lack of responses to support requests;
*   we see increased instances of your app being uninstalled;
*   we see large numbers of errors for your app;
*   the support page or privacy policy page links for the app are broken.

If we do not hear back from you after reaching out to you for any reason, we will reach out again while simultaneously delisting your app to protect users. If we hear back from you, and confirm that issues are resolved, we'll be able to re-list your app.

**We may delist your app without prior notice (other than to inform you of that action) when**:

*   your app's landing page or installation flow are broken;
*   your app appears to be unmaintained or abandoned;
*   your app's functionality changes substantially without notice and without the app being resubmitted for review.

**We reserve the right to revoke access and tokens for your app** if we receive no response from you about security-related issues.

* * *

## Testing and developing updates to a published app {#testing}

Apps change, and that's a good thing. When you need to make changes to your app, deploy the updates with a test app (staging app) that will be identical to your published app so that you (and we!) can test during the review process. If you try to make these changes to your live app, it can break your app's experience for users.

For example, if your app is `cycling_tips`, create a staging app called `cycling_tips-dev` that can be [distributed](/app-management/distribution). Use this staging app to test updates to your app's functionalities, such as adding a new feature, scopes, or events.

A staging app should:

*   have identical scopes of your submitted app
*   be distributable on other workspaces

If you're making changes to your app's long description or app name, a test app _isn't_ necessary, but we may still ask for one.

In order for us to test your app thoroughly please include any login credentials for any account or paid web service your staging app uses.

**Changes that don't require a test app:**

*   Updating Display information (app name, descriptions, icon)
*   Changes to pricing, languages your app supports
*   Adding another instance of an existing functionality

Please note that in cases where you've added significant changes to an existing feature, (such as a very different shortcut or slash command), we may need a staging app for testing.

**Changes that will require a test app:**

*   Enabling new functionalities to your app
*   Toggling on Messages or App Home tabs for the first time
*   Adding new scopes to your app

* * *

## Updating your published app {#updating}

If you plan to make changes to the functionality of your app, you must submit those changes for review and approval. Before you do that, be sure to [test and develop your changes](#testing) using a **separate** test app, as described above.

Once you've tested your changes, you can resubmit for review:

1.  Open your [app's settings dashboard](https://api.slack.com/apps)
2.  Click _Submit changes for review_.
3.  Under the _Help us review your app_ section, add information about the functionality changes you've made in the _Other notes_ fields, as well as the testing information for your staging/test app and web service, if applicable.
4.  Click the _Preview Submission_ button.
5.  On the _Review Your App Submission_ modal, verify everything is correct, and click the _Submit_ button.

* * *

## Resubmitting your app with granular permissions {#resubmitting}

If you maintain a classic app in the Slack Marketplace, perhaps making use of the umbrella [`bot`](/reference/scopes/bot) scope, you'll want to [migrate to granular permissions](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps). Read on for a walkthrough on how to [migrate](/legacy/legacy-app-migration/migrating-classic-apps#resubmit) your published Slack Marketplace app.

Note: Upgrading to granular permissions is a _fundamental change_ to your app. It **cannot** be undone. Make sure you test your app fully, including your [modified OAuth flow](/authentication/installing-with-oauth) with updated scopes and provide a staging app with those scopes in your submission.

[Read on](#upgrading_granular) for more details on migrating your Slack Marketplace app.

### Upgrading scopes {#upgrading_granular}

To migrate your app, you must upgrade your OAuth flow to use the [Slack V2 of OAuth 2.0](/authentication/installing-with-oauth)—if you do not upgrade your OAuth flow, you will not be able to use new permissions. Our [migration quickstart](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps) will help you see the differences in new and old Slack apps at a glance.

The [migration guide](/legacy/legacy-app-migration/migrating-classic-apps) fully walks you through choosing new scopes and using the new OAuth flow, but here's a helpful tip: use only the absolute minimum number of scopes for your app to work. Do not automatically select all the scopes listed during migration.

The easiest way to find a minimum set of scopes is to list which [API methods](/reference/methods) your app uses. Select the [scopes needed for those methods](/reference/methods). Avoid scope duplication: choose only the scopes you need for a bot token and any user tokens—and use the bot token unless you need to act on behalf of a specific user.

### Communicating with customers {#communicating_granular}

While updating your app to use granular permissions, you've most likely changed the scopes that your app requires. Your existing users will need to reinstall the app. To alert your users about those changes, consider using your app's [App Home](/surfaces/app-home), or [context block messages](/reference/block-kit/blocks/context-block)) from your app, to let users know an update is available.

* * *

## Making app settings changes {#config_changes}

When your app is published to the Slack Marketplace, you'll be able to safely make settings changes in the [dashboard](https://api.slack.com/apps).

Changes made in this dashboard won't affect a published app until you submit the app for re-review ([as above](#updating)) and this review is successful.

You can view the settings that apply to the published app under the _Published app settings_ section of the dashboard.

* * *

## Removing your app from the Slack Marketplace {#removing}

You can remove your published app from the Slack Marketplace in the _Published app settings_ section of your app's settings dashboard.

* * *

## Discontinuing your published app {#discontinuing}

If your app is no longer being actively maintained or developed, you should ensure you adequately sunset your app by:

*   [removing it](#removing) from the Slack Marketplace;
*   contacting the Slack Marketplace team;
*   contacting your customers where appropriate;
*   deleting and revoking any tokens your app generated.