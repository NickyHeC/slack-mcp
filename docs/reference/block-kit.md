Source: https://docs.slack.dev/reference/block-kit

# Reference: Block Kit

## Blocks

| Name | Description |
|------|-------------|
| [Actions](https://docs.slack.dev/reference/block-kit/blocks/actions-block.md) | Holds multiple interactive elements. |
| [Context](https://docs.slack.dev/reference/block-kit/blocks/context-block.md) | Provides contextual info, which can include both images and text. |
| [Context actions](https://docs.slack.dev/reference/block-kit/blocks/context-actions-block.md) | Displays actions as contextual info, which can include both feedback buttons and icon buttons. |
| [Divider](https://docs.slack.dev/reference/block-kit/blocks/divider-block.md) | Visually separates pieces of info inside of a message. |
| [File](https://docs.slack.dev/reference/block-kit/blocks/file-block.md) | Displays info about remote files. |
| [Header](https://docs.slack.dev/reference/block-kit/blocks/header-block.md) | Displays a larger-sized text. |
| [Image](https://docs.slack.dev/reference/block-kit/blocks/image-block.md) | Displays an image. |
| [Input](https://docs.slack.dev/reference/block-kit/blocks/input-block.md) | Collects information from users via elements. |
| [Markdown](https://docs.slack.dev/reference/block-kit/blocks/markdown-block.md) | Displays formatted markdown. |
| [Plan](https://docs.slack.dev/reference/block-kit/blocks/plan-block.md) | Displays a collection of related tasks. |
| [Rich text](https://docs.slack.dev/reference/block-kit/blocks/rich-text-block.md) | Displays formatted, structured representation of text. |
| [Section](https://docs.slack.dev/reference/block-kit/blocks/section-block.md) | Displays text, possibly alongside elements. |
| [Table](https://docs.slack.dev/reference/block-kit/blocks/table-block.md) | Displays structured information in a table. |
| [Task card](https://docs.slack.dev/reference/block-kit/blocks/task-card-block.md) | Displays a single task, representing a single action. |
| [Video](https://docs.slack.dev/reference/block-kit/blocks/video-block.md) | Displays an embedded video player. |

## Block elements

| Name | Description |
|------|-------------|
| [Button](https://docs.slack.dev/reference/block-kit/block-elements/button-element.md) | Allows users a direct path to performing basic actions. |
| [Checkboxes](https://docs.slack.dev/reference/block-kit/block-elements/checkboxes-element.md) | Allows users to choose multiple items from a list of options. |
| [Date picker](https://docs.slack.dev/reference/block-kit/block-elements/date-picker-element.md) | Allows users to select a date from a calendar style UI. |
| [Datetime picker](https://docs.slack.dev/reference/block-kit/block-elements/datetime-picker-element.md) | Allows users to select both a date and a time of day. |
| [Email input](https://docs.slack.dev/reference/block-kit/block-elements/email-input-element.md) | Allows user to enter an email into a single-line field. |
| [Feedback buttons](https://docs.slack.dev/reference/block-kit/block-elements/feedback-buttons-element.md) | Buttons to indicate positive or negative feedback. |
| [File input](https://docs.slack.dev/reference/block-kit/block-elements/file-input-element.md) | Allows user to upload files. |
| [Icon button](https://docs.slack.dev/reference/block-kit/block-elements/icon-button-element.md) | An icon button to perform actions. |
| [Image](https://docs.slack.dev/reference/block-kit/block-elements/image-element.md) | Displays an image as part of a larger block of content. |
| [Multi-select menu](https://docs.slack.dev/reference/block-kit/block-elements/multi-select-menu-element.md) | Allows users to select multiple items from a list of options. |
| [Number input](https://docs.slack.dev/reference/block-kit/block-elements/number-input-element.md) | Allows user to enter a number into a single-line field. |
| [Overflow menu](https://docs.slack.dev/reference/block-kit/block-elements/overflow-menu-element.md) | Allows users to press a button to view a list of options. |
| [Plain-text input](https://docs.slack.dev/reference/block-kit/block-elements/plain-text-input-element.md) | Allows users to enter freeform text data into a single-line or multi-line field. |
| [Radio button group](https://docs.slack.dev/reference/block-kit/block-elements/radio-button-group-element.md) | Allows users to choose one item from a list of possible options. |
| [Rich text input](https://docs.slack.dev/reference/block-kit/block-elements/rich-text-input-element.md) | Allows users to enter formatted text in a WYSIWYG composer, offering the same messaging writing experience as in Slack. |
| [Select menu](https://docs.slack.dev/reference/block-kit/block-elements/select-menu-element.md) | Allows users to choose an option from a drop down menu. |
| [Time picker](https://docs.slack.dev/reference/block-kit/block-elements/time-picker-element.md) | Allows users to enter numerical data into a single-line field. |
| [URL input](https://docs.slack.dev/reference/block-kit/block-elements/url-input-element.md) | Allows user to enter a URL into a single-line field. |
| [URL source](https://docs.slack.dev/reference/block-kit/block-elements/url-source-element.md) | Displays a URL source for referencing within a task card block. |
| [Workflow button](https://docs.slack.dev/reference/block-kit/block-elements/workflow-button-element.md) | Allows users to run a link trigger with customizable inputs. |

## Composition objects

| Name | Description |
|------|-------------|
| [Confirmation dialog object](https://docs.slack.dev/reference/block-kit/composition-objects/confirmation-dialog-object.md) | Provides a dialog that adds a confirmation step to interactive elements. |
| [Conversation filter object](https://docs.slack.dev/reference/block-kit/composition-objects/conversation-filter-object.md) | Provides a way to filter the list of options in conversation selector menus. |
| [Dispatch action configuration object](https://docs.slack.dev/reference/block-kit/composition-objects/dispatch-action-configuration-object.md) | Defines when a plain-text input element will return a `block_actions` interaction payload. |
| [Input parameter object](https://docs.slack.dev/reference/block-kit/composition-objects/input-parameter-object.md) | Defines an object containing information about an input parameter. |
| [Option object](https://docs.slack.dev/reference/block-kit/composition-objects/option-object.md) | Represents a single item in a number of item selection elements. |
| [Option group object](https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object.md) | Used to group option objects in select menus. |
| [Text object](https://docs.slack.dev/reference/block-kit/composition-objects/text-object.md) | Defines text for many different blocks and elements. |
| [Trigger object](https://docs.slack.dev/reference/block-kit/composition-objects/trigger-object.md) | Defines an object containing trigger information. |
| [Workflow object](https://docs.slack.dev/reference/block-kit/composition-objects/workflow-object.md) | Defines an object containing workflow information. |
| [Slack file object](https://docs.slack.dev/reference/block-kit/composition-objects/slack-file-object.md) | Defines an object containing Slack file information to be used in an image block or image element. |