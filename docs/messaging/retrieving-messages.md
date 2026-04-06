Source: https://docs.slack.dev/messaging/retrieving-messages

# Retrieving messages

Slack apps tend to encounter messages most often when receiving them in [Events API](/apis/events-api/) payloads or in request payloads when users invoke [slash commands](/interactivity/implementing-slash-commands) or [custom actions](/interactivity/implementing-shortcuts).

However, there are some occasions where it might be necessary for an app to actively seek out a message and find it in the wild.

This guide will show you how to access the history of a Slack conversation and then pull out the details of a specific message. It will also show you how to identify threaded messages and retrieve the replies in a thread.

* * *

## Before you begin {#begin}

You'll need a Slack app if you don't already. [Here's a quick guide to help you create one](/app-management/quickstart-app-settings). Make sure you create the app in a test workspace, because you're going to be requesting some major data access permissions.

Once you've done that, come back here.

## Requesting the necessary permissions {#permissions}

In a raw state, your app will only be able to view messages that are sent to it. In order to read anything else, it will need to [request scopes to get permission](/authentication).

There are [lots of scopes available](/reference/scopes), and you can read our [OAuth guide](/authentication) for more information on why they're needed, and what they do. For this guide, we need to add two scopes:

*   [`channels:read`](/reference/scopes/channels.read). This scope lets your app retrieve a list of all the public channels in a workspace so that we can [pick one to retrieve a message from](#finding_conversation).
*   [`channels:history`](/reference/scopes/channels.history). This scope lets your app view all the messages within any public channel in a workspace.

You can add these scopes to your app like so:

1.  Open the settings for your app from the [App Management](https://api.slack.com/apps) page.
2.  In the navigation menu, select **OAuth & Permissions**.
3.  Scroll down to the **Scopes** section, and pick `channels:read` and `channels:history` from the drop down menu.
4.  Click **Save changes**.
5.  Scroll back to the top of this page and look for the button that says **Install App to Workspace** (or **Reinstall App** if you've done this before). Click it. You'll now see a permission request screen to install your app to its original workspace.

If you had already installed your app to its original workspace before, you might still see the permissions screen if the scopes you just added weren't previously granted to your app.

Authorize your app and you should see a success message. On the **OAuth & Permissions** settings page you're brought back to, you should now see an OAuth access token available. Grab this token and store it for later, as we'll use that token to make some [Web API](/apis/web-api/) calls.

## Finding a conversation {#finding_conversation}

In order to find a valid Slack conversation ID, we'll use the [`conversations.list`](/reference/methods/conversations.list) method. This API will return a list of all public channels in the workspace your app is installed to. You'll need the [`channels:read`](/reference/scopes/channels.read) scope granted to your app.

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

## Retrieving conversation history {#conversations}

With the information you just collected and your previously generated token, we can make another [Web API](/apis/web-api/) call to [`conversations.history`](/reference/methods/conversations.history):

*   HTTP
*   Java
*   JavaScript
*   Python

```
GET https://slack.com/api/conversations.historyAuthorization: Bearer xoxb-your-token{  "channel": "YOUR_CONVERSATION_ID",  "latest": "YOUR_TS_VALUE",  "limit": 1,  "inclusive": true}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// Store messagelet message;// Fetch conversation history using the ID and a TS from the last exampleasync function fetchMessage(id, ts) {  try {    // Call the conversations.history method using the built-in WebClient    const result = await app.client.conversations.history({      // The token you used to initialize your app      token: "xoxb-your-token",      channel: id,      // In a more realistic app, you may store ts data in a db      latest: ts,      // Limit results      inclusive: true,      limit: 1    });    // There should only be one result (stored in the zeroth index)    message = result.messages[0];    // Print message text    console.log(message.text);  }  catch (error) {    console.error(error);  }}// Fetch message using a channel ID and message TSfetchMessage("C12345", "15712345.001500");
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# ID of channel that the message exists inconversation_id = "C01JASD6802"try:    # Call the conversations.history method using the WebClient    # The client passes the token you included in initialization        result = client.conversations_history(        channel=conversation_id,        inclusive=True,        oldest="1610144875.000600",        limit=1    )    message = result["messages"][0]    # Print message text    print(message["text"])except SlackApiError as e:    print(f"Error: {e}")
```

Dropping in your token and `id` values, [this method will return](/reference/methods/conversations.history#response) a list of a list of messages and events within the chosen conversation. The [method's reference](/reference/methods/conversations.history#response) contains [example responses](/reference/methods/conversations.history#response) and some explanations of the data included within.

The important part for this guide is the `messages` array, which contains every message in the conversation. For the next part of the guide, you need to grab the `ts` value of one of these message objects; we'll explain why in a second.

## Retrieving individual messages {#individual_messages}

The structure of message objects retrieved via Slack APIs is very similar to the [general structure of a message payload you want to publish](/messaging#payloads).

There are a few additional fields that describe the author (such as `user` or `bot_id`), but there's also an additional `ts` field. The `ts` value is essentially the ID of the message, guaranteed unique within the context of a channel or conversation.

They _look like_ UNIX/epoch timestamps, hence `ts`, with specified milliseconds. But they're actually message IDs, even if they're partially composed in seconds-since-the-epoch.

The `ts` of a message can be used in many operations such as [replying to it in a thread](/messaging/sending-and-scheduling-messages#threading), or [modifying the message](/messaging/modifying-messages). But it can also be used to retrieve the message by itself.

Using the [`ts` from the previous step](#conversations) with the information previously collected, and your token, we can make a slightly different call to [`conversations.history`](/reference/methods/conversations.history):

*   HTTP
*   Java
*   JavaScript
*   Python

```
GET https://slack.com/api/conversations.historyAuthorization: Bearer xoxb-your-token{  channel: "CONVERSATION_ID_HERE"}
```

```
import com.slack.api.Slack;import com.slack.api.methods.SlackApiException;import com.slack.api.model.Message;import org.slf4j.LoggerFactory;import java.io.IOException;import java.util.List;import java.util.Optional;import static java.util.Collections.emptyList;public class ConversationsHistory {    static Optional<List<Message>> conversationHistory = Optional.empty();    /**     * Fetch conversation history using ID from last example     */    static void fetchHistory(String id) {        // you can get this instance via ctx.client() in a Bolt app        var client = Slack.getInstance().methods();        var logger = LoggerFactory.getLogger("my-awesome-slack-app");        try {            // Call the conversations.history method using the built-in WebClient            var result = client.conversationsHistory(r -> r                // The token you used to initialize your app                .token(System.getenv("SLACK_BOT_TOKEN"))                .channel(id)            );            conversationHistory = Optional.ofNullable(result.getMessages());            // Print results            logger.info("{} messages found in {}", conversationHistory.orElse(emptyList()).size(), id);        } catch (IOException | SlackApiException e) {            logger.error("error: {}", e.getMessage(), e);        }    }    public static void main(String[] args) throws Exception {        fetchHistory("C24601");    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// Store conversation historylet conversationHistory;// ID of channel you watch to fetch the history forlet channelId = "C24601";try {  // Call the conversations.history method using WebClient  const result = await client.conversations.history({    channel: channelId  });  conversationHistory = result.messages;  // Print results  console.log(conversationHistory.length + " messages found in " + channelId);}catch (error) {  console.error(error);}
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# Store conversation historyconversation_history = []# ID of the channel you want to send the message tochannel_id = "C123ABC456"try:    # Call the conversations.history method using the WebClient    # conversations.history returns the first 100 messages by default    # These results are paginated, see: /methods/conversations.history$pagination    result = client.conversations_history(channel=channel_id)    conversation_history = result["messages"]    # Print results    logger.info("{} messages found in {}".format(len(conversation_history), channel_id))except SlackApiError as e:    logger.error("Error creating conversation: {}".format(e))
```

You can read the [`conversations.history` reference](/reference/methods/conversations.history) for a more in-depth explanation of what these additional parameters do, but essentially we're telling the API to return one result from the conversation's history, using the message `ts` as a starting point.

## Other encounters with individual messages {#other_individual_messages}

As we mentioned before, your app is likely to encounter individual messages in ways other than a direct retrieval.

If you subscribe to certain [Events API](/apis/events-api/) types, you will receive a notification payload from each event that may contain a message object. For example, the [`app_mention`](/reference/events/app_mention) event will be sent whenever someone mentions your app in a message, and that source message will be included in the notification payload.

After you [publish a message](/messaging/sending-and-scheduling-messages#publishing), you'll receive an API response that will include a message object containing the newly-created message.

[Slash commands](/interactivity/implementing-slash-commands#app_command_handling) and [custom actions](/interactivity/implementing-shortcuts#request_payload) both send similar request payloads when a user invokes them in Slack. Those payloads contain a message object that describes the source message of the invocation.

[Interactive components in messages](/messaging/creating-interactive-messages) will also [send request payloads](/interactivity/handling-user-interaction#payloads) when the components are used. Again, these payloads will contain a message object that describes the source of the interaction.

In all of the above cases, the structure of the message object is similar to [that outlined above](#individual_messages). Read the relevant individual guides to see examples of the kinds of payloads or responses your app will receive.

* * *

## Threaded messages {#threading}

We've explained the basics behind threaded messages [elsewhere](/messaging#threading) (familiarize yourself with our terminology if you haven't already, because it can get tangled), but how do you know when the message you've received or retrieved is part of a thread? And if you have a parent message, how do you retrieve all the replies to it? Read on to find out.

### Spotting threads {#finding_threads}

There's a few steps involved with [spotting a thread](/messaging#threading) and then understanding the context of a message within it. Let's unspool them:

1.  Detect a threaded message by looking for a `thread_ts` value in the message object. The existence of such a value indicates that the message is part of a thread.
2.  Identify parent messages by comparing the `thread_ts` and `ts` values. If they are _equal_, the message is a parent message.
3.  Threaded replies are also identified by comparing the `thread_ts` and `ts` values. If they are _different_, the message is a reply.

One quirk of threaded messages is that a parent message object will retain a `thread_ts` value, even if all its replies have been deleted.

### Retrieving threads {#pulling_threads}

Use [`conversations.replies`](/reference/methods/conversations.replies) to retrieve replies to a specific message, regardless of whether it's from a public or private channel, direct message, or otherwise.

Here's an example response from `conversations.replies`:

```
{    "ok": true,    "messages": [        {            "type": "message",            "user": "U123ABC456",            "text": "Was there was there was there what was there was there what was there was there there was there.",            "thread_ts": "1482960137.003543",            "reply_count": 3,            "replies": [                // Deprecated, to be removed on October 18, 2019.                {                    "user": "U123ABC456",                    "ts": "1483037603.017503"                },                {                    "user": "U123ABC456",                    "ts": "1483051909.018632"                },                {                    "user": "U123ABC456",                    "ts": "1483125339.020269"                }            ],            "reply_users": ["U123ABC456", "U123ABC456", "U123ABC456"],  // max 5            "reply_users_count": 3,            "latest_reply": "1483125339.020269",            "subscribed": true,            "last_read": "1484678597.521003",            "unread_count": 0,            "ts": "1482960137.003543"        },        {            "type": "message",            "user": "U123ABC456",            "text": "Shutters shut and shutters and so shutters shut and shutters and so and so shutters and so shutters shut and so shutters shut and shutters and so.",            "thread_ts": "1482960137.003543",            "parent_user_id": "U123ABC456",            "ts": "1483037603.017503"        },        {            "type": "message",            "user": "U123ABC456",            "text": "Let me recite what history teaches. History teaches.",            "thread_ts": "1482960137.003543",            "parent_user_id": "U123ABC456",            "ts": "1483051909.018632"        },        {            "type": "message",            "user": "U123ABC456",            "text": "I love you Alice B. Toklas and so does Gertrude Stein.",            "thread_ts": "1482960137.003543",            "parent_user_id": "U123ABC456",            "ts": "1483125339.020269"        }    ],    "has_more": true,    "response_metadata": {        "next_cursor": "bmV4dF90czoxNDg0Njc4MjkwNTE3MDkx"    }}
```

This [`conversations.replies`](/reference/methods/conversations.replies) method returns a `messages` array that first contains the parent message object, followed by message objects for all the threaded replies.

Want to learn how to _reply_ to threads? [Read our guide to sending messages](/messaging/sending-and-scheduling-messages).