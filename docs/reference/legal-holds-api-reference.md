Source: https://docs.slack.dev/reference/legal-holds-api-reference

# Slack Legal Holds API reference

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

If you're sending a POST request to the Legal Holds API, you need to send the input below as `application/x-www-form-urlencoded` data.

## OAuth Scopes {#scopes}

For the best customer experience, please instruct the Org Owner to log into their Slack organization within their browser before initiating the OAuth flow. If not, the expected behavior is that the user will be logged into their organization without the redirect.

Scope

Related Methods

`admin.legal_holds:read`

`admin.legalHolds.policies.info`, `admin.legalHolds.policies.list`, `admin.legalHolds.entities.list`

`admin.legal_holds:write`

`admin.legalHolds.policies.activate`, `admin.legalHolds.policies.create`, `admin.legalHolds.policies.release`, `admin.legalHolds.policies.set`, `admin.legalHolds.entities.add`, `admin.legalHolds.entities.remove`

* * *

## Methods {#methods}

### Policies {#policy_management}

When creating a new Legal Hold policy, the API method caller can specify one or more restrictions to apply to the policy. These restrictions modify the data which is held to include or exclude customer created content.

Restriction

Description

`NO_RESTRICTION`

The policy does not define any restrictions and data will be held for all relevant conversations.

`ONLY_DMS`

The policy will only apply to conversations occurring in direct message channels only. All other conversations will not be considered by this policy.

Use these methods to define and manage Legal Hold policies.

