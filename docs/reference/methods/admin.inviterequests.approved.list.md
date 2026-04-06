Source: https://docs.slack.dev/reference/methods/admin.inviteRequests.approved.list

# admin.inviteRequests.approved.list method

DocsCall generator

## Facts {#facts}

**Description**List all approved workspace invite requests.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.inviteRequests.approved.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.inviteRequests.approved.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_inviteRequests_approved_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminInviteRequestsApprovedList
```

**Scopes**

User token:

[`admin.invites:read`](/reference/scopes/admin.invites.read)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`team_id`**`string`Optional

ID for the workspace where the invite requests were made.

**`cursor`**`string`Optional

Value of the `next_cursor` field sent as part of the previous API response

_Example:_ `5cweb43`

**`limit`**`integer`Optional

The number of results that will be returned by the API on each invocation. Must be between 1 - 1000, both inclusive

_Default:_ `100`

_Example:_ `100`

## Usage info {#usage-info}

This [invite request management API](/admins/managing-invite-requests) method lists workspace invite requests that have already been approved.

This method requires an `admin.*` scope. It's obtained through the normal [OAuth process](/authentication), but there are a few additional requirements. The scope must be requested by an [Enterprise org](/enterprise) admin or owner, and the OAuth install must take place on the entire Enterprise org, not an individual workspace. See the [`admin.invites:read` page](/reference/scopes/admin.invites.read) for more detailed instructions.

`team_id` is **required** if your Enterprise org contains more than one workspace.

* * *

## Response {#response}

```
    {        "ok": true,        "approved_requests": [            [                "invite_request": [                    "id": "IrNKPK5TK3",                    "email": "foo@example.com",                    "date_created": "1616127454"                    "requester_ids": [                        "UNKPK5TJM"                    ],                    "channel_ids": [                        "CNKPK5TJW",                        "CNKPK5TJH"                    ],                    "invite_type": "full_member",                    "real_name": null,                    "date_expire": null,                    "request_reason" null                ],                "approved_by": [                    "actor_id": "UNKPK5TJB",                    "actor_type": "user"                ],                "invite": [                    "id": "INKPK5TK4",                    "inviter_id": "UNKPK5TJM",                    "email": "foo@example.com",                    "date_created": 1616127724,                    "date_resent": null,                    "is_bouncing": false,                    "invite_preferences": [                        "is_restricted": false,                        "is_ultra_restricted": false,                        "date_expire": null,                        "channel_ids": [                            "CNKPK5TJW",                            "CNKPK5TJH"                        ],                        "is_domain_matched": false,                        "real_name": null                    ],                ],            ],              [                "invite_request": [                    "id": "IrNKPK5TG3",                    "email": "foo2@example.com",                    "date_created": "161612723454"                    "requester_ids": [                        "UNKPK5TJK"                    ],                    "channel_ids": [                        "CNKEK5TJS",                        "CNKPK5TJG"                    ],                    "invite_type": "full_member",                    "real_name": null,                    "date_expire": null,                    "request_reason" null                ],                "approved_by": [                    "actor_id": "UNKPK5TJK",                    "actor_type": "user"                ],                "invite": [                    "id": "INKPK5TK4",                    "inviter_id": "UNKPK5TJM",                    "email": "foo2@example.com",                    "date_created": 1616127726,                    "date_resent": null,                    "is_bouncing": false,                    "invite_preferences": [                        "is_restricted": false,                        "is_ultra_restricted": false,                        "date_expire": null,                        "channel_ids": [                            "CNKPK5TJW",                            "CNKPK5TJH"                        ],                        "is_domain_matched": false,                        "real_name": null                    ],                ],            ],          ],    }
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

`feature_not_enabled`

The Invite Requests admin APIs feature is not enabled

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

This token doesn't have the scope required.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_an_admin`

This token doesn't have admin privileges.

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

`team_not_found`

The `team_id` specified wasn't found.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.