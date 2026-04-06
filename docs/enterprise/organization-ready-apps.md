Source: https://docs.slack.dev/enterprise/organization-ready-apps

# Managing organization-ready apps

For administrators, you may be wondering about what makes apps organization-ready, and when they need to be. Read on for more information.

## Benefits of org-ready apps {#benefits}

First, let's take a look at some of the benefits for users within your Enterprise organization:

*   Org Admins (that's you!) will be able to distribute apps easily across all workspaces, or restrict access to certain workspaces.
*   Pre-approved apps can be automatically installed when a workspace is created.
*   Users only have to authenticate with an app once for all workspaces that have access to the app.

Organization-ready apps are installed once at the organization level, but an organization-ready app isn't automatically added to the workspaces in an organization, nor does it enjoy any additional privileges by being installed at the organization level. Read more about this nuance [below](#choose-workspaces). The app has a single token that represents the permissions for the app on multiple workspaces, and is authorized once for an entire organization using an OAuth flow. Org Admins can then add it to workspaces in the organization without further authorization.

Sometimes apps are required to be organization-ready:

*   Apps that contain [custom steps](/workflows/workflow-steps) intended for use in Workflow Builder must opt-in to be organization-ready.
*   [Deno-based apps](/workflows) are automatically organization-ready.

In the latter case, the apps are Slack-hosted, so we take care of the heavy lifting for you— but for the former case, read on to learn what actions need to be taken to ensure that apps with custom steps are available for use in Workflow Builder.

* * *

## Preparing apps for an Enterprise org {#why_prepare_for_enterprise}

There are a few ways an app can be installed within an Enterprise organization:

1.  On a workspace within an [Enterprise organization](/enterprise/developing-for-enterprise-orgs). This type of installation is only available for a Slack app that does not contain a [custom step](/workflows/workflow-steps) intended for use in Workflow Builder (the only option for this case would be organization-wide installation). Similarly, [apps created with the Deno Slack SDK](/tools/deno-slack-sdk/) cannot be installed in this way.
2.  [Org-ready apps installed on the organization level](/enterprise/organization-ready-apps) can be granted access for some or all of the workspaces in that Enterprise organization. This is the only installation option compatible with custom steps intended for use in Workflow Builder.
3.  An app can be installed at an organization level. This is a specific type of app; usually an admin or Data Loss Prevention (DLP) type app.

Now, if an app is installed by one or more Enterprise org workspaces, or a workspace the app is already installed on becomes part of an Enterprise organization's workspace:

*   The app may not know what to do with messages and users originating from [shared channels](#shared_channels).
*   The app may have trouble dealing with object IDs beginning with atypical characters, such as user IDs starting with `W`.
*   The bot could blindly reply multiple times to messages, not recognizing a unique message delivery scenario introduced by [shared channels](#shared_channels).
*   Workspaces in an Enterprise org are often large and some API responses, such as channel memberships, can grow immense. The app may need to change how it digests this information.

You never know when a specific workspace in an Enterprise org will install the app. Without making a few tweaks, new users may notice these quirks in the app's behavior. Although apps that are installed in an Enterprise organization look similar to apps installed on a single workspace, there are a few changes to be aware of before apps can be deployed across an organization.

* * *

## Installing organization-ready apps {#installing}

When you install an app across the entire organization, it is not added to any workspaces in the organization. You must do this later, but you can add the app to several workspaces at once.

Organization-ready apps can be installed in the following ways:

*   via the UI from [app settings](https://api.slack.com/apps)
*   via the [OAuth flow](/authentication/installing-with-oauth)
*   via the [CLI](/tools/slack-cli)

Apps installed via app settings will generate the organization-wide token automatically, whereas apps installed via OAuth will require a handshake to succeed in order to programmatically generate the token. Both installation methods provide the token the app will use to interact with the Slack platform APIs. Regardless of how the app is installed, the organization-wide token behaves the same.

## Choosing which workspaces the app is in {#choose-workspaces}

Apps installed at the organization level and granted to one or more workspaces in the organization do not have any additional privileges compared to an app installed at the workspace level alone. Organization-ready apps do not need to be granted to all workspaces, and they in fact are not added to any automatically when they are org-installed. Org Admins can determine to which workspaces the app is granted from the admin dashboard. The advantages of installing at the organization level are as follows:

*   the ability to have the app follow an [organization policy](https://slack.com/help/articles/360038559694-Set-organization-level-policies-for-apps#:~:text=Setting%20an%20app%20management%20policy,been%20approved%20for%20their%20workspaces.)
*   to [simplify token storage](/enterprise/migrating-to-organization-wide-deployment#tokens)
*   the ability to share [custom steps](/workflows/workflow-steps) defined in app code for use in Workflow Builder

The restrictions defined by which workspaces the app is added to carry through to which users will have access to the app's custom steps in Workflow Builder.

For example, say you have an Enterprise organization called Fiber Arts. Fiber Arts has three workspaces: Knitting, Crochet, and Embroidery. If the organization-ready app, StitchFix, is shared only with workspaces Knitting and Crochet, then users in Embroidery cannot access it or any custom steps belonging to it. Further, any workflows built using the custom steps from StitchFix cannot be accessed or used by users in Embroidery.

### How to add the app to a workspace from the admin dashboard {#how-to-add-the-app-to-a-workspace-from-the-admin-dashboard}

Once an app has been installed on the organization, follow these steps to add it to one or more workspaces.

1.  As an admin user, navigate to the admin dashboard for your org. You can find this by clicking on the workspace name in Slack and selecting **Organization Settings**. The URL will be something like `app.slack.com/manage/<your-enterprise-id-here>`.
2.  Click on **Integrations** in the left-hand sidebar; then **Installed apps**.
3.  Find the app you'd like to add, then click the three dots to the right of its name. Select **Add to more workspaces**. Select the workspaces you'd like to add it to, then click **Next**.
4.  Review the permissions that the app requires, then click **Next**. Select **I'm ready to add this app** at the next modal, and finally click **Add App**.

## Next steps {#next-steps}

✨ Read more about [automating app approvals in an Enterprise org](/admins/managing-app-approvals).