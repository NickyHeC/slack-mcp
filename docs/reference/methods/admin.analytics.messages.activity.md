Source: https://docs.slack.dev/reference/methods/admin.analytics.messages.activity

# admin.analytics.messages.activity method

DocsCall generator

## Facts {#facts}

**Description**Retrieves activity metrics for messages from a given channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
GET https://slack.com/api/admin.analytics.messages.activity
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.analytics.messages.activity
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_analytics_messages_activity
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminAnalyticsMessagesActivity
```

**Scopes**

User token:

[`admin.analytics:read`](/reference/scopes/admin.analytics.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel`**`string`Required

Channel ID for channel of the message activity to query.

### Optional arguments

**`oldest_ts`**`string`Optional

Oldest timestamp to include in the results. Defaults to 7 days before current time. If not passed while still passing the `latest_ts` parameter, defaults to 7 days before `latest_ts`.

**`latest_ts`**`string`Optional

Most recent timestamp to include in results. Defaults to current time. If not passed while still passing the `oldest_ts` parameter, defaults to 7 days after `oldest_ts`.

**`cursor`**`string`Optional

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first "page" of the collection.

_Example:_ `abcd...`

**`limit`**`integer`Optional

Maximum number of entries to return. The maximum limit is 100.

_Default:_ `50`

## Usage info {#usage-info}

This Web API method retrieves activity metrics for messages from a given channel.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "message_activities": [    {      "channel_id": "C123ABC456",      "timestamp": "1234567890.123456",      "unique_user_reactions_count": 15,      "unique_user_shares_count": 8,      "unique_user_views_count": 142,      "unique_user_clicks_count": 23,      "unique_views_client": {        "desktop_views_count": 89,        "mobile_views_count": 42,        "web_views_count": 11      },      "unique_stats_by_department": [        {          "department": "Engineering",          "views": 45,          "reactions": 8,          "shares": 3,          "clicks": 12        },        {          "department": "Product",          "views": 32,          "reactions": 4,          "shares": 2,          "clicks": 7        }      ],      "unique_stats_by_org": [        {          "team_id": "T123ABC456",          "views": 98,          "reactions": 12,          "shares": 5,          "clicks": 18        }      ]    }  ],  "response_metadata": {    "next_cursor": "abcd..."  }}
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

`channel_not_found`

The specified channel was not found.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

Required arguments either were not provided or contain invalid values.

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

`not_an_enterprise`

The user token does not belong to an enterprise.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

The token does not have permission to access this resource.

`restricted_plan_level`

The enterprise plan level does not have access to this feature.

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