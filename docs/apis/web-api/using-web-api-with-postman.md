Source: https://docs.slack.dev/apis/web-api/using-web-api-with-postman

# Using the Web API with Postman

This guide focuses on using Slack Web API methods via the [Postman application](https://www.postman.com/). This approach is helpful even if you have limited experience with APIs or coding.

First things first: some basic definitions. The Slack Web API is a set of methods (200+ of them) that provide a way for software programs to communicate directly with and request actions from Slack. Postman is an API client—a tool that simplifies the process of interacting with APIs. An API client provides a simplified way to collect method parameters, authorization, body content, and necessary headers required for communicating with API methods.

Postman allows you to construct and send requests to APIs through a user interface, offering a more forgiving environment than sending commands via the terminal. This guide covers three tasks:

1.  Creating a new Slack channel
2.  Posting a message in a Slack channel
3.  Creating a Salesforce channel in Slack

## Setup {#setup}

Before getting started with the Postman client, a few prerequisites are necessary.

### Prerequisites {#prerequisites}

1.  **Slack Admin Permissions**: You must have a workspace where you have permissions to install apps. If you don't have one, you can [go here](https://slack.com/get-started#create) to create one, or you can join the [Developer Program](https://api.slack.com/developer-program) and provision a sandbox (where you can create a workspace) with access to all Slack features for free. We recommend using a sandbox if you're just trying things out.
    
    Additionally, some API methods require admin scopes. You can find which scopes each method requires under the "Required scopes" section within the **Facts** box of the method's [documentation](/reference/methods).
    
2.  **Postman Installed**: Ensure you have downloaded and installed the [Postman application](https://www.postman.com/). The free version is adequate.
    

### Obtaining a Token {#obtaining-a-token}

To authorize requests with the Slack Web API, you need a specific type of credential from Slack called an OAuth token (more on token types [here](/authentication/tokens)). To get an OAuth token from Slack, you must first create an app from the [app settings page](https://api.slack.com/apps). We'll create a simple, private Slack app for your administrative use. Follow these steps:

1.  Create your admin helper app
    
    *   Once logged into your org's workspace, go to its Slack app settings page: [https://api.slack.com/apps](https://api.slack.com/apps)
    *   Click the **Create New App** button.
    *   Select **From scratch**.
    *   Enter an **App Name**. This name is mostly for your reference.
    *   Select the workspace where you want to perform these actions.
    *   Click **Create App**. You'll be taken to your new app's configuration page.
2.  Request permissions (scopes)
    
    Scopes are the specific permissions you grant your app. For the tasks in this guide, we will be using the [`conversations.create`](/reference/methods/conversations.create), [`chat.postMessage`](/reference/methods/chat.postMessage), and [`admin.conversations.createForObjects`](/reference/methods/admin.conversations.createForObjects) methods. You'll need to add the following scopes: `channels:manage`, `chat:write`, and `admin.conversations:manage_objects`, corresponding to the methods, respectfully. Add them with the following instructions:
    
    *   On your app's configuration page, navigate to **OAuth & Permissions** in the left-hand sidebar.
    *   Scroll down to the **Scopes** section.
    *   Find the **Bot Token Scopes** subsection. Click **Add an OAuth Scope**.
    *   Type or find and select the `channels:manage` and `chat:write` scopes.
    *   Find the **User Token Scopes** subsection. Click **Add an OAuth Scope**.
    *   Type or find and select the `admin.conversations.manage_objects` scope. This scope is only needed for the third example. Do not add it unless you are using the method in the third example.
    
    Important
    
    The `admin.*` scopes are highly privileged. Only users with sufficient administrative rights in the workspace can grant them during the installation step.
    
    Reviewing the reference pages of the methods listed above, you will see additional scopes listed that aren't listed in the instructions here. These are not necessary for the use cases in the examples shown here, so we have not included them. Scopes like `groups:write` and `im:write` are needed for private channel creation; here we create a public channel.
    
3.  Install the app and obtain the token
    
    Now you need to install this app configuration to your workspace/org to generate the actual token.
    
    *   Enterprise Org Installation
    *   Non-enterprise Org Installation
    
    If you are developing in an Enterprise organization, follow these steps:
    
    *   Find and click the **Org Level Apps** section in the left-hands sidebar. Click the button to enable org readiness and follow the prompts to do so.
    *   Once org readiness is enabled, go back to the **OAuth & Permissions** page.
    *   Click the **Install to Organization** button.
    *   A confirmation screen will appear. Review it carefully, then click **Allow**. If you do not have sufficient privileges, you may need to request that a Workspace Owner/Admin complete this step.
    *   After installing to the org, the app needs to be added to a workspace. Follow the instructions [here](/enterprise/organization-ready-apps#how-to-add-the-app-to-a-workspace-from-the-admin-dashboard) to do so.
    *   Once you've added the app to a workspace, navigate back to your app settings on the **OAuth & Permissions** page.
    
    If you are not developing in an Enterprise organization, follow these steps:
    
    *   On the **OAuth & Permissions** page, scroll up to the **OAuth Tokens** section and click the button to install the app to your workspace. Follow the prompts and click **Allow**.
    
    *   Once the app is installed in a workspace, the tokens will be available. For the first two examples, we'll need the **Bot User OAuth Token** displayed in the **OAuth Tokens** section. It will start with `xoxb-`. For the third example, we'll need the **User OAuth Token**. It will start with an `xoxp-`. Copy both of these and save them for later.
    
    Keep it secret. Keep it safe.
    
    Treat this token like a master key or password. Keep it secret and secure. Do not share it in public channels, emails, or commit it to shared code repositories. Store it securely, for example, using Postman's environment variables feature.
    
    You now have the necessary tokens to use in the **Authorization** section of your Postman requests.
    

## Using Postman to Interact with Slack APIs {#using-postman-to-interact-with-slack-apis}

Postman organizes API requests using these main components:

1.  **HTTP Method**: The type of request (e.g., `POST` for sending data to create/modify).
2.  **Request URL**: The specific web address (endpoint) for the Slack API method.
3.  **Parameters**: The key-value pairs of arguments, if the method requires any.
4.  **Authorization**: Where you'll put your `xoxb-` or `xoxp-` token.
5.  **Headers**: Additional metadata for the request, like data format specification.
6.  **Body**: The data payload required by the API method, typically in JSON format.

There are also tabs for Scripts and Settings, but we won't use those in these examples.

### Example 1: Creating a new Slack channel {#example-1-creating-a-new-slack-channel}

Using the [`conversations.create`](/reference/methods/conversations.create) method, we will create a new public channel.

#### Postman configuration steps {#postman-configuration-steps}

Configure the Postman request with the following values. All of the method-specific information can be found on the [`conversations.create`](/reference/methods/conversations.create) reference page.

1.  HTTP Method: `POST`
2.  Request URL: `https://slack.com/api/conversations.create`
3.  Params: Enter each as a key-value pair.
    *   Key: `name`, Value: enter a name for the channel, like `team-gossip`
    *   Key: `is_private`, Value: `false`
    *   Key: `team_id`, Value: enter the team/workspace ID of where you want your channel to live. It is only necessary if you are in an Enterprise organization. To find the team ID, navigate to your organization admin dashboard, click **Workspaces**, then click the three dots next to the workspace you want to create the channel in, and **copy workspace ID**. Paste that value in `team_id`. It will look something like `T12345678`.
4.  Authorization:
    *   Go to the **Authorization** tab below the URL field.
    *   Select **Bearer Token** from the **Type** dropdown.
    *   Paste your bot token (the `xoxb-` token you obtained) into the **Token** field on the right.
5.  Headers:
    *   Go to the **Headers** tab.
    *   Enter a key-value pair.
        *   Key: `Content-type`
        *   Value: `application/x-www-form-urlencoded`
6.  Body: You don't need to pass a body in this example.

#### Send and verify {#send-and-verify}

Click the **Send** button and verify the response in the lower window. If it was successful, you will see something like this:

```
{    "ok": true,    "channel": {        "id": "C123ABC4567",        "name": "team-gossip",        "is_channel": true,        "is_group": false,        "is_im": false,        "is_mpim": false,        "is_private": false,        "created": 1747414789,        "is_archived": false,        "is_general": false,        "unlinked": 0,        "name_normalized": "team-gossip",        "is_shared": false,        "is_org_shared": false,        "is_pending_ext_shared": false,        "pending_shared": [],        "context_team_id": "T123456ABCD",        "updated": 1747414789113,        "parent_conversation": null,        "creator": "U01234ABCDE",        "is_moved": 0,        "is_ext_shared": false,        "shared_team_ids": [            "T123456ABCD"        ],        "internal_team_ids": [            "T123456ABCD"        ],        "pending_connected_team_ids": [],        "is_member": true,        "last_read": "0000000000.000000",        "topic": {            "value": "",            "creator": "",            "last_set": 0        },        "purpose": {            "value": "",            "creator": "",            "last_set": 0        },        "previous_names": [],        "priority": 0    }}
```

If the call was not successful, you will see a response containing `"ok": false` with the error it encountered. If you were missing a necessary argument, for example:

```
{    "ok": false,    "error": "missing_argument",    "arg": "team_id"}
```

### Example 2: Posting a message in a Slack channel {#example-2-posting-a-message-in-a-slack-channel}

Using the [`chat.postMessage`](/reference/methods/chat.postMessage) method, we will post a new message in a channel.

#### Postman configuration steps {#postman-configuration-steps-1}

Configure the Postman request with the following values. All of the method-specific information can be found on the [`chat.postMessage`](/reference/methods/chat.postMessage) reference page. The `chat.postMessage` method has many optional arguments; for the sake of brevity in this example, we will only show the required ones.

1.  HTTP Method: `POST`
2.  Request URL: `https://slack.com/api/chat.postMessage`
3.  Params: Enter each as a key-value pair.
    *   Key: `channel`, Value: a channel ID of where you would like to post the message; i.e. `C0123456ABC`
    *   Key: `text`, Value: `hello world`
4.  Authorization:
    *   Go to the **Authorization** tab below the URL field.
    *   Select **Bearer Token** from the **Type** dropdown.
    *   Paste your bot token (the `xoxb-` token you obtained) into the **Token** field on the right.
5.  Headers:
    *   Go to the **Headers** tab.
    *   Enter a key-value pair.
        *   Key: `Content-type`
        *   Value: `application/x-www-form-urlencoded`
6.  Body: You don't need to pass a body in this example.

#### Send and verify {#send-and-verify-1}

Click the **Send** button and verify the response in the lower window. If it was successful, you will see something like this:

```
{    "ok": true,    "channel": "C0123456ABC",    "ts": "1747421657.751559",    "message": {        "user": "U01234ABCDE",        "type": "message",        "ts": "1747421657.751559",        "bot_id": "B0123456ABC",        "app_id": "A0123456ABC",        "text": "hello world",        "team": "T0123456ABC",        "bot_profile": {            "id": "B0123456ABC",            "app_id": "A0123456ABC",            "user_id": "U01234ABCDE",            "name": "PostmanTest",            "icons": {                "image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png",                "image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png",                "image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png"            },            "deleted": false,            "updated": 1747411567,            "team_id": "T0123456ABC"        },        "blocks": [            {                "type": "rich_text",                "block_id": "X+m",                "elements": [                    {                        "type": "rich_text_section",                        "elements": [                            {                                "type": "text",                                "text": "hello world"                            }                        ]                    }                ]            }        ]    }}
```

If your app is not in the channel you want to post to, the response might look like this:

```
{    "ok": false,    "error": "not_in_channel"}
```

You can fix this particular problem by adding your app to the channel. Go to the channel and @mention the name of the app in a message and send it; Slack will prompt you to add it.

### Example 3: Creating a Salesforce channel in Slack {#example-3-creating-a-salesforce-channel-in-slack}

Using the [`admin.conversations.createForObjects`](/reference/methods/admin.conversations.createForObjects) method, we will create a channel in Slack for the corresponding Salesforce object provided. Salesforce channels are a bit different than standard Slack channels; learn more about them [here](https://slack.com/help/articles/32664824986259-Use-Salesforce-channels-in-Slack).

#### Postman configuration steps {#postman-configuration-steps-2}

Configure the Postman request with the following values. All of the method-specific information can be found on the [`admin.conversations.createForObjects`](/reference/methods/admin.conversations.createForObjects) reference page.

1.  HTTP Method: `POST`
2.  Request URL: `https://slack.com/api/admin.conversations.createForObjects`
3.  Params: Enter each as a key-value pair.
    *   Key: `object_id`, Value: the Salesforce object you'd like to link; i.e. `0019000000DmehKAAR`
    *   Key: `salesforce_org_id`, Value: your org ID; i.e. `00DGC00000024hsuWY`
4.  Authorization:
    *   Because this method uses an `admin` scope, you must use the user OAuth token instead of the bot token. This is the one you copied earlier that begins with `xoxp-`.
    *   Go to the **Authorization** tab below the URL field.
    *   Select **Bearer Token** from the **Type** dropdown.
    *   Paste your user token (the `xoxp-` token you obtained) into the **Token** field on the right.
5.  Headers:
    *   Go to the **Headers** tab.
    *   Enter a key-value pair.
        *   Key: `Content-type`
        *   Value: `application/x-www-form-urlencoded`
6.  Body: You don't need to pass a body in this example.

#### Send and verify {#send-and-verify-2}

Click the **Send** button and verify the response in the lower window. If it was successful, you will see something like this:

```
{  "ok": true,  "channel_id": "C123456ABC"}
```

If you used the bot token instead of the user token, you will get an error response like this:

```
{    "ok": false,    "error": "not_allowed_token_type"}
```