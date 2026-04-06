Source: https://docs.slack.dev/reference/methods/entity.presentDetails

# entity.presentDetails method

DocsCall generator

## Facts {#facts}

**Description**Provide custom flexpane behavior for Work Objects. Apps call this endpoint to send per-user flexpane metadata to the client.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/entity.presentDetails
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.entity.presentDetails
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.entity_presentDetails
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().entityPresentDetails
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`trigger_id`**`string`Required

A reference to the original user action that initiated the request.

### Optional arguments

**`metadata`**`object`Optional

URL-encoded JSON object containing flexpane metadata from the app that will be conformed to a Work Object metadata schema, keyed by entity ID.

**`user_auth_required`**`boolean`Optional

Set to true (or 1) to indicate that the user must authenticate to view full flexpane data.

_Default:_ `0`

**`user_auth_url`**`string`Optional

A custom URL to which users are directed for authentication if required.

_Example:_ `https://example.com/onboarding?user_id=xxx`

**`error`**Optional

## Usage info {#usage-info}

This method is used to provide custom flexpane behavior for [Work Objects](/messaging/work-objects-overview). Apps call this API method to send per-user flexpane metadata to the client.

Here is an example of what the `metadata` object looks like:

```
{  "entity_type": "slack#/entities/file",  "url": "https://miro.com/app/board/XYZ=/",  "external_ref": {    "id": "XYZ=",  },  "entity_payload": {    "attributes": {      "title": {        "text": "GTM Project Capybara",      },      "display_type": "Miro Board",      "product_name": "Miro"    },    "fields": {      "created_by": {        "value": "Platform Integrations",        "type": "string"      },      "preview": {        "alt_text": "Miro Board image",        "image_url": "https://miro.com/app/images/application/icons/XYZ/540x540/board_icon_5.png?etag=XYZ"      },      "last_modified_by": {        "value": "Platform Integrations",        "type": "string"      },      "date_created": {        "value": 1742923321,      },      "date_updated": {        "value": 1742923333,      },      "file_size": {        "value": "NA"      },      "mime_type": {        "value": "Miro"      }    },    "display_order": ["created_by", "last_modified_by", "date_created", "date_updated", "file_size", "mime_type", "preview"]  }}
```

### Accepted properties for the error object {#accepted-properties-for-the-error-object}

Property

Accepted values

Required/Optional

Description

`actions`

Array of action button objects

optional

Set of action buttons to be shown in case of a specific error.

`custom_message`

string

optional

Used when status is 'custom' to provide a specific message to the client.

`custom_title`

string

optional

Used when status is 'custom' to provide a specific title.

`message_format`

"markdown"

optional

String format for custom message.

`status`

object

String. Can be one of \["restricted", "internal\_error", "not\_found" "custom", "custom\_partial\_view", "timeout", "edit\_error"\]

An error status for why an entity could not be presented.

### Action button schema {#action-button-schema}

Property

Required/Optional

Type

`action_id`

required

string

`accessibility_label`

optional

string

`processing_state`

optional

object

`style`

optional

string, can be one of: \["primary", "danger"\]

`text`

required

string

`url`

optional

string

`value`

options

string

### Processing state object schema {#processing-state-object-schema}

Property

Required/Optional

Type

`enabled`

required

boolean

`interstitial_text`

optional

string

### Enterprise Grid considerations {#enterprise-grid}

When your app receives the [`entity_details_requested`](/reference/events/entity_details_requested) event in an Enterprise Grid context, the check to see whether the user has connected their Slack and third party accounts can be workspace agnostic, and does not need to rely on the `team_id` sent in the [`entity_details_requested`](/reference/events/entity_details_requested) event. This is because Slack user IDs are globally unique, and the flexpane is not scoped to a team. As such, as long as the Slack user ID is associated to a user in the app's service, that should be enough to determine whether the user has a connected account.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_auth"}
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

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`entity_metadata_does_not_match_trigger`

The provided entity's ID does not match the ID of the entity used to initiate the request

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

temporarily gating API

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_app_id`

App ID is not a valid format

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Invalid token provided

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_metadata`

The provided `metadata` argument could not be parsed or understood.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_trigger_id`

Trigger id is not valid

`method_deprecated`

The method has been deprecated.

`missing_interactivity_url`

App does not have an interactivity URL configured

`missing_options_load_url`

App does not have an options load URL configured

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

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

`user_auth_url_missing`

User auth url is required if user\_auth\_required is true