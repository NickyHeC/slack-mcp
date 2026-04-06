Source: https://docs.slack.dev/apis/web-api/real-time-search-api

# Using the Real-time Search API

The API formerly known as the Data Access API

Are you looking for the Data Access API? You found it! The Data Access API has evolved into the Real-time Search API. Read more about it [here](/changelog/2026/02/17/slack-mcp).

The Real-time Search (RTS) API allows apps to access Slack data through a secure search interface. This approach enables third-party applications to retrieve relevant Slack data without storing customer information on external servers. Supplying this data as context to a large language model (LLM) helps ensure more relevant and accurate responses to user queries. Read on to discover how to employ this API exclusively in your [app using AI features](/ai/developing-agents).

The Real-time Search API is designed for real-time data retrieval and is intended to be used in response to user interactions, either within Slack or from a third-party system that has an active Slack connection. It performs searches across all channels the user has access to within their Slack workspace and returns an array of messages and files relevant to the search query.

Make it org-ready

Consider making your app that uses the RTS API an [org-ready](/enterprise/organization-ready-apps/) app. Doing so allows you to manage a single user token and send a single request to query every workspace the user and app have access to.

## API overview {#overview}

The Real-time Search API can be used in two scenarios:

*   When a user interacts with an [AI-enabled app](/ai) within the Slack client. With this method, a bot or user token can be used.
*   When a user interacts with a third-party service that has an active Slack connection outside of the Slack client. With this method, a user token is required. Details on user authentication and API flows are outlined below.

Using the Real-time Search API, your app performs the search on behalf of the authenticated user, ensuring that only content the user has access to is returned.

### User authentication {#auth}

To use the Real-time Search API to fetch private conversation data or to use it outside the Slack client, a user token is required. To obtain this token, your application must ask each user to go through the [OAuth authorization flow](/authentication/installing-with-oauth). To initiate this, direct the user to your Slack app's installation URL, which can be found in the **Manage Distribution** section of the app settings page. Upon successful authorization, your app will receive the user's `xoxp-` user token.

### Required Scopes {#required-scopes}

Your app must contain at least the `search:read.public` scope and can optionally contain any of the scopes following that in this list. Each provides various levels of access. Include all of them for a wider base from which to search.

Scope

Description

Token Type Allowed

[`search:read.public`](/reference/scopes/search.read.public)

Read access to all public channel messages

Bot, User

[`search:read.private`](/reference/scopes/search.read.private)

Read access to all private channel messages

User

[`search:read.mpim`](/reference/scopes/search.read.mpim)

Read access to all multi-person direct messages

User

[`search:read.im`](/reference/scopes/search.read.im)

Read access to all direct messages

User

[`search:read.files`](/reference/scopes/search.read.files)

Read access to all files

Bot, User

[`search:read.users`](/reference/scopes/search.read.users)

Read access to a workspace's users

Bot, User

The `search:read.public` scope allows searching for data in public channels within the workspace(s) where the app is installed AND the searching user is a member. The searching user need not be a member of the public channels, just of the workspace, for the channels to be included in the search results.

Including any one of the `search:read.private`, `search:read.mpim`, and `search:read.im` scopes allows users to consent to those scopes within the Slack client. Users can choose to grant access to their private channels. They can only grant that access if the app has been installed with the corresponding scope. For example, if an admin installs the app with the `search:read.public` and `search:read.im` scopes, users will be able to consent to the IM scope, but not private/MPIM.

The `search:read.files` scope grants access to search for files, but it needs to be combined with channel-type scopes to determine where those files can be search. For example,

*   `search:read.files` + `search:read.public` grants access to public files
*   `search:read.files` + `search:read.private` grants access to public and private files

Having the `search:read.files` scope lets you search for files, but if you want to download the file content, you also need the `files:read` scope.

Additionally, the following scopes are useful to have in an AI-enabled app too:

Scope

Description

[`im:history`](/reference/scopes/im.history)

View messages and other content in DMs the app has been added to

[`chat:write`](/reference/scopes/chat.write)

Write access to post messages channels and conversations

