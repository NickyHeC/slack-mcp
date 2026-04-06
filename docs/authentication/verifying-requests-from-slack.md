Source: https://docs.slack.dev/authentication/verifying-requests-from-slack

# Verifying requests from Slack

Slack signs its requests using a secret unique to your app.

With the help of signed secrets, your app can more confidently verify whether requests from Slack are authentic. The signing process is the cooler, younger sibling of verification tokens.

## Understanding HTTP requests from Slack {#http-requests}

Slack uses HTTP requests to notify your app that something has happened. If you're subscribed to the [Events API](/apis/events-api/), your app might receive a request when a reacji has been added to a message. If you're the proud owner of a [slash command](/interactivity/implementing-slash-commands), your app'll be notified when someone uses your command. You might even be notified that your app has been given new resources and permissions.

An HTTP request contains:

*   a request line: GET /slackapi/interactive-message-action-response
*   a series of headers, like Content-type: application/json; charset=utf-8
*   a blank line
*   a UTF-8 encoded message body, like userID=1234&someField=5678

When Slack sends your app a request, your app must check to make sure it's authentic. You do this by computing a signature.

## Understanding signed secrets {#about}

Slack creates a unique string for your app and shares it with you. Verify requests from Slack with confidence by verifying signatures using your signing secret.

On each HTTP request that Slack sends, Slack adds an `X-Slack-Signature` HTTP header (or `x-slack-signature` — **header names are meant to be case-insensitive, so the letter case should not be assumed**).

