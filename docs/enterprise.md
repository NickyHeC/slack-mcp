Source: https://docs.slack.dev/enterprise

# Enterprise Organizations

Whether you're a developer, an administrator, or a member of a security team tasked with implementing and protecting the infrastructure of your Enterprise organization, we're here to help you get started—but first, let's go over the basics.

## What is Enterprise organization? {#what}

An Enterprise organization is a network of two or more Slack workspace instances. Each Slack workspace has its own ID, directory of members, channels, conversations, and files. For the most part, each workspace behaves and functions as you're used to on a single, standalone workspace.

For developers, the biggest change for your apps to handle is that some channels and conversations can be [shared](#understanding_shared_channels) between multiple workspaces within the same Enterprise organization. But as with a standalone Slack workspace, workspaces in an Enterprise org have their own application installations.

In addition, this guide may be your first introduction to the following terms:

*   _Enterprise organization_: An entity used to describe multiple Slack workspaces within the same organization.
*   _Enterprise organization user_: These users have the same identity and profile across all workspaces within an organization.
*   _Enterprise user ID_: A user ID beginning with `U` or `W`, representing the user across all workspaces within an Enterprise org.
*   _Legacy user ID_: Also known as a "team user ID", these are the User IDs you've come to know and love in Slack if you've only developed for standalone workspaces before. They begin with `U`. Also known as a _local user ID_.
*   _Shared channel_: A channel shared between two or more workspaces within an organization.
*   _Translation layer_: A translating service that converts new organization-based user IDs to legacy team user IDs, allowing apps to migrate data.
*   _Workspace_: Where a team works. The terms _workspace_ and _team_ are often used interchangeably. When you see the object name such as `team_id`, it means the ID for a workspace.

## Enterprise organizations for developers {#enterprise-org-devs}

Developers may encounter a variety of use cases when developing apps for Enterprise organizations:

*   CI/CD integration: automate app deployment with CI/CD pipelines for secure and compliant releases.
*   Streamlined app approvals: automate admin approvals for Slack apps to reduce friction while maintaining security.
*   Cross-platform workflows: connect Slack with Enterprise tools for seamless automation.

To address those use cases, we recommend checking out the following resources:

*   [Setting up CI/CD with the Slack CLI](/tools/slack-cli/guides/setting-up-ci-cd-with-the-slack-cli)
*   [CI/CD authorization in the Slack CLI](/tools/slack-cli/guides/authorizing-the-slack-cli/#ci-cd)
*   [Developing apps for Enterprise orgs](/enterprise/developing-for-enterprise-orgs)
*   [Enterprise readiness](/workflows/run-on-slack-infrastructure/#enterprise)
*   [App approval process for developers](/tools/deno-slack-sdk/guides/controlling-permissions-for-admins/#approval-developers)
*   [Migrating existing apps to an Enterprise org](/enterprise/migrating-to-organization-wide-deployment)
*   [Testing Enterprise org apps](/enterprise/testing-enterprise-org-apps)
*   [Understanding Slack Connect](/apis/slack-connect/)
*   [Using Slack Connect API methods](/apis/slack-connect/using-slack-connect-api-methods)

## Enterprise organizations for admins {#enterprise-org-admins}

Org Admins (or admins in general) may encounter a variety of use cases when developing for Enterprise orgs:

*   Automated user provisioning: sync with Enterprise directories for easy onboarding/offboarding.
*   Compliance and policy enforcement: automate security policies, app restrictions, and audits.
*   Enterprise-wide automation governance: provide oversight for all Slack automation while keeping teams empowered.

To address those use cases, we recommend checking out the following resources:

*   [Managing users](/admins/managing-users)
*   [Using the Slack SCIM API](/admins/scim-api)
*   [Managing organization-ready apps](/enterprise/organization-ready-apps)
*   [Managing app approvals](/admins/managing-app-approvals)
*   [App approval process for admins](/tools/deno-slack-sdk/guides/controlling-permissions-for-admins/#approval-developers)
*   [Managing workflow and connector permissions](/admins/managing-workflow-and-connector-permissions)

## Enterprise organizations for security teams {#enterprise-org-security}

Security developers or team members may encounter a variety of use cases when developing for Enterprise orgs:

*   App and token security reviews: automatically review new apps and flag security risks.
*   Security alerts and incident response: route critical security alerts to the right teams in real-time.
*   Automated token rotation and secret management: keep credentials secure without manual intervention.

To address those use cases, we recommend checking out the following resources:

*   [Security best practices](/security)
*   [Installing with OAuth](/authentication/installing-with-oauth)
*   [Using Sign in with Slack](/authentication/sign-in-with-slack/)
*   [Verifying requests from Slack](/authentication/verifying-requests-from-slack)
*   [Using the Audit Logs API](/admins/audit-logs-api)
*   [Using token rotation](/authentication/using-token-rotation)

## Shared channels {#shared-channels}

A shared channel is a bridge between workspaces that need to collaborate together. Teams can use shared channels to connect, chat, share files, and use apps in the same way as they do on a standalone workspace.

To illustrate the power of shared channels, let's rewind to life _before_ them to understand how they can make your working life more pleasant and productive:

![Before shared channels](/assets/images/before_shared_channels-85237b8d0b9bb40eaaf0110b35ba5e43.png)

Previously, what team members of Catnip Inc. were saying and doing on a shared project with Woof Inc. was a mystery. When the two teams tried to communicate, it was disconnected and disparate.

This is solved with the shared channels of today. Now, the project channel `#projectM` exists in each team's workspace, making communication much simpler.

![After shared channels](/assets/images/after_shared_channels-81b0f71b1325e4871e50faba05ec0c24.png)

There are two types of shared channels, each with different uses:

*   **Slack Connect channels**, which allow up to 20 organizations to come together in a single channel (e.g., Catnip, Inc. and Woof Inc. from the examples above). To learn more about how shared channels work, check out our documentation on [Slack Connect](/apis/slack-connect/).
    
*   **Multi-workspace shared channels**, which are channels shared between multiple workspaces within the same organization's Slack instance. For example, the `#treats` channel is shared in Woof Inc's, Marketing, Engineering, _and_ Social workspaces. It exists in all three places, within Woof Inc.'s single Enterprise org instance.
    

## Next steps {#next-steps}

✨ Read about [migrating existing apps to an Enterprise org](/enterprise/migrating-to-organization-wide-deployment).