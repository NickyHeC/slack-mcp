Source: https://docs.slack.dev/apis/web-api/rate-limits

# Rate limits

Slack platform features and APIs rely on rate limits to help provide a predictably pleasant experience for users.

The details of how and when rate limiting works _differs_ between features. This article gives an overview of the rate limits you're likely to encounter for Slack platform features, and then notes how the limits apply to each feature.

App types and rate limits

Slack is changing the way rate limits are applied to non-Marketplace apps. Apps already approved for the Slack Marketplace and internal customer-built applications should not see rate limit changes.

Effective **May 29, 2025**, all newly-created Slack apps that are commercially distributed and have not been approved for the Slack Marketplace will be subject to new rate limits for the [`conversations.history`](/reference/methods/conversations.history) and [`conversations.replies`](/reference/methods/conversations.replies) API methods. Existing installations of apps that are not Marketplace-approved are not subject to the new posted limits. You can read more in our [changelog post](/changelog/2025/05/29/rate-limit-changes-for-non-marketplace-apps) and can find more info about our Marketplace guidelines and submission process [here](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements).

## Overview {#overview}

Broadly, you'll encounter limits like these, applied on a "_per API method per workspace/team per app_" basis.

Feature/API

Limit

Notes

Web API Tier 1

1+ per minute

Access tier 1 methods infrequently. A small amount of burst behavior is tolerated.

Web API Tier 2

20+ per minute

Most methods allow at least 20 requests per minute, while allowing for occasional bursts of more requests.

Web API Tier 3

50+ per minute

Tier 3 methods allow a larger number of requests and are typically attached to methods with paginating collections of conversations or users. Sporadic bursts are welcome.

Web API Tier 4

100+ per minute

Enjoy a large request quota for Tier 4 methods, including generous burst behavior.

Web API Special Tier

_Varies_

Rate limiting conditions are unique for methods with this tier. For example, [`chat.postMessage`](/reference/methods/chat.postMessage) generally allows posting one message per second per channel, while also maintaining a workspace-wide limit. Consult the method's documentation to better understand its rate limiting conditions.

Posting messages

1 per second

Short bursts >1 allowed. If you attempt bursts, there is no guarantee that messages will be stored or displayed to users. If the burst exceeds available limits, users will see an error message indicating that some messages from your app are not being displayed.

Incoming webhooks

1 per second

Short bursts >1 allowed.

Events API events

30,000 deliveries per workspace/team per app per 60 minutes

Larger bursts are sometimes allowed.

Workflow triggers: event triggers

10,000 per hour

Workflow triggers: webhook triggers

10 per minute

Workflow steps: AI summary

At the overall team level: 150 requests per minute, and a burst of 300 requests is allowed; per workflow: 1 request per hour, and a burst of 10 requests is allowed

Read on for more details on how rate limits are applied to different Slack features and APIs.

## Burst limiting {#burst-limiting}

You'll see mentions of burst tolerance in the chart above; burst limits are similar to rate limits. While a rate limit defines the maximum requests allowed in a specific timeframe (typically per minute), a burst limit defines the maximum rate of requests allowed concurrently.

Slack does not share precise burst limits externally, because these numbers are subject to change and we don't want you to to build your app with a specific burst capacity in mind only to have to change it later. However, we do recommend you design your apps with a limit of 1 request per second for any given API call, knowing that we'll allow it to go over this limit as long as this is only a temporary burst.

"Why even have burst limits?" you might ask. Slack is primarily a communication tool for humans. We try to detect apps acting spammy, unintentionally or not, and quiet them down to avoid hindering users' ability to communicate and use their workspace's archive.

* * *

## Web API rate limiting {#web}

Your app's requests to the [Web API](/apis/web-api/) are evaluated per method, per workspace. Rate limit windows are per minute.