The signature is created by hashing the request body with the SHA-256 function, and combining it with an [HMAC](https://en.wikipedia.org/wiki/HMAC) signing secret. The resulting signature is unique to each request and doesn't contain any secret information, keeping your app secure.

Signing secrets replace the old [verification tokens](/apis/events-api/#url_verification). Good news: the new signature is used _exactly the same way_ as the deprecated verification token. It's just computed more securely.

Some SDKs perform signature verification automatically, accessible via a drop-in replacement of your signing secret for your old verification token. See the [SDK support](#sdk_support) section for more detail.

Request signing follows this pattern:

*   Your app receives a request from Slack.
*   Your app computes a signature based on the request.
*   You make sure the signature _you've_ computed matches the signature _on the request_.

Let's go over the recipe for this signature dish.

## Validating a request {#validating-a-request}

Ingredients required:

*   1 HTTP request from Slack
*   1 signing secret
*   1 programming language of your choice

**Note:** This pseudocode example walks through validating a request. Nearly all modern programming languages can perform equivalent calculations with HMAC SHA256. [Here's the library for Node, for example.](https://nodejs.org/api/crypto.html#crypto_crypto_createhmac_algorithm_key_options)

**1\. Grab your Slack [Signing Secret](#signing_secrets_admin_page), available in the app admin panel under Basic Info.**

In this example, the **Signing Secret** is `8f742231b10e8888abcd99yyyzzz85a5`. (You don't need to convert the **Signing Secret** to binary. Treat it as a standard UTF-8 string.) While you're at it, extract the raw request body from the request.

```
slack_signing_secret = 'MY_SLACK_SIGNING_SECRET' // Set this as an environment variable>>> 8f742231b10e8888abcd99yyyzzz85a5request_body = request.body()>>> token=xyzz0WbapA4vBCDEFasx0q6G&team_id=T1DC2JH3J&team_domain=testteamnow&channel_id=G8PSS9T3V&channel_name=foobar&user_id=U2CERLKJA&user_name=roadrunner&command=%2Fwebhook-collect&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT1DC2JH3J%2F397700885554%2F96rGlfmibIGlgcZRskXaIFfN&trigger_id=398738663015.47445629121.803a0bc887a14d10d2c447fce8b6703c
```

Use the raw request body, without headers, before it has been deserialized from JSON or other forms

For example, in Python's Flask, use `request.get_data()` before accessing any other methods on the request in order to get the raw request payload, without performing JSON deserialization.

**2\. Extract the timestamp header from the request.**

In our example the timestamp header is `1531420618`.

The signature depends on the timestamp to protect against replay attacks. While you're extracting the timestamp, check to make sure that the request occurred recently. In this example, we verify that the timestamp does not differ from local time by more than five minutes.

```
timestamp = request.headers['X-Slack-Request-Timestamp']>>> 1531420618if absolute_value(time.time() - timestamp) > 60 * 5:    # The request timestamp is more than five minutes from local time.    # It could be a replay attack, so let's ignore it.    return
```

**3\. Concatenate the version number, the timestamp, and the request body together, using a colon (`:`) as a delimiter.**

In this example, we have the following values:

*   version number: `v0`
*   timestamp: `1531420618`
*   request body: `token=xyzz...`

The resulting example basestring is (`'v0:1531420618:token=xyzz...`).

```
sig_basestring = 'v0:' + timestamp + ':' + request_body>>> 'v0:1531420618:token=xyzz0WbapA4vBCDEFasx0q6G&team_id=T1DC2JH3J&team_domain=testteamnow&channel_id=G8PSS9T3V&channel_name=foobar&user_id=U2CERLKJA&user_name=roadrunner&command=%2Fwebhook-collect&text=&response_url=https%3A%2F%2Fhooks.slack.com%2Fcommands%2FT1DC2JH3J%2F397700885554%2F96rGlfmibIGlgcZRskXaIFfN&trigger_id=398738663015.47445629121.803a0bc887a14d10d2c447fce8b6703c'
```

**4\. Hash the resulting string, using the signing secret as a key, and taking the hex digest of the hash.**

In this example, we compute a hex digest of `a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503`.

The full signature is formed by prefixing the hex digest with `v0=`, to make `'v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503'`.

```
my_signature = 'v0=' + hmac.compute_hash_sha256(slack_signing_secret,sig_basestring).hexdigest()>>> 'v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503'
```

**5\. Compare the resulting signature to the header on the request.**

For best practice, use an hmac `compare` function instead of directly comparing the signatures for equality.

```
slack_signature = request.headers['x-slack-signature']>>> 'v0=a2114d57b48eac39b9ad189dd8316235a7b4a8d21a10bd27519666489c69b503'if hmac.compare(my_signature, slack_signature):    # hooray, the request came from Slack!    deal_with_request(request)
```

## App management updates {#app-management-updates}

For a while, you'll see two secrets side-by-side in the app management panel:

![Admin page with signing secret and verification token](/assets/images/signing_secrets_admin_page-f7bedc42883405cc5d03c586b4905b25.png)

One secret is the new **Signing Secret**, and one is the deprecated verification token. **We strongly recommend you _only_ use the Signing Secret from now on.**

## Regenerating secrets {#regenerating}

Regenerate your secret using the "Regenerate" button next to the **Signing Secret** in the [admin panel](https://api.slack.com/apps).

## Regenerating client secrets {#client-secrets}

Regenerate your client secret using the "Regenerate" button next to the **Client Secret** in the [admin panel](https://api.slack.com/apps). The previous secret remains valid for 24 hours unless revoked manually. Ensure to update the client secret in your app and re-deploy it within that time frame to avoid user authentication failures.

## SDK support {#SDK-support}

These Slack SDKs, among others, currently support signing secrets:

*   [Built-in support in Bolt for JavaScript](https://github.com/slackapi/bolt-js/blob/main/src/receivers/verify-request.ts)
*   [Built-in support in Bolt for Python](https://github.com/slackapi/bolt-python/tree/main/slack_bolt/middleware/request_verification)
*   [Built-in support in Bolt for Java](https://github.com/slackapi/java-slack-sdk/blob/main/bolt/src/main/java/com/slack/api/bolt/middleware/builtin/RequestVerification.java)

In each package, using a signed secret is no different than using the old verification token. Set your **Signing Secret** as an environment variable: `export SLACK_SIGNING_SECRET=abc123`. Then, initialize the package with the secret.

For example, a Node app that uses interactive messages would create a message listener using the following single line of code:

```
// Create the adapter using the app's signing secret, read from envconst interactions = createMessageAdapter(process.env.SLACK_SIGNING_SECRET);
```

A Node app that uses the Events API would initialize a listener for events using the following code:

```
const slackEvents = createSlackEventAdapter(process.env.SLACK_SIGNING_SECRET);
```

A Python app that uses the Events API would initialize a listener for events using the following code:

```
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]slack_events = SlackEventAdapter(SLACK_SIGNING_SECRET, "/slack/events")
```

You can also examine the open-source [BotKit](https://github.com/howdyai/botkit/blob/main/packages/botbuilder-adapter-slack/src/slack_adapter.ts) to see an implementation of Slack signature verification in the wild.

## Types of requests that support signed secrets {#types_of_events}

*   [Events API](/apis/events-api/)
*   [Shortcuts](/interactivity/implementing-shortcuts)
*   [Slash commands](/interactivity/implementing-slash-commands)

Some legacy features also support signed secrets, but we'd rather you not use them:

*   [Legacy interactive messages](/legacy/legacy-messaging/legacy-making-messages-interactive)
*   [Legacy message buttons](/legacy/legacy-messaging/legacy-message-buttons)
*   [Legacy message menus](/legacy/legacy-messaging/legacy-adding-menus-to-messages)
*   [Legacy outgoing webhooks](/legacy/legacy-custom-integrations/legacy-custom-integrations-outgoing-webhooks)

## Using mutual TLS {#mutual-tls}

Requests from Slack also support authentication through [**Mutual TLS**](https://en.wikipedia.org/wiki/Mutual_authentication).

Mutual TLS has the same goal as request signing: it allows your app to verify that an outgoing HTTP request is authentic. Mutual TLS _differs_ from request signing in where and how it occurs. Instead of verifying request signatures in your application code, you configure your TLS-terminating server to authenticate client certificates from Slack.

Here's the Mutual TLS process in more detail:

**1\. Configure your TLS-terminating server to request client certificates.**

Your TLS-terminating server should be configured to accept client certificates under _any_ [DigiCert root CA certificate](https://www.digicert.com/kb/digicert-root-certificates.htm#roots).

Slack's client certificate may not be signed directly by a root CA certificate, but requests from Slack will include any intermediate CA certificates necessary for verification.

**2\. Extract either of the following fields in the certificate:**

*   `Subject Alternative Name`: `DNS:platform-tls-client.slack.com`. By [RFC 6125](https://tools.ietf.org/html/rfc6125), this is the recommended field to extract.
*   `Subject Common Name`: `platform-tls-client.slack.com`.

**3\. Inject the extracted domain into a header, and forward the request to your application server.**

Here's an example header you might add to the request: `X-Client-Certificate-SAN: platform-tls-client.slack.com`. Whatever you choose to call your header, check to make sure this header hasn't _already_ been added to the request. Your upstream application server **must know** that the header was added by your TLS-terminating server as part of the Mutual TLS process.

**4\. In your application server, check the header and verify that its value matches the expected domain, `platform-tls-client.slack.com`.**

Do not accept header values with any other domain name, including other subdomains of slack.com.