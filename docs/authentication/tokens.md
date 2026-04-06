Source: https://docs.slack.dev/authentication/tokens

# Tokens

Tokens are the keys to the Slack platform. They tie together all the scopes and permissions your app has obtained, allowing it to read, write, and interact. There are multiple types of tokens available. Each type is suited for different types of apps and their functionality. Certain scopes are unique to particular token types, as summarized in the table below:

Token

App type

Description

[Bot token](#bot)

Slack apps

Bot tokens ascribe to a granular permission model to request only the scopes you need. Refer to the [quickstart guide for Slack apps](/app-management/quickstart-app-settings) to learn how to get one.

[Workflow token](#wfb)

Slack apps

Workflow tokens, or "just in time" tokens, are a subset of bot tokens. They cannot perform actions that require a user scope.

[User token](#user)

Slack apps

User tokens allow you to work directly on behalf of users when necessary.

[Configuration token](#config)

Slack apps

Configuration tokens are per-workspace tokens used with [App Manifest APIs](/app-manifests/configuring-apps-with-app-manifests#manifest_apis) to create and configure your apps.

[App-level token](#app-level)

Slack apps

App-level tokens are for use with Slack apps but only with specific APIs, which are related to the app across all organizations where the app is installed.

[Service token](#service)

Apps created with the Deno Slack SDK

Service tokens are long-lived, non-rotatable user tokens that won't expire, so they can be used to perform any Slack CLI action without the need to refresh tokens. Refer to [obtaining a service token](/tools/slack-cli/guides/authorizing-the-slack-cli#obtain-token) to learn how to get one.

## Bot tokens {#bot}

Bot tokens represent a bot associated with an app installed in a workspace. Unlike user tokens, they're not tied to a user's identity—they're only tied to your app. Since acting independently allows your app to stay installed even when an installing user is deactivated, using bot tokens is usually for the best.

*   New bot users can request individual scopes, similar to user tokens.
*   Bot token strings begin with `xoxb-`.

Ready to get one? Refer to the [quickstart guide for Slack apps](/app-management/quickstart-app-settings).

## Workflow tokens {#wfb}

Workflow tokens expire, but cannot be refreshed. These tokens expire either 15 minutes after being issued, or when a function step is completed successfully or returns an error—whichever occurs first. The token is then revoked immediately. Workflow token strings begin with `xwfp-`.

### "Borrowed visibility" {#borrowed-visibility}

Unlike `xoxb-` tokens, workflow tokens can sometimes access private channels their bot users are not a member of. This feature is called "borrowed visibility" because a workflow temporarily borrows the access of the user who ran it.

When evaluating a _"Can this user see this channel?"_ check for a workflow, we consider the bot user to have visibility based on these rules:

*   If the bot user is actually in the channel, the workflow has visibility.
*   If the bot user is not a member of the channel, the workflow may still have visibility if all of the following are true:
    *   The user (human, not bot) who started the workflow (i.e. the `user_id` on the token) is in the channel.
    *   The channel the workflow is attempting to view is either:
        1.  the channel where the workflow was tripped, or
        2.  a channel that was selected in the workflow's [OpenForm](/tools/deno-slack-sdk/reference/slack-functions/open_form) channel picker.

This feature only grants visibility into channels (e.g. acting as though the bot user is a member of the channel for that specific workflow run). It does not allow the bot user to act on behalf of a user (this requires a user scope) or to bypass any organization policies.

## User tokens {#user}

User tokens represent workspace members. They are issued for the user who installed the app and for users who authenticate the app. When your app asks for OAuth scopes, they are applied to user tokens. You can use these tokens to take actions on behalf of users.

*   User tokens gain the resource-based OAuth scopes requested in the installation process (e.g. asking for `channels:history` grants a user token access to `conversations.history` for any public channel).
*   User tokens represent the same access a user has to a workspace — the channels, conversations, users, reactions, and so on that they can see. Write actions with user tokens are performed as if by the user themselves.
*   User token strings begin with `xoxp-`.

Both configuration and service tokens are also tied to a user logged into Slack.

## Configuration tokens {#config}

App configuration tokens (or config tokens for short) are solely used to create and configure Slack apps using our [App Manifest APIs](/app-manifests/configuring-apps-with-app-manifests). Each configuration token is unique to a user and a workspace, but not an app. This means you can manage the configuration of any of your apps in a single development workspace, with just one config token.

These tokens are created on the [app settings page](https://api.slack.com/apps) below the list of apps. Under **Your App Configuration Tokens**, click **Generate Token** to create one.

## App-level tokens {#app-level}

App-level tokens represent your app across organizations, including installations by all individual users on all workspaces in a given organization.

*   These tokens give you the ability to handle things that relate to your app as a whole, such as [listing all the authorizations an event is visible to](/reference/methods/apps.event.authorizations.list).
*   App-level token strings begin with `xapp-`.

App-level tokens are obtained upon app creation. Find your app-level token in the **Basic Information** tab of the [app settings](https://api.slack.com/apps).

## Service tokens {#service}

Service tokens can only be used by [apps created with the Deno Slack SDK](/workflows).

Service tokens won't expire, so they can be used to perform any Slack CLI action without the need to refresh tokens.

*   The service token will not conflict with your regular authentication token; you can continue using your regular authentication token within the Slack CLI.

Ready to get one? Refer to [obtaining a service token](/tools/slack-cli/guides/authorizing-the-slack-cli#obtain-token).

## Legacy token types {#legacy_types}

For posterity, here is a list of tokens that are no longer supported or recommended for use.

### Legacy bot tokens {#legacy-bot-tokens}

These bot tokens, obtained through an older OAuth flow, should only be used in special cases — such as connecting to the now-deprecated [Real Time Messaging (RTM) API](/legacy/legacy-rtm-api).

*   Legacy bot tokens requested an umbrella `bot` scope with many different permissions included within it. We have now moved away from this umbrella permission model, and instead recommend you use newer, granular bot tokens. Newer platform features will no longer be supported with the legacy bot token.
*   Legacy bot tokens can't have resource-based OAuth scopes added to them; any scopes other than `bot` requested during the OAuth installation flow have no effect on the legacy bot token.
*   Revoking a legacy bot token with [`auth.revoke`](/reference/methods/auth.revoke) does not uninstall the bot user. A new token may be obtained via OAuth or, for internal integrations, your app management console.

### Legacy workspace tokens {#legacy-workspace-tokens}

Legacy workspace apps [have been fully deprecated as of August 2021](/changelog/2021-01-workspace-apps-retiring-the-platform-graveyard-in-aug-2021). Don't use this token type for new apps.

*   The developer preview for workspace apps has ended. We took the components of workspace apps and broke them apart: applying them in phases to _existing_ apps as well as new ones. [Read more about the motivation behind ending the preview](https://medium.com/@SlackAPI/an-important-update-on-workspace-apps-aabc9e42a98b).

### Legacy custom integration tokens {#legacy-custom-integration-tokens}

These tokens were associated with legacy custom integrations and early Slack integrations requiring an ambiguous "API token." They were generated using the legacy token generator, and are no longer recommended for use.

*   These tokens take on the full operational scope of the user that created them. If you're building a tool for your own team, we encourage creating a [single-workspace app](/app-management/distribution) with only the scopes it needs.