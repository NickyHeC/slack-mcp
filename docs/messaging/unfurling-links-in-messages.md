Source: https://docs.slack.dev/messaging/unfurling-links-in-messages

# Unfurling links in messages

When users post messages in Slack containing links, we attach previews, adding context and continuity to conversations. Three facets of link unfurling exist:

*   **Classic link unfurling** is the default treatment for links posted in Slack. When a link is spotted, Slack crawls it and provides a preview.
    
*   **Slack app unfurling** is a customizable experience initiated when Slack recognizes a link associated with _your_ app, and then sends your Slack app a corresponding event.
    
*   **Work Objects** take the unfurling experience even further by allowing you to create rich user interactions with any type of entity or data _other_ than conversations within Slack. Examples of these entities include files, tasks, and incident tickets.
    

## Work Objects {#work-objects}

![Flexpane component](/assets/images/flexpane-component-e2014db88fe890c9028afdb7fd373bad.png)

Work Objects allow you to provide users with richer previews and greater feature extensibility than Slack app unfurling. With Work Objects, you can offer users a dynamic, real-time view of app data (files, tasks, tickets, and so on), side-by-side with conversations to provide your users with more context.

Refer to our [Work Objects](/messaging/work-objects-overview) documentation for more details.

## Slack app unfurling {#app_unfurling}

Teach links new tricks by using the [Events API](/apis/events-api/) and [Web API](/apis/web-api/) together. To begin, you'll need your very own [Slack app](/app-management/quickstart-app-settings#creating).

While we'll provide explanation of each step, here's a glance at what the configuration and process of unfurling looks like for an app:

![Diagram of an app unfurling a link](/assets/images/chat_unfurl_diagram-1773039376abfc7fcc9dd93baa966494.svg)

1.  Provide an inciting incident: have a user post a message containing a fully-qualified URL matching the registered domain.
2.  Your app will receive a [`link_shared`](/reference/events/link_shared) event, giving your app the hints it needs for the unfurling process.
3.  Your app uses [`chat.unfurl`](/reference/methods/chat.unfurl) to attach custom unfurling behavior to the original message. Like a cherry on top of an already delicious sundae, you can use [blocks](/block-kit) to make the message rich and interactive.

We'll go into the details of each step in the following sections, from configuring your app to contextualizing the link in conversation.

### Configuring your app {#setup}

To support custom app unfurling, your app needs to have permissions to listen to links posted in Slack _and_ to unfurl those links.

#### Scopes and token types {#configure_scopes}

