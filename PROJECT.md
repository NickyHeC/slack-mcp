# PROJECT.md — Platform Research Notes

> This file is a working notepad for the developer (or AI coding agent) building
> this MCP server. Fill in each section as you research the target platform.
> The information here drives the implementation in `src/main.py` and `src/tools.py`.
>
> **Do not commit secrets.** Store credentials in `.env` (which is gitignored).

---

## Platform Overview

**Platform name:** Slack Web API
**Official docs:** https://docs.slack.dev/apis/web-api/
**Base URL:** `https://slack.com/api`

Brief description of what this platform does and why we are building an MCP server for it:

Slack is a business communication platform that organizes conversations in channels, direct messages, and threads. The Web API provides over 200 HTTP methods for reading, writing, and interacting with Slack workspaces. This MCP server enables AI agents to search through Slack data, send messages, manage channels, create canvases, and interact with users - allowing AI to access team context, conversations, and collaborate within the flow of work.

---

## Authentication

**Auth type:** Bearer Token (Bot Token or User Token)
**How to obtain credentials:** https://api.slack.com/apps (create app, install to workspace, obtain tokens via OAuth)

### Credential details

- **Token / key name:** `SLACK_BOT_TOKEN` or `SLACK_USER_TOKEN`
- **Header format:** `Bearer {token}` (e.g. `Bearer xoxb-1234-5678-90123`)
- **Scopes required:** 
  - For search: `search:read.public`, `search:read.private`, `search:read.mpim`, `search:read.im`, `search:read.files`, `search:read.users`
  - For messaging: `chat:write`, `chat:write.public`
  - For channel access: `channels:history`, `groups:history`, `mpim:history`, `im:history`, `channels:read`, `groups:read`
  - For canvas management: `canvases:read`, `canvases:write`
  - For user info: `users:read`, `users:read.email`

### OAuth-specific (skip if using API Key)

- **Authorize URL:** `https://slack.com/oauth/v2/authorize`
- **Token URL:** `https://slack.com/api/oauth.v2.access`
- **Client ID:** (store in `.env` as `SLACK_CLIENT_ID`)
- **Client Secret:** (store in `.env` as `SLACK_CLIENT_SECRET`)
- **Available scopes:** See https://docs.slack.dev/reference/scopes

### Example authenticated request

```bash
curl -X GET \
  -H 'Authorization: Bearer xoxb-1234-5678-90123' \
  'https://slack.com/api/conversations.list?limit=50'
```

---

## Endpoints / Features to Implement

List the API endpoints or features you plan to expose as MCP tools.
For each, note the HTTP method, path, key parameters, and response shape.

| Tool name | Method | Path | Description |
|-----------|--------|------|-------------|
| search_messages | GET | `/search.messages` | Search for messages across workspace with query, sort, count parameters |
| search_files | GET | `/search.files` | Search for files with query, sort, count parameters |
| search_users | GET | `/users.list` | List/search users with limit, cursor pagination |
| search_channels | GET | `/conversations.list` | List/search channels with types, exclude_archived, limit parameters |
| send_message | POST | `/chat.postMessage` | Send message to channel with text, channel, blocks, attachments |
| get_channel_history | GET | `/conversations.history` | Get message history from channel with channel, limit, oldest, latest |
| get_thread_replies | GET | `/conversations.replies` | Get replies in a thread with channel, ts, limit parameters |
| create_canvas | POST | `/canvases.create` | Create new canvas with title, document_content |
| update_canvas | POST | `/canvases.edit` | Update existing canvas with canvas_id, changes |
| get_canvas | GET | `/canvases.sections.lookup` | Read canvas content by canvas_id |
| get_user_profile | GET | `/users.profile.get` | Get user profile info with user parameter |
| list_channels | GET | `/conversations.list` | List all channels user has access to |
| get_channel_info | GET | `/conversations.info` | Get detailed info about specific channel |

---

## Rate Limits and Restrictions

- **Rate limit:** Tiered limits - Tier 1: 1+/min, Tier 2: 20+/min, Tier 3: 50+/min, Tier 4: 100+/min. Special limits for posting (1/sec per channel) and search methods.
- **Retry strategy:** HTTP 429 responses include `Retry-After` header with seconds to wait. Implement exponential backoff respecting this header.
- **Other restrictions:** Burst limiting for concurrent requests. Enhanced rate limits available when using cursor-based pagination. Message posting has workspace-wide limits beyond per-channel limits.

---

## Response Format Notes

Describe the general shape of API responses — JSON structure, pagination style,
error format, etc. Paste a representative example if helpful.

All responses contain a top-level `ok` boolean indicating success/failure. Failed responses include an `error` property with machine-readable error code. Successful responses may include a `warning` property. Many collection methods use cursor-based pagination with `response_metadata.next_cursor` for retrieving additional results.

```json
{
    "ok": true,
    "messages": [
        {
            "type": "message",
            "user": "U1234567890",
            "text": "Hello world",
            "ts": "1512085950.000216",
            "channel": "C1234567890"
        }
    ],
    "response_metadata": {
        "next_cursor": "bmV4dF90czoxNTEyMDg1ODYxMDAwNTQz"
    }
}
```

---

## Token / Credential Notes

Notes on token lifecycle, expiry, rotation, or platform-specific quirks:

- OAuth tokens do not expire by default
- Bot tokens begin with `xoxb-`, user tokens with `xoxp-`, app-level tokens with `xapp-`
- Tokens can be revoked via `auth.revoke` method or when user/workspace admin removes app
- Token permissions are additive - new OAuth flows add scopes to existing tokens
- Responses include `x-oauth-scopes` header showing current token scopes
- Store tokens securely and restrict API access by IP allowlisting when possible

---

## Additional References

- Web API overview: https://docs.slack.dev/apis/web-api/
- Method reference: https://docs.slack.dev/reference/methods
- Conversation API guide: https://docs.slack.dev/apis/web-api/using-the-conversations-api
- Pagination documentation: https://docs.slack.dev/apis/pagination
- Rate limits details: https://docs.slack.dev/apis/rate-limits
- Authentication guide: https://docs.slack.dev/authentication
- Request verification: https://docs.slack.dev/authentication/verifying-requests-from-slack

---

## Notes for README

Bullet points to include in the project README when it is written:

- Supports both bot tokens and user tokens for different permission levels
- Implements comprehensive search across messages, files, users, and channels  
- Provides message sending and channel history retrieval
- Includes canvas creation and management for rich document collaboration
- Handles Slack's tiered rate limiting and cursor-based pagination automatically
- Requires OAuth app setup with appropriate scopes for intended functionality
- Follows Slack's security best practices for token handling and request verification