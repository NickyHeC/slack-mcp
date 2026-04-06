Source: https://docs.slack.dev/reference/methods/apps.datastore.bulkPut

# apps.datastore.bulkPut method

DocsCall generator

## Facts {#facts}

**Description**Creates or replaces existing items in bulk

**Method Access**

*   HTTP

```
POST https://slack.com/api/apps.datastore.bulkPut
```

**Scopes**

Bot token:

[`datastore:write`](/reference/scopes/datastore.write)

**Content types**

`application/x-www-form-urlencoded`

`application/json`

**Rate Limits**[Tier 3: 50+ per minute](/apis/web-api/rate-limits)

## Arguments {#arguments}

### Required arguments

**`token`**`string`Required

Authentication token bearing required scopes. Tokens should be passed as an HTTP Authorization header or alternatively, as a POST parameter.

_Example:_ `xxxx-xxxxxxxxx-xxxx`

**`datastore`**`string`Required

name of the datastore

**`items`**`array`Required

attribute names and values of the items; limit of 25

_Example:_ `[{"id": "7c6dd137", "favourite_meal": "Shawarma", "reason": "Who doesn't like Shawarma?"}]`

### Optional arguments

**`app_id`**Optional

## Usage info {#usage-info}

This method is only available for [workflow apps](/workflows).

This method is used to create or replace items in a datastore in bulk. Limit of 25.

```
	{		"datastore": "delicious_meals",		"items": [		  {		    "id": "12462",		    "meal": "Shawarma"		  }		]	}
```

Refer to [Datastores](/tools/deno-slack-sdk/guides/using-datastores) for more information.

* * *

## Response {#response}

#### Typical success response

```
{  "ok": true,  "datastore": "delicious_meals",  "failed_items": []}
```

#### Error response for invalid datastore parameter

```
{  "ok": false,  "error": "datastore_error",  "errors": [    {      "code": "datastore_config_not_found",      "message": "The datastore configuration could not be found",      "pointer": "/datastores"    }  ]}
```

## Errors {#errors}

This table lists the expected errors that this method could return. However, other errors can be returned in the case where the service is down or other unexpected factors affect processing. Callers should always check the value of the `ok` parameter in the response.

Error

Description

`access_denied`

Not authorized to access the datastore.

`access_denied`

Access to a resource specified in the request is denied.

`accesslimited`

Access to this method is limited on the current network

`account_inactive`

Authentication token is for a deleted user or workspace when using a `bot` token.

`app_not_hosted`

The app developer is not using a Slack-hosted environment. App datastores are exclusively available for Slack-hosted apps.

`datastore_error`

Datastore error

`datastore_migration_in_progress`

The datastore is currently unavailable due to an in progress Enterprise org migration.

`deprecated_endpoint`

The endpoint has been deprecated.

`ekm_access_denied`

Administrators have suspended the ability to post a message.

`enterprise_is_restricted`

The method cannot be called from an Enterprise.

`fatal_error`

The server could not complete your operation(s) without encountering a catastrophic error. It's possible some aspect of the operation succeeded before the error was raised.

`free_team_not_allowed`

Datastore put not allowed on a free team.

`internal_error`

The server could not complete your operation(s) without encountering an error, likely due to a transient issue on our end. It's possible some aspect of the operation succeeded before the error was raised.

`invalid_app_id`

The app\_id provided is not valid for team and user.

`invalid_arg_name`

The method was passed an argument whose name falls outside the bounds of accepted or expected values. This includes very long names and names with non-alphanumeric characters other than `_`. If you get this error, it is typically an indication that you have made a _very_ malformed API call.

`invalid_arguments`

The request is missing required arguments.

`invalid_arguments`

The method was called with invalid arguments.

`invalid_array_arg`

The method was passed an array as an argument. Please only input valid strings.

`invalid_auth`

Not authorized to create datastore items.

`invalid_auth`

Some aspect of authentication cannot be validated. Either the provided token is invalid or the request originates from an IP address disallowed from making the request.

`invalid_charset`

The method was called via a `POST` request, but the `charset` specified in the `Content-Type` header was invalid. Valid charset names are: `utf-8` `iso-8859-1`.

`invalid_datastore`

The provided datastore is invalid.

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

`no_permission`

The workspace token used in this request does not have the permissions necessary to complete the request. Make sure your app is a member of the conversation it's attempting to post a message to.

`not_allowed_token_type`

The token type used in this request is not allowed.

`not_authed`

No authentication token provided.

`org_login_required`

The workspace is undergoing an enterprise migration and will not be available until migration is complete.

`partial_failure`

some items failed to be updated

`ratelimited`

The request has been ratelimited. Refer to the `Retry-After` header for when to retry the request.

`request_timeout`

The method was called via a `POST` request, but the `POST` data was either missing or truncated.

`restricted_plan_level`

Feature is not available on this team

`service_unavailable`

The service is temporarily unavailable

`team_access_not_granted`

The token used is not granted the specific workspace access required to complete this request.

`team_added_to_org`

The workspace associated with your request is currently undergoing migration to an Enterprise Organization. Web API and other platform operations will be intermittently unavailable until the transition is complete.

`team_quota_exceeded`

Total number of requests exceeded team quota.

`token_expired`

Authentication token has expired

`token_revoked`

Authentication token is for a deleted user or workspace or the app has been removed when using a `user` token.

`two_factor_setup_required`

Two factor setup is required.

`unknown_method`

This method does not exist