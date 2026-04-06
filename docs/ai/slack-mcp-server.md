Source: https://docs.slack.dev/ai/slack-mcp-server

# Overview

Model Context Protocol (MCP) is an open standard designed to give AI agents a consistent, secure way to discover and use external data, tools, and services. MCP standardizes how applications provide context to LLMs.

With the Slack MCP server, your integrated apps can search channels, send messages, and perform other Slack actions through MCP clients. Workspace admins can approve and manage all MCP client integrations, keeping your Slack data safe. This guide discusses the overall MCP architecture, offerings from Slack, and how to develop with the Slack MCP server.

## MCP overview {#overview}

There are three components to MCP: the host, client, and server.

*   The **MCP host** is the user-facing application where you interact with the AI. The hosts's job is managing the overall user experience, taking requests, and coordinating the flow of communication.
*   The **MCP client** is the component that handles the actual communication on the host side. You can think of this as a specialized bridge or adapter built into the host application. The host's job is to take the AI's internal request (i.e. "I need to read a file to answer this question") and translate it into a standard MCP request, maintaining a one-to-one connection with an MCP server.
*   The **MCP server** is the gateway to a specific external tool or data source that the AI needs access to. It is a separate program that acts as a secure wrapper around a system like a database, file system, or an external API, like Slack. It's job is to tell the client what it can do ("I can `read_file`, `query_database`, etc."), translate and execute the standardized MCP request from the client, and enforce security by ensuring the AI only accesses what it's allowed to.

There are a few distinctions to make between MCP and APIs.

Feature

APIs

MCP

Optimization

Software-to-software communication; deterministic integrations

AI model-to-data communication and agent interactions

Implementation

Client (developer) must read documentation and write code to invoke specific endpoints and process the output

Client (agent) can ask the server, "What tools can you offer?" at runtime. The server responds with machine-readable tool descriptions that match the token provided. The same input might result in different output across runs.

Output

Machine readable (JSON) and entity IDs

Human readable (markdown) with hydrated names for entities

### Slack MCP server features {#slack-mcp}

The Slack MCP server provides tools for searching through Slack, retrieving and sending messages, managing canvases, and managing users. Each of these tools provides useful functionality for interacting with Slack; combine them for comprehensive integrations that grasp your team's context and history.

#### Searching throughout Slack {#searching}

The MCP server can search for a variety of information found throughout a Slack workspace:

*   Messages and files — filter by date, user, and content type. Retrieve metadata and content.
*   Users in a workspace — filter by name (with partial name matching), email, and user ID. Retrieve user details and statuses.
*   Private and public channels — filter by channel name and description. Retrieve channel metadata.

#### Retrieving and sending messages {#retrieving-sending-messages}

The MCP server can retrieve and send messages throughout a Slack workspace:

*   Send messages — send messages to any type of conversation in Slack.
*   Draft messages — draft, format, and preview messages directly within AI clients.
*   Read channels — grab the complete message history of channels.
*   Read threads — grab complete message thread conversations.

#### Managing canvases {#managing-canvases}

The MCP server can interact and modify Slack canvases:

*   Create/update a canvas — create and share rich, formatted documents.
*   Read a canvas — export canvases as markdown files.

#### Managing users {#managing-users}

The MCP server can also fetch user info. It can access complete user profile info, including custom profile fields and statuses.

#### Example use cases {#use-cases}

There are many possibilities with the Slack MCP server. Here are just a few ideas:

*   Create an AI assistant in Slack that can search through your team's Slack history to answer questions, find past decisions, and provide context for current projects.
*   Bring content from outside Slack into Slack via messages and canvases for discussion with coworkers.
*   Bring content from Slack to AI agents, providing them full context of projects that exist across multiple products.

### Rate limits {#rate-limits}

Like all Slack Web API methods, the Slack MCP server is subject to rate limits. Limits are enforced per tool or action type. Whether an action is performed via an MCP tool or directly through Slack Web API methods, the same rate limits apply. Here is the full list of MCP tools and their associated rate limit:

MCP Tool

Rate Limit

Search messages & files

