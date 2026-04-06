Source: https://docs.slack.dev/admins/legal-holds-api

# Using the Legal Holds API

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

The [Slack Legal Hold APIs](/reference/legal-holds-api-reference) allow developers to build applications with read and write permissions to Slack legal holds. These applications can ensure that relevant data is saved when an organization needs to place a legal hold in Slack.

The Legal Hold APIs can do the following:

*   Create legal holds
*   Edit legal holds
*   Release legal holds

These permissions include being able to set the custodians on each legal hold, which determines the data that Slack will preserve.

Legal holds do not provide access to the contents of what is preserved.

API method reference

Find a full reference of the Slack Legal Holds API methods [here](/reference/legal-holds-api-reference).

* * *

## Setting up your Slack Workspace and Enterprise org {#setup}

There are a number of steps to enable usage of the Legal Holds API on a Slack Enterprise org.

First some prerequisites:

*   Customer must be an Enterprise customer, and app installation must happen at the top-level Enterprise org.
*   Only an Owner-level account can install the app — this should be an account created specifically for this purpose, so that the app is not tied to a single user.

And some other important info:

*   Third-party apps using the Legal Holds scopes must be approved for distribution via the Slack Marketplace before they can be installed on a customer org.
*   Legal holds are not supported on Slack Connect channels. In Slack Connect channels, messages will adhere to the retention policies of the org of the message sender.

* * *

## Building your app {#building}

OAuth ensures a way for us to provide tokens to applications that can request data on behalf of those who install the application.

Your app's access token opens the door to Slack API methods, events, and other features. During the OAuth flow, you specify which scopes your app needs. Those scopes determine exactly which doors (methods, events, and features) your app can unlock.

Your app gains an access token in three steps:

*   Asking for scopes
*   Waiting for a user to approve your requested scopes
*   Exchanging a temporary authorization code for an access token

### Scopes {#scopes}

Scopes at Slack are additive, but anytime a scope is added or removed, the app must be reinstalled. For the purpose of this API, please consider the following scopes based on your need.

Tokens with `admin.legalHolds:*` scopes are granted at the enterprise level.

Scope

Purpose

`admin.legalHolds:read`

View all of the organization’s Legal Holds policies and custodians

`admin.legalHolds:write`

Make changes to the organization’s Legal Holds policies and custodians

OAuth tokens are associated with the user who authorizes an application. In the event that the original installer's account is deactivated or their role drops below an "Org Owner", the token will be revoked. For this reason, we encourage customers to authorize the application with an admin or persistent account to prevent disruptions.

If you have more questions about this process, you can find a [more detailed description of OAuth here.](/authentication/installing-with-oauth)

### Partner app installation {#partner-app-installation}

Partners should create a single app that can be distributed and installed in multiple workspaces and customer instances. Customers should install the single production version of Partner applications via the Slack Marketplace (and should not create individual applications to share tokens).

### On prem solutions {#on-prem-solutions}

On prem solutions should also be condensed into a single application. An on prem customer can authenticate the app via the link in the Slack Marketplace after logging into their Slack instance. Once the OAuth handshake is completed via a link hosted within your application, the customer administrator can copy and paste the temporary code or the encrypted access token into their on prem deployment of your application. From there, requests can be made to the Legal Holds API from the on prem deployment.

For "hybrid" on-prem deployments, we also recommend adding redirect URIs for each customer instance.