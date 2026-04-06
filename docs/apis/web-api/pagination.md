Source: https://docs.slack.dev/apis/web-api/pagination

# Pagination

Throughout the Slack platform, you'll encounter collections of _things_. Lists of users. Arrays of channels. A pride of lion emoji.

When you call an [API method](/reference/methods) to retrieve most of these collections, they're returned to you in portions. Check out more detail below on pagination in API methods, including how to use them and which methods follow the pattern.

Most methods that support pagination use a cursor-based approach. However, some older methods use varied versions of pagination.

The individual documentation for each API method is your source of truth for which pattern the method follows.

## Cursor-based pagination {#cursors}

For larger collections like channel and user lists, Slack API methods return results using a cursor-based approach.

Cursors are like pointers. Pointers point at things: they reference a specific iota, a place in the list where your last request left off. They help avoid loading an entire set just to give you a slice.

A cursor-paginated method returns two things: a portion of the total set of results, and a **cursor** that points to the next portion of the results.

Cursor-based pagination is spreading across the platform quickly and is mandatory on some methods.

Please paginate along with us.

### Just the facts {#facts}

*   Cursor-paginated methods accept `cursor` and `limit` parameters.
*   If you don't pass a `cursor` parameter, but **do** pass a `limit` parameter, the default value retrieves the first portion (or "page") of results.
*   Paginated responses include a top-level `response_metadata` object that includes a `next_cursor` _when there are additional results to be retrieved_.
*   On your next call to the same method, set the `cursor` parameter equal to the `next_cursor` value you received on the last request to retrieve the next portion of the collection.
*   An empty, null, or non-existent `next_cursor` in the response indicates no further results.
*   The `limit` parameter sets a _maximum_ number of results to return per call.
*   Provide sensible `limit` values. We recommend `100`\-`200` results at a time.
*   The `limit` parameter maximum is `1000` and subject to change and may vary per method.
*   It's possible to receive _fewer_ results than your specified `limit`, even when there are additional results to retrieve. Avoid the temptation to check the size of results against the limit to conclude the results have been completely returned. Instead, check the `next_cursor` value in the `response_metadata` object to make sure that it's empty, null, or non-existent.

### Walkthrough {#walkthrough}

When accessing the first virtual page of a paginated collection — for instance making a [`users.list`](/reference/methods/users.list) request for the first time — you'll receive a `response_metadata` attribute containing a cursor for your next request.

Here's an example request to `users.list`, where we limit our list of users to `2` users per "page", making it easier to test on a workspace with a low number of users.

```
GET https://slack.com/api/users.list?limit=2Authorization: Bearer xoxb-1234-5678-90123
```

In return, we get our typical `users.list` response, limited to `2` results. Skip down to the bottom to see the `response_metadata`, containing cursor information on the next page of results.

```
{    "ok": true,    "members": [        {            "id": "USLACKBOT",            "team_id": "T0123ABC456",            "name": "slackbot",            "deleted": false,            "color": "757575",            "real_name": "slackbot",            "tz": null,            "tz_label": "Pacific Daylight Time",            "tz_offset": -25200,            "profile": {                "first_name": "slackbot",                "last_name": "",                "image_24": "https:\/\/a.slack-edge.com...png",                "image_32": "https:\/\/a.slack-edge.com...png",                "image_48": "https:\/\/a.slack-edge.com...png",                "image_72": "https:\/\/a.slack-edge.com...png",                "image_192": "https:\/\/a.slack-edge.com...png",                "image_512": "https:\/\/a.slack-edge.com...png",                "avatar_hash": "sv1444671949",                "always_active": true,                "real_name": "slackbot",                "real_name_normalized": "slackbot",                "fields": null            },            "is_admin": false,            "is_owner": false,            "is_primary_owner": false,            "is_restricted": false,            "is_ultra_restricted": false,            "is_bot": false,            "updated": 0        },        {            "id": "W0123ABC456",            "team_id": "T0123ABC456",            "name": "glinda",            "deleted": false,            "color": "9f69e7",            "real_name": "Glinda Southgood",            "tz": "America\/Los_Angeles",            "tz_label": "Pacific Daylight Time",            "tz_offset": -25200,            "profile": {                "avatar_hash": "8fbdd10b41c6",                "image_24": "https:\/\/a.slack-edge.com...png",                "image_32": "https:\/\/a.slack-edge.com...png",                "image_48": "https:\/\/a.slack-edge.com...png",                "image_72": "https:\/\/a.slack-edge.com...png",                "image_192": "https:\/\/a.slack-edge.com...png",                "image_512": "https:\/\/a.slack-edge.com...png",                "image_1024": "https:\/\/a.slack-edge.com...png",                "image_original": "https:\/\/a.slack-edge.com...png",                "first_name": "Glinda",                "last_name": "Southgood",                "title": "Glinda the Good",                "phone": "",                "skype": "",                "real_name": "Glinda Southgood",                "real_name_normalized": "Glinda Southgood",                "email": "glenda@south.oz.coven"            },            "is_admin": true,            "is_owner": true,            "is_primary_owner": true,            "is_restricted": false,            "is_ultra_restricted": false,            "is_bot": false,            "updated": 1480527098,            "has_2fa": false        }    ],    "cache_ts": 1498777272,    "response_metadata": {        "next_cursor": "dXNlcjpVMEc5V0ZYTlo="    }}
```

