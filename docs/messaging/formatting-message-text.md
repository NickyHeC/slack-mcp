Source: https://docs.slack.dev/messaging/formatting-message-text

# Formatting message text

These are developer-focused instructions for posting messages to Slack using API methods.

For user instructions on message formatting in your Slack client, refer to this [Help Center article](https://slack.com/help/articles/202288908).

You can format messages within the various [surfaces](/surfaces) of your app, such as messages, modals, or the app's App Home. The [Block Kit](/block-kit) blocks and elements that comprise the layouts for these surfaces frequently use [text objects](/reference/block-kit/composition-objects/text-object) to insert content, which can be formatted with markdown to create useful visual highlights or utilize certain syntax to trigger special parsing.

[Block Kit Builder](https://api.slack.com/tools/block-kit-builder) is a visual prototyping sandbox that will allow you to choose from, configure, and preview all the available blocks. You can also check out the reference guide on [blocks](/reference/block-kit/blocks), which contains the specifications of every block and the JSON fields required for each.

## Formatting with markdown {#formatting}

There are a variety of ways to format message using markdown in Slack:

*   You can use it in most Block Kit [text objects](/reference/block-kit/composition-objects/text-object) by setting the `type` field to `mrkdwn`. (There are a few blocks and elements that only allow `plain_text`; these are called out in the documentation on [blocks](/reference/block-kit/blocks)).
*   We support markdown types for rich text when using Block Kit. Check out our [rich text block](/reference/block-kit/blocks/rich-text-block/) and [markdown block](/reference/block-kit/blocks/markdown-block/) references for more details.
*   The `mrkdwn` argument is the default formatting method when publishing a message, for example by using the [`chat.postMessage`](/reference/methods/chat.postmessage) API method.
*   The `mrkdwn` property can also be used to format blocks and elements used when unfurling links in messages using [composer unfurls](/messaging/unfurling-links-in-messages#unfurl_previews) or within [Work Objects](/messaging/work-objects-implementation#implementation-unfurl).
*   The `markdown_text` argument can be used to format text when beginning a new streaming conversation, for example by using the [`chat.startStream`](/reference/methods/chat.startStream) API method.

Markdown vs. `mrkdown`

Note that `mrkdwn` is Slack's custom text formatting syntax. It is inspired by markdown, but uses different rules. Read on for more details.

### Basic visual styles {#visual-styles}

Apply visual styles as follows:

*   `_italic_` will produce _italicized_ text
*   `*bold*` will produce **bold** text
*   `~strike~` will produce strikethrough text

### Line breaks {#line-breaks}

You can use multi-line text in app-generated text. Insert a newline by including the string `\n` in your text. For example, the following formatting:

```
This is a line of text.\nAnd this is another one.
```

will produce the following text:

```
This is a line of text.And this is another one.
```

### Block quotes {#quotes}

You can highlight text as a block quote by using the `>` character at the beginning of one or more lines:

```
This is unquoted text\n>This is quoted text\n>This is still quoted text\nThis is unquoted text again
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22This%20is%20unquoted%20text%5Cn%3EThis%20is%20quoted%20text%5Cn%3EThis%20is%20still%20quoted%20text%5CnThis%20is%20unquoted%20text%20again%22%0A%09%09%7D%0A%09%7D%0A%5D)

### Code blocks {#inline-code}

If you have text that you want highlighted like code (`like this`), surround it with backtick (\`) characters:

```
This is a sentence with some `inline *code*` in it.
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22This%20is%20a%20sentence%20with%20some%20%60inline%20*code*%60%20in%20it.%20%22%0A%09%09%7D%0A%09%7D%0A%5D)

Text within inline code blocks will not use any other formatting, so it can be useful even if you're not displaying actual code.

You can also highlight larger, multi-line code blocks by placing 3 backticks before and after the block:

````
```This is a code block\nAnd it's multi-line```
````

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22%60%60%60This%20is%20a%20code%20block%5CnAnd%20it%27s%20multi-line%60%60%60%22%0A%09%09%7D%0A%09%7D%0A%5D)

### Lists {#lists}

There's no specific list syntax in app-published text, but you can mimic list formatting with regular text and line breaks as follows:

```
- Mihara and New Tideland\n- RaviHyral\n- TranRollinHyfa
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22%E2%80%A2%20Mihara%20and%20New%20Tideland%5Cn%E2%80%A2%20RaviHyral%5Cn%E2%80%A2%20TranRollinHyfa%22%0A%09%09%7D%0A%09%7D%0A%5D)

### Links {#linking-urls}

To link to URLs in a conversation, include the URL directly in `mrkdwn` text and it will be auto-transformed by the server into a link.

URLs with spaces will break, so we recommend that you remove any spaces from your URL links.

```
This message contains a URL: https://docs.slack.dev/
```

```
So does this one: https://docs.slack.dev/
```

You can also use `mrkdwn` to manually add links:

```
This message contains a URL: <https://docs.slack.dev/>
```

Adjust the text that appears as the link from the URL to something else:

```
<https://docs.slack.dev/|This message is a link>
```

And create email links:

```
<mailto:perihelion@univmiharanewtideland.com|Email Perihelion>
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22This%20message%20contains%20a%20URL:%20http%3A%2F%2Fdocs.slack.dev%2F%5CnSo%20does%20this%20one%3A%20https://docs.slack.dev%5CnThis%20message%20contains%20a%20URL:%20%3Chttp%3A%2F%2Fdocs.slack.dev%2F%3E%5Cn%3Chttp%3A%2F%2Fwww.docs.slack.dev%7CThis%20message%20is%20a%20link%3E%5Cn%3Cmailto%3Aperehelion%40univmiharanewtideland.com%7CEmail%20Perehelion%3E%22%0A%09%09%7D%0A%09%7D%0A%5D)

You can also use [Block Kit buttons](/reference/block-kit/block-elements/button-element) as links by using the `url` parameter in [button elements](/reference/block-kit/block-elements/button-element).

#### Links in retrieved messages {#links-in-retrieved-messages}

When you use any of the [messaging API methods](/messaging/) to [retrieve a message](/messaging/retrieving-messages), you'll see that auto-transformed URLs are shown in the formatted `mrkdwn` text. So this:

```
This message contains a URL: https://docs.slack.dev/
```

Will be represented in the API as:

```
This message contains a URL <https://docs.slack.dev/>
```

While this message:

```
So does this one: https://docs.slack.dev/
```

Will be retrieved in this form:

```
So does this one: <https://docs.slack.dev/|https://docs.slack.dev/>
```

### Emoji {#emoji}

Emoji can be included directly in text. Once published, Slack will convert the emoji into their common 'colon' format. For example, a message published as follows:

```
It's Friday 🎉
```

will be converted into 'colon' format:

```
It's Friday :tada:
```

If you're publishing text with emoji, you don't need to worry about converting them. If you're [retrieving messages](/messaging/retrieving-messages), you'll receive the emojis in 'colon' format, so you may want to convert them back to their unicode emoji form. The list of supported emoji are taken from [https://github.com/iamcal/emoji-data](https://github.com/iamcal/emoji-data).

### Escaping text {#escaping}

It's important to know that there are some characters in text strings that must be escaped.

Slack uses `&`, `<`, and `>` as control characters for [special parsing in text objects](#advanced), so they must be converted to HTML entities if they're not going to be used for their parsing purpose. Therefore, if you want to use one of these characters in a text string, you should replace the character with its corresponding HTML entity as shown:

Symbol

HTML entity

`&`

`&amp;`

`<`

`&lt;`

`>`

`&gt;`

You shouldn't encode the entire piece of text, as only the specific characters shown above will be decoded for display in Slack.

## Advanced formatting {#advanced}

We mentioned earlier the need to escape certain strings in text objects. These strings are used to trigger special parsing of the text, such as [user mentions](#mentioning-users) or [advanced date formatting](#date-formatting). Read on to learn more about this advanced formatting.

### Linking to channels {#linking-channels}

Text can refer to a [Slack channel](/reference/objects/conversation-object) and transform that reference into a link to the channel itself. This uses a similar `mrkdwn` syntax as regular URL links:

```
Why not join <#C123ABC456>?
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22Why%20not%20join%20%3C%23C024BE7LR%7Cgeneral%3E%3F%22%0A%09%09%7D%0A%09%7D%0A%5D)

In this example, `#C123ABC456` is the channel's ID. Your app can get this ID from an [interaction request payload](/messaging/creating-interactive-messages#request), the [Event API payload](/reference/events/app_mention) sent when [one of the event types](/reference/events) occurs, or by looking it up directly with [the conversation-related methods of the Web API](/apis/web-api/using-the-conversations-api). You can also manually retrieve a specific channel's ID from its URL:

```
https://app.slack.com/client/E123ABC456/C123ABC456
```

When text containing the channel linking syntax is published in an app surface, the ID is automatically converted to show the actual name of the conversation. If any of the channel members do not have access to the linked private channel, they will only see an unclickable `private channel` label.

If you're [retrieving messages](/messaging/retrieving-messages), use the [`conversations.info`](/reference/methods/conversations.info) API method to look up by channel ID and find out other relevant information, such as the actual name of the channel.

### Mentioning users {#mentioning-users}

A [mention](https://slack.com/help/articles/205240127-Mention-a-member) is a special type of reference that provides a link to the mentioned user's profile in the text. If the mention is included in an app-published [message](/messaging), the mentioned user will also be notified about the reference. This [Help Center article](https://slack.com/help/articles/205240127-Mention-a-member) describes what that notification process looks like.

To mention a user, provide their user ID with the following syntax:

```
Hey <@U012AB3CD>, thanks for submitting your report.
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22Hey%20%3C%40U024BE7LH%3E%2C%20thanks%20for%20submitting%20your%20report!%22%0A%09%09%7D%0A%09%7D%0A%5D)

Your app can get this user ID from an [interaction request payload](/messaging/creating-interactive-messages#request), the [Event API payload](/reference/events/app_mention) sent when [one of the event types](/reference/events) occurs, or by looking them up via the [`users.list` Web API](/reference/methods/users.list) using another unique piece of information you have about them, such as their email address. You can also manually retrieve a specific user's ID by clicking the overflow button in their Slack profile and choosing the `Copy member ID` option. When text containing the user-mention syntax is published by an app, the ID will be automatically converted to show the [display name](https://slack.com/help/articles/216360827-Change-your-display-name) of the user.

If you're [retrieving messages](/messaging/retrieving-messages), you can use the [`users.info`](/reference/methods/users.info) API method to look up by user ID and find out other relevant information, such as their display name.

### Mentioning groups {#mentioning-groups}

As with [users](#mentioning-users), you can also mention [user groups](https://slack.com/help/articles/212906697-Create-a-user-group), which will link to the group's profile.

If the mention is included in an app-published [message](/messaging), Slack will notify each user in the group about the mention. To mention a user group, provide the group ID with the following general syntax:

```
`<!subteam^ID>`
```

`!subteam^` is a literal string that should not change, but `ID` should be replaced with the actual user group ID. Here's an example:

```
Hey <!subteam^SAZ94GDB8>, there's a new task in your queue.
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22Hey%20%3C!subteam%5ESAZ94GDB8%3E%2C%20did%20you%20see%20my%20file%3F%22%0A%09%09%7D%0A%09%7D%0A%5D)

Your app can get this group ID from the [Event API payload](/reference/events/app_mention) sent when [one of the `subteam` event types](/reference/events) occurs, or by looking them up via the [`usergroups.list`](/reference/methods/usergroups.list) API method. You can also manually retrieve a specific user group's ID from the URL shown when viewing its profile. When text containing the user group mention syntax is published by an app, the ID will be automatically converted to show the name of the user group.

If you're [retrieving messages](/messaging/retrieving-messages), you can use the [`usergroups.list`](/reference/methods/usergroups.list) API method to look up by user group ID and find out other relevant information.

### Special mentions {#special-mentions}

These special groups should be mentioned sparingly, as they tend to notify a large group of users.

Use discretion by mentioning [individuals](#mentioning-users) or [more specific groups](#mentioning-groups) whenever possible.

There are a few core user groups built into Slack that can be mentioned:

*   `@here` notifies the [active](https://slack.com/help/articles/201864558#availability-in-slack) members of a channel.
*   `@channel` notifies all members of a channel, active or not.
*   `@everyone` notifies every person in the [`#general` channel](https://slack.com/help/articles/220105027-The-general-channel) (i.e., every non-guest member of a workspace).

To add these to a message, use the following syntax:

```
Hey <!here>, there's a new task in your queue.
```

### Date formatting {#date-formatting}

Text containing a date or time should display that date in the local timezone of the person seeing the text. For app-published text, there is a handy date syntax available to format a Unix timestamp, and Slack will handle the timezone localization for you.

The displayed time will be based on the timezone setting of the device used to observe the text, not the timezone set within **Preferences** in the Slack client being used to observe it. For more details about managing your timezone preferences, refer to this [Help Center article](https://slack.com/help/articles/219889247-Manage-your-time-zone-preferences).

The `<!date>` command will format the timestamp using tokens within a string that you set, and it must include some fallback text for older Slack clients. Here's the general syntax to use:

```
<!date^timestamp^token_string^optional_link|fallback_text>
```

This can be broken down as follows:

*   The wrapping `<>` is used as a control character for the whole string, and `^` is used to divide different parts of the string.
*   `!date` indicates to use the special date parsing.
*   `timestamp` is a number in standard [Unix time format](https://en.wikipedia.org/wiki/Unix_time), the date and time that you want to include in your text.
*   `token_string` should provide a formatting for your timestamp, using plain text along with any of the following tokens:
    *   `{date_num}` is displayed as `2014-02-18`. It will include leading zeros before the month and date and is probably best for more technical integrations that require a developer-friendly date format.
    *   `{date}` is displayed as `February 18th, 2014`. The year will be omitted if the date is less than six months in the past or future.
    *   `{date_short}` is displayed as `Feb 18, 2014`. The year will be omitted if the date is less than six months in the past or future.
    *   `{date_long}` is displayed as `Tuesday, February 18th, 2014`. The year will be omitted if the date is less than six months in the past or future.
    *   `{date_pretty}` displays the same as `{date}` but uses "yesterday", "today", or "tomorrow" where appropriate.
    *   `{date_short_pretty}` displays the same as `{date_short}` but uses "yesterday", "today", or "tomorrow" where appropriate.
    *   `{date_long_pretty}` displays the same as `{date_long}` but uses "yesterday", "today", or "tomorrow" where appropriate.
    *   `{time}` is displayed as `6:39 AM` or `6:39 PM` in 12-hour format. If the client is set to show 24-hour format, it is displayed as `06:39` or `18:39`.
    *   `{time_secs}` is displayed as `6:39:45 AM` `6:39:42 PM` in 12-hour format. In 24-hour format it is displayed as `06:39:45` or `18:39:42`.
    *   `{ago}` is displayed as a human-readable period of time, e.g. `3 minutes ago`, `4 hours ago`, `2 days ago`.
*   `optional_link` can be provided if your timestamp needs to be linked, specified using a standard, fully qualified URL.
*   `fallback_text` should be included just in case the client is unable to process the date. Consider adding timezone information to your fallback text since it will potentially be different from the timezone of the person reading it.

Here are some examples of date formatting strings:

```
<!date^1392734382^Posted {date_num} {time_secs}|Posted 2014-02-18 6:39:42 AM PST>
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22%3C!date%5E1392734382%5EPosted%20%7Bdate_num%7D%20%7Btime_secs%7D%7CPosted%202014-02-18%206%3A39%3A42%20AM%20PST%3E%22%0A%09%09%7D%0A%09%7D%0A%5D)

```
<!date^1392734382^{date} at {time}|February 18th, 2014 at 6:39 AM PST>
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22%3C!date%5E1392734382%5E%7Bdate%7D%20at%20%7Btime%7D%7CFebruary%2018th%2C%202014%20at%206%3A39%20AM%20PST%3E%22%0A%09%09%7D%0A%09%7D%0A%5D)

```
<!date^1392734382^{date_short}^https://example.com/|Feb 18, 2014 PST>
```

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22%3C!date%5E1392734382%5E%7Bdate_short%7D%5Ehttps%3A%2F%2Fexample.com%2F%7CFeb%2018%2C%202014%20PST%3E%22%0A%09%09%7D%0A%09%7D%0A%5D)

If you're [retrieving messages](/messaging/retrieving-messages), you'll receive the `<!date>` string back in its original format, and you can use the information above to parse it if necessary.

### Automatic parsing {#automatic-parsing}

Earlier, we explained how to include various types of special syntax in your app-published text. What we didn't mention is that you _can_ just include the same text that a user would post directly in Slack to achieve some of these things. For example, given the following text:

```
<http://example.com|example link> http://example.com #general @here 🤩 :smile:
```

Most of these references can be automatically parsed upon publishing to turn them into links or mentions:

```
<http://example.com|example link> <http://example.com> <#C0838UC2D|general> <!here> :star-struck: :smile:
```

You can achieve this in different ways, depending on where the text is being placed:

*   For text in [layout blocks](/messaging#complex_layouts), set a `verbatim` attribute of your [text objects](/reference/block-kit/composition-objects/text-object) to `false`. This is the default method of processing these text objects.
*   For the top-level `text` field, or text in [secondary message attachments](#attachments), include a `link_names` argument with value of `1` when publishing the message; refer to the [reference docs for the relevant publishing method](/messaging/sending-and-scheduling-messages#publishing) for more information.

#### Disabling automatic parsing {#disabling-automatic-parsing}

If you want to disable automatic parsing, you have a couple options depending on the type of text:

*   For text in [layout blocks](/messaging#complex_layouts) set a `verbatim` attribute of your [text objects](/reference/block-kit/composition-objects/text-object) to `true`.
*   For the top-level `text` field, or text in [secondary message attachments](#attachments), as long as you exclude the `link_names` argument when publishing, this will be disabled by default. [Regular URLs](#linking-urls) will still be converted into clickable links; however, to disable this, you can pass the `parse` argument with a value of `none` when publishing.

#### Why you should consider disabling automatic parsing {#why-you-should-consider-disabling-automatic-parsing}

Even with this functionality available, we still recommend that you use the manual methods shown [above](#advanced). This is important because the names of conversations or user groups may change at any time. What was previously a functioning reference may no longer work. Meanwhile, an ID will always remain the same. The same holds true for [special mentions](#special-mentions), such as `@here`.

Another good reason to disable automatic parsing is to be more explicit about where you want to include links and mentions. This could prevent random text from being unintentionally parsed and turned into a link. For example, imagine your app passes user input from a third-party service straight into the published text. Using automatic parsing, if this user text contained a string like `@everyone`, your app could unintentionally send a notification to the entire workspace.

We've since [deprecated this functionality for user mentions](/changelog/2017-09-the-one-about-usernames), so always parsing manually will keep you prepared in case automatic parsing is deprecated for other entities in the future, such as conversations or user groups.

## Creating rich message layouts {#rich-layouts}

We can take message formatting a step further by making [rich message layouts](/reference/block-kit/blocks/rich-text-block) using Block Kit, which enables us to structure complex data in a readable and understandable way within messages.

While message text formatting can improve information density and visual hierarchy at a basic level, you can combine that with [Block Kit](/block-kit) **layout blocks** and **block elements** to vastly expand the possibilities for visual organization.

You can create messages using blocks and introduce the tools for building a compelling visual experience. Stack individual blocks together into an array that defines the visual layout and style of your messages. Check out the [formatting with rich text tutorial](/block-kit/formatting-with-rich-text) for more details.

### Defining a single block {#define_block}

Each block is represented in our APIs as a JSON object. Here's an example of a [`section`](/reference/block-kit/blocks/section-block) block:

```
{  "type": "section",  "text": {    "type": "mrkdwn",    "text": "New Paid Time Off request from <example.com|Fred Enriquez>\n\n<https://example.com|View request>"  }}
```

[View in Block Kit Builder](https://api.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22New%20Paid%20Time%20Off%20request%20from%20%3Cexample.com%7CFred%20Enriquez%3E%5Cn%5Cn%3Chttps://example.com%7CView%20request%3E%22%7D%7D%5D%7D)

Every block contains a `type` field, specifying which of the [available blocks](/reference/block-kit/blocks) to use, along with other fields that describe the content of the block.

### Stacking multiple blocks {#stack_of_blocks}

Individual blocks can be stacked together to create complex visual layouts. When you've chosen each of the blocks you want in your layout, place each of them in an array, in visual order, as follows:

```
[  {    "type": "header",    "text": {      "type": "plain_text",      "text": "New request"      }  },  {    "type": "section",    "fields": [      {        "type": "mrkdwn",        "text": "*Type:*\nPaid Time Off"      },      {        "type": "mrkdwn",        "text": "*Created by:*\n<example.com|Fred Enriquez>"      }    ]  },  {    "type": "section",    "fields": [      {        "type": "mrkdwn",        "text": "*When:*\nAug 10 - Aug 13"      }    ]  },  {    "type": "section",    "text": {      "type": "mrkdwn",      "text": "<https://example.com|View request>"    }  }]
```

[View in Block Kit Builder](https://api.slack.com/block-kit-builder/#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22New%20request%22,%22emoji%22:true%7D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type:*%5CnPaid%20Time%20Off%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Created%20by:*%5Cn%3Cexample.com%7CFred%20Enriquez%3E%22%7D%5D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*When:*%5CnAug%2010%20-%20Aug%2013%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Type:*%5CnPaid%20time%20off%22%7D%5D%7D,%7B%22type%22:%22section%22,%22fields%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Hours:*%5Cn16.0%20\(2%20days\)%22%7D,%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Remaining%20balance:*%5Cn32.0%20hours%20\(4%20days\)%22%7D%5D%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22%3Chttps://example.com%7CView%20request%3E%22%7D%7D%5D%7D)

[Block Kit Builder](https://api.slack.com/tools/block-kit-builder) allows you to drag, drop, and rearrange blocks to design and preview Block Kit layouts. Alternatively, you can use the reference guide on [blocks](/reference/block-kit/blocks) to manually generate a complete `blocks` array, like the one shown above.

### Adding your blocks array {#add_blocks_array}

Blocks are added to messages by adding a `blocks` array to [the message payload](/messaging#payloads) as follows:

```
{  "channel": "C123ABC456",  "text": "New Paid Time Off request from Fred Enriquez",  "blocks": [    {      "type": "header",      "text": {        "type": "plain_text",        "text": "New request"      }    },    {      "type": "section",      "fields": [        {          "type": "mrkdwn",          "text": "*Type:*\nPaid Time Off"        },        {          "type": "mrkdwn",          "text": "*Created by:*\n<example.com|Fred Enriquez>"        }      ]    },    {      "type": "section",      "fields": [        {          "type": "mrkdwn",          "text": "*When:*\nAug 10 - Aug 13"        }      ]    },    {      "type": "section",      "text": {        "type": "mrkdwn",        "text": "<https://example.com|View request>"      }    }  ]}
```

When you're using `blocks` in your message payload, the top-level `text` field becomes a fallback message displayed in notifications. Blocks should define everything else about the desired visible message.

### Sending messages with blocks {#sending-messages}

There are [multiple ways for apps to send messages](/messaging#sending_methods), and you can use Block Kit with most of them. Here's a list of the methods you can use to publish messages with blocks:

*   [Incoming webhooks](/messaging/sending-messages-using-incoming-webhooks).
*   The [`chat.postMessage`](/reference/methods/chat.postMessage) and [`chat.postEphemeral`](/reference/methods/chat.postEphemeral) API methods.
*   In response to [slash commands](/interactivity/implementing-slash-commands).
*   In response to [message actions](/interactivity/implementing-shortcuts).
*   When creating Slack app-based [URL unfurls](/messaging/unfurling-links-in-messages#slack_app_unfurling).

There are no special OAuth scopes needed to publish blocks beyond those already specified within the methods above.

Read our [guide to sending messages](/messaging/sending-and-scheduling-messages) for more details. Once you've decided which sending method to use, consult that method's reference guide to find out where to include your JSON payload. When you call your selected method, your stack of blocks will transform into a beautiful new message, like this:

![Message with blocks showing a review of a hotel with 1 stars given](/assets/images/message_blocks_getting_started-d14906a412120ca80605c6924f87fdb7.png)

[View in Block Kit Builder](https://api.slack.com/tools/block-kit-builder?blocks=%5B%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22Danny%20Torrence%20left%20the%20following%20review%20for%20your%20property%3A%22%0A%09%09%7D%0A%09%7D%2C%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22block_id%22%3A%20%22section567%22%2C%0A%09%09%22text%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%22text%22%3A%20%22%3Chttps%3A%2F%2Fexample.com%7COverlook%20Hotel%3E%20%5Cn%20%3Astar%3A%20%5Cn%20Doors%20had%20too%20many%20axe%20holes%2C%20guest%20in%20room%20237%20was%20far%20too%20rowdy%2C%20whole%20place%20felt%20stuck%20in%20the%201920s.%22%0A%09%09%7D%2C%0A%09%09%22accessory%22%3A%20%7B%0A%09%09%09%22type%22%3A%20%22image%22%2C%0A%09%09%09%22image_url%22%3A%20%22https%3A%2F%2Fis5-ssl.mzstatic.com%2Fimage%2Fthumb%2FPurple3%2Fv4%2Fd3%2F72%2F5c%2Fd3725c8f-c642-5d69-1904-aa36e4297885%2Fsource%2F256x256bb.jpg%22%2C%0A%09%09%09%22alt_text%22%3A%20%22Haunted%20hotel%20image%22%0A%09%09%7D%0A%09%7D%2C%0A%09%7B%0A%09%09%22type%22%3A%20%22section%22%2C%0A%09%09%22block_id%22%3A%20%22section789%22%2C%0A%09%09%22fields%22%3A%20%5B%0A%09%09%09%7B%0A%09%09%09%09%22type%22%3A%20%22mrkdwn%22%2C%0A%09%09%09%09%22text%22%3A%20%22*Average%20Rating*%5Cn1.0%22%0A%09%09%09%7D%0A%09%09%5D%0A%09%7D%0A%5D)

## Notes on retrieving formatted messages {#retrieving-messages}

If you're [retrieving messages](/messaging/retrieving-messages), we've included some extra details in the sections above to help you parse the formatting syntax. This will allow you to properly format it for display on different services, or help your app fully understand the intent of a message. Here are the general steps involved in detecting advanced formatting syntax:

1.  Detect all sub-strings matching `<(.*?)>`.
2.  Within those sub-strings, format content starting with `#C` as a [channel link](#linking-channels).
3.  Format content starting with `@U` or `@W` as a [user mention](#mentioning-users).
4.  Format content starting with `!subteam` as a [user group mention](#mentioning-groups).
5.  Format content starting with `!` according to the rules for [special mentions](#special-mentions).
6.  For any other content within those sub-strings, format as a [URL link](#linking-urls).

## Disabling formatting {#disabling-formatting}

If you want to turn Slack's markdown-like processing off, you have different options depending on where the text is:

*   For text in [layout blocks](/messaging#complex_layouts) set the `type` of your [text objects](/reference/block-kit/composition-objects/text-object) to `plain_text`.
*   For the top-level `text` field in messages, include a `mrkdwn` property set to `false` when publishing.
*   For text in [secondary message attachments](#attachments), exclude the relevant field from the [`mrkdwn_in` attribute](/legacy/legacy-messaging/legacy-secondary-message-attachments).

## Legacy: secondary attachments {#attachments}

This feature is a legacy part of messaging functionality for Slack apps. You can read more about them [here](/legacy/legacy-messaging/legacy-secondary-message-attachments/).

## Next steps {#next-steps}

Congratulations! You've learned all about the message composition options available to Slack apps.

✨ **To learn about all the available blocks**, head to the reference guide for [blocks](/reference/block-kit/blocks).

✨ **To learn about Block Kit elements**, head to the reference guide for [block elements](/reference/block-kit/block-elements).

✨ **To learn about formatting and unfurling links in messages**, check out [unfurling links in messages](/messaging/unfurling-links-in-messages).