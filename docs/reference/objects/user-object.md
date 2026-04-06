Source: https://docs.slack.dev/reference/objects/user-object

# User object

A user object contains information about a Slack workspace user.

If you develop for an [Enterprise organization](/enterprise), there's a lot to consider about the most important field in a user object: the `id` or `user_id`. [Learn more about global IDs and migration](/enterprise#user_ids).

## Example {#example}

```
{    "user": {        "id": "U123ABC456",        "team_id": "T123ABC456",        "name": "sherlock",        "deleted": false,        "color": "99a949",        "real_name": "Sherlock Holmes",        "tz": "Europe/London",        "tz_label": "Greenwich Mean Time",        "tz_offset": 0,        "profile": {            "title": "Senior Detective",            "phone": "(000) 000-0000",            "skype": "",            "real_name": "Sherlock Holmes",            "real_name_normalized": "Sherlock Holmes",            "display_name": "sherlock",            "display_name_normalized": "sherlock",            "fields": {                "Xf111AAA111": {                    "value": "1 dog: Sherlock Bones",                    "alt": ""                },                "Xf222BBB222": {                    "value": "no tree nuts!",                    "alt": ""                }            },            "status_text": "elementary, my dear watson ",            "status_emoji": ":thinking-face:",            "status_emoji_display_info": [                {                    "emoji_name": "thinking-face",                    "display_url": "https://emoji.slack-edge.com/T123ABC456/thinking-face/123...abc.png"                }            ],            "status_expiration": 0,            "avatar_hash": "b187f5128ba4",            "start_date": "2015-12-25",            "image_original": "https://avatars.slack-edge.com/2021-10-21/..._...__original.jpg",            "is_custom_image": true,            "email": "sholmes@example.com",            "pronouns": "they/them",            "huddle_state": "default_unset",            "huddle_state_expiration_ts": 0,            "first_name": "Sherlock",            "last_name": "Holmes",            "image_24": "https://avatars.slack-edge.com/2021-10-21/..._...__24.jpg",            "image_32": "https://avatars.slack-edge.com/2021-10-21/..._...__32.jpg",            "image_48": "https://avatars.slack-edge.com/2021-10-21/..._...__48.jpg",            "image_72": "https://avatars.slack-edge.com/2021-10-21/..._...__72.jpg",            "image_192": "https://avatars.slack-edge.com/2021-10-21/..._...__192.jpg",            "image_512": "https://avatars.slack-edge.com/2021-10-21/..._...__512.jpg",            "image_1024": "https://avatars.slack-edge.com/2021-10-21/..._...__1024.jpg",            "status_text_canonical": "",            "team": "T0123ABC456"        },        "is_admin": false,        "is_owner": false,        "is_primary_owner": false,        "is_restricted": false,        "is_ultra_restricted": false,        "is_bot": false,        "is_app_user": false,        "updated": 1675264590,        "is_email_confirmed": true,        "who_can_share_contact_card": "EVERYONE",        "enterprise_user": {            "id": "U123ABC456",            "enterprise_id": "E123ABC456",            "enterprise_name": "Sherlock Holmes Detective Agency",            "is_admin": false,            "is_owner": false,            "is_primary_owner": false,            "teams": [                "T123ABC456",                "T789DEF000"            ]        }    }}
```

## Common fields {#fields}

