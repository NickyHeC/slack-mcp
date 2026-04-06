Source: https://docs.slack.dev/reference/methods/team.externalTeams.disconnect

# team.externalTeams.disconnect method

DocsCall generator

## Facts {#facts}

**Description**Disconnect an external organization.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/team.externalTeams.disconnect
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.team.externalTeams.disconnect
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.team_externalTeams_disconnect
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().teamExternalTeamsDisconnect
```

**Scopes**

Bot token:

[`conversations.connect:manage`](/reference/scopes/conversations.connect.manage)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 1: 1+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`target_team`**Required

The team ID of the target team.

_Example:_ `T726G27TT`

## Usage info {#usage-info}

This method disconnects [Slack Connect](https://slack.com/help/articles/115004151203-Slack-Connect-guide--work-with-external-organizations) channels and direct messages (DMs) from an organization to end all communication with them. Disconnecting from an organization ends all communication, but depending on permissions, still allows access to conversation history. Refer to [this help center article](https://slack.com/help/articles/360063030933-Slack-Connect--Disconnect-from-an-organization-#:~:text=Below%20Administration%20in%20the%20left,%5D%2C%20then%20Disconnect%20to%20confirm) for the expected behavior of disconnecting a channel, MPDM, or DM.

Example request:

```
{  "target_team": "T123ABCDEF"}
```

Note that the disconnect process occurs in the background and may take some time to complete.

### Use cases {#use-cases}

This method may be useful for:

*   Automating compliance—automatically disconnect from organizations that no longer meet your compliance or security standards.
    
*   Streamlining management—integrate disconnection into on-boarding/off-boarding processes for seamless management of external collaborations.
    
*   Routine maintenance—schedule regular audits and disconnections as part of your organization's routine maintenance tasks.
    

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

`invalid_target_team`

target team is invalid

`method_deprecated`

The method has been deprecated.

`missing_argument`

A required argument is missing.

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

`restricted_action`

The actor is restricted from archiving or disconnecting.

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