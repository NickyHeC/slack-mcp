"""Smoke tests for Slack MCP tools."""

import pytest
from unittest.mock import Mock, patch
from slack_mcp.slack_client import SlackClient
from slack_mcp.tools import get_tools, handle_tool_call


@pytest.fixture
def mock_slack_client():
    """Create a mock Slack client for testing."""
    # Use from_token() for testing instead of from_env()
    client = SlackClient.from_token(bot_token="xoxb-test-token")
    return client


@pytest.fixture
def mock_web_client():
    """Create a mock WebClient."""
    mock_client = Mock()
    mock_client.auth_test.return_value = {"ok": True}
    mock_client.conversations_list.return_value = {
        "ok": True,
        "channels": [
            {"id": "C123", "name": "general", "is_private": False, "is_archived": False},
        ],
    }
    mock_client.conversations_info.return_value = {
        "ok": True,
        "channel": {
            "id": "C123",
            "name": "general",
            "is_private": False,
            "is_archived": False,
            "created": 1234567890,
            "num_members": 10,
        },
    }
    mock_client.chat_postMessage.return_value = {
        "ok": True,
        "channel": "C123",
        "ts": "1234567890.123456",
        "message": {"text": "Test message"},
    }
    mock_client.conversations_history.return_value = {
        "ok": True,
        "messages": [
            {"ts": "1234567890.123456", "user": "U123", "text": "Hello", "type": "message"},
        ],
    }
    mock_client.users_list.return_value = {
        "ok": True,
        "members": [
            {"id": "U123", "name": "testuser", "real_name": "Test User", "is_bot": False, "deleted": False},
        ],
    }
    mock_client.users_info.return_value = {
        "ok": True,
        "user": {
            "id": "U123",
            "name": "testuser",
            "real_name": "Test User",
            "profile": {"display_name": "Test User", "email": "test@example.com"},
            "is_bot": False,
            "deleted": False,
        },
    }
    return mock_client


@pytest.mark.asyncio
async def test_get_tools(mock_slack_client):
    """Test that tools are properly defined."""
    tools = get_tools(mock_slack_client)
    assert len(tools) > 0
    assert any(tool.name == "slack_list_channels" for tool in tools)
    assert any(tool.name == "slack_send_message" for tool in tools)


@pytest.mark.asyncio
async def test_list_channels_tool(mock_slack_client, mock_web_client):
    """Test slack_list_channels tool."""
    # Patch the _client attribute instead of client
    mock_slack_client._client = mock_web_client
    
    # Mock list_channels_all() to return channels directly
    mock_slack_client.list_channels_all = Mock(return_value=[
        {"id": "C123", "name": "general", "is_private": False, "is_archived": False},
    ])
    
    result = await handle_tool_call("slack_list_channels", {}, mock_slack_client)
    assert len(result) == 1
    assert result[0].type == "text"
    assert "C123" in result[0].text


@pytest.mark.asyncio
async def test_get_channel_info_tool(mock_slack_client, mock_web_client):
    """Test slack_get_channel_info tool."""
    mock_slack_client._client = mock_web_client
    
    result = await handle_tool_call("slack_get_channel_info", {"channel_id": "C123"}, mock_slack_client)
    assert len(result) == 1
    assert result[0].type == "text"
    assert "general" in result[0].text


@pytest.mark.asyncio
async def test_send_message_tool(mock_slack_client, mock_web_client):
    """Test slack_send_message tool."""
    mock_slack_client._client = mock_web_client
    
    # Mock post_message() to return expected format
    mock_slack_client.post_message = Mock(return_value={
        "ok": True,
        "channel": "C123",
        "ts": "1234567890.123456",
        "message": {"text": "Test message"},
    })
    
    result = await handle_tool_call(
        "slack_send_message",
        {"channel": "C123", "text": "Test message"},
        mock_slack_client,
    )
    assert len(result) == 1
    assert result[0].type == "text"
    assert "ok" in result[0].text.lower() or "true" in result[0].text


@pytest.mark.asyncio
async def test_get_messages_tool(mock_slack_client, mock_web_client):
    """Test slack_get_messages tool."""
    mock_slack_client._client = mock_web_client
    
    result = await handle_tool_call("slack_get_messages", {"channel": "C123", "limit": 10}, mock_slack_client)
    assert len(result) == 1
    assert result[0].type == "text"


@pytest.mark.asyncio
async def test_list_users_tool(mock_slack_client, mock_web_client):
    """Test slack_list_users tool."""
    mock_slack_client._client = mock_web_client
    
    # Mock get_users_all() to return users directly
    mock_slack_client.get_users_all = Mock(return_value=[
        {"id": "U123", "name": "testuser", "real_name": "Test User", "is_bot": False, "deleted": False},
    ])
    
    result = await handle_tool_call("slack_list_users", {}, mock_slack_client)
    assert len(result) == 1
    assert result[0].type == "text"
    assert "U123" in result[0].text


@pytest.mark.asyncio
async def test_get_user_info_tool(mock_slack_client, mock_web_client):
    """Test slack_get_user_info tool."""
    mock_slack_client._client = mock_web_client
    
    result = await handle_tool_call("slack_get_user_info", {"user_id": "U123"}, mock_slack_client)
    assert len(result) == 1
    assert result[0].type == "text"
    assert "testuser" in result[0].text


@pytest.mark.asyncio
async def test_unknown_tool(mock_slack_client):
    """Test handling of unknown tool."""
    result = await handle_tool_call("unknown_tool", {}, mock_slack_client)
    assert len(result) == 1
    assert "Unknown tool" in result[0].text
