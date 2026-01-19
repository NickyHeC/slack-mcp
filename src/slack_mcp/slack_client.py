"""
Slack client wrapper for an MCP server.

Merges:
- MCP-friendly, user-displayable errors (SlackMCPError)
- Env-based config (SLACK_BOT_TOKEN, optional SLACK_ALLOWED_CHANNELS)
- Single reused WebClient instance
- Safer posting via allowlist enforcement
- Thread + search support
- Optional pagination helpers
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any, Optional

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class SlackMCPError(RuntimeError):
    """Slack-related failures that are safe to show to the MCP client."""


def _parse_allowed_channels(raw: str) -> set[str] | None:
    # Split by comma, strip whitespace, filter empty strings, convert to set
    # Empty set becomes None to distinguish "no channels" from "all channels allowed"
    allowed = {c.strip() for c in (raw or "").split(",") if c.strip()}
    return allowed or None


@dataclass(slots=True)
class SlackClient:
    """Wrapper around Slack WebClient for MCP server operations."""

    token: str  # Bot token (xoxb-...) required for all API operations
    allowed_channels: set[str] | None = None  # Optional allowlist for posting safety
    _client: WebClient = field(init=False, repr=False)  # Lazy-initialized API client

    def __post_init__(self) -> None:
        """Initialize WebClient after dataclass instantiation."""
        # Critical: Token validation must happen before WebClient creation
        # Empty tokens will cause authentication failures on all API calls
        if not self.token:
            raise SlackMCPError("Missing SLACK_BOT_TOKEN. Put it in your .env.")
        
        # Create WebClient instance - this is the main interface to Slack API
        # WebClient handles HTTP requests, rate limiting, retries, and response parsing
        self._client = WebClient(token=self.token)

    @classmethod
    def from_env(cls) -> "SlackClient":
        """Factory method to create client from environment variables."""
        # Read bot token from environment - required for all operations
        # strip() removes leading/trailing whitespace that could cause auth failures
        token = os.getenv("SLACK_BOT_TOKEN", "").strip()
        if not token:
            raise SlackMCPError("Missing SLACK_BOT_TOKEN. Put it in your .env.")

        # Read optional channel allowlist - if set, restricts where bot can post
        # Format: comma-separated channel IDs or names (e.g., "C123,#general")
        allowed_raw = os.getenv("SLACK_ALLOWED_CHANNELS", "").strip()
        return cls(token=token, allowed_channels=_parse_allowed_channels(allowed_raw))

    @classmethod
    def from_token(
        cls, bot_token: str, allowed_channels: set[str] | None = None
    ) -> "SlackClient":
        """Factory method for programmatic instantiation (useful for testing)."""
        return cls(token=bot_token, allowed_channels=allowed_channels)

    # -------------------------
    # Internal helpers
    # -------------------------
    def _enforce_allowed_channel(self, channel: str) -> None:
        """Security check: Block posting outside an allowlist if configured."""
        # None means "no restrictions" - skip check
        # If allowlist exists, channel must be in it
        if self.allowed_channels is not None and channel not in self.allowed_channels:
            raise SlackMCPError(
                f"Channel {channel} is not in SLACK_ALLOWED_CHANNELS. Add it to allow posting."
            )

    def _slack_error(self, action: str, e: SlackApiError) -> SlackMCPError:
        """Convert SlackApiError to user-friendly SlackMCPError."""
        # SlackApiError.response is a SlackResponse object
        # It usually contains an "error" field with error code/description
        err = None
        try:
            # Try to extract structured error from response
            err = e.response.get("error")
        except Exception:
            # If response structure is unexpected, fall back to exception string
            err = None
        
        # Use extracted error if available, otherwise use exception message
        detail = err or str(e)
        return SlackMCPError(f"Slack API error ({action}): {detail}")

    # -------------------------
    # Connection / auth
    # -------------------------
    def test_connection(self) -> bool:
        """Lightweight token validation."""
        try:
            # auth_test() is the lightest API call - just validates token
            # Returns workspace info (team_id, user_id, etc.) if successful
            resp = self._client.auth_test()
            # Check "ok" field - True means token is valid
            return bool(resp.get("ok", False))
        except SlackApiError:
            # Any exception means connection/auth failed
            # Return False instead of raising to allow graceful degradation
            return False

    # -------------------------
    # Channels
    # -------------------------
    def list_channels(
        self,
        *,
        limit: int = 200,
        types: str = "public_channel,private_channel",
        exclude_archived: bool = True,
        cursor: Optional[str] = None,
    ) -> dict[str, Any]:
        """
        List channels the bot can see. Returns the raw SlackResponse-like dict.

        Requires scopes: channels:read (public), groups:read (private) depending on types.
        """
        try:
            # conversations_list() retrieves conversations (channels, DMs, groups)
            # types parameter filters: "public_channel,private_channel" excludes DMs
            # cursor enables pagination - pass None for first page, then use next_cursor
            resp = self._client.conversations_list(
                limit=limit,
                types=types,
                exclude_archived=exclude_archived,
                cursor=cursor,
            )
            # Return raw dict so caller can access response_metadata for pagination
            return dict(resp)
        except SlackApiError as e:
            # Convert to user-friendly error with context
            raise self._slack_error("list_channels", e) from e

    def list_channels_all(
        self,
        *,
        limit: int = 200,
        types: str = "public_channel,private_channel",
        exclude_archived: bool = True,
        max_pages: int = 50,
    ) -> list[dict[str, Any]]:
        """Convenience paginator to fetch many channels."""
        channels: list[dict[str, Any]] = []
        cursor: Optional[str] = None  # Start with no cursor (first page)
        pages = 0  # Track pages for safety limit

        # Pagination loop: continue until no more pages or max_pages reached
        while pages < max_pages:
            pages += 1
            
            # Fetch one page of channels
            resp = self.list_channels(
                limit=limit,
                types=types,
                exclude_archived=exclude_archived,
                cursor=cursor,
            )
            
            # Extract channels from this page and add to accumulator
            channels.extend(resp.get("channels", []) or [])
            
            # Get next cursor from response_metadata for next iteration
            # If no cursor, we've reached the last page
            cursor = (resp.get("response_metadata") or {}).get("next_cursor") or None
            if not cursor:
                break

        return channels

    def get_channel_info(self, channel_id: str) -> Optional[dict[str, Any]]:
        """Get metadata for a single channel."""
        try:
            # conversations_info() gets detailed metadata for one conversation
            # Requires channel ID (not name) - use channel name resolution if needed
            resp = self._client.conversations_info(channel=channel_id)
            
            # Check "ok" status - False means channel not found or no access
            if resp.get("ok"):
                return resp.get("channel")
            return None
        except SlackApiError as e:
            raise self._slack_error("get_channel_info", e) from e

    # -------------------------
    # Messaging
    # -------------------------
    def post_message(self, channel: str, text: str) -> dict[str, Any]:
        """
        Post a message as the bot (allowlist enforced if configured).

        Requires scope: chat:write
        """
        # Security: Check allowlist before attempting to post
        # Raises SlackMCPError if channel is not allowed
        self._enforce_allowed_channel(channel)
        
        try:
            # chat_postMessage() sends message to channel
            # Channel can be ID or name - API resolves names automatically
            # Returns message metadata including timestamp (ts) for the sent message
            resp = self._client.chat_postMessage(channel=channel, text=text)
            # Return a normalized payload (handy for tool outputs)
            return {
                "ok": resp.get("ok", False),
                "channel": resp.get("channel"),
                "ts": resp.get("ts"),  # Message timestamp - use for threading
                "message": resp.get("message", {}),
            }
        except SlackApiError as e:
            raise self._slack_error("post_message", e) from e

    def get_messages(self, channel: str, limit: int = 100) -> list[dict[str, Any]]:
        """
        Get recent messages from a channel.

        Requires: channels:history (public), groups:history (private) depending on channel type.
        """
        try:
            # conversations_history() retrieves message history
            # Messages returned newest-first (reverse chronological)
            # For >1000 messages, use pagination with cursor parameter
            resp = self._client.conversations_history(channel=channel, limit=limit)
            
            # Extract messages list - empty list if no messages or error
            if resp.get("ok"):
                return resp.get("messages", []) or []
            return []
        except SlackApiError as e:
            raise self._slack_error("get_messages", e) from e

    def get_thread(
        self, channel: str, thread_ts: str, limit: int = 20
    ) -> list[dict[str, Any]]:
        """
        Fetch replies in a thread (includes parent as first item).

        Requires: channels:history / groups:history / im:history depending on conversation type.
        """
        try:
            # conversations_replies() retrieves all messages in a thread
            # thread_ts is the timestamp of the parent message (from post_message response)
            # Returns parent message + all replies in chronological order
            resp = self._client.conversations_replies(
                channel=channel, ts=thread_ts, limit=limit
            )
            
            if resp.get("ok"):
                return resp.get("messages", []) or []
            return []
        except SlackApiError as e:
            raise self._slack_error("get_thread", e) from e

    def search_messages(self, query: str, limit: int = 20) -> list[dict[str, Any]]:
        """
        Search messages (workspace settings may restrict search).

        Requires scope: search:read
        """
        try:
            # search_messages() performs workspace-wide message search
            # Query supports Slack search syntax (e.g., "from:user in:channel")
            # Note: Search may be restricted by workspace settings
            resp = self._client.search_messages(query=query, count=limit)
            
            # Response structure: {"messages": {"matches": [...]}}
            # Extract matches array, handling missing/empty responses gracefully
            matches = (resp.get("messages") or {}).get("matches", []) or []
            return matches
        except SlackApiError as e:
            raise self._slack_error("search_messages", e) from e

    # -------------------------
    # Users
    # -------------------------
    def get_users(self, *, limit: int = 200, cursor: Optional[str] = None) -> dict[str, Any]:
        """
        List users (paged). Returns the raw dict so caller can handle pagination.

        Requires scope: users:read
        """
        try:
            # users_list() retrieves workspace members
            # Returns active users, deactivated users, and bots
            # Use cursor for pagination in large workspaces
            resp = self._client.users_list(limit=limit, cursor=cursor)
            
            # Return raw dict so caller can access response_metadata.next_cursor
            return dict(resp)
        except SlackApiError as e:
            raise self._slack_error("get_users", e) from e

    def get_users_all(self, *, limit: int = 200, max_pages: int = 50) -> list[dict[str, Any]]:
        """Convenience paginator to fetch many users."""
        users: list[dict[str, Any]] = []
        cursor: Optional[str] = None  # Start with no cursor (first page)
        pages = 0  # Track pages for safety limit

        # Pagination loop: continue until no more pages or max_pages reached
        while pages < max_pages:
            pages += 1
            
            # Fetch one page of users
            resp = self.get_users(limit=limit, cursor=cursor)
            
            # Extract members from this page and add to accumulator
            # "members" contains the list of user objects
            users.extend(resp.get("members", []) or [])
            
            # Get next cursor from response_metadata for next iteration
            # If no cursor, we've reached the last page
            cursor = (resp.get("response_metadata") or {}).get("next_cursor") or None
            if not cursor:
                break

        return users

    def get_user_info(self, user_id: str) -> Optional[dict[str, Any]]:
        """Get detailed info for a single user."""
        try:
            # users_info() retrieves detailed profile for one user
            # Requires user ID (not username) - use user lookup if needed
            resp = self._client.users_info(user=user_id)
            
            # Check "ok" status - False means user not found or no access
            if resp.get("ok"):
                return resp.get("user")
            return None
        except SlackApiError as e:
            raise self._slack_error("get_user_info", e) from e