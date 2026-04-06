Source: https://docs.slack.dev/reference/methods/chat.unfurl

# chat.unfurl method

DocsCall generator

## Facts {#facts}

**Description**Provide custom unfurl behavior for user-posted URLs

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/chat.unfurl
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.chat.unfurl
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.chat_unfurl
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().chatUnfurl
```

**Scopes**

Bot token:

[`links:write`](/reference/scopes/links.write)

User token:

[`links:write`](/reference/scopes/links.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`channel`**`string`Optional

Channel ID of the message. Both `channel` and `ts` must be provided together, _or_ `unfurl_id` and `source` must be provided together.

**`ts`**`string`Optional

Timestamp of the message to add unfurl behavior to.

**`unfurls`**`string`Optional

URL-encoded JSON map with keys set to URLs featured in the the message, pointing to their unfurl blocks or message attachments. Either `unfurls` or `metadata` must be provided.

**`user_auth_message`**Optional

Provide a simply-formatted string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior. Provides two buttons, `Not now` or `Never ask me again`.

**`user_auth_required`**`boolean`Optional

Set to `true` or `1` to indicate the user must install your Slack app to trigger unfurls for this domain

_Default:_ `0`

**`user_auth_url`**Optional

Send users to this custom URL where they will complete authentication in your app to fully trigger unfurling. Value should be properly URL-encoded.

_Example:_ `https://example.com/onboarding?user_id=xxx`

**`user_auth_blocks`**Optional

Provide a JSON based array of structured blocks presented as URL-encoded string to send as an ephemeral message to the user as invitation to authenticate further and enable full unfurling behavior

**`unfurl_id`**`string`Optional

The ID of the link to unfurl. Both `unfurl_id` and `source` must be provided together, _or_ `channel` and `ts` must be provided together.

_Example:_ `Uxxxxxxx-909b5454-75f8-4ac4-b325-1b40e230bbd8`

**`source`**`string`Optional

The source of the link to unfurl. The source may either be `composer`, when the link is inside the message composer, or `conversations_history`, when the link has been posted to a conversation.

_Acceptable values:_ `composer` `conversations_history`

_Example:_ `composer`

**`metadata`**Optional

JSON object with an entities field providing an array of Work Object entities. Either unfurls or metadata must be provided.

## Usage info {#usage-info}

