Source: https://docs.slack.dev/ai/agents

# Welcome to building agents for Slack

Slack is uniquely suited for rich agent experiences. It is conversational by default, built on a rich interaction model (Block Kit), and context-aware. It also supports multi-surface orchestration and secures data with built-in identity and permissions.

This guide is an overview of the core principles and use cases of what an agent is and is not in Slack.

## What is an agent? {#what-is-an-agent}

An AI agent is a partially autonomous system that can operate independently over extended periods, using various tools to accomplish complex tasks.

AI agents can complete complex tasks beyond natural language processing that include:

*   Gathering relevant context
*   Defining a goal
*   Planning a sequence of actions
*   Executing against those actions

It also can observe the results and iterate without the constant intervention of a person.

### Agents are {#agents-are}

*   **Autonomous within defined boundaries**: The defining characteristic of an agent is that it can decide what to do next without a human prompting each step. The agent should understand the boundaries of its authority and recognize when a decision exceeds those boundaries; it can then pause for human input rather than guess.
*   **Goal-oriented**: The agent is given an objective by a person. It determines how to achieve the goal by itself. It's likely the agent will need to call on multiple tools, gather context from a variety of sources, and take multiple turns to generate a response or output.
*   **Able to use tools**: Agents take actions using tools; these are functions the agent can invoke to read or write to external systems. The agent decides which tools to call, when to call them, and the parameters in which to use the tools. A few examples of common tools types are:
    *   Read tools: search, query a database, fetch a document, read a calendar.
    *   Write tools: send an email, create a ticket, update a record, post a message.
    *   Execution tools: run code, trigger a workflow, call an API.
    *   Agent tools: invoke another agent.
*   **Able to have memory**: Agents maintain context and knowledge across steps within a task. They take into consideration different types of memory:
    *   In-context memory: what's in the active prompt window right now.
    *   Short-term memory: what happened earlier in this task thread.
    *   Long-term memory: facts persisted across sessions in a workspace.
    *   Shared memory: state accessible to other agents in a multi-agent system.

### Agents are not just {#agents-are-not}

*   **Bots**: Bots respond to specific inputs with predetermined outputs with no reasoning, memory, or adaptation. They can only do what they were explicitly programmed to do.
*   **Workflows**: Workflows (that is, non-AI powered workflows) are automations that execute a sequence of steps reliably and repeatably when triggered.
*   **Assistants**: An assistant is a conversational and reactive tool. It responds to a question or prompt with language understanding and reasoning, but it cannot take autonomous actions or decide what to do next.
*   **Magic ✨**: The agent is only as capable as the tools it's given and the quality of the goal you define.

## Core principles {#core-principles}

Let these core principles of agents guide you in your building journey.

### People feel in control of their experience

Using agents is still very new for many people, so investing in features that build trust is a top priority. This trust is built by showing people what the agent is doing and why.

1.  Ensure that every action taken and decision made is accessible to the user.
2.  Any action with real-world output (sending an email, approvals, updating a record) should require explicit human confirmation.
3.  Designing for failure is a primary part of building an agent experience. Agents can make mistakes and hallucinate, so users should have a clear way to understand what happened and continue with their work.

![control icon](/img/guides/ai_container/agent_principle _control.png)

### Agents are available where people are already working, but not disruptive

Don't take people out of their flow-of-work to engage with an agent. An effective agent acts as a context-aware tool embedded in the space where work is already happening (channels, canvas, etc.).

![flow of work icon](/img/guides/ai_container/agent_principle _flow_of_work.png)

### Agents are not inherently safe

An autonomous tool with unfettered access to information and creation capabilities can do real world harm. It is the duty of every developer to build guardrails, permissions, and human-in-the-loop checkpoints as engineering requirements, not afterthoughts.

![unsafe icon](/img/guides/ai_container/agent_principle _safety.png)

## Use cases {#use-cases}

Agents can solve a variety of use cases in any industry. Knowing that AI models, Slack, and third-party integrated apps are your data sources, the world is your agent's oyster. Take for example these use cases for agents:

*   Channel expert/channel agent unlocks channel-level use cases, helping surface relevant context and answer questions right in channels.
*   Service agent replaces traditional chatbots with AI that can handle a wide range of service issues without preprogrammed scenarios.
*   Case management support agent for email marketing content management workflows with Slack approvals.

**Sales-focused agents**

*   Sales Development Representative (SDR) engages with prospects 24/7, answering questions, managing objections, and scheduling meetings based on CRM and external data.
*   Sales Coach provides personalized role-play sessions for your sales team, using Salesforce data and generative AI to help sellers practice pitches and objections tailored to specific deals.
*   Merchandiser assists your ecommerce merchandisers with site setup, goal setting, personalized promotions, product descriptions, and data-driven insights, simplifying daily tasks.
*   Campaign Optimizer automates the full campaign lifecycle, using AI to analyze, generate, personalize, and optimize marketing campaigns based on business goals.

## Distribution options {#distribution}

Once you've created an agent, Slack has distribution options. You may choose to keep your agent [undistributed](/app-management/distribution) for internal use or submit it to the [Slack Marketplace](https://www.slack.com/marketplace) for wider adoption.

Choose internal distribution when:

*   Your use case is company-specific
*   Your app depends on private or internal systems
*   You do not need broad cross-org distribution

Choose Slack Marketplace when:

*   The problem is generalizable across organizations
*   You can support multiple external customers
*   You can meet review, support, and security requirements

Review Slack Marketplace guidelines and requirements [here](/slack-marketplace/slack-marketplace-app-guidelines-and-requirements).

## Next steps {#next-steps}

➡️ Learn the ins and outs of building a great agent in the guide to [Agent design](/ai/agent-design).

➡️ Get started building with AI feature offerings in the [Developing agents guide](/ai/developing-agents).

➡️ Browse which third-party agents are available for Slack in the [Slack Marketplace](http://www.slack.com/marketplace).