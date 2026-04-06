Source: https://docs.slack.dev/enterprise/testing-enterprise-org-apps

# Testing Enterprise org apps

## Provisioning a sandbox {#sandbox}

Need a safe place to test your Enterprise org applications? The Slack Developer Program offers [developer sandboxes](/tools/developer-sandboxes) and the Slack Partner Developer Program offers [partner sandboxes](/tools/partner-sandboxes), which are fully-featured Enterprise org environments that allow you to build and test safely without impacting a production environment.

As a member of the Slack Developer Program, you can provision up to two active sandboxes at any given time. Each sandbox supports up to three workspaces, eight users, and provides access to all Enterprise org features needed for comprehensive testing. Developer sandboxes have a default lifespan of six months and can be extended as long as you remain in the Developer Program.

## Completing the organization setup {#complete_the_org_setup}

1.  Click **Finish Setup** in the email invitation.
2.  Enter your name and create a password to set up a Primary Org Owner account.
3.  Give your organization a name. This name can be updated later if you decide you want to change it, but please note that you cannot change the URL of your sandbox organization.
4.  Agree to the general terms of service.

## Creating a workspace {#create_a_workspace}

Once the Primary Org Owner creates their account, they should create at least one workspace. Click **Manage Workspaces**, and you will be guided through the process of setting up a new workspace. You will need to provide a name and a subdomain for each workspace you create.

## Setting up authentication {#set_up_authentication}

Enterprise orgs, besides our dandy [developer sandboxes](/tools/developer-sandboxes), require all users to use SSO, which means that admins must set up an Identity Provider (IdP).

### Simple IdP {#simple-idp}

If you don't have access to an IdP, we offer a Slack app, Simple IdP, which mocks an IdP to enable creation and management of user accounts. If you opt to use Simple IdP, all user accounts for your Enterprise org sandbox must be created with the test IdP, and it will not be possible to create and use accounts outside of the test IdP app. Instructions for managing accounts are as follows:

Navigate to​ [https://slack-test-idp-for-sandboxes.herokuapp.com](https://slack-test-idp-for-sandboxes.herokuapp.com) and install the app. Make sure you install the app on the org and not a workspace!

![Image showing the install step where the user can select the organization for installing.](/assets/images/sandbox-install-idp-d03914a1724355a54bd1138acc425520.png)

Copy over the required pre-configured settings from Simple IdP that you need to copy into your sandbox's SSO configurations.

![Image showing the where to copy and paste SSO configuration settings](/assets/images/sandbox-config-fields_full-f20b0e9640fe2a8e8ab49b3f16162989.png)

You can now add as many auto-generated users as you like through Simple IdP. For the most part, these auto-generated users are good for testing your app. However, if you need more than one real person signed into your organization at a time, you'll need to take a few extra steps due to how the Simple IdP app works: each person that you want to be able to sign into the sandbox will first need to sign in as the primary owner, authenticate the Simple IdP app, sign out, and then sign in as themselves.

First, navigate to **Create a custom user** and provision an account for them in the Simple IdP app. They will now appear in the **Organization Members** list at http://\[org-domain\].enterprise.slack.com/manage/people.

Add that user to a workspace, then instruct them to follow these steps:

1.  Navigate to the sign-in page for the workspace you added them to (http://\[workspace-domain\].slack.com/).
2.  Click **Sign in with SAML**.
3.  Click **Sign in with Slack** on the page that loads.
4.  Sign in with the primary owner's email and password.
5.  Authorize the Simple IdP app.
6.  Enter the user's email address on the resulting page, and click **Sign In**. That will take them to the Org control panel, where they can then launch the team. After that, they'll remain logged in.

If you have questions as you start to use your sandbox, please contact support and the Slack support team will get back to you as quickly as possible.

## Data retention {#data_retention}

As a test instance, your Enterprise org sandbox comes with some limitations. For those building third party apps on Slack, the developer instance of an Enterprise org is a **development sandbox** with limitations around data retention and user account creation. These limitations exist because **the sandbox isn't intended for normal use**; it is intended for testing purposes only. Therefore, Slack will retain messages and files shared in the sandbox for only three days after they're created.

## Next steps {#next-steps}

✨ Read more about [developing apps for Enterprise orgs](/enterprise/developing-for-enterprise-orgs).