Source: https://docs.slack.dev/reference/interaction-payloads/shortcuts-interaction-payload

# Shortcuts interaction payloads

Received when a user uses any [shortcut created by the receiving app](/interactivity/implementing-shortcuts).

Read our guide to [handling payloads from user interactions](/interactivity/handling-user-interaction#payloads) to learn how your app should process and respond to these payloads.

* * *

## Fields {#fields}

This is a non-exhaustive list of fields that can be encountered in this type of interaction payload:

Field

Description

`type`

Helps identify which type of interactive component sent the payload. [Global shortcuts](/interactivity/implementing-shortcuts#global) will return `shortcut`, [message shortcuts](/interactivity/implementing-shortcuts#message) will return `message_action`.

`callback_id`

An ID that you [defined when creating the shortcut](/interactivity/implementing-shortcuts#creating_shortcut).

`trigger_id`

A temporary ID generated for the interaction in your app. This value [can be used to open modals](/interactivity/handling-user-interaction#modal_responses).

`response_url`

A temporary [webhook](/messaging/sending-messages-using-incoming-webhooks) that can be used [to send messages in response to interactions](/interactivity/handling-user-interaction#message_responses). **This field will only be included for [message shortcuts](/interactivity/implementing-shortcuts)**. If you want to send messages in response to global shortcuts, [read this guide](/surfaces/modals#modal_response_url).

`user`

The user who initiated the shortcut.

`message`

The [message](/messaging/retrieving-messages#individual_messages) that the user initiated the shortcut from. **This field will only be included for [message shortcuts](/interactivity/implementing-shortcuts#message)**. This will include the full structure of the message.

`channel`

The [channel](/reference/objects/channel-object) that the source `message` was located in. **This field will only be included for [message shortcuts](/interactivity/implementing-shortcuts#message)**.

`team`

The workspace (what we used to call a [`team`](/reference/methods/team.info)) that the shortcut was initiated in.

`token`

A deprecated verification token feature. You _should_ validate the request payload, however, and the best way to do so is to [use the signing secret provided to your app](/authentication/verifying-requests-from-slack).

* * *

## Examples {#examples}

A payload received when a [global shortcut](/interactivity/implementing-shortcuts#global) is used:

```
{    "type": "shortcut",    "token": "XXXXXXXXXXXXX",    "action_ts": "1581106241.371594",    "team": {        "id": "TXXXXXXXX",        "domain": "shortcuts-test"    },    "user": {        "id": "UXXXXXXXXX",        "username": "aman",        "team_id": "TXXXXXXXX"    },    "callback_id": "shortcut_create_task",    "trigger_id": "944799105734.773906753841.38b5894552bdd4a780554ee59d1f3638"}
```

A payload received when a [message shortcut](/interactivity/implementing-shortcuts#message) is used in a message context menu:

```
{    "token": "Nj2rfC2hU8mAfgaJLemZgO7H",    "callback_id": "chirp_message",    "type": "message_action",    "trigger_id": "13345224609.8534564800.6f8ab1f53e13d0cd15f96106292d5536",    "response_url": "https://hooks.slack.com/app-actions/T0MJR11A4/21974584944/yk1S9ndf35Q1flupVG5JbpM6",    "team": {        "id": "T0MJRM1A7",        "domain": "pandamonium"    },    "channel": {        "id": "D0LFFBKLZ",        "name": "cats"    },    "user": {        "id": "U0D15K92L",        "name": "dr_maomao"    },    "message": {        "type": "message",        "user": "U0MJRG1AL",        "ts": "1516229207.000133",        "text": "World's smallest big cat! <https://youtube.com/watch?v=W86cTIoMv2U>"    }}
```