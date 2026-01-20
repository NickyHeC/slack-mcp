"""MCP server implementation for Slack."""

import asyncio
from dotenv import load_dotenv
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Resource, TextContent, Tool
from slack_mcp.slack_client import SlackClient, SlackMCPError
from slack_mcp.tools import get_tools, handle_tool_call

# Load environment variables
load_dotenv()

# Initialize Slack client from environment variables
try:
    slack_client = SlackClient.from_env()
except SlackMCPError as e:
    # If initialization fails, we'll handle it when tools are called
    # This allows the server to start even if token is missing (for testing)
    slack_client = None

# Create MCP server
app = Server("slack-mcp-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    if slack_client is None:
        return []  # Return empty list if client not initialized
    return get_tools(slack_client)


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if slack_client is None:
        return [
            TextContent(
                type="text",
                text="Error: Slack client not initialized. Check SLACK_BOT_TOKEN environment variable.",
            )
        ]
    return await handle_tool_call(name, arguments, slack_client)


@app.list_resources()
async def list_resources() -> list[Resource]:
    """List available resources."""
    # Resources can be added here if needed
    return []


async def main():
    """Main entry point for the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options(),
        )


if __name__ == "__main__":
    asyncio.run(main())
