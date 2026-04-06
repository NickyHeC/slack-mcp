Source: https://docs.slack.dev/apis

# Slack APIs

Every Slack app and [workflow](/workflows) has access to a range of APIs that provide access to read, write, and update many types of data in Slack.

Read on to learn about our core APIs, and discover how to use them to make magic.

* * *

## Web API {#web-api}

The Web API supplies a collection of [HTTP methods](/reference/methods) that underpin the majority of Slack app functionality.

With over 100 methods available, it's impossible to explain _everything_ that's possible with the Web API, but we're sure there's one right for your app.

Our [Web API](/apis/web-api/) guide explains the basic process of interacting with these methods. Once you've read up on that, dive into the [list of available methods](/reference/methods).

* * *

## Events API {#events-api}

The Events API is a streamlined way to build apps that respond to activities in Slack.

Subscribe to the [events](/reference/events) you want from a range of possibilities. Build a Slack app that can [react to those events](/interactivity#responses) usefully.

Tell us where to send the events you carefully select and we'll push them to your app securely. We'll even retry when things don't work out.

Read our [Events API](/apis/events-api/) guide to learn how to subscribe to and handle events.

Check out our [Event delivery](/apis/events-api/comparing-http-socket-mode) guide to explore your options with how to receive event payloads: via a public HTTP URL or using the magic of WebSocket via Socket Mode.

If you don't wish to expose a public, static HTTP endpoint to communicate with Slack, [Socket Mode](/apis/events-api/using-socket-mode) can help.

* * *

## Slack Status API {#slack-status-api}

The Slack Status API describes the health of the Slack product. When there's an incident, outage, or maintenance, the Slack Status API reflects all the information we have on the issue, including which features of Slack are affected and detailed updates over time.

### Atom and RSS Feed {#feed}

Receive updates on the health of Slack services by subscribing to our Atom or RSS feeds. Use your favorite subscription tool to subscribe to `https://slack-status.com/feed/atom` or `https://slack-status.com/feed/rss`. You could even use the `/feed` command in Slack to subscribe to our Status feed — but it might not work if some parts of Slack are unavailable. An outside feed reader might be a better choice.

Note that many readers check for updates only a few times an hour. Set your feed reader to poll for updates often (for example, once a minute) if you need to be notified immediately of a Slack issue.

See the [Slack Status API reference](/reference/slack-status-api) for endpoint information.

* * *

## Other APIs {#other-apis}

Beyond the Web and Events APIs, we have a range of other niche APIs that are suitable for specific types of apps.

*   [**Admin API**](/admins) are a subset of Web APIs that are geared towards automating and simplifying the administration of Slack organizations.
*   [**SCIM API**](/admins/scim-api/) are available for user provisioning and management.
*   [**Audit Logs API**](/admins/audit-logs-api/) are tailored for building security information and event management tools.
*   [**Legacy RTM API**](/legacy/legacy-rtm-api) is an outmoded API that provides WebSocket access to some of the same functionality as the Web and Events APIs. We list it here for completeness even though it has been deprecated.