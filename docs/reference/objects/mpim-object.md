Source: https://docs.slack.dev/reference/objects/mpim-object

# MPIM object

A MPIM object is a legacy object that contains information about a multi-party instant message. MPIM objects are now [conversation](/reference/objects/conversation-object) objects.

```
{    "id": "G024BE91L",    "name": "mpdm-user1--user2--user3-1",    "is_mpim": true,    "is_group": false,    "created": 1360782804,    "creator": "U024BE7LH",    "members": [        "U024BE7LH"    ],    "last_read": "1401383885.000061",    "latest": {},    "unread_count": 0,    "unread_count_display": 0}
```

## MPIM object fields {#fields}

Field

Type

Description

`id`

string

The ID of the MPIM.

`name`

string

Indicates the name of the MPIM.

`is_mpim`

boolean

Indicates if a multi-party instant message (`mpim`) is being emulated as a group. For compatibility with older clients, `mpims` can appear as groups unless `rtm.start` is called with `mpim_aware=1`.

`is_group`

boolean

Indicates if the object is a group.

`created`

Unix timestamp

Indicates when the MPIM was created.

`creator`

string

The user ID of the member that created the MPIM.

`members`

array

A list of user IDs for all users in this MPIM. This includes any disabled accounts that were in this MPIM when they were disabled.