To add these scopes, go to your [app settings](https://api.slack.com/apps), select your app, then:

1.  Go to the **OAuth & Permissions** section in the navigation sidebar
2.  Scroll down to the **Scopes** section
3.  Add the scopes listed above

### Using the action_token {#action-token}

All API calls made using a bot token require an `action_token`. API calls made using a user token do not require an `action_token`.

An app can obtain the `action_token` needed to query the Real-time Search API from either a [`message`](/reference/events/message) event or an [`app_mention`](/reference/events/app_mention) event. Message events that include the `action_token` are:

*   [`message.im`](/reference/events/message.im)
*   [`message.mpim`](/reference/events/message.mpim)
*   [`message.groups`](/reference/events/message.groups)
*   [`message.channels`](/reference/events/message.channels) (when the app is mentioned)

The [`app_mention`](/reference/events/app_mention) event contains an `action_token` in the payload when the app is mentioned using `@app-name`. If a user sends a DM to your app, the @ mention is not needed and you will receive an `action_token` either way. The app must be subscribed to at least one of these events in order to get the token to pass to the `assistant.search.context` API method.

## API usage {#api-usage}

The Real-time Search API consists of two methods.

The [`assistant.search.context`](/reference/methods/assistant.search.context) method searches messages, files, channels and users across your Slack organization. See the [method reference page](/reference/methods/assistant.search.context) for details regarding parameters, their types and descriptions, expected request/response formats, and rate limiting details.

```
{  "query": "What is project gizmo?",  "channel_types": ["public_channel", "private_channel", "mpim", "im"]}
```

The [`assistant.search.info`](/reference/methods/assistant.search.info) method returns the search capabilities on a given team. See the [method reference page](/reference/methods/assistant.search.info) for more details.

### Call patterns {#call-patterns}

The Real-time Search API enables powerful workflows that combine search discovery with messaging capabilities. Partners can build agents that help users find and interact with Slack channels and users directly from external platforms.

#### Context call pattern {#context-call-pattern}

To enable more context around RTS search results, use these two endpoints:

*   [`conversations.history`](/reference/methods/conversations.history)
*   [`conversations.replies`](/reference/methods/conversations.replies)

Related and necessary scopes to use:

*   [`channels:history`](/reference/scopes/channels.history)
*   [`groups:history`](/reference/scopes/groups.history)
*   [`im:history`](/reference/scopes/im.history)
*   [`mpim:history`](/reference/scopes/mpim.history)

How to use them in a sequence:

1.  Call the [`assistant.search.context`](/reference/methods/assistant.search.context) method to search on behalf of a user. Identify a channel or thread where more context would be helpful. Use the results (including `context_messages`) to identify a thread or channel.
2.  Pull full thread messages using the [`conversations.replies`](/reference/methods/conversations.replies) method.
3.  Or pull surrounding messages in channel via the [`conversations.history`](/reference/methods/conversations.history) method.

This might be helpful when you'd like to:

*   Get the full thread from a specific message timestamp
*   Pull the last 50 messages from a project channel
*   Fetch replies to a specific announcement
*   Pull the details of a thread around a document shared in Slack from your platform

#### User and channel discovery pattern {#discovery-pattern}

This pattern involves using the RTS API to search for users and channels, then enabling direct messaging to those discovered entities. This workflow is particularly useful for agents operating outside of Slack that need to facilitate communication within Slack workspaces.

Pattern overview:

1.  **Search for users or channels**: Use the [`assistant.search.context`](/reference/methods/assistant.search.context) method with a `content_types: ["users", "channels"]` argument to discover relevant people or channels based on their query.
    
    Example query:
    
    ```
    {  "query": "What channels are related to project alpha?",  "content_types": ["channels"],  "channel_types": ["public_channel", "private_channel"]}
    ```
    
2.  **Present discovery results**: Show users the found channels and users with relevant context from the search results.
    
3.  **Enable direct messaging**: Allow users to send messages directly to discovered channels or users through your agent interface.
    
    ```
    {  "channel": "C0123456", // from search results  "text": "Hi team! I have an update on project alpha...",  "token": "xoxp-..."}
    ```
    

You might use this for the following scenarios:

*   **Project channel discovery**: Help users find and message project-specific channels when working from external project management tools.
*   **Team member lookup**: Allow users to search for team members by expertise or project involvement, then initiate direct conversations.
*   **Cross-platform notifications**: Enable agents to search for relevant channels and post updates or alerts from external systems.
*   **Onboarding assistance**: Help new team members discover relevant channels and introduce themselves.

When using this pattern, keep in mind the following best practices:

*   Always respect user permissions when displaying search results.
*   Provide clear context about why specific channels or users are being suggested.
*   Allow users to confirm before sending messages to discovered channels or users.
*   Include relevant information from search results to help users make informed decisions.

#### Advanced query patterns with OR operator {#or-operator}

The Real-time Search API supports powerful `OR` operations that allow you to search for multiple alternative terms or concepts in a single query. This feature is particularly useful for building flexible search experiences that can accommodate different terminology or multiple related topics.

The `OR` operator can be used in both semantic and keyword search modes:

*   **Natural language**: `"What are the updates on project alpha or project beta?"`
*   **Keyword search**: `"budget OR finance OR expenses"`
*   **Mixed content**: `"meeting notes OR action items OR decisions"`

A common scenario involves building a dashboard that shows updates across multiple related projects or initiatives. Using the `OR` operator, you can efficiently search for content related to any of several projects in a single API call.

```
{  "query": "What are the latest updates on project alpha OR project beta OR project gamma?",  "content_types": ["messages", "files"],  "channel_types": ["public_channel", "private_channel"],  "token": "xoxp-...",  "sort": "timestamp",  "sort_dir": "desc",  "limit": 20}
```

Here are some other examples.

Technology stack query

```
{  "query": "deployment issues with kubernetes OR docker OR terraform",  "content_types": ["messages", "files"]}
```

Multi-team coordination

```
{  "query": "blockers OR dependencies OR handoffs from engineering OR design OR product",  "channel_types": ["public_channel", "private_channel"]}
```

Incident management

```
{  "query": "outage OR downtime OR performance issues OR errors in production",  "content_types": ["messages", "files"],  "after": 1704067200  // Last 24 hours}
```

Content type flexibility

```
{  "query": "quarterly review OR Q4 planning OR budget discussion OR roadmap",  "content_types": ["messages", "files", "channels"]}
```

Some benefits of the `OR` operator include:

*   **Efficiency**: Single API call instead of multiple separate searches
*   **Comprehensive results**: Captures content using different terminology for the same concept
*   **Flexibility**: Users don't need to know exact keywords or project names
*   **Rate limit optimization**: Reduces the number of API calls needed for broad searches

Keep in mind these best practices when using the `OR` operator:

*   Combine related terms that users might use interchangeably
*   Use `OR` for synonyms, alternative project names, or related concepts
*   Consider combining with time filters to focus on recent discussions
*   Group similar concepts together (e.g., "bugs OR issues OR problems")
*   Use natural language `OR` queries for semantic search when available

### Intelligent conversation discovery example {#full-example}

This example demonstrates a complete workflow where a user asks about a previous conversation, and the system intelligently disambiguates, searches, retrieves full context, and enables follow-up actions.

The following scopes are needed to execute this workflow. For search and discovery:

*   [`search:read.users`](/reference/scopes/search.read.users)
*   [`search:read.public`](/reference/scopes/search.read.public)
*   [`search:read.private`](/reference/scopes/search.read.private)
*   [`search:read.mpim`](/reference/scopes/search.read.mpim)
*   [`search:read.im`](/reference/scopes/search.read.im)

For thread retrieval:

*   [`channels:history`](/reference/scopes/channels.history)
*   [`groups:history`](/reference/scopes/groups.history)
*   [`im:history`](/reference/scopes/im.history)
*   [`mpim:history`](/reference/scopes/mpim.history)

For messaging:

*   [`chat:write`](/reference/scopes/chat.write)

Scenario: A user asks, "Jason and I were talking about reporting yesterday, where did we leave off?"

#### Step 1: User disambiguation {#step-1-user-disambiguation}

First, search for users named "Jason" to help disambiguate which Jason the user means.

**Request**

```
{  "query": "Jason",  "content_types": ["users"],  "limit": 5}
```

**Response**

```
{  "ok": true,  "results": {    "users": [      {        "user_id": "U05KTJUUX5E",        "permalink": "https://platform-demos.slack.com/team/U05KTJUUX5E",        "full_name": "Jason Chen",        "title": "Product Manager",        "timezone": "America/Los_Angeles",        "email": "jason.chen@company.com",        "profile_pic_permalink": "https://avatars.slack-edge.com/2023-07-27/5635409927239_08fedea44d3fe8a8e9ae_original.jpg"      },      {        "user_id": "U789012",        "permalink": "https://platform-demos.slack.com/team/U789012ABC",        "full_name": "Jason Rodriguez",        "title": "Data Analyst",        "timezone": "America/New_York",        "email": "jason.rodriguez@company.com",        "profile_pic_permalink": "https://avatars.slack-edge.com/2024-01-15/6789012345678_12fedea44d3fe8a8e9ae_original.jpg"      }    ]  }}
```

Platform response to user: `"I found multiple people named Jason. Is this the Jason you mean?"`.

*   `Jason Chen (Product Manager, Growth Team)`
*   `Jason Rodriguez (Data Analyst, Analytics Team)`

User selects `"Jason Rodriguez"`.

#### Step 2: Search for relevant conversation {#step-2-search-for-relevant-conversation}

Now search for conversations about reporting involving both the user and Jason Rodriguez from yesterday.

**Request**:

```
{  "query": "reporting discussion with <@U789012> yesterday",  "content_types": ["messages"],  "channel_types": ["public_channel", "private_channel", "mpim", "im"],  "include_context_messages": true,  "after": 1704153600,  // Yesterday timestamp  "before": 1704240000,  // End of yesterday  "limit": 10}
```

**Response**

```
{  "ok": true,  "results": {    "messages": [      {        "author_name": "Jason Rodriguez",        "author_user_id": "U789012",        "team_id": "T0123456",        "channel_id": "C0789012",        "channel_name": "data-analytics",        "message_ts": "1704220800.123456",        "thread_ts": "1704220800.123456",        "content": "Let's dive deeper into the monthly reporting automation. I think we can streamline the process significantly...",        "permalink": "https://company.slack.com/archives/C0789012/p1704220800123456",        "context_messages": {          "before": [            {              "text": "The current manual process is taking too much time each month",              "user_id": "U456789",              "author_name": "Jane Doe"              "ts": "1704220740.012345"            }          ],          "after": [            {              "text": "Absolutely! What specific areas do you think we should focus on first?",              "user_id": "U456789",              "author_name": "Jane Doe"              "ts": "1704220860.234567"            }          ]        }      }    ]  }}
```

#### Step 3: Retrieve full thread context {#step-3-retrieve-full-thread-context}

Use the thread timestamp to get all messages in the conversation thread, calling the [`conversations.replies`](/reference/methods/conversations.replies) method.

**Request**

```
{  "channel": "C0789012",  "ts": "1704220800.123456"}
```

**Response**

```
{  "ok": true,  "messages": [    {      "type": "message",      "user": "U789012",      "text": "Let's dive deeper into the monthly reporting automation. I think we can streamline the process significantly...",      "ts": "1704220800.123456"    },    {      "type": "message",       "user": "U456789", // The requesting user      "text": "Absolutely! What specific areas do you think we should focus on first?",      "ts": "1704220860.234567"    },    {      "type": "message",      "user": "U789012",       "text": "I was thinking we could automate the data collection from our three main sources, then build templates for the executive summary. We should also consider real-time dashboards.",      "ts": "1704220920.345678"    },    {      "type": "message",      "user": "U456789",      "text": "That sounds like a solid plan. Should we set up a follow-up meeting to map out the technical requirements?",      "ts": "1704220980.456789"    },    {      "type": "message",      "user": "U789012",      "text": "Yes, let's do that. I'll prepare a rough timeline and we can discuss resource allocation too.",      "ts": "1704221040.567890"    }  ]}
```

#### Step 4: Provide intelligent summary {#step-4-provide-intelligent-summary}

Platform response to user: `I found your conversation with Jason Rodriguez about reporting automation from yesterday in the #data-analytics channel. Here's where you left off:`

**Conversation summary**:

*   Jason suggested streamlining the monthly reporting process through automation
*   You both agreed to focus on automating data collection from three main sources
*   Plans include building executive summary templates and real-time dashboards
*   You proposed setting up a follow-up meeting to map technical requirements
*   Jason agreed and will prepare a timeline plus discuss resource allocation
*   Next Steps Discussed: Follow-up meeting to plan technical requirements and timeline

#### Step 5: Enable follow-up action {#step-5-enable-follow-up-action}

User responds: `"Great! Can you send a query to that thread to pull the latest Q3 reporting data we discussed?"`

You can send this information by calling the [`chat.postMessage`](/reference/methods/chat.postMessage) method.

**Request**

```
{  "channel": "C0789012",  "thread_ts": "1704220800.123456",  "text": "Here's the Q3 reporting data we discussed earlier:\n\n**Key Metrics:**\n• Revenue: $2.4M (↑15% vs Q2)\n• Customer Acquisition: 1,250 new customers\n• Conversion Rate: 3.2% (↑0.4% vs Q2)\n• Monthly Active Users: 45,000\n\n**Top Performing Channels:**\n1. Organic Search (35% of traffic)\n2. Email Marketing (28% of conversions)\n3. Social Media (22% engagement rate)\n\nThis data supports our automation discussion - we can streamline these reports significantly."}
```

Platform response: `"Report sent! I've posted the Q3 reporting data to the thread in #data-analytics, connecting it back to your automation discussion."`

### Rate limiting {#rate-limiting}

The Real-time Search API has special rate limiting conditions. Refer to the [method documentation](/reference/methods/assistant.search.context#rate-limiting) for details.

* * *

## Use in public channels {#public-channels}

When calling the Real-time Search API from within a public channel, the scope of content searched and shared is more limited. The Real-time Search API will only return results from public channels, regardless of whether or not the user has more granular scopes, such as `search:read.private`, enabled. If the channel is public, then the API will return results from all public channels the user has access to in the workspace that the API was invoked in.

If the Real-time Search API is called from an MPDM or a private channel, it returns results from only the MPDM/private channel and all public channels that exist in that same workspace. This workspace limitation is because users may be in different workspaces, and thus have different public channel data access.

If the Real-time Search API is called from a Slack Connect channel, it will return results from _only_ the channel where it was invoked. This prevents users from seeing data they might otherwise not have access to.

Subscribe to the [`app_mention`](/reference/events/app_mention) event to be notified when it is mentioned in channels. When it is mentioned, the `action_token` will be present in the event payload.

* * *

## Limitations {#limitations}

Formatting in the search string can cause unexpected results, so be sure to strip any formatting from the search string before sending to the Real-time Search API.

The Real-time Search API will provide the most relevant results based on the search query. As such, the following are excluded from the results:

*   Low relevance results
*   Non-text files
*   Google Drive links (if it is not installed)

Only directory-published apps or internal apps may use the Real-time Search API.

* * *

## Data privacy {#privacy}

When performing a search, a third-party app requires various permissions to access data. In order to search public channel content, an app needs to be present within a workspace (and thus approved by an admin). For private channel content and files, both an admin and the end user need to have granted access to private scopes.

For DMs and MPDMs, admin and user permissions are also required, but only for a single workspace, as they’re not tied to any particular workspace. The user can revoke their consent for the granted private/DM/MPDM scopes after initially granting them.

The Real-time Search API relies on which workspace(s) apps are installed on to determine and limit content access. An Admin should not install an app with a `search:read.*` scope to multiple workspaces if they do not want specific data to be accessible to the app. Alternatively, developers have the option to create separate apps for secure workspaces, such as [GovSlack](https://slack.com/solutions/govslack).

Slack does not store any LLM prompts or response data (other than in the feedback payload), and Slack does not train anything on Personally Identifiable Information (PII).

Per Slack policy, zero-data copy and zero-data usage for training LLMs is allowed.

You must not store or copy any of the data retrieved from this API.

You must not store or copy any of the data retrieved from this API. You may not use any of this data for training. You may not use this API to scrape data in a workspace that is unrelated to user queries.

* * *

## Guest access {#guests}

Workspace guests are not permitted to access [apps using platform AI features](/ai/), and therefore, the Real-time Search API.

* * *

## Slack Connect channels {#slack-connect}

The API will retrieve results from Slack Connect channels.

* * *

## General usage guidelines {#guidelines}

*   ✅ DO have an in-Slack experience for your app.
*   ✅ DO ensure the app's long description contains information on which search option is offered (i.e. just keyword search or both keyword search and semantic search). If the app offers semantic search, please include a disclaimer that users must have a Business+ or Enterprise+ Slack plan to use the feature.
*   ✅ DO ensure the formatting of query results are neat.
*   ✅ DO ensure sources and citations in query results are referenced properly (e.g. hyperlinks are included where necessary and extra syntax is not displayed).
*   ✅ DO ensure advanced formatting are displayed properly in query results (e.g. references to channels and mentions in Slack transform into a link to the channel or user).
*   ✅ DO respond with relevant and helpful error messages if something goes wrong. It will be useful if the error messages help guide users in drafting prompts which the app can provide contextually appropriate responses to.
*   🚫 DON'T use Slack data to train LLMs.
*   🚫 DON'T expose messages/files to anyone who would not have access to them in Slack.
*   🚫 DON'T allow your Slack app's authorization to be shared between users of your service.
*   🚫 DON'T perform unexpected actions (e.g. apps should not take any action on behalf of a user in Slack without consent from the user themselves).
*   🚫 DON'T use the legacy `search:read` scope and related `search.messages` and `search.all` endpoints in API requests.

In addition to the above, if the app is requesting the user token `*:history` scopes to support RTS call patterns, the app should not be subscribed to any user-level message event subscriptions (e.g. `message.channels`, `message.groups`, `message.im`, `message.mpim`).