Source: https://docs.slack.dev/reference/objects/channel-object

# Channel object

A channel object is a legacy object that contains information about a workspace channel. These channel objects are not the same object type as private channels, which are considered [group objects](/reference/objects/group-object). Channels and groups are now considered a type of [conversation](/reference/objects/conversation-object).

## Channel object fields {#fields}

Field

Type

Description

`id`

string

The channel ID.

`name`

string

Indicates the name of the channel-like thing, without a leading hash sign. Don't get too attached to that name. It might change. Don't even bother storing it. When thinking about channel-like things, think about their IDs, their type, and the team/workspace they belong to.

`is_channel`

boolean

Indicates if it is a channel.

`created`

Unix timestamp

Timestamp of when the channel was created.

`creator`

string

The user ID of the member that created the channel.

`is_archived`

boolean

`true` if the channel is archived.

`is_general`

boolean

`true` if this channel is the "general" channel that includes all regular members. In most workspaces this is called `#general`, but some workspaces have renamed it.

`name_normalized`

string

A normalized string of the name.

`is_shared`

boolean

`true` if the channel is shared.

`is_org_shared`

boolean

Indicates if the organization which the channel belongs to is shared.

`is_member`

boolean

`true` if the calling member is part of the channel.

`is_private`

boolean

Indicates if the channel is private.

`is_mpim`

boolean

Indicates if the channel is a multi-party instant message.

`last_read`

Unix timestamp

The timestamp for the last message the calling user has read in this channel.

`latest`

object

The latest message in the channel.

`unread_count`

integer

A full count of visible messages that the calling user has yet to read.

`unread_count_display`

integer

A count of messages that the calling user has yet to read that matter to them (this means it excludes things like join/leave messages).

`members`

array

A list of user IDs for all users in this channel. This includes any disabled accounts that were in this channel when they were disabled.

`topic`

object

The topic of the channel.

`purpose`

object

The purpose of the channel.

`previous_names`

array

A list of prior names the channel has used.

## Example {#example}

```
{    "channel": {        "id": "C1H9RESGL",        "name": "busting",        "is_channel": true,        "created": 1466025154,        "creator": "U0G9QF9C6",        "is_archived": false,        "is_general": false,        "name_normalized": "busting",        "is_shared": false,        "is_org_shared": false,        "is_member": true,        "is_private": false,        "is_mpim": false,        "last_read": "1503435939.000101",        "latest": {            "text": "Containment unit is 98% full",            "username": "ecto1138",            "bot_id": "B19LU7CSY",            "attachments": [                {                    "text": "Don't get too attached",                    "id": 1,                    "fallback": "This is an attachment fallback"                }            ],            "type": "message",            "subtype": "bot_message",            "ts": "1503435956.000247"        },        "unread_count": 1,        "unread_count_display": 1,        "members": [            "U0G9QF9C6",            "U1QNSQB9U"        ],        "topic": {            "value": "Spiritual containment strategies",            "creator": "U0G9QF9C6",            "last_set": 1503435128        },        "purpose": {            "value": "Discuss busting ghosts",            "creator": "U0G9QF9C6",            "last_set": 1503435128        },        "previous_names": [            "dusting"        ]    }}
```