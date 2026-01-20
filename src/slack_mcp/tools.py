"""MCP tools for Slack operations."""

from typing import Any
from mcp.types import Tool, TextContent
from slack_mcp.slack_client import SlackClient, SlackMCPError


def get_tools(slack_client: SlackClient) -> list[Tool]:
    """Get list of available MCP tools.

    Args:
        slack_client: Initialized SlackClient instance.

    Returns:
        List of Tool definitions.
    """
    return [
        Tool(
            name="slack_list_channels",
            description="List all channels in the Slack workspace",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="slack_get_channel_info",
            description="Get information about a specific Slack channel",
            inputSchema={
                "type": "object",
                "properties": {
                    "channel_id": {
                        "type": "string",
                        "description": "The channel ID (e.g., C1234567890)",
                    },
                },
                "required": ["channel_id"],
            },
        ),
        Tool(
            name="slack_send_message",
            description="Send a message to a Slack channel",
            inputSchema={
                "type": "object",
                "properties": {
                    "channel": {
                        "type": "string",
                        "description": "Channel ID or name (e.g., C1234567890 or #general)",
                    },
                    "text": {
                        "type": "string",
                        "description": "The message text to send",
                    },
                },
                "required": ["channel", "text"],
            },
        ),
        Tool(
            name="slack_get_messages",
            description="Get recent messages from a Slack channel",
            inputSchema={
                "type": "object",
                "properties": {
                    "channel": {
                        "type": "string",
                        "description": "Channel ID or name",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of messages to retrieve (default: 100)",
                        "default": 100,
                    },
                },
                "required": ["channel"],
            },
        ),
        Tool(
            name="slack_list_users",
            description="List all users in the Slack workspace",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="slack_get_user_info",
            description="Get information about a specific Slack user",
            inputSchema={
                "type": "object",
                "properties": {
                    "user_id": {
                        "type": "string",
                        "description": "The user ID (e.g., U1234567890)",
                    },
                },
                "required": ["user_id"],
            },
        ),
    ]


async def handle_tool_call(tool_name: str, arguments: dict[str, Any], slack_client: SlackClient) -> list[TextContent]:
    """Handle a tool call and return results.

    Args:
        tool_name: Name of the tool to call.
        arguments: Arguments for the tool.
        slack_client: Initialized SlackClient instance.

    Returns:
        List of TextContent with the results.
    """
    import json

    try:
        if tool_name == "slack_list_channels":
            # Use list_channels_all() to get all channels (handles pagination)
            channels = slack_client.list_channels_all()
            result = [
                {
                    "id": ch["id"],
                    "name": ch["name"],
                    "is_private": ch.get("is_private", False),
                    "is_archived": ch.get("is_archived", False),
                }
                for ch in channels
            ]
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif tool_name == "slack_get_channel_info":
            channel_id = arguments["channel_id"]
            channel_info = slack_client.get_channel_info(channel_id)
            if channel_info:
                result = {
                    "id": channel_info["id"],
                    "name": channel_info["name"],
                    "is_private": channel_info.get("is_private", False),
                    "is_archived": channel_info.get("is_archived", False),
                    "created": channel_info.get("created"),
                    "num_members": channel_info.get("num_members"),
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            else:
                return [TextContent(type="text", text=f"Channel {channel_id} not found")]

        elif tool_name == "slack_send_message":
            channel = arguments["channel"]
            text = arguments["text"]
            # Use post_message() instead of send_message()
            response = slack_client.post_message(channel, text)
            result = {
                "ok": response.get("ok", False),
                "channel": response.get("channel"),
                "ts": response.get("ts"),
                "message": response.get("message", {}),
            }
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif tool_name == "slack_get_messages":
            channel = arguments["channel"]
            limit = arguments.get("limit", 100)
            messages = slack_client.get_messages(channel, limit)
            result = [
                {
                    "ts": msg["ts"],
                    "user": msg.get("user"),
                    "text": msg.get("text", ""),
                    "type": msg.get("type"),
                }
                for msg in messages
            ]
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif tool_name == "slack_list_users":
            # Use get_users_all() to get all users (handles pagination)
            users = slack_client.get_users_all()
            result = [
                {
                    "id": user["id"],
                    "name": user["name"],
                    "real_name": user.get("real_name"),
                    "is_bot": user.get("is_bot", False),
                    "deleted": user.get("deleted", False),
                }
                for user in users
            ]
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif tool_name == "slack_get_user_info":
            user_id = arguments["user_id"]
            user_info = slack_client.get_user_info(user_id)
            if user_info:
                result = {
                    "id": user_info["id"],
                    "name": user_info["name"],
                    "real_name": user_info.get("real_name"),
                    "display_name": user_info.get("profile", {}).get("display_name"),
                    "email": user_info.get("profile", {}).get("email"),
                    "is_bot": user_info.get("is_bot", False),
                    "deleted": user_info.get("deleted", False),
                }
                return [TextContent(type="text", text=json.dumps(result, indent=2))]
            else:
                return [TextContent(type="text", text=f"User {user_id} not found")]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {tool_name}")]

    except SlackMCPError as e:
        # Handle Slack-specific errors with user-friendly messages
        return [TextContent(type="text", text=f"Slack error: {str(e)}")]
    except Exception as e:
        # Handle unexpected errors
        return [TextContent(type="text", text=f"Error: {str(e)}")]
