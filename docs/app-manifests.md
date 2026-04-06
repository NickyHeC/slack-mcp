Source: https://docs.slack.dev/app-manifests

# App manifests

All apps have a manifest. Manifests are reusable configurations; they are designed to make an app's configuration "portable". You can store a manifest in version control such as GitHub where collaborators can easily grasp the setup of your app. Manifests can also make testing easier for apps that have the same setup.

Manifests are expressed in `JSON` or `YAML` and can be authored in your app's configuration page.

Currently, there are two versions of app manifests. [Apps created using the Deno Slack SDK](/tools/deno-slack-sdk/) exclusively use version 2, while Slack apps may use either version. If the `version _metadata` property is not specified, Slack will treat your manifest configuration as v1. The [properties](/reference/app-manifest#fields) outlined in the app manifest reference indicate which manifest version they are included in.

## Manifests for granular permissions apps {#manifests-for-granular-permissions-apps}

For granular permissions apps, [the app manifest](/app-manifests/configuring-apps-with-app-manifests) can help you quickly create, configure, and copy Slack apps. You can share and reuse these manifests. Use this capability to create development clones of production apps.

App manifests be created and managed by visiting [Your Apps](https://api.slack.com/apps), selecting the app, then navigating to **Features** > **App Manifest** or directly by using the [App Manifest API](/app-manifests/configuring-apps-with-app-manifests#manifest_apis).

When you create an app through [Your Apps](https://api.slack.com/apps) using the **Create New App** button, you have an option to create from scratch or from an existing app manifest. This is how you could replicate a manifest from another app, pasting the recycled manifest there.

✨ Read more on the [Create and configure apps with manifests page](/app-manifests/configuring-apps-with-app-manifests) for Slack apps page.

## Manifests for apps created with the Deno Slack SDK {#manifests-for-apps-created-with-the-deno-slack-sdk}

For apps built with the Deno Slack SDK, the manifest holds the details of your app’s configuration, declaring the custom types, steps, workflows, and more that the automation contains.

Keep your local `manifest.ts` or `manifest.js` file up-to-date with any custom types, steps, datastores, and workflows required for your app.

✨ Read more on the [App manifest page](/tools/deno-slack-sdk/guides/using-the-app-manifest) for apps created with the Deno Slack SDK.