Source: https://docs.slack.dev/authentication

# Authentication overview

Authentication is a critical part of the development process, but it doesn’t have to be daunting. With the right tools and best practices, you’ll have a secure, smooth authentication flow. Whether you’re handling [OAuth 2.0](/authentication/installing-with-oauth), [verifying requests](/authentication/verifying-requests-from-slack), or setting up [Sign in with Slack](/authentication/sign-in-with-slack/), we’ve got you covered.

## Authentication basics {#basics}

Before your app can access Slack data or interact with Slack workspaces, it must go through an authentication process. This involves obtaining the necessary tokens and permissions for your app to function properly. Slack apps use OAuth [scopes](/reference/scopes) to govern what they can access. These are added in the app settings when building an app. You will attach these scopes to your tokens. Check out [tokens](/authentication/tokens) to learn more. You can rotate those tokens too! Find out how on the [Using token rotation](/authentication/using-token-rotation) page.

## Key concepts {#concepts}

*   [**OAuth 2.0**](/authentication/installing-with-oauth): Learn how to use OAuth 2.0 to securely authenticate users and request access tokens.
*   [**Tokens**](/authentication/tokens): Understand the different types of tokens your app can use (user tokens, bot tokens, and app tokens) and how to manage them, as well as employ token rotation and expiry to keep things fresh.
*   [**Security best practices**](/security): Learn about security practices for managing authentication, such as validating tokens, handling sensitive data, and protecting your app from unauthorized access.

## Reference {#reference}

*   [**Scopes and Permissions**](/reference/scopes): Find the right permissions for your app to ensure access is limited to only the necessary data.