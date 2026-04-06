Source: https://docs.slack.dev/ai/workflow-ai-integration

# Integrating AI into workflows

AI integration isn't just for agents. You can use AI in workflows too! Integrate AI into workflows by creating a [custom workflow step](/workflows/workflow-steps). The process goes like this:

1.  Create a Slack app or agent
2.  Add a custom function to it that contains the AI functionality you want in your workflow
3.  Deploy the app for the function to be available as a workflow step
4.  Users add the custom workflow step to their workflows in Workflow Builder

## AI Code Assistant tutorial {#ai-code-assistant-tutorial}

Follow the instructions set forth in the [AI Code Assistant with Hugging Face](/tools/bolt-js/tutorials/code-assistant) tutorial to create an app, install it to your workspace, code the app, then run it. The tutorial breaks down the finer details, but the way AI is integrated into the workflow begins with adding the custom function definition to the app manifest. This tutorial uses [Bolt for JavaScript](/tools/bolt-js/), but you can do this using [Bolt for Python](/tools/bolt-python/) too.

### Add a custom function {#add-a-custom-function}

Adding a custom function is a two-step process. You must add the function's definition in the app manifest, then implement the function in your app code.

Adding a custom function to an app manifest looks like this:

```
  "functions": {    "code_assist": {      "title": "Code Assist",      "description": "Get an answer about a code related question",      "input_parameters": {        "message_id": {          "type": "string",          "title": "Message ID",          "description": "The message the question was asked in.",          "is_required": true        },        "channel_id": {          "type": "slack#/types/channel_id",          "title": "Channel ID",          "description": "The channel the question was asked in",          "is_required": true        }      },      "output_parameters": {        "message": {          "type": "string",          "title": "Answer",          "description": "The response from the Code Assistant LLM",          "is_required": true        }      }    }  }
```

The app manifest tells Workflow Builder which custom functions are used in the app and what inputs and outputs to expect from them. This comes into play later when using the function as a custom step in Workflow Builder. The next step is coding the function logic.

Refer to the [AI Code Assistant with Hugging Face](/tools/bolt-js/tutorials/code-assistant) tutorial for the whole app's code. This is the portion that defines the custom step logic:

```
app.function("code_assist", async ({ client, inputs, logger, complete, fail }) => {  try {    const { channel_id, message_id } = inputs;    let messages;    try {      const result = await client.conversations.history({        channel: channel_id,        oldest: message_id,        limit: 1,        inclusive: true,      });      messages = [        { role: "system", content: DEFAULT_SYSTEM_CONTENT },        { role: "user", content: result.messages[0].text },      ];    } catch (e) {      // If the Assistant is not in the channel it's being asked about,      // have it join the channel and then retry the API call      if (e.data.error === "not_in_channel") {        await client.conversations.join({ channel: channel_id });        const result = await client.conversations.history({          channel: channel_id,          oldest: message_id,          limit: 1,          inclusive: true,        });        messages = [          { role: "system", content: DEFAULT_SYSTEM_CONTENT },          { role: "user", content: result.messages[0].text },        ];      } else {        logger.error(e);      }    }    const modelResponse = await hfClient.chatCompletion({      model: "Qwen/Qwen2.5-Coder-32B-Instruct",      messages,      max_tokens: 2000,    });    await complete({      outputs: {        message: convertMarkdownToSlack(          modelResponse.choices[0].message.content,        ),      },    });  } catch (error) {    logger.error(error);    fail({ error: `Failed to complete the step: ${error}` });  }});
```

### Add the step to a workflow {#add-the-step-to-a-workflow}

Once the app is [running](/tools/bolt-js/tutorials/code-assistant#run), the custom function becomes available for use as a workflow step in Workflow Builder. To find it, you'll open Workflow Builder, create a new workflow, and search for your custom step when adding a step to the workflow. Full details are in the [tutorial](/tools/bolt-js/tutorials/code-assistant#custom-step).

## Next steps {#next-steps}

Looking for other ways to integrate AI into your Slack apps? Check out the [Slack MCP Server](/ai/slack-mcp-server) and [Agents in Slack](/ai/agents).