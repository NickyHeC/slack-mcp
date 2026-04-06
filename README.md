# Slack MCP Server

An MCP server for the [Slack Web API](https://docs.slack.dev/apis/web-api/) built with the [Dedalus MCP](https://docs.dedaluslabs.ai/dmcp) framework. Credentials are secured by [DAuth](https://www.dedaluslabs.ai/blog/dedalus-auth-launch) — your server code never sees raw tokens.

## Features

- Comprehensive search across messages, files, users, and channels
- Message sending with thread reply support
- Channel listing, history retrieval, and detailed info
- Canvas creation, editing, and reading for rich document collaboration
- User profile lookup
- Cursor-based pagination on all list endpoints
- Slack's tiered rate limiting handled by DAuth

## Setup

### 1. Create a Slack App

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and create a new app
2. Under **OAuth & Permissions**, add the scopes listed below
3. Install the app to your workspace
4. Copy the **Bot User OAuth Token** (`xoxb-...`) or **User OAuth Token** (`xoxp-...`)

### 2. Required Scopes

| Scope | Needed for |
|-------|-----------|
| `channels:read` | `list_channels`, `search_channels`, `get_channel_info` |
| `channels:history` | `get_channel_history`, `get_thread_replies` |
| `groups:read` | Private channel access |
| `groups:history` | Private channel history |
| `chat:write` | `send_message` |
| `users:read` | `search_users` |
| `users.profile:read` | `get_user_profile` |
| `search:read` | `search_messages`, `search_files` (user token only) |
| `canvases:read` | `get_canvas` |
| `canvases:write` | `create_canvas`, `update_canvas` |

> **Note:** Search tools (`search_messages`, `search_files`) require a **user token** (`xoxp-...`). All other tools work with a bot token.

### 3. Configure Environment

```bash
cp .env.example .env
```

Fill in your token and Dedalus credentials:

```env
DEDALUS_AS_URL=https://as.dedaluslabs.ai
DEDALUS_API_KEY=your-dedalus-api-key
SLACK_TOKEN=xoxb-your-bot-token
```

### 4. Install and Run

```bash
pip install -e .
python -m src.main
```

The server starts on port 8080. Test the connection first:

```bash
python -m src.client --test-connection
```

## Available Tools

### Search

| Tool | Description |
|------|-------------|
| `search_messages` | Search messages across the workspace (user token required) |
| `search_files` | Search files across the workspace (user token required) |
| `search_users` | List/search users by name or display name |
| `search_channels` | List/search channels by name |

### Channels

| Tool | Description |
|------|-------------|
| `list_channels` | List all accessible channels with pagination |
| `get_channel_info` | Get detailed metadata for a specific channel |
| `get_channel_history` | Retrieve message history from a channel |
| `get_thread_replies` | Get all replies in a message thread |

### Messaging

| Tool | Description |
|------|-------------|
| `send_message` | Send a message to a channel or reply in a thread |

### Canvas

| Tool | Description |
|------|-------------|
| `create_canvas` | Create a new canvas with markdown content |
| `update_canvas` | Replace the content of an existing canvas |
| `get_canvas` | Read the sections and content of a canvas |

### Users

| Tool | Description |
|------|-------------|
| `get_user_profile` | Get detailed profile info for a user |

## Project Structure

```
slack-mcp/
├── src/
│   ├── __init__.py
│   ├── main.py        # DAuth connection + server config
│   ├── tools.py       # All 13 Slack tools
│   └── client.py      # Test client
├── pyproject.toml
├── .env.example
└── README.md
```

## References

- [Slack Web API docs](https://docs.slack.dev/apis/web-api/)
- [Slack method reference](https://docs.slack.dev/reference/methods)
- [Dedalus MCP docs](https://docs.dedaluslabs.ai/dmcp)
- [DAuth launch post](https://www.dedaluslabs.ai/blog/dedalus-auth-launch)

## License

MIT
