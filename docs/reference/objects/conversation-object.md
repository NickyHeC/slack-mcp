Source: https://docs.slack.dev/reference/objects/conversation-object

# Conversation object

A conversation object contains information about a channel-like thing in Slack. It might be a public channel, a private channel, a direct message, a multi-person direct message, or a huddle. You'll find all of these objects throughout the [Conversations API](/apis/web-api/using-the-conversations-api). Different fields are included in the object payload depending on the type of conversation (channel, DM, MPIM, etc.). The legacy objects—[channel](/reference/objects/channel-object), [group](/reference/objects/group-object), [im](/reference/objects/im-object), and [mpim](/reference/objects/mpim-object)—reference pages are nested under this one for posterity, but they are all now represented by the conversation object.

## Example responses {#examples}

An example response for the [`conversations.info`](/reference/methods/conversations.info) method is as follows:

```
{    "channel": {        "id": "C123456",        "name": "general",        "is_channel": true,        "is_group": false,        "is_im": false,        "is_mpim": false,        "is_private": false,        "created": 1449252889,        "is_archived": false,        "is_general": true,        "unlinked": 0,        "name_normalized": "general",        "is_shared": false,        "is_frozen": false,        "is_org_shared": false,        "is_pending_ext_shared": false,        "pending_shared": [],        "context_team_id": "T12345ABCDE",        "updated": 1689965803820,        "parent_conversation": null,        "creator": "W123456",        "is_ext_shared": false,        "shared_team_ids": [            "T12345ABCDE"        ],        "pending_connected_team_ids": [],        "is_member": true,        "topic": {            "value": "For public discussion of generalities",            "creator": "W123456",            "last_set": 1449709364        },        "purpose": {            "value": "This part of the workspace is for fun. Make fun here.",            "creator": "W123456",            "last_set": 1449709364        },        "properties": {            "posting_restricted_to": {                "type": [                    "admin"                ]            },            "threads_restricted_to": {                "type": [                    "ra"                ]            },            "tabs": [                {                    "id": "files",                    "label": "",                    "type": "files"                },                {                    "id": "bookmarks",                    "label": "",                    "type": "bookmarks"                }            ]        },        "previous_names": [            "specifics",            "abstractions",            "etc"        ]    }}
```

An example response for the [`conversations.history`](/reference/methods/conversations.history) method is as follows:

```
{    "messages": [        {            "type": "message",            "text": "",            "user": "USLACKBOT",            "channel": "C12345ABCDE",            "room": {                "id": "R12345ABCDE",                "name": "",                "media_server": "",                "created_by": "U12345ABCDE",                "date_start": 1689964161,                "date_end": 0,                "participants": [],                "participant_history": [                    "U12345ABCDE"                ],                "participants_camera_on": [],                "participants_camera_off": [],                "participants_screenshare_on": [],                "participants_screenshare_off": [],                "canvas_thread_ts": "1689964161.419229",                "thread_root_ts": "1689964161.419229",                "channels": [                    "C12345ABCDE"                ],                "is_dm_call": false,                "was_rejected": false,                "was_missed": false,                "was_accepted": false,                "has_ended": false,                "background_id": "GRADIENT_03",                "canvas_background": "GRADIENT_03",                "is_prewarmed": false,                "is_scheduled": false,                "attached_file_ids": [],                "media_backend_type": "free_willy",                "display_id": "",                "external_unique_id": "12345abc-123a-123b-123c-12345abcde7",                "app_id": "A00",                "call_family": "huddle",                "pending_invitees": {},                "last_invite_status_by_user": {}            },            "no_notifications": true,            "permalink": "https://example.com",            "subtype": "huddle_thread",            "ts": "1689964161.419229",            "blocks": [                {                    "type": "rich_text",                    "block_id": "aBcDe",                    "elements": [                        {                            "type": "rich_text_section",                            "elements": [                                {                                    "type": "text",                                    "text": "A huddle started"                                }                            ]                        }                    ]                }            ],            "team": "T12345ABCDE"        },        // ...    ]}
```

## Conversation-related booleans {#booleans}

Property

Description

`is_archived`

Indicates a conversation is archived, frozen in time.

`is_channel`

Indicates whether a conversation is a channel. Private channels created before March 2021 (with IDs that begin with `G`) will return `false`, and `is_group` will be `true` instead. Use `is_private` to determine whether a channel is private or public.

`is_ext_shared`

Indicates whether a conversation is part of a [Shared Channel](/apis/slack-connect/) with a remote organization. Your app should make sure the data it shares in such a channel is appropriate for both workspaces. `is_shared` will also be `true`.

`is_general`

Means the channel is the workspace's "general" discussion channel (even if it may not be named `#general`). That might be important to your app because almost every user is a member.

`is_group`