The composition of user objects can vary greatly depending on the API being used, or the context of each Slack workspace. Data that has not been supplied may not be present at all, may be `null`, or may contain an empty string. One example where the profile information varies is getting data for a user connected through Slack Connect; an example of that type of user object can be found in the [External members section](/apis/slack-connect/#members) of the Slack Connect page.

Therefore, consider the following a non-exhaustive list of potential user object fields you _might_ encounter.

Field

Type

Description

`always_active`

Boolean

Indicates that a bot user is set to be constantly active in [presence status](/apis/web-api/user-presence-and-status).

`color`

String

Used in some clients to display a special username color.

`deleted`

Boolean

This user has been deactivated when the value of this field is `true`. Otherwise the value is `false`, or the field may not appear at all.

`enterprise_user`

Object

An object containing info related to an [Enterprise org user](/enterprise). See our [Enterprise org](/enterprise) documentation for more detail.

`enterprise_user.enterprise_id`

String

A unique ID for the Enterprise organization this user belongs to.

`enterprise_user.enterprise_name`

String

A display name for the Enterprise organization.

`enterprise_user.id`

String

This user's ID - some Enterprise org users have a kind of dual identity — a local, workspace-centric user ID as well as a org-wise user ID, called the Enterprise user ID. In most cases these IDs can be used interchangeably, but when it is provided, we strongly recommend using this Enterprise user `id` over the root level user `id` field.

`enterprise_user.is_admin`

Boolean

Indicates whether the user is an Admin of the Enterprise organization.

`enterprise_user.is_owner`

Boolean

Indicates whether the user is an Owner of the Enterprise organization.

`enterprise_user.teams`

String\[\]

An array of workspace IDs that are in the Enterprise organization.

`has_2fa`

Boolean

Describes whether [two-factor authentication](https://slack.com/intl/en-ie/help/articles/204509068-Set-up-two-factor-authentication) is enabled for this user. Only visible if the user executing the call is an admin.

`id`

String

Identifier for this workspace user. It is unique to the workspace containing the user. Use this field together with `team_id` as a unique key when storing related data or when specifying the user in API requests. We recommend considering the format of the string to be an opaque value, and not to rely on a particular structure.

`is_admin`

Boolean

Indicates whether the user is an Admin of the current workspace.

`is_app_user`

Boolean

Indicates whether the user is an authorized user of the calling app.

`is_bot`

Boolean

Indicates whether the user is actually a bot user. Bleep bloop. Note that **Slackbot** is special, so `is_bot` will be false for it.

`is_invited_user`

Boolean

Only present (and always `true`) when a user has been [invited](https://slack.com/intl/en-ie/help/articles/201330256-invite-new-members-to-your-workspace) but has not yet signed in. Once the user signs in, this field is no longer present.

`is_owner`

Boolean

Indicates whether the user is an Owner of the current workspace.

`is_primary_owner`

Boolean

Indicates whether the user is the [Primary Owner](https://slack.com/intl/en-ie/help/articles/360038161033-Understand-the-Primary-Owner-role) of the current workspace.

`is_restricted`

Boolean

Indicates whether or not the user is a [guest user](https://slack.com/intl/en-ie/help/articles/202518103-Multi-Channel-and-Single-Channel-Guests). Use in combination with the `is_ultra_restricted` field to check if the user is a single-channel guest user.

`is_stranger`

Boolean

If `true`, this user belongs to a different workspace than the one associated with your app's token, and isn't in any [shared channels](/apis/slack-connect/) visible to your app. If `false` (or this field is not present), the user is either from the same workspace as associated with your app's token, or they are from a different workspace, but are in a [shared channel](/apis/slack-connect/) that your app has access to. Read our [shared channels docs](/apis/slack-connect/) for more detail.

`is_ultra_restricted`

Boolean

Indicates whether or not the user is a [single-channel guest](https://slack.com/intl/en-ie/help/articles/202518103-Multi-Channel-and-Single-Channel-Guests).

`locale`

String

Contains a [IETF language code](https://en.wikipedia.org/wiki/IETF_language_tag) that represents this user's chosen display language for Slack clients. Useful for [localizing your apps](/surfaces/app-design).

`name`

String

Don't use this. It once indicated the preferred username for a user, but that behavior has [fundamentally changed](/changelog/2017-09-the-one-about-usernames) since.

`profile`

Object

[The profile object](/reference/objects/user-object/#profile) contains the default fields of a user's workspace profile. A user's _custom_ profile fields may be discovered using [`users.profile.get`](/reference/methods/users.profile.get).

`two_factor_type`

Enum (String)

Indicates the type of two-factor authentication in use. Only present if `has_2fa` is `true`. The value will be either `app` or `sms`.

`tz`

String

A human-readable string for the geographic timezone-related region this user has specified in their account.

`tz_label`

String

Describes the commonly used name of the `tz` timezone.

`tz_offset`

Integer

Indicates the number of seconds to offset UTC time by for this user's `tz`. Changes silently if changed due to daylight savings.

`updated`

String

A Unix timestamp indicating when the user object was last updated.

## Profile fields {#profile}

The following fields are the default fields of a user's workspace profile. A user may have additional custom fields, though! Use [`users.profile.get`](/reference/methods/users.profile.get) to view all the user's profile fields.

Field

Type

Description

`avatar_hash`

String

`display_name`

String

The display name the user has chosen to identify themselves by in their workspace profile. Do not use this field as a unique identifier for a user, as it may change at any time. Instead, use `id` and `team_id` in concert.

`display_name_normalized`

String

The `display_name` field, but with any non-Latin characters filtered out.

`email`

String

A valid email address. It cannot have spaces, and it must have an `@` and a domain. It cannot be in use by another member of the same team. Changing a user's email address will send an email to both the old and new addresses, and also post a slackbot to the user informing them of the change. This field can only be changed _by admins_ for users on **paid** teams.

`fields`

Object

All the [custom profile fields](/reference/methods/users.profile.set#custom_profile) for the user.

`first_name`

String

The user's first name. The name `slackbot` cannot be used. Updating `first_name` will update the first name within `real_name`.

`image_*`

String

These various fields will contain `https` URLs that point to square ratio, web-viewable images (GIFs, JPEGs, or PNGs) that represent different sizes of a user's profile picture.

`last_name`

String

The user's last name. The name `slackbot` cannot be used. Updating `last_name` will update the second name within `real_name`.

`phone`

String

The user's phone number, in any format.

`pronouns`

String

The pronouns the user prefers to be addressed by.

`real_name`

String

The user's first and last name. Updating this field will update `first_name` and `last_name`. If only one name is provided, the value of `last_name` will be cleared.

`real_name_normalized`

String

The `real_name` field, but with any non-Latin characters filtered out.

`skype`

String

A shadow from a bygone era. It will always be an empty string and cannot be set otherwise.

`start_date`

String

The date the person joined the organization. Only available if [Slack Atlas](https://slack.com/atlas) is enabled.

`status_emoji`

String

The displayed emoji that is enabled for the Slack team, such as `:train:`.

`status_expiration`

Integer

the Unix timestamp of when the status will expire. Providing `0` or omitting this field results in a custom status that will not expire.

`status_text`

String

The displayed text of up to 100 characters. We strongly encourage brevity.

`team`

String

The ID of the team the user is on.

`title`

String

The user's title.

Accessing Email Addresses

The [`users:read.email`](/reference/scopes/users.read.email) OAuth scope is now required to access the `email` field in user objects returned by the [`users.list`](/reference/methods/users.list) and [`users.info`](/reference/methods/users.info) web API methods. [`users:read`](/reference/scopes/users.read) is no longer a sufficient scope for this data field. [Learn more](/changelog/2017-04-narrowing-email-access).