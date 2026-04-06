Source: https://docs.slack.dev/block-kit/designing-with-block-kit

# Designing with Block Kit

It's important to consider accessibility when designing your app.

Accessibility in your apps means ensuring users with disabilities can understand, navigate, and interact with them effectively. And it benefits everyone! Consider that everyone at some point in life will experience a disability, whether it be permanent, temporary, or situational (think "I sat on my glasses and can't quite see today"). Building your apps in an accessible way will make the world a better place.

Here are our tips and recommendations for how to make your apps accessible when using Block Kit to compose [your app's surfaces](/surfaces).

## Keep content clear and concise {#content}

Here are some general guidelines for content in Slack apps.

Do:

*   Use short, clear sentences and paragraphs.
*   Explain abbreviations.

Don't:

*   Use jargon, buzzwords, idioms, and slang; be fun but don't alienate anyone.
*   Use directional and sensory language, including emojis. For example, do not use an arrow to refer to a prior message.

## Use color carefully {#color}

There are two main rules around the use of color:

*   **Use more than just color to convey meaning**. Color can enhance and reinforce meaning, but it should not be the only way to convey meaning. Say, for instance, you'd like to have a button to cancel a subscription. A red button that says "cancel" would not be sufficient because "cancel" is used in many contexts that are not a severe action. Instead, the button should read "cancel subscription" to fully convey the meaning of the action.
    
*   **Provide sufficient contrast for text and important visual indicators**. The ideal contrast ratio is 4.5:1 for regular text, though we at Slack mostly control this so you don't need to worry about it. However, it's always a good idea to test your apps in both light and dark mode to ensure usability in both.
    

## Simplify with pictures {#pictures}

Sometimes faces can be better than names, or maps better than addresses. Sprinkle [image elements](/reference/block-kit/block-elements/image-element) into blocks to remove some of that text.

This message is okay:

![App message featuring a text list of tagged users](/assets/images/dg_pictures_bad-fa70230e15de83b838d5b7e31f527f55.png)

But this version is easier to parse, without losing any vital information:

![App message featuring the tagged users as profile photos instead of text](/assets/images/dg_pictures_good-b6978e87ef758932626681e8cdb8c71f.png)

The example above is using a [context block](/reference/block-kit/blocks/context-block), which is great for storing helpful information that isn’t primary content. [Context blocks](/reference/block-kit/blocks/context-block) can store text, images, and emoji.

## Use interactivity to reduce complexity {#complexity}

Use [interactive components](/block-kit#making-things-interactive) to break workflows into steps, and only show what’s needed for the current step. Let interaction choices reveal further information or options only when they’re necessary.

For example, this calendar app has a lot of information and interactive options to display:

![Calendar app message featuring lots of text and interactive options](/assets/images/dg_complex_bad-5ecefd1202d09f60e615f7fe57dc1f27.png)

But it could achieve the same functionality by keeping advanced options tucked away until they're needed. Here's the same app using [context blocks](/reference/block-kit/blocks/context-block) to better organize info, and [an overflow menu](/reference/block-kit/block-elements/overflow-menu-element) to store lesser-used options:

![Calendar app message where options have been hidden behind interactivity, and other elements turned visual](/assets/images/dg_complex_good-8ba29853abc0c644cfa561037145c614.png)

By streamlining the default interactivity, you're helping your users intuit the most important action to take on the message.

## Choose sensible default options {#defaults}

Save people work wherever you can by minimizing the choices they have to make. When you give [select menus](/reference/block-kit/block-elements/select-menu-element) and [buttons](/reference/block-kit/block-elements/button-element) good default values, you decrease the number of choices they have to make from many to one - yes or no.

![Coffee ordering app message showing previous order and asking whether to reorder it with yes or no buttons](/assets/images/dg_defaults-da5518f0eafd914f403b0f8d7b42c227.png)

Say your app helps people buy coffee. Instead of presenting a full menu of choices every time someone orders, you could make the user’s last order the default option. In the best case scenario, this reduces the coffee order to a single click.

## Cleaning up after your app {#cleanup}

[Visually rich messages](/messaging) are great in the moment you receive them: they’re nice to read and understandable to interact with. They also take up a lot of space on a person’s screen:

![Lunch group app message showing text and a couple of buttons](/assets/images/dg_cleanup_before-3d4dc21b9b93b9f72814409ae8902bf8.png)

Think about what a person will need to remember about their interaction with your app when they come back to it later, at the end of the message’s life—or after an exchange of several messages. Do those buttons and menus need to stick around, or can you condense the message down to a short text record of what happened?

Be considerate and update your message after the interactive flow or the conversation expires:

![Lunch group app message after cleanup, with the buttons gone](/assets/images/dg_cleanup_after-4da6ada3ce3fe4e0d287a44d6750d7d2.png)

Read our guide to [updating messages](/messaging/modifying-messages#updating) to see how you can cleanup after your app has done some work.

## Screen reader considerations {#screen-reader}

A screen reader is a tool used that helps people who have difficulties seeing with accessing and interacting with digital content. There are several considerations to keep in mind to most effectively work with a screen reader, including emoji use, images, and interactive elements.

### Emoji use 😄 {#emoji-use}

Emojis are tied to text aliases, which display on hover and when emojis are turned off. Text aliases also act as the accessible name for the emoji. A screen reader user will hear “\[alias\] emoji” when they read an emoji. There is no way to indicate that an emoji is decorative or add an ARIA (Accessible Rich Internet Applications) label to an emoji to describe it better. Also, organizations and end users have the ability to turn off emojis and default to the alias as plain text. Knowing this, here are some tips:

*   **Do not use an emoji as a control**. Do not use them for field labels or inline help, in a button, or to trigger a workflow. Always pair emojis with text.
*   **Always the grand finale**. Ideal emoji placement is at the end of a sentence or line; this improves readability.
*   **Just a sprinkle**. Use emojis sparingly in headers and append them to the end. We recommend using emojis either in the header or the subtext, but not both.
*   **Emojis are not word replacements**. Ensure they are paired with relevant text.
*   **Avoid using emojis as bullet points**. You can talk about them in bulleted lists, just don't make them the bullets themselves.

### Images {#images}

Guidelines regarding images in Slack apps are:

*   **Describe your images**. Provide clear, context-specific `alt_text` for all images, and if appropriate, a `title` too.
*   **Save the gallery wall for your stairway**. Limit the number of redundant and purely decorative images in your apps. Because each image requires `alt_text`, and each will be read by a screen reader, the experience could get messy with too many extraneous images.

### Animations {#animations}

Keep in mind that users can turn off animated gifs and emojis in their Slack accessibility preferences, so for every informational animation you have, ensure its meaning is conveyed even when paused. Either the freeze frame or the animation's surrounding text should capture the main point. Like images, always include descriptive `alt_text`.

Don't cause seizures

Do not add more than three large flashes per second in animations. This is a WCAG (Web Content Accessibility Guidelines) standard.

### Charts {#charts}

Every chart that an app visually displays needs an accompanying accessible PDF. Include:

*   An image block containing a chart screenshot with brief `alt_text`, e.g. “chart preview”.
*   A button allowing the user to download the chart as an accessible PDF.
*   An accessible PDF in PDF/UA format containing a properly-tagged table version of the data displayed visually in the chart screenshot.

### Interactive elements {#interactive-elements}

#### Input fields {#input-fields}

Do:

*   Wrap inputs in input blocks.
*   Be a good host and provide associated labels for all inputs fields, so all users are clear on what information to enter where.
*   Use descriptive placeholder text for selects.

Don't:

*   Wrap inputs in section or action blocks.
*   Use emojis in input labels.

#### Repetitive controls in lists {#controls}

To ensure the best experience for your users, we recommend you:

*   Give buttons brief, repetitive labels to avoid truncation.
*   Make placeholder text for inputs record-specific where possible.

If you get a little wordy with your button and/or placeholder text such that Block Kit truncates the text, know that a screen reader will still read the entire placeholder text, but the button text will be cut off, so prioritize brevity on those buttons!