Source: https://docs.slack.dev/surfaces/canvases

# Canvases

Canvases are simple but powerful documents built into Slack. Canvases can either exist attached to a channel or all on their own. Here are some uses for canvases to inspire you:

✨ Use a channel canvas in a feedback channel to instruct users how to submit feedback in a desired format or denote certain urgency.

✨ Welcome new team members with an onboarding canvas filled with tasks, team resources, and user references of their fellow comrades.

✨ Create a canvas in connection with an incident to gather all pertinent information in one place.

Canvases can be added to Slack apps via the [Slack API](/reference/methods?query=canvas) or with a [built-in function](/tools/deno-slack-sdk/guides/creating-slack-functions) in an app created with the Deno Slack SDK. How you format canvas content depends on how you are interacting with it. Note that currently, Block Kit is not supported in canvases.

## Formatting canvas content with the Slack API {#api}

When [creating](/reference/methods/canvases.create) or [editing](/reference/methods/canvases.edit) a canvas with the API, you will encounter a `document_content` object, which contains two properties of its own: `type`, and `markdown`. Currently, the only supported `type` is `markdown`.

The `document_content` object supports the following [markdown](https://markdownguide.offshoot.io/basic-syntax/) elements:

*   bold
*   bulleted lists
*   [checklist](https://markdownguide.offshoot.io/extended-syntax/#task-lists)
*   canvas unfurl
*   [code block](https://markdownguide.offshoot.io/extended-syntax/#fenced-code-blocks)
*   code span
*   divider (horizontal rule)
*   [emojis](https://markdownguide.offshoot.io/extended-syntax/#emoji)—standard and custom
*   file unfurls
*   hard line break
*   headings h1-h3
*   italic
*   link (in line)
*   link reference
*   markdown table
*   message unfurl
*   ordered lists
*   paragraph
*   profile unfurl
*   quote block
*   [strikethrough](https://markdownguide.offshoot.io/extended-syntax/#strikethrough)
*   website unfurl
*   @ mentions for users and channels

### Markdown formatting {#markdown-formatting}

Markdown formatting varies slightly for standard elements, like headers and quotes, and Slack-specific elements, like user and channel mentions.

For guidance on markdown formatting for standard elements, refer to [this markdown guide](https://markdownguide.offshoot.io/basic-syntax/) and our internal documentation [Formatting text for surfaces](/messaging/formatting-message-text).

For Slack-specific elements, the markdown syntax for canvases is a bit different. For example, a channel mention, where the channel ID is `C123ABC456`:

```
Why not join ![](#C123ABC456)
```

And a user mention, where the user ID is `U123ABCDEFG`:

```
![](@U123ABCDEFG)
```

In both of these cases, the link will automatically be converted to show the channel name or user card, respectively. If any of the channel members do not have access to the linked channel, they will see an unclickable `private channel` label.

Below are some more examples of these Slack-specific elements in action.

#### Formatting markdown tables in canvases {#tables}

Markdown tables are supported in canvases. Providing the following markdown:

```
|Header|Header2||---|---||content1|content2|
```

will be parsed and inserted into the canvas as the following:

Header

Header2

content1

content2

Canvas tables have a limit of 300 cells per table; this may be any number of rows or columns that add up to that limit.

In addition to plain text, markdown tables in canvases also support:

*   Canvas links
*   Checkboxes
*   Links
*   Lists (ordered and unordered)
*   Mentions
*   Text styles like bold, italic, strikethrough, and code
*   Unfurls

See how these are implemented in the example below.

**Example 1**

Here is what the markdown and request would look like to create a markdown table with the [`canvases.create`](/reference/methods/canvases.create) API method.

The markdown:

```
|Header|Header2||---|---||content1|content2|
```

The request input:

```
{    "title": "The Best Canvas",    "document_content": {        "type": "markdown",        "markdown": "|Header|Header2|\n|--|--|\n|content1|content2|"    }}
```

The request output:

```
{    "ok": true,    "canvas_id": "1234ABCDEF"}
```

**Example 2**

Here is a more robust example of the additional fields supported in markdown tables.

The markdown:

```
| Feature | Content || ------- | ------- || Canvas | ![](https://devrelsandbox.slack.com/docs/T038J6TH5PF/F080JDE025R) || Checkboxes | Tasks:<br>- [ ] **Incomplete** task go to [Task List](http://www.your-special-url.com)<br>- [x] *Completed* task in  ![](https://www.slack.com/archives/C01234567) || Link | [Slack Home](http://docs.slack.dev) || List (ordered) | Steps:<br>1. First step<br>2. Second step<br>3. Third step || List (unordered) | Items:<br>- Apple<br>- Banana<br>- Orange || Mentions | User: ![](https://devrelsandbox.slack.com/team/U045A5X302V) Channel: ![](https://devrelsandbox.slack.com/archives/C038M39A2TV) || Text Styles | **Bold text** and *italic text* and ~~strikethrough~~ and `code snippet` || Unfurl | ![](https://devrelsandbox.slack.com/archives/C0386FU7SMD) |
```

The request input:

```
{    "title": "The Best Canvas",    "document_content": {        "type": "markdown",        "markdown": "| Feature | Content |\n| ------- | ------- |\n| Canvas | ![](https://devrelsandbox.slack.com/docs/T038J6TH5PF/F080JDE025R) |\n| Checkboxes | Tasks:<br>- [ ] **Incomplete** task go to [Task List](http://www.your-special-url.com)<br>- [x] *Completed* task in  ![](https://www.slack.com/archives/C01234567) |\n| Link | [Slack Home](http://docs.slack.dev) |\n| List (ordered) | Steps:<br>1. First step<br>2. Second step<br>3. Third step |\n| List (unordered) | Items:<br>- Apple<br>- Banana<br>- Orange |\n| Mentions | User: ![](https://devrelsandbox.slack.com/team/U045A5X302V) Channel: ![](https://devrelsandbox.slack.com/archives/C038M39A2TV) |\n| Text Styles | **Bold text** and *italic text* and ~~strikethrough~~ and `code snippet` |\n| Unfurl | ![](https://devrelsandbox.slack.com/archives/C0386FU7SMD) |"    }}
```

The request output:

```
{    "ok": true,    "canvas_id": "1234ABCDEF"}
```

To yield a canvas with the following content:

![](/assets/images/canvas_markdown_table-36a7c0eec53a7fce1cb5c7cb467e5cb3.png)

### Project canvas example {#project-canvas}

Given the example request of this code:

```
POST https://slack.com/api/conversations.canvases.createRequest{ "channel_id": "C07317JTXCP", "document_content":  { "type":"markdown", "markdown":"# Headers\n# Status\n:large_green_circle: On Track\n# Goal\nThe channel to coordinate the build, testing, and launch of Platypus\n# :people_hugging:Stakeholders\n![](@U071CCRCVFH)\n\n![](@UQSSGHV0Q)\n# :books:Resources\n* Project Plan\n* Google Drive\n# :slack:Related channels\n* ![](#C073UAJRW4R) - Project Channel\n* ![](#C073UAJRW4R) - GTM Channel"}}
```

Here's the same content in a more human-readable format:

```
 # Headers  # Status  :large_green_circle: On Track  # Goal  The channel to coordinate the build, testing, and launch of Platypus  # :people_hugging:Stakeholders  ![](@U071CCRCVFH)  ![](@UQSSGHV0Q)  # :books:Resources  * Project Plan  * Google Drive  # :slack:Related channels  * ![](#C073UAJRW4R) - Project Channel  * ![](#C073UAJRW4R) - GTM Channel
```

The output canvas would look like the channel canvas in this image: ![Project canvas example](/assets/images/project_canvas_example-b225297b318a0e0d2be4e98c60747173.png)

#### Unfurl behavior {#unfurl}

Some objects, like user references, support both "card" and "title" unfurls. This unfurling behavior is contextual. To be unfurled as a "card" (like the image above for this example), the reference needs to be in its own syntax block. If the reference is is a child of another syntax block, the unfurl will be a "title" style. In this example, the double spacing around the users (the `\n\n` part) ensures the user mentions unfurl as a card.

#### Referencing an image {#image}

When referencing an image in the `document_content` field, you can pass a publicly-hosted image URL.

Alternatively, to reference an image that is already hosted in Slack, pass the image permalink for the URL value.

If the image hasn’t been uploaded already, you’ll first need to upload it. Instructions to do so can be found in [Uploading files](/messaging/working-with-files#uploading_files) in the files documentation. Once completed, you can use the returned file ID with the [`files.info`](/reference/methods/files.info) endpoint to find the image permalink.

For which permalink to use, refer to [Permalinks](/reference/objects/file-object#permalinks) in the file object documentation.

Once you have the permalink, pass the value to your canvas like this:

```
POST https://slack.com/api/canvases.editRequest{ "canvas_id": "F072RA30WRL", "changes": [{ "operation": "insert_after", "document_content": { "type":"markdown", "markdown":"![graph](https://your_workspace_URL.slack.com/files/U071SRU8BA7/F073FVDABQS/image.png)" }, "section_id": "temp:C:YKV9b3fab0f992e4080ae952deca" }]}
```

Let's look at another example of this in a weekly newsletter example.

### Weekly newsletter example {#weekly-newsletter}

To create a weekly newsletter canvas for your team, it could look something like this:

```
POST https://slack.com/api/canvases.createRequest{ "title": "Weekly Newsletter for May 2", "document_content": { "type":"markdown","markdown":"Welcome to the latest edition of our weekly newsletter! We're thrilled to share with you some exciting updates and news from our organization.\n ## :chart-green: Weekly Targets\n ![graph](https://your_workspace_URL.slack.com/files/UQSSGHV0Q/F071Q447X6Z/image__1_.png)\n ## :tada: Latest News\n* :act-app: Just a few days left to complete our FY25 Corporate Message Certification! Block 30 minutes on your calendar, head to Astro’s Course Tracker, and align on our corporate strategy and message. :lets-go:\n* :sales-elevate-wow: We relaunched Slack Sales Elevate at World Tour New York, with new features including deal insight notifications, deal filters, and Slack AI, to help sales leaders stay informed, take action, and guide their teams to close deals faster. :amaze:\n* :love: ![](@U071CCRCVFH) wished our wonderful Executive Assistants a happy Administrative Professionals Day, where we saw lots of love in thread for our amazing EA crew!\n* :party-parrot: ![](@UQSSGHV0Q) recapped a busy trip to London and Amsterdam, highlighting meetings with customers like Aperture Science and Black Mesa!\n\n ## 📅 Upcoming Events\n* May 1: Hear from the VP of Sales on how to create culture 😀\n* May 18: Women at Acme Happy Hour at The Book Bar 🍷\n* May 15: Sign up for our monthly lightning networking event ⚡️\n\nNot part of our calendar group? Add yourself to receive invites" }}
```

Here is the same content in a more human-readable format:

```
Welcome to the latest edition of our weekly newsletter! We're thrilled to share with you some exciting updates and news from our organization. ## :chart_green: Weekly Targets![graph](https://your_workspace_URL.slack.com/files/UQSSGHV0Q/F071Q447X6Z/image__1_.png)## :tada: Latest News* :act-app: Just a few days left to complete our FY25 Corporate Message Certification! Block 30 minutes on your calendar, head to Astro’s Course Tracker, and align on our corporate strategy and message. :lets-go:* :sales-elevate-wow: We relaunched Slack Sales Elevate at World Tour New York, with new features including deal insight notifications, deal filters, and Slack AI, to help sales leaders stay informed, take action, and guide their teams to close deals faster. :amaze:* :love: ![](@U071CCRCVFH) wished our wonderful Executive Assistants a happy Administrative Professionals Day, where we saw lots of love in thread for our amazing EA crew!* :party-parrot: ![](@UQSSGHV0Q) recapped a busy trip to London and Amsterdam, highlighting meetings with customers like Aperture Science and Black Mesa! ## 📅 Upcoming Events* May 1: Hear from the VP of Sales on how to create culture 😀* May 18: Women at Acme Happy Hour at The Book Bar 🍷* May 15: Sign up for our monthly lightning networking event ⚡️Not part of our calendar group? Add yourself to receive invites
```

This example request would yield this canvas as a result:

![Newsletter example](/assets/images/newsletter_example-d47896fa9475e92b0358ee9cb2f40525.png)

## Formatting canvas content with a built-in Slack function {#builtin}

Formatting canvas content within an app created with the Deno Slack SDK is different. If you are [creating](/tools/deno-slack-sdk/reference/slack-functions/canvas_create) or [updating](/tools/deno-slack-sdk/reference/slack-functions/canvas_update_content) a canvas with the built-in Slack methods, you will encounter a `content` input parameter that is an expanded rich text object. Refer to the automation types page for an example of [`expanded_rich_text`](/tools/deno-slack-sdk/guides/utilizing-slack-and-custom-data-types#expandedrichtext) and all of its sub-elements.

## Finding canvases with files.list {#search_canvas}

To programmatically look up a list of canvases, use the [`files.list`](/reference/methods/files.list) method while filtering for the `canvas` type. Your query may look something like this `https://slack.com/api/files.list?types=canvas`.