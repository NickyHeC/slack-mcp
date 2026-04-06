Source: https://docs.slack.dev/reference/objects/im-object

# IM object

An IM object An IM object is a legacy object that contains information about a direct message channel. IM objects are now [conversation](/reference/objects/conversation-object) objects. information about a direct message channel.

```
{    "id": "D024BFF1M",    "is_im": true,    "user": "U024BE7LH",    "created": 1360782804,    "is_user_deleted": false}
```

## IM object fields {#fields}

Field

Type

Description

`id`

string

The ID of the object.

`is_im`

boolean

Indicates if the object is an IM.

`user`

string

Each direct message channel is between two users. One of these users is always the calling user, the other's ID is indicated by the `user` property.

`created`

Unix timestamp

When the IM was created.

`is_user_deleted`

boolean

`true` if the other user's account has been disabled.

Some API methods will include extra state information for the channel.

*   `is_open` shows if the DM channel is open.
*   `last_read` is the timestamp for the last message the calling user has read in this channel.
*   `unread_count` is a count of messages that the calling user has yet to read.
*   `latest` is the latest message in the channel.