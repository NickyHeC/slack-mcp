Source: https://docs.slack.dev/enterprise-search/connection-reporting

# Connection reporting using Enterprise Search

Slack’s connection reporting feature allows your app to communicate a user's authentication status, or connection status, directly to Slack. By offloading the UI management for "connect/disconnect" states to Slack, you can ensure a consistent user experience while reducing development overhead.

Read on for information about how to implement your own connection-enabled app using [Enterprise Search](/enterprise-search/developing-apps-with-search-features).

Want to try it out with a Developer Sandbox?

Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

## Event handling and status updating {#event-handling}

Your app should listen for the [`user_connection`](/reference/events/user_connection) event. This event has a `subtype` field that dictates whether a user is attempting to connect or disconnect from your app. The app's event handler should handle both cases.

The app is always expected to invoke the [`apps.user.connection.update`](/reference/methods/apps.user.connection.update) API method in its connecting flow to notify Slack when a user's connection status changes. Otherwise, Slack will assume the status for this user has not changed.

## Sequence of events {#sequence}

Below is a diagram showing how it all works together:

![Connection reporting sequence diagram](/assets/images/connection-reporting-sequence-8b9f40c5cefd6687308b369d5a3aff5b.png)

## Example {#example}

The following is an example of this sequence of events from the user's point of view within Slack:

1.  When the user is not connected, they'll see the following: ![User not connected](/assets/images/user-not-connected-d05ca0186d8500e82bac1a11a4556025.png)
    
2.  Once they click **Connect**, your app receives a [`user_connection`](/reference/events/user_connection) event with the `subtype: connect`. This event contains a `trigger_id`, which is used to open a modal that allows the user to connect to your app: ![Connect to app](/assets/images/connect-to-app-1eb8b3f18d4428969ce3323b8c9cf0c4.png)
    
3.  Once the user is connected, your app must report the connection status change to Slack by calling the [`apps.user.connection.update`](/reference/methods/apps.user.connection.update) API method to update the UI with the results: ![User connected](/assets/images/user-connected-96531baed6c9d60f4d8d93e1559e398c.png)
    
4.  Finally, putting it all together we have the following flow: