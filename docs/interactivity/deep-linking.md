Source: https://docs.slack.dev/interactivity/deep-linking

# Deep linking into Slack

Your application might live outside of Slack. Perhaps it includes a website, or a mobile application. Ever wish you could send a user back to a meaningful location in Slack?

You can do so with `slack://`!

[Open Slack](slack://open)

[Open #general](https://slack.com/app_redirect?channel=general)

Swiftly send users back to work during the installation process by redirecting them to a conversation with your app or bot using an `app_redirect` URL.

* * *

### Opening a direct message with your app or bot {#app_or_bot}

Slack apps with bot users can send users right into a conversation with your app.

Combine this feature with channel creation or installation and provide a guided onboarding experience.

Whether you want to send users to a conversation directly after you receive an access token using OAuth, or you want to link from your website or from within a message, send them to a URL like this:

```
https://slack.com/app_redirect?app=A123ABC456
```

When linking to a direct message, the `app_redirect` URL accepts two parameters:

*   `app` - your application's unique ID, such as `A123ABC456`. Find your Slack app's ID in the [app settings](https://api.slack.com/apps) under **Basic Information**. If invalid, users will be sent to the Slack Marketplace instead.
*   `team` - the team ID belonging to a target workspace. Useful when you know which workspace the user should be sent to. When no `team` is provided or the user is not signed in, users will be sent to their default team or asked to sign in. Use the [`team.info`](/reference/methods/team.info) method to obtain the ID of the workspace your app is currently installed in.

If your app is marked for distribution but not installed yet, users will be directed to your app's profile in the Slack Marketplace.

If your app is not marked for distribution and not yet installed, users will be sent to the Slack Marketplace.

If your app _is_ installed, users will be sent directly to a conversation with your bot user.

### Opening a channel by name or ID {#app_channel}

Send users to a specific channel or conversation , whether you know it only by name or have its authentic ID.

We'll handle addressing permissions however you present the request. When a channel is private or otherwise privileged, the logged in user must be a member of that conversation.

If the user does not have access to the channel or the channel does not exist, users will be presented with a HTTP 404 page.

Sending users to a known channel by ID:

```
https://slack.com/app_redirect?channel=C123ABC456
```

Sending users to a channel by name:

```
https://slack.com/app_redirect?channel=release-notes
```

When linking to a direct message, the `app_redirect` URL accepts two parameters:

*   `channel` - The destination channel ID or channel name to send a user to. If invalid or inaccessible, users will receive a 404.
*   `team` - the team ID belonging to a target workspace. Useful when you know which workspace the user should be sent to. When no `team` is provided or the user is not signed in, users will be sent to their default team or asked to sign in.

* * *

## Deep linking with slack:// {#client}

Use the `slack://` URI scheme to deep link into a user's native Slack client on the following operating systems:

### Desktop clients {#desktop-clients}

*   Macintosh
    
*   Windows
    

### Mobile clients {#mobile-clients}

*   iPhone
    
*   Android
    

### Supported URIs {#supported_URIs}

Send a user to Slack by linking users to these URI templates.

To make the best use of these URL patterns, make sure you're keeping tabs on team IDs, channel IDs, user IDs, and file IDs — these schemes do not support workspace subdomains, channel names, or user names. Not even filenames.

For best results, properly URL-encode your query parameters. Unrecognized paths will fall back to `slack://open`.

#### Open Slack {#open_slack}

```
slack://open
```

Open the native Slack client on behalf of the user's default workspace.

```
slack://open?team={TEAM_ID}
```

Open Slack and switch workspaces to the specified `team`. The provided `TEAM_ID` should be a string, the ID of your Slack workspace, like `T12345`.

#### Open an App Home {#open_app_home}

```
slack://app?team={TEAM_ID}&id={APP_ID}
```

Opens the App Home belonging to the app specified by the `APP_ID` in the `id` field, like `A123ABC456`. You should specify `team` with a `TEAM_ID`, using the ID of your Slack workspace.

You can also deep-link directly to a specific [tab within an App Home](/surfaces/app-home):

```
slack://app?team={TEAM_ID}&id={APP_ID}&tab=home
```

The value of `tab` should be one of:

*   `home` - opens the [Home tab](/surfaces/app-home) of the app specified by `id` within the Slack workspace specified by `team`.
*   `about` - opens the [About tab](/surfaces/app-home) of the app specified by `id` within the Slack workspace specified by `team`.
*   `messages` - opens the [Messages tab](/surfaces/app-home) of the app specified by `id` within the Slack workspace specified by `team`.

#### Open a channel {#open_a_channel}

```
slack://channel?team={TEAM_ID}&id={CHANNEL_ID}
```

Open the channel specified by the `CHANNEL_ID` provided in the `id` field, like `C123ABC456`. You must also specify the `team` with a `TEAM_ID`, using the ID of your Slack workspace.

#### Open a direct message {#open_a_direct_message}

```
slack://user?team={TEAM_ID}&id={USER_ID}
```

Open a direct message with the presented `USER_ID` value of the `id` field. You must also specify a `team` with a `TEAM_ID`, using the ID of your Slack workspace.

#### Open a file {#open_a_file}

```
slack://file?team={TEAM_ID}&id={FILE_ID}
```

Open the file specified by `FILE_ID` value of the `id` field. Don't forget to also specify a `team` with a `TEAM_ID`, using the ID of your Slack workspace.

#### Share a file {#share_a_file}

```
slack://share-file?team={TEAM_ID}&id={FILE_ID}
```

Open the `share file` dialog to share file specified by `FILE_ID` value of the `id` field. Don't forget to also specify a `team` with a `TEAM_ID`, using the ID of your Slack workspace.

* * *

## Link to messages {#permalinks}

Easily generate a permalink URL for any message using [`chat.getPermalink`](/reference/methods/chat.getPermalink). All you need is the channel/conversation ID and the message's `ts`.

* * *

## Example workflows {#example_workflows}

*   Your company's internal wiki includes a "getting started" guide for new employees. Encourage them to easily join the right channels by linking with `slack://channel`.
*   Your app's conversational UI lives in Slack, so you use `slack://user` to open your ongoing direct message correspondence with your user.
*   Send users directly back to Slack after app installation, by [sending them to a conversation with your app](#slack_apps).