Source: https://docs.slack.dev/reference/methods/admin.apps.activities.list

# admin.apps.activities.list method

DocsCall generator

## Facts {#facts}

**Description**Get logs for a specified team/org

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/admin.apps.activities.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.admin.apps.activities.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.admin_apps_activities_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().adminAppsActivitiesList
```

**Scopes**

User token:

[`admin.app_activities:read`](/reference/scopes/admin.app_activities.read)

**Content types**

`application/x-www-form-urlencoded`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

### Optional arguments

**`app_id`**Optional

The ID of the app to get activities from.

_Example:_ `A12345`

**`team_id`**`string`Optional

The team who owns this log.

_Example:_ `T12345`

**`cursor`**`string`Optional

Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. See [pagination](/apis/web-api/pagination) for more detail.

_Example:_ `bG9nX2lkOjc5NjQ1NA==`

**`limit`**`integer`Optional

The maximum number of items to return.

_Example:_ `100`

**`min_log_level`**`string`Optional

The minimum log level of the log events to be returned. Defaults to `info`. Acceptable values (in order of relative importance from smallest to largest) are `trace`, `debug`, `info`, `warn`, `error` and `fatal`.

_Example:_ `info`

**`log_event_type`**`string`Optional

The event type of log events to be returned.

_Example:_ `test_log_event`

**`source`**`string`Optional

The source of log events to be returned. Acceptable values are `slack` and `developer`.

_Example:_ `slack`

**`component_type`**`string`Optional

The component type of log events to be returned. Acceptable values are `events_api`, `workflows`, `functions` and `tables`.

_Example:_ `workflows`

**`component_id`**`string`Optional

The component ID of log events to be returned. Will be `FnXXXXXX` for functions, and `WfXXXXXX` for workflows

_Example:_ `Wf013SMGL4V9`

**`trace_id`**`string`Optional

The trace ID of log events to be returned.

_Example:_ `Tr432f2`

**`min_date_created`**`integer`Optional

The earliest timestamp of the log to retrieve (epoch microseconds).

_Example:_ `1646665572336251`

**`max_date_created`**`integer`Optional

The latest timestamp of the log to retrieve (epoch microseconds).

_Example:_ `1646665572336299`

**`sort_direction`**`string`Optional

The direction you want the data sorted by (always by timestamp)

_Acceptable values:_ `asc` `desc`

_Example:_ `asc`

## Usage info {#usage-info}

This method returns all workflow executions for an organization.

Additionally, it can be used to ingest logs and to monitor errors across an organization. This can help admins identify and fix problems with workflows and apps, and ensure that their users are having a positive experience.

Here are some specific examples of how the method can be used:

1.  An admin can use the method to identify all executions of a particular app that have failed. This information can be used to troubleshoot the app and fix the problem.
2.  An admin can use the method to track the number of executions of a workflow over time. This information can be used to identify any trends in usage, such as an increase in usage during certain times of the day or week.

Overall, this method is a powerful tool that can be used to manage and analyze executions in an organization. It can help admins to troubleshoot problems and monitor usage.

Note that if multiple filters are used, filtering will be performed with a logical 'and' operator.

## Event type definitions {#event-type-definitions}

Each event type has some subtleties, which are documented here. For example, some event types might carry a different meaning based on the log level. The content of the `payload` object for each `activity` in the `activities[]` array is also dependent on the `event_type`.

### function_execution_started {#function_execution_started}

```
	"payload": {		"function_name": "Reverse",		"function_type": "app"	}
```

### function_execution_result {#function_execution_result}

The log level could be `info` meaning the execution was a success, or could be `error` in case of failure.

```
	"payload": {		"function_name": "Reverse",		"error": "An optional error message, this property is absent in case of success."	}
```

### function_execution_output {#function_execution_output}

```
	"payload": {		"log": "The raw stdout/stderr from the function execution captured at the end of the process execution."	}
```

### function_deployment {#function_deployment}

The possible values for the `action` property are: 'Create', 'Update', and 'Delete'. _Note_: For the 'Delete' action, the property `bundle_size_kb` will be absent.

```
	"payload": {		"action": "Create",		"team_id": "T12345",		"user_id": "U12345",		"bundle_size_kb": 13	}
```

### workflow_bot_invited {#workflow_bot_invited}

```
	"payload": {		"channel_id": "C12345",		"bot_user_id": "U12345"	}
