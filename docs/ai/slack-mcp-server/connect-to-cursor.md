Source: https://docs.slack.dev/ai/slack-mcp-server/connect-to-cursor

# Connect to Cursor

Use the Add to Cursor button below or follow the instructions to connect the Slack MCP server to Cursor.

## Prerequisites {#prerequisites}

Before setting up connection to the Slack MCP server, ensure you have:

*   Cursor IDE installed
*   Access to a Slack workspace with the MCP integration approved by your workspace admin

## Add by button {#add-by-button}

Click the button and follow the flow.

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=slack&config=eyJ1cmwiOiJodHRwczovL21jcC5zbGFjay5jb20vbWNwIiwiYXV0aCI6eyJDTElFTlRfSUQiOiIzNjYwNzUzMTkyNjI2Ljg5MDM0NjkyMjg5ODIifX0%3D)

## Add to Cursor settings {#add-to-cursor-settings}

If you've gone through the flow of the Add to Cursor button above, you do not need to follow these steps.

**Step 1: Open Cursor Settings**

Navigate to **Cursor → Settings → Cursor Settings** (or use the keyboard shortcut `Cmd+,` on macOS, `Ctrl+,` on Windows/Linux).

**Step 2: Navigate to the MCP tab**

In the Settings interface, click on the **MCP** tab to access MCP server configurations.

**Step 3: Add Slack MCP configuration**

Add the following configuration to connect to the remote Slack MCP server:

```
{  "mcpServers": {    "slack": {      "url": "https://mcp.slack.com/mcp",      "auth": {        "CLIENT_ID": "3660753192626.8903469228982"      }    }  }}
```

Save the configuration. You will also see a connect button once added. Click that to authenticate into your Slack Workspace.