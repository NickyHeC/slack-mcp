# Slack MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that provides Slack integration capabilities. This server enables AI assistants and other MCP clients to interact with Slack workspaces through a standardized interface.

## Features

- **Channel Management**: List channels, get channel information
- **Messaging**: Send messages to Slack channels
- **Message Retrieval**: Get recent messages from channels
- **User Management**: List users and get user information
- **Security**: Optional channel allowlist to restrict where messages can be posted
- **Error Handling**: User-friendly error messages for MCP clients
- **Pagination Support**: Automatic handling of paginated API responses

## Installation

### Prerequisites

- Python 3.10 or higher
- A Slack bot token (see [Configuration](#configuration) below)

### Install from Source

```bash
# Clone the repository
git clone https://github.com/NickyHeC/slack-mcp.git
cd slack-mcp

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install "mcp[cli]" slack_sdk python-dotenv anyio
```

### Install as Package

```bash
pip install -e .
```

## Configuration

### Environment Variables

Create a `.env` file in the project root or set the following environment variables:

#### Required

- `SLACK_BOT_TOKEN`: Your Slack bot token (starts with `xoxb-`)
  - Get this from [api.slack.com/apps](https://api.slack.com/apps)
  - Create a new app or use an existing one
  - Go to "OAuth & Permissions" and install the app to your workspace
  - Copy the "Bot User OAuth Token"

#### Optional

- `SLACK_ALLOWED_CHANNELS`: Comma-separated list of channel IDs or names where the bot is allowed to post
  - Example: `C1234567890,#general,#announcements`
  - If not set, the bot can post to any channel it has access to
  - **Security Note**: Setting this restricts where messages can be sent, preventing accidental posts to unauthorized channels

### Example `.env` file

```env
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_ALLOWED_CHANNELS=C1234567890,#general
```

## Usage

### Running the Server

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the server
python -m slack_mcp.server
```

The server communicates via stdio (standard input/output) as per the MCP protocol specification.

### MCP Client Configuration

Configure your MCP client (e.g., Claude Desktop, Cursor) to use this server:

```json
{
  "mcpServers": {
    "slack": {
      "command": "python",
      "args": ["-m", "slack_mcp.server"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-your-token-here",
        "SLACK_ALLOWED_CHANNELS": "C1234567890,#general"
      }
    }
  }
}
```

## Available Tools

The server provides the following MCP tools:

### `slack_list_channels`

List all channels in the Slack workspace.

**Parameters**: None

**Returns**: Array of channel objects with:
- `id`: Channel ID
- `name`: Channel name
- `is_private`: Whether the channel is private
- `is_archived`: Whether the channel is archived

### `slack_get_channel_info`

Get detailed information about a specific channel.

**Parameters**:
- `channel_id` (required): The channel ID (e.g., `C1234567890`)

**Returns**: Channel object with:
- `id`: Channel ID
- `name`: Channel name
- `is_private`: Whether the channel is private
- `is_archived`: Whether the channel is archived
- `created`: Unix timestamp of creation
- `num_members`: Number of members

### `slack_send_message`

Send a message to a Slack channel.

**Parameters**:
- `channel` (required): Channel ID or name (e.g., `C1234567890` or `#general`)
- `text` (required): The message text to send

**Returns**: Message response with:
- `ok`: Success status
- `channel`: Channel ID where message was sent
- `ts`: Message timestamp
- `message`: Message object

**Note**: If `SLACK_ALLOWED_CHANNELS` is set, posting to channels not in the allowlist will fail.

### `slack_get_messages`

Get recent messages from a Slack channel.

**Parameters**:
- `channel` (required): Channel ID or name
- `limit` (optional): Maximum number of messages to retrieve (default: 100, max: 1000)

**Returns**: Array of message objects with:
- `ts`: Message timestamp
- `user`: User ID who sent the message
- `text`: Message text
- `type`: Message type

### `slack_list_users`

List all users in the Slack workspace.

**Parameters**: None

**Returns**: Array of user objects with:
- `id`: User ID
- `name`: Username
- `real_name`: Real name
- `is_bot`: Whether the user is a bot
- `deleted`: Whether the user is deactivated

### `slack_get_user_info`

Get detailed information about a specific user.

**Parameters**:
- `user_id` (required): The user ID (e.g., `U1234567890`)

**Returns**: User object with:
- `id`: User ID
- `name`: Username
- `real_name`: Real name
- `display_name`: Display name
- `email`: Email address (if available)
- `is_bot`: Whether the user is a bot
- `deleted`: Whether the user is deactivated

## Required Slack Bot Scopes

Your Slack bot needs the following OAuth scopes:

### Required Scopes

- `channels:read` - Read public channel information
- `channels:history` - Read messages in public channels
- `chat:write` - Send messages
- `users:read` - Read user information

### Optional Scopes (for private channels)

- `groups:read` - Read private channel information
- `groups:history` - Read messages in private channels

### Optional Scopes (for search)

- `search:read` - Search messages (if using search functionality)

## Security Features

### Channel Allowlist

The `SLACK_ALLOWED_CHANNELS` environment variable provides an additional security layer:

- When set, the bot can only post messages to channels listed in the allowlist
- Prevents accidental or unauthorized posting to channels
- Format: Comma-separated channel IDs or names (e.g., `C1234567890,#general`)
- If not set, the bot can post to any channel it has access to (based on Slack permissions)

### Error Handling

- All errors are converted to user-friendly `SlackMCPError` exceptions
- Error messages are safe to display to MCP clients
- No sensitive information is exposed in error messages

## Development

### Project Structure

```
slack-mcp/
├── src/
│   └── slack_mcp/
│       ├── __init__.py
│       ├── server.py          # MCP server implementation
│       ├── slack_client.py    # Slack API client wrapper
│       └── tools.py            # MCP tool definitions
├── tests/
│   └── test_tools_smoke.py    # Smoke tests
├── pyproject.toml
└── README.md
```

### Running Tests

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Code Formatting

```bash
# Format code with black
black src/ tests/

# Lint with ruff
ruff check src/ tests/
```

## Troubleshooting

### Server won't start

- **Check token**: Ensure `SLACK_BOT_TOKEN` is set correctly
- **Check token format**: Bot tokens start with `xoxb-`
- **Check permissions**: Verify the bot has the required OAuth scopes

### "Channel not in SLACK_ALLOWED_CHANNELS" error

- Add the channel ID or name to `SLACK_ALLOWED_CHANNELS` environment variable
- Or remove `SLACK_ALLOWED_CHANNELS` to allow posting to all channels (if desired)

### "Slack API error" messages

- Check that the bot is installed in your workspace
- Verify the bot has the required scopes
- Ensure the bot is a member of channels you're trying to access (for private channels)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Links

- [Model Context Protocol](https://modelcontextprotocol.io)
- [Slack API Documentation](https://api.slack.com)
- [GitHub Repository](https://github.com/NickyHeC/slack-mcp)
