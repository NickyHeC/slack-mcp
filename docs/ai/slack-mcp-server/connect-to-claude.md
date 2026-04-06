Source: https://docs.slack.dev/ai/slack-mcp-server/connect-to-claude

# Connect to Claude

Use the following instructions to connect the Slack MCP server to Claude Code or Claude Desktop.

## Prerequisites {#prerequisites}

Before setting up connection to the Slack MCP server, ensure you have:

*   Claude Code CLI installed
*   Access to a Slack workspace with the MCP integration approved by your workspace admin

## Connect to Claude Code via plugin {#connect-to-claude-code-via-plugin}

If you're already within a Claude Code session, run the slash command:

```
/plugin install slack
```

Or from the command line, use this command:

```
claude plugin install slack
```

The Slack MCP server will be automatically configured when the plugin loads. You will be prompted to authenticate into your Slack workspace via OAuth.

The Claude plugin uses the following MCP configuration (`.mcp.json`):

```
{  "mcpServers": {    "slack": {      "type": "http",      "url": "https://mcp.slack.com/mcp",      "oauth": {        "clientId": "1601185624273.8899143856786",        "callbackPort": 3118      }    }  }}
```

## Connect to Claude Desktop {#connect-to-claude-desktop}

Use the following instructions to connect the Slack MCP server to Claude Desktop.

**Step 1: Open settings**

Open the sidebar to get to the **Customize** page.

**Step 2: Add connector**

On the **Customize** page, click **Connectors**, then click **+** to add a connector. Find Slack and add it.

**Step 3: Complete flow**

Complete the OAuth flow to connect to your Slack workspace.