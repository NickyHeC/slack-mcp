"""Slack MCP server (OAuth).

Uses the Slack Web API via HTTPS REST. Base URL: https://slack.com/api

Authentication is handled via OAuth 2.0. The Dedalus platform reads
OAUTH_* environment variables to orchestrate the browser-based OAuth
flow and token refresh. The server code never manages OAuth tokens
directly — it calls ctx.dispatch() and DAuth applies the token inside
the enclave.

To start the server:
    python -m src.main
"""

import os
import asyncio

from dotenv import load_dotenv
from dedalus_mcp import MCPServer
from dedalus_mcp.server import TransportSecuritySettings
from dedalus_mcp.auth import Connection, SecretKeys

load_dotenv()

slack_connection = Connection(
    name="slack",
    secrets=SecretKeys(token="SLACK_ACCESS_TOKEN"),
    base_url="https://slack.com/api",
    auth_header_format="Bearer {api_key}",
)


def create_server() -> MCPServer:
    as_url = os.getenv("DEDALUS_AS_URL", "https://as.dedaluslabs.ai")
    return MCPServer(
        name="slack-mcp",
        connections=[slack_connection],
        http_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
        streamable_http_stateless=True,
        authorization_server=as_url,
    )


async def main() -> None:
    from src.tools import tools

    server = create_server()
    for tool_func in tools:
        server.collect(tool_func)
    await server.serve(port=8080)


if __name__ == "__main__":
    asyncio.run(main())