Special rate limits apply; consult [method page documentation](/reference/methods/assistant.search.context/#rate-limiting)

Search users

[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

Search channels

[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

Send message

Special rate limits apply; consult [method page documentation](/reference/methods/chat.postMessage/#rate_limiting)

Read a channel

[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

Read a thread

[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

Create a canvas

[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

Update a canvas

[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

Read a canvas

[Tier 3: 50+ per minute](/apis/web-api/rate-limits) / [Tier 4: 100+ per minute](/apis/web-api/rate-limits)

Read a user profile

[Tier 4: 100+ per minute](/apis/web-api/rate-limits)

* * *

## Transport protocol and endpoint {#transport-protocol}

Slack supports JSON-RPC 2.0 over Streamable HTTP. All requests should be sent to:

```
https://mcp.slack.com/mcp
```

We do not support SSE-based connections or Dynamic Client Registration at this time.

* * *

## App Identity {#app-identity}

MCP clients must be backed by a registered Slack app with a fixed app ID and hardcode that app ID. This allows Slack to:

*   Let admins manage and approve your app/MCP client app using standard Slack app approval process.
*   Associate requests with your app for logging, rate limits, and access control.
*   Provide better support and visibility into usage.

If you're already using a Slack app for your integration, you can reuse it for MCP access.

Only directory-published apps or internal apps may use MCP.

* * *

## Security concerns {#security}

When using the Slack MCP server, please be mindful about connecting to or utilizing other MCP servers at the same time. Different servers may have their own security, stability, and usage characteristics, so think carefully before mixing them together. Use judgment when evaluating what to connect and share across environments. Using these clients means giving them access to your Slack data so you can use it as context while interacting with those apps.

Audit MCP activity with the associated [audit logs](/reference/audit-logs-api/methods-actions-reference/#mcp-server).

Only apps published in the Slack Marketplace and internal apps can use MCP at this time; unlisted apps are prohibited from using MCP.

* * *

## Authentication and Token Handling {#authentication}

Slack supports confidential OAuth for MCP clients. You'll need to use your app's `client_id` and `client_secret` for Slack OAuth.

If your MCP client supports OAuth 2.0 Authorization Server Metadata (RFC 8414) per MCP spec, you can rely on that. Users go through OAuth consent and authorize the app. You can initiate this OAuth request from your UX following standard MCP metadata discovery files:

*   `https://mcp.slack.com/.well-known/oauth-protected-resource`
*   `https://mcp.slack.com/.well-known/oauth-authorization-server`

### OAuth URL and endpoints {#oauth-endpoints}

*   Authorization endpoint for Slack user tokens: `https://slack.com/oauth/v2_user/authorize`
*   Token endpoint for Slack user tokens: `https://slack.com/api/oauth.v2.user.access` (method docs [here](/reference/methods/oauth.v2.user.access))
*   If you also want to generate bot tokens (for in-Slack experience), follow instructions [here](/authentication/).

### OAuth scopes needed on user token for different tools {#oauth-scopes}

*   Search messages/channels: [`search:read.public`](/reference/scopes/search.read.public), [`search:read.private`](/reference/scopes/search.read.private), [`search:read.mpim`](/reference/scopes/search.read.mpim), [`search:read.im`](/reference/scopes/search.read.im)
*   Search files: [`search:read.files`](/reference/scopes/search.read.files)
*   Search users: [`search:read.users`](/reference/scopes/search.read.users)
*   Send message: [`chat:write`](/reference/scopes/chat.write)
*   Read a channel/thread: [`channels:history`](/reference/scopes/channels.history), [`groups:history`](/reference/scopes/groups.history), [`mpim:history`](/reference/scopes/mpim.history), [`im:history`](/reference/scopes/im.history)
*   Canvas create/update: [`canvases:read`](/reference/scopes/canvases.read), [`canvases:write`](/reference/scopes/canvases.write)
*   User profile/email: [`users:read`](/reference/scopes/users.read), [`users:read.email`](/reference/scopes/users.read.email)

Consider using PKCE

Looking to use desktop clients? PKCE support is now available! Read more [here](/authentication/using-pkce).

* * *

## Available clients {#partner-clients}

Another method of using the Slack MCP server (if building a Slack app is not your jam) is accessing it via a partner application. The Slack MCP server is available in these select partner-built clients, no coding needed:

*   [Claude.ai](https://claude.ai)
*   [Claude Code](https://code.claude.com)
*   [Perplexity](https://perplexity.ai)
*   [Cursor](https://cursor.com)

* * *

## Related content {#related}

✨ Check out our documentation on Developing agents [here](/ai/developing-agents).

✨ To search Slack data without connecting it to an AI, see documentation for the Real Time Search API [here](/apis/web-api/real-time-search-api). The Real Time Search (RTS) API offers access to Slack data via API call.