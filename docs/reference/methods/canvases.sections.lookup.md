Source: https://docs.slack.dev/reference/methods/canvases.sections.lookup

# canvases.sections.lookup method

DocsCall generator

## Facts {#facts}

**Description**Find sections matching the provided criteria

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/canvases.sections.lookup
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.canvases.sections.lookup
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.canvases_sections_lookup
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().canvasesSectionsLookup
```

**Scopes**

Bot token:

[`canvases:read`](/reference/scopes/canvases.read)

User token:

[`canvases:read`](/reference/scopes/canvases.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Auth token with which to authenticate the session

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`canvas_id`**Required

Encoded ID of the canvas

_Example:_ `F1234ABCD`

**`criteria`**Required

Filtering criteria

_Example:_ `{"section_types": ["any_header"], "contains_text": "CAN Report"}`

## Usage info {#usage-info}

This method is used to identify sections within a canvas.

Those identifiers may then be used to edit the section or apply edits relative to that section. Refer to the [`canvases.edit`](/reference/methods/canvases.edit) method for more details.

Different `criteria` may be used in combination to narrow down the targeted section. Sections may be identified by `section_type`, which can be any of the following:

*   `h1`
*   `h2`
*   `h3`
*   `any_header`

For instance, using `"section_types": ["h1"]` in the `criteria` argument will search for all `h1` headings. Alternatively, using `any_header` will return the section IDs of any type of heading in the canvas. This may make more sense when used in combination with text criteria.

Sections may also be identified by the text they contain by using the `contains_text` property. Referencing the example below, this set of criteria will return the section IDs of any heading that is a `h1` or `h2` style and contains the words "Grocery List".

```
{    "canvas_id": "F0166DCSTS7",    "criteria": {        "section_types": ["h1", "h2"],        "contains_text": "Grocery List"    }}
```

Keep in mind, other types of sections exist that are not currently able to be used as a type to filter on. You may discover these when using a query with no section type provided.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "sections": [    {      "id": "temp:C:eBa219af721c664422cb90a52fac"    }  ]}
```

#### Typical error for a canvas that the actor does not have access to

```
{  "ok": false,  "error": "canvas_not_found"}
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

`canvas_deleted`

The canvas you wish to search is not available.

`canvas_disabled_user_team`

Canvas is disabled on user's team.

`canvas_not_found`

The canvas you wish to search for is not available.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

Something went wrong on our end, please try again.

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