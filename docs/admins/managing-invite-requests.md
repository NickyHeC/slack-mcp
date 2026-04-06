Source: https://docs.slack.dev/admins/managing-invite-requests

# Managing invite requests

The features within are only available to Slack workspaces on an Enterprise plan.

Don't have a paid plan? Join the [Developer Program](https://api.slack.com/developer-program) and provision a fully-featured sandbox for free.

By default, Slack users can [invite other users](https://slack.com/help/articles/201330256-Invite-new-members-to-your-workspace) into their Slack workspace and Enterprise org, either as a [guest](https://slack.com/help/articles/202518103-multi-channel-and-single-channel-guests) or full member.

You can restrict who can invite users, however. When the **Invite Request approval** setting is turned on, [users need to request invitations for other people](https://slack.com/help/articles/201330256-invite-new-members-to-your-workspace#manage-pending-invitations). Those invitation requests can be approved or denied by a workspace owner or admin.

That process can be time-consuming. Instead, use the invite request management APIs to build an app that gracefully approves and denies invite requests across all workspaces in your Enterprise org.

Read on for all the details on the invite request management APIs.

* * *

## Scopes {#scopes}

Two scopes allow an app to manage invite requests across an Enterprise org:

*   [`admin.invites:read`](/reference/scopes/admin.invites.read) allows the app to list invite requests, and subscribe to the [`invite_requested`](#events) event.
*   [`admin.invites:write`](/reference/scopes/admin.invites.write) allows the app to [approve](/reference/methods/admin.inviteRequests.approve) or [deny](/reference/methods/admin.inviteRequests.deny) requests for an invite.

All `admin.*` scopes are obtained using the normal [OAuth flow](/authentication), but there are a few extra requirements. The OAuth installation must:

*   be initiated by an Enterprise org admin or owner.
*   take place on the Enterprise org, not on an individual workspace, using the workspace switcher during the install flow.

![Installing the app on a workspace](/assets/images/workspace-v-org-audit-10f163aac79dc5f2c15e3ebe8267dbf4.png)

Check out the [scope documentation for more detail](/reference/scopes/admin.invites.read).

* * *

## Listen for the invite_requested event {#events}

Now that you're setup with the scopes needed to handle invite requests, it's time to listen for requests. The [`invite_requested`](/reference/events/invite_requested) event from the [Events API](/apis/events-api/) notifies your app when a user makes a request to invite someone new to a workspace.

When an application subscribed to the `invite_requested` event is installed to an org, workspace owners and admins will no longer receive invite notifications from Slackbot.

Subscribe to the `invite_requested` event by navigating to your [App page](https://api.slack.com/apps) and clicking on **Event Subscriptions** in the left sidebar. The **Add Workspace Event** button will lead you to the `invite_requested` event. You'll need to reinstall your app for your subscription to take effect.

Here's the outline of an `invite_requested` event:

```
{    "type": "invite_requested",    "invite_request": {        "id": string,        "email": string,        "date_created": int,        "requester_ids": [string],        "channel_ids": [string],        "invite_type": string,        "real_name": string,        "date_expire": int,        "request_reason": string,        "team": {            "id": string,            "name": string,            "domain": string        }    }}
```

A few nuances on those fields inside the `invite_request` object you'll find in the event payload:

*   `email` is the email of the new, invited user.
*   `invite_type` indicates whether the user is a multi-channel guest, a single-channel guest, or full member. It accepts either the string `restricted`, `ultra_restricted`, or `full_member` corresponding to those three types of channel members.

* * *

## Approve, deny, and manage requests {#methods}

Armed with the `id` of the `invite_request` object you received in the [above event](#events), your app is ready to approve or deny a request.

### Approve a request {#approve}

Approve a request to invite someone into a workspace with the [`admin.inviteRequests.approve`](/reference/methods/admin.inviteRequests.approve) method:

```
curl -F token=xoxp-... -F team_id=T9876 -F invite_request_id=1234 https://slack.com/api/admin.inviteRequests.approve
```

### Deny a request {#deny}

Alternatively, if that request invite is not requited by your admins, deny it with the [`admin.inviteRequests.deny`](/reference/methods/admin.inviteRequests.deny) method:

```
curl -F token=xoxp-... -F team_id=T9876 -F invite_request_id=1234 https://slack.com/api/admin.inviteRequests.deny
```

### Manage requests {#manage}

Lost your place? You can list the pending request invites in a specific workspace with the [`admin.inviteRequests.list`](/reference/methods/admin.inviteRequests.list) method:

```
curl -F token=xoxp-... -F team_id=T9876 https://slack.com/api/admin.inviteRequests.list
```

You'll receive a response containing a list of `invite_requests`, each of which is identical to what's found in the `invite_requested` event payload [described above](#events).

And, finally, if you want to know which requests have been approved or denied, you can use the [`admin.inviteRequests.approved.list`](/reference/methods/admin.inviteRequests.approved.list) method:

```
curl -F token=xoxp-... -F team_id=T9876 https://slack.com/api/admin.inviteRequests.approved.listcurl -F token=xoxp-... -F team_id=T9876 https://slack.com/api/admin.inviteRequests.denied.list
```

* * *

## Parting words of wisdom {#parting-words}

The more partners who partake in a Slack conversation, the more productive Slack can be. Let your users bring their +1s to the party, while retaining the peace of mind afforded by admin approval of invites.

Use the invite request management APIs to gracefully approve or deny invite requests. Spare your Enterprise org admins time and focus. Plus, users win too: they get an immediate response, rather than waiting until an admin can carve out time for approvals.

If you love streamlining the Slack admin experience, read up on our other [APIs for workspace management](/admins).