Means the channel is a private channel created before March 2021. `is_private` will also be `true`.

`is_im`

Means the conversation is a direct message between two distinguished individuals or a user and a bot. `is_private` will also be `true`.

`is_member`

Indicates whether the user, bot user or Slack app associated with the token making the API call is itself a member of the conversation.

`is_mpim`

Represents an unnamed private conversation between multiple users. `is_private` will also be `true`.

`is_org_shared`

Indicates whether this shared channel is shared between [Enterprise organization](/enterprise) workspaces within the same organization. It's a little different from (_externally_) [Shared Channels](/apis/slack-connect/), yet `is_shared` will be `true`.

`is_pending_ext_shared`

Means the conversation is ready to become an `is_ext_shared` channel, but needs some kind of approval or sign off first. Best to treat it as if it were a shared channel, even if it traverses only one workspace.

`is_private`

Means the conversation is privileged between two or more members. Ensure that you meet their privacy expectations.

`is_read_only`

Means the conversation can't be written to by the user performing the API call.

`is_shared`

Means the conversation is in some way shared between multiple workspaces. Look for `is_ext_shared` and `is_org_shared` to learn which kind it is, and if that matters, act accordingly.

`is_thread_only`

Means the conversation can't be written to by the user performing the API call, except to reply to messages in the channel.

`num_members`

The number of members in the conversation. `num_members` may not make an appearance in the response for conversation types like DMs, where the number of members is constant.

## Other conversation-related attributes {#other-attributes}

Property

Type

Description

`name`

String

Indicates the name of the channel-like thing, without a leading hash sign. Don't get too attached to that name; it may change — instead, when working with channel-like things, focus on their IDs, their type, and the team/workspace they belong to.

`creator`

String

The ID of the member that created this conversation.

`created`

Int

Timestamp of when the conversation was created.

`conversation_host_id`

String

Appears on shared channel objects and indicates the "host" of the shared channel. The value may contain a workspace's ID (beginning with `T`) _or_ an Enterprise organization's ID (beginning with `E`).

`topic`

String

Provides information about the channel topic.

`purpose`

String

Provides information about the channel purpose.

`updated`

Int

The timestamp, in milliseconds, when the channel settings were updated — for example, the "topic" or "description" of the channel changed.

Some API methods; for example, [`conversations.join`](/reference/methods/conversations.join), can include extra state information for channels when the calling user is a member:

Property

Type

Description

`last_read`

Int

The timestamp for the last message the calling user has read in this channel.

`unread_count`

Int

A full count of visible messages that the calling user has yet to read.

`unread_count_display`

Int

A count of messages that the calling user has yet to read that matter to them (excludes things like join/leave messages).

`latest`

String

The latest message in the channel.

`properties`

Object

Additional channel properties (see below).

The `properties` object contains many additional fields that appear based on the context of the object.

Property

Type

Description

`posting_restricted_to`

Object

An object comprised of three arrays: `subteam`, `type`, and `user`, each offering a different way to restrict who can post in the channel.

`threads_restricted_to`

Object

An object comprised of three arrays: `subteam`, `type`, and `user`, each offering a different way to restrict who can post in threads in the channel.

`at_channel_restricted`

Boolean

Indicates if the `@channel` mention is restricted.

`at_here_restricted`

Boolean

Indicates if the `@here` mention is restricted.

`huddles_restricted`

Boolean

Indicates if huddles are restricted.

`sharing_disabled`

Boolean

Indicates if sharing is disabled.

`canvas`

Object

The channel canvas.

`record_channel`

Object

Properties for Salesforce channels.

`crm`

Object

Properties for Slack CRM.

`workflow`

Object

Properties for a workflow; currently contains one field, `primary_workflow_url`.

`tabs`

Object

List of channel tabs. Each tab has an `id`, `label`, `type`, `data`, and `is_disabled` property. Its `type` can be any of the following: `list`, `canvas`, `files`, `bookmarks`, `folder`, `pins`, `workflows`, `channel_canvas`, `record_list`, `record_overview`, `record_summary`, `record_related_list`,`salesforce_list_view`.

`huddles`

Object

Properties for huddles for the channel the huddle occurred in.

`membership_limit`

Integer

Limit of users in channel.

`channel_workflows`

Array

An array of workflows in the channel.

`channel_solutions`

Object

Properties for channel solutions: `workflow_trigger_ids`, `workflow_workflow_ids`, `canvas_ids`, `list_ids`.

`default_tab_id`

String

Indicates which tab in the channel is the default.

`auto_open_tab_id`

String

Indicates which tab in the channel auto opens.

`meeting_notes`

Object

Properties for channel meeting notes.

These channel objects are not the same object type as those for private channels created before March 2021, which are considered [group objects](/reference/objects/group-object).