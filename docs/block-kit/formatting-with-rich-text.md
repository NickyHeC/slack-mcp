Source: https://docs.slack.dev/block-kit/formatting-with-rich-text

# Formatting with rich text

Wow, what a beautifully constructed message! Wouldn’t it be great to create a bot to keep your new hires informed of what they should be doing in their first days with the company, in a clear, organized message sent directly to them? Yes, the answer is yes, it would be great.

In this tutorial, we’ll walk through how to structure the [Block Kit](/block-kit) blocks to achieve this message, while explaining the ins and outs of rich text. To learn how to incorporate these blocks in messages and modals, read up on [Building with Block Kit](/block-kit).

![Rich text example](/assets/images/rich_text_example-ff9c3f9bb7bcd2c6a02fa9d6ce6031eb.png)

If you’d like to follow along with the code already constructed, you can check it out [here](https://app.slack.com/block-kit-builder/T024BE7LD?cdn_fallback=1&force_cold_boot=1#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Onboarding%20Week%201%22%7D%7D,%7B%22type%22:%22context%22,%22elements%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22Hello%20there!%20This%20is%20a%20weekly%20reminder%20of%20what%20you%20should%20be%20doing%20during%20onboarding.%22%7D%5D%7D,%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Welcome%20aboard!*%5Cn%20:eye:%20:lips:%20:eye:%5Cn%5CnHere%20are%20some%20things%20you%20should%20do%20in%20week%201.%5Cn%20Of%20course,%20reach%20out%20to%20your%20manager%20with%20any%20questions.%22%7D,%22accessory%22:%7B%22type%22:%22image%22,%22image_url%22:%22https://media.giphy.com/media/Ae7SI3LoPYj8Q/giphy.gif%22,%22alt_text%22:%22One%20of%20us%22%7D%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22emoji%22,%22name%22:%22office%22%7D,%7B%22type%22:%22text%22,%22text%22:%22%20Company%20business%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Fill%20out%20your%20W-2%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Enroll%20in%20%22%7D,%7B%22type%22:%22link%22,%22text%22:%22benefits%22,%22url%22:%22https://salesforcebenefits.com%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Fill%20out%20your%20Slack%20profile,%20including:%22%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22ordered%22,%22indent%22:1,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Time%20zone%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Pronouns%22%7D%5D%7D%5D%7D%5D%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22emoji%22,%22name%22:%22green_book%22%7D,%7B%22type%22:%22text%22,%22text%22:%22%20Read%20about%20our%20culture%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22link%22,%22text%22:%22Four%20tips%20for%20building%20a%20digital%20first%20culture%22,%22url%22:%22https://slack.com/blog/collaboration/four-tips-build-digital-first-culture%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22link%22,%22text%22:%226%20simple%20ways%20to%20foster%20a%20positive%20hybrid%20work%20environment%22,%22url%22:%22https://slack.com/blog/collaboration/ways-foster-positive-work-environment%22%7D%5D%7D%5D%7D%5D%7D,%7B%22type%22:%22divider%22%7D,%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22emoji%22,%22name%22:%22speech_balloon%22%7D,%7B%22type%22:%22text%22,%22text%22:%22%20Inspirational%20quote%20of%20the%20day%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D,%7B%22type%22:%22rich_text_quote%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Having%20no%20destination%20I%20am%20never%20lost.%20-%20Ikky%C5%AB.%22%7D%5D%7D%5D%7D,%7B%22type%22:%22input%22,%22block_id%22:%22quote_input_block%22,%22element%22:%7B%22type%22:%22plain_text_input%22%7D,%22label%22:%7B%22type%22:%22plain_text%22,%22text%22:%22:envelope:%20Enter%20your%20favorite%20quote,%20to%20be%20shared%20with%20future%20hires%20like%20you:%22,%22emoji%22:true%7D%7D,%7B%22type%22:%22actions%22,%22block_id%22:%22submit_button_action_block%22,%22elements%22:%5B%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Submit%22%7D,%22value%22:%22submit%22,%22action_id%22:%22button_1%22%7D%5D%7D%5D%7D) in Block Kit Builder.

## Mapping an outline {#outline}

Building with Block Kit is layering one block on after another, all independent pieces with their own details within their structure. The main blocks of this message are:

Block Type

Description of block in image

[`header`](/reference/block-kit/blocks/header-block)

Onboarding Week 1

[`context`](/reference/block-kit/blocks/context-block)

Line of text in smaller, lighter font providing context for the message

[`section`](/reference/block-kit/blocks/section-block)

Text and accessory image

[`divider`](/reference/block-kit/blocks/divider-block)

Horizontal line

[`rich_text`](/reference/block-kit/blocks/rich-text-block)

Company business header, bulleted and ordered lists

[`divider`](/reference/block-kit/blocks/divider-block)

Horizontal line

[`rich_text`](/reference/block-kit/blocks/rich-text-block)

Read about our culture header and bullet list

[`divider`](/reference/block-kit/blocks/divider-block)

Horizontal line

[`rich_text`](/reference/block-kit/blocks/rich-text-block)

Inspirational quote of the day section

[`input`](/reference/block-kit/blocks/input-block)

Component for text data collection

[`actions`](/reference/block-kit/blocks/actions-block)

Button

Now let's step through these individually.

## Introducing the content {#introduction}

To give the user context of the overall content of the message, we provide a header, a context sentence, and an introductory blurb.

### Header block {#header-block}

The [header block](/reference/block-kit/blocks/header-block) is straightforward. The only option for the `text` object's `type` field is `plain_text`, so if you wanted to add emoji here, it would need to be in a separate component. We'll explore adding emoji later.

Header code

```
{    "type": "header",    "text": {        "type": "plain_text",        "text": "Onboarding Week 1"    }},
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22header%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Onboarding%20Week%201%22%7D%7D%5D%7D)

### Context block {#context-block}

The [context block](/reference/block-kit/blocks/context-block) is a bit of text that gives the user context for the rest of the message. It is shown in smaller text that is grey instead of black. A context block's `elements` property is an array of objects, either [`image`](/reference/block-kit/block-elements/image-element) or [`text`](/reference/block-kit/composition-objects/text-object). Here we are using `text`. It's important to know that `text` in a context block cannot be rich text, only `mrkdwn` or `plain_text`.

Context code

```
{    "type": "context",    "elements": [        {            "type": "mrkdwn",            "text": "Hello there! This is a weekly reminder of what you should be doing during onboarding."        }    ]},
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22context%22,%22elements%22:%5B%7B%22type%22:%22mrkdwn%22,%22text%22:%22Hello%20there!%20This%20is%20a%20weekly%20reminder%20of%20what%20you%20should%20be%20doing%20during%20onboarding.%22%7D%5D%7D%5D%7D)

