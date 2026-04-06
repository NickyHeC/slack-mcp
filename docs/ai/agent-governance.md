Source: https://docs.slack.dev/ai/agent-governance

# Governance and trust

This guide explores how to build a governance framework that balances oversight with a seamless user experience. By focusing on stakeholder balance, human-in-the-loop controls, and progressive trust, you can create agents that are as reliable as they are capable.

## Stakeholder balance {#stakeholder-balance}

Each stakeholder group needs something different from your agent. Admins need governance controls, compliance teams need oversight and auditability, developers need reusable infrastructure, and end users need an experience that's faster than doing the task themselves. Here's how to address each in Slack.

### For admins {#for-admins}

*   **Clear AI/data usage guidelines**: Make it straightforward for admins to understand how your agent uses AI and what data it accesses. Document which models are used, what data is sent to them, what is retained, and what isn't.
    
*   **Audit trails and observability baseline**: Observability is the ability to monitor, trace, and understand what an agent is doing. Log which channels were accessed, what actions were taken, who triggered the request, and what model was used.
    
    *   Use the [Audit Logs API](/admins/audit-logs-api) to keep a record of admin-level changes (e.g., exclusion settings, configuration changes).
        
    *   Implement dashboards and alerts for tracking agent incidents, performance, and reliability.
        
    *   Include elements like an "AI Excluded" indicator in a channel header so admins and users can see what's in effect.
        
    *   Here are some common metrics to track for each response:
        
        Key
        
        Description
        
        `total_latency_ms`
        
        End-to-end clock time including tool calls
        
        `outcome`
        
        `success`, `partial`, or `failure` to reflect whether the agent actually accomplished what the user asked for, not just whether a response was sent
        
        `user_id`
        
        User in the interaction
        
        `agent_id`
        
        Which agent or handler produced this response; critical in multi-agent setups
        
        `tools_called`
        
        Array of tool names invoked; shows agent decision path
        
        `model`
        
        Model name and version; required for cost attribution and regression tracking
        
        `retry_attempts`
        
        Count of retries; signals LLM or API instability
        
        `total_tokens`
        
        Input and output token count combined
        
        `token_efficiency`
        
        Output/input token ratio; low ratio indicates over-prompting
        
        `error_type`
        
        `llm_error`, `tool_error`, `validation_error`, or `timeout`
        
*   **Policy controls and governance tooling**: Give admins the ability to configure agent behavior, set boundaries on what data the agent can access, and control which capabilities are enabled. Capabilities should be modular so admins can start narrow and expand.
    

### For compliance teams {#for-compliance}

Ensuring your agent is built to be reliable is feasible when you keep the following guidance in mind:

*   **Build explicit fallback behaviors**: Define what the agent does when it can't answer or a tool call fails. Don't let it silently fail or hallucinate confidently.
*   **Set timeouts and retry logic**: Handle async tool calls gracefully; don't let hung requests degrade the user experience.
*   **Rate-limit and monitor API usage**: Token/cost runaway is a real risk; monitor usage and set guardrails.
*   **Use traceable, sourced responses**: Encourage agents to cite or reference the source of their answers so users can verify accuracy.
*   **Test for consistency**: Identical queries should return consistent enough responses.
*   **Demonstrate business value**: Technically reliable tools that can't show a return on investment get abandoned. Help developers provide metrics so teams can sustain their AI tools beyond early experimentation.

