Source: https://docs.slack.dev/messaging/modifying-messages

# Modifying messages

A message captures a specific moment in time. But if you're an app, you might want to publish messages that communicate something that changes over time. Perhaps its the progress of a long running database request, or maybe just a message asking a user to wait for the response of an external API request.

In these cases and others, it's useful to have a way to modify messages from their original form. Slack apps are able to update and delete messages via APIs.

* * *

## Updating messages {#updating}

Any non-[ephemeral](/messaging#ephemeral) message may possibly be updated by an app, by using the [`chat.update`](/reference/methods/chat.update) method.

The process for using this API is largely the same as that for [sending messages](/messaging/sending-and-scheduling-messages), but there are a few small differences:

*   You can't _move_ a message, so the `channel` parameter is used as an identifier for the target message to update, not as a way to update the conversation a message is in.
*   Ephemeral messages can't be updated in this way.
*   An app can't just update every message in a conversation - only ones posted by the authenticated user of the token being used, including those posted _as the app_. The same applies to bot users, where you use a bot user token. [Read the API reference for more information](/reference/methods/chat.update#valid_message_types).

### Updating messages using response_url {#updating_response_url}

When a user interacts with an [interactive element in a message](/messaging/creating-interactive-messages#interaction), [a payload containing a `response_url` will be sent](/interactivity/handling-user-interaction#payloads) to the app that published the interactive message.

This `response_url` can be used to [publish new messages](/interactivity/handling-user-interaction#message_responses). It can also be used to **update** the original interactive message, regardless of whether it was an [ephemeral message](/messaging#ephemeral) or not.

Read [our interactive messages guide](/interactivity/handling-user-interaction#updating_message_response) for more details on how to update messages using `response_url`.

* * *

## Deleting messages {#deleting}

The [`chat.delete`](/reference/methods/chat.delete) API method offers apps the powerful ability to delete messages, using the [same permissions as those used to send messages](/messaging/sending-and-scheduling-messages#permissions):

*   HTTP
*   Java
*   JavaScript
*   Python

```
POST https://slack.com/api/chat.deleteContent-type: application/jsonAuthorization: Bearer xoxb-your-token{  "channel": "PARENT_CHANNEL_ID",  "ts": "MESSAGE_TO_DELETE"}
```

```
import com.slack.api.bolt.App;import com.slack.api.bolt.AppConfig;import com.slack.api.bolt.jetty.SlackAppServer;import com.slack.api.methods.SlackApiException;import com.slack.api.model.event.ReactionAddedEvent;import java.io.IOException;public class ChatDelete {    public static void main(String[] args) throws Exception {        var config = new AppConfig();        config.setSingleTeamBotToken(System.getenv("SLACK_BOT_TOKEN"));        config.setSigningSecret(System.getenv("SLACK_SIGNING_SECRET"));        var app = new App(config); // `new App()` does the same        // When a user reacts to a message with an X emoji, delete the message        app.event(ReactionAddedEvent.class, (req, ctx) -> {            var logger = ctx.logger;            try {                var event = req.getEvent();                // Only delete message if emoji is "x"                if (event.getReaction().equals("x")) {                    // Call the chat.delete method using the built-in WebClient                    var item = event.getItem();                    var result = ctx.client().chatDelete(r -> r                        // The token you used to initialize the app, stored in context                        .token(ctx.getBotToken())                        .channel(item.getChannel())                        .ts(item.getTs())                    );                    logger.info("result: {}", result);                }            } catch (IOException | SlackApiException e) {                logger.error("error: {}", e.getMessage(), e);            }            return ctx.ack();        });        var server = new SlackAppServer(app);        server.start();    }}
```

```
// Require the Node Slack SDK package (github.com/slackapi/node-slack-sdk)const { WebClient, LogLevel } = require("@slack/web-api");// WebClient instantiates a client that can call API methods// When using Bolt, you can use either `app.client` or the `client` passed to listeners.const client = new WebClient("xoxb-your-token", {  // LogLevel can be imported and used to make debugging simpler  logLevel: LogLevel.DEBUG});// The ts of the message you want to deleteconst messageId = "12345.9876";// The ID of the channel that contains the messageconst channelId = "C12345";try {  // Call the chat.delete method using the WebClient  const result = await client.chat.delete({    channel: channelId,    ts: messageId  });  console.log(result);}catch (error) {  console.error(error);}
```

```
import loggingimport os# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)from slack_sdk import WebClientfrom slack_sdk.errors import SlackApiError# WebClient instantiates a client that can call API methods# When using Bolt, you can use either `app.client` or the `client` passed to listeners.client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))logger = logging.getLogger(__name__)# The ts of the message you want to deletemessage_id = "12345.9876"# The ID of the channel that contains the messagechannel_id = "C12345"try:    # Call the chat.chatDelete method using the built-in WebClient    result = client.chat_delete(        channel=channel_id,        ts=message_id    )    logger.info(result)except SlackApiError as e:    logger.error(f"Error deleting message: {e}")
```

The right for an app to delete a message depends on a few caveats:

*   If using a standard user's [user token](/authentication/tokens#user), only messages posted by that user, or those posted as the app, may be deleted.
*   If using a Workspace Admin user's [user token](/authentication/tokens#user), most messages in that workspace can be deleted.
*   If using a [bot user token](/authentication/tokens#bot), only messages posted by that bot user, or those posted as the app, may be deleted.
*   Ephemeral messages can't be deleted in this way.

If the message has some [threaded replies](/messaging#threading), then those replies will be left in the conversation, with a placeholder informing viewers about the deleted message:

![This message was deleted placeholder, showing orphaned replies](/assets/images/messaging_deleting_threaded-1f4479267377e42c7a4c5796841c4d9b.png)

### Deleting messages using response_url {#deleting_response_url}

When a user interacts with an [interactive element in a message](/messaging/creating-interactive-messages#interaction), [a payload containing a `response_url` will be sent](/interactivity/handling-user-interaction#payloads) to the app that published the interactive message.

This `response_url` can be used to [publish new messages in response](/interactivity/handling-user-interaction#message_responses). It can also be used to **delete** the original interactive message, regardless of whether it was an [ephemeral message](/messaging#ephemeral) or not.

Read [our interactive messages guide for more details on how to delete messages using `response_url`](/interactivity/handling-user-interaction#deleting_message_response).