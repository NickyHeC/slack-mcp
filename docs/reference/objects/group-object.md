Source: https://docs.slack.dev/reference/objects/group-object

# Group object

For information about private channels, refer to [conversation objects](/reference/objects/conversation-object).

The [Conversations API](/apis/web-api/using-the-conversations-api) will tell you whether a conversation is private or not with the `is_private` boolean field.

For posterity, a group object contains information about a private channel that was created before March 2021. The private channel's ID will begin with `G`, as private channels were previously known as "private groups."

An example response is below:

```
{    "id": "G123456",    "name": "secretplans",    "is_group": "true",    "created": 1360782804,    "creator": "U123456",    "is_archived": false,    "is_mpim": false,    "members": [        "U012AB3CD"    ],    "topic": {        "value": "Secret plans on hold",        "creator": "U123456",        "last_set": 1369677212    },    "purpose": {        "value": "Discuss secret plans that nobody else should know",        "creator": "U123456",        "last_set": 1360782804    },    "last_read": "1401383885.000061",    "latest": {},    "unread_count": 0,    "unread_count_display": 0}
```

## Group object fields {#fields}

Field

Type

Description

`id`

string

The ID of the private channel.

`name`

string

The name of the private channel.

`is_group`

boolean

Whether this object is a conversation.

`created`

Unix timestamp

When the conversation was created.

`creator`

string

The user ID of the member that created this private channel.

`is_archived`

boolean

`true` if the private channel is archived.

`is_mpim`

boolean

Whether a multiparty instant message (`mpim`) is being emulated as a private channel. For compatibility with older clients, `mpims` can appear as private channels unless `rtm.start` is called with `mpim_aware=1`.

`members`

array

A list of user IDs for all users in this private channel. This includes any disabled accounts that were in this private channel when they were disabled.

`topic`

object

The topic of the conversation.

`purpose`

object

The purpose of the conversation.

Some API methods (such as [conversations.create](/reference/methods/conversations.create)) will include extra state information for channels when the calling user is a member:

*   `last_read`: the Unix timestamp for the last message the calling user has read in this channel.
*   `unread_count`: a full count of visible messages that the calling user has yet to read.
*   `unread_count_display`: a count of messages that the calling user has yet to read that matter to them (this means it excludes things like join/leave messages).
*   `latest`: the latest message in the channel.