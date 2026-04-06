Source: https://docs.slack.dev/reference/methods/conversations.listConnectInvites

# conversations.listConnectInvites method

DocsCall generator

## Facts {#facts}

**Description**Lists shared channel invites that have been generated or received but have not been approved by all parties

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.listConnectInvites
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.listConnectInvites
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_listConnectInvites
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsListConnectInvites
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

### Optional arguments

**`team_id`**`string`Optional

Encoded team id for the workspace to retrieve invites for, required if org token is used

**`count`**`integer`Optional

Maximum number of invites to return

_Default:_ `100`

**`cursor`**`string`Optional

Set to `next_cursor` returned by previous call to list items in subsequent page

_Example:_ `5c3e53d5`

## Usage info {#usage-info}

This [Slack Connect API](/apis/slack-connect/using-slack-connect-api-methods) method returns information about pending shared channel invites that have been sent or received by a workspace. Pending shared channel invites are invites that have been sent or received by the workspace but have not yet been denied or approved and may turn into shared channels on the team in the future.

This API does not currently return Slack Connect DM invite information.

* * *

## Response {#response}

Returns a [paginated list](/apis/web-api/pagination) of invites that represent pending shared channel invitations.

```
{  "ok": true,  "invites": [    {      "direction": "outgoing",      "status": "sent",      "date_last_updated": 1622591318,      "invite_type": "channel",      "invite": {        "id": "I0139HVDSDQ",        "date_created": 1622591287,        "date_invalid": 1623800887,        "inviting_team": {          "id": "E0ANZNL03",          "name": "oonamole",          "icon": {            ...          },          "is_verified": false,          "domain": "oonamole",          "date_created": 1559335482        },        "inviting_user": {          "id": "W0ANZNNAX",          "team_id": "E0ANZNL03",          "name": "ben_boss",          "updated": 1616521338,          "profile": {            "real_name": "Puppy InCharge",            "display_name": "puppy_incharge",            "real_name_normalized": "Puppy InCharge",            "display_name_normalized": "puppy_incharge",            "team": "E0ANZNL03",            "avatar_hash": "g767309df8c3",            "email": "puppyincharge@slack.com",            "image_24": "...",            "image_32": "...",            "image_48": "...",            "image_72": "...",            "image_192": "...",            "image_512": "..."          }        },        "link": "..."      },      "channel": {        "id": "C013AGH1GBD",        "is_private": false,        "is_im": false,        "name": "pb-shared-7"      },      "acceptances": [        {          "approval_status": "pending_approval",          "date_accepted": 1622591318,          "date_invalid": 1623800918,          "date_last_updated": 1622591318,          "accepting_team": {            "id": "T0PP93X0Q",            "name": "Doughboy",            "icon": {              ...            },            "is_verified": false,            "domain": "doughboy",            "date_created": 1521573656          },          "accepting_user": {            "id": "U0PP93X1N",            "team_id": "T0PP93X0Q",            "name": "bredman",            "updated": 1619479454,            "profile": {              "real_name": "Brent Doodle",              "display_name": "Brent Doodle",              "real_name_normalized": "Brent",              "display_name_normalized": "Brent Doodle",              "team": "T0PP93X0Q",              "avatar_hash": "ge2de9bb3fde",              "email": "bdoodle@slack.com",              "image_24": "...",              "image_32": "...",              "image_48": "...",              "image_72": "...",              "image_192": "...",              "image_512": "..."            }          },          "reviews": [            {              "type": "approval",              "date_review": 1622591318,              "reviewing_team": {                "id": "T0PP93X0Q",                "name": "Doughboy",                "icon": {                  ...                },                "is_verified": false,                "domain": "doughboy",                "date_created": 1521573656              }            }          ]        }      ]    },    {      "direction": "incoming",      "status": "sent",      "date_last_updated": 1622591697,      "invite_type": "channel",      "invite": {        "id": "I0139HWQ134",        "date_created": 1622591671,        "date_invalid": 1623801271,        "inviting_team": {          "id": "T0PP93X0Q",          "name": "Doughboy",          "icon": {            ...          },          "is_verified": false,          "domain": "doughboy",          "date_created": 1521573656        },        "inviting_user": {          "id": "U0PP93X1N",          "team_id": "T0PP93X0Q",          "name": "bredman",          "updated": 1619479454,          "profile": {            "real_name": "Pet Dog",            "display_name": "Pet Dog",            "real_name_normalized": "Pet Dog",            "display_name_normalized": "Pet Dog",            "team": "T0PP93X0Q",            "avatar_hash": "ge2de9bb3fde",            "email": "bront@slack.com",            "image_24": "...",            "image_32": "...",            "image_48": "...",            "image_72": "...",            "image_192": "...",            "image_512": "..."          }        },        "link": "..."      },      "channel": {        "id": "C013AGJCG9H",        "is_private": false,        "is_im": false,        "name": "shared-channel-72"      },      "acceptances": [        {          "approval_status": "pending_approval",          "date_accepted": 1622591697,          "date_invalid": 1623801297,          "date_last_updated": 1622591697,          "accepting_team": {            "id": "E0ANZNL03",            "name": "oonamole",            "icon": {              ...            },            "is_verified": false,            "domain": "oonamole",            "date_created": 1559335482          },          "accepting_user": {            "id": "W0ANZNNAX",            "team_id": "E0ANZNL03",            "name": "ben_boss",            "updated": 1616521338,            "profile": {              "real_name": "Brent Puppies",              "display_name": "Bront",              "real_name_normalized": "Brent Puppies",              "display_name_normalized": "brent_puppies",              "team": "E0ANZNL03",              "avatar_hash": "g767309df8c3",              "email": "brent@slack.com",              "image_24": "...",              "image_32": "...",              "image_48": "...",              "image_72": "...",              "image_192": "...",              "image_512": "..."            }          },          "reviews": [            {              "type": "approval",              "date_review": 1622591697,              "reviewing_team": {                "id": "E0ANZNL03",                "name": "oonamole",                "icon": {                  ...                },                "is_verified": false,                "domain": "oonamole",                "date_created": 1559335482              }            }          ]        }      ]    }  ]}
```

Some fields in the response, like `unread_count` and `unread_count_display`, are included for DM conversations only.

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

An invalid argument was supplied to the method.

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

`restricted_action`

A team preference prevents the authenticated user from viewing shared channel invites.

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