### Introductory section block {#section-block}

The [section block](/reference/block-kit/blocks/section-block) provides an introductory blurb with a fun gif welcoming the user to the team. While we strongly encourage rich text to markdown formatting, we've used a `section` block here (which offers _only_ markdown formatting, not rich text) for use the of the accessory image. The same content could be achieved by creating a `rich_text` block followed by an `image` block, but they would be stacked, as opposed to side by side as shown in this example. Also note that we use a link to a gif, and while it is not animated in this screenshot, it will be in a message (and even in the Block Kit Builder preview). After this section, we'll use rich text for formatting text.

Intro section code

```
{    "type": "section",    "text": {        "type": "mrkdwn",        "text": "*Welcome aboard!*\n :eye: :lips: :eye:\n\nHere are some things you should do in week 1.\n Of course, reach out to your manager with any questions."    },    "accessory": {        "type": "image",        "image_url": "https://media.giphy.com/media/Ae7SI3LoPYj8Q/giphy.gif",        "alt_text": "One of us"    }}
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22*Welcome%20aboard!*%5Cn%20:eye:%20:lips:%20:eye:%5Cn%5CnHere%20are%20some%20things%20you%20should%20do%20in%20week%201.%5Cn%20Of%20course,%20reach%20out%20to%20your%20manager%20with%20any%20questions.%22%7D,%22accessory%22:%7B%22type%22:%22image%22,%22image_url%22:%22https://media.giphy.com/media/Ae7SI3LoPYj8Q/giphy.gif%22,%22alt_text%22:%22One%20of%20us%22%7D%7D%5D%7D)

### Divider block {#divider}

The [divider block](/reference/block-kit/blocks/divider-block) is simply a horizontal line to provide a visual break in content.

Divider block code

```
{    "type": "divider"},
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22divider%22%7D%5D%7D)

## The main content {#main-content}

The main content of this message is comprised of a few visual sections: "Company business", "Read about our culture", and "Inspirational quote of the day".

### Company business {#company-business}

The entirety of the "Company business" section of this message is contained within a single [`rich_text`](/reference/block-kit/blocks/rich-text-block) block. The flexibility of formatting is possible through many element types we'll dive into deeper here.

#### Rich text section {#rich-text-section}