```

### workflow_execution_started {#workflow_execution_started}

```
	"payload": {		"workflow_name": "Reverse",		"actor": "U12345",	}
```

### workflow_execution_result {#workflow_execution_result}

The possible values for the `exec_outcome` property are: 'Pending', 'Success', and "Error'.

```
	"payload": {		"workflow_name": "Reverse",		"exec_outcome": "Success"	}
```

### workflow_step_started {#workflow_step_started}

```
	"payload": {		"function_id": "Fn12345",        "total_steps": 1,        "current_step": 1,        "function_name": "Reverse",        "function_execution_id": "Fx12345"	}
```

### workflow_published {#workflow_published}

```
	"payload": {		"workflow_name": "Reverse"	}
```

### workflow_unpublished {#workflow_unpublished}

```
	"payload": {		"workflow_name": "Reverse"	}
```

### workflow_step_execution_result {#workflow_step_execution_result}

The `inputs` property will display the workflow inputs, this can be anything. The possible values for the `exec_outcome` property are: 'Pending', 'Success', and "Error'.

```
	"payload": {		"inputs": {            "string": "Reverse"        },        "function_id": "Fn12345",        "exec_outcome": "Success",        "function_name": "Reverse",        "function_execution_id": "Fx12345"	}
```

### workflow_created_from_template {#workflow_created_from_template}

```
	"payload": {		"template_id": "SEND_KUDOS",		"date_created": 12345	}
```

### trigger_executed {#trigger_executed}

The possible values for the `type` property are: 'event', 'shortcut', 'webhook', 'scheduled', 'external' and "blockkit'. _Note_: The `trip_information` can be null/empty and the`config` property will be different based on the type of trigger.

```
	"payload": {		"trigger": {            "id": "Ft12345",            "type": "shortcut",            "config": {                "name": "Reverse",                "description": "Reverses a string"            },            "trip_information": {                "user_id": "U12345",                "channel_id": "C12345"            }        },        "function_name": "Reverse"	}
```

### external_auth_started {#external_auth_started}

The possible values for the `code` property are: 'app\_not\_found', 'app\_not\_installed', 'provider\_not\_found', and "external\_auth\_started'.

```
	"payload": {		"code": "external_auth_started",		"team_id": "T12345",		"user_id": "U12345",		"provider_key": "secret:key:12345",		"app_id": "A12345"	}
```

### external_auth_result {#external_auth_result}

The possible values for the `code` property can be 'oauth2\_callback\_error' or "oauth2\_exchange\_success'.

```
	"payload": {		"code": "oauth2_exchange_success",		"team_id": "T12345",		"user_id": "U12345",		"provider_key": "secret:key:12345",		"app_id": "A12345"	}
```

### external_auth_token_fetch_result {#external_auth_token_fetch_result}

There are multiple possible values for the `code` property, it will display successful or unsuccessful codes such as: 'no\_collaborator\_found', 'external\_token\_found', 'token\_not\_found', etc.

```
	"payload": {		"code": "external_token_found",		"team_id": "T12345",		"user_id": "U12345",		"provider_key": "secret:key:12345",		"app_id": "A12345"	}
```

### external_auth_missing_function {#external_auth_missing_function}

The possible value for the `code` property is only 'function\_not\_found'.

```
	"payload": {		"code": "function_not_found",		"team_id": "T12345",		"function_id": "Fn12345",		"app_id": "A12345"	}
```

### external_auth_missing_selected_auth {#external_auth_missing_selected_auth}

The possible values for the `code` property can be any error encountered; for example 'missing\_oauth\_token\_or\_selected\_auth'.

```
	"payload": {		"code": "missing_oauth_token_or_selected_auth",		"team_id": "T12345",		"user_id": "U12345",		"provider_key": "secret:key:12345",		"app_id": "A12345"	}
```

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "activities": [    {      "app_id": "A123456789",      "level": "info",      "event_type": "function_execution_started",      "source": "slack",      "component_type": "functions",      "component_id": "Fn123",      "payload": {        "function_name": "Reverse",        "function_type": "app"      },      "created": 1650463798824317,      "trace_id": "Tr123"    }  ],  "response_metadata": {    "next_cursor": ""  }}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

Something went wrong on our end, please try again.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_app`

App ID provided is not valid for team and user.

`invalid_app_id`

App ID provided is not valid.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_args`

Required arguments either were not provided or contain invalid values.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_cursor`

Value passed for `cursor` was not valid or is no longer valid.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`invalid_team`

Team ID provided is not valid

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.