Within `response_metadata` you'll note `next_cursor`, a string pointing at the next page of results. To retrieve the next page of results, provide this value as the `cursor` parameter to the paginated method.

Cursor strings typically end with the `=` character

When presenting this value as a URL or POST parameter, it _must_ be encoded as `%3D`.

We issue our request for the next page of no more than 2 results like this:

```
GET https://slack.com/api/users.list?limit=2&cursor=dXNlcjpVMEc5V0ZYTlo%3DAuthorization: Bearer xoxb-1234-5678-90123
```

And (_spoiler alert_): we only get one result back. This workspace actually only has three users. We've reached the end of our pagination journey and there are no more results to retrieve. Our `next_cursor` becomes but an empty string:

```
{    "ok": true    "members": [        // that one last member    ],    "cache_ts": 1498777272,    "response_metadata": {        "next_cursor": ""    }}
```

You'll know that there are no further results to retrieve when a `next_cursor` field contains an empty string (`""`). You're not even paginating at all if you receive no `response_metadata` or its `next_cursor` value.

Cursors expire and are meant to be used within a reasonable amount of time. You should have no trouble pausing between [rate limiting](/apis/web-api/rate-limits) windows, but do not persist cursors for hours or days.

Enhanced rate limiting conditions are provided when using cursor-based pagination.

### Error conditions {#errors}

Currently, the only error specific to pagination that you might encounter is:

*   `invalid_cursor` - Returned when navigating a paginated collection and providing a `cursor` value that just does not compute — either it's gibberish, somehow encoded wrong, or of too great a vintage.

Invalid `limit` values are currently magically adjusted to something sensible. We recommend providing reasonable values for best results, as with most parameters.

### Methods supporting cursor-based pagination {#methods}

We're adding cursor-based pagination to almost every collection-yielding method.

Today, cursor-based pagination is supported by these methods:

*   [`conversations.history`](/reference/methods/conversations.history)
*   [`conversations.list`](/reference/methods/conversations.list)
*   [`conversations.members`](/reference/methods/conversations.members)
*   [`conversations.replies`](/reference/methods/conversations.replies)
*   [`files.info`](/reference/methods/files.info)
*   [`reactions.list`](/reference/methods/reactions.list)
*   [`stars.list`](/reference/methods/stars.list)
*   [`users.list`](/reference/methods/users.list)
*   `groups.list` (_deprecated_)
*   `im.list` (_deprecated_)
*   `mpim.list` (_deprecated_)

* * *

## Classic pagination {#classic}

You'll find a variety of other _pseudo_ and _real_ pagination schemes through a few other Web API methods.

Each of those API methods detail their pagination strategy.

### Timeline methods {#timeline}

These methods are more positional than page oriented and allow you to navigate through time with `oldest`, `latest`, and a special `inclusive` parameter.

They're all deprecated too!

*   `channels.history`
*   `groups.history`
*   `im.history`
*   `mpim.history`

### Traditional paging {#traditional-paging}

These methods use some form of archaic numeric-based `page` and `count` or other limiting parameters.

*   [`files.list`](/reference/methods/files.list)
*   [`search.all`](/reference/methods/search.all)
*   [`search.files`](/reference/methods/search.files)
*   [`search.messages`](/reference/methods/search.messages)