Source: https://docs.slack.dev/reference/scim-api

# SCIM API reference

The SCIM API is RESTful and the endpoint URLs are different than other Slack API endpoints.

*   v1.1
*   v2.0

Endpoint

Description

[`GET /ServiceProviderConfigs`](#get-serviceproviderconfigs)

Returns Slack's configuration details for our SCIM API

[`GET /Schemas/Users`](#get-schemas-users)

Returns Slack's configuration details for how users are formatted

[`GET /Schemas/Groups`](#get-schemas-groups)

Returns Slack's configuration details for how groups are formatted

[`GET /Users`](#get-users)

Returns a paginated list of users

[`GET /Users/<id>`](#get-users-id)

Retrieves a single user resource

[`POST /Users`](#post-users)

Creates a user

[`PATCH /Users/<id>`](#patch-users-id)

Updates an existing user resource, overwriting specified values

[`PUT /Users/<id>`](#put-users-id)

Updates an existing user resource, overwriting all values

[`DELETE /Users/<id>`](#delete-users-id)

Sets a Slack user to deactivated

[`GET /Groups/`](#get-groups)

Returns a paginated list of groups

[`GET /Groups/<id>`](#get-groups-id)

Retrieves a single group resource

[`POST /Groups`](#post-groups)

Creates a new group

[`PATCH /Groups/<id>`](#patch-groups-id)

Updates an existing group resource

[`PUT /Groups/<id>`](#patch-groups-id)

Updates an existing group resource, overwriting all values

[`DELETE /Groups/<id>`](#delete-groups-id)

Permanently removes a group

Endpoint

Description

[`GET /ServiceProviderConfig`](#get-serviceproviderconfigs)

Returns Slack's configuration details for our SCIM API

[`GET /ResourceTypes`](#get-resource-types)

Returns Slack's type of resources available

[`GET /Schemas/Users`](#get-schemas-users-2)

Returns Slack's configuration details for how users are formatted

[`GET /Schemas/Groups`](#get-schemas-groups-2)

Returns Slack's configuration details for how groups are formatted

[`GET /Users`](#get-users-2)

Returns a paginated list of users

[`GET /Users/<id>`](#get-users-id-2)

Retrieves a single user resource

[`POST /Users`](#post-users-2)

Creates a user

[`PATCH /Users/<id>`](#patch-users-id-2)

Updates an existing user resource, overwriting specified values

[`PUT /Users/<id>`](#put-users-id-2)

Updates an existing user resource, overwriting all values

[`DELETE /Users/<id>`](#delete-users-id-2)

Sets a Slack user to deactivated

[`GET /Groups/`](#get-groups-2)

Returns a paginated list of groups

[`GET /Groups/<id>`](#get-groups-id-2)

Retrieves a single group resource

[`POST /Groups`](#post-groups-2)

Creates a new group

[`PATCH /Groups/<id>`](#patch-groups-id-2)

Updates an existing group resource

[`PUT /Groups/<id>`](#put-groups-id-2)

Updates an existing group resource, overwriting all values

[`DELETE /Groups/<id>`](#delete-groups-id-2)

Permanently removes a group

## Service Provider Configuration {#serviceproviderconfigs}

Endpoint

Description

[`GET /ServiceProviderConfigs`](#get-serviceproviderconfigs)

Returns Slack's configuration details for our SCIM API

### GET /ServiceProviderConfigs {#get-serviceproviderconfigs}

Returns Slack's configuration details for our SCIM API, including which operations are supported.

## Resource types {#resourcetypes}

*   v1.1
*   v2.0

Not applicable to SCIM v1.1.

Endpoint

Description

[`GET /ResourceTypes`](#get-resource-types)

Returns Slack's configuration details for our SCIM API

### GET /ResourceTypes {#get-resource-types}

Returns Slack's type of resources available.

## Schemas {#schemas}

Slack currently supports schemas for users and groups. Querying the schemas will provide the most up-to-date rendering of the supported SCIM attributes.

*   v1.1
*   v2.0

Endpoint

Description

[`GET /Schemas/Users`](#get-schemas-users)

Returns Slack's configuration details for how users are formatted

[`GET /Schemas/Groups`](#get-schemas-groups)

Returns Slack's configuration details for how groups are formatted

### GET /Schemas/Users {#get-schemas-users}

Returns Slack's configuration details for how users are formatted.

#### Multi-channel guest user schema {#get-multi-channel-guest-schemas}

Provisioning multi-channel guest users with the SCIM API is only available to Enterprise plan customers.

Slack also supports a custom extension, called `urn:scim:schemas:extension:slack:guest:1.0`, that can be used to designate a user as a multi-channel guest. The details of this schema are also returned as part of the `GET /scim/v1/Schemas/Users` payload.

### GET /Schemas/Groups {#get-schemas-groups}

Returns Slack's configuration details for how groups are formatted.

Endpoint

Description

[`GET /Schemas`](#get-schemas-2)

Returns a list of Slack supported schemas along with Slack's configuration details

[`GET /Schemas/Users`](#get-schemas-users-2)

Returns Slack's configuration details for how users are formatted

[`GET /Schemas/Groups`](#get-schemas-groups-2)

Returns Slack's configuration details for how groups are formatted

### Get /Schemas {#get-schemas-2}

Returns a list of Slack supported schemas along with Slack's configuration details.

### GET /Schemas/Users {#get-schemas-users-2}

Returns Slack's configuration details for how users are formatted.

#### Multi-channel guest user schema {#get-multi-channel-guest-schemas-2}

Provisioning multi-channel guest users with the SCIM API is only available to Enterprise plan customers.

Slack also supports a custom extension, called `urn:scim:schemas:extension:slack:guest:2.0:User`, that can be used to designate a user as a multi-channel guest. The details of this schema are also returned as part of the `GET /scim/v2/Schemas/Users` payload.

### GET /Schemas/Groups {#get-schemas-groups-2}

Returns Slack's configuration details for how groups are formatted.

## Users {#users}

Users map to the individuals of your team across a workspace or Enterprise organization. Each user contains properties called attributes, like `userName` and `title`. You can list users, filter by attribute, add new users, update a user's profile information, or remove a user entirely.

*   v1.1
*   v2.0

Endpoint

Description

[`GET /Users`](#get-users)

Returns a paginated list of users

[`GET /Users/<id>`](#get-users-id)

Retrieves a single user resource

[`POST /Users`](#post-users)

Creates a user

[`PATCH /Users/<id>`](#patch-users-id)

Updates an existing user resource, overwriting specified values

[`PUT /Users/<id>`](#put-users-id)

Updates an existing user resource, overwriting all values

[`DELETE /Users/<id>`](#delete-users-id)

Sets a Slack user to deactivated

### User attributes {#user-attributes}

Attributes are the details associated with a user's account. These are the details that someone would typically set in their profile (for example, by clicking the **Edit Profile** button in the Slack application).

The following tables map SCIM attributes to the profile fields that Slack uses. Most of these profile fields are exposed directly in a person's profile in the Slack UI. Sometimes, multiple SCIM attributes map to a single Slack profile field. For example, Slack's **Display name** field will populate from either the `displayName` or the `userName` SCIM attribute, depending on which is set. If both are set, it will use `displayName`.

When you sync some user attributes to Slack via SCIM, these fields become locked in Slack and you can no longer delete them or edit them. However, you may choose to hide them from user profiles.

Attribute values will vary by identity provider. For example, some may use a single field for a user's full name, others may provide sub-attributes such as `givenName` and `familyName`, still others may provide both. Either is acceptable, but they should only describe the same name (i.e. sub-attributes should not contain additional or optional information, such as a nickname).

Not every attribute will be displayed in a user's profile. For example, `active` does not appear as a field but can be used to determine if a user's account is active.

Slack Profile Field

SCIM Attribute

Attribute Type

Notes

Username

`userName`

Singular

Required Max of 21 characters. Support periods `.`, underscores `_`, and hyphens `-`. All other special characters are converted to underscores.

Full Name

`name`, familyName

Singular

Nickname

`nickName`

Singular

Display Name

`displayName`, `userName`

Singular

Support periods `.`, underscores `_`, and hyphens `-`. All other special characters are converted to underscores. Max of 80 characters.

Email

`emails[0]['value']`

Multi-Valued

Required

Profile URL

`profileUrl`

Singular

Profile Photo

`photos[0]['values']`

Multi-Valued

Groups

`groups`

Multi-Valued

Title

`title`

Singular

Timezone

`timezone`

Singular

Active

`active`

Singular

Password

`password`

Singular

Never returned but can be used to set the initial password for a user if the team is not using an identity manager.

Start Date

`profile.startDate`

Singular

Date should be in the ISO 8601 format, such as `2024-04-10T00:00:00+0000`. Must provide the `urn:scim:schemas:extension:slack:profile:1.0` schema in request body.

Slack will also create profile fields if the following SCIM attributes are present:

Custom Profile Field

SCIM Attribute

Attribute Type

Addresses

`addresses`

Multi-Valued

City

`addresses[primary]['locality']`

Singular

Cost Center

`enterprise.costCenter`

Singular

Country

`addresses[primary]['country']`

Singular

Department

`enterprise.department`

Singular

Division

`enterprise.division`

Singular

Employee ID

`enterprise.employeeNumber`

Singular

Honorific Prefix

`name.honorificPrefix`

Singular

Locale

`locale`

Singular

Manager

`enterprise.manager.managerId`

Singular

Organization

`enterprise.organization`

Singular

Phone

`phoneNumbers[0]['values']`

Multi-Valued

Preferred Language

`preferredLanguage`

Singular

Roles

`roles`

Multi-Valued

Title

`title`

Singular

UserType

`userType`

Singular

Zip Code

`addresses[primary]['postalCode']`

Singular

### GET /Users {#get-users}

Returns a paginated list of users, ten users per page by default.

When querying larger Slack instances, reduce the `count` parameter to 1,000 or less, and use the `startIndex` parameter to paginate through users. [Pagination will be required](/changelog/2019-06-have-scim-will-paginate) for large lists of users as of August 30, 2019.

It's possible to return a list of specific types of users with the [`filter` parameter](#filter).

```
 GET /scim/v1/Users?startIndex=4&count=500 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

### GET /Users/<id> {#get-users-id}

Retrieves a single user resource.

The value of the `<id>` should be the user's corresponding Slack ID, beginning with either `U` or `W`.

```
 GET /scim/v1/Users/U1A23BC4D HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

### POST /Users {#post-users}

Creates a user.

Must include the `userName` attribute and at least one email address. You may provide an email address in the `userName` field, but it will be automatically converted to a Slack-appropriate username.

The `value` sub-attribute for `photos` can either be a publicly accessible URL e.g. `"https://photos.example.com/profilephoto.jpg"`, or a Data URL containing raw image data, e.g. `"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..."`.

This example request body provides a detailed example of which attributes Slack uses, especially for the multi-valued attributes.

```
{    "schemas": [        "urn:scim:schemas:core:1.0",        "urn:scim:schemas:extension:enterprise:1.0",        "urn:scim:schemas:extension:slack:profile:1.0"    ],    "userName": "other_username",    "nickName": "slack_username",    "name": {        "familyName": "Last",        "givenName": "First",        "honorificPrefix": "Dr."    },    "displayName": "First Last",    "profileUrl": "https://login.example.com/slack_username",    "emails": [        {            "value": "thedoctor@gallifrey.com",            "type": "work",            "primary": true        },        {            "value": "some_other@email.com",            "type": "home"        }    ],    "addresses": [        {            "streetAddress": "1234 Doctor St",            "locality": "New York",            "region": "NY",            "postalCode": "12345",            "country": "USA",            "primary": true        }    ],    "phoneNumbers": [        {            "value": "555-555-5555",            "type": "work"        },        {            "value": "555-555-4444",            "type": "mobile"        }    ],    "photos": [        {            "value": "https://photos.example.com/profilephoto.jpg",            "type": "photo"        }    ],    "roles": [        {            "value": "Lead Detective",            "primary": "true"        }    ],    "userType": "Employee",    "title": "Detective",    "preferredLanguage": "en_US",    "locale": "en_US",    "timezone": "America/New York",    "active": true,    "password": "Doctor!Who??",    "urn:scim:schemas:extension:enterprise:1.0": {        "employeeNumber": "701984",        "costCenter": "4130",        "organization": "Torchwood",        "division": "Alien Investigations",        "department": "Detective Agency",        "manager": {            "managerId": "U123ABC456"        }    },    "urn:scim:schemas:extension:slack:profile:1.0": {        "startDate": "2024-04-10T00:00:00+0000"    }}
```

### POST /Users (Multi-Channel Guests) {#post-multi-channel-guest}

Provisioning multi-channel guest users with the SCIM API is only available to Enterprise plan customers.

You can create a multi-channel guest user using the `urn:scim:schemas:extension:slack:guest:1.0` attribute. Within that attribute:

*   The `type` sub attribute is mandatory.
*   The optional `expiration` sub attribute must be an ISO 8601 date time string.
*   The only valid value for the `type` sub-attribute is `"multi"` string.

Be sure to include the `urn:scim:schemas:extension:slack:guest:1.0` URI in the `schemas` attribute.

Here are two ways to create a multi-channel guest user:

_**Option 1**_

Specifies a multi-channel guest user account that expires on "11/30/2020 23:59:59 UTC".

```
    "urn:scim:schemas:extension:slack:guest:1.0": {        "type": "multi",        "expiration": "2020-11-30T23:59:59Z"    }
```

_**Option 2**_

Specifies a multi-channel guest user account with no expiration date.

```
    "urn:scim:schemas:extension:slack:guest:1.0": {        "type": "multi"    }
```

Full example

```
{    "schemas": [        "urn:scim:schemas:core:1.0",        "urn:scim:schemas:extension:enterprise:1.0",        "urn:scim:schemas:extension:slack:guest:1.0"    ],    "userName": "other_username",    "nickName": "slack_username",    "name": {        "familyName": "Last",        "givenName": "First",        "honorificPrefix": "Dr."    },    "displayName": "First Last",    "profileUrl": "https://login.example.com/slack_username",    "emails": [        {            "value": "thedoctor@gallifrey.com",            "type": "work",            "primary": true        },        {            "value": "some_other@email.com",            "type": "home"        }    ],    "addresses": [        {            "streetAddress": "1234 Doctor St",            "locality": "New York",            "region": "NY",            "postalCode": "12345",            "country": "USA",            "primary": true        }    ],    "phoneNumbers": [        {            "value": "555-555-5555",            "type": "work"        },        {            "value": "555-555-4444",            "type": "mobile"        }    ],    "photos": [        {            "value": "https://photos.example.com/profilephoto.jpg",            "type": "photo"        }    ],    "roles": [        {            "value": "Lead Detective",            "primary": "true"        }    ],    "userType": "Employee",    "title": "Detective",    "preferredLanguage": "en_US",    "locale": "en_US",    "timezone": "America/New York",    "active": true,    "password": "Doctor!Who??",    "urn:scim:schemas:extension:enterprise:1.0": {        "employeeNumber": "701984",        "costCenter": "4130",        "organization": "Torchwood",        "division": "Alien Investigations",        "department": "Detective Agency",        "manager": {            "managerId": "U123ABC456"        }    },    "urn:scim:schemas:extension:slack:guest:1.0": {        "type": "multi",        "expiration": "2020-11-30T23:59:59Z"    }}
```

### PATCH /Users/<id> {#patch-users-id}

Updates an existing user resource, overwriting values for specified attributes.

The value of the `<id>` should be the user's corresponding Slack ID, beginning with either `U` or `W`. Attributes that are not provided in the request will remain unchanged. Updating a value to `" "` will clear and remove the field from the user's profile.

:::info\[Updates to the `password`, `externalId`, and `profileUrl` attributes are not supported.

:::

active

Deactivate activated users by setting the `active` attribute equal to `false`. Alternatively, re-enable deactivated users by setting the `active` attribute equal to `true`.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "active": true}
```

userName

Updates to the `userName` attribute will also update the `nickName` attribute and vice versa.

The `userName` attribute _cannot_ be empty.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "userName": "other_username"}
```

nickName

Updates to the `nickName` attribute will also update the `userName` attribute and vice versa.

The `nickName` attribute _cannot_ be empty.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "nickName": "slack_username"}
```

displayName

Updates a user's Slack display name profile field. The following request will update the user's handle to **@First Last**.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "displayName": "First Last"}
```

title

Updates a user's `title` profile field.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "title": "Tour Guide"}
```

userType

Updates a user's `userType` profile field.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "userType": "Employee"}
```

preferredLanguage

Updates the user's preferred language profile field.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "preferredLanguage":"en_US"}
```

locale

Updates the user's locale profile field.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "locale": "en_US"}
```

timezone

Updates the user's timezone profile field.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "timezone": "America/Chicago"}
```

emails

Only two user emails are stored; the primary and secondary email. The primary email may be specified by setting the `primary` sub-attribute to `true`. If the `primary` sub-attribute is omitted, the `type` sub-attribute may be specified and set to `"work"`. Otherwise, if both the `primary` and `type` sub-attributes are omitted, the primary and secondary emails will be selected in the order they appear.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "emails": [        {            "value": "some@email.com",            "type": "work",            "primary": true        },        {            "value": "some_other@email.com",            "type": "home"        }    ]}
```

A user's primary email cannot be deleted, only updates are supported. Attempts to delete the primary email without providing a replacement value will result in a `missing_primary_email` error. However, the secondary email may be modified at will. For example, the following request will remove the secondary email.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "emails": [        {            "value": "some_other@email.com",            "operation": "delete"        }    ]}
```

The following request will only remove the secondary email.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "emails"        ]    }}
```

phoneNumbers

Only two user phone numbers are stored: the `primaryPhone` and `mobilePhone`. Updating numbers is done by setting one of the `primary` or `type` fields for each updated number.

The `type` field means different things depending on whether it's in the request or in the response

In the request, the `"type": "mobile"` field specifies the `primaryPhone`. In the response, `"type": "mobile"` is assigned to the `mobilePhone`.

**Only update** `primaryPhone`

Option

`primary` value

`type` value

Option 1

Option 2

`true`

Option 3

`false`

Option 4

`"mobile"`

**Example request (option 2)**

In this example, 123-333-3333 is set as the `primaryPhone`.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "phoneNumbers": [        {            "value": "123-333-3333",            "primary": true        }    ]}
```

**Only update** `mobilePhone`

`primary` value

`type` value

`"work"`

**Example request**

In this example, 123-333-3333 is set as the `mobilePhone`.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "phoneNumbers": [        {            "value": "123-333-3333",            "type": "work"        }    ]}
```

**Update both** `primaryPhone` **and** `mobilePhone` **with different values**

Option

`primaryPhone` `primary` value

`primaryPhone` `type` value

`mobilePhone` `primary` value

`mobilePhone` `type` value

Option 1

`true`

`false`

Option 2

`"mobile"`

`"work"`

Option 3

`true`

**Example Request (option 1)**

In this example, 222-222-2222 is set as the `mobilePhone` and 333-333-3333 is set as the `primaryPhone`.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "phoneNumbers": [        {            "value": "222-222-2222",            "primary": false        },        {            "value": "333-333-3333",            "primary": true        }    ]}
```

**Delete phone numbers**

The primary or secondary phone numbers may be deleted by specifying their respective values and setting the `operation` sub-attribute to `"delete"`. The following requests are equivalent; they will delete all of the user's phone numbers.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "phoneNumbers": [        {            "value": "555-555-5555",            "operation": "delete"        },        {            "value": "555-555-4444",            "operation": "delete"        }    ]}
```

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "phoneNumbers"        ]    }}
```

photos

Only one user photo is stored and used as the user's profile photo. The photo may be specified by setting the `primary` sub-attribute to `true`. If the `primary` sub-attribute is omitted, the first element in the `photos` array will be selected. The `value` sub-attribute for `photos` can either be a publicly accessible URL e.g. `"https://photos.example.com/profilephoto.jpg"`, or a Data URL containing raw image data, e.g. `"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..."`.

After a successful PATCH request, the response will not reflect the updated value immediately. It takes a few moments for the URL to be generated and propagated to the Slack client.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "photos": [        {            "value": "https://photos.example.com/profilephoto.jpg",            "primary": true        }    ]}
```

addresses

Only one user address is stored. The address may be specified by setting the `primary` sub-attribute to `true`. If the `primary` sub-attribute is omitted, the first element in the `addresses` array will be selected. Only the `streetAddress`, `locality`, `region`, `postalCode` and `country` sub-attributes are supported.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "addresses": [        {            "streetAddress": "1060 W Addison St",            "locality": "Chicago",            "region": "IL",            "postalCode": "60613",            "country": "USA",            "primary": true        }    ]}
```

To remove a user address, provide the `operation` sub-attribute set to `"delete"`. An address is only deleted if the `streetAddress`, `locality`, `region`, `postalCode` and `country` sub-attribute values all match the current value.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "addresses": [        {            "streetAddress": "1060 W Addison St",            "locality": "Chicago",            "region": "IL",            "postalCode": "60613",            "country": "USA",            "operation": "delete"        }    ]}
```

roles

Only one user role is stored. The SCIM spec does not specify a canonical type for the `roles` attribute so both of the following variations are accepted. The role may be specified by setting the `primary` sub-attribute to `true`. If the `primary` sub-attribute is omitted, the first element in the `roles` array will be selected.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "roles": [        {            "value": "Tech Lead",            "primary": true        }    ]}
```

or

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "roles": [        "Tech Lead"    ]}
```

To remove a user's role, provide the `operation` sub-attribute and set it to `"delete"`.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "roles": [        {            "value": "Tech Lead",            "operation": "delete"        }    ]}
```

name

Updates the user's name profile fields. Only the `familyName`, `givenName` and `honorificPrefix` sub-attributes are supported. To update all of the name sub-attributes in one request, use the following request:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "name": {        "familyName": "Last",        "givenName": "First",        "honorificPrefix": "Ms."    }}
```

Otherwise, specify only the sub-attributes to update.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "name": {        "givenName": "First"    }}
```

To remove a specific `name` sub-attribute, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "name.honorificPrefix"        ]    }}
```

To remove all of the `name` sub-attributes, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "name"        ]    }}
```

urn:scim:schemas:extension:enterprises:1.0

Updates a user's enterprise profile fields.

The `managerId` sub-attribute

If the `manager` sub-attribute is specified, the `managerId` sub-attribute _must_ be specified as well. The value for the `managerId` sub-attribute can be their valid Slack `id`, their primary `email`, or their `userName` attribute. Each request can use a different type of value for the `managerId` sub-attribute.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "urn:scim:schemas:extension:enterprise:1.0": {        "employeeNumber": "701984",        "costCenter": "4130",        "organization": "Chicago Cubs",        "division": "Wrigley Field",        "department": "Tour Operations",        "manager": {            "managerId": "U123ABC456"        }    }}
```

Otherwise, specify only the sub-attributes to update.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "urn:scim:schemas:extension:enterprise:1.0": {        "manager": {            "managerId": "ernie@example.com"        }    }}
```

To remove a specific `urn:scim:schemas:extension:enterprise:1.0` sub-attribute, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "urn:scim:schemas:extension:enterprise:1.0.manager.managerId"        ]    }}
```

To remove all of the `urn:scim:schemas:extension:enterprise:1.0` sub-attributes, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "urn:scim:schemas:extension:enterprise:1.0"        ]    }}
```

urn:scim:schemas:extension:slack:guest:1.0

Provisioning multi-channel guest users with the SCIM API is only available to Enterprise plan customers.

Converts a full member to a multi-channel guest, or converts a multi-channel guest to a full member.

##### Converting a full member to a multi-channel guest {#converting-a-full-member-to-a-multi-channel-guest}

If the full member is deactivated, this method will reactivate them on conversion.

To convert a full member to a multi-channel guest _with_ an expiration date, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0",		"urn:scim:schemas:extension:slack:guest:1.0"    ],    "urn:scim:schemas:extension:slack:guest:1.0": {        "type": "multi",        "expiration": "2020-11-30T23:59:59Z"    }}
```

To convert a full member to a multi-channel guest _without_ an expiration date, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0",		"urn:scim:schemas:extension:slack:guest:1.0"    ],    "urn:scim:schemas:extension:slack:guest:1.0": {        "type": "multi"    }}
```

To remove the expiration date from a multi-channel guest, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "urn:scim:schemas:extension:slack:guest:1.0.expiration"        ]    }}
```

##### Converting a multi-channel guest to a full member {#converting-a-multi-channel-guest-to-a-full-member}

If the multi-channel guest is deactivated, this method will reactivate them on conversion.

To convert a multi-channel guest to a full member, use:

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "urn:scim:schemas:extension:slack:guest:1.0"        ]    }}
```

urn:scim:schemas:extension:slack:profile:1.0

Updates the user's start date profile field.

```
{    "schemas": [        "urn:scim:schemas:extension:slack:profile:1.0"    ],    "urn:scim:schemas:extension:slack:profile:1.0": {        "startDate": "2024-04-10T00:00:00+0000"    },}
```

meta

To remove a specific attribute or sub-attributes, use the `meta.attributes` request.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "meta": {        "attributes": [            "roles",            "name.familyName",            "urn:scim:schemas:extension:enterprise:1.0.department"        ]    }}
```

### PUT /Users/<id> {#put-users-id}

Updates an existing user resource, overwriting all values for a user even if an attribute is empty or not provided.

If an attribute that had been set previously is left blank during a `PUT` operation, the new value will be blank in accordance with the data type of the attribute and the storage provider.

Deactivated users can be re-enabled by setting the `active` attribute to `true`. The value of the `<id>` should be the user's corresponding Slack ID, beginning with either `U` or `W`.

:::info\[Updates to the `externalId` attribute are not supported.

:::

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "id": "U123ABC456",    "active": false,    "userName": "other_username",    "nickName": "slack_username",    "name": {        "givenName": "First",        "familyName": "Last"    },    "title": "Ms.",    "emails": [        {            "value": "some@email.com",            "primary": true        }    ],    "photos": [        {            "value": "https://some.image/url",            "type": "photo"        }    ]}
```

### DELETE /Users/<id> {#delete-users-id}

Sets a Slack user to deactivated.

The value of the `<id>` should be the user's corresponding Slack ID, beginning with either `U` or `W`.

```
 DELETE /scim/v1/Users/42 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

Endpoint

Description

[`GET /Users`](#get-users-2)

Returns a paginated list of users

[`GET /Users/{id}`](#get-users-id-2)

Retrieves a single user resource

[`POST /Users`](#post-users-2)

Creates a user

[`PATCH /Users/{id}`](#patch-users-id-2)

Updates an existing user resource, overwriting specified values

[`PUT /Users/{id}`](#put-users-id-2)

Updates an existing user resource, overwriting all values

[`DELETE /Users/{id}`](#delete-users-id-2)

Sets a Slack user to deactivated

### User attributes {#user-attributes-2}

Attributes are the details associated with a user's account. These are the details that someone would typically set in their profile (for example, by clicking the **Edit Profile** button in the Slack application).

The following tables map SCIM attributes to the profile fields that Slack uses. Most of these profile fields are exposed directly in a person's profile in the Slack UI. Sometimes, multiple SCIM attributes map to a single Slack profile field. For example, Slack's **Display name** field will populate from either the `displayName` or the `userName` SCIM attribute, depending on which is set. If both are set, it will use `displayName`.

When you sync some user attributes to Slack via SCIM, these fields become locked in Slack and you can no longer delete them or edit them. However, you may choose to hide them from user profiles.

Attribute values will vary by identity provider. For example, some may use a single field for a user's full name, others may provide sub-attributes such as `givenName` and `familyName`, still others may provide both. Either is acceptable, but they should only describe the same name (i.e. sub-attributes should not contain additional or optional information, such as a nickname).

Not every attribute will be displayed in a user's profile. For example, `active` does not appear as a field but can be used to determine if a user's account is active.

Slack Profile Field

SCIM Attribute

Attribute Type

Notes

Username

`userName`

Singular

Required

Full Name

`name`, familyName

Singular

Nickname

`nickName`

Singular

Display Name

`displayName`, `userName`

Singular

Support periods `.`, underscores `_`, and hyphens `-`. All other special characters are converted to underscores. Max of 80 characters.

Email

`emails[0]['value']`

Multi-Valued

Required

Profile URL

`profileUrl`

Singular

Profile Photo

`photos[0]['values']`

Multi-Valued

Groups

`groups`

Multi-Valued

Title

`title`

Singular

Timezone

`timezone`

Singular

Active

`active`

Singular

Password

`password`

Singular

Never returned but can be used to set the initial password for a user if the team is not using an identity manager.

Start Date

`profile.startDate`

Singular

Date should be in the ISO 8601 format, such as `2024-04-10T00:00:00+0000`. Must provide the `urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User` schema in request body.

Slack will also create profile fields if the following SCIM attributes are present:

Custom Profile Field

SCIM Attribute

Attribute Type

Addresses

`addresses`

Multi-Valued

City

`addresses[primary]['locality']`

Singular

Cost Center

`enterprise.costCenter`

Singular

Country

`addresses[primary]['country']`

Singular

Department

`enterprise.department`

Singular

Division

`enterprise.division`

Singular

Employee ID

`enterprise.employeeNumber`

Singular

Honorific Prefix

`name.honorificPrefix`

Singular

Locale

`locale`

Singular

Manager

`enterprise.manager.managerId`

Singular

Organization

`enterprise.organization`

Singular

Phone

`phoneNumbers[0]['values']`

Multi-Valued

Preferred Language

`preferredLanguage`

Singular

Roles

`roles`

Multi-Valued

Title

`title`

Singular

UserType

`userType`

Singular

Zip Code

`addresses[primary]['postalCode']`

Singular

### GET /Users {#get-users-2}

#### Request {#request}

```
 GET /scim/v2/Users?startIndex=1&count=1 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

#### Response {#response}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:ListResponse"    ],    "Resources": [        {            "schemas": [                "urn:ietf:params:scim:schemas:core:2.0:User",                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",                "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"            ],            "id": "U123ABC456",            "externalId": "",            "meta": {                "created": "2022-05-27T15:19:18-07:00",                "location": "https://api.slack.com/scim/v2/Users/U123ABC456"            },            "userName": "pamela",            "nickName": "pam",            "name": {                "givenName": "Pam",                "familyName": "Halpert",                "honorificPrefix": "Mrs."            },            "displayName": "Jay",            "profileUrl": "https://aDoeenterpriseorg.enterprise.slack.com/team/pamela",            "title": "receptionist",            "timezone": "America/New_York",            "active": true,            "emails": [                {                    "value": "pamhalpert@slack-corp.com",                    "primary": true                },                {                    "value": "pam@slack-corp.com",                    "primary": false                }            ],            "photos": [                {                    "value": "https://s3-us-west-2.amazonaws.com/slack-files-dev2/avatars/2022-08-09/1139718205683_4f58e078d159d6e22a79_192.png",                    "type": "photo"                }            ],            "addresses": [                {                    "streetAddress": "1725 Slough Avenue",                    "locality": "Scranton",                    "region": "PA",                    "postalCode": "12345",                    "country": "USA"                }            ],            "phoneNumbers": [                {                    "value": "+1 555 555 1234",                    "type": "mobile"                },                {                    "value": "+1 555 555 5678",                    "primary": true                }            ],            "userType": "Employee",            "roles": [                {                    "value": "Sales Representative",                    "primary": true                }            ],            "preferredLanguage": "en_US",            "locale": "en_US",            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {                "employeeNumber": "SR-005",                "costCenter": "123456789",                "organization": "Dunder Mifflin Paper Company",                "division": "Scranton Branch",                "department": "Sales",                "manager": {                    "managerId": null                }            },            "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {                "startDate": "2024-04-10T00:00:00+0000"            },            "groups": []        }    ],    "totalResults": 1373,    "itemsPerPage": 1,    "startIndex": 1}
```

* * *

### GET /Users/<id> {#get-users-id-2}

#### Request {#request-1}

```
 GET /scim/v2/Users/U123ABC456 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

#### Response {#response-1}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "id": "U123ABC456",    "externalId": "",    "meta": {        "created": "2022-08-16T12:49:47-07:00",        "location": "https://api.slack.com/scim/v2/Users/U123ABC456"    },    "userName": "pamela",    "nickName": "pam",    "name": {        "givenName": "Pam",        "familyName": "Halpert",        "honorificPrefix": "Mrs."    },    "displayName": "PamHalpert123",    "profileUrl": "https://aDoeenterpriseorg.enterprise.slack.com/team/pamela",    "title": "receptionist",    "timezone": "America/Scranton",    "active": true,    "emails": [        {            "value": "pamhalpert@slack-corp.com",            "primary": true        },        {            "value": "pam@slack-corp.com",            "primary": false        }    ],    "photos": [        {            "value": "https://s3-us-west-2.amazonaws.com/slack-files-dev2/avatars/2023-02-19/1152719686210_6e95789b151a47536455_192.png",            "type": "photo"        }    ],    "addresses": [        {            "streetAddress": "1725 Slough Avenue",            "locality": "Scranton",            "region": "North America",            "postalCode": "12345",            "country": "US"        }    ],    "phoneNumbers": [        {            "value": null,            "type": "mobile"        },        {            "value": "4168312999",            "primary": true        }    ],    "userType": null,    "roles": [        {            "value": "role 1",            "primary": true        }    ],    "preferredLanguage": null,    "locale": "en-US",    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {        "employeeNumber": "123",        "costCenter": null,        "organization": "Dunder Mifflin Paper Company",        "division": "Scranton Branch",        "department": "Sales",        "manager": {            "managerId": null        }    },    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {        "startDate": "2024-04-10T00:00:00+0000"    },    "groups": [        {            "value": "S123ABC456",            "display": "SCIM V2 Test Group"        }    ]}
```

* * *

### POST /Users {#post-users-2}

#### Request {#request-2}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "userName": "some_fake_username",    "nickName": "some_fake_username",    "name": {        "familyName": "Last",        "givenName": "First",        "honorificPrefix": "Ms."    },    "displayName": "First Last",    "profileUrl": "https://login.example.com/some_fake_username",    "emails": [        {            "value": "some_fake_user@email.com",            "type": "work",            "primary": true        },        {            "value": "some_other@email.com",            "type": "home"        }    ],    "addresses": [        {            "streetAddress": "1060 W Addison St",            "locality": "Chicago",            "region": "IL",            "postalCode": "60613",            "country": "USA",            "primary": true        }    ],    "phoneNumbers": [        {            "value": "555-555-5555",            "type": "work"        },        {            "value": "555-555-4444",            "type": "mobile"        }    ],    "photos": [        {            "value": "https://photos.example.com/profilephoto.jpg",            "type": "photo"        }    ],    "roles": [        {            "value": "Tech Lead",            "primary": "true"        }    ],    "userType": "Employee",    "title": "Tour Guide",    "preferredLanguage": "en_US",    "locale": "en_US",    "timezone": "America/Chicago",    "active": true,    "password": "Cub$winCub$win!!",    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {        "employeeNumber": "701984",        "costCenter": "4130",        "organization": "Chicago Cubs",        "division": "Wrigley Field",        "department": "Tour Operations",        "manager": {            "managerId": "U123ABC456"        }    },    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {        "startDate": "2024-04-10T00:00:00+0000"    }}
```

#### Response {#response-2}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "id": "U123ABC456",    "externalId": "",    "meta": {        "created": "2023-02-20T14:33:21-08:00",        "location": "https://api.slack.com/scim/v2/Users/U123ABC456"    },    "userName": "some_fake_username",    "nickName": "some_fake_username",    "name": {        "givenName": "First",        "familyName": "Last",        "honorificPrefix": "Ms."    },    "displayName": "First Last",    "profileUrl": "https://login.example.com/some_fake_username",    "title": "Tour Guide",    "timezone": "America/Chicago",    "active": true,    "emails": [        {            "value": "some_fake_user@email.com",            "primary": true        },        {            "value": "some_other@email.com",            "primary": false        }    ],    "photos": [        {            "value": "https://secure.gravatar.com/avatar/a27ac11dd7b9af585d8fb54cbd0921e8.jpg?s=192&d=https%3A%2F%2Fslack.com%2Fdev-cdn%2Fv1676505571%2Fimg%2Favatars%2Fuser_shapes%2Fava_0018-192.png",            "type": "photo"        }    ],    "addresses": [        {            "streetAddress": "1060 W Addison St",            "locality": "Chicago",            "region": "IL",            "postalCode": "60613",            "country": "USA"        }    ],    "phoneNumbers": [        {            "value": "555-555-5555",            "type": "mobile"        },        {            "value": "555-555-4444",            "primary": true        }    ],    "userType": "Employee",    "roles": [        {            "value": "Tech Lead",            "primary": true        }    ],    "preferredLanguage": "en_US",    "locale": "en_US",    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {        "employeeNumber": "701984",        "costCenter": "4130",        "organization": "Chicago Cubs",        "division": "Wrigley Field",        "department": "Tour Operations",        "manager": {            "managerId": "U123ABC456"        }    },    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {        "startDate": "2024-04-10T00:00:00+0000"    },    "groups": []}
```

### POST /Users (Multi-Channel Guest Users) {#post-users-guest-2}

#### Request {#request-3}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User"    ],    "userName": "guestUser",    "displayName": "TestGuestUser",    "emails": [        {            "value": "some_guest_email@fake.com"        }    ],    "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User": {        "type": "multi"    }}
```

#### Response {#response-3}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User"    ],    "id": "U123ABC456",    "externalId": "",    "meta": {        "created": "2023-02-20T14:28:23-08:00",        "location": "https://api.slack.com/scim/v2/Users/U123ABC456"    },    "userName": "guestuser",    "nickName": "guestuser",    "name": {        "givenName": "TestGuestUser",        "familyName": ""    },    "displayName": "TestGuestUser",    "profileUrl": "https://aDoeenterpriseorg.enterprise.slack.com/team/guestuser",    "title": "",    "timezone": "America/Los_Angeles",    "active": true,    "emails": [        {            "value": "some_guest_email@fake.com",            "primary": true        }    ],    "photos": [        {            "value": "https://secure.gravatar.com/avatar/2572f0dc723e0a547a14c5a472740cf6.jpg?s=192&d=https%3A%2F%2Fslack.com%2Fdev-cdn%2Fv1676505571%2Fimg%2Favatars%2Fuser_shapes%2Fava_0011-192.png",            "type": "photo"        }    ],    "groups": [],    "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User": {        "type": "multi"    }}
```

* * *

### PUT /Users/<id> {#put-users-id-2}

#### Request {#request-4}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "externalId": "",    "userName": "updated_username",        "emails": [        {            "value": "some_updated_username@email.com",            "type": "work",            "primary": true        },        {            "value": "some_other@email.com",            "type": "home"        }    ],}
```

#### Response {#response-4}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "id": "U123ABC456",    "externalId": "",    "meta": {        "created": "2022-08-16T12:49:47-07:00",        "location": "https://api.slack.com/scim/v2/Users/U123ABC456"    },    "userName": "updated_username",    "nickName": "updated_username",    "name": {        "givenName": "Jay",        "familyName": "Doe",        "honorificPrefix": null    },    "displayName": "",    "profileUrl": "https://aDoeenterpriseorg.enterprise.slack.com/team/updated_username",    "title": "",    "timezone": "America/Los_Angeles",    "active": false,    "emails": [        {            "value": "some_updated_username@email.com",            "primary": true        },        {            "value": "some_other@email.com",            "primary": false        }    ],    "photos": [        {            "value": "https://secure.gravatar.com/avatar/ca904af062782178167c3790cb28940a.jpg?s=192&d=https%3A%2F%2Fslack.com%2Fdev-cdn%2Fv1676505571%2Fimg%2Favatars%2Fuser_shapes%2Fava_0001-192.png",            "type": "photo"        }    ],    "addresses": [        {            "streetAddress": null,            "locality": null,            "region": null,            "postalCode": null,            "country": null        }    ],    "phoneNumbers": [        {            "value": null,            "type": "mobile"        },        {            "value": null,            "primary": true        }    ],    "userType": null,    "roles": [        {            "value": null,            "primary": true        }    ],    "preferredLanguage": null,    "locale": null,    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {        "employeeNumber": null,        "costCenter": null,        "organization": null,        "division": null,        "department": null,        "manager": {            "managerId": null        }    },    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {        "startDate": null    }    "groups": []}
```

* * *

### PATCH /Users/<id> {#patch-users-id-2}

#### Request {#request-5}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "op": "add",            "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:employeeNumber",            "value": "121"        },        {            "op": "add",            "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User:costCenter",            "value": "001919"        },        {            "op": "remove",            "path": "address"        }    ]}
```

#### Response {#response-5}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:User",        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "id": "U123ABC456",    "externalId": "",    "meta": {        "created": "2022-08-16T12:49:47-07:00",        "location": "https://api.slack.com/scim/v2/Users/U123ABC456"    },    "userName": "updated_username",    "nickName": "updated_username",    "name": {        "givenName": "Jay",        "familyName": "Doe",        "honorificPrefix": null    },    "displayName": "",    "profileUrl": "https://aDoeenterpriseorg.enterprise.slack.com/team/updated_username",    "title": "",    "timezone": "America/Los_Angeles",    "active": false,    "emails": [        {            "value": "some_updated_username@email.com",            "primary": true        },        {            "value": "some_other@email.com",            "primary": false        }    ],    "photos": [        {            "value": "https://secure.gravatar.com/avatar/ca904af062782178167c3790cb28940a.jpg?s=192&d=https%3A%2F%2Fslack.com%2Fdev-cdn%2Fv1676505571%2Fimg%2Favatars%2Fuser_shapes%2Fava_0001-192.png",            "type": "photo"        }    ],    "addresses": [        {            "streetAddress": null,            "locality": null,            "region": null,            "postalCode": null,            "country": null        }    ],    "phoneNumbers": [        {            "value": null,            "type": "mobile"        },        {            "value": null,            "primary": true        }    ],    "userType": null,    "roles": [        {            "value": null,            "primary": true        }    ],    "preferredLanguage": null,    "locale": null,    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {        "employeeNumber": "121",        "costCenter": "001919",        "organization": null,        "division": null,        "department": null,        "manager": {            "managerId": null        }    },    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {        "startDate": "2024-04-10T00:00:00+0000"    },    "groups": []}
```

#### Using PATCH /Users/<id> with specific attributes {#attributes-2}

info

If the manager sub-attribute is specified, the managerId sub-attribute must be specified as well. The value for the managerId sub-attribute can be their valid Slack id, their primary email, or their userName attribute. Each request can use a different type of value for the managerId sub-attribute.

activate

Deactivate activated users by setting the `active` attribute equal to `false`. Alternatively, re-enable deactivated users by setting the `active` attribute equal to `true`.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "active",            "op": "replace",            "value": true        }    ]}
```

userName

Updates to the `userName` attribute will also update the `nickName` attribute and vice versa.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "userName",            "op": "replace",            "value": "other_username"        }    ]}
```

nickName

Updates to the `nickName` attribute will also update the `userName` attribute and vice versa.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "nickName",            "op": "replace",            "value": "slack_username"        }    ]}
```

displayName

Updates a user's Slack display name profile field. The following request will update the user's handle to @First Last.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "displayName",            "op": "replace",            "value": "First Last"        }    ]}
```

title

Updates a user's title profile field.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "title",            "op": "replace",            "value": "Tour Guide"        }    ]}
```

userType

Updates a user's `userType` profile field.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "userType",            "op": "replace",            "value": "Employee"        }    ]}
```

preferredLanguage

Updates the user's preferred language profile field

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "preferredLanguage",            "op": "replace",            "value": "en_US"        }    ]}
```

locale

Updates the user's locale profile field.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "locale",            "op": "replace",            "value": "en_US"        }    ]}
```

timezone

Updates the user's timezone profile field.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "timezone",            "op": "replace",            "value": "America/Chicago"        }    ]}
```

emails

Only two user emails are stored; the primary and secondary email. The primary email may be specified by setting the `primary` sub-attribute to `true`. If the `primary` sub-attribute is omitted, the `type` sub-attribute may be specified and set to `"work"`. Otherwise, if both the `primary` and `type` sub-attributes are omitted, the primary and secondary emails will be selected in the order they appear.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "emails",            "op": "add",            "value": [                {                    "value": "some@email.com",                    "type": "work",                    "primary": true                },                {                    "value": "some_other@email.com",                    "type": "home"                }            ]        }    ]}
```

Alternatively, you can add a single email entry using

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "emails",            "op": "add",            "value": {                "value": "some_other@email.com",                "type": "home"            }        }    ]}
```

You can also replace a secondary email using the following

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "emails[primary eq false]",            "op": "replace",            "value": {                "value": "some_other_replaced@email.com",                "type": "work"            }        }    ]}
```

A user's primary email cannot be deleted, only updates are supported. Attempts to delete the primary email without providing a replacement value will result in a `missing_primary_email` error. However, the secondary email may be modified at will. For example, the following request will remove the secondary email.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "emails[primary eq false]",            "op": "remove"        }    ]}
```

or

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "emails[value eq \"some_other@email.com\"]",            "op": "remove"        }    ]}
```

The following request will only remove the secondary email.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "emails",            "op": "remove"        }    ]}
```

phoneNumbers

Only two user phone numbers are stored: the `primaryPhone` and `mobilePhone`. Updating numbers is done by setting one of the `primary` or `type` fields for each updated number.

In this example, 123-333-3333 is set as the primaryPhone.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "phoneNumbers",            "op": "add",            "value": {                "value": "123-333-3333",                "primary": true             }        }    ]}
```

In this example, 123-333-3333 is set as the mobilePhone.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "phoneNumbers",            "op": "add",            "value": [                {                    "value": "123-333-3333",                    "type": "work"                }            ]        }    ]}
```

In this example, 222-222-2222 is set as the mobilePhone and 333-333-3333 is set as the primaryPhone.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "phoneNumbers",            "op": "add",            "value": [                {                    "value": "222-222-2222",                    "primary": false                },                {                    "value": "333-333-3333",                    "primary": true                }            ]        }    ]}
```

The primary or secondary phone numbers may be deleted by specifying their respective values using the remove operation. The following request will delete all of the user's phone numbers.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "phoneNumbers[value eq \"333-333-3333\"]",            "op": "remove"        },        {            "path": "phoneNumbers[value eq \"222-222-2222\"]",            "op": "remove"        }    ]}
```

or

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "phoneNumbers",            "op": "remove"        }    ]}
```

The primary or secondary phone number value can be replaced using the “replace operation”. The following request will replace the phoneNumber value with 222-222-2222 to 111-111-111.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "phoneNumbers[value eq \"333-333-3333\"].value",            "op": "replace",            "value": "111-111-111"        }    ]}
```

photos

Only one user photo is stored and used as the user's profile photo. The photo may be specified by setting the `primary` sub-attribute to `true`. If the `primary` sub-attribute is omitted, the first element in the `photos` array will be selected. The `value` sub-attribute for `photos` can either be a publicly accessible URL e.g. `"https://photos.example.com/profilephoto.jpg"`, or a Data URL containing raw image data, e.g. `"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA..."`.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "photos",            "op": "add",            "value": [                {                    "value": "https://photos.example.com/profilephoto.jpg",                    "primary": true                }            ]        }    ]}
```

addresses

Only one user address is stored. The address may be specified by setting the primary sub-attribute to true. If the primary sub-attribute is omitted, the first element in the addresses array will be selected. Only the streetAddress, locality, region, postalCode and country sub-attributes are supported.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "addresses",            "op": "add",            "value": [{                "streetAddress": "1060 W Addison St",                "locality": "Chicago",                "region": "IL",                "postalCode": "60613",                "country": "USA",                "primary": true            }]        }    ]}
```

To remove a user address, use the remove operation.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "addresses",            "op": "remove"        }    ]}
```

roles

Only one user role is stored. The SCIM spec does not specify a canonical type for the roles attribute so both of the following variations are accepted. The role may be specified by setting the primary sub-attribute to true. If the primary sub-attribute is omitted, the first element in the roles array will be selected.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "roles",            "op": "add",            "value": [                {                    "value": "Tech Lead",                    "primary": true                }            ]        }    ]}
```

or

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "roles",            "op": "add",            "value": ["Tech Lead"]        }    ]}
```

To remove a user's role, use the operation “remove”.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "roles",            "op": "remove"        }    ]}
```

name

Updates the user's name profile fields. Only the familyName, givenName and honorificPrefix sub-attributes are supported. To update all of the name sub-attributes in one request, use the following request:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "name",            "op": "add",            "value": {                "familyName": "Last",                "givenName": "First",                "honorificPrefix": "Ms."            }        }    ]}
```

Otherwise, specify only the sub-attributes to update using the “replace” operation.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "name.givenName",            "op": "replace",            "value": "First"        }    ]}
```

To remove a specific name sub-attribute, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "name.honorificPrefix",            "op": "remove"        }    ]}
```

urn:ietf:params:scim:schemas:extension:enterprise:2.0:User

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",            "op": "add",            "value": {                "employeeNumber": "701984",                "costCenter": "4130",                "organization": "Chicago Cubs",                "division": "Wrigley Field",                "department": "Tour Operations",                "manager": {                    "managerId": "U123ABC456"                }            }        }    ]}
```

Otherwise, specify only the sub-attributes to update.

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",            "op": "replace",            "value": {                "manager": {                    "managerId": "U123ABC456"                }            }        }    ]}
```

To remove a specific urn:ietf:params:scim:schemas:extension:enterprise:2.0:User sub-attribute, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User.manager.managerId",            "op": "remove"        }    ]}
```

To remove all of the urn:ietf:params:scim:schemas:extension:enterprise:2.0:User sub-attributes, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",            "op": "remove"        }    ]}
```

urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User

Provisioning multi-channel guest users with the SCIM API is only available to Enterprise plan customers.

Converts a full member to a multi-channel guest, or converts a multi-channel guest to a full member.

##### Converting a full member to a multi-channel guest {#converting-a-full-member-to-a-multi-channel-guest-1}

If the full member is deactivated, this method will reactivate them on conversion.

To convert a full member to a multi-channel guest _with_ an expiration date, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User",            "op": "add",            "value": {                "type": "multi",                "expiration": "2024-11-30T23:59:59Z"            }        }    ]}
```

To convert a full member to a multi-channel guest _without_ an expiration date, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User",            "op": "add",            "value": {                "type": "multi"            }        }    ]}
```

To remove the expiration date from a multi-channel guest, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User.expiration",            "op": "remove"        }    ]}
```

##### Converting a multi-channel guest to a full member {#converting-a-multi-channel-guest-to-a-full-member-1}

If the multi-channel guest is deactivated, this method will reactivate them on conversion.

To convert a multi-channel guest to a full member, use:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "path": "urn:ietf:params:scim:schemas:extension:slack:guest:2.0:User",            "op": "remove"        }    ]}
```

urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User

Updates the user's start date profile field.

```
{    "schemas": [        "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User"    ],    "urn:ietf:params:scim:schemas:extension:slack:profile:2.0:User": {        "startDate": "2024-04-10T00:00:00+0000"    },}
```

* * *

### DELETE /Users/<id> {#delete-users-id-2}

#### Request {#request-6}

```
 DELETE /scim/v2/Users/42 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

#### Response {#response-6}

```
204
```

## Groups {#groups}

Groups are for organizing users in logical divisions across a workspace, such as by team or affinity.

*   v1.1
*   v2.0

Endpoint

Description

[`GET /Groups/`](#get-groups)

Returns a paginated list of groups

[`GET /Groups/<id>`](#get-groups-id)

Retrieves a single group resource

[`POST /Groups`](#post-groups)

Creates a new group

[`PATCH /Groups/<id>`](#patch-groups-id)

Updates an existing group resource

[`PUT /Groups/<id>`](#patch-groups-id)

Updates an existing group resource, overwriting all values

[`DELETE /Groups/<id>`](#delete-groups-id)

Permanently removes a group

### Group attributes {#group-attributes}

Attributes are the details associated with a group.

Slack Group Field

SCIM Attribute

Attribute Type

Required

Name

`displayName`

String

Required

Members

`members`

Multi-valued

Required

### GET /Groups {#get-groups}

Returns a paginated list of groups, ten groups per page by default.

Use the `startIndex` and `count` (max 1000) query parameters to paginate long lists of groups. [Pagination will be required](/changelog/2019-06-have-scim-will-paginate) as of August 30, 2019.

```
 GET /scim/v1/Groups?startIndex=4&count=500 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

### GET /Groups/<id> {#get-groups-id}

Retrieves a single group resource.

```
 GET /scim/v1/Groups/42 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

### POST /Groups {#post-groups}

Creates a new group.

Must include the `displayName` attribute (as defined in the [schema specification](#get-schemas-groups)). Users (regular and/or multi-channel guest users) can be added to the group during creation by supplying the Slack user ID values in the `members` array attribute.

Although 15,000 users can be added per call, we recommend a batch size of no more than 5,000 users.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "displayName": "Group Name",    "members": [        {            "value": "U111AAA111"        },        {            "value": "U222BBB222"        }    ]}
```

### PATCH /Groups/<id> {#patch-groups-id}

Updates an existing group resource, allowing individual (or groups of) users (regular and/or multi-channel guest users) to be added or removed from the group with a single operation.

Setting the `operation` attribute of a member object to `delete` will remove members from a group; `add` is the default operation for PATCH. [More details on editing a resource with PATCH](http://www.simplecloud.info/specs/draft-scim-api-00.html#edit-resource-with-patch).

Although 15,000 users can be modified per call, we recommend a batch size of no more than 5,000 users.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "members": [        {            "value": "U111AAA111"        },        {            "value": "U222BBB222",            "operation": "delete"        },        {            "value": "U333CCC333"        }    ]}
```

### PUT /Groups/<id> {#put-groups-id}

Updates an existing group resource, overwriting all values for a group even if an attribute is empty or not provided.

PUT will replace all members of a group with those members provided via the `members` attribute. If an attribute that had been set previously is left blank during a `PUT` operation, the new value will be blank in accordance with the data type of the attribute and the storage provider.

Although 15,000 users can be modified per call, we recommend a batch size of no more than 5,000 users.

```
{    "schemas": [        "urn:scim:schemas:core:1.0"    ],    "displayName": "New Group Name",    "members": [        {            "value": "U111AAA111"        }    ]}
```

### DELETE /Groups/<id> {#delete-groups-id}

Permanently removes a group (members are not deleted, only the group). In an Enterprise organization, deleting an IDP group connected to workspaces will not remove connected members from the workspace. To do so, disconnect the IDP group from the workspace(s) in the Org Dashboard before deleting the group.

```
 DELETE /scim/v1/Groups/42 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

Endpoint

Description

[`GET /Groups/`](#get-groups-2)

Returns a paginated list of groups

[`GET /Groups/{id}`](#get-groups-id-2)

Retrieves a single group resource

[`POST /Groups`](#post-groups-2)

Creates a new group

[`PATCH /Groups/{id}`](#patch-groups-id-2)

Updates an existing group resource

[`PUT /Groups/{id}`](#patch-groups-id-2)

Updates an existing group resource, overwriting all values

[`DELETE /Groups/{id}`](#delete-groups-id-2)

Permanently removes a group

### Group attributes {#group-attributes-2}

Attributes are the details associated with a group.

Slack Group Field

SCIM Attribute

Attribute Type

Required

Name

`displayName`

String

Required

Members

`members`

Multi-valued

Required

### GET /Groups {#get-groups-2}

#### Request {#request-7}

```
 GET /scim/v2/Groups?startIndex=1&count=1 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

#### Response {#response-7}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:ListResponse"    ],    "Resources": [        {            "schemas": [                "urn:ietf:params:scim:schemas:core:2.0:Group"            ],            "id": "S123ABC456",            "meta": {                "created": "2022-07-26T14:05:41-07:00",                "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"            },            "displayName": "SOMETHING NEW",            "members": []        }    ],    "totalResults": 15,    "itemsPerPage": 1,    "startIndex": 1}
```

* * *

### GET /Groups/<id> {#get-groups-id-2}

#### Request {#request-8}

```
 GET /scim/v2/Groups/S123ABC456 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

#### Response {#response-8}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "id": "S123ABC456",    "meta": {        "created": "2023-02-10T07:36:51-08:00",        "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"    },    "displayName": "Applications-600",    "members": [        {            "value": "U123ABC456",            "display": "Lexus Powlowski"        },        {            "value": "U123ABC456",            "display": "Porter Prosacco"        }    ]}
```

* * *

### POST /Groups {#post-groups-2}

#### Request {#request-9}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "displayName": "Some Group Name",    "members": [        {            "value": "U123ABC456"        }    ]}
```

#### Response {#response-9}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "id": "S123ABC456",    "meta": {        "created": "2023-02-20T15:10:03-08:00",        "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"    },    "displayName": "Some Group Name",    "members": [        {            "value": "U123ABC456",            "display": "example"        }    ]}
```

* * *

### PUT /Groups/<id> {#put-groups-id-2}

#### Request {#request-10}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "displayName": "Updated Group Name"}
```

#### Response {#response-10}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "id": "S123ABC456",    "meta": {        "created": "2023-02-20T15:10:03-08:00",        "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"    },    "displayName": "Updated Group Name",    "members": []}
```

* * *

### PATCH /Groups/<id> {#patch-groups-id-2}

#### Request {#request-11}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "op": "replace",            "path": "members",            "value": [                {                    "value": "U123ABC456"                },                {                    "value": "U999ABC456"                }            ]        }    ]}
```

#### Response {#response-11}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "id": "S123ABC456",    "meta": {        "created": "2023-02-20T15:10:03-08:00",        "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"    },    "displayName": "Updated Group Name",    "members": [        {            "value": "U123ABC456",            "display": "Jay Doe"        },        {            "value": "U222ABC222",            "display": "Kay Doe"        }    ]}
```

#### Remove all existing members {#remove-all-existing-members}

##### Request {#request-12}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "op": "remove",            "path": "members"        }    ]}
```

##### Response {#response-12}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "id": "S123ABC456",    "meta": {        "created": "2023-02-20T15:10:03-08:00",        "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"    },    "displayName": "Updated Group Name",    "members": []}
```

#### Remove a single member {#remove-a-single-member}

##### Request {#request-13}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "op": "remove",            "path":"members[value eq U123ABC456]"        }    ]}
```

* * *

### DELETE /Groups/<id> {#delete-groups-id-2}

In an Enterprise organization, deleting an IDP group connected to workspaces will not remove connected members from the workspace. To do so, disconnect the IDP group from the workspace(s) in the Org Dashboard before deleting the group.

##### Request {#request-14}

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:PatchOp"    ],    "Operations": [        {            "op": "remove",            "path": "members"        }    ]}
```

##### Response {#response-13}

```
{    "schemas": [        "urn:ietf:params:scim:schemas:core:2.0:Group"    ],    "id": "S123ABC456",    "meta": {        "created": "2023-02-20T15:10:03-08:00",        "location": "https://api.slack.com/scim/v2/Groups/S123ABC456"    },    "displayName": "Updated Group Name",    "members": []}
```

## Filter {#filter}

*   v1.1
*   v2.0

For methods that return a list, such as `GET /Users`, it's possible to filter the list by the `username`, `email`, `restricted`, and `ultra_restricted` attributes, and return only the values matching that filter. The following rules apply:

*   The filter parameter must contain one valid boolean operator
*   Each expression must contain an **attribute name** followed by an **attribute operator**, (also supports an **optional value**)
*   Multiple expressions may be combined using two logical operators.
*   Expressions can be grouped together using "( )"
*   Expressions must be evaluated using standard order of operations
*   String literals must be valid JSON strings

The following is a list of valid operators:

Operator

Description

eq

`equal`

co

`contains`

sw

`starts with`

pr

`present value`

gt

`greater than`

ge

`greater than or equal`

lt

`less than`

le

`less than or equal`

and

`logical And`

or

`logical Or`

Attribute name and attribute operator are case insensitive. For example, the following two expressions will evaluate to the same logical value:

```
filter=userName Eq "Carly"filter=username eq "carly"
```

Filters may be applied to the `username` and `email` [user attributes](#user-attributes), with the addition of two membership filters:

Attribute Name

SCIM Attribute

Attribute Type

Multi-Channel-Guest

`restricted`

Singular

Single-Channel-Guest

`ultra_restricted`

Singular

The following would return a list of all multi-channel guests of a workspace:

```
 GET /scim/v1/Users?filter=restricted eq '1' HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-4956040672-4956040692-6476208902-xxxxxx
```

Not applicable to SCIM v2.0.

## Errors {#errors}

Occasionally, interacting with our APIs will result in an error instead of the result you're expecting. Slack will make every attempt to respond with a descriptive error message that will help you figure out what went wrong and how to fix it.

Error

Description

`addresses_invalid`

The `addresses` attribute provided is invalid.

`bad_email_address`

The email address provided does not exist or was poorly formatted.

`bad_endpoint`

The endpoint URL does not exist.

`cannot_make_user_guest`

Admins, Owners and Primary owners cannot be made guests via SCIM.

`cannot_decode_user_id`

The given user ID cannot be decoded.

`cannot_modify_owner`

A Workspace's ownership can not be modified via SCIM, please use the Slack admin.

`cannot_modify_gdpr`

Users who have had their personal information forgotten under GDPR can not be modified.

`cannot_disable_bot_user_with_scim`

The SCIM API can not be used to deactivate a bot user, this must be done via the bot admin.

`cannot_disable_primary_owner`

The primary owner of a Workspace can not be deactivated. If this user needs to be deactivated, please make another team member the primary owner first.

`email_empty`

The user's primary email is missing from the request.

`email_invalid`

The provided user email values are invalid.

`email_taken`

The provided user email value already exists.

`emails_invalid`

The `emails` attribute provided is invalid.

`failed_to_remove_users_for_linked_subteam`

An error occurred when removing users from this IDP group.

`group_members_create_failed`

An error occurred during an update to a user group.

`group_member_max_exceeded`

15k is the recommended limit for IDP groups, The maximum is 5k for user groups. Additional users cannot be added unless some are removed.

`group_creation_failed`

The request to create a user group has failed.

`groups_invalid`

The `groups` attribute provided is invalid.

`idp_group_linked_to_channels`

This IDP group is linked to one or more channels via `admin.conversations.restrictAccess.addGroup`. You must call `admin.conversations.restrictAccess.removeGroup` for each link before you can delete the group.

`improper_enterprise_schema_format`

The `urn:scim:schemas:extension:enterprise:1.0.manager` sub-attribute is missing the required `managerId` sub-attribute.

`incomplete_filter`

A malformed filter query has been specified. Please check that the filter are separated by a single space. `filter=attribute eq "value"`

`invalid_attribute_format`

A singular or multi-valued attribute has been specified with the wrong type.

`invalid_authentication`

There's a problem with the OAuth token. It may not have been granted the proper `admin` scope or may not have been installed by an administrator. The token may also be malformed or not properly sent via an Authorization header with a type of Bearer.

`invalid_display_name`

The provided display name is not allowed. Only send the display name from your IDP upon account creation (not upon subsequent updates or to sync to a Slack account), or disable the [**Allow users to change their display name**](https://my.slack.com/admin/auth/saml) setting.

`invalid_emoji_not_allowed`

An attribute value contains an emoji.

`invalid_filter_group`

The provided filter contains a group that is malformed.

`invalid_name_maxlength`

The provided display name is not allowed because it exceeds the maximum allowable characters.

`invalid_name_specials`

The provided display name is not allowed because it is using invalid special characters such as `@`.

`invalid_name_required`

Only a string containing spaces has been provided for both the `givenName` and `familyName` sub-attributes.

`invalid_query`

There's a problem with the filter parameter. Please check that the entities and operators are valid.

`invalid_request_payload`

The provided request payload may contain unsupported attributes or properties.

`invalid_reserved_word`

A reserved word has been specified in an attribute.

`invalid_starts_with_at`

The `displayName` attribute value provided starts with an `@`

`invalid_sort_order`

The `sortOrder` parameter is not equal to `ascending` or `descending`.

`long_nickname`

The `nickName` parameter is longer than we allow. Max length is 21 characters.

`method_not_allowed`

Unsupported http method provided. Only `GET`, `POST`, `PUT`, `PATCH` and `DELETE` are supported.

`missing_authentication`

The authentication token is missing.

`missing_primary_email`

The request is attempting to remove the primary email without providing a replacement value.

`missing_schema_element`

The `schemas` attribute is missing from the request.

`missing_group_id`

The group ID has not been specified.

`missing_user_id`

The user ID has not been specified.

`no_filters`

The filter query parameter was provided but no filters were specified.

`no_such_group`

The group provided does not exist.

`no_such_group_members`

The group members provided do not exist.

`no_such_user`

The user provided does not exist.

`non_org_teams_only`

When using SCIM in an Enterprise organization, the app must be installed on the organization, not individual workspaces. SCIM methods are called against the entire org organization.

`query_building_failed`

The provided filter did not translate to a proper database query.

`database_query_failure`

An error was encountered while executing a filter.

`password_change_not_allowed`

Updates to the `password` attribute via SCIM is prohibited.

`permission_denied`

The OAuth token has not been granted permission to perform the requested action.

`phoneNumbers_invalid`

The `phoneNumbers` attribute provided is invalid.

`photos_invalid`

The `photos` attribute provided is invalid.

`plus_teams_only`

The SCIM APIs are only available for Business+ and Enterprise plans. SCIM access is not available for Free and Pro plans.

`primary_owner_check_failure`

The primary owner of a Workspace within an organization can not deactivated. If this user needs to be deactivated, please make another team member the primary owner first.

`resource_locked`

The app is making too many requests over a short period of time for group update requests. Please make fewer requests to stay within Slack's rate limits.

`roles_invalid`

The `roles` attribute provided is invalid.

`too_many_requests`

The app is making too many requests over a short period of time. Please make fewer requests to stay within Slack's rate limits.

`too_many_users`

The request to update a Group contains more than 15,000 users. Please make the request with smaller batches of users.

`truncation_error`

The `userName` could not be truncated in an attempt to avoid a username conflict for the organization.

`unable_to_add_deleted_or_guest_to_group`

Deleted or guest users cannot be added to the Group.

`unable_to_create_team_profile_fields`

An error occurred during custom profile creation.

`unknown_user`

The user provided does not exist.

`unsupported_version`

The provided SCIM version is not supported.

`user_creation_failed`

The specified user already exists or an error was encountered when attempting to create a user.

`username_empty`

The `userName` attribute is empty when the user's endpoint is invoked via `PUT` or `POST`

`username_invalid`

The `userName` attribute provided is invalid.

`username_not_allowed`

The provided `userName` is reserved.

`username_required`

This method requires a username parameter.

`username_taken`

When provisioning a new user via SCIM, usernames must be unique and must also be unique from channel names.

`username_too_long`

The specified username is too long (max length is 21 characters).

### Example error {#example-error}

The following is an example error using SCIM v2.0:

```
{    "schemas": [        "urn:ietf:params:scim:api:messages:2.0:Error"    ],    "detail": "missing_schema_element",    "status": 400}
```

## Concurrency {#concurrency}

The SCIM API only allows one update to a user or group at a time (by locking the user or group while the update is in progress). Locking prevents overlapping requests, which can cause unpredictable results.

As a consequence, if you attempt to send multiple non-GET requests to the same user or group, and that user or group is still being updated from a previous request, you'll see a 429 HTTP response code. The 429 code will be returned with a retry-after header—wait for the time specified in that header to resend the request.