Navigate to your [**app settings**](https://api.slack.com/apps) and choose the **OAuth & Permissions** sidebar to select scopes.

*   [`links:read`](/reference/scopes/links.read) lets your app read specific links that are posted in Slack.
*   [`links:write`](/reference/scopes/links.write) gives your app permission to unfurl content associated with links.

A [bot token](/authentication/tokens#bot) is recommended for all link unfurling operations.

#### Events {#configure_events}

If you haven't already, configure your app to [support the Events API](/apis/events-api/#prepare). After that, navigate to the **Event Subscriptions** sidebar.

*   Under **Subscribe to bot events**, add the [`link_shared`](/reference/events/link_shared) event to receive information about links posted in Slack that are associated with your app.
*   The [`link_shared`](/reference/events/link_shared) event will dispatch for all channels in each workspace it's installed in.

These events do not contain the message itself, they contain only the info about the message you need to provide it unfurl behavior: the message's `ts` value, the channel it appeared in, and which URLs it contained matching your registered domains.

#### Domain(s) {#configuring_domains}

On the **Event Subscriptions** page, select **App unfurl domains**. Your app can register up to five domains, and will only receive [`link_shared`](/reference/events/link_shared) events for URLs that match your registered domains.

Adding or removing domains **requires re-installation of your Slack app**. Every time an app is installed, the installing user is agreeing to those specifically-mentioned domains.

Each domain you register will be matched to URLs by a few heuristics:

*   Domains must have a TLD and cannot be a TLD alone (`example.com` and `another.example.com` are valid, `example` is not and nor is `.com`).
*   IP addresses are not domains, and cannot be matched.
*   All _additive_ subdomains and paths to the domain you provide will be considered matches.
*   By including a subdomain in your domain, you _exclude_ the _naked_ domain.
*   When users mention links to one of your domains, it must be fully qualified with a protocol (`http://` or `https://`). Slack will not unfurl decidedly ambiguous domain and URL mentions.
*   The `link_shared` event is dispatched when a message posted includes a matching domain, with the exception of messages posted by classic apps. Apps will also not receive `link_shared` events for their own messages. Refer to [Differences between classic apps and Slack apps](/legacy/legacy-app-migration/differences-between-classic-apps-and-granular-slack-apps) for more information.
*   When users mention links and they contain an explicit port (such as `https://example.com:23/skidoo`), Slack will still consider it a clean match to a registered `example.com`.

Be courteous, kind, and helpful

You should own these domains and if you don't, you must follow all the terms, conditions, rules, policies, proclamations, warnings, and edicts around a domain.

Be sure to leave out the protocol part of a URL when registering your domain. Discard any `http://` or `https://` or path or query string components. Finally, Unicode domains are not supported.

### Receiving link_shared events {#event_deliveries}

You've set everything up: your Slack app, the [Events API](/apis/events-api/), a [`link_shared`](/reference/events/link_shared) event subscription, and you've registered your domain(s). You've installed your Slack app on a workspace, specifically requesting the scopes you needed _after_ you've registered your domains.

You have the knowledge. You have the power. You are ready to receive and react to [`link_shared`](/reference/events/link_shared) events.

When a user shares a link in a channel that matches your criteria, you'll receive an event shaped like this:

```
{    "token": "XXYYZZ",    "team_id": "TXXXXXXXX",    "api_app_id": "AXXXXXXXXX",    "event": {        "type": "link_shared",        "channel": "Cxxxxxx",        "is_bot_user_member": false,        "user": "Uxxxxxxx",        "message_ts": "123452389.9875",        "unfurl_id": "C123456.123456789.987501.1b90fa1278528ce6e2f6c5c2bfa1abc9a41d57d02b29d173f40399c9ffdecf4b",        "thread_ts": "123456621.1855",        "source": "conversations_history",        "links": [            {                "domain": "example.com",                "url": "https://example.com/12345"            },            {                "domain": "example.com",                "url": "https://example.com/67890"            },            {                "domain": "another-example.com",                "url": "https://yet.another-example.com/v/abcde"            }        ],        "user_locale": "en-US"    },    "type": "event_callback",    "authorizations": [        {            "user_id": "UXXXXXXX1",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev08MFMKH6",    "event_time": 123456789}
```

For details on these fields, reference the [`link_shared`](/reference/events/link_shared) event page.

Once you've received the `link_shared` event, you can decide what to do next. Most likely, you'll use those `url` values within the `event` object to look up what to display to the user. Maybe you'll make an API call to another service. Maybe you'll just reference your app's own base of knowledge and never query another service at all.

Be sure and respond with a friendly `HTTP 200 OK` to the event as quickly as possible. Do not wait to wrestle an unfurl with [`chat.unfurl`](#attaching_content) before telling Slack you received the event: consider this [`link_shared`](/reference/events/link_shared) event a kind of ping. Now it's up to you to pong with [`chat.unfurl`](/reference/methods/chat.unfurl).

#### Composer unfurls {#unfurl_previews}

A `link_shared` event with `"source": "composer"` will be dispatched to your service when a user pastes a link from your domain into the message composer of a channel where your app is installed to the channel's workspace or org.

The event structure will be as follows:

```
{    "token": "XXYYZZ",    "team_id": "T123ABC456",    "api_app_id": "A123ABC456",    "event": {        "type": "link_shared",        "user": "U123ABC456",        "channel_id": "COMPOSER",        "message_ts": "gryl3kb80b3wm49ihzoo35fyqoq08n2y",        "unfurl_id": "gryl3kb80b3wm49ihzoo35fyqoq08n2y",        "source": "composer",        "links": [            {                "domain": "example.com",                "url": "https://example.com/12345"            },            {                "domain": "example.com",                "url": "https://example.com/67890"            },            {                "domain": "another-example.com",                "url": "https://yet.another-example.com/v/abcde"            }        ]    },    "type": "event_callback",    "authorizations": [        {            "user_id": "U123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev123ABC456",    "event_time": 123456789}
```

Unlike existing app unfurl `link_shared` events, There won't be a `message_ts`, and potentially not a `channel_id` yet. It is possible to compose a message that does not (yet) contain this context.

To ensure backwards compatibility, the `channel_id` will always be set to the value `"COMPOSER"`. The `unfurl_id` property serves as the unique identifier for an unfurl. The `message_ts` property will be set to the same value as `unfurl_id`.

The `source` property indicates where this unfurl is coming from. Its value can be either `composer` (for previews) or `conversations_history` (for posted messages).

Your app then calls the `chat.unfurl` API method using the stored corresponding user token for the user who sent the link (or bot token if the app is installed) with the contents of the unfurl, including the `unfurl_id` and `source` (or alternatively the `channel_id` & `ts`):

**Example with `unfurl_id` and `source`**

```
{    "token": "xoxp-xxxxxxx-xxxxxx",    "unfurl_id": "gryl3kb80b3wm49ihzoo35fyqoq08n2y",    "source": "composer",    "unfurls": {        "https://gentle-buttons.com/carafe": {            "preview": {                "type": "preview",                "elements": [                    {                        "type": "image",                        "image_url": "https://gentle-buttons.com/img/carafe-filled-with-red-wine.png",                        "alt_text": "Secret Project Walkthrough thumbnail"                    },                    {                        "type": "mrkdwn",                        "text": "*Secret Project Walkthrough*"                    }                ]            },            "blocks": [                {                    "type": "section",                    "text": {                        "type": "mrkdwn",                        "text": "Take a look at this carafe, just another cousin of glass"                    },                    "accessory": {                        "type": "image",                        "image_url": "https://gentle-buttons.com/img/carafe-filled-with-red-wine.png",                        "alt_text": "Stein's wine carafe"                    }                }            ]        }    }}
```

**Example with `channel_id` and `ts`**

```
{    "token": "xoxp-xxxxxxx-xxxxxx",    "channel_id": "COMPOSER",    "ts": "gryl3kb80b3wm49ihzoo35fyqoq08n2y",    "unfurls": {        "https://gentle-buttons.com/carafe": {            "preview": {                "type": "preview",                "elements": [                    {                        "type": "image",                        "image_url": "https://gentle-buttons.com/img/carafe-filled-with-red-wine.png",                        "alt_text": "Secret Project Walkthrough thumbnail"                    },                    {                        "type": "mrkdwn",                        "text": "*Secret Project Walkthrough*"                    }                ]            },            "blocks": [                {                    "type": "section",                    "text": {                        "type": "mrkdwn",                        "text": "Take a look at this carafe, just another cousin of glass"                    },                    "accessory": {                        "type": "image",                        "image_url": "https://gentle-buttons.com/img/carafe-filled-with-red-wine.png",                        "alt_text": "Stein's wine carafe"                    }                }            ]        }    }}
```

The Slack client will update the message composition with a preview of the unfurl. The contents of the preview are pulled from the preview key if present, otherwise the preview will be generated from the existing blocks layout or legacy attachment. The app name and icon are retrieved from your Slack Marketplace listing.

See below for an example:

![Unfurl Preview](/assets/images/unfurl_preview-7038c21be9cff0a92d47030bd6f873fd.png)

The user has an option to remove the unfurl while composing the message, but if they leave it in and hit send, a second `link_shared` event will be dispatched to your app, providing the `channel` and `message_ts` context with a `source` property of `conversations_history`.

#### Sending unfurl content via chat.unfurl {#attaching_content}

The [`chat.unfurl`](/reference/methods/chat.unfurl) method requires a token and your content. It also requires either a combination of `ts` and `channel` or `unfurl_id` and `source`.

You can fetch the `ts` and `channel` values [from the `link_shared` event](#handling_event_deliveries) sent to your app. Once you're in possession of these parameters, you can call the [`chat.unfurl`](/reference/methods/chat.unfurl) method and include your content within the `unfurls` parameter.

The `unfurls` parameter expects a JSON map where the keys correspond to the URLs contained in the [`link_shared`](/reference/events/link_shared) event.

Each defined URL may contain [an array of blocks](/block-kit#getting_started), including your custom arrangement of text alongside actionable buttons and selects. All of the [typical formatting](/block-kit) available to you in messages holds true.

If you call `chat.unfurl` with a `application/x-www-form-encoded type` content type (rather than `application/json`), the unfurls parameter will expect a URL-encoded string fragment of your JSON map.

Here's an example if you're using a `application/json` content type:

```
{    "channel": "C12345",    "ts": "156762948.24601",    "unfurls": {        "https://gentle-buttons.com/carafe": {            "blocks": [                {                    "type": "section",                    "text": {                        "type": "mrkdwn",                        "text": "Take a look at this carafe, just another cousin of glass"                    },                    "accessory": {                        "type": "image",                        "image_url": "https://gentle-buttons.com/img/carafe-filled-with-red-wine.png",                        "alt_text": "Stein's wine carafe"                    }                }            ]        }    }}
```

To explore all `chat.unfurl` parameters, [reference its method page](/reference/methods/chat.unfurl).

If your attempt to attach your unfurl to the message is successful, you'll be the proud winner of a rather generic `HTTP 200 OK` response:

```
{    "ok": true}
```

There are error responses too. You'll receive them if you forget to include `ts`, `channel`, or properly-formed `unfurls` parameter. See the errors section of [`chat.unfurl`](/reference/methods/chat.unfurl#errors) for more details.

That's it, you made a link unfurl! While your work could be done here, you can opt to make your unfurl richer with interactivity.

### Making unfurls interactive {#interactivity}

Since the blocks you provide in link unfurls are just like other Slack app-enabled [message layouts](/messaging#complex_layouts), you can also make them interactive with [interactive components](/messaging/creating-interactive-messages#getting_started). Let's build on the knowledge gained so far and, provided you've set yourself up to use message buttons already, let's examine a more complicated example.

Let's say your app received an event detailing a match for `https://figment.example.com/imagine`. This is a service you provide to help stimulate the imagination. At this specific URL, you generate a random imagination exercise to stimulate the mind.

![Choosing what to do next on Neptune](/assets/images/unfurl_interactive-4aafc6e3de76b5759ce1ba0252d6df42.svg)

This imagination machine might construct its JSON hash response to something resembling this:

```
{    "https://figment.example.com/imagine": {        "blocks": [            {                "type": "section",                "text": {                    "type": "mrkdwn",                    "text": "*Let's pretend we're on a rocket ship to Neptune.*\nThe planet Neptune looms near. What do you want to do?"                },                "accessory": {                    "type": "button",                    "action_id": "orbit",                    "text": {                        "type": "plain_text",                        "text": "Orbit"                    },                    "style": "primary"                }            },            {                "type": "actions",                "elements": [                    {                        "type": "button",                        "action_id": "land",                        "text": {                            "type": "plain_text",                            "text": "Attempt to land"                        }                    },                    {                        "type": "button",                        "action_id": "leave",                        "text": {                            "type": "plain_text",                            "text": "Go home"                        },                        "style": "danger"                    }                ]            }        ]    }}
```

Now your interactive unfurl is firmly attached to the originating message, complete with buttons. Almost everything you already know about [interactive components](/block-kit#making-things-interactive) is true for these kind of buttons too.

#### Alternate interactive payload behavior {#interactive_payloads}

When a user decides to click on one of your interactive components, we'll send your request URL an invocation payload as usual.

The only catch is that there will be no `message` field. Instead, there will be an `app_unfurl` field that will only contain the blocks that your app added when providing the unfurl. You still can't see the entire message.

Here's an example invocation:

```
{  "type": "block_actions",  "actions": [    {      "action_id": "orbit",      "block_id": "05cM",      "text": { ... },      "style": "primary",      "type": "button",      "action_ts": "123456791.2111"    }  ],  "app_unfurl": {    "id": 1,    "blocks": [ ... ],    "app_unfurl_url": "https://figment.example.com/imagine",    "is_app_unfurl": true  },  "team": {        "id": "T123456",        "domain": "example"    },    "channel": {        "id": "C123456",        "name": "generators"    },    "user": {        "id": "U061F7AUR",        "name": "exemplar"    },    "token": "xxx",    "container": {        "type": "message_attachment",        "message_ts": "123456789.9875",        "attachment_id": 1,        "channel_id": "C123456",        "is_ephemeral": false,        "is_app_unfurl": true,        "app_unfurl_url": "https://figment.example.com/imagine"  },  "trigger_id": "112345.327112347633.59cee77e21deda86fd37639d3b5ddbcc",  "response_url": "https://hooks.slack.com/actions/T123456/XXXX/XXXX",}
```

Here's a closer look at the most relevant fields in this kind of interactive unfurl:

Field

Type

Description

Required?

`is_app_unfurl`

boolean

When set to `true`, this invocation is related to a Slack app unfurl your app is registered to handle. When absent or `false`, it's a standard action.

No

`app_unfurl`

object

Contains blocks relevant to link unfurling from the original message that started this flow. See below.

No

From this point forward, you can use the `response_url` and all the other tools in the interactive toolbox to evolve this interaction. What next will befall our intrepid interstellar travelers?

### Requiring authenticated unfurls {#authenticated_unfurls}

Not all links are wild and free, full of content anyone can see. Some links require users to validate their identity. Slack provides several paths to unfurl non-public content based on user authentication.

Note that for apps using these authenticated unfurl requests, users who are on the workspace where the app was created will always receive these requests, regardless of whether they have muted unfurl requests (i.e. selecting `No` as shown below) or whether the app is already one of the user's Muted Apps:

![An ephemeral message asking the user to set up a Slack app](/assets/images/muted_unfurl_auth-fd74174a80fb778d76c378a66ea142c2.png)

### Slack Marketplace {#slack-marketplace}

If you have a Slack Marketplace app, we provide a way to ask the user posting a link to your service to authenticate before proceeding with an unfurl that the whole channel can see.

If you react to a `link_shared` event with a call to [`chat.unfurl`](/reference/methods/chat.unfurl) with the `user_auth_required` parameter set to `true`, instead of displaying custom unfurl content, Slack displays an ephemeral message encouraging the user to install your app:

![An ephemeral message asking the user to install the Slack app before proceeding with unfurling services](/assets/images/ephemeral_unfurl_auth-7253e0f887cfc6b5ace3f7352bc7cff6.svg)

By selecting **Install from Slack Marketplace**, users will be taken to your application's installation or configuration page — even if it's not a part of the Slack Marketplace.

Unless you're building an internal integration, you'll likely want to provide an [Add to Slack](/authentication/installing-with-oauth#overview) button on your app's home page that requests the `links:read` and `links:write` scopes during the OAuth flow.

This way, you use the OAuth sequence to validate the authority of the member to unfurl privileged content within a channel for everyone to see. During the callback step where the user returns to your website, you would capture any needed additional information about the user and their identity on your service. What you need to do is up to you and the context of your content. Avoid surprising users by doing something unexpected.

After installation, the next time the user posts a message mentioning your links (or even retroactively), you can provide unfurl content.

### Custom authentication flows {#custom_auth_flow}

To send users more directly to your website and a personalized authentication flow, use [`chat.unfurl`](/reference/methods/chat.unfurl)'s `user_auth_url` parameter to provide a "just in time" URL on your servers.

Or, painstakingly author an amazing ephemeral message with formatting using the `user_auth_message` parameter, including the link to your custom authentication flow in the message. Your ephemeral message can also include [block kit](/block-kit) content with use of [`user_auth_blocks`](/reference/methods/chat.unfurl#arg_user_auth_blocks).

### Typical flows {#typical-flows}

When building an app that also needs to authenticate with your service or a third party service outside of your control — for example, if your app uses Facebook to authorize users or you require them to sign in to your app first — you can handle that authentication step as part of this flow.

*   First specify the `user_auth_url` or `user_auth_message` parameters when using [`chat.unfurl`](/reference/methods/chat.unfurl). The URL should point to a page you control. If relevant to your app, include any `state` information you need in the URL.
*   As users arrive, send them down one of these paths — the order is up to you:
    *   Authenticate them into your app using service-specific login and password techniques.
    *   Generate a Slack OAuth authorization URL and send the now-authenticated-with-your-service user to authorize your Slack app.
    *   Associate any additional accounts like Facebook by invoking each authentication flow and returning back to your service.

Whether you authorize users _before_ or _after_ Slack redirects the user to your OAuth redirect URI depends on how you want to juggle maintaining state, and where you expect any authentication fatigue-based drop-off to occur.

### Tips, tricks, and warnings {#tips}

*   Links will only unfurl if the message they appear in contains a fully-qualified URL. The protocol, such as `http` or `https`, is required.
*   As you register additional domains, workspaces will need to install your Slack app again for changes to take effect on that workspace.
*   App unfurls are a terrific way to build [interactive workflows](/block-kit#making-things-interactive).
*   Interactive payloads do not include a `message` object. For limited information about the original message, you can instead look in the `app_unfurl` object.
*   It's best to only register domains that you own, but if you're providing wrapper functionality for domains owned by others, you must follow all the terms, conditions, and policies declared by the owner. Even if that means you can't provide app unfurl functionality for that domain.
*   The `link_shared` event doesn't contain the original message; your app just learns about any links that match your registered domains.
*   Everyone in a channel can see your app's unfurls. Using [authenticated unfurls](#authenticated_unfurls) only requires authentication to _unfurl_, but still broadcasts those unfurls to a conversation.
*   The `link_shared` event is **not** dispatched when a message posted by an _app or integration_ includes a matching domain.
*   If two apps are installed and are both subscribed to `link_shared` events for the same domain, only the originally installed app will receive the event.
*   You may run into an `invalid_blocks` error when passing a valid Block Kit message containing a [rich text section element](/reference/block-kit/blocks/rich-text-block#section) to the [`chat.unfurl`](/reference/methods/chat.unfurl) API method. Even though rich text blocks are now generally supported for use with the Slack API, the [`chat.unfurl`](/reference/methods/chat.unfurl) API method does not currently support them.

In addition to Slack app unfurling, we generate content previews by default. Learn more about classic unfurling below.

Link unfurls and prompt injection

Consider disabling link unfurls when working with messages from an LLM in your app. Read more about the risk of data exfiltration and how to prevent it in the [security](/security#prompt-injection) documentation.

* * *

## Classic link unfurling {#classic_unfurl}

If a workspace doesn't have a Slack app handler for a specific domain, unfurling will fall back to classic behavior: Slack crawls the URL, looks for common OpenGraph and X (formerly known as Twitter) Card metadata, and renders some micro-approximation of the content. For some domains, Slack even provides its own extra bells and whistles. See the anatomy of a classic unfurl below:

![Anatomy of an unfurl](/assets/images/message_anatomy_of_an_unfurl-9caa8495978de17414a1d26ca6a7b7ab.png)

When deciding whether to unfurl a link, we consider the type of content that was linked to. Our servers must fetch every URL in a message to determine what kind of content it references. We treat "media"—images, videos, or audio—differently to pages that are primarily text-content.

Here are some examples of media content:

*   [http://www.youtube.com/watch?v=wq1R93UMqlk](http://www.youtube.com/watch?v=wq1R93UMqlk)
*   [http://www.flickr.com/photos/karstenmay/11787125913/](http://www.flickr.com/photos/karstenmay/11787125913/)
*   [https://twitter.com/tweetsoutloud/status/416692366037094400](https://twitter.com/tweetsoutloud/status/416692366037094400)
*   [http://imgs.xkcd.com/comics/regex\_golf.png](http://imgs.xkcd.com/comics/regex_golf.png)

While these are examples of text-based content:

*   [http://www.cnn.com/2014/01/06/tech/web/ces-unveiled/index.html?hpt=hp\_c3](http://www.cnn.com/2014/01/06/tech/web/ces-unveiled/index.html?hpt=hp_c3)
*   [https://slack.com/](https://slack.com/)

By default, we unfurl all links in any messages posted by users and Slack apps. This applies to messages posted via [incoming webhooks](/messaging/sending-messages-using-incoming-webhooks), [`chat.postMessage`](/reference/methods/chat.postMessage) and [`chat.postEphemeral`](/reference/methods/chat.postEphemeral). We also unfurl links to media based content within Block kit [`blocks`](/reference/block-kit/blocks).

If you'd like to override these defaults on a per-message basis, you can pass `unfurl_links` or `unfurl_media` top-level fields while posting the message. `unfurl_links` applies to text-based content, while `unfurl_media` applies to media-based content. These flags are mutually exclusive; the `unfurl_links` flag has no effect on media content.

Ensure that the `links:write` scope is added to your [**app settings**](https://api.slack.com/apps) for apps that will be performing app unfurling.

To prevent links from unfurling, set both `unfurl_links` and `unfurl_media` to `false` when posting messages to **stop** Slack from crawling a link and attempting to display an unfurl.

For example, Slack will not crawl or unfurl the URL featured in `text` below:

```
{	"channel": "birds",	"text": "Here's an example of a bird.",	"unfurl_links": false,	"unfurl_media": false,	"blocks": [		{			"type": "section",			"text": {				"type": "mrkdwn",				"text": "Check out the Easter Bluebird <https://www.allaboutbirds.org/guide/Eastern_Bluebird/|Eastern Bluebird>"			}		}	]}
```

There is one notable exception to these rules: we never unfurl links where the label is a complete substring of your URL minus the protocol. This is so that a paragraph of text can contain domain names or abbreviated URLs that are treated as a reference rather than link to be unfurled. For example, if a message contains a link to `http://example.com` with the label `example.com`, that link will not be unfurled. There are more examples of this rule in the following section.

#### Examples {#examples}

All of these examples are for incoming webhooks, but similar rules apply to our other APIs:

`api.slack.com` is text-based, so this link will not unfurl:

```
{    "text": "<https://api.slack.com>"}
```

Passing `"unfurl_links": true` means the link will unfurl:

```
{    "text": "<https://api.slack.com>",    "unfurl_links": true}
```

This xkcd link is an image, so the content will be unfurled by default:

```
{    "text": "<http://imgs.xkcd.com/comics/regex_golf.png>"}
```

We can then disable that using the `unfurl_media` flag:

```
{    "text": "<http://imgs.xkcd.com/comics/regex_golf.png>",    "unfurl_media": false}
```

Even though `unfurl_links` is true, this link has a label that matches the URL minus the protocol, so the link will not unfurl:

```
{    "text": "<https://api.slack.com|api.slack.com>",    "unfurl_links": true}
```

The label for this link does not match the URL minus the protocol, so this link will unfurl:

```
{    "text": "<https://api.slack.com|Slack API>",    "unfurl_links": true}
```