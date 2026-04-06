Source: https://docs.slack.dev/reference/methods/assistant.search.context

# assistant.search.context method

DocsCall generator

## Facts {#facts}

**Description**Searches messages, files, channels and users across your Slack organization.

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/assistant.search.context
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.assistant.search.context
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.assistant_search_context
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().assistantSearchContext
```

**Scopes**

Bot token:

[`search:read.files`](/reference/scopes/search.read.files)[`search:read.public`](/reference/scopes/search.read.public)[`search:read.users`](/reference/scopes/search.read.users)

User token:

[`search:read.files`](/reference/scopes/search.read.files)[`search:read.im`](/reference/scopes/search.read.im)[`search:read.mpim`](/reference/scopes/search.read.mpim)[`search:read.private`](/reference/scopes/search.read.private)[`search:read.public`](/reference/scopes/search.read.public)[`search:read.users`](/reference/scopes/search.read.users)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Special rate limits apply.](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`query`**`string`Required

User prompt or search query

_Example:_ `What is project gizmo?`

### Optional arguments

**`action_token`**`string`Optional

Send `action_token` as received in a message event.

_Example:_ `12345.98765.abcd2358fdea`

**`channel_types`**`array`Optional

Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`.

_Default:_ `public_channel`

_Example:_ `public_channel,private_channel`

**`content_types`**`array`Optional

Content types to include, a comma-separated list of any combination of `messages`, `files`, `channels`, `users`.

_Default:_ `messages`

_Example:_ `messages,files`

**`include_bots`**`boolean`Optional

Whether the results should include bots.

_Example:_ `true`

**`include_deleted_users`**`boolean`Optional

Whether to include deleted users in the user search results. Defaults to false.

_Example:_ `false`

**`before`**`integer`Optional

UNIX timestamp filter. If present, filters for results before this date.

_Example:_ `1754670081`

**`after`**`integer`Optional

UNIX timestamp filter. If present, filters for results after this date.

_Example:_ `1754670081`

**`include_context_messages`**`boolean`Optional

Whether to include context messages surrounding the main message result. Defaults to false if unspecified.

_Example:_ `true`

**`context_channel_id`**Optional

Context channel ID to support scoping the search when applicable.

**`cursor`**`string`Optional

The cursor returned by the API. Leave this blank for the first request and use this to get the next page of results.

_Example:_ `asf91j9jfd`

**`limit`**`integer`Optional

Number of results to return, up to a max of 20. Defaults to 20.

_Example:_ `20`

**`sort`**`string`Optional

The field to sort the results by. Defaults to score. Can be one of: score, timestamp.

_Default:_ `score`

_Acceptable values:_ `score` `timestamp`

**`sort_dir`**`string`Optional

The direction to sort the results by. Defaults to desc.

_Default:_ `desc`

_Acceptable values:_ `asc` `desc`

**`include_message_blocks`**`boolean`Optional

Whether to return the message blocks in the response.

**`highlight`**`boolean`Optional

Whether to highlight the search query in the results. Defaults to false if unspecified.

**`term_clauses`**`array`Optional

A list of term clauses. A term clause is a string with search terms. Search results returned will match every term clause specified (i.e., conjunctive normal form).

**`modifiers`**`string`Optional

A string containing only modifiers in the format of `modifier:value`. Search results returned will match the modifier value. For now modifiers only affect term clauses.

_Example:_ `has:pin before:yesterday`

**`include_archived_channels`**`boolean`Optional

Whether to include archived channels in the search results.

**`disable_semantic_search`**`boolean`Optional

Whether to disable semantic search. When true, only keyword-based search is used. Defaults to false.

## Usage info {#usage-info}

This method is used to search messages across your Slack organization when used with an [app using AI features](/ai). Full details on this method's usage are in the [Real-time Search API usage guide](/apis/web-api/real-time-search-api).

