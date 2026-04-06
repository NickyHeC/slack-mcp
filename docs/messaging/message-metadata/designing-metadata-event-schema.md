Source: https://docs.slack.dev/messaging/message-metadata/designing-metadata-event-schema

# Designing metadata event schema

This document provides design guidelines for developers looking to emit typed [metadata events](/tools/deno-slack-sdk/guides/integrating-message-metadata-events) from their applications. These guidelines are intended to be _strong recommendations_ (rather than prescriptive). Following these patterns will serve developers in providing better readability, maintainability, and DRYness across their workflows and applications.

While in the future this guide may serve as a launching point for additional features, none of these guidelines are enforced programmatically and only provide guidance in how to best use structured data.

This document repeatedly uses the word **should** (and occasionally MUST), as to be interpreted as described in \[[RFC2119](https://tools.ietf.org/html/rfc2119)\].

## General Guidelines {#general}

Metadata Events are structured data payloads that contain information about events occurring in your Slack-connected application, in the form of a custom `event_payload` as part of a message's `metadata` property.

Developers can use different Slack API methods to transmit these events. One such method would be `chat.postMessage`, where `metadata` can be included as a JSON payload, and arrives in channel as part of a message (not visible to the user).

### Payload Structure {#payload_structure}

*   Metadata always includes an `event_type` and an `event_payload`. While order doesn't matter, developers should send `event_type` first for readability.
*   Event properties are always sent as part of an `event_payload`, and property order within the event payload is not important.
*   The value of `event_type` should be an alphanumeric string, and human readable. The value of this field may appear in the UI to developers, so keep this in mind when choosing a value. Developers should make an effort to name with the pattern `<resource_name_singular>` _and_ `<action_in_past_tense>`

```
{    "event_type": "job_created",    "event_payload": {        "job_id": 12345,        "date_created": 1623346792    }}
```

_A sample_ `metadata` _payload as part of_ `chat.postMessage`.

### Property Basics {#property_basics}

When writing your JSON representation of event metadata:

*   Always use double quotes
    *   Property names should be surrounded with double quotes.
    *   Property values, if string, should be surrounded with double quotes, otherwise, no quotes should be used.
*   Names should always begin with a character `[a-z]`, and may only contain characters, numbers `[0-9]` and underscores `[_]`
*   Property names should be an alphanumeric string and human readable. The value of this field may appear in the UI to developers, so keep this in mind when choosing a value.

```
    {      "event_type": "example_created",      'event_payload': { ❌ // Always use double quotes        "user": 'U1234567', ❌ // Always use double quotes        "date_created": "1623346792" ❌ // Number (epoch) should not have quotes        "date_deleted": 1623346793 ✅        "9tails": "gotta catch em all!", ❌ // Don't begin properties with a number        "bad idea": true, ❌ // no spaces in property names        "the_quick_brown_fox_jumped_over_the_lazy_dog": false, ❌ // too long        "name": "Bologne" ✅    }
```

### Casing and Compounding {#casting}

*   Property names should always be snake case (lowercase with underscores)

**✅ Recommended**

**❌ Not Recommended**

`user`

`User`

`user_id`

`userId`

`assigned_user_id`

`assignedUserId`

*   We should avoid using articles such as 'a', 'the', 'of' unless needed to convey meaning.
    *   e.g. names such as `a_user`, `the_team` should NOT be used, rather `user`, `team` should be preferred.
*   Multi-word properties should be separated by an underscore.

**✅ Recommended**

**❌ Not Recommended**

`poll_id`

`pollId`

`channel`

`the_channel`, `theChannel`, `Channel`

```
    "event_payload": {      "user": "U1234567", ✅      "date_created": 1623346792 ✅      "poll_id": 42 ✅    }
```

```
    "event_payload": {      "User": "U1234567", ❌      "DateCreate": 1623346792 ❌      "the_poll_id": 42 ❌
```

### Singular vs Plural Names {#singular_vs_plural}

*   Plural names should always represent a type `array`. All other property names should be singular. (Including counts).
*   Properties should not contain superfluous words to indicate units of the item exist (i.e. `user_objects` (just `users`), or `task_items` (just `tasks`)

**Context**

**✅ Recommended**

**❌ Not Recommended**

Property representing an array of User strings.

`users`

`user`

Property representing an array of tasks

`tasks`

`task_items`

Property representing an object with a number of properties.

`profile`

`profiles`

✅ Recommended

```
    "event_payload":{       "job":{          "id":1001 ✅       },       "tasks":[          {             "id":420, ✅             "name":"Task"          },          {             "id":421,             "name":"Task 2"          }       ],
```

❌ Not Recommended

```
    "event_payload": {      "jobs":{ ❌        "id": 1001,      },      "task_items":[{ ❌      "id": 420,      "name":"Task"      },      {           "id": 421,      "name":"Task 2"       }],
```

### Flattened data vs Structured Hierarchy {#flattened}

Data should only be grouped as it is sensible semantically. Developers should not arbitrarily group data for visual convenience. We currently don't support objects within objects (unless a custom type has already been defined), or arrays that contain objects or other arrays.

*   Properties should not use superfluous hierarchy to represent an ID unless there is a semantic use for the resulting object.

❌ Not Recommended

```
    "event_payload": {      "user":{ ✅        "id": 123        "date_created": 1623857773,        "names": { ❌ /* There is no reason to group these unless the object has a use */          "first_name": "John",          "middle_name": "Dino",          "last_name": "Hammond",        },      }    }
```

✅ Recommended

```
    "event_payload": {      "user":{ ✅        "id": 123,        "date_created": 1623857773,        "first_name": "John",        "middle_name": "Dino",        "last_name": "Hammond"      }    }
```

*   Flattened, an event containing metadata about a poll and some associated work called job might look like so:

```
    "event_payload": {        "job_id": 12345,        "date_created": 1623346792        "poll_name": "my_poll",        "poll_id": 42        "poll_vote_count": 19        "permalink_url": "https://example.com/my_poll/42"    }
```

*   Using a structured hierarchy, a potentially more useful format could look like:

```
    "event_payload": {        "job_id": 12345,        "poll": {          "date_created": 1623346792          "name": "my_poll",          "id": 42          "vote_count": 19          "permalink_url": "https://example.com/my_poll/42"        }    }
```

Using structured hierarchy where meaningful provides a number of benefits:

*   Reusability of objects across multiple applications and workflows
*   Clear intentionality of fields without overly verbose naming (i.e `date_created`).
*   Creating new object types

### Null Values {#null_values}

Fields that are **required** should always have a value. Wherever possible, avoid sending `null`. Optional fields that are not sent as part of an event should be assumed to be `null`.

Consider configuring your event consumption in such a way that the setting and unsetting of specific properties is controlled by their presence in the event payload.

For example, if we wanted to set the first and last name, our event would look like so:

✅ Recommended

```
    "event_payload": {      "first_name": "John",      "last_name": "Hammond"    }
```

If the user already existed, but had been previously set up with a middle name, and we wanted to unset the middle name, our event would look like so (the same):

✅ Recommended

```
    "event_payload": {      "first_name": "John",      "last_name": "Hammond"    }
```

Anti-patterns:

❌ Not Recommended

```
    "event_payload": {      "first_name": null, ❌ // never set required values to be null      "last_name": "Hammond"    }    "event_payload": {      "first_name": "John",      "middle_name": null, ❌ // not recommended way to unset optional value      "last_name": "Hammond"    }
```

### Type Selection {#type_selection}

While most basic values can be defined using primitives, consider using custom types and objects wherever it may improve clarity, extensibility, and reusability.

Examples:

*   Representing a non Slack User ID (perhaps one associated with your customers?), declare your own type definition called `mybusiness#/reference/objects/user-object_id` as opposed to using a `string` or `integer`.
*   Creating a custom `mybusiness#/reference/objects/user-object` object will let you add new properties to the type object later without changing the event schema
*   Slack has many predefined types for you (non exhaustive). You should always use them over defining them yourself:
    *   `slack#/reference/objects/channel-object`
    *   `slack#/reference/objects/channel-object_id`
    *   `slack#/reference/objects/user-object`
    *   `slack#/reference/objects/user-object_id`
    *   `slack#/types/team`
    *   `slack#/types/team_id`
    *   `slack#/types/timestamp`

## Property and Value Guidelines {#property_guidelines}

### DateTime {#datetime}

**Properties**

*   Date and time property keys should begin with date\_.
*   DateTime properties should always use past tense in the format `date_{past_tense_verb}` like `date_created`, `date_archived`. _The exception to this rule is when the value of the date going into the property is intended to generally be greater than the timestamp of the event._

**✅ Recommended**

**❌ Not Recommended**

`date_expired`

`date_expire`

`date_created`

`date_create`, `created_at`

*   If value that will go into the event is always greater than event timestamp at time of sending, than it should use future tense by dropping `date` and appending `at`

**✅ Recommended**

**❌ Not Recommended**

`expires_at`

`date_expires`

`send_at`

`date_send`

`ticket_due_at`

`date_ticket_due`, `ticket_due`

*   Properties describing the modification of a resource should include the resource noun in the name of the property when the property is not nested in an object that provides context. i.e. `date_{resource}_{past_tense_verb}`

**✅ Recommended**

**❌ Not Recommended**

`date_user_created`

`user_creation_date`

`date_task_deleted`

`task_date_deleted`

✅ Recommended

```
    "event_payload": {      "date_project_created":1515472552, ✅      "task":{        "id": 1002,        "date_created":1525472552, ✅        "due_at": 1725472552 ✅      },
```

❌ Not Recommended

```
    "event_payload": {      "date_project_created":1515472552, ✅      "task":{        "id": 1002,        "date_task_created": 1525472552, ❌      },
```

**Values**

*   Date & time objects should be returned as integer unix epoch timestamp
*   Unix epoch timestamp values should be have second precision, not millisecond

**✅ Recommended**

**❌ Not Recommended**

`1525472552`

`Fri, 04 May 2018 22:22:31 GMT`

`1514764800`

`2018-01-01T00:00:00Z`

```
    types:      date_created:        description: Date object was created        title: Date Created        type: slack#/types/timestamps        example: 1525472552
```

### DateTime Relative {#relative_datetime}

**Properties**

*   Properties denoting relationships in time should use following verbs:
    *   `since`, `until` - inclusive
    *   `before`, `after` - exclusive

✅ Recommended

❌ Not Recommended

`since_completed`

`since_complete`

`until_completed`

`until_complete`

`before_expired`

`time_to_expire`

`after_expired`

`time_after_expired`

**Values**

*   Relationships should be expressed in seconds as an integer

```
    since_deleted:      description: How long its been since the issue was deleted      title: Time Since Deleted      type: integer      example: 3600
```

### DateTime Interval {#interval_datetime}

**Properties**

*   When denoting intervals in time (such as calendar events), those periods should be described using two properties: `date_<noun>_start` \*\*and `date_<noun>_end`.
*   Avoid the anti pattern of a combination of properties like `date_start` and then `since_started` to describe objects which have a start and an end (interval).

**Values**

*   Interval start and stop should be returned as integer unix epoch timestamp
*   Unix epoch timestamp values should be have second precision, not millisecond

### Counts {#counts}

**Properties**

*   Counts should be named as `<singular_resource>_count`
*   Counts represent a number, not a collection

**✅** Recommended

**❌ Not Recommended**

`response_count`

`num_responses`

`ticket_count`

`num_tickets`

`authed_member_count`

`members_authed`

`item_count`

`total_items`

`user_count`

`users`

✅ Recommended

```
    "event_payload": {                 "user_count": 10,
```

```
❌ Not Recommended    "event_payload": {                 "users": 10,
```

**Values**

*   Counts should always be represented by an integer.

```
    issue_count:      description: How many issues are there      title: Issue Count      type: integer      example: 12
```

### Booleans {#booleans}

**Properties**

*   Booleans should be prefixed with `is_` or `has_`

**✅** Recommended

**❌ Not Recommended**

`is_expired`

`expired`

`is_due`

`due`

`has_attachments`

`attachments`

**Values**

*   Boolean values may only be `true` or `false`.

### Enums {#enums}

**Properties**

*   Enums should always be non plural

**Context**

**✅ Recommended**

**❌ Not Recommended**

Property representing an incident level

`severity`

`severities`

**Values**

*   Enum values should always be strings in uppercase

```
    severity:      description: Severity of the incoming incident      title: Incident Severity      type: enum:["SEV1", "SEV2", "SEV3"],      example: "SEV2"
```

```
    "metadata":{      "event_type": "new_incident",      "event_payload": {                   "severity": "SEV2"
```

### Identities {#identities}

*   Properties that contain an ID should denote it with the suffix `_id`

```
    "event_payload": {      "user_id": "U1234M112", ✅    }
```

```
    "event_payload": {      "user": "U1234M112" ❌    }
```

### Slack Types {#slack_types}

**Properties**

*   Properties representing Slack objects (channel, user, team, etc) should be defined with Slack provided types `slack#/types`

✅ Recommended

```
    types:      assignee_user_id:        description: Slack user ID of assignee user        title: Assignee user's ID        type: slack#/reference/objects/user-object_id ✅        example: U01234XM1
```

❌ Not Recommended

```
    types:      assignee_user_id:        description: Slack user ID of assignee user        title: Assignee user's ID        type: string ❌ // Use the slack user_id type        example: U01234XM1
```

### Slack Message Timestamps {#slack_message_timestamps}

**Properties**

*   Developers should call a property that represents a Slack message timestamp `message_timestamp`

**✅ Recommended**

**❌ Not Recommended**

`message_time stamp`

`timestamp`, `ts`

**Values**

*   Slack message timestamps MUST be sent as a string

**✅ Recommended**

**❌ Not Recommended**

`"1525471335.000320"`

`1525471335000320`

`"1525471335.000320"`

`1525471335`

✅ Recommended

```
    "metadata":{      "event_type": "slack_message_processed",      "event_payload": {                   "date_received": 1525472552, ✅                   "message_timestamp": "1525471335.000320" ✅
```

```
❌ Not Recommended    "metadata":{      "event_type": "slack_message_processed",      "event_payload": {                   "date_received": "2018-01-01T00:00:00Z", ❌                   "message_timestamp": 1525471335 ❌
```

### Latitude/Longitude {#latitude_longitude}

*   Latitude/Longitude should be strings formatted as recommended by [ISO 6709](https://en.wikipedia.org/wiki/ISO_6709).
*   They should favor the `±DD.DDDD±DDD.DDDD` degrees format.

```
{    "slack_hq": "+40.6894-074.0447"}
```

## Patterns {#patterns}

Here are some example patterns of types and events as they would be described by an app manifest file, and the resulting output of your events:

#### On-call Escalation {#oncall_escalation}

This is what an example message schema might look like if you were describing an event sent by a product like PagerDuty or similar.

**Types - Manifest Schema**

```
    types:      incident_severity:        type: string        enum: ["S1", "S2", "S3", "S4"]        choices:          S1:            title: Severity 1          S2:            title: Severity 2          S3:            title: Severity 3          S4:            title: Severity 4      incident:          title: Incident          description: Represents an incident that was opened and hopefully resolved          type: object          required:            - id            - title            - summary            - severity            - reported_by            - created_at          properties:            id:              type: integer              title: Incident ID            title:              type: string            summary:              type: string            severity:              type: "#/types/incident_severity"            reported_by:              type: slack#/reference/objects/user-object_id            assigned_to:              type: slack#/reference/objects/user-object_id              description: Who was on call and assigned to the incident              nullable: true            date_created:              type: slack#/types/timestamp            date_closed:              type: slack#/types/timestamp              nullable: true
```

**Event - Manifest Schema**

```
    events:      incident_created:        title: Incident Created        description: Event triggered when a new incident is created        type: object        required:          - incident        properties:          incident:            type: "#/types/incident"
```

**Metadata - Message Object**

```
"metadata": {    "event_type": "incident_created",    "event_payload": {        "incident": {            "id": 9001,            "title": "A new incident was created!",            "summary": "Something really bad!",            "severity": "S1",            "reported_by": "U12345678",            "date_created": 1623792755        }    }
```