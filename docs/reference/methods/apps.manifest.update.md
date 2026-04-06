Source: https://docs.slack.dev/reference/methods/apps.manifest.update

# apps.manifest.update method

DocsCall generator

## Facts {#facts}

**Description**Update an app from an app manifest

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/apps.manifest.update
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.apps.manifest.update
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.apps_manifest_update
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().appsManifestUpdate
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 1: 1+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

An [app configuration access token](/authentication/tokens#config).

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`manifest`**`string`Required

A JSON app manifest encoded as a string. This manifest **must** use a valid [app manifest schema - read our guide to creating one](/app-manifests/configuring-apps-with-app-manifests#fields). As this method entirely _replaces_ any previous configuration, manifest must contain both unmodified and modified fields.

**`app_id`**Required

The ID of the app whose configuration you want to update.

## Usage info {#usage-info}

### Using manifests {#using_manifests}

This method accepts an app manifest as an argument. Read our [guide to app manifests](/app-manifests/configuring-apps-with-app-manifests) to learn how create or reuse them.

If you receive an `invalid_manifest` response when trying to use any App Manifest API, it indicates that the manifest you supplied didn't match the [correct schema](/reference/app-manifest#fields).

To better locate the problem with your manifest, the `invalid_manifest` error should be accompanied by an `errors` array:

```
{	"ok": false,	"error": "invalid_manifest",	"errors": [		{			"message": "Event Subscription requires either Request URL or Socket Mode Enabled",			"pointer": "/settings/event_subscriptions"		},		{			"message": "Interactivity requires a Request URL",			"pointer": "/settings/interactivity"		},		{			"message": "Interactivity requires Socket Mode enabled",			"pointer": "/settings/interactivity"		}	]}
```

Each of the items in this array contain a `message` which describes the problem, and a `pointer` which indicates the problem's location within your supplied manifest. Use these two pieces of info to correct your manifest and try again.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "app_id": "A012ABCD0A0",  "permissions_updated": false}
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

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`failed_adding_collaborator`

Failed writing a collaborator record for this new app

`failed_creating_app`

Failed to create the app model

`failed_datastore_operation`

Failed while managing datastore infrastructure

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

Internal error.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_app`

An app created from the provided manifest would not be valid.

`invalid_app_id`

The app id passed is invalid.

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

`invalid_manifest`

The provided manifest file does not validate against schema.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

User does not have permission to update app

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

Unknown method