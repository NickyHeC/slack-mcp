Source: https://docs.slack.dev/govslack

# GovSlack

Welcome to [GovSlack](https://slack-gov.com), an instance of Slack designed for U.S. public sector use.

Read on to learn more about how to build apps for GovSlack.

## What is GovSlack? {#govSlack-about}

GovSlack is an instance of Slack that enables agencies, contractors, citizens, and partners to work together in one centralized, secure tool. This instance is designed to comply with the most stringent security and operational requirements of public sector customers.

## GovSlack compliance and security {#compliance-and-security}

GovSlack does not run on the `slack.com` domain. Instead, it runs on the entirely separate domain `slack-gov.com`. For compliance reasons, data between commercial Slack and GovSlack are completely isolated from one another.

Running in AWS GovCloud-certified data centers, GovSlack instances can help customers maintain compliance with the following:

*   **FedRAMP**: Federal Risk and Authorization Management Program. A compliance standard that ensures the proper level of security for cloud services (FedRAMP High authorized).
    
*   **FIPS 140.2**: Federal Information Processing Standard. A standard of security/cryptography for keeping government data safe. Includes requirements on encryption key length, key management, roles/access management, physical security of servers, and so forth.
    
*   **DOD IL**: Department of Defense Impact Level. Standards defining different levels of information sensitivity and requirements for systems housing that data (currently holding DoD/DISA IL4 certification).
    

Some of these standards may be inheritable or complied with by using compliant infrastructure such as AWS GovCloud, but it’s up to individual providers to determine the standards they want to comply with and whether they are certified or not.

Additionally, GovSlack Services have controls that can help customers maintain compliance with the United States International Traffic and Arms Regulations (ITAR). Customers remain responsible to ensure compliance with the ITAR at all times and must not provide data or information subject to the ITAR to Salesforce as part of any support request or other communication.

## Making your commercial Slack app available in GovSlack {#commercial-slack-app}

If you would like to make your app available in GovSlack, you will need to deploy your app in the GovSlack environment, then have it approved and published in the GovSlack Marketplace.

You'll also need to do the following:

*   Generate app credentials for your app in the [GovSlack environment](https://api.slack-gov.com/apps) (on [api.slack-gov.com/apps](https://api.slack-gov.com/apps) instead of [api.slack.com](https://api.slack.com)) in a similar way as you do for commercial Slack. We recommend keeping the same codebase and using `env` variables to distinguish between GovSlack and commercial Slack instances; this can help streamline your app's review time.
*   Use granular bot permissions and [V2 OAuth 2.0](/authentication/installing-with-oauth) (legacy V1 OAuth 2.0 and classic apps cannot be created or installed in GovSlack workspaces).
*   Redirect users to [https://slack-gov.com/oauth/v2/authorize](https://slack-gov.com/oauth/v2/authorize) instead of [http://slack.com/oauth/v2/authorize](http://slack.com/oauth/v2/authorize) when asking for scopes during installation. Refer to [Installing with OAuth](/authentication/installing-with-oauth) for more details.
*   Make [`oauth.v2.access`](/reference/methods/oauth.v2.access) API calls to the `slack-gov.com` domain instead of the `slack.com` domain. In fact, use `slack-gov.com` when calling any API endpoint instead of `slack.com` when using [Slack Web APIs](/apis/web-api/).
*   Point any other dynamically-generated URLs your app might use, such as [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks) or a [`response_url`](/interactivity/handling-user-interaction), to `slack-gov.com` instead of `slack.com`.
*   Point any other hardcoded URLs to `slack-gov.com` instead of `slack.com`.
*   Specify new [interactivity](/interactivity), [events API](/apis/events-api), and other configuration URLs that will handle GovSlack functionality.
*   If using the SDK or Bolt, you can override the API root in our web client or SDKs (e.g. [Node SDK](/tools/node-slack-sdk/web-api#custom-api-url) or [Bolt for JavaScript](https://github.com/slackapi/bolt-js/blob/main/examples/socket-mode/app.js#L13)).

## Setting compliance values {#compliance-values}

To set compliance values, navigate to your [App Manifest](/app-manifests) within your app settings on `slack-gov.com`.

Valid FedRAMP values are as follows:

*   `None`
*   `Low`
*   `Moderate`
*   `High`
*   `Customer Responsibility`

Valid ITAR values are as follows:

*   `No`
*   `Customer Responsibility`

Valid Department of Defense values are as follows:

*   `None`
*   `Customer Responsibility`
*   `IL2`
*   `IL4`
*   `IL5`
*   `IL6`

## Example manifest {#example-manifest}

The following is an example manifest written in YAML format:

```
display_information:  name: My Gov Appsettings:  org_deploy_enabled: false  socket_mode_enabled: false  token_rotation_enabled: falsecompliance:  fedramp_authorization: High  dod_srg_ilx: None  itar_compliant: No
```

## Unavailable features {#unavailable-features}

*   **Steps from Apps have been deprecated.** [Learn more about the deprecation](/changelog/2023-08-workflow-steps-from-apps-step-back).
*   The [`link_shared`](/reference/events/link_shared) event will not be dispatched when a user pastes a link in the message composer for a domain your app has registered. Instead, the event is only dispatched when a message is sent to the channel. This means you should not expect the `source` property in the `link_shared` request payload (it will implicitly always be `conversations_history`). You should not use the `preview` field (found within the `unfurls` URL-encoded JSON string) when [unfurling](/reference/methods/chat.unfurl); doing so will return the error `cannot_parse_attachment`.
*   The Slack Model Context Protocol (MCP) server and Real-time Search (RTS) API are not yet supported for GovSlack.

## FAQ {#govslack-faq}

### Is there a separate Slack Marketplace for apps on GovSlack? {#is-there-a-separate-slack-marketplace-for-apps-on-govslack}

Yes, only apps submitted to the GovSlack Marketplace will be available for installation in GovSlack workspaces.

*   Commercial Slack Marketplace: [https://slack.com/marketplace](https://slack.com/marketplace)
*   GovSlack Marketplace: [https://slack-gov.com/marketplace](https://slack-gov.com/marketplace)

### Since Slack is running a FedRAMP High version, is my app in the Slack Marketplace also required to be FedRAMP High? {#since-slack-is-running-a-fedramp-high-version-is-my-app-in-the-slack-marketplace-also-required-to-be-fedramp-high}

This is not a requirement. Each compliance level can optionally be set to [`None`](#compliance-values), meaning that your app does not meet any of the available standards. GovSlack customers will be able to see which compliance level each app follows, and can then decide which apps to install in their GovSlack workspaces.

### What does creating another app settings in GovSlack mean for the submission process? {#what-does-creating-another-app-settings-in-govslack-mean-for-the-submission-process}

The app submission process in GovSlack is the same as in commercial Slack. The app will need to be submitted to both app directories if you want the app to be available to both instances.

When developing your app for listing in the GovSlack Marketplace, we recommend creating a second app to serve as your development app. This will also allow us to [test the updates](/slack-marketplace/distributing-your-app-in-the-slack-marketplace#testing) you submit to your app once published.

### Does my app need to be published to the Slack Marketplace in order to be installable? {#does-my-app-need-to-be-published-to-the-slack-marketplace-in-order-to-be-installable}

No. Similar to commercial Slack, apps in GovSlack can be installed by one or more workspaces when [public distribution](/app-management/distribution) has been enabled in your app settings. That said, it is during the Slack Marketplace submission process where you define your app's compliance level.

### Does my app need to be Enterprise ready? {#does-my-app-need-to-be-enterprise-ready}

GovSlack customers are Enterprise customers, so your app should work for [Enterprise](/enterprise/). Slack supports development of [organization-ready apps](/enterprise/organization-ready-apps) to ease the install flow for admins and to increase adoption of your app.

### What if my app is not a granular bot permissions app? {#what-if-my-app-is-not-a-granular-bot-permissions-app}

Any app that is created on a GovSlack workspace is a granular bot permissions app with no ability to create a non-granular bot permissions app. If your existing app in commercial Slack is not a granular bot permissions app, you'll first need to [upgrade](/legacy/legacy-app-migration/migrating-classic-apps) the app before it can be configured and published in GovSlack and made available in the GovSlack Marketplace.

### When can I start developing on GovSlack and submit my app to the new Slack Marketplace? {#when-can-i-start-developing-on-govslack-and-submit-my-app-to-the-new-slack-marketplace}

Once your app is a granular bot permissions app and your compliance levels are set, submit a request to [feedback@slack.com](mailto:feedback@slack.com). We'll review your submission and once approved, publish it to the [GovSlack Marketplace](https://slack-gov.com/apps).