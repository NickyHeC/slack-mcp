Source: https://docs.slack.dev/reference/methods/conversations.requestSharedInvite.list

# conversations.requestSharedInvite.list method

DocsCall generator

## Facts {#facts}

**Description**Lists requests to add external users to channels with ability to filter.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/conversations.requestSharedInvite.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.conversations.requestSharedInvite.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.conversations_requestSharedInvite_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().conversationsRequestSharedInviteList
```

**Scopes**

Bot token:

[`conversations.connect:manage`](/reference/scopes/conversations.connect.manage)

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

**`user_id`**Optional

Optional filter to return invitation requests for the inviting user.

**`include_expired`**`boolean`Optional

When true expired invitation requests will be returned, otherwise they will be excluded

**`include_approved`**`boolean`Optional

When true approved invitation requests will be returned, otherwise they will be excluded

**`include_denied`**`boolean`Optional

When true denied invitation requests will be returned, otherwise they will be excluded

**`invite_ids`**`array`Optional

An optional list of invitation ids to look up

**`limit`**`integer`Optional

The number of items to return. Must be between 1 - 1000 (inclusive).

_Default:_ `200`

**`cursor`**`string`Optional

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. See [pagination](/apis/web-api/pagination) for more detail.

_Example:_ `bG9nX2lkOjc5NjQ1NA==`

## Usage info {#usage-info}

This [Slack Connect API](/apis/slack-connect/using-slack-connect-api-methods) method lists requested [Slack Connect invitations](/apis/slack-connect/).

### Prerequisites {#prerequisites}

*   You must have administrator access to a workspace that is part of an [Enterprise plan](https://app.slack.com/plans/T01G0063H29).
*   You must have the following settings configured within your Admin Dashboard under **Slack Connect Settings**: a) Toggle on the **Apply automation rules before channel invitations are sent** preference. b) Under **Channels**, toggle on either the **Sending Invitations with Permission to Post Only** or the **Sending Invitations with permission to post, invite and more** preference.

For more details, refer to [governing Slack Connect invites](/tools/deno-slack-sdk/tutorials/governing-slack-connect-invites).

### Using the user_id argument {#using-the-user_id-argument}

The optional `user_id` argument allows the caller to filter requested invitations by a given user.

### Using the include_approved argument {#using-the-include_approved-argument}

The optional `include_approved` argument will return approved requested invitations in the API response. By default approved requested invitations are not returned.

### Using the include_denied argument {#using-the-include_denied-argument}

The optional `include_denied` argument will return denied requested invitations in the API response. By default denied requested invitations are not returned.

### Using the include_expired argument {#using-the-include_expired-argument}

The optional `include_expired` argument will return expired requested invitations in the API response. By default expired requested invitations are not returned.

### Using the invite_ids argument {#using-the-invite_ids-argument}

The optional `invite_ids` will return a list of requested invitations with matching IDs. All other filters are applicable in combination with this filter.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "invite_requests": [    {      "date_last_updated": 1722372331,      "id": "I12345",      "date_created": 1722372331,      "expires_at": 1723581931,      "inviting_team": {        "id": "E12345",        "name": "Acme corp",        "icon": {          "image_34": "https://.../avatar/avatars-teams/ava_0011-34.png",          "image_44": "https://.../avatar/avatars-teams/ava_0011-44.png",          "image_68": "https://.../avatar/avatars-teams/ava_0011-68.png",          "image_88": "https://.../avatar/avatars-teams/ava_0011-88.png",          "image_102": "https://.../avatar/avatars-teams/ava_0011-102.png",          "image_132": "https://.../avatar/avatars-teams/ava_0011-132.png",          "image_230": "https://.../avatar/avatars-teams/ava_0011-230.png",          "image_default": true        },        "avatar_base_url": "https://dev.slack.com/avatarsource/",        "is_verified": false,        "domain": "acme-corp",        "date_created": 1637947110,        "requires_sponsorship": false      },      "inviting_user": {        "id": "U12345",        "team_id": "E12345",        "name": "acme-corp-user",        "updated": 1721741979,        "who_can_share_contact_card": "EVERYONE",        "profile": {          "real_name": "acme-corp-user",          "display_name": "acme-corp-user",          "real_name_normalized": "acme-corp-user",          "display_name_normalized": "acme-corp-user",          "team": "E12345",          "avatar_hash": "hash",          "email": "acme-corp-user@acme-corp.com",          "image_24": "https://secure.gravatar.com/avatar/...0001-24.png",          "image_32": "https://secure.gravatar.com/avatar/...0001-32.png",          "image_48": "https://secure.gravatar.com/avatar/...0001-48.png",          "image_72": "https://secure.gravatar.com/avatar/...0001-72.png",          "image_192": "https://secure.gravatar.com/avatar/...0001-192.png",          "image_512": "https://secure.gravatar.com/avatar/...0001-512.png"        }      },      "is_external_limited": false,      "is_sponsored": true,      "recipient_email": "external-user@other-corp.com",      "target_user": {        "recipient_email": "external-user1@other-corp.com",        "recipient_user_id": "U123456"      }    },    {      "id": "I12345",      "date_created": 1722372331,      "expires_at": 1723581931,      "date_denied": 1723581901,      "inviting_team": {        "id": "E12345",        "name": "Acme Corp.",        "icon": {          "image_34": "https://.../avatars-teams/ava_0011-34.png",          "image_44": "https://.../avatars-teams/ava_0011-44.png",          "image_68": "https://.../avatars-teams/ava_0011-68.png",          "image_88": "https://.../avatars-teams/ava_0011-88.png",          "image_102": "https://.../avatars-teams/ava_0011-102.png",          "image_132": "https://.../avatars-teams/ava_0011-132.png",          "image_230": "https://.../avatars-teams/ava_0011-230.png",          "image_default": true        },        "avatar_base_url": "https://dev.slack.com/avatarsource/",        "is_verified": false,        "domain": "acme-corp",        "date_created": 1637947110,        "requires_sponsorship": false      },      "inviting_user": {        "id": "U12345",        "team_id": "E12345",        "name": "acme-corp-user",        "updated": 1721741979,        "who_can_share_contact_card": "EVERYONE",        "profile": {          "real_name": "acme-corp-user",          "display_name": "acme-corp-user",          "real_name_normalized": "acme-corp-user",          "display_name_normalized": "acme-corp-user",          "team": "E12345",          "avatar_hash": "hash",          "email": "acme-corp-user@acme-corp.com",          "image_24": "https://secure.gravatar.com/avatar/...0001-24.png",          "image_32": "https://secure.gravatar.com/avatar/...0001-32.png",          "image_48": "https://secure.gravatar.com/avatar/...0001-48.png",          "image_72": "https://secure.gravatar.com/avatar/...0001-72.png",          "image_192": "https://secure.gravatar.com/avatar/...0001-192.png",          "image_512": "https://secure.gravatar.com/avatar/...0001-512.png"        }      },      "is_external_limited": false,      "channel": {        "id": "C12345",        "is_im": false,        "is_private": true,        "date_created": 1721764754,        "name": "channel-name",        "connections": [          {            "team": {              "id": "E12345",              "name": "Acme Corp.",              "icon": {                "image_34": "https://.../ava_0011-34.png",                "image_44": "https://.../ava_0011-44.png",                "image_68": "https://.../ava_0011-68.png",                "image_88": "https://.../ava_0011-88.png",                "image_102": "https://.../ava_0011-102.png",                "image_132": "https://.../ava_0011-132.png",                "image_230": "https://.../ava_0011-230.png",                "image_default": true              },              "avatar_base_url": "https://dev.slack.com/avatarsource/",              "is_verified": false,              "domain": "acme-corp",              "date_created": 1637947110,              "requires_sponsorship": false            },            "is_private": true          }        ],        "pending_connections": [],        "previous_connections": []      },      "target_user": {        "recipient_email": "external-user@other-corp.com"      },      "reviewing_user": {        "id": "U12345",        "team_id": "E12345",        "name": "acme-corp-user",        "updated": 1721741979,        "who_can_share_contact_card": "EVERYONE",        "profile": {          "real_name": "acme-corp-user",          "display_name": "acme-corp-user",          "real_name_normalized": "acme-corp-user",          "display_name_normalized": "acme-corp-user",          "team": "E12345",          "avatar_hash": "hash",          "email": "acme-corp-user@acme-corp.com",          "image_24": "https://secure.gravatar.com/avatar/...0001-24.png",          "image_32": "https://secure.gravatar.com/avatar/...0001-32.png",          "image_48": "https://secure.gravatar.com/avatar/...0001-48.png",          "image_72": "https://secure.gravatar.com/avatar/...0001-72.png",          "image_192": "https://secure.gravatar.com/avatar/...0001-192.png",          "image_512": "https://secure.gravatar.com/avatar/...0001-512.png"        }      }    }  ],  "response_metadata": {    "next_cursor": "aWQ6STAxNkszN0FBQUU="  }}
```

#### Typical error response

```
{  "ok": false,  "error": "invalid_cursor"}
```

Returns a list of [paginated](/apis/web-api/pagination) requested invitations objects ordered by IDs in ascending order.

### Pagination {#pagination}

This method uses cursor-based pagination to make it easier to incrementally collect information. To begin pagination, specify a `limit` value under `1000`. We recommend no more than `200` results at a time.

Responses will include a top-level `response_metadata` attribute containing a `next_cursor` value. By using this value as a `cursor` parameter in a subsequent request, along with `limit`, you may navigate through the collection page by virtual page.

See [pagination](/apis/web-api/pagination) for more information.

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

Something unexpected went wrong.

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

`invalid_cursor`

The provided cursor is not valid.

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

`not_implemented`

its not implemented! TODO: remove me

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_action`

A team preference prevents the user from listing invitation requests.

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