Each [Web API method](/reference/methods) is assigned one of four _rate limit tiers_, listed [above](#overview). Tier 1 accepts the fewest requests and Tier 4 the most. There's also a `special` tier for rate-limiting behavior that's unique to a method.

All Slack plans receive the same rate limit tier for each method.

The _Facts_ section of each method's reference documentation will indicate its rate limit tier. Check out the [`conversations.list` documentation](/reference/methods/conversations.list) for an example of a Tier 2 method. Each tier's limits are subject to change.

### Pagination limitation {#pagination}

For methods supporting [cursored pagination](/apis/web-api/pagination), the rate limit given applies when you're _using_ pagination. If you're not, you'll receive stricter rate limits—for example, you'll be allowed to make fewer requests if you attempt to fetch all of [`users.list`](/reference/methods/users.list) without pagination.

## Responding to rate limiting conditions {#headers}

If you exceed a rate limit when using any of our HTTP-based APIs (including incoming webhooks), Slack will return a `HTTP 429 Too Many Requests` error, and a `Retry-After` HTTP header containing the number of seconds until you can retry.

For example, if your app exceeds the rate limit of `conversations.info`, you might receive a raw HTTP response like this:

```
HTTP/1.1 429 Too Many RequestsRetry-After: 30
```

This response instructs your app to wait 30 seconds before attempting to call `conversations.info` with any [token](/authentication/tokens) awarded to your app from this workspace. By evaluating the `Retry-After` header you can wait for the indicated number of seconds before retrying the same request or continuing to use that method for this workspace.

Calls to other methods on behalf of this workspace are not restricted. Calls to the same method for other workspaces for this app are also not restricted.

## Limits when posting messages {#posting-messages}

In general, apps may post no more than one message per second per channel, whether a message is posted via [`chat.postMessage`](/reference/methods/chat.postMessage), an incoming webhook, or one of the many other ways to send messages in to Slack. We allow bursts over that limit for short periods. However, if your app continues to exceed its allowance over longer periods of time, we will begin rate limiting.

If you go over these limits while using the [Real Time Messaging API](/legacy/legacy-rtm-api) you will receive an error message as a reply. If you continue to send messages, your app will be disconnected. Continuing to send messages after exceeding a rate limit runs the risk of your app being permanently disabled.

What if your app requires a higher volume of messaging? Other services provide an interface for logging, searching, aggregating, and archiving messages at higher throughputs. These include [Papertrail](https://papertrailapp.com/), [Loggly](https://www.loggly.com/), [Splunk](http://www.splunk.com/) and [LogStash](http://logstash.net/).

## Profile update rate limits {#profile_updates}

Update a user's profile, including custom status, sparingly. Special [rate limit](/apis/web-api/rate-limits) rules apply when updating profile data with [`users.profile.set`](/reference/methods/users.profile.set). A token may update a single user's profile no more than **10** times per minute. And a single token may only set **30** user profiles per minute. Some burst behavior is allowed.

## Events API {#events}

Event deliveries to your server via the Events API currently max out at 30,000 per workspace/team per app per 60 minutes.

When a workspace generates more than 30,000 events, you'll receive an informative event called [`app_rate_limited`](/reference/events/app_rate_limited), describing the workspace and timestamp when rate limiting began.

```
{    "token": "Jhj5dZrVaK7ZwHHjRyZWjbDl",    "type": "app_rate_limited",    "team_id": "T123456",    "minute_rate_limited": 1518467820,    "api_app_id": "A123456"}
```

Learn more about [Events API rate limiting](/apis/events-api/#rate_limiting) and our tolerance for [delivery failures](/apis/events-api/#failure_limits).

## RTM APIs (legacy) {#rtm}

### Message delivery {#rtm-message-delivery}

Message delivery to your app is not rate limited over RTM. You'll receive every event the connecting token is allowed to see. You may receive more events than you can come up with, so we recommend decoupling your processing of events from the receiving of them.

### Posting messages {#rtm-posting-messages}

Rate limits _do_ apply to posting messages or other write events to the Real Time Messaging websocket. Please limit writes to 1 per second.

If you sustain writes beyond these limits when using our [Real Time Messaging API](/legacy/legacy-rtm-api) you will receive an [error message](/legacy/legacy-rtm-api#errors) as a reply. If you continue to send messages your app will be disconnected.

The message server will disconnect any client that sends a message longer than 16 kilobytes. This includes all parts of the message, including JSON syntax, not just the message text. Clients should limit messages sent to channels to 4000 characters, which will always be under 16k bytes even with a message comprised solely of non-BMP Unicode characters at 4 bytes each. If the message is longer a client should prompt to split the message into multiple messages, create a snippet or create a post.

### Obtaining websocket URLs {#rtm-websocket-urls}

Rate limits also apply to the [`rtm.start`](/reference/methods/rtm.start) and [`rtm.connect`](/reference/methods/rtm.connect) methods for obtaining the URL needed to connect to a websocket.

Limit requests to these methods to no more than 1 per minute, with some bursting behavior allowed. If you enter rate limit conditions when trying to fetch websocket URLs, you won't be able to reconnect until the window passes.

## Other functionality {#other}

We reserve the right to rate limit other functionality to prevent abuse, spam, denial-of-service attacks, or other security issues. Where possible we'll return a descriptive error message, but the nature of this type of rate limiting often prevents us from providing more information.