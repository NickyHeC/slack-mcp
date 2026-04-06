Source: https://docs.slack.dev/reference/methods/functions.workflows.steps.list

# functions.workflows.steps.list method

DocsCall generator

## Facts {#facts}

**Description**List the steps of a specific function of a workflow's versions

**Method Access**

*   HTTP
*   JavaScript
*   Python
*   Java

```
POST https://slack.com/api/functions.workflows.steps.list
```

[![bolt-js](/img/logos/bolt-js-logo.svg)](/tools/bolt-js)

```
app.client.functions.workflows.steps.list
```

[![bolt-py](/img/logos/bolt-py-logo.svg)](/tools/bolt-python)

```
app.client.functions_workflows_steps_list
```

[![bolt-java](/img/logos/bolt-java-logo.svg)](/tools/java-slack-sdk/guides/getting-started-with-bolt)

```
app.client().functionsWorkflowsStepsList
```

**Scopes**_No scopes required_

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`function_id`**`string`Required

The ID of the function to query

### Optional arguments

**`workflow_id`**`string`Optional

The workflow ID, starts with Wf\*

**`workflow`**`string`Optional

The workflow encoded ID or workflow reference

_Example:_ `#/workflows/my-workflow`

**`workflow_app_id`**`string`Optional

The app tied to the workflow reference.

## Usage info {#usage-info}

This method is used to list steps in a workflow that use a specific function. Most commonly, it's used to find steps that use the [OpenForm Slack function](/tools/deno-slack-sdk/guides/creating-a-form), so that form responses may be exported using the [functions.workflows.steps.responses.export](/reference/methods/functions.workflows.steps.responses.export) method. The `function_id` of OpenForm will always be `Fn010N`.

To identify the workflow you want to list steps from, you can use a workflow ID:

```
	{		"workflow_id": "WfABC123",		"function_id": "Fn010N",	}
```

or the app ID that contains the workflow and the workflow reference:

```
	{		"workflow_app_id": "AABC123",		"workflow": "#/workflows/my_workflow_callback_id",		"function_id": "Fn010N",	}
```

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "steps_versions": [    {      "title": "Send a greeting",      "workflow_id": "Wf014H7FCWG2",      "step_id": "0",      "is_deleted": false,      "workflow_version_created": "1677282339978193"    }  ]}
```

#### Error response for an unknown workflow

```
{  "ok": false,  "error": "unknown_workflow_id"}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

This actor does not have access to the functions on this team.

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`cannot_fetch_versions`

Encountered unexpected error while trying to fetch versions

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The arguments passed in are invalid.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_form_data`

The method was called via a `POST` request with `Content-Type` `application/x-www-form-urlencoded` or `multipart/form-data`, but the form data was either missing or syntactically invalid.

`invalid_post_type`

The method was called via a `POST` request, but the specified `Content-Type` was invalid. Valid types are: `application/json` `application/x-www-form-urlencoded` `multipart/form-data` `text/plain`.

`method_deprecated`

The method has been deprecated.

`missing_post_type`

The method was called via a `POST` request and included a data payload, but the request did not include a `Content-Type` header.

`missing_scope`

The token used is not granted the specific scope permissions required to complete this request.

`missing_step_ids`

The passed in workflow is missing step IDs

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

`unknown_app_id`

The passed in workflow\_app\_id is invalid.

`unknown_function_id`

The passed in function\_id is invalid.

`unknown_method`

This method does not exist.

`unknown_workflow_id`

The passed in workflow\_id is invalid.