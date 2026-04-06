Source: https://docs.slack.dev/reference/scim-api/rate-limits

# SCIM API rate limits

Slack uses rate limits for the SCIM API to help provide a predictable experience.

Although the exact limits for each endpoint, [listed below](#orgwide), are different from other Slack API methods, rate limiting for SCIM [still uses the same principles as our other APIs](/apis/web-api/rate-limits). That being said, unlike many of the other Slack API rate limits, the limits below apply to all SCIM apps in an org, not on a per-app basis.

Small bursts above the limit are acceptable. If you receive an HTTP `429` response from Slack, you've come up against the rate limit - parse the `Retry-After` header and retry your request after that time.

### Organization-wide rate limits {#orgwide}

In your organization, Slack applies per-minute rate limits across all SCIM endpoints in certain sets. Each call to any of the endpoints in that set counts toward the **same** rate limit.

Endpoint set

Limit (requests per minute)

Bursts (requests)

Writes: `POST, PUT, PATCH, DELETE`

600

180

Reads: `GET`

1000

1000

**In addition** to the above org-wide limits across sets of endpoints, Slack _also_ applies rate limits on **individual endpoints**.

### Rate limits for Users endpoints {#userlimits}

Endpoint

Limit (requests per minute)

Bursts (requests)

[Get a user](#get-users): `GET /scim/VERSION/Users/<id>`

300

300

[Create a user](#post-users): `POST /scim/VERSION/Users`

180

20

[Update a user](#patch-users-id): `PUT` or `PATCH /scim/VERSION/Users/<id>`

180

20

[Delete a user](#delete-users-id): `DELETE /scim/VERSION/Users/<id>`

180

20

### Rate limits for Groups endpoints {#grouplimits}

Endpoint

Limit (requests per minute)

Bursts (requests)

[Get a group](#get-groups): `GET /scim/VERSION/Groups/<id>`

300

300

[Create a group](#post-groups): `POST /scim/VERSION/Groups`

180

20

[Update a group](#patch-groups-id): `PUT` or `PATCH /scim/VERSION/Groups/<id>`

180

80

[Delete a group](#delete-groups-id): `DELETE /scim/VERSION/Groups/<id>`

180

20