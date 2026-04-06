"""Slack API tools.

Tools make authenticated requests to the Slack Web API using ctx.dispatch().
DAuth applies the credential inside the enclave — tool code never handles
raw secrets.

Supports both bot tokens (xoxb-) and user tokens (xoxp-). Search methods
(search_messages, search_files) require a user token.
"""

from typing import Any
from urllib.parse import urlencode

from dedalus_mcp import tool, get_context, HttpMethod, HttpRequest
from pydantic import BaseModel

from src.main import slack_connection


# --- Result Models ---


class SlackResult(BaseModel):
    success: bool
    data: Any = None
    next_cursor: str | None = None
    error: str | None = None


# --- Request Helpers ---


async def slack_get(path: str, params: dict | None = None) -> dict:
    """Dispatch an authenticated GET request to the Slack API through DAuth."""
    ctx = get_context()
    if params:
        filtered = {k: v for k, v in params.items() if v is not None}
        if filtered:
            path = f"{path}?{urlencode(filtered)}"
    req = HttpRequest(method=HttpMethod.GET, path=path)
    resp = await ctx.dispatch(slack_connection, req)
    if resp.success and resp.response is not None:
        body = resp.response.body
        if isinstance(body, dict) and not body.get("ok", True):
            return {"success": False, "error": body.get("error", "Slack API error")}
        return _extract_result(body)
    error = resp.error.message if resp.error else "Request failed"
    return {"success": False, "error": error}


async def slack_post(path: str, body: dict | None = None) -> dict:
    """Dispatch an authenticated POST request to the Slack API through DAuth."""
    ctx = get_context()
    req = HttpRequest(method=HttpMethod.POST, path=path, body=body)
    resp = await ctx.dispatch(slack_connection, req)
    if resp.success and resp.response is not None:
        resp_body = resp.response.body
        if isinstance(resp_body, dict) and not resp_body.get("ok", True):
            return {"success": False, "error": resp_body.get("error", "Slack API error")}
        return _extract_result(resp_body)
    error = resp.error.message if resp.error else "Request failed"
    return {"success": False, "error": error}


def _extract_result(body: Any) -> dict:
    """Normalize a Slack API response body into a consistent result dict."""
    if not isinstance(body, dict):
        return {"success": True, "data": body}
    cursor = None
    meta = body.get("response_metadata")
    if isinstance(meta, dict):
        c = meta.get("next_cursor", "")
        if c:
            cursor = c
    result: dict[str, Any] = {"success": True, "data": body}
    if cursor:
        result["next_cursor"] = cursor
    return result


# --- Search Tools ---


@tool(description="Search for messages across the Slack workspace. Requires a user token (xoxp-).")
async def search_messages(
    query: str,
    sort: str = "timestamp",
    sort_dir: str = "desc",
    count: int = 20,
) -> SlackResult:
    """Search messages matching a query string.

    Args:
        query: The search query (supports Slack search modifiers like from:, in:, has:).
        sort: Sort results by 'score' or 'timestamp'.
        sort_dir: Sort direction — 'asc' or 'desc'.
        count: Number of results to return (max 100).

    """
    params = {"query": query, "sort": sort, "sort_dir": sort_dir, "count": min(count, 100)}
    result = await slack_get("/search.messages", params)
    return SlackResult(**result)


@tool(description="Search for files across the Slack workspace. Requires a user token (xoxp-).")
async def search_files(
    query: str,
    sort: str = "timestamp",
    sort_dir: str = "desc",
    count: int = 20,
) -> SlackResult:
    """Search files matching a query string.

    Args:
        query: The search query.
        sort: Sort results by 'score' or 'timestamp'.
        sort_dir: Sort direction — 'asc' or 'desc'.
        count: Number of results to return (max 100).

    """
    params = {"query": query, "sort": sort, "sort_dir": sort_dir, "count": min(count, 100)}
    result = await slack_get("/search.files", params)
    return SlackResult(**result)


# --- User Tools ---


@tool(description="List and optionally search users in the Slack workspace")
async def search_users(
    query: str | None = None,
    limit: int = 100,
    cursor: str | None = None,
) -> SlackResult:
    """List workspace users, optionally filtering by name or display name.

    Args:
        query: Optional text to filter users by name, real_name, or display_name.
        limit: Maximum number of users to return per page (max 200).
        cursor: Pagination cursor from a previous response.

    """
    params: dict[str, Any] = {"limit": min(limit, 200)}
    if cursor:
        params["cursor"] = cursor
    result = await slack_get("/users.list", params)
    if result.get("success") and query and isinstance(result.get("data"), dict):
        members = result["data"].get("members", [])
        q = query.lower()
        result["data"]["members"] = [
            m for m in members
            if q in m.get("name", "").lower()
            or q in m.get("real_name", "").lower()
            or q in m.get("profile", {}).get("display_name", "").lower()
        ]
    return SlackResult(**result)


@tool(description="Get a user's profile information")
async def get_user_profile(user: str) -> SlackResult:
    """Fetch detailed profile information for a specific user.

    Args:
        user: The user ID (e.g. U1234567890).

    """
    result = await slack_get("/users.profile.get", {"user": user})
    return SlackResult(**result)


# --- Channel Tools ---


