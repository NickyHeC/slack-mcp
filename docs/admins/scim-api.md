Source: https://docs.slack.dev/admins/scim-api

# Using the Slack SCIM API

The SCIM API is only available to Slack workspaces on Business+ or Enterprise plans

Provision and manage user accounts and groups with the [Slack SCIM API](/reference/scim-api/scim-api) using either version 1.1 or version 2.0 of the SCIM protocol.

API method reference

Find a full reference of the Slack SCIM API methods [here](/reference/scim-api/).

## Manage people in a workspace {#manage}

[SCIM](https://scim.cloud/) is used by Single Sign-On (SSO) services and identity providers to manage people across a variety of tools, including Slack.

While other APIs are for interacting with a Slack workspace directly, the SCIM API allows teams on the Plus and Enterprise plans to administer the users on a workspace (or in an organization, in the case of Enterprise orgs).

If you've found yourself wishing for a set of `users.admin.*` endpoints, SCIM might be right for you. Use the SCIM API to write your own apps and scripts to programmatically manage the members of your workspace.

Slack [supports member provisioning](https://slack.com/help/articles/212572638-Managing-team-members-with-SCIM-provisioning) via helper apps with supported identity providers.

It's possible to de-provision an entire workspace or Enterprise organization with SCIM.

Please test your scripts thoroughly before executing them. [Our support team](https://slack.com/help/contact) is ready to assist you should you run into any trouble.

## Transitioning to SCIM 2.0 from SCIM 1.1 {#transition}

Most IDPs currently support SCIM version 2, therefore you should be able to specify the version of SCIM you’d like to use and assign the correct SCIM version connector on the IDP.

There are a few differences to be aware of between SCIM 2.0 and SCIM 1.1:

*   The base URL is `/scim/v2` instead of `/scim/v1`.
*   There are different namespaces for the SCIM V2 URI.
*   PATCH requests expect a different request body that includes an “Operations” field. The supported Operations are `remove`, `replace` and `add`. Each operation must follow the [SCIM V2 standard](https://www.rfc-editor.org/rfc/rfc7644#section-3.5.2).
*   SCIM V2 supports the scim/v2/ResourceTypes.
*   [Errors](#example-error) have a different structure.

## Accessing the SCIM API {#access}

Like other Slack APIs, the [SCIM methods](/reference/scim-api) are accessed over that old standby protocol, HTTP. It behaves slightly differently than other Slack APIs, as it is a proper REST API and thus expects HTTP verbs to be used in a specific manner.

The base URL for all calls to the SCIM API is `https://api.slack.com/scim/VERSION/`. All SCIM methods are branches of this base URL.

### Acquire an OAuth token {#permissions}

An [OAuth token](//authentication#flow) with the [`admin`](/reference/scopes/admin) scope is required to access the SCIM API.

On Business+, Slack Owners and Admins can generate a token to use the SCIM API. The token-generating account must remain an Admin or Owner in order to make SCIM updates.

In an Enterprise organization, Org Owners and Admins can use SCIM to modify users, however, only Org Owners can install the SCIM app. The token-generating account must remain an Owner or Admin in order to make SCIM updates.

One more note: the token generated can only take action on accounts with the same or fewer permissions. For example, if an Admin account generates a SCIM token, they can take action on other Admins or members. They cannot take action on Owners.

To acquire a token:

1.  [Create an app](https://api.slack.com/apps?new_app=1)
    
2.  Add the [`admin`](/reference/scopes/admin) OAuth scope.
3.  [Install the app](/app-management/quickstart-app-settings#installing).

Then you can [use the generated token](#request). If you intend to build a Slack app for other teams to install, your app will need to properly handle the OAuth flow to generate the proper token.

### Restrict API token usage by IP address {#ip-address-allowlist}

Slack can limit use of your app’s OAuth tokens to a list of IP addresses and ranges you provide. Slack will then reject Web API method calls from unlisted IP addresses.

Once you provide a list of allowed IP addresses, Slack will ony accept a request to call Web API methods if it comes from one of those IP addresses. If the request matches your allowed list, Slack will execute the request and respond as usual.

To configure your allowed IP list:

1.  Navigate to your [application management](https://api.slack.com/apps) and select the relevant privately-distributed app.
2.  Select the **OAuth & Permissions** section from the left-hand navigation.
3.  Find the **Restrict API Token Usage** section. This section lists all the **Allowed IP Address Ranges** you set up.
4.  Click **Add a new IP address range**.
5.  Enter in the desired IP address range and click **Add**.
6.  Select **Save IP address ranges**.

You can add up to 10 _entries_. Each entry specifies either a CIDR range of IP addresses or a single IP address.

For example:

*   Entering `101.101.101.106` will allow only that IP address, which we'll consider as `101.101.101.106/32`.
*   Entering a [submask](https://en.wikipedia.org/wiki/Subnetwork#Subnetting) like `101.101.101.0/24` will allow all 256 IP address between `101.101.101.0` and `101.101.101.255`.

"Local" IP addresses cannot be added to allowed lists and IPv6 is not supported.

### Use the token in a SCIM API request {#request}

The API token must be included via an `Authorization` header with a type of `Bearer` when calling any of the SCIM methods.

Provide a JSON request body for `POST`, `PUT`, and `PATCH` write operations, and set your HTTP `Content-Type` header to `application/json`.

A SCIM call may take a form like this:

```
 GET /scim/VERSION/Users?count=1000 HTTP/1.1 Host: api.slack.com Accept: application/json Authorization: Bearer xoxp-...
```

## Using SCIM in an Enterprise organization {#enterprise-org}

In an Enterprise organization, SCIM operations work across the entire organization, not individual workspaces. A SCIM app can provision, de-provision, and update team members in just one place rather than having to do so across every workspace in an organization.

For this reason, the OAuth token used for calling SCIM API methods must be obtained from installing the app on the organization, not just a workspace within the organization. To get a SCIM app working in an Enterprise organization, you'll need to do the following:

1.  Implement a standard [OAuth 2 flow](//authentication#flow). The web service powering your app requires this.
2.  [Create an app](https://api.slack.com/apps?new_app=1)
    
3.  In the app's settings, select **OAuth & Permissions** from the left navigation. Scroll down to the section titled **Scopes**, add the `admin` scope, and click **Save Changes**.
4.  Next, configure the **Redirect URI** for your app. This signifies where Slack should redirect users once they complete the OAuth flow.
5.  In the app's settings, select **Manage Distribution** from the left navigation. Under the section titled **Share Your App with Other Workspaces**, ensure all four sections are checked. Then, click **Activate Public Distribution**.
6.  Under the **Share Your App with Your Workspace** section, copy the **Shareable URL** and paste it into a browser to initiate the OAuth handshake that will install the app on your organization. You will need to be logged in as an owner of your Enterprise organization to install the app.
7.  Before you can continue, you'll need to ensure that you have implemented the OAuth flow mentioned in the first step so that users can install your app. If you don't have it set up yet, now is the time—refer to our [Installing with OAuth](/authentication/installing-with-oauth) guide for more details.
8.  Check the drop-down menu in the upper right of the installation screen to ensure you are installing the app on the Enterprise organization, not an individual workspace within the organization. (See image below.)
9.  Once your app completes the OAuth flow, you will be granted an OAuth token that can be used for calling all of the SCIM API methods for your organization. This token is the one your app should use to call the SCIM methods.

When installing the SCIM app, be sure to install it on your Enterprise organization, not a workspace within the organization.

![Installing the app on a workspace](/assets/images/workspace-v-org-d14515a9d3c6e681fa184dc7cfab99a0.png)

Usergroups on Enterprise organizations work a bit differently as well. Creating SCIM groups will create an [IDP group](https://slack.com/help/articles/115001435788-Connect-IDP-groups-to-workspaces), which may or may not be the correct behavior depending on what you hope to accomplish.

## SCIM provisioning limitations {#limitations}

*   Users can not be permanently deleted from Slack, they can only be deactivated.
*   Attempts to provision a user with a duplicate email address (even if the existing user has been previously deactivated in Slack) will fail. The existing user email address must be updated manually in Slack to free up the email to be re-provisioned.
*   When creating a new user, if anything in custom profile is invalid, all profile fields will be dropped
*   Single-Channel Guests can not be fully provisioned via SCIM. You will first need to provision them as a full user, then restrict them via the Slack admin page.
*   Group mention handles (@group) can not be set via the SCIM provisioning API.
*   Subteams that are automatically generated by Slack, such as `Team Admins`, can not be updated via the SCIM API.
*   The SCIM API is rate limited. If your requests are being limited, an `HTTP: 429` error will be returned.
*   Slack does not store `type` for `addresses`. The `type` field will be used to determine which address is the "primary address" if the request does not specify one, however the `type` is not stored.
*   Username values and channel name values must be unique and share the same namespace. For example, you can't have a username for `@general` if you also have a `#general` channel in the Slack workspace.
*   There is a limit of 50 custom profile fields, which includes fields set via the SCIM API. If your request would cause more than 50 fields to exist, the call will fail with a `unable_to_create_team_profile_fields` error.