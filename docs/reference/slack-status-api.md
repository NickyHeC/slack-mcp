Source: https://docs.slack.dev/reference/slack-status-api

# Slack Status API

Slack offers two API endpoints to describe its status. Use the `https://slack-status.com/api/v2.0.0/current` endpoint to check for active incidents. Use the `https://slack-status.com/api/v2.0.0/history` endpoint to learn about past incidents. Both are unauthenticated: you can even open these API endpoints directly in your browser. [Try it](https://slack-status.com/api/v2.0.0/current).

You can also find either endpoint with a cURL command:

```
curl https://slack-status.com/api/v2.0.0/currentcurl https://slack-status.com/api/v2.0.0/history
```

## Version 2.0.0 {#v2_0_0}

### Current Status API {#current-status-api}

The `current` endpoint returns a JSON object containing a `status` field. When all is well, the `status` will be "ok", and the response will be brief. Here's a sample "ok" response.

```
{"status":"ok","active_incidents": [],"date_created":"2018-09-07T18:34:15-07:00","date_updated":"2018-09-07T18:34:15-07:00"}
```

If there's an incident, outage, or planned maintenance, you'll receive a richer JSON response containing a title that describes the issue, a time updated, and affected services. Here's a sample JSON response describing an issue with email forwarding:

```
{  "status": "active",  "date_created": "2019-04-09T07:35:46-07:00",  "date_updated": "2019-04-09T07:35:46-07:00",  "active_incidents": [    {      "id": "546",      "date_created": "2018-09-07T14:35:00-07:00",      "date_updated": "2018-09-07T18:34:15-07:00",      "title": "Slack’s forwarding email feature is failing for some customers",      "type": "incident",      "status": "active",      "url": "https://slack-status.com/2018-09/7dea1cd14cd0f657",      "services": [        "Apps/Integrations/APIs"      ],      "notes": [        {          "date_created": "2018-09-07T18:34:15-07:00",          "body": "Technical Summary:\r\nOn September 7th at 2:35pm PT, we received reports that emails were failing to deliver to Slack forwarding addresses. We identified that this was the result of an expired certificate used to verify requests sent from our email provider. At 4:55pm PT, we deployed an update that corrected this and fixed the problem. Unfortunately any email sent to a forwarding address during this time is not retrievable and will need to be re-sent."        }      ],    },    ...  ]}
```

Here's more detail on each of the fields in the response:

Field

Description

`id`

A unique ID for the issue.

`date_created`

The timestamp when incident response or maintenance began.

`date_updated`

The timestamp when incident response or maintenance was most recently updated.

`title`

A short description of what's happening.

`type`

The type of issue we're experiencing. The options are "incident", "notice", or "outage".

`status`

We use status "ok" when all is well. Otherwise, the `status` field is "active" when the issue has not yet been resolved, and "resolved" when the issue has been resolved. The status may also be "scheduled," "completed," or "cancelled" in the case of planned maintenance.

`url`

A web URL tracking this incident. The information displayed is the same as in the API endpoint.

`services`

An array that lists the Slack services affected:  
\- "Login/SSO"  
\- "Messaging"  
\- "Notifications"  
\- "Search"  
\- "Workspace/Org Administration"  
\- "Canvases"  
\- "Connectivity"  
\- "Files"  
\- "Huddles"  
\- "Apps/Integrations/APIs"  
\- "Workflows"

`notes`

An array of notes with additional specifics and updates.

In version 2.0.0, the current API endpoint displays all active incidents. If you don't pass a version, the API endpoint defaults to version 1.0.0, which only displays one incident at a time. If there are multiple incidents, it displays the most urgent one according to Slack internal incident ranking. If there are no active incidents, it'll display the most recent incident that was updated within the last hour. If no incidents have been reported or updated in the last hour, the endpoint returns the terse "ok" response.

### History API {#history-api}

The `history` endpoint returns a list of all past Slack issues. Each object in the response array is an incident like the ones returned by the `current` endpoint. As with the `current` endpoint, you can expect the following fields for each issue:

Field

Description

`id`

A unique ID for the issue.

`date_created`

The timestamp when incident response or maintenance began.

`date_updated`

The timestamp when incident response or maintenance was most recently updated.

`title`

A short description of the issue.

`type`

The type of issue we experienced. The options are "incident", "notice", or "outage".

`status`

We use status "ok" when all is well. Otherwise, the `status` field is "active" when the issue has not yet been resolved, and "resolved" when the issue has been resolved. The status may also be "scheduled," "completed," or "cancelled" in the case of planned maintenance.

`url`

A web URL for this incident. The information displayed is the same as in the API endpoint.

`services`

An array that lists the Slack services affected. Current and past service names can include the following:  
\- "Login/SSO"  
\- "Messaging"  
\- "Notifications"  
\- "Search"  
\- "Workspace/Org Administration"  
\- "Connections"  
\- "Files"  
\- "Huddles"  
\- "Apps/Integrations/APIs"  
\- "Workflows"  
\- "Posts/Files"  
\- "Calls"  
\- "Link Previews"

`notes`

An array of notes with additional specifics and updates.

## Version 1.0.0 {#v1_0_0}

Version 1.0.0 of the Slack Status API endpoints can be found at both `https://slack-status.com/api/v1.0.0/current` and `https://slack-status.com/api/current`. The information returned is similar to version 2.0.0, except that the `current` endpoint shows only one incident at a time. If there are multiple incidents, the endpoint displays the most urgent one according to Slack internal incident ranking. If there are no active incidents, it'll display the most recent incident that was updated within the last hour. If no incidents have been reported or updated in the last hour, the endpoint returns the terse "ok" response.

## Best practices {#best-practices}

*   Use the most recent version of the API endpoint (`v2.0.0`).
*   Call the `current` endpoint as frequently or infrequently as you need to in order to respond to issues with Slack; if you need to be notified immediately of an incident, consider polling the `current` endpoint once a minute. Polling more frequently than that isn't recommended.
*   If you rely on a specific feature of Slack heavily, check the `services` field of an incident to verify that the feature is working as usual. For example, if your app doesn't use Huddles, but does rely on messaging, consider filtering for incidents that contain "Messaging" in the `services` array, and ignoring alerts that only affect "Huddles".