Source: https://docs.slack.dev/enterprise/migrating-to-organization-wide-deployment

# Migrating existing apps to an Enterprise org

If you have an existing single-workspace app that's ready for an Enterprise org, you'll want to make it available for organization-wide deployment.

* * *

## Opt into organization-wide deployment {#opt-in}

Specify within your [app settings](https://api.slack.com/apps) that the app may be deployed to an entire Enterprise organization by finding the **Org Level Apps** section in your app settings sidebar. Click **Opt-in**.

That's it! Your app can now be installed by an Org Admin or Owner at the organization level, rather than on an individual workspace.

* * *

## Best practices {#best-practices}

Read on for tips to keep in mind when making the transition from a single-workspace app to an Enterprise org app.

### Use a minimum version of the SDKs {#sdks}

If you make use of the [Bolt framework](/tools#bolt) to build Slack apps, make sure your version supports organization-ready apps:

Bolt framework

Required version

[Bolt for JavaScript](/tools/bolt-js/concepts/authenticating-oauth)

`3.0.0`

[Bolt for Python](/tools/bolt-python/concepts/authenticating-oauth)

`1.1.0`

[Bolt for Java](/tools/java-slack-sdk/guides/app-distribution)

`1.4.0`

### Visualize token storage {#tokens}

When your app turns from a single-workspace app into one that's deployed across an organization, you may want to rethink the way you store tokens.

Previously, you may have stored one row in a database for each installation, and each row might contain a token. Now, you can change your schema to reflect a one-to-many relationship between tokens and installations.

Alternatively, you can maintain the same one-to-one relationship and have rows for each installation and token—but you'll probably want to organize these with a sort key: the `enterprise_id`.

### Remember tokens from previous installations {#previous}

If your app is installed on an organization where previously it was installed for specific users and workspaces, you may still have thousands of existing user tokens. These tokens will continue to function after your app becomes organization-ready.

Once the app is installed on the organization, you'll be able to use a single organization-wide user token for any users that authenticate after that moment (or that reauthenticate).

And don't worry: your existing paths to gain user tokens (such as [Sign in with Slack](/authentication/sign-in-with-slack/), or just a regular OAuth sign-in flow for users) will still work. Those permissions will each be added to your organization-wide user token, rather than creating a new token.

After an organization-wide deployment, all the workspaces where your bot was installed will automatically be accessible to the new organization-wide **bot user token**.

Your app does not lose access to workspaces or need to interrupt users. You can use the organization-wide bot user token for workspaces where your app had already been installed.

### Turn off User IDs {#users}

If you previously had **User ID translation** `ON` in your Enterprise app, now is the time to turn it `OFF`.

Single enterprise user IDs are now available. There's no benefit to continuing to maintain local IDs. Use [`migration.exchange`](/reference/methods/migration.exchange) to obtain the new single IDs for any users that you have remaining local IDs for.

### Receive inherited scopes {#scopes}

When your app is installed across an organization, the scopes set during that installation pass down to each installation on individual workspaces within that organization. Even if you pass different scopes during the [OAuth redirect](/authentication/installing-with-oauth) when you gain access to an individual workspace, you'll still receive only the scopes set during the organization-wide install.

### Begin using channel IDs with the chat.postMessage API method {#chat}

Usually, when you call the [chat.postMessage](/reference/methods/chat.postMessage) API method to post a message to Slack, you specify the channel using a channel ID. If, however, you specified the channel using a _channel name_, the call from your organization-ready app will not succeed. You'll want to begin using channel IDs instead.

### Nothing to do here: apps for admins will already work {#admin}

Some Slack app features that are specifically designed for Enterprise administration, such as the [Audit Logs API](/admins/audit-logs-api/), the [SCIM API](/admins/scim-api/), and other [Admin APIs](/admins), already work with Enterprise organizations, rather than individual workspaces. You'll only need to install your app at the organization level to use these [Admin APIs](/admins)—you won't need to deploy your app across your organization.

## Next steps {#next-steps}

✨ Read more about [testing apps in an Enterprise org](/enterprise/testing-enterprise-org-apps).