@tool(description="Search and filter channels in the Slack workspace")
async def search_channels(
    query: str | None = None,
    types: str = "public_channel,private_channel",
    exclude_archived: bool = True,
    limit: int = 100,
    cursor: str | None = None,
) -> SlackResult:
    """List channels, optionally filtering by name.

    Args:
        query: Optional text to filter channels by name.
        types: Comma-separated channel types — public_channel, private_channel, mpim, im.
        exclude_archived: Whether to exclude archived channels.
        limit: Maximum number of channels per page (max 1000).
        cursor: Pagination cursor from a previous response.

    """
    params: dict[str, Any] = {
        "types": types,
        "exclude_archived": str(exclude_archived).lower(),
        "limit": min(limit, 1000),
    }
    if cursor:
        params["cursor"] = cursor
    result = await slack_get("/conversations.list", params)
    if result.get("success") and query and isinstance(result.get("data"), dict):
        channels = result["data"].get("channels", [])
        q = query.lower()
        result["data"]["channels"] = [
            c for c in channels if q in c.get("name", "").lower()
        ]
    return SlackResult(**result)


@tool(description="List all channels the authenticated user has access to")
async def list_channels(
    types: str = "public_channel,private_channel",
    exclude_archived: bool = True,
    limit: int = 200,
    cursor: str | None = None,
) -> SlackResult:
    """List all accessible channels with pagination support.

    Args:
        types: Comma-separated channel types — public_channel, private_channel, mpim, im.
        exclude_archived: Whether to exclude archived channels.
        limit: Maximum number of channels per page (max 1000).
        cursor: Pagination cursor from a previous response.

    """
    params: dict[str, Any] = {
        "types": types,
        "exclude_archived": str(exclude_archived).lower(),
        "limit": min(limit, 1000),
    }
    if cursor:
        params["cursor"] = cursor
    result = await slack_get("/conversations.list", params)
    return SlackResult(**result)


@tool(description="Get detailed information about a specific Slack channel")
async def get_channel_info(channel: str) -> SlackResult:
    """Fetch detailed metadata for a channel.

    Args:
        channel: The channel ID (e.g. C1234567890).

    """
    result = await slack_get("/conversations.info", {"channel": channel})
    return SlackResult(**result)


# --- Message Tools ---


@tool(description="Send a message to a Slack channel or thread")
async def send_message(
    channel: str,
    text: str,
    thread_ts: str | None = None,
) -> SlackResult:
    """Post a message to a channel. Optionally reply in a thread.

    Args:
        channel: Channel ID (e.g. C1234567890) or name (e.g. #general).
        text: The message text (supports Slack mrkdwn formatting).
        thread_ts: Optional thread timestamp to reply in a thread.

    """
    body: dict[str, Any] = {"channel": channel, "text": text}
    if thread_ts:
        body["thread_ts"] = thread_ts
    result = await slack_post("/chat.postMessage", body)
    return SlackResult(**result)


@tool(description="Get message history from a Slack channel")
async def get_channel_history(
    channel: str,
    limit: int = 50,
    oldest: str | None = None,
    latest: str | None = None,
    cursor: str | None = None,
) -> SlackResult:
    """Retrieve recent messages from a channel.

    Args:
        channel: The channel ID (e.g. C1234567890).
        limit: Number of messages to return (max 1000).
        oldest: Unix timestamp — only messages after this time.
        latest: Unix timestamp — only messages before this time.
        cursor: Pagination cursor from a previous response.

    """
    params: dict[str, Any] = {"channel": channel, "limit": min(limit, 1000)}
    if oldest:
        params["oldest"] = oldest
    if latest:
        params["latest"] = latest
    if cursor:
        params["cursor"] = cursor
    result = await slack_get("/conversations.history", params)
    return SlackResult(**result)


@tool(description="Get replies in a message thread")
async def get_thread_replies(
    channel: str,
    ts: str,
    limit: int = 50,
    cursor: str | None = None,
) -> SlackResult:
    """Retrieve all replies in a conversation thread.

    Args:
        channel: The channel ID containing the thread.
        ts: The timestamp of the parent message.
        limit: Number of replies to return (max 1000).
        cursor: Pagination cursor from a previous response.

    """
    params: dict[str, Any] = {"channel": channel, "ts": ts, "limit": min(limit, 1000)}
    if cursor:
        params["cursor"] = cursor
    result = await slack_get("/conversations.replies", params)
    return SlackResult(**result)


# --- Canvas Tools ---


@tool(description="Create a new Slack canvas document")
async def create_canvas(
    title: str,
    markdown: str,
) -> SlackResult:
    """Create a canvas with markdown content.

    Args:
        title: The title of the canvas.
        markdown: The canvas content in markdown format.

    """
    body = {
        "title": title,
        "document_content": {"type": "markdown", "markdown": markdown},
    }
    result = await slack_post("/canvases.create", body)
    return SlackResult(**result)


@tool(description="Update an existing Slack canvas document")
async def update_canvas(
    canvas_id: str,
    markdown: str,
) -> SlackResult:
    """Replace the content of an existing canvas.

    Args:
        canvas_id: The ID of the canvas to update (e.g. F1234567890).
        markdown: The new canvas content in markdown format.

    """
    body = {
        "canvas_id": canvas_id,
        "changes": [
            {
                "operation": "replace",
                "document_content": {"type": "markdown", "markdown": markdown},
            }
        ],
    }
    result = await slack_post("/canvases.edit", body)
    return SlackResult(**result)


@tool(description="Read the content of a Slack canvas")
async def get_canvas(canvas_id: str) -> SlackResult:
    """Retrieve the sections and content of a canvas.

    Args:
        canvas_id: The ID of the canvas to read (e.g. F1234567890).

    """
    body = {"canvas_id": canvas_id, "criteria": {}}
    result = await slack_post("/canvases.sections.lookup", body)
    return SlackResult(**result)


# --- Tool Registry ---

tools = [
    search_messages,
    search_files,
    search_users,
    get_user_profile,
    search_channels,
    list_channels,
    get_channel_info,
    send_message,
    get_channel_history,
    get_thread_replies,
    create_canvas,
    update_canvas,
    get_canvas,
]