Using search-related scopes related to the [Real-time Search API](/apis/web-api/real-time-search-api#required-scopes) may bring up questions surrounding data privacy. Consider marking some scopes as [optional](/authentication/installing-with-oauth#optional-scopes) in order to reduce installation abandonment. If you are concerned about data being accessed from a secure workspace, for example a [FedRAMP](https://slack.com/solutions/govslack) workspace, we recommend either only installing the app in that workspace or restricting any app with a `search:read.*` scope from being installed.

Read more about data privacy concerns in the [Real-time Search API](/apis/web-api/real-time-search-api#privacy) guide.

### For developers {#for-developers}

*   **Slack platform building blocks**: Use [Block Kit](/block-kit) for composable interactive UI, the [Real-Time Search API](/apis/web-api/real-time-search-api) for search-based context gathering, the [Conversations API](/apis/web-api/using-the-conversations-api) for thread-specific situational context, and the [assistant API methods](/reference/methods?family=assistant) for thread status, suggested prompts, and thread management.
*   **Reusable patterns and deterministic fallback handling**: Use deterministic, local fallback messages when things go wrong. For example, have the agent respond with "I could not format that response safely. Try again." or "I hit a temporary processing issue. Retry in a moment.", rather than outputting raw model payload when validation fails.
*   **Slack tooling**: Use the [Slack CLI](/tools/slack-cli/) for scaffolding, local run, and installation. Use the [Bolt framework](/tools#bolt) (JavaScript, Python, or Java) for app implementation, and use [Block Kit Builder](https://app.slack.com/block-kit-builder) for prototyping UI.

### For end users {#for-end-users}

*   **Transparency in UI**: Users should always know what's happening, what's complete, and what's blocked. Use [thread status](/reference/methods/assistant.threads.setstatus), [task cards](/reference/block-kit/blocks/task-card-block/), and structured responses to keep the user informed throughout the interaction.
*   **Control surfaces**: Implement [buttons](/reference/block-kit/block-elements/button-element), [actions](/reference/block-kit/blocks/actions-block), and [slash commands](/interactivity/implementing-slash-commands) that let users steer agent behavior.
*   **Contextual UI that fits workflow**: Use threads for in-context work alongside the conversation that triggered it, the [App Home](/surfaces/app-home) for workflow visibility and configuration, and [modals](/surfaces/modals) for structured input and multi-step flows.

## Human-in-the-loop {#human-in-the-loop}

Keeping humans in the loop requires making agent state visible, giving users real controls, and ensuring the agent's internal state is queryable at any time. Slack provides specific APIs and surfaces for each.

### Transparency {#transparency}

*   **Use the [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus) API method** to show visible progress. If generation takes longer than expected or if there are multiple tasks working behind the scenes, keep the user informed that the app is still working. This ensures the user does not assume the app is glitching and gives them insight into what the app is doing to provide them an answer.
    
    Implementing status updates
    
    Do this by calling the [`assistant.threads.setStatus`](/reference/methods/assistant.threads.setStatus) method to set a follow-up status.
    
    ```
    status="is thinking..."status="is searching company knowledge..."status="spinning the digital hamster wheel..."
    ```
    
*   **Streaming with task cards for orchestration visibility**: Use the [`chat.startStream`](/reference/methods/chat.startStream) API method with `task_display_mode` set to `plan` or `timeline` to show the agent's work as it happens. Emit task updates for each major operation so users can follow the chain of actions. Update task state progressively: `pending` → `in_progress` → `complete`.
    
*   **Clear agent identity**: The agent should be clearly distinguishable from a human at all times. An agent that masquerades as a human user breaks trust and complicates auditability.
    

### Control {#control}

*   **App Home for pause/resume/stop controls**: Use the [App Home](/surfaces/app-home) as the persistent surface for workflow visibility and controls. Show running workflows, recent completions, and blocked items. Expose pause/resume/stop/retry/redirect actions so users can intervene without reconstructing thread history.
*   **Block Kit actions for confirmations and next steps**: Include next-step actions in every agent response—buttons and selects that let users steer what happens next. Require confirmation for high-impact actions.
*   **Slash commands for state inspection**: These [commands](/interactivity/implementing-slash-commands) give users a way to inspect and configure agent behavior without interrupting work in progress.
    *   `/agent logs` — view recent agent activity
    *   `/agent state` — inspect current interstitial state (goal, constraints, decisions)
    *   `/agent settings` — configure agent behavior and preferences

The best agents expose their plan in a way that lets users edit it while in progress.

*   **Reversing actions**: Users should be able to pause, resume, redirect, or stop the agent.
*   **Checkpoints**: Each pattern should reduce the cognitive burden on the user, not add process for its own sake.
    *   Approval gates before the agent creates, sends, or deletes anything.
    *   Options to choose between approaches.
    *   Structured, proactive prompts when the agent is missing something it needs.
    *   A status panel showing what's running, waiting, or blocked.

### Inspectable state {#inspectable-state}

The agent's state must be visible and queryable, not just described or narrated. Users can query agent state at any time through [slash commands](/interactivity/implementing-slash-commands), [App Home](/surfaces/app-home) views, or inline [Block Kit blocks](/reference/block-kit/blocks). When transparency, control, and inspectable state work together, users develop a mental model of the agent that lets them delegate with confidence rather than limiting it to trivial tasks where mistakes don't matter.

## Progressive trust {#progressive-trust}

Trust is earned through consistent behavior over time. Slack's streaming APIs, Block Kit, and permission model give you the tools to make orchestration visible, actions reversible, guardrails explicit, and authority progressive.

*   **Visible orchestration**: Use `task_display_mode` in the [`chat.startStream`](/reference/methods/chat.startStream) API method to control how tasks appear; `plan` for grouped steps, `timeline` for step-by-step updates. [Task cards](/reference/block-kit/blocks/task-card-block) show the progression of work: `pending` → `in_progress` → `complete`. Users can follow what's happening at each step.
*   **Reversible actions**: Provide undo flows for meaningful operations. Surface recovery paths clearly in the UI so users can recover without starting over. For example, "Re-run with different parameters," "Undo," and "Show original".
*   **Explicit guardrails**: Use least-privilege scopes and respect Slack's permission model. The default action scope should be narrow. Expanding scope should require explicit user or admin action.
*   **Progressive authority with Block Kit actions**: The agent identifies an opportunity to provide more value: "I can also create a more detailed canvas if you'd like?"

Block Kit actions present the permission choice:

```
{  "type": "section",  "text": {    "type": "mrkdwn",    "text": "*Canvas Permissions*\nAllow this agent to create canvases on your behalf?"  }},{  "type": "actions",  "elements": [    {      "type": "button",      "text": { "type": "plain_text", "text": "Always allow" },      "action_id": "canvas_always_allow",      "style": "primary"    },    {      "type": "button",      "text": { "type": "plain_text", "text": "Allow once" },      "action_id": "canvas_allow_once"    },    {      "type": "button",      "text": { "type": "plain_text", "text": "Deny" },      "action_id": "canvas_deny",      "style": "danger"    }  ]}
```

Start with confirmations for every new capability. As the user selects "Always allow" for specific action classes, remove the friction for those actions.

## Next steps {#next-steps}

✨ Develop the entire response loop of your agent with guidance from [Developing agents](/ai/developing-agents).

✨ Learn the best way to [manage context](/ai/agent-context-management) in agents.