Source: https://docs.slack.dev/reference/methods/views.push

# views.push method

DocsCall generator

## Facts {#facts}

**Description**Push a view onto the stack of a root view.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/views.push
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.views.push
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.views_push
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().viewsPush
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 4: 100+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`view`**Required

A [view payload](/reference/views). This must be a JSON-encoded string.

### Optional arguments

**`trigger_id`**Optional

Exchange a trigger to post to the user.

_Example:_ `12345.98765.abcd2358fdea`

**`interactivity_pointer`**Optional

Exchange an interactivity pointer to post to the user.

_Example:_ `12345.98765.abcd2358fdea`

## Usage info {#usage-info}

Push a new view onto the existing view stack by passing a view object and a valid `trigger_id` generated from an interaction within the existing modal. The pushed view is added to the top of the stack, so the user will go back to the previous view after they complete or cancel the pushed view.

After a modal is opened, the app is limited to pushing 2 additional views.

Read the [modals](/block-kit#adding_blocks) documentation to learn more about the lifecycle and intricacies of views.

* * *

## Response {#response}

#### Typical success response includes the pushed view payload.

```
{  "ok": true,  "view": {    "id": "VNM522E2U",    "team_id": "T9M4RL1JM",    "type": "modal",    "title": {      "type": "plain_text",      "text": "Pushed Modal",      "emoji": true    },    "close": {      "type": "plain_text",      "text": "Back",      "emoji": true    },    "submit": {      "type": "plain_text",      "text": "Save",      "emoji": true    },    "blocks": [      {        "type": "input",        "block_id": "edit_details",        "element": {          "type": "plain_text_input",          "action_id": "detail_input"        },        "label": {          "type": "plain_text",          "text": "Edit details"        }      }    ],    "private_metadata": "",    "callback_id": "view_4",    "external_id": "",    "state": {      "values": {}    },    "hash": "1569362015.55b5e41b",    "clear_on_close": true,    "notify_on_close": false,    "root_view_id": "VNN729E3U",    "previous_view_id": null,    "app_id": "AAD3351BQ",    "bot_id": "BADF7A34H"  }}
```

#### Typical error response.

```
{  "ok": false,  "error": "invalid_arguments",  "response_metadata": {    "messages": [      "missing required field: title"    ]  }}
```

If you pass a valid view object along with a valid `trigger_id`, you'll receive a success response with the view object that was pushed to the stack.

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

`duplicate_external_id`

Error returned when the given `external_id` has already be used.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`exchanged_trigger_id`

The trigger\_id was already exchanged in a previous call.

`expired_trigger_id`

The trigger\_id is expired.

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

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_trigger_id`

The trigger\_id is invalid. The expected format for the trigger\_id argument is "132456.7890123.abcdef".

`method_deprecated`

The method has been deprecated.

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

`not_found`

Error returned when the requested view can't be found.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`push_limit_reached`

Error returned when the max push limit has been reached for views. Currently the limit is 3.

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

`view_too_large`

Error returned if the provided view is greater than 250kb.