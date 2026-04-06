Source: https://docs.slack.dev/reference/interaction-payloads

# Interaction payloads

Interaction payloads are sent to your app when an end user interacts with one of a range of Slack app features.

The resulting interaction payload can have different structures depending on the source. The structures will have a `type` field that indicates the source of the interaction.

The `interactivity` type includes properties for both context about the `interactor` (i.e., the user) and an `interactivity_pointer`. This type can be input to function as with other attributes: through a Workflow Builder template (e.g., a user who clicked a button) or as an output from a previous step. The only functions allowed to output the `interactivity context` are [Slack functions](/tools/deno-slack-sdk/guides/creating-slack-functions). An example is as follows:

```
{  "interactor": {    "id": "U01AB2CDEFG",    "secret": "AbCdEFghIJklOMno1P2qRStuVwXyZAbcDef3GhijKLM4NoPqRSTuVWXyZaB5CdEfGHIjKLM6NoP7QrSt"  },  "interactivity_pointer": "1234567890123.4567890123456.78a90bc12d3e4f567g89h0i1j23k4l56"}
```

For more details, refer to [interactivity](/tools/deno-slack-sdk/guides/utilizing-slack-and-custom-data-types#interactivity).

Read the individual reference guides to see the breakdown of each `type` of payload:

Payload type

Description

[`block_actions`](/reference/interaction-payloads/block_actions-payload)

Received when a user clicks a [Block Kit interactive component](/block-kit#making-things-interactive).

[`message_actions`](/reference/interaction-payloads/shortcuts-interaction-payload#message_actions)

Received when an [app action in the message menu](/interactivity/implementing-shortcuts#messages) is used.

[`view_closed`](/reference/interaction-payloads/view-interactions-payload#view_closed)

Received when a [modal is canceled](/surfaces/modals#modal_cancellations).

[`view_submission`](/reference/interaction-payloads/view-interactions-payload#view_submission)

Received when a [modal is submitted](/surfaces/modals#handling_submissions).

Read our guide to [handling payloads from user interactions](/interactivity/handling-user-interaction#payloads) to learn how your app should process and respond to these payloads.