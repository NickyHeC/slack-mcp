Source: https://docs.slack.dev/workflows

# Workflows

Workflows are a subset of Slack apps with unique abilities and restrictions. You can create workflows without any code in the developer-adjacent [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder). While Workflow Builder contains many built-in steps spanning both Slack-native and external app functionality, you may wish to create a step that carries out custom logic. For that, we have custom workflow steps.

Custom workflow steps can be written in an app created using the [Deno Slack SDK](/tools/deno-slack-sdk) or using the Bolt framework, available in [Bolt for Python](/tools/bolt-python/concepts/custom-steps), [Bolt for JavaScript](/tools/bolt-js/concepts/custom-steps), and [Bolt for Java](/tools/java-slack-sdk/guides/custom-steps). Regardless of which framework you choose to create your app, you can do so where you already work, using the [Slack CLI](/tools/slack-cli).

Functionality varies slightly when choosing which framework to create custom steps in; the biggest difference is where the steps are hosted. Apps created using the Deno Slack SDK are Slack-hosted, and apps created using the Bolt framework are self-hosted.

✨ **Learn more about custom workflow steps and how to build them** in our [guide to workflow steps](/workflows/workflow-steps).

✨ **If you'd rather _build_ instead of _develop_** and need no custom logic, check out [Workflow Builder](https://slack.com/help/articles/360035692513-Guide-to-Slack-Workflow-Builder).

✨ **Want a side-by-side breakdown of workflows vs. apps?** Look no further than [this guide](/workflows/comparing-workflows-apps).