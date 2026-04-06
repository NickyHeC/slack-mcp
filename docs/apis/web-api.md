Source: https://docs.slack.dev/apis/web-api

# Slack Web API

The Slack Web API is an interface for querying information _from_ and enacting change _in_ a Slack workspace.

Use it for individual queries, or as part of a more complex tapestry of platform features in a Slack app.

[Web API methods](/reference/methods)

* * *

## Basic overview {#basics}

*   The Web API is a collection of [HTTP RPC-style methods](/reference/methods), all with URLs in the form `https://slack.com/api/METHOD_FAMILY.method`.
*   While it's not a REST API, those familiar with REST should be at home with its foundations in HTTP.
*   Use HTTPS, SSL, and TLS v1.2 or above when calling all methods. [Learn more about our SSL and TLS requirements](#ssl).
*   Each method has a series of arguments informing the execution of your intentions.
*   Pass arguments as:
    *   GET querystring parameters,
    *   POST parameters presented as `application/x-www-form-urlencoded`, or
    *   a mix of both GET and POST parameters
*   [Most write methods](#methods_supporting_json) allow arguments with `application/json` attributes.
*   Some methods, such as [`chat.postMessage`](/reference/methods/chat.postMessage) and [`dialog.open`](/reference/methods/dialog.open), feature arguments that accept an associative JSON array. However, these methods can be difficult to properly construct when using a `application/x-www-form-urlencoded` Content-type, so we strongly recommend using [JSON-encoded bodies](#posting_json) instead.

### POST bodies {#post-bodies}

When sending a HTTP POST, you may present your arguments as either standard POST parameters, or you may use JSON instead.

#### URL-encoded bodies {#url-encoded-bodies}

When sending URL-encoded data, set your HTTP `Content-type` header to `application/x-www-form-urlencoded` and present your key/value pairs according to [RFC-3986](https://tools.ietf.org/html/rfc3986).

For example, a POST request to the [`conversations.create`](/reference/methods/conversations.create) method might look something like this:

```
POST /api/conversations.createContent-type: application/x-www-form-urlencodedtoken=xoxp-xxxxxxxxx-xxxx&name=something-urgent
```

#### JSON-encoded bodies {#posting_json}

For [write methods that support JSON](#methods_supporting_json), you may alternatively send your HTTP POST data as `Content-type: application/json`.

There are some ground rules:

*   You must explicitly set the `Content-type` HTTP header to `application/json`. We won't interpret your POST body as such without it.
*   You must transmit your `token` as a bearer token in the `Authorization` HTTP header.
*   You cannot send your token as part of the query string or as an attribute in your posted JSON.
*   Do not mix arguments between query string, URL-encoded POST body, and JSON attributes. Choose one approach per request.
*   Providing an explicitly `null` value for an attribute will result in whichever default behavior is assigned to it.

For example, to send the same request above to the `conversations.create` method with a JSON POST body, send something like this:

```
POST /api/conversations.createContent-type: application/jsonAuthorization: Bearer xoxp-xxxxxxxxx-xxxx{"name":"something-urgent"}
```

Note how we present the token with the string `Bearer` pre-pended to it, indicating the [OAuth 2.0](/authentication) authentication scheme. Consult your favorite HTTP tool or library's manual for further detail on setting HTTP headers.

Here's a more complicated example — posting a message with [menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages) using [`chat.postMessage`](/reference/methods/chat.postMessage):

```
POST /api/chat.postMessageContent-type: application/jsonAuthorization: Bearer xoxp-xxxxxxxxx-xxxx{"channel":"C123ABC456","text":"I hope the tour went well, Mr. Wonka.","attachments":[{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}
```

The `attachments` argument is sent a straightforward JSON array.

Here's how to do that with [cURL](https://curl.haxx.se/):

```
curl -X POST -H 'Authorization: Bearer xoxb-1234-56789abcdefghijklmnop' \-H 'Content-type: application/json' \--data '{"channel":"C123ABC456","text":"I hope the tour went well, Mr. Wonka.","attachments": [{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}' \https://slack.com/api/chat.postMessage<
```

#### Errors specific to passing JSON {#JSON-errors}

If the posted JSON is invalid, you'll receive one of the following errors in response:

*   `invalid_json`: The JSON you've included in your POST body cannot be parsed. This might be because it's actually not JSON, or perhaps you did not correctly set your HTTP `Content-type` header. Ensure your JSON attribute keys are strings wrapped with double-quote (`"`) characters.
*   `json_not_object`: We could understand that your code was JSON-like enough to parse it, but it's not actually a JSON hash of attribute key/value pairs. Perhaps you sent us an array, or just a string or a number.

In both cases, you'll need to revise your JSON or how you're transmitting your data to resolve the error condition.

## Evaluating responses {#responses}

All Web API responses contain a JSON object, which will always contain a top-level boolean property `ok` that indicates success or failure.

For failure results, the `error` property will contain a short machine-readable error code. In the case of problematic calls that could still be completed successfully, `ok` will be `true` and the `warning` property will contain a short machine-readable warning code (or comma-separated list of them, in the case of multiple warnings). See the following examples:

```
{    "ok": true,    "stuff": "This is good"}
```

```
{    "ok": false,    "error": "something_bad"}
```

```
{    "ok": true,    "warning": "something_problematic",    "stuff": "Your requested information"}
```

Other properties are defined in the documentation for each relevant method. There's a lot of "stuff" to unpack, including [these types](/reference/objects) and other method or domain-specific curiosities.

## Authentication {#authentication}

Authenticate your Web API requests by providing a [bearer token](/authentication/tokens), which identifies a single user or bot user relationship.

[Register your application](https://api.slack.com/apps) with Slack to obtain credentials for use with our [OAuth 2.0](/authentication/installing-with-oauth) implementation, which allows you to negotiate tokens on behalf of users and workspaces.

We prefer tokens to be sent in the `Authorization` HTTP header of your outbound requests. However, you may also pass tokens in all Web API calls as a POST body parameter called `token`. Tokens cannot be sent as a query parameter.

Treat tokens with care

Never share tokens with other users or applications. Do not publish tokens in public code repositories. [Review token safety tips](/security).

## HTTPS, SSL, and TLS {#ssl}

Slack requires HTTPS, SSL, and TLS v1.2 or above. The platform and the Web API are governed by the same rules. [Learn more about our deprecation of early TLS versions](/changelog/2019-07-deprecate-early-tls-versions). Stay safe and secure.

All TLS connections must use the [SNI extension](https://en.wikipedia.org/wiki/Server_Name_Indication). Lastly, TLS connections must support at least one of the following cipher suites:

TLS 1.2:

*   `ECDHE-RSA-AES128-GCM-SHA256`
*   `ECDHE-RSA-CHACHA20-POLY1305`
*   `ECDHE-RSA-AES256-GCM-SHA384`

TLS 1.3:

*   `TLS_AES_128_GCM_SHA256`
*   `TLS_AES_256_GCM_SHA384`
*   `TLS_CHACHA20_POLY1305_SHA256`

## Methods {#methods}

With over 200 methods, surely there's one right for you. You can find them all in the [reference](/reference/methods), where you can filter by method family.