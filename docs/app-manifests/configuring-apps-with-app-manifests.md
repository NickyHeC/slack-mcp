Source: https://docs.slack.dev/app-manifests/configuring-apps-with-app-manifests

# Configuring apps with app manifests

Use the [app manifest system](/app-manifests) to quickly create, configure, and reuse Slack app configurations.

Manifests are [YAML](https://yaml.org/) or [JSON](https://www.json.org/json-en.html)\-formatted configurations bundles for Slack apps. With a manifest, you can use a UI or an API to create an app with a pre-defined configuration, or adjust the configuration of existing apps.

You can share and reuse your manifests. Use this capability to create development clones of production apps. A complete reference of manifest properties can be found [here](/reference/app-manifest).

* * *

## Creating apps using manifests {#creating_apps}

1.  [Create an app](https://api.slack.com/apps?new_app=1)
    
2.  Choose to create an app **from a manifest**.
3.  Pick a development workspace and click _Next_.
4.  Paste your [manifest configuration](/reference/app-manifest#fields) in the input field provided and click _Next_.
5.  Review and verify that the configuration you entered matches the summary and click _Create_.

A new app has been created to your manifest specification! If you wish, you can also [use App Manifest APIs](#manifest_apis) to create apps programmatically.

### Updating configurations via manifests {#updating}

App configurations can be modified by editing their manifests using the [app settings page](https://api.slack.com/apps). To edit an app's configuration, click on **App Manifest** in the app settings page sidebar. You'll see a manifest editor, which will let you edit your app's configuration in YAML or JSON. Use the same [manifest schema as noted above](/reference/app-manifest#fields) to edit the manifest, and update your app.

Any validation errors will be shown inline, and there are typeahead features to help you update your manifest.

Alternatively, you can [use App Manifest APIs](#manifest_apis) to update existing apps programmatically, as explained below.

* * *

## Using the App Manifest APIs {#manifest_apis}

You can use your manifest YAML or JSON together with a range of APIs that help you to manage your apps:

*   [`apps.manifest.create`](/reference/methods/apps.manifest.create) is used to create apps from JSON manifests.
*   [`apps.manifest.update`](/reference/methods/apps.manifest.update) will let you update configurations of your existing apps.
*   [`apps.manifest.delete`](/reference/methods/apps.manifest.delete) can delete any of your apps.
*   [`apps.manifest.export`](/reference/methods/apps.manifest.export) exports the manifest of your existing apps.
*   [`apps.manifest.validate`](/reference/methods/apps.manifest.validate) will validate any JSON manifest against the [correct schema](/reference/app-manifest#fields).

Each of these API methods should be used with an [**app configuration access token**](#config-tokens). Create an app config token on the [app settings page](https://api.slack.com/apps) below the list of apps. Under **Your App Configuration Tokens**, click **Generate Token** to create one.

* * *

## Managing configuration tokens {#config-tokens}

Each config token is unique to a user and a workspace, but not an app. This means you can manage the configuration of any of your apps in a single development workspace, with just one config token.

When you create a configuration token, the "Slack Tooling Tokens Vendor" app will be added to the workspace.

### Rotating configuration tokens {#rotating}

Each app configuration token will expire 12 hours after it has been generated. In order to continually rotate your config tokens, you are also provided with a **refresh token**.

It's strongly suggested that you refresh your token before it expires, rather than waiting for it to expire and checking for an error from the Slack API.

In order to refresh config tokens, make a call to [`tooling.tokens.rotate`](/reference/methods/tooling.tokens.rotate), using the refresh token in the `refresh_token` argument. In response you'll receive something like this:

```
{	"ok": true,	"token": "xoxe.xoxp-...",	"refresh_token": "xoxe-...",	"team_id": "...",	"user_id": "...",	"iat": 1633095660,	"exp": 1633138860}
```

The `token` field contains your new config access token, which you can then store and use for Manifest API calls. The `refresh_token` field contains a _new_ refresh token.

The remainder of the response above contains fields which identify the source workspace and user of each token, as well as timestamps which indicate when the token was issued and when it will expire.

* * *

## Sharing manifests {#sharing}

You can share manifests with others so they can create Slack apps based off of your own app's configurations.

You can view and export the manifest for any existing app within the [app config pages](https://api.slack.com/apps). First, open your app's config and then browse to the **App Manifest** section.

From here, you'll be able to directly copy the manifest configuration, or export them to a downloadable file. You can also use the [`apps.manifest.export`](/reference/methods/apps.manifest.export) API method to export programmatically.

Once exported, you can safely share the manifest with anyone — it doesn't contain any secure information, although you might prefer to keep any request URLs private — or use it yourself to duplicate your app for development purposes.

If you want to share your manifest as a link, you can use the following URL pattern:

```
https://api.slack.com/apps?new_app=1&manifest_yaml=<manifest_here>
```

Or to share the manifest in JSON format:

```
https://api.slack.com/apps?new_app=1&manifest_json=<manifest_here>
```

Ensure you URL encoded the YAML or JSON before sharing the URL.

You can use this URL in any link or button you want — the URL will direct users right into the app creation flow.

* * *

### Troubleshooting errors {#schema_errors}

If you receive an `invalid_manifest` response when trying to use any App Manifest API, it indicates that the manifest you supplied didn't match the [correct schema](/reference/app-manifest#fields).

To better locate the problem with your manifest, the `invalid_manifest` error should be accompanied by an `errors` array:

```
{	"ok": false,	"error": "invalid_manifest",	"errors": [		{			"message": "Event Subscription requires either Request URL or Socket Mode Enabled",			"pointer": "/settings/event_subscriptions"		},		{			"message": "Interactivity requires a Request URL",			"pointer": "/settings/interactivity"		},		{			"message": "Interactivity requires Socket Mode enabled",			"pointer": "/settings/interactivity"		}	]}
```

Each of the items in this array contain a `message` which describes the problem, and a `pointer` which indicates the problem's location within your supplied manifest. Use these two pieces of info to correct your manifest and try again.

## Try pre-defined manifests {#tutorials}

Our guided tutorials show you the process of building common app use cases, using [Bolt](/tools). Every tutorial has its own pre-defined app manifest to allow you to create and configure a Slack app.

[View tutorials](/samples)