*   [`admin.legalHold.policies.activate`](#policies_activate)
*   [`admin.legalHold.policies.create`](#policies_create)
*   [`admin.legalHold.policies.info`](#policies_info)
*   [`admin.legalHold.policies.list`](#policies#list)
*   [`admin.legalHold.policies.release`](#policies_release)
*   [`admin.legalHold.policies.set`](#policies_set)

### Custodians {#entity_management}

In order for a Legal Hold policy to retain customer data, a policy must define one or more entities. Entities attach to policies and specify which types of content are to be held.

Entity Type

Entity ID

Description

`USER`

Encoded user ID

Hold message data authored by or visible to the specified user. This includes message data sent in conversations the user was previously a member of.

Use these methods to add or remove custodians to or from a Legal Hold policy.

*   [`admin.legalHold.entities.add`](#entities_add)
*   [`admin.legalHold.entities.list`](#entities#list)
*   [`admin.legalHold.entities.remove`](#entities_remove)

* * *

### admin.legalHold.policies.activate {#policies_activate}

This method activates a previously [released](#policies_release) policy. Activating a policy will hold data visible to custodians specified by the policy.

**Method URL**: `https://slack.com/api/admin.legalHold.policies.activate`  
**Required scope:** `admin.legalHolds:write`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to activate.

### Example Request {#example-request}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01RR4604RZ"}
```

### Example Response {#example-response}

```
{  "ok": true,  "policy": {    "id": "H01RR4604RZ",    "team_id": "E81A4BN3H",    "creator_id": "WKUNKUXSL",    "name": "First Policy",    "description": "...",    "restrictions": [      "NO_RESTRICTION"    ],    "status": "ACTIVE",    "date_created": 1616084896,    "date_updated": 1616084896,    "date_released": 0,    "date_policy_start": 0,    "date_policy_end": 0  }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.policies.create {#policies_create}

This method creates a new Legal Hold policy. By default all policies are created as `ACTIVE` (enforced) policies.

**Method URL**: `https://slack.com/api/admin.legalHold.policies.create`  
**Required scope:** `admin.legalHolds:write`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`name`

Policy name

Required

A textual name for the policy. This must be a unique name.

`description`

Content under review for case xxxx

Optional

A long form textual description of the policy.

`policy_start_date`

`1606809600`

Optional

Unix timestamp of when a policy should start. Omit to hold all historical data. This value cannot be changed once a policy is created.

`policy_end_date`

`1609401600`

Optional

Unix timestamp of when a policy should end. Omit to hold data until policy release. This value cannot be changed once a policy is created.

`restrictions`

`["ONLY_DMS"]`

Optional

You can either pass `ONLY_DMS` or omit this argument to set no restrictions on the policy. See example request below for the no restrictions use case. More details in the [Restrictions](/reference/legal-holds-api-reference#policy_management) section reference.

### Example Request {#example-request-1}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "name": "Second Policy",  "description": "A policy covering custodians in group A"}
```

### Example Response {#example-response-1}

```
{  "ok": true,  "policy": {    "id": "H01S3583Z4M",    "team_id": "E81A4BN3H",    "creator_id": "WKUNKUXSL",    "name": "Second Policy",    "description": "A policy covering a custodians in group A",    "restrictions": [        "NO_RESTRICTION"    ],    "status": "ACTIVE",    "date_created": 1616516022,    "date_updated": 1616516022,    "date_released": 0,    "date_policy_start": 0,    "date_policy_end": 0  }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.policies.info {#policies_info}

This method returns the complete details for an existing Legal Hold policy.

**Method URL**: `https://slack.com/api/admin.legalHold.policies.info`  
**Required scope:** `admin.legalHolds:read`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to activate.

### Example Request {#example-request-2}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01RR4604RZ"}
```

### Example Response {#example-response-2}

```
{  "ok": true,  "policy": {    "id": "H01RR4604RZ",    "team_id": "E81A4BN3H",    "creator_id": "WKUNKUXSL",    "name": "First Policy",    "description": "",    "restrictions": [        "NO_RESTRICTION"    ],    "status": "ACTIVE",    "date_created": 1616084896,    "date_updated": 1616084896,    "date_released": 0,    "date_policy_start": 0,    "date_policy_end": 0  }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.policies.list {#policies_list}

This method returns a paginated list of Legal Hold policies.

This method accepts a `cursor` parameter for pagination. When paginating, these values will be returned as `next_cursor` value located within the `response_metadata` object of the response.

**Method URL**: `https://slack.com/api/admin.legalHold.policies.list`  
**Required scope:** `admin.legalHolds:read`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`cursor`

`Hxxxxxxxxx`

Optional

Specify to obtain the next page of results from a previous response `next_cursor` value.

`limit`

`10`

Optional

Number of policies to return per page. (Max: `1000`, Default: `1000`)

`status`

`RELEASED`

Optional

Limit responses to only include policies of a given status. (E.g.: `ACTIVE` or `RELEASED`)

### Example Request {#example-request-3}

```
{  "token": "xxxx-xxxxxxxxx-xxxx"}
```

### Example Response {#example-response-3}

```
{  "ok": true,  "policies": [    {      "id": "H01S3583Z4M",      "team_id": "E81A4BN3H",      "creator_id": "WKUNKUXSL",      "name": "Second Policy",      "description": "A policy covering a custodians in group A",      "restrictions": [        "NO_RESTRICTION"      ],      "status": "ACTIVE",      "date_created": 1616516022,      "date_updated": 1616516022,      "date_released": 0,      "date_policy_start": 0,      "date_policy_end": 0    },    {      "id": "H01RR4604RZ",      "team_id": "E81A4BN3H",      "creator_id": "WKUNKUXSL",      "name": "First Policy",      "description": "",      "restrictions": [        "NO_RESTRICTION"      ],      "status": "ACTIVE",      "date_created": 1616084896,      "date_updated": 1616517381,      "date_released": 0,      "date_policy_start": 0,      "date_policy_end": 0    }  ],  "policy_total_count": 2,  "response_metadata": {    "next_cursor": ""  }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.policies.release {#policies_release}

This method releases an [active](#policies_activate) Legal Hold policy. Released policies will no longer hold data for any custodians that fall under those policies.

**Method URL**: `https://slack.com/api/admin.legalHold.policies.release`  
**Required scope:** `admin.legalHolds:write`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to release.

### Example Request {#example-request-4}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01RR4604RZ"}
```

### Example Response {#example-response-4}

```
{  "ok": true,  "policy": {    "id": "H01RR4604RZ",    "team_id": "E81A4BN3H",    "creator_id": "WKUNKUXSL",    "name": "First Policy",    "description": "",    "restrictions": [      "NO_RESTRICTION"    ],    "status": "RELEASED",    "date_created": 1616084896,    "date_updated": 1616518337,    "date_released": 1616518337,    "date_policy_start": 0,    "date_policy_end": 0  }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.policies.set {#policies_set}

This method can be used to update the details of an existing Legal Hold policy. Changes can only be made to active policies.

**Method URL**: `https://slack.com/api/admin.legalHold.policies.set`  
**Required scope:** `admin.legalHolds:write`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to modify.

`name`

Policy name

Optional

A textual name for the policy. This must be a unique name.

`description`

Content under review for case xxxx

Optional

A long form textual description of the policy.

### Example Request {#example-request-5}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01S3583Z4M",  "description": "This policy applies to custodians in group A and B"}
```

### Example Response {#example-response-5}

```
{    "ok": true,    "policy": {        "id": "H01S3583Z4M",        "team_id": "E81A4BN3H",        "creator_id": "WKUNKUXSL",        "name": "Second Policy",        "description": "This policy applies to custodians in group A and B",        "restrictions": [            "NO_RESTRICTION"        ],        "status": "ACTIVE",        "date_created": 1616516022,        "date_updated": 1616519107,        "date_released": 0,        "date_policy_start": 0,        "date_policy_end": 0    }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.entities.add {#entities_add}

This method associates one or more custodians (or entities) to an active Legal Hold policy.

**Method URL**: `https://slack.com/api/admin.legalHold.entities.add`  
**Required scope:** `admin.legalHolds:write`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to modify.

`entities`

`[{"entity_type": "USER","entity_id":"W8V90M2U9"}]`

Required

List if entity objects to add. Please see the [Entity Types](/reference/legal-holds-api-reference#entity_management) reference page for a complete list of supported entities. Only `100` entities can be added at a time. There is a max limit of `1000` active entities per Legal Hold policy.

### Example Request {#example-request-6}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01RR4604RZ",  "entities": [    {      "entity_type": "USER",      "entity_id": "W8V90M2U9"    }  ]}
```

### Example Response {#example-response-6}

```
{  "ok": true,  "created_entities": [    {      "id": "He01RA72HZL7",      "team_id": "E81A4BN3H",      "policy_id": "H01RR4604RZ",      "entity_type": "USER",      "entity_id": "W8V90M2U9",      "date_created": 1616085744,      "date_deleted": 0    }  ],  "failed_entities": []}
```

[Return to method list](#methods)

* * *

### admin.legalHold.entities.list {#entities_list}

This method returns a paginated list of custodians (or entities) assigned to a Legal Hold policy.

This method accepts a `cursor` parameter for pagination. When paginating, these values will be returned as `next_cursor` value located within the `response_metadata` object of the response.

**Method URL**: `https://slack.com/api/admin.legalHold.entities.list`  
**Required scope:** `admin.legalHolds:read`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to fetch custodians (or entities) for.

`cursor`

`Hexxxxxxxxx`

Optional

Specify to obtain the next page of results from a previous response `next_cursor` value.

`limit`

`10`

Optional

Number of custodians (or entities) to return per page. (Max: `1000`, Default: `1000`)

`include_deleted`

`true`

Optional

Specify to include/exclude deleted custodians from the response. (Default: `false`)

### Example Request {#example-request-7}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01RR4604RZ"}
```

### Example Response {#example-response-7}

```
{  "ok": true,  "entities": [    {      "id": "He01RA72HZL7",      "team_id": "E81A4BN3H",      "policy_id": "H01RR4604RZ",      "entity_type": "USER",      "entity_id": "W8V90M2U9",      "date_created": 1616085744,      "date_deleted": 0    }  ],  "response_metadata": {    "next_cursor": ""  }}
```

[Return to method list](#methods)

* * *

### admin.legalHold.entities.remove {#entities_remove}

This method removes one or more custodians (or entities) from an active Legal Hold policy.

**Method URL**: `https://slack.com/api/admin.legalHold.entities.remove`  
**Required scope:** `admin.legalHolds:write`  
**HTTP Method:** `POST`

Argument

Example

Required

Description

`token`

`xxxx-xxxxxxxxx-xxxx`

Required

Authentication token bearing required scopes.

`policy_id`

`Hxxxxxxxxx`

Required

Policy ID to modify.

`ids`

`["Hexxxxxxxxx","Hexxxxxxxxx"]`

Required

List of entity IDs to remove from the policy. IDs can be found using the entities [list](#entities#list) method. Only `100` entities can be removed at a time.

### Example Request {#example-request-8}

```
{  "token": "xxxx-xxxxxxxxx-xxxx",  "policy_id": "H01RR4604RZ",  "ids": ["He01RA72HZL7"]}
```

### Example Response {#example-response-8}

```
{    "ok": true,    "failed_ids": []}
```

[Return to method list](#methods)

* * *

## Errors {#errors}

The following errors may be returned from the API.

Error

Description

`invalid_cursor`

The pagination cursor provided is invalid. Please use the `next_cursor` value from a previous request response only.

`legal_hold_not_found`

The requested policy does not exist. Check that the policy ID provided is valid.

`released_policy_edit_not_allowed`

Polices which are released cannot be edited.

`too_many_entities`

The request cannot be completed because it includes too many entities. Retry the request with a smaller number of entities.

`max_active_entities_reached`

A legal hold policy can have up to 1000 entities. Try reducing the number of entities being added.

`unknown_method`

The requested method cannot be found. You will see this error if the Legal Holds API is enabled, but your token does not have `admin.legalHolds:*` scopes.