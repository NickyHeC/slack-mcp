Source: https://docs.slack.dev/ai/agent-context-management

# Context management

Good context management means pulling a targeted slice of workspace data relevant to the current goal, storing it as structured state, and passing that state to the LLM on every subsequent exchange. This avoids re-querying the same thread or channel on every turn and keeps token costs and noise under control. Slack offers multiple tools for gathering context intelligently.

## Context management best practices {#context-management-best-practices}

These best practices surrounding context management will keep your agent aligned with the user's goal while minimizing waste.

*   **Don't refetch entire threads:** Use structured state objects, like `{ goal, constraints, decisions, artifacts }`. Keep interstitial state between turns rather than re-injecting the same long thread or external artifacts on every turn.
*   **Progressive summarization of older interactions:** Summarize older material into reusable state while preserving key decisions and unresolved items. This keeps context compact without losing what matters.
*   **Token budgets per request:** Enforce token budgets and prefer small, relevant context slices over raw conversational exhaust.
*   **Slack-specific context gathering:** Use the Real-Time Search API for channel summaries, topic searches, and relevant messages across the workspace.
*   **Conversations API:** Use the Conversations API sparingly to retrieve thread history and replies when you need the full picture of a specific discussion.
*   **Drift detection:** Have your app detect when the current work has diverged from the original objective. Before taking significant actions, confirm the current goal and constraints with the user.

## Context types {#context-types}

### Workspace search {#workspace-search}

Use the [`assistant.search.context`](/reference/methods/assistant.search.context) API method for cross-workspace context gathering across messages, files, channels, and canvases. Phrasing the query as a natural language question will trigger Slack to use semantic search. This method requires an `action_token` from the triggering event payload when using a bot token. Do not use the legacy `search.messages` endpoint. Reference the [Real-time Search API](/apis/web-api/real-time-search-api) docs for more information.

```
const result = await client.assistant.search.context({  query: 'What are the latest decisions on project alpha?',  action_token: event.action_token,  content_types: ['messages', 'files', 'channels'],  channel_types: ['public_channel', 'private_channel'],  include_context_messages: true,  limit: 20});const matches = result.results?.messages || [];// Each match includes: content, permalink, channel_id, message_ts, context_messages
```

### Thread context {#thread-context}

Use the [`conversations.replies`](/reference/methods/conversations.replies) API method to drill into a specific thread from search results. `messages[0]` is the parent; the rest of the array is made up replies. You can use the chat's `thread_ts` parameter to gather the immediate message history.

```
const result = await client.conversations.replies({  channel: match.channel_id,  ts: match.message_ts,  limit: 100});const replies = result.messages || [];
```

### Channel context {#channel-context}

Use the [`conversations.history`](/reference/methods/conversations.history) API method to pull surrounding messages from a channel identified in search results. Paginate with `cursor` when `has_more` is true.

```
const result = await client.conversations.history({  channel: channelId,  oldest: String((Date.now() / 1000) - 7 * 24 * 60 * 60),  limit: 100});const messages = result.messages || [];// Paginate: result.has_more, result.response_metadata.next_cursor
```

### Structured state object {#structured-state-object}

After acquiring context, use structured state objects: `{ goal, constraints, decisions, artifacts }` to keep interstitial state between turns rather than re-injecting the same long thread or external artifacts on every turn.

```
const state = {  goal: '',        // user's current objective  constraints: '', // date range, channel scope, filters  decisions: [],   // key decisions identified this session  artifacts: [],   // outputs created (summaries, canvases, links)  sources: []      // [{ text, link }] — attribution for cited messages};
```

### Minimal context pattern example {#minimal-context-pattern}

This is a focused example showing workspace search, narrowing down the thread, and structured state in a single `app_mention` handler:

```
app.event('app_mention', async ({ event, client }) => {  const channel = event.channel;  const threadTs = event.thread_ts ?? event.ts;  const prompt = (event.text || '').trim();  });
```

When context management is done well, the agent gets more useful over time rather than degrading as conversations grow longer.

## Next steps {#next-steps}

✨ Develop the entire response loop of your agent with guidance from [Developing agents](/ai/developing-agents).

✨ Ensure your app is secure and trustworthy with guidance from [Governance and trust](/ai/agent-governance).