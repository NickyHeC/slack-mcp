Source: https://docs.slack.dev/reference/audit-logs-api/anomalous-events-reference

# Anomalous events

Anomaly events are a special part of the Audit Logs API that help surface unexpected app and user behaviors. Use logged anomalous events to guide decisions such as:

*   determining whether a behavior is expected
*   automating a response from a Security Information and Event Management (SIEM) tool or a Security Orchestration, Automation, and Response (SOAR) tool
*   reaching out to the user for more information

The `Entities` column in the table below reflects which anomalies are applicable for users vs apps. We don't monitor apps for some behaviors that we monitor users for, as they tend to have different usage patterns. What might be anomalous for users may be reasonable for apps.

There will be a `reason` code published for any anomalous event. Learn how to configure audit log anomaly event responses [here](https://slack.com/help/articles/37193054707603-Configure-audit-log-anomaly-event-responses-in-Slack).

Anomalous event

What it means

Entities

`asn`

An ASN was on a list of suspicious ASNs. This will always be accompanied by an `ip_address` reason.

app, user

`excessive_downloads`

The file download detection generates alerts when it detects anomalous behavior, such as when a user downloads an excessive number of files.

app, user

`excessive_file_shares`

The file share detection generates alerts when it detects anomalous behavior, such as when a user shares an excessive number of files.

app, user

`excessive_malware_uploads`

The malware uploads detection generates alerts when it detects anomalous behavior, such as when a user shares an excessive number of malware files.

app, user

`ip_address`

An anomaly was detected in the IP address used for the user token. Based on the IP enhancements we used and the history of IP usage of the user token, we identified something anomalous in `ip_address`. You can check `ip_address` and `previous_ip_address` to look at the change, as well as the `ip_address_details` field within `details` for more information. This field may contain the following values:  

*   `new-asn`: The IP address is from an ASN not recently seen with this token.
*   `cloud-asn`: The IP address is from a cloud ASN which may be unexpected for a user.
*   `in-ioc-list`: The IP address is on an IOC (indicators of compromise) watchlist. These lists flag potentially malicious indicators based on previously identified threats.

If no `ip_address_details` are provided, check if the reason also includes `asn` indicating that the anomaly triggered due to being from a suspicious ASN.

app, user

`potential_spam`

A user is making a high volume of calls to an API that can cause disruption on a workspace. The `api_call_method` field within `details` indicates what API is being called. Possible values are:  

*   `functions.workflows.publish`

user

`search_volume`

The search volume detection generates alerts when it detects anomalous behavior such as a user issuing searches under suspicious circumstances. _This anomaly is currently being re-tooled and is deprecated as of 5-02-2025_.

user

`session_fingerprint`

The session cookie has an unexpected or stale timestamp associated with it, or a client fingerprint differs from an expected one.

user

`spoofed_user_agent`

Characteristics of the client do not match the user agent indicating that the user agent may be spoofed. This will always be accompanied by a `unexpected_client` reason.

user

`tor`

A Tor exit node was used.

app, user

`unexpected_admin_action`

The unexpected admin action detection generates alerts when anomalous behavior occurs from an administrator account.

user

`unexpected_api_call_volume`

The unexpected API call volume detection generates anomalies when a user generates a larger volume of API calls than would be expected from a browser or official Slack client accessing Slack. This could indicate that a user is using a non-standard client or performing scraping activities.

user

`unexpected_client`

The unexpected client detection generates alerts when an anomalous Slack client is detected. See the `detected_client` and `detected_os` fields within details for additional context. Note: the `detected_os` field is not always populated.

user

`unexpected_credential_testing`

The unexpected credential testing detection generates anomalies when it detects a credential being tested for validity under suspicious circumstances.

app

`unexpected_message_deletion`

The unexpected message deletion detection generates alerts when it detects anomalous behaviors, such as when a user deletes an excessive number of messages.

user

`unexpected_scraping`

The unexpected scraping detection generates anomalies when it detects a tool that can be used for scraping. Scraping tools can be used to rapidly retrieve and save data that a user has access to on a workspace.

user

`unexpected_user_agent`

The user agent changed to a value that is not expected from a user. This will always be accompanied by a `user_agent` reason.

user

`user_agent`

An anomaly was detected in the user agent used for the user token (ex: there was a downgrade in a version). The best way to investigate such an event is to look at `ua` and `previous_ua` in the audit logs, as these will illustrate the change in `user_agent`. The `user_agent_change_details` field within `details` will provide more context on the change.

user

The format of the `anomaly` detection logs is similar to the rest of the audit logs, but with the addition of a `details` object adding the reasoning for the behavior being detected as an anomaly. Note: The `previous_ua` field will be blank if the entity has not connected to Slack with a different user agent since establishing a session. Similarly, the `previous_ip_address` field will be blank if the entity has not connected from a different ip address since establishing a session.

For example, here's an `anomaly` audit log caused by an `ip_address` anomaly.

```
{    "id": "<id>",    "date_create": 1644428305,    "action": "anomaly",    "actor": {        "type": "user",        "user": {            "id": "U123ABC456",            "name": "Alice Smith",            "email": "alice.smith@example.com",            "team": "T123ABC456"        }    },    "entity": {        "type": "user",        "user": {            "id": "U123ABC456",            "name": "Alice Smith",            "email": "alice.smith@example.com",            "team": "T123ABC456"        }    },    "context": {        "location": {            "type": "workspace",            "id": "E123ABC456",            "name": "Elysium",            "domain": "elysium"        },        "ua": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/64.0.3282.186 Safari\/537.36",        "session_id": "847288190092",        "ip_address":"1.23.45.678"    },    "details": {        "action_timestamp": 1644428253989994,        "location": "Reno, Nevada",        "previous_ip_address": "9.87.65.432",        "previous_ua": "Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0",        "reason": [            "ip_address"        ],        "ip_address_details": [            "cloud-asn"        ]    }}
```

## Exclude a list of trusted ASNs and/or IP ranges from detection {#exclude}

Slack provides an API for admins to manage allow-lists of trusted ASNs and IP ranges (using CIDR notation) on their Enterprise organization Slack instance. Traffic from allow-listed ASNs and IP ranges are not marked as anomalous in admin audit logs.

There are two endpoints you can use to manage your allow-lists of ASNs and IP ranges:

*   [`admin.audit.anomaly.allow.updateItem`](#update_item)
*   [`admin.audit.anomaly.allow.getItem`](#get_item)

### admin.audit.anomaly.allow.updateItem {#update_item}

> allows Enterprise organization admins to add trusted ASNs and IP ranges to their Enterprise organization instance

Writing to this endpoint will overwrite previously added ASNs and IP ranges.

When adding new ASNs and IP ranges, they must include all of the previously added IP ranges and ASNs in the new API call.

Parameter

Required

Type

Description

`token`

Required

String

The Enterprise org admin's token

`trusted_asn`

Array

All trusted ASNs

`trusted_cidr`

Array

All trusted IP ranges, in CIDR notation

**Example request payload**

```
{    "token":"xoxb-...",    "trusted_cidr":["8.8.8.8/24","8.8.4.4/22"],    "trusted_asn":[34245,8530]}
```

**Typical Response**

```
{"ok":true}
```

### admin.audit.anomaly.allow.getItem {#get_item}

> allows Enterprise organization admins to view the trusted ASNs and IP ranges on their Enterprise organization instance

Parameter

Required

Type

Description

`token`

Required

String

The Enterprise org admin's token

**Example request payload**

```
{   "token":"xoxb-..."}
```

**Typical response**

```
Response:{   "ok":true,   "trusted_cidr":["8.8.8.8/24","8.8.4.4/22"],   "trusted_asn":[34245,8530]}
```