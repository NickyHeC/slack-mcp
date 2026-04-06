Source: https://docs.slack.dev/reference/methods/apps.manifest.export

# apps.manifest.export method

DocsCall generator

## Facts {#facts}

**Description**Export an app manifest from an existing app

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/apps.manifest.export
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.apps.manifest.export
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.apps_manifest_export
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().appsManifestExport
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

An [app configuration access token](/authentication/tokens#config).

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`app_id`**Required

The ID of the app whose configuration you want to export as a manifest.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "manifest": {    "_metadata": {      "major_version": 1,      "minor_version": 1    },    "display_information": {      "name": "Zork",      "description": "You are likely to be eaten by a grue.",      "background_color": "#0000AA",      "long_description": "Play the Infocom classic text adventure and find your way to the end of the maze. ZORK is a game of adventure, danger, and low cunning. In it you will explore some of the most amazing territory ever seen by mortals. No workspace should be without one!"    },    "features": {      "app_home": {        "home_tab_enabled": true,        "messages_tab_enabled": false,        "messages_tab_read_only_enabled": false      },      "bot_user": {        "display_name": "zork",        "always_online": true      },      "slash_commands": [        {          "command": "/zork",          "description": "You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here.",          "usage_hint": "/zork open mailbox",          "should_escape": false        }      ],      "workflow_steps": [        {          "name": "Example step",          "callback_id": "tutorial_example_step"        }      ]    },    "oauth_config": {      "redirect_urls": [        "https://example.com/slack/auth"      ],      "scopes": {        "bot": [          "commands",          "workflow.steps:execute"        ]      }    },    "settings": {      "event_subscriptions": {        "bot_events": [          "workflow_step_execute"        ]      },      "interactivity": {        "is_enabled": true      },      "org_deploy_enabled": false,      "socket_mode_enabled": true,      "is_hosted": false,      "token_rotation_enabled": false    }  }}
```

#### Typical error response if invalid app ID used

```
{  "ok": false,  "error": "invalid_app_id"}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`app_not_eligible`

The specified app is not elgible for this API.

`app_not_found`

The specified app was not found.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`failed_export`

Failed to export manifest for given app ID

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

Internal error.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_app_id`

The app ID passed is invalid.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

User does not have proper permissions.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

This method does not exist.