Within the top-level [`rich_text`](/reference/block-kit/blocks/rich-text-block) block, we have a [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section), a [`rich_text_list`](/reference/block-kit/blocks/rich-text-block#list), and another [`rich_text_list`](/reference/block-kit/blocks/rich-text-block#list). Think of each [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section) as a single line of text. This may be deceiving, given that it holds an array of elements. However, structuring it as an array of elements provides maximum flexibility with styling each element (which can be as tiny as a single character), as well as ease in parsing. For instance, looking at the [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section), we see two elements: an `emoji` and a `text` element. While these are different elements in the array, they appear on the same line.

The [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section) block allows for elements of the following types, providing many possibilities for styling: `text`, `link`, `emoji`, `user`, `user_group`, and `channel`.

Our text object has a `style` field, in which we specify `bold`. Other style options include `italic`, `strike`, and `code`. You apply them in the same manner as `bold` is shown here.

#### Rich text list {#rich-text-list}

Moving on to the lists, you'll see in the code that we have two lists. One is the bulleted list, containing the first three bullets, and the second is an ordered list containing the last two elements. Notice how the [`rich_text_list`](/reference/block-kit/blocks/rich-text-block#list) is comprised of another `elements` array. This again allows for flexibility in the types of text you want to show, whether that be links, quotes, code snippets, or simply formatted text. To achieve the style of linking one word in a line of plain text, we use a [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section), remembering that each [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section) is read as a single line of text.

To achieve the nested list that is part of the third bullet point, we simply create another [`rich_text_list`](/reference/block-kit/blocks/rich-text-block#list) below the prior one and set the `indent` property to 1. To indent a list further, you keep increasing the number by one to create deeply nested lists.

This section ends with another [divider block](#divider).

Company business code

```
{    "type": "rich_text",    "elements": [        {            "type": "rich_text_section",            "elements": [                {                    "type": "emoji",                    "name": "office"                },                {                    "type": "text",                    "text": " Company business",                    "style": {                        "bold": true                    }                }            ]        },        {            "type": "rich_text_list",            "style": "bullet",            "elements": [                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "text",                            "text": "Fill out your W-2"                        }                    ]                },                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "text",                            "text": "Enroll in "                        },                        {                            "type": "link",                            "text": "benefits",                            "url": "https://salesforcebenefits.com"                        }                    ]                },                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "text",                            "text": "Fill out your Slack profile, including:"                        }                    ]                }            ]        },        {            "type": "rich_text_list",            "style": "ordered",            "indent": 1,            "elements": [                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "text",                            "text": "Time zone"                        }                    ]                },                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "text",                            "text": "Pronouns"                        }                    ]                }            ]        }    ]},
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22emoji%22,%22name%22:%22office%22%7D,%7B%22type%22:%22text%22,%22text%22:%22%20Company%20business%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Fill%20out%20your%20W-2%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Enroll%20in%20%22%7D,%7B%22type%22:%22link%22,%22text%22:%22benefits%22,%22url%22:%22https://salesforcebenefits.com%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Fill%20out%20your%20Slack%20profile,%20including:%22%7D%5D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22ordered%22,%22indent%22:1,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Time%20zone%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Pronouns%22%7D%5D%7D%5D%7D%5D%7D%5D%7D)

### Read about our culture {#read}

The entirety of the "Read about our culture" section is also contained within a single [`rich_text`](/reference/block-kit/blocks/rich-text-block) block. Let's look at how to format links in a list like the ones shown in this example.

Again within this block we see it is constructed using a [`rich_text_section`](/reference/block-kit/blocks/rich-text-block#section) and a [`rich_text_list`](/reference/block-kit/blocks/rich-text-block#list). Unlike the prior section, we have decided to link the entire text line of the bullet, which can be done using the `text` property of the `link` element, instead of breaking it into multiple `link` and `text` elements.

This section ends with another [divider block](#divider).

Read about our culture code

```
{    "type": "rich_text",    "elements": [        {            "type": "rich_text_section",            "elements": [                {                    "type": "emoji",                    "name": "green_book"                },                {                    "type": "text",                    "text": " Read about our culture",                    "style": {                        "bold": true                    }                }            ]        },        {            "type": "rich_text_list",            "style": "bullet",            "elements": [                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "link",                            "text": "Four tips for building a digital first culture",                            "url": "https://slack.com/blog/collaboration/four-tips-build-digital-first-culture"                        }                    ]                },                {                    "type": "rich_text_section",                    "elements": [                        {                            "type": "link",                            "text": "6 simple ways to foster a positive hybrid work environment",                            "url": "https://slack.com/blog/collaboration/ways-foster-positive-work-environment"                        }                    ]                }            ]        }    ]},
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22emoji%22,%22name%22:%22green_book%22%7D,%7B%22type%22:%22text%22,%22text%22:%22%20Read%20about%20our%20culture%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D,%7B%22type%22:%22rich_text_list%22,%22style%22:%22bullet%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22link%22,%22text%22:%22Four%20tips%20for%20building%20a%20digital%20first%20culture%22,%22url%22:%22https://slack.com/blog/collaboration/four-tips-build-digital-first-culture%22%7D%5D%7D,%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22link%22,%22text%22:%226%20simple%20ways%20to%20foster%20a%20positive%20hybrid%20work%20environment%22,%22url%22:%22https://slack.com/blog/collaboration/ways-foster-positive-work-environment%22%7D%5D%7D%5D%7D%5D%7D%5D%7D)

