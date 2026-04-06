Source: https://docs.slack.dev/authentication/sign-in-with-slack/using-auth0-for-sign-in-with-slack-links

# Using Auth0 for Sign in with Slack links

Sign in with Slack links is a paid feature.

Interested parties should reach out to [partnersupport@slack-corp.com](mailto:partnersupport@slack-corp.com) for more information.

Sign in with Slack (SIWS) links allow a user to share their Slack identity with your app when they click on a link from your service. When a user clicks on your link, Slack will utilize the [OpenID Connect (OIDC) standard](https://openid.net/specs/openid-connect-core-1_0.html) to send over a user’s identity information.

## Prerequisites {#prerequisites}

*   You have a Slack app using [granular permissions](/app-management/quickstart-app-settings).
*   You have implemented [Sign in with Slack using OpenID Connect](/authentication/sign-in-with-slack/).
*   You are able to implement automatic provisioning and account linking within your product.

## Domain Verification {#domain}

In order to receive a user’s information when a link is clicked, you will first need to verify that you own your domain(s). This domain must be different from your production domain.

1.  Reach out to [partnersupport@slack-corp.com](mailto:partnersupport@slack-corp.com) to request that Domain Verification be enabled for your team.
    
2.  Navigate to your app's "Domain Verification" page. Go to your [app settings](https://api.slack.com/apps) page - you'll find "Domain Verification" under **Settings** in the left sidebar.
    
3.  Click "Add Domain". Follow the prompts and enter the domain.
    
4.  Reach out to [partnersupport@slack-corp.com](mailto:partnersupport@slack-corp.com) to confirm your domains.
    

## Set up OpenID {#implement}

You will need to implement Sign in with Slack for your service using [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html).

1.  Choose an existing OpenID Connect Relying Party client for your tech stack (or create your own by following the standard) and point it towards Slack’s provided OpenID configuration URL. For this guide, we are using Auth0 as our client, but you can use whichever you’d like.
    
2.  Navigate to your app settings `Oauth and Permissions` page. Add a redirect URL where you would like the OpenID flow to redirect after it’s completed, then click Save.
    
    For an Auth0 service, this may look like: `https://slacktest.us.auth0.com/login/callback`
    
3.  Add the OpenID scopes:
    

*   [`openid`](/reference/scopes/openid)
*   [`email`](/reference/scopes/email)
*   [`profile`](/reference/scopes/profile).

4.  Navigate to your OpenID connect Relying Party client (Auth0 for us), navigate to **Enterprise** and then **Connections**. Click on **OpenID Connect** to create a new connection.
    
    *   For Logo URL, you can use this sample URL: `https://a.slack-edge.com/80588/marketing/img/meta/favicon-32.png`
        
    *   For Issuer URL, use this URL: `https://slack.com/.well-known/openid-configuration`
        
5.  We support both **Front Channel** and **Back Channel** types.
    
    We have noticed that using the **Front Channel** method means that cookies are not sent by default in Chrome once the `form_post` actually posts due to the SameSite restriction. If this means nothing to you, feel free to ignore!
    
    If you use Back Channel, enter your **Client Secret** as well. The **Client Secret** can be found on the "Basic Information" page in App Management.
    
    Click **Issuer Details** and check whether or not the **Token Endpoint** is filled in. If it is not filled in, please enter: `https://slack.com/api/openid.connect.token`. This endpoint is subject to change but we'll alert you if it is changed.
    
6.  Under **Scopes**, you should see `openid profile email`. Add the identity scopes from your Slack App scopes: `openid profile email identity.basic identity.email identity.team identity.avatar`
    
7.  Click **Save Changes**.
    

For reference, here an example of a filled out Auth0 Configuration page:

![](https://media.slack-github.com/user/847/files/d659bd80-38df-11eb-850a-714a3baf5a48)

From the **OpenID Connect** page, click the **Try** button to give it a try!

## Implement automatic account provisioning and linking {#account-provision}

When a link that conforms to the domain pattern (e.g. `https://your-service.net/work-object/1`) is first clicked in Slack, Slack will prompt the user to transfer their Slack identity to you.

The prompt will look something like this:

![SIWS Modal](/assets/images/siws_modal-9153ae2c1f147a5a0dee84c3f2edb3fd.png)

If a user clicks **Accept**, Slack will redirect the user to an [endpoint](https://openid.net/specs/openid-connect-core-1_0.html#ThirdPartyInitiatedLogin) with a login hint to start the identity transfer.

If the user clicks **Decline**, we will redirect to the link clicked. If a user declines three times, they will no longer see the prompt.

Below is what this process looks like:

![](https://media.slack-github.com/user/847/files/0608c580-38e0-11eb-8f76-279a441db823)

Slack will redirect to a login initiation endpoint that you have specified in your App Configuration Pages with the following parameters:

Name

Value

Notes

`iss`

`https://slack.com`

`login_hint`

JWT-encoded target user information

Option to JWT decode this and check if the target user is already logged-in, bypassing the OpenID connect flow

The OpenID Connect specification for [initiating Login from a Third Party](https://openid.net/specs/openid-connect-core-1_0.html#ThirdPartyInitiatedLogin) specifies how this endpoint is used. After receiving the request, your app will start an OpenID Connect authentication similar to the Sign in with Slack flow described above but with the `login_hint` parameter appended to the authorization URL.

When the flow is complete, there should be an additional key set with the claims called `https://slack.com/target_uri`. This is the URI the user originally clicked.

## Sample workflow {#sample}

1.  Your app sends an Authentication Request to a Slack endpoint (e.g. [https://slack.com/openid/connect/authorize](https://slack.com/openid/connect/authorize)):
    
    ```
      GET /siws/authorize?    response_type=id_token    &client_id=6371490080.1055357699042    &redirect_uri=https%3A%2F%2Fid.test.net%2Fsiws%2Fauth    &scope=openid%20email%20profile    &login_hint=T5J4Q04QG-W1H5Z2EHE-bjzess81jq7ehbvq6ewta90pllihsqor    &response_mode=form_post    &state=af0ifjsldkj    &nonce=n-0S6_WzA2Mj HTTP/1.1  Host: slack.com
    ```
    
2.  Slack verifies the request but will _**not**_ **conduct End-User Consent authorization**, it will proceed without prompting the user. If the `login_hint` does not match an existing stored link click, the Authentication Request will fail.
    
3.  Slack sends an Authentication Response to your app by sending a POST request to your response endpoint (e.g. `https://id.test.net/siws/auth`) with the following parameters:
    

Name

Value

`id_token`

JWT-encoded payload

`expires_in`

300

`state`

State sent in Authentication Request

4.  After decoding, the JWT-encoded payload will include the following:
    
    ```
    {    "iss": "https://slack.com",    "sub": "jsmith@slack-corp.com",    "aud": "6371490080.1055357699042",    "exp": 1592939535,    "iat": 1592939235,    "auth_time": 1592939235,    "nonce": "n-0S6_WzA2Mj",    "email": "bfan@slack-corp.com",    "locale": "en-US",    "name": "John Smith",    "given_name": "John",    "family_name": "Smith",    "picture": "https://s3-us-west-2.amazonaws.com/slack-files-dev2/avatars/...",    "https://slack.com/user_id": "U123ABC456",    "https://slack.com/user_image_24": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/user_image_32": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/user_image_48": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/user_image_72": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/user_image_192": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/user_image_512": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/user_image_1024": "https://s3-us-west-2.amazonaws.com/...",    "https://slack.com/team_id": "T0123ABC456",    "https://slack.com/team_name": "John Testy",    "https://slack.com/team_domain": "johntesty",    "https://slack.com/team_image_34": "https://slack.com/dev-cdn/v1587409668/...",    "https://slack.com/team_image_44": "https://slack.com/dev-cdn/v1587409668/...",    "https://slack.com/team_image_68": "https://slack.com/dev-cdn/v1587409668/...",    "https://slack.com/team_image_default": true,    "https://slack.com/target_uri": "https://johnjiratest.test.net/browse/PLAT-1"}
    ```
    
5.  You MUST verify that the `nonce` matches the one originally sent. It should also verify the JWT using the JWKS defined by Slack and verify that the JWT has not expired.
    
6.  You can now check if an account with this email already exists. If it does not, you can automatically provision an account for the user. If it does, it will add Sign in with Slack as an additional login method for the account.