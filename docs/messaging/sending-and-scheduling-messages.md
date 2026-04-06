Source: https://docs.slack.dev/messaging/sending-and-scheduling-messages

# Sending and scheduling messages

Apps that only _listen_ can be useful, but there's so much more utility to explore by transforming a monologue into a conversation. Give your app the gift of dialogue by setting it up to send Slack messages.

This guide will help you learn a basic way to accomplish this and show you the paths you can take to make things complex and interactive.

* * *

## Sending messages {#getting_started}

If you don't have a Slack app yet, [here's a guide to help you create one](/app-management/quickstart-app-settings#creating). Make sure you create the app in a workspace that won't mind you posting lots of test messages.

Once you've done that, come back here and keep reading.

### Requesting the necessary permissions {#permissions}

Each Slack app starts off without permission to do very much at all. You will have to grant your app the correct scopes required in order for you to publish messages. There are [lots of scopes available](/reference/scopes), and you can read our [OAuth guide](/authentication/installing-with-oauth) for more information on why they're needed, and what they do.

For the purposes of this guide, however, we'll skip over that and just tell you the permissions we need right now.

The first is [`channels:read`](/reference/scopes/channels.read). That scope lets your app retrieve a list of all the public channels in a workspace so that you can [pick one to publish a message to](#conversations). If you already know the ID of the channel you wish to send messages to, you can skip out on requesting `channels:read`.

The second is [`chat:write`](/reference/scopes/chat.write). This one grants permission for your app to send messages as itself (apps _can_ send messages as users or bot users, but [we'll cover that later](#impersonation)).

To request permissions:

1.  Open the settings for your app from the [App Management](https://api.slack.com/apps) page.
2.  In the navigation menu, select **OAuth & Permissions**.
3.  Scroll down to the **Scopes** section, and pick `channels:read` and `chat:write` from the drop-down menu.
4.  Click **Save changes**.
5.  Scroll back to the top of this page and look for the button that says **Install App to Workspace** (or **Reinstall App** if you've done this before). Click it. You'll now see a permission request screen to install your app to its original workspace.

If you had already installed your app to its original workspace before, you might still see the permissions screen if the scopes you just added weren't previously granted to your app.

Authorize your app, and you should see a success message. On the **OAuth & Permissions** page you're brought back to, you should now see an OAuth access token available. Grab this token and store it for later, as we'll use that token to make some [Web API](/apis/web-api/) calls.

### Picking the right conversation {#conversations}

Now we need to find somewhere within your workspace to send a message. This [could be any Slack conversation](/messaging#conversations), but we'll use a public channel.

We'll remind you again, it's not a good idea to attempt the instructions in this guide with a real, living workspace. If you really have to, at least [create a new, empty public channel](https://slack.com/help/articles/201402297-Create-a-channel) within the workspace for testing purposes.

In order to find a valid Slack conversation ID, we'll use the [`conversations.list`](/reference/methods/conversations.list) method. This API method will return a list of all public channels in the workspace your app is installed to. You'll need the [`channels:read`](/reference/scopes/channels.read) scope granted to your app.

Within that list, we'll be able to find a specific `id` of the conversation that we want to access. Here's an example API call:

*   HTTP
*   Java
*   JavaScript
*   Python

```
GET https://slack.com/api/conversations.listAuthorization: Bearer xoxb-your-token
```

```
import com.slack.api.Slack;import com.slack.api.methods.SlackApiException;import com.slack.api.model.Conversation;import org.slf4j.LoggerFactory;import java.io.IOException;public class FindingConversation {    /**     * Find conversation ID using the conversations.list method     */    static void findConversation(String name) {        // you can get this instance via ctx.client() in a Bolt app        var client = Slack.getInstance().methods();        var logger = LoggerFactory.getLogger("my-awesome-slack-app");        try {            // Call the conversations.list method using the built-in WebClient            var result = client.conversationsList(r -> r                // The token you used to initialize your app                .token(System.getenv("SLACK_BOT_TOKEN"))            );            for (Conversation channel : result.getChannels()) {                if (channel.getName().equals(name)) {                    var conversationId = channel.getId();                    // Print result                    logger.info("Found conversation ID: {}", conversationId);                    // Break from for loop                    break;                }            }        } catch (IOException | SlackApiException e) {            logger.error("error: {}", e.getMessage(), e);        }    }    public static void main(String[] args) throws Exception {        // Find conversation with a specified channel `name`        findConversation("tester-channel");    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// Find conversation ID using the conversations.list methodasync function findConversation(name) {  try {    // Call the conversations.list method using the built-in WebClient    const result = await app.client.conversations.list({      // The token you used to initialize your app      token: "xoxb-your-token"    });    for (const channel of result.channels) {      if (channel.name === name) {        conversationId = channel.id;        // Print result        console.log("Found conversation ID: " + conversationId);        // Break from for loop        break;      }    }  }  catch (error) {    console.error(error);  }}// Find conversation with a specified channel `name`findConversation("tester-channel");
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)channel_name = "needle"conversation_id = Nonetry:    # Call the conversations.list method using the WebClient    for result in client.conversations_list():        if conversation_id is not None:            break        for channel in result["channels"]:            if channel["name"] == channel_name:                conversation_id = channel["id"]                #Print result                print(f"Found conversation ID: {conversation_id}")                breakexcept SlackApiError as e:    print(f"Error: {e}")
```

You'll get back a JSON object, with a `channels` array containing all the public channels that your app can see. You can find your channel by looking for the `name` in each object.

When you've found the matching channel, make note of the `id` value, as you'll need it for certain API calls.

If your app implements [shortcuts](/interactivity/implementing-shortcuts), [slash commands](/interactivity/implementing-slash-commands), or uses the [Events API](/apis/events-api/), your app will see conversation `id`s in request payloads sent by those features.

In those cases, your app can dynamically respond using the payload data to identify the relevant conversation, rather than needing to use the `conversations.list` method described above.

Now that we've picked a destination, we need to decide what our message will look like.

### Composing your message {#composing}

Designing a message is a complicated topic, so we've [broken it out into its own section](/messaging/formatting-message-text) that you can read at your leisure.

For this guide, we'll just publish a plain-text message. Here's the [message payload](/messaging#payloads) we're going to send:

```
{  "channel": "YOUR_CHANNEL_ID",  "text": "Hello, world"}
```

That seems appropriate, right? Let's get down to the actual business of sending this message.

### Publishing your message {#publishing}

We're nearly there; we just need to make one more API call, this time to [`chat.postMessage`](/reference/methods/chat.postMessage). Again, substitute in the values of the token and conversation ID that you noted earlier:

*   HTTP
*   Java
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.postMessageContent-type: application/jsonAuthorization: Bearer xoxb-your-token{  "channel": "YOUR_CHANNEL_ID",  "text": "Hello world :tada:"}
```

```
import com.slack.api.Slack;import com.slack.api.methods.SlackApiException;import org.slf4j.LoggerFactory;import java.io.IOException;public class PublishingMessage {    /**     * Post a message to a channel your app is in using ID and message text     */    static void publishMessage(String id, String text) {        // you can get this instance via ctx.client() in a Bolt app        var client = Slack.getInstance().methods();        var logger = LoggerFactory.getLogger("my-awesome-slack-app");        try {            // Call the chat.postMessage method using the built-in WebClient            var result = client.chatPostMessage(r -> r                // The token you used to initialize your app                .token("xoxb-your-token")                .channel(id)                .text(text)                // You could also use a blocks[] array to send richer content            );            // Print result, which includes information about the message (like TS)            logger.info("result {}", result);        } catch (IOException | SlackApiException e) {            logger.error("error: {}", e.getMessage(), e);        }    }    public static void main(String[] args) throws Exception {        publishMessage("C12345", "Hello world :tada:");    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// Post a message to a channel your app is in using ID and message textasync function publishMessage(id, text) {  try {    // Call the chat.postMessage method using the built-in WebClient    const result = await app.client.chat.postMessage({      // The token you used to initialize your app      token: "xoxb-your-token",      channel: id,      text: text      // You could also use a blocks[] array to send richer content    });    // Print result, which includes information about the message (like TS)    console.log(result);  }  catch (error) {    console.error(error);  }}publishMessage("C12345", "Hello world :tada:");
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# ID of channel you want to post message tochannel_id = "C01JASD6802"try:    # Call the conversations.list method using the WebClient    result = client.chat_postMessage(        channel=channel_id,        text="Hello world!"        # You could also use a blocks[] array to send richer content    )    # Print result, which includes information about the message (like TS)    print(result)except SlackApiError as e:    print(f"Error: {e}")
```

This time we're using a POST request, so your token from before has to be included in the header of the request as a [bearer token](https://tools.ietf.org/html/rfc6750).

Submit the request and your message should be delivered instantly. You'll get back a response payload containing an `ok` confirmation value of `true`, and other data such as the `channel` the message was posted to. One very important piece of information in this response is the `ts` value, which is essentially the ID of the message, and which you'll need if you want to [reply to this message](#threading).

Locate the Slack conversation the message was sent to and it should be waiting for you:

![Bot avatar](/assets/images/oslo-b2272998a620e09f3081347b23f939cc.png)

Oslo

Woof! (Hello world!)

Amazing work! You've now implemented one of the core pieces of functionality for any Slack app. Keep reading to see how you can add a little more complexity.

* * *

### Replying to your message {#threading}

In some cases, you might find it more useful for your app to reply to another message, creating a [thread](/messaging#threading). For example, if your app is sending a message in response to being mentioned, then it makes sense to add a [threaded reply](/messaging#threading) to the source of the mention.

[Make sure the message you want to reply to isn't a reply itself](/messaging/retrieving-messages#finding_threads), as shown in our [retrieving messages guide](/messaging/retrieving-messages#finding_threads).

For this guide, we'll assume the message is an unthreaded one. In fact, let's reply to the message [you just published](#publishing). You need three pieces of information to reply in a thread:

*   An access token with the right permissions, like the [`token` created earlier](#permissions).
*   The `channel` that the parent message lives in.
*   The `ts` value of the parent message.

You should still have the last two pieces of information from the response payload you received after [publishing the parent message](#publishing).

In more generic terms, you can also find the `ts` value of messages by following our [guide to retrieving individual messages](/messaging/retrieving-messages#individual_messages).

Pulling all that data together, we can make another [`chat.postMessage`](/reference/methods/chat.postMessage) API call to publish a reply:

*   HTTP
*   Java
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.postMessageContent-type: application/jsonAuthorization: Bearer xoxb-your-token{  "channel": "YOUR_CHANNEL_ID",  "thread_ts": "PARENT_MESSAGE_TS",  "text": "Hello again!"}
```

```
import com.slack.api.Slack;import com.slack.api.methods.SlackApiException;import org.slf4j.LoggerFactory;import java.io.IOException;public class ReplyingMessage {    /**     * Reply to a message with the channel ID and message TS     */    static void replyMessage(String id, String ts) {        // you can get this instance via ctx.client() in a Bolt app        var client = Slack.getInstance().methods();        var logger = LoggerFactory.getLogger("my-awesome-slack-app");        try {            // Call the chat.postMessage method using the built-in WebClient            var result = client.chatPostMessage(r -> r                // The token you used to initialize your app                .token("xoxb-your-token")                .channel(id)                .threadTs(ts)                .text("Hello again :wave:")                // You could also use a blocks[] array to send richer content            );            // Print result            logger.info("result {}", result);        } catch (IOException | SlackApiException e) {            logger.error("error: {}", e.getMessage(), e);        }    }    public static void main(String[] args) throws Exception {        // Uses a known channel ID and message TS        replyMessage("C12345", "15712345.001500");    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// Reply to a message with the channel ID and message TSasync function replyMessage(id, ts) {  try {    // Call the chat.postMessage method using the built-in WebClient    const result = await app.client.chat.postMessage({      // The token you used to initialize your app      token: "xoxb-your-token",      channel: id,      thread_ts: ts,      text: "Hello again :wave:"      // You could also use a blocks[] array to send richer content    });    // Print result    console.log(result);  }  catch (error) {    console.error(error);  }}// Uses a known channel ID and message TSreplyMessage("C12345", "15712345.001500");
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# TS of message you want to post thread tomessage_ts = "1610144875.000600"# ID of channel you want to post message tochannel_id = "C01JASD6802"try:    # Call the chat.postMessage method using the WebClient    # The client passes the token you included in initialization        result = client.chat_postMessage(        channel=channel_id,        thread_ts=message_ts,        text="Hello again :wave:"        # You could also use a blocks[] array to send richer content    )    print(result)except SlackApiError as e:    print(f"Error: {e}")
```

You'll see another API response payload containing information about the newly published threaded reply. Return to the same conversation in Slack, and you'll see your original message now has a reply:

![Bot avatar](/assets/images/oslo-b2272998a620e09f3081347b23f939cc.png)

Oslo

Woof! (Hello world!)

![Bot avatar](/assets/images/oslo-b2272998a620e09f3081347b23f939cc.png)

Oslo

Woof Woof! (Hello world, again!)

When publishing threaded reply messages, you can also supply a `reply_broadcast` boolean parameter, as listed in the relevant API docs. This parameter, if set to `true`, will 'broadcast' a reference to the threaded reply to the parent conversation. Read more about the [Slack user-facing equivalent of this feature here](https://slack.com/help/articles/115000769927-Message-and-file-threads#reply_to_channel).

* * *

### Sending messages as other entities {#impersonation}

Apps can publish messages that appear to have been created by a user in the conversation. The message will be attributed to the user and show their profile photo beside it.

This is a powerful ability and must only be used when the user themselves gives permission to do so. For this reason, this ability is only available when an app has requested and been granted an additional scope: [`chat:write.customize`](/reference/scopes/chat.write.customize).

Your app should only use this feature in response to an inciting user action. It should never be unexpected or surprising to a user that a message was posted on their behalf, and it should be heavily signposted in advance.

To modify the appearance of the app, make calls to [`chat.postMessage`](/reference/methods/chat.postMessage) while providing any of the following parameters:

*   `username` to specify the username for the published message.
*   `icon_url` to specify a URL to an image to use as the profile photo alongside the message.
*   `icon_emoji` to specify an emoji (using colon shortcodes, eg. `:white_check_mark:`) to use as the profile photo alongside the message.

If the `channel` parameter is set to a User ID (beginning with `U`), the message will appear in that user's direct message channel with Slackbot. To post a message to that user's direct message channel with the app, use the DM ID (beginning with `D`) instead.

* * *

### Text streaming in messages {#text-streaming}

Three Web API methods work together to provide users a text streaming experience to provide a closer alignment with expected behavior from LLM tools.

Use the [`chat.startStream`](/reference/methods/chat.startStream) method to start a text stream, the [`chat.appendStream`](/reference/methods/chat.appendStream) method to append it, and the [`chat.stopStream`](/reference/methods/chat.stopStream) method to stop it. These allow the user to see the response from the LLM as a text stream, rather than a single block of text sent all at once.

The [task card](/reference/block-kit/blocks/task-card-block) block and [plan](/reference/block-kit/blocks/plan-block) block can be used alongside the streaming API methods to help show the reader what the Agent is and will be doing. Use the `task_display_mode` parameter in `chat.startStream` to choose between displaying tasks individually in a timeline view or grouped together in a plan view. Then use the `chunks` parameter in the three streaming API methods to create and modify the plan and task content.

The Bolt framework, available for [Python](/tools/bolt-python/concepts/message-sending/) and [JavaScript](/tools/bolt-js/concepts/message-sending) use underlying SDKs that makes this process simpler. Click the links to review the implementation of those methods in the Bolt framework.

* * *

## Scheduling messages {#scheduling}

Scheduling a message is just a bit of fancy footwork on top of sending a message directly. One thing you'll need before starting is a Slack app. If you don't have one yet, [here's a very quick guide to help you create one](/app-management/quickstart-app-settings#creating). Make sure you create the app in a workspace that won't mind you posting lots of test messages!

### Permissions {#scheduling-permissions}

Now for some particularly pleasant permissions news: your app's permissions are actually the ones you've already acquired to post messages!

Let’s quickly recap. Your app uses a bot token to perform actions as itself. You grant your app permission to perform specific actions by giving its bot token the corresponding scopes.

For your app to send scheduled messages, it only needs one scope: [`chat:write`](/reference/scopes/chat.write).

If you don't already know the ID of the channel you wish to send messages to, you may also want to give your app another scope: [`channels:read`](/reference/scopes/channels.read). This scope lets your app retrieve a list of all the public channels in a workspace so you can [pick one to publish a message to](/messaging/sending-and-scheduling-messages#conversations).

### Schedule a message {#scheduling-a-message}

Our guide to directly sending messages talked you through a call to [`chat.postMessage`](/reference/methods/chat.postMessage). Let's reinvent our app to send a reminder instead: say, about a weekly team breakfast.

```
{  "channel": "YOUR_CHANNEL_ID",  "text": "Woooooooof! (Dinner time!)"}
```

If you want to do things the hard way, your app **could** implement state storage and job scheduling to send this message at the right time each week, using a database and batch task runner.

If you prefer an easier approach, use a scheduled message instead. Add a `post_at` parameter to your JSON request, and pass your JSON to the [`chat.scheduleMessage`](/reference/methods/chat.scheduleMessage) method instead of the `chat.postMessage` method:

*   HTTP
*   Java
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.scheduleMessageContent-type: application/jsonAuthorization: Bearer xoxb-your-token{  "channel": "YOUR_CHANNEL_ID",  "text": "Hey, team. Don't forget about breakfast catered by John Hughes Bistro today.",  "post_at": 1551891428,}
```

```
import com.slack.api.bolt.App;import com.slack.api.bolt.AppConfig;import com.slack.api.bolt.jetty.SlackAppServer;import com.slack.api.methods.SlackApiException;import java.io.IOException;import java.time.ZonedDateTime;import java.time.temporal.ChronoUnit;public class ChatScheduleMessage {    public static void main(String[] args) throws Exception {        var config = new AppConfig();        config.setSingleTeamBotToken(System.getenv("SLACK_BOT_TOKEN"));        config.setSigningSecret(System.getenv("SLACK_SIGNING_SECRET"));        var app = new App(config); // `new App()` does the same        app.command("/schedule", (req, ctx) -> {            var logger = ctx.logger;            var tomorrow = ZonedDateTime.now().truncatedTo(ChronoUnit.DAYS).plusDays(1).withHour(9);            try {                var payload = req.getPayload();                // Call the chat.scheduleMessage method using the built-in WebClient                var result = ctx.client().chatScheduleMessage(r -> r                    // The token you used to initialize your app                    .token(ctx.getBotToken())                    .channel(payload.getChannelId())                    .text(payload.getText())                    // Time to post message, in Unix Epoch timestamp format                    .postAt((int) tomorrow.toInstant().getEpochSecond())                );                // Print result                logger.info("result: {}", result);            } catch (IOException | SlackApiException e) {                logger.error("error: {}", e.getMessage(), e);            }            // Acknowledge incoming command event            return ctx.ack();        });        var server = new SlackAppServer(app);        server.start();    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// Unix timestamp for tomorrow morning at 9AMconst tomorrow = new Date();tomorrow.setDate(tomorrow.getDate() + 1);tomorrow.setHours(9, 0, 0);// Channel you want to post the message toconst channelId = "C12345";try {  // Call the chat.scheduleMessage method using the WebClient  const result = await client.chat.scheduleMessage({    channel: channelId,    text: "Looking towards the future",    // Time to post message, in Unix Epoch timestamp format    post_at: tomorrow.getTime() / 1000  });  console.log(result);}catch (error) {  console.error(error);}
```

```
import datetimeimport loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# Create a timestamp for tomorrow at 9AMtomorrow = datetime.date.today() + datetime.timedelta(days=1)scheduled_time = datetime.time(hour=9, minute=30)schedule_timestamp = datetime.datetime.combine(tomorrow, scheduled_time).strftime('%s')# Channel you want to post message tochannel_id = "C12345"try:    # Call the chat.scheduleMessage method using the WebClient    result = client.chat_scheduleMessage(        channel=channel_id,        text="Looking towards the future",        post_at=schedule_timestamp    )    # Log the result    logger.info(result)except SlackApiError as e:    logger.error("Error scheduling message: {}".format(e))
```

Then sit back and relax. Like magic, the message appears at the moment specified in the `post_at` Unix timestamp.

![Bot avatar](/assets/images/oslo-b2272998a620e09f3081347b23f939cc.png)

Oslo

Woooooooof! (Dinner time!)

Messages can only be scheduled up to 120 days in advance.

The HTTP response from `chat.scheduleMessage` includes a `scheduled_message_id`, which can be used to [delete the scheduled message](#deleting) before it is sent. Read on to find out how.

### List your scheduled messages {#listing}

"Fire and forget" reminders are all well and good, but the best-laid breakfast plans sometimes fall through. Let's say a holiday closes the office during one of your team's scheduled breakfast clubs. Better cancel that reminder message!

Your app can list all the messages that it currently has scheduled with the [`chat.scheduledMessages.list`](/reference/methods/chat.scheduledMessages.list) method.

Call the `chat.scheduledMessages.list` method with optional `channel`, `latest`, and `oldest` parameters to specify which channel and time range you're interested in:

*   HTTP
*   Java
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.scheduledMessages.listContent-type: application/jsonAuthorization: Bearer xoxb-your-token{    "channel": "YOUR_CHANNEL_ID",    "latest": 1551991429,    "oldest": 1551991427,}
```

```
import com.slack.api.Slack;import com.slack.api.methods.SlackApiException;import org.slf4j.LoggerFactory;import java.io.IOException;public class ChatScheduledMessagesList {    /**     * Lists scheduled messages using latest and oldest timestamps     */    static void listScheduledMessages(String latest, String oldest) {        // you can get this instance via ctx.client() in a Bolt app        var client = Slack.getInstance().methods();        var logger = LoggerFactory.getLogger("my-awesome-slack-app");        try {            // Call the chat.scheduledMessages.list method using the built-in WebClient            var result = client.chatScheduledMessagesList(r -> r                // The token you used to initialize your app                .token(System.getenv("SLACK_BOT_TOKEN"))                .latest(latest)                .oldest(oldest)            );            // Print scheduled messages            for (var message : result.getScheduledMessages()) {                logger.info("message: {}", message);            }            // Print result            logger.info("result: {}", result);        } catch (IOException | SlackApiException e) {            logger.error("error: {}", e.getMessage(), e);        }    }    public static void main(String[] args) throws Exception {        listScheduledMessages("1551991429", "1551991427");    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// List scheduled messages using latest and oldest timestampsasync function listScheduledMessages(latest, oldest) {  try {    // Call the chat.scheduledMessages.list method using the WebClient    const result = await client.chat.scheduledMessages.list({      latest: latest,      oldest: oldest    });    // Print scheduled messages    for (const message of result.scheduled_messages) {      console.log(message);    }  }  catch (error) {    console.error(error);  }}listScheduledMessages("1551991429", "2661991427");
```

```
import osimport loggingfrom slack_sdk.errors import SlackApiError# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk.web import WebClient# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])logger = logging.getLogger(__name__)# List scheduled messages using latest and oldest timestampsdef list_scheduled_messages(latest, oldest):    try:        # Call the chat.scheduledMessages.list method using the WebClient        result = client.chat_scheduledMessages_list(            latest=latest,             oldest=oldest        )        # Print scheduled messages        for message in result["scheduled_messages"]:            logger.info(message)    except SlackApiError as e:        logger.error("Error creating conversation: {}".format(e))list_scheduled_messages("1551991429", "2661991427")
```

`oldest` signifies the Unix timestamp of the earliest range you're interested in. `latest` signifies, well, the latest. So `oldest` must be less than `latest` if both are specified.

The endpoint yields scheduled messages sent by your app, plus [pagination information](/apis/web-api/pagination).

```
{    "ok": true,    "scheduled_messages": [        {            "id": "YOUR_SCHEDULED_MESSAGE_ID",            "channel_id": "YOUR_CHANNEL_ID",            "post_at": 1551991428,            "date_created": 1551891734        }    ],    "response_metadata": {        "next_cursor": ""    }}
```

Now that you've got the `id` of the breakfast club reminder you want to delete, one more method call awaits, so read on.

### Delete a scheduled message {#deleting}

With the `scheduled_message_id` that you need in hand, it's time to banish that breakfast reminder. Use the [`chat.deleteScheduledMessage`](/reference/methods/chat.deleteScheduledMessage) endpoint:

*   HTTP
*   Java
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.deleteScheduledMessageContent-type: application/jsonAuthorization: Bearer xoxb-your-token{    "channel": "YOUR_CHANNEL_ID",    "scheduled_message_id": "YOUR_SCHEDULED_MESSAGE_ID"}
```

```
import com.slack.api.Slack;import com.slack.api.methods.SlackApiException;import org.slf4j.LoggerFactory;import java.io.IOException;public class ChatDeleteScheduledMessage {    /**     * Deletes scheduled message using channel ID and scheduled message ID     */    static void deleteScheduledMessage(String channel, String id) {        // you can get this instance via ctx.client() in a Bolt app        var client = Slack.getInstance().methods();        var logger = LoggerFactory.getLogger("my-awesome-slack-app");        try {            var result = client.chatDeleteScheduledMessage(r -> r                // The token you used to initialize your app                .token(System.getenv("SLACK_BOT_TOKEN"))                .channel(channel)                .scheduledMessageId(id)            );            // Print result            logger.info("result: {}", result);        } catch (IOException | SlackApiException e) {            logger.error("error: {}", e.getMessage(), e);        }    }    public static void main(String[] args) throws Exception {        deleteScheduledMessage("C12345", "Q123ABC95");    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// The ts of the message you want to deleteconst messageId = "U12345";// ID of channel that the scheduled message was sent toconst channelId = "C12345";try {  // Call the chat.deleteScheduledMessage method using the WebClient  const result = await client.chat.deleteScheduledMessage({    channel: channelId,    scheduled_message_id: messageId  });  console.log(result);}catch (error) {  console.error(error);}
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# The ts of the message you want to deletemessage_id = "U12345"# ID of channel that the scheduled message was sent tochannel_id = "C12345"try:    # Call the chat.deleteScheduledMessage method using the built-in WebClient    result = client.chat_deleteScheduledMessage(        channel=channel_id,        scheduled_message_id=message_id    )    # Log the result    logger.info(result)except SlackApiError as e:    logger.error(f"Error deleting scheduled message: {e}")
```

You'll receive the typical success response once your scheduled message has been deleted.

### Update a scheduled message {#updating}

To update a pending scheduled message, [delete](#deleting) the old message and then [schedule](#scheduling) a new one.

Reminders, notifications, even calendars—all now fall within grasp of your app. You don't have to store any state at all if you don't wish to. Instead, list and delete your scheduled messages on the fly. Combine scheduled messages with [user interactivity](/messaging/creating-interactive-messages) to create a chat bot that's a capable, clever assistant. Enjoy the newfound simplicity of scheduled messages!