### Inspirational quote {#inspirational-quote}

While the header and emoji of the last section of content also use the [`rich_text`](/reference/block-kit/blocks/rich-text-block) block, the following rich text element is different: the [`rich_text_quote`](/reference/block-kit/blocks/rich-text-block#quote). Using this element creates the vertical bar to the left of the text that indicates it is a quote, similar to how it is shown in messages in the Slack client or app.

The next piece is an [`input`](/reference/block-kit/blocks/input-block) block, which allows collection of data, in this case, a quote, from the user that can be stored and recalled again at a later date.

The final block is the [`actions`](/reference/block-kit/blocks/actions-block) block, which is the call to action after the user submits their favorite quote — they push the button, letting the app know the action has been completed and the data is submitted. Read more about button function on the [Block elements & interactive components reference page](/reference/block-kit/block-elements/button-element). We've added a `block_id` for both the `input` and `actions` block in order to reference them later. When a `block_id` is not explicitly added for a block, one will be automatically generated.

Inspirational quote code

```
{    "type": "rich_text",    "elements": [        {            "type": "rich_text_section",            "elements": [                {                    "type": "emoji",                    "name": "speech_balloon"                },                {                    "type": "text",                    "text": " Inspirational quote of the day",                    "style": {                        "bold": true                    }                }            ]        },        {            "type": "rich_text_quote",            "elements": [                {                    "type": "text",                    "text": "Having no destination I am never lost. - Ikkyū."                }            ]        }    ]},{    "type": "input",    "block_id": "quote_input_block",    "element": {        "type": "plain_text_input"    },    "label": {        "type": "plain_text",        "text": ":envelope: Enter your favorite quote, to be shared with future hires like you:",        "emoji": true    }},{    "type": "actions",    "block_id": "submit_button_action_block",    "elements": [        {            "type": "button",            "text": {                "type": "plain_text",                "text": "Submit"                },            "value": "submit",            "action_id": "button_1"        }    ]}
```

[View in Block Kit Builder](https://app.slack.com/block-kit-builder/T024BE7LD#%7B%22blocks%22:%5B%7B%22type%22:%22rich_text%22,%22elements%22:%5B%7B%22type%22:%22rich_text_section%22,%22elements%22:%5B%7B%22type%22:%22emoji%22,%22name%22:%22speech_balloon%22%7D,%7B%22type%22:%22text%22,%22text%22:%22%20Inspirational%20quote%20of%20the%20day%22,%22style%22:%7B%22bold%22:true%7D%7D%5D%7D,%7B%22type%22:%22rich_text_quote%22,%22elements%22:%5B%7B%22type%22:%22text%22,%22text%22:%22Having%20no%20destination%20I%20am%20never%20lost.%20-%20Ikky%C5%AB.%22%7D%5D%7D%5D%7D,%7B%22type%22:%22input%22,%22block_id%22:%22quote_input_block%22,%22element%22:%7B%22type%22:%22plain_text_input%22%7D,%22label%22:%7B%22type%22:%22plain_text%22,%22text%22:%22:envelope:%20Enter%20your%20favorite%20quote,%20to%20be%20shared%20with%20future%20hires%20like%20you:%22,%22emoji%22:true%7D%7D,%7B%22type%22:%22actions%22,%22block_id%22:%22submit_button_action_block%22,%22elements%22:%5B%7B%22type%22:%22button%22,%22text%22:%7B%22type%22:%22plain_text%22,%22text%22:%22Submit%22%7D,%22value%22:%22submit%22,%22action_id%22:%22button_1%22%7D%5D%7D%5D%7D)

## Summary {#summary}

This concludes our guide on how to construct a beautiful message with Block Kit! We hope you will continue to explore all that blocks have to offer in [Block Kit Builder](https://app.slack.com/block-kit-builder) and by reviewing the material below.

### Further reading {#further-reading}

Check out these articles to expand your knowledge and skills of Block Kit:

➡️ [Building with Block Kit](/block-kit)

➡️ [Designing with Block Kit](/block-kit/designing-with-block-kit)

➡️ [Block Kit reference](/reference/block-kit)

### Slack developer tools helper {#dev-tools}

Another tool to help you in your rich text journey is the [Slack Developer Tools Inspect tool](https://sdt.builtbyslack.com/). Once installed, you can click the kebab (or three dots) menu on the upper-right of any message in Slack, then click "more message shortcuts." Search for the Inspect tool and click on it. This tool shows you the `json` behind any given message in Slack, which helps you understand how blocks are used to construct them. Magic. ✨