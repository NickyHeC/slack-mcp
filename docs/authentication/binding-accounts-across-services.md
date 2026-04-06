Source: https://docs.slack.dev/authentication/binding-accounts-across-services

# Binding accounts across services

A user account on Slack can be bound to a user account on an another system.

In order to do this, you'll need to be able to make changes to the internal application to add a new endpoint, which will be used in the account binding process.

We have a [sample app](https://github.com/slackapi/template-account-binding) that shows this behavior on GitHub.

## Invoke an action {#invoke}

When someone uses a [slash command](/interactivity/implementing-slash-commands) associated with the Slack app, the app will receive an HTTP POST request that contains the user's Slack user ID and the command they invoked. With this Slack user ID, the app can check whether it already knows who the user is in the internal application. If the user is found, the command can be run against the other application on behalf of the user. The results can then be sent back to Slack as a well-formatted message.

The following steps assume that a matching user was not found; therefore the account binding process must be kicked off.

## Generate and send a unique association URL {#generate}

In order to link a Slack user to a user on the internal application, we need the user to authenticate into the internal system with some information that can tie them securely back to the Slack user who initiated the slash command.

To do this, the app generates a unique token (a [nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce)), stores it in a database alongside the Slack user ID, and passes it to the URL of a page behind authentication on the internal system. As soon as the user authenticates into the internal system, the unique token in the URL can be used to search for that user's Slack ID.

The association URL (the URL that contains the nonce and which is behind authentication on the internal system) is sent to the user as an ephemeral message in response to the slash command that invoked the action. The ephemeral message is only visible to the user who ran the slash command.

## Bind the user accounts {#bind}

Once the user clicks the association URL in the ephemeral message, they are sent to the internal application and if they are not already logged in, they'll be prompted to do so using the typical authentication flow.

Once a user session is established, the nonce is extracted from the URL and queried. The internal application will then store the user ID of the user who has been authenticated, along with the Slack user ID and the nonce, in its database.

## Send a success message {#success}

Once the accounts are bound, the user will see a success response. At the same time, a confirmation message is sent to the user in a Slack DM using the [`chat.postMessage`](/reference/methods/chat.postMessage) Web API method.

To post to a restricted channel, this kind of app must either be installed by a team admin approver _or_ a user with posting permissions in that channel.

![A flow for binding accounts between services](/assets/images/account_binding-d60f864cbd74d5e4bff7abb3aefb1a7a.png)

## Additional customization suggestions {#customize}

You can customize the following:

*   Which actions initiate the account binding process
*   Whether to send the association URL as a DM instead of an ephemeral message
*   Whether to set an expiration date on the account binding URL
*   Whether you want to generate a personal API access token for the internal application for the Slack app to use once the accounts have been bound