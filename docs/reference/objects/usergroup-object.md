Source: https://docs.slack.dev/reference/objects/usergroup-object

# Usergroup object

A usergroup object contains information about a group of users.

```
{    "id": "S123ABC456",    "team_id": "T060RNRCH",    "is_usergroup": true,    "name": "Workspace Admins",    "description": "A group of all Administrators on your workspace.",    "handle": "admins",    "is_external": false,    "date_create": 1446598059,    "date_update": 1446670362,    "date_delete": 0,    "auto_type": "admin",    "created_by": "USLACKBOT",    "updated_by": "U060RNRCZ",    "deleted_by": null,    "prefs": {        "channels": [],        "groups": []    },    "users": [        "U060RNRCZ",        "U060ULRC0",        "U06129G2V",        "U061309JM"    ],    "user_count": "4"}
```

## Usergroup object fields {#fields}

Field

Type

Description

`id`

string

The ID of the usergroup.

`team_id`

string

The ID of the team.

`is_usergroup`

boolean

Indicates if the object is a user group.

`name`

string

Indicates the friendly name of the group.

`description`

string

Explains the purpose of the group (optional).

`handle`

string

Indicates the value used to notify group members via a mention without a leading @ sign.

`is_external`

boolean

Indicates if the user group is external.

`date_create`

Unix timestamp

When the user group was created.

`date_update`

Unix timestamp

When the user group was last updated.

`date_delete`

Unix timestamp

Non-zero value for disabled groups.

`auto_type`

string

Can be `admins` for a Workspace Admins group, `owners` for a Workspace Owners group or `null` for a custom group.

`created_by`

string

User ID of the member who created the user group.

`updated_by`

string

User ID of the member who updated the user group.

`deleted_by`

string

User ID of the member who deleted the user group.

`prefs`

object

Contains default `channels` and `groups` (private channels) that members of this group will be invited to upon joining.

`users`

array

Contains a list of [user object](/reference/objects/user-object) `id` values which belong to the user group. This parameter is included if the `include_users` option is enabled on some API endpoints.

`user_count`

integer

Indicates the total number of users in a group.