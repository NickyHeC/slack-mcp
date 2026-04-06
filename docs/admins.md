Source: https://docs.slack.dev/admins

# Admin resources

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

Managing Slack, more streamlined than ever. Use approval and provisioning APIs to help Slack Admins work more effectively. Secure your organization with auditing and session management APIs.

## Guides for admins {#management}

### Manage app approvals {#manage_app_approvals}

Build an app that can handle approvals and restrictions for admins across an entire Slack org. Read our guide to [app approval APIs](/admins/managing-app-approvals).

### Manage channels {#manage_channels}

Handle the intricacies of creating public and private channels, setting preferences, and connecting new workspaces—all with a single app. Use the [APIs for channel management](/admins/managing-channels).

### Manage invite requests {#manage_invite_requests}

Let users invite friends to unexplored workspaces, while maintaining admin approval over those invites. Explore [the invite request management APIs](/admins/managing-invite-requests).

### Manage users {#manage_users}

An app can create a workspace and control addition and removal of that workspace's users. Apps can even mark a user as an admin or owner. Read our guide to [the APIs for managing users in a workspace](/admins/managing-users).

Other things you can do to manage users include:

*   Using **allowlists**: You can add, remove, and list membership allowlists for private channels.
*   **Reset sessions rapidly**: When you suspect a device—mobile, web, or both—has been swiped, take immediate action.
*   **Define default channels for IDP groups**: An [IDP group](https://slack.com/help/articles/115001435788-Connect-identity-provider-groups-to-your-Enterprise-organization) represents a group of users synced from your identity provider (IDP). You can add, remove, and list default channels for an IDP group.

### Manage workflow and connector permissions {#workflow-connector}

Learn more about using the suite of API methods, including bulk actions, to manage workflow permissions and approval requests [here](/admins/managing-workflow-and-connector-permissions).

## APIs for admins {#apis}

### Admin Oversight API {#oversight}

Access channel information, channel membership, and specific messages with the [Admin Oversight API](/admins/admin-oversight-api).

### Audit Logs API {#audit-logs}

Monitor workspace events and keep track of what's happening in your organization using the [Audit Logs API](/admins/audit-logs-api/).

### Legal Holds API {#legal-holds}

Use the [Legal Holds API](/admins/legal-holds-api) to ensure that relevant data in Slack is saved to preserve potentially important electronically stored information for legal or compliance purposes.

### SCIM API {#scim}

Provision and manage user accounts and groups with the [SCIM API](/admins/scim-api/).