This method [unfurls](/messaging/unfurling-links-in-messages#slack_app_unfurling) a link—either in the message composer or in a posted message.

Ensure that the `links:write` scope is added to your [**app settings**](https://api.slack.com/apps) for apps that will be performing app unfurling.

This method supports both granular bot and user tokens. The bot token is recommended.

Both `unfurl_id` and `source` must be provided together, _or_ `channel` and `ts` must be provided together.

The first time this method is executed with a particular `ts` and `channel` (or `unfurl_id` and `source`) combination, the valid `unfurls` attachments you provide will be attached to the message. Subsequent attempts with the same `ts` and `channel` values will modify the same attachments, rather than adding more.

The `ts` value you supply must correspond to a message in the specified `channel`. Also, the message must contain a fully-qualified URL pointing to a domain that is already registered and associated with your Slack app.

The `user_auth_required` parameter is optional. By providing a `1` or `true` value, it will require the user posting the link first authenticate themselves with your app. See also the [authenticated unfurling docs](/messaging/unfurling-links-in-messages#authenticated_unfurls).

If you'd rather directly point users to a specific page on your server to authenticate, pass a valid URL using the `user_auth_url` parameter. When sending this parameter via `application/x-www-form-urlencoded` GETs or POSTs, values must be URL-encoded such that `https://example.com/onboarding?user_id=xxx` becomes `https%3A%2F%2Fexample.com%2Fonboarding%3Fuser_id%3Dxxx`.

Or, you can send an ephemeral message to that user by providing a simple string-based `user_auth_message` value or JSON array of blocks using `user_auth_blocks`. [Simple slack message formatting](/messaging/formatting-message-text) like `*bold*`, `_italics_`, and linking is supported, so you can wrap your custom URLs in a blanket of situationally accurate, actionable text.

`user_auth_message` offers two default buttons, `Not now` and `Never ask me again` which allows your app to prompt a user multiple times before opting out of an install. To make your ephemeral message extra fancy, you can also use `user_auth_blocks` which will override the default buttons. Using both properties shows the `user_auth_message` in a notification and the `user_auth_blocks` in the ephemeral message.

Specifying `user_auth_url` or `user_auth_message` will automatically imply `user_auth_required` being set to `true`. If both `user_auth_url` and `user_auth_message` are provided, `user_auth_message` takes precedence.

### The unfurls parameter {#unfurls}

The `unfurls` parameter expects a URL-encoded string of JSON. Unlike [`chat.postMessage`](/reference/methods/chat.postMessage)'s `attachments` parameter, it does not expect a JSON array but instead, a hash keyed on the specific URLs you're offering an unfurl for. Each URL can have a [single attachment](/messaging/formatting-message-text), including message buttons.

You can define your own preview for a link that you're unfurling inside the message composer by passing the `preview` field:

```
"unfurls": {  "https://example.com": {    "blocks": [...],    "preview": {        "title": {          "type": "plain_text",          "text": "custom preview"        },        "icon_url":          "https://images.pexels.com/photos/774731/pexels-photo-774731.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"      }    }}
```

This `preview` field is optional, however, if `preview` and `title` are not provided, Canvas app unfurls will be unable to render title text. In the absence of `preview` for uses outside of Canvas, we will generate the preview based on the blocks layout or legacy attachment. If the preview is provided in an unfurl for a **posted message**, rather than a link inside the message composer, we will simply ignore this property.

Read the [unfurling](/messaging/unfurling-links-in-messages#slack_app_unfurling) docs for [more guidance](/messaging/unfurling-links-in-messages#unfurls_parameter) on this parameter.

For use specifically with a file unfurl, you can set the `hide_color` field to `true` to remove the color bar from a message as in the following example:

```
"unfurls": {  "https://example.com": {    "hide_color": true,    "blocks": [{      "type": "file",      "external_id": "ABCD1",      "source": "remote",    }]  }}
```

This property works only with a file block; if this property is included along with other blocks (for example, a section block), this method will throw an error.

### The metadata parameter {#metadata}

The `metadata` parameter expects a JSON object with `entity_type` and `entity_payload` fields, presented as a URL-encoded string. Either `unfurls` or `metadata` must be provided. Slack uses this parameter to generate a Work Object representing the resource your app is unfurling. The JSON schema of the parameter is found below:

```
"metadata": {  "entities": [    {      "app_unfurl_url": "https://example.com/document/123?eid=123456&edit=abcxyz",       // URL posted by the user in a conversation      "url": "https://example.com/document/123",       // URL representing the resource in the third party system      "external_ref": {        "id": "123", // a string ID that uniquely identifies the resource being unfurled        "type": "document" // An optional internal type for entity in the source system.         // Only needed if the ID is not globally unique or needed when retrieving the item.      },      "entity_type": "slack#/entities/file", // entity type      "entity_payload": {}, // entity schema    }  ]}
```

Refer to [Work Objects](/messaging/work-objects-overview) for more details.

* * *

## Response {#response}

#### Typical, minimal success response

```
{  "ok": true}
```

#### Typical error response

```
{  "ok": false,  "error": "cannot_unfurl_url"}
```

As you can see, we provide a minimal positive response when your unfurl attempt is successful. When it is not, you'll receive one of the [errors](#errors) below and `ok` will be `false`.

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

`cannot_auth_user`

The current user cannot be authenticated.

`cannot_find_channel`

The specified channel could not be located for this token.

`cannot_find_message`

The `ts` value in the request does not match a message.

`cannot_find_service`

A record of your app being allowed to unfurl for this workspace could not be found.

`cannot_parse_attachment`

The provided `unfurls` argument could not be parsed or understood.

`cannot_prompt`

The current user has already interacted with and dismissed a prompt for this application.

`cannot_unfurl_message`

The URL cannot be unfurled because the URL provided does not appear in the message.

`cannot_unfurl_url`

The URL cannot be unfurled. This error may be returned if you haven't acknowledged a `link_shared` event tied to the same URL. It is also returned when the domain appears in a workspace's administrative blocklists.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`error_processing_metadata`

The metadata parameter was invalid.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

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

`invalid_metadata_format`

The `metadata` parameter cannot be JSON-decoded into the expected format.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_source`

The unfurl source is invalid.

`invalid_unfurl_id`

The unfurl ID is invalid.

`invalid_unfurls_format`

The `unfurls` parameter cannot be JSON-decoded into a map of URLs to attachments.

`method_deprecated`

The method has been deprecated.

`missing_channel`

The request is missing the `channel` parameter

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`missing_source`

The request is missing the `source` parameter.

`missing_ts`

The request is missing the `ts` parameter

`missing_unfurl_id`

The request is missing the `unfurl_id` parameter.

`missing_unfurls`

The request is missing the `unfurls` parameter.

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