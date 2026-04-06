Source: https://docs.slack.dev/ai/agent-design

# Agent design

Agents operate alongside people in Slack, joining conversations, taking actions, and surfacing information. That proximity comes with responsibility. This guide covers the design tenets that help agents earn trust: showing up transparently, respecting data boundaries, and balancing autonomy with appropriate guardrails.

## How agents show up in Slack {#how-agents-show-up}

Your users should not have to question whether they are talking to a human or an automated system. When an agent acts on a user's behalf, signal it clearly. This preserves trust in the channel and helps users understand what is human and what is automated. When naming an agent, consider leading with its utility and function rather than a branded name. This allows it to be easily identified in spaces with coworkers, apps and other agents.

Agents perform actions alongside humans in Slack. As such, follow these best practices for agent messaging:

*   Agents having conversations in channels should respect best practices. For example, if the agent is @-mentioned in a channel, it should reply in thread.
*   If the agent is sharing private information, send it only through DMs, private channels, or ephemeral messages.
*   To avoid overwhelming notifications, try batching multiple updates in one message rather than posting sequentially.
*   Avoid contributing to overwhelm by summarizing rather than narrating and providing links and sources for supporting information.

Agents should always respect data boundaries. Slack has a clear model of accessing information in conversations. Slack uses DMs, private channels, and public channels to ensure users understand where their conversation data is visible. An agent must follow this same model.

*   An agent shouldn't be able to read, access or use information that the invoking user wouldn't be able to access on their own.
*   If the invoking user can't open a file (canvas, list, Salesforce record, etc.) normally, the agent shouldn't use it for context or to generate information.
*   Huddles offer a different type of conversation but follow the same sharing model. Transcripts, meeting summaries, and notes should not be used for generating responses in an agent conversation if they can't be accessed by a user.

## Bounded autonomy {#bounded-autonomy}

An advantage of agents is their autonomy. If you're overly cautious and provide too many constraints, you may limit the capabilities and value that an agent can provide. In contrast, giving an agent too much autonomy and access may risk exposing sensitive data or taking inappropriate actions.

Bounded autonomy allows for a balance. Developers give the agent a goal and the freedom to figure out how to achieve it, but also set clear boundaries around what it can and cannot do without asking. It's possible for agents to be given access and autonomy as they earn trust and are able to perform tasks and deliver high quality responses consistently over time.

Build strong defaults with flexibility over time. Restrict default settings so it can build capabilities over time.

## Final note {#final-note}

Agent experiences on Slack, and on every platform, are moving fast. These guidelines reflect where things stand today. Some newer interaction patterns like ambient agents and agent-to-agent handoffs are still being defined and under exploration. Think of this as a living document.