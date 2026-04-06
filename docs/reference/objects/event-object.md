Source: https://docs.slack.dev/reference/objects/event-object

# Event object

We package all [event types](/reference/events) delivered over the [Events API](/apis/events-api/) in a common JSON-formatted event wrapper.

## Example {#example}

```
{    "token": "XXYYZZ",    "team_id": "T123ABC456",    "api_app_id": "AXXXXXXXXX",    "event": {        "type": "name_of_event",        "event_ts": "1234567890.123456",        "user": "U123ABC456"    },    "type": "event_callback",    "authorizations": [        {            "team_id": "T123ABC456",            "user_id": "U123ABC456",            "is_bot": false,            "is_enterprise_install": false,        }    ],    "event_id": "Ev08MFMKH6",    "event_time": 1234567890}
```