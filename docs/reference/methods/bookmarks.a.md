Source: https://docs.slack.dev/reference/methods/bookmarks.add

# bookmarks.add method

DocsCall generator

## Facts {#facts}

**Description**Add bookmark to a channel.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/bookmarks.add
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.bookmarks.add
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.bookmarks_add
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().bookmarksAdd
```

**Scopes**

Bot token:

[`bookmarks:write`](/reference/scopes/bookmarks.write)

User token:

[`bookmarks:write`](/reference/scopes/bookmarks.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 2: 20+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`channel_id`**`string`Required

Channel to add bookmark in.

**`title`**`string`Required

Title for the bookmark.

**`type`**`string`Required

Type of the bookmark i.e link.

### Optional arguments

**`link`**`string`Optional

Link to bookmark.

**`emoji`**`string`Optional

Emoji tag to apply to the link.

**`entity_id`**`string`Optional

ID of the entity being bookmarked. Only applies to message and file types.

**`access_level`**`string`Optional

The level that we are setting the file's permission to (read or write)

_Acceptable values:_ `read` `write`

**`parent_id`**`string`Optional

Id of this bookmark's parent

## Usage info {#usage-info}

Add bookmark to a channel.

This API method can add bookmarked resources to conversations.

Conversations are limited to **100** bookmarks.

Bookmarks can contain external links as well as internal resources such as messages, files, or other channels within Slack. These resources are readily available in the header of the Slack client near pinned messages.

![Bookmarks in channel screenshot](/assets/images/bookmarks_screenshot-df68a338f525c8d880f44cf08bc6ac61.png)

The [bookmarks.add](/reference/methods/bookmarks.add) method currently accepts the following types:

*   `link`

Bookmarking a `link` requires: `channel_id`, `title`, `type`, and a `url`:

```
https://slack.com/api/bookmarks.add?channel_id=C123TGZ4XYX&title=bookmark-example&type=link&link=http%3A%2F%2Fslack.com
```

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "bookmark": {    "id": "Bk033XFJ9BTJ",    "channel_id": "C1RQ000",    "title": "bookmark-1",    "link": "https://google.com",    "emoji": ":clap:",    "icon_url": "https://www.google.com/favicon.ico",    "type": "link",    "entity_id": null,    "date_created": 1644956055,    "date_updated": 0,    "rank": "g",    "last_updated_by_user_id": "U0334B6G6G5",    "last_updated_by_team_id": "T018DF03GHY",    "shortcut_id": null,    "app_id": null  }}
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

Actor lacks access to the requested resource.

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`cannot_bookmark_from_external_org`

File is an external file and cannot be bookmarked.

`cannot_bookmark_restricted_sharing_enabled`

File has restricted sharing enabled and cannot be bookmarked.

`channel_not_found`

Channel cannot be found.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`file_already_added`

The file has already been added to the folder.

`file_not_found`

File cannot be found.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_app_action_type`

App action type is not valid.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_bookmark_type`

Bookmark type is not valid.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_child_type`

Child type is not valid.

`invalid_emoji`

Invalid emoji, does not follow the pattern of a valid emoji name.

`invalid_entity_id`

Invalid entity\_id, file or message type bookmark should have original file or message ID.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_link`

Invalid link, link should begin with either http:// or https://.

`invalid_parent_type`

Parent type is not valid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_shortcut_type`

Shortcut type is not valid.

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

bookmarking not available for the user.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`parent_bookmark_disabled`

Parent bookmark feature flag is off.

`parent_with_link`

Parent bookmark should not have link.

`permission_denied`

No permission to perform this operation.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`slack_connect_blocked_file_type`

Files with certain extensions are blocked from being uploaded in all Slack Connect communications

`slack_connect_clip_sharing_blocked`

Admin has disabled Clip sharing in Slack Connect channels

`slack_connect_file_upload_sharing_blocked`

Admin has disabled File uploads in all Slack Connect communications

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`too_many_bookmarks`

Bookmark limit reached for channel.

`too_many_tabs`

tab limit reached for channel.

`two_factor_setup_required`

Two factor setup is required.