The `is_author_bot` field can be used to distinguish bot messages from regular user messages when formatting contextual information to send to an LLM. The `permalink` field provides a permalink to the message. This can be useful to provide to your users in a `sources` list when the app responds to the user in a thread. Sharing sources in the app response is a best practice.

If there are additional pages of results, the API will return a value in the `next_cursor` field; if not, there will be an empty string. Use the value of `next_cursor` to query the API again for subsequent results pages. The API allows a maximum of 20 results per page.

All API calls made using a bot token require an `action_token`. API calls made using a user token do not require an `action_token`. Read more about using the `action_token` [here](/apis/web-api/real-time-search-api/#action-token).

### Contextual messages {#contextual-messages}

The API returns contextual messages for the top search results. Each result includes a `context_messages` object, which contains lists of relevant messages sent before and after the original message.

In some cases, there may be no relevant messages either before or after the original message.

If the original message was part of a thread, the contextual messages will be limited to that thread only.

### Search filters {#search-filters}

By adding channels to the `content_types` parameter, you can search channels by their name.

The same filters that are available in the Slack search bar can also be used with this API. You can view the full list of available filters [here](https://slack.com/help/articles/202528808-Search-in-Slack?_gl=1*vx7n9z*_gcl_aw*R0NMLjE3NTk5NjE0MzUuQ2owS0NRandsNWpIQmhESEFSSXNBQjBZcWp6UkRuS1VzSTlrU3lkaGJvR1hQalNoWUhRUElKY19lZlVBZmVsc2g0SFFUNmxxV2tDSXFaOGFBdEFIRUFMd193Y0I.*_gcl_dc*R0NMLjE3NTk5NjE0MzUuQ2owS0NRandsNWpIQmhESEFSSXNBQjBZcWp6UkRuS1VzSTlrU3lkaGJvR1hQalNoWUhRUElKY19lZlVBZmVsc2g0SFFUNmxxV2tDSXFaOGFBdEFIRUFMd193Y0I.*_gcl_au*MTAxNDEwNzMyLjE3NTg1NTEyNTc.*_ga*Mjk0NjA4Njk0LjE2NjM2MDk0MTU.*_ga_QTJQME5M5D*czE3NjI4OTk2MjEkbzkwNiRnMSR0MTc2MjkwMTQ4NCRqNTgkbDAkaDA.). These filters should be included in the `query` parameter of your request:

```
{  "query": "What is a recipe for banana milkshakes or date milkshakes before:2025-06-30",  "keywords_clauses": [    ["banana", "date"],    ["milkshake"],    ["recipe"]  ],  "channel_types": ["public_channel", "private_channel", "mpim", "im"],  "content_types": ["messages"],}
```

This query retrieves all messages containing the keywords `banana`, `date`, `milkshake`, or `recipe` that were posted in any public or private channel, MPIM or DM before the date June 30, 2025.

Note, when using channel or user filters, enclose the IDs in angle brackets `<>` with the appropriate mention symbol (`#` for channels,`@` for users). Dates used in `before:`, `after:`, `on:`, or `during:` filters should follow the `YYYY-MM-DD` format.

Additionally, the following filters are supported.

Filter

Purpose

Example

`type`

Filter a filetype; see full list of filetypes [here](/reference/objects/file-object#types)

`"query": "type:pdf"`

`types`

Filter multiple filetypes

`"query": "type:pdf,pptx,png"`

`threads`

Filter for messages that are part of a thread; two possible values

`"query": "threads:all"` filters for messages in a thread, regardless of if it's the root message or a thread reply message  
`"query": "threads:replies"` filters for messages that are replies in a thread, not the root message

`has`

Filters for messages that contain one or more of the properties listed in the Example cell

`"query": "has:[link]"` filters for messages with the link provided (you must provide a link as the value of the property)  
`"query": "has:pin"` a message that has been pinned  
`"query": "has:reaction"` a message with a reaction from a user  
`"query": "has:file"` a message with a file attachment  
`"query": "has:[emoji_ref]"` filters for messages containing the emoji reference (you must provide an emoji reference as the value of the property)

`hasmy`

Filters for messages that contain specific emoji reactions from the searching user

`"query": "hasmy:[emoji_ref]"` returns messages where the searching user has reacted with the emoji reference (you must provide an emoji reference as the value of the property)

`is`

Filters for messages that are saved, in a thread, or part of a DM or MPDM

`"query": "is:saved"`  
`"query": "is:thread"`  
`"query": "is:dm"`

`with`

Filters for messages that contain a user

`"query": "with:<@U12345>"` retrieves messages in a DM or MPDM where user `U12345` is a member; retrieves methods in a thread where user `U12345` is a participant

`creator`

Filters for Canvases and Lists that have been created by a user

`"query": "creator:<@U12345>"` returns Canvases and Lists created by user `U12345`

### Search capabilities {#search-capabilities}

The Real-time Search API supports both keyword and semantic retrieval. Semantic search is used when specific conditions are met. Otherwise, the API defaults to keyword-based retrieval.

#### Semantic search {#semantic-search}

Slack AI Search

Semantic search is available only on workspaces within plans that include Slack AI Search. To request a sandbox with this feature, please join the [Slack Developer Program](https://api.slack.com/developer-program) and reach out to the Slack partnerships team.

To verify if a customer workspace has the Slack AI Search feature enabled, you can use the [`assistant.search.info`](/reference/methods/assistant.search.info) method.

Semantic search is triggered when the `query` provided is structured as a natural language question. This includes queries that:

*   Begin with a question word such as what, where, how, etc.
*   End with a question mark (?).

When semantic search is triggered, the API retrieves results that are topically related to the question, even if the exact keywords aren’t present.

Note: Semantic search may introduce higher response latency compared to keyword search.

Examples of valid semantic queries:

*   `What is the status of project koho?`
*   `What did Jennifer say last week about our Q1 goals?`
*   `How many customer inbounds did we receive today?`

If the query does not follow this structure, the API will fall back to keyword search.

Examples of non-semantic queries:

*   `project Koho status`
*   `Q1 goals Jennifer`
*   `customer inbounds today`

Using semantic search, the Real-time Search API will extract the following filters when written in natural language:

*   User mentions
*   Channels
*   Dates
*   File types
*   Keywords

It's important to note that results may vary. The best way to use filters is to specify them explicitly as described in [this section](#search-filters).

#### Keyword search {#keyword-search}

Keyword search is the default mode when:

*   The workspace does not have the Slack AI Search feature enabled, or
*   The query is not phrased as a natural language question

In this mode, results must include the keywords specified in the query. Some key behaviors:

*   Keyword stemming is supported (e.g., "plan" matches "planning")
*   Synonyms are not (e.g., "revenue" will not return results for "profit")
*   Formatting in the query string may interfere with results, so be sure to strip any formatting from the search string before sending to the API

Keyword search will provide the most relevant results based on the search query and the keyword hits. As such, the following are excluded from the results:

*   Results with insufficient keyword matches
*   Non-text files (such as presentation files, image files, etc)
*   Google Drive links (if the Google Drive app is not installed)

## Rate limiting {#rate-limiting}

This method has special [rate limiting](/apis/web-api/rate-limits) conditions. For most teams, the limit is 10+ requests per minute while allowing for occasional bursts of more requests. For larger teams, this limit will be increased up to 400+ requests per minute with a generous burst.

There's an additional user-level limit of 10 requests per minute with burst. This rate limit is specifically designed to support interactive user searches. Sustained usage at or above this rate will hit daily user limits and may result in rate limiting errors.

It's important that you optimize for calling this less than 10 times for a user inquiry; you will quickly be rate limited for the user and potentially the entire workspace if you attempt consistently make more calls.

**Important:** Paginated requests (such as fetching additional search results via cursors) count toward this rate limit.

When using the [`conversations.history`](/reference/methods/conversations.history) method and the [`conversations.replies`](/reference/methods/conversations.replies) method to supplement search with the user token, the rate limits will be limited 5 requests per minute with 100 messages per request. Similar to the `assistant.search.context` endpoint, you will quickly hit both user and workspace limits if you attempt to make more calls per query consistently or call these outside of a user initiated action.

## Request {#request}

```
{  "query": "What is the latest on project Gizmo?",  "keywords_clauses": [    ["project", "gizmo"],  ],  "channel_types": ["public_channel", "private_channel", "mpim", "im"],  "content_types": ["messages", "files", "channels"],  "include_context_messages": true,   "include_bots": false,  "sort": "timestamp",   "sort_dir": "asc",   "before": 1755191113,   "after": 1752512713,   "include_message_blocks": true }
```

* * *

## Response {#response}

```
{   "ok": true,   "results": {      "messages": [        {          "author_name": "Jennifer Hynes",          "author_user_id": "U0123456",          "team_id": "T0123456",          "channel_id": "C0123456",          "channel_name": "proj-gizmo",          "message_ts": "123456.7890",          "content": "Hey team, we'll be kicking off our mobile UX revamp for the Gizmo App...",          "is_author_bot": false,          "permalink": "https://mycompany.slack.com/archives/C012345ABC/p123456789",          "blocks": [             {              "type": "rich_text",              "block_id": "0c2PW",              "elements": [                {                  "type": "rich_text_section",                  "elements": [                    {                      "type": "text",                      "text": "Hey team, we'll be kicking off our mobile UX revamp for the Gizmo App..."                    }                  ]                }              ]            }          ],          "context_messages": {            "before": [              {                "text": "What are we discussing in today's sync?",                "user_id:": "U098765",                "ts": "123456.7777",                "blocks": [                   {                    "type": "rich_text",                    "block_id": "0c5KQ",                    "elements": [                      {                        "type": "rich_text_section",                        "elements": [                          {                            "type": "text",                            "text": "What are we discussing in today's sync?"                          }                        ]                      }                    ]                  }                ],              }            ],            "after": [              {                "text": "Woohoo! Exciting news!",                "user_id:": "U555930",                "ts": "123456.9999",                "blocks": [                   {                    "type": "rich_text",                    "block_id": "0P6G5",                    "elements": [                      {                        "type": "rich_text_section",                        "elements": [                          {                            "type": "text",                            "text": "Woohoo! Exciting news!"                          }                        ]                      }                    ]                  }                ],              }            ],          }        }      ],      "files": [        {          "uploader_user_id": "U0123456",          "author_user_id": "U0123456",          "author_name": "Jennifer Hynes",          "team_id": "T0123456",          "file_id": "F0123456",          "date_created": 1733260762,          "date_updated": 1733260763,          "title": "Project tracker",          "file_type": "application/vnd.slack-list",          "permalink": "https://mycompany.slack.com/lists/T0123456/F0123456",          "content": "Project tracker"        }      ],      "channels": [         {          "team_id": "T0123456",          "creator_user_id": "U0123456",          "creator_name": "Jennifer Hynes",          "date_created": 1746570052,          "date_updated": 1746570052,          "name": "project-gizmo",          "topic": "Launch date: Q4 2025",          "purpose": "Discuss project-related topics on the new Gizmo app update",          "permalink": "https://slack.com/archives/C123456"        },      ]    },    "response_metadata": {        "next_cursor": "Q1VSUkVOVF9QQUdFOjI="    }}
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

`assistant_search_context_disabled`

We're having issues returning your search results. Please wait and try again.

`context_channel_not_found`

Specified `context_channel_id` is invalid or the user lacks permission to view it.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`feature_not_enabled`

The feature is not available on the current workspace.

`internal_error`

Internal error.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_action_token`

The `action_token` provided is not valid.

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

The cursormark provided is not valid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_query`

Missing query.

`missing_scope`

The requested channel types are not allowed by the provided scopes.

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

`query_too_long`

Query too long.

`rate_limited`

Rate limited.

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