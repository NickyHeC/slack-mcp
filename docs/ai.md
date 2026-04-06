Source: https://docs.slack.dev/ai

# AI in Slack overview

Slack provides a set of tools, APIs, and platform features for bringing AI-powered experiences into the flow of work.

## Build agents {#build-agents}

Agents are autonomous, goal-oriented AI apps that can reason, use tools, and maintain context across conversations in Slack. They go beyond simple Q&A bots by planning actions, calling external systems, and iterating on results without constant human intervention.

Slack offers dedicated surfaces for agents, including a split-view container, top navigation entry point, app threads, text streaming, and suggested prompts. Use these alongside design best practices around trust, transparency, and bounded autonomy to build agents that feel native to Slack. Explore all things agents with the following pages:

*   [**Agents overview**:](/ai/agents) Core concepts, principles, and use cases for agents in Slack.
*   [**Agent design**:](/ai/agent-design) Design principles for how agents show up in Slack.
*   [**Entry points and interaction surfaces**:](/ai/agent-entry-and-interaction) Where users access your agent and the Slack surfaces available for interaction, including the agent container, channels, App Home, modals, and more.
*   [**Developing agents**:](/ai/developing-agents) Technical guide for implementing the agent response loop, including loading states, text streaming, thinking steps, feedback, and app threads.
*   [**Context management**:](/ai/agent-context-management) Best practices for gathering, structuring, and maintaining context across turns using workspace search, thread history, and structured state.
*   [**Governance and trust**:](/ai/agent-governance) Guidance on stakeholder balance, human-in-the-loop design, and progressive trust to build agents that earn sustained use.

## Connect to Slack data with the Slack MCP Server {#connect-mcp}

The Slack MCP server lets AI apps search channels, send messages, manage canvases, and perform other Slack actions through any MCP-compatible client. Explore the Slack MCP Server with the following docs:

*   [**Slack MCP Server overview**:](/ai/slack-mcp-server) Architecture, available tools, and how to get started.
*   [**Connect to Cursor**:](/ai/slack-mcp-server/connect-to-cursor) Set up the Slack MCP server in Cursor.
*   [**Connect to Claude**:](/ai/slack-mcp-server/connect-to-claude) Set up the Slack MCP server in Claude.
*   [**Developing a sample app with the Slack MCP Server**:](/ai/slack-mcp-server/developing) Build apps that integrate with Slack data through MCP.

## Integrate in other ways {#other-integrations}

AI doesn't have to only live in an agent. You can bring AI capabilities into Slack through workflow automations and Salesforce Agentforce.

*   [**Integrating AI into workflows**:](/ai/workflow-ai-integration) Add AI-powered custom steps to Workflow Builder so any user can access AI in their automations.
*   [**Customizing Agentforce agents**:](/ai/customizing-agentforce-agents-with-custom-slack-actions) Build and deploy Agentforce agents with custom Slack actions.