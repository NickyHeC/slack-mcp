Source: https://docs.slack.dev/messaging/work-objects-implementation

# Implementing Work Objects

Implementing Work Objects requires a Slack app. For more information on how to create an app, check out this [quickstart guide](/quickstart).

First, you must enable the Work Objects feature on your app. To do so, perform the following steps:

1.  Visit [https://api.slack.com/apps](https://api.slack.com/apps) and select your app.
2.  Navigate to **Work Object Previews** under the left sidebar menu.
3.  Enable the toggle.
4.  Select the entity type(s) that you would like to add to your app. Supported entity types can be found [here](#supported-entity-types).
5.  Click **Save**.

![App settings](/assets/images/app-settings-24048cae4f180b3538ea1eb7c14165a3.png)

### Unfurl implementation {#implementation-unfurl}

Work Object unfurls are an extension of the existing [link unfurl feature](/messaging/unfurling-links-in-messages/) for Slack apps. If your app has not been configured with it yet, please follow the [setup instructions](/messaging/unfurling-links-in-messages/#setup) to do so; supporting [composer unfurls](/messaging/unfurling-links-in-messages/#unfurl_previews) should be the standard for all apps.

The [`chat.unfurl`](/reference/methods/chat.unfurl/) API method, which provides unfurl content to Slack, has been updated with a new optional parameter: `metadata`. Slack uses this parameter to generate a Work Object representing the resource your app is unfurling. Please ensure that the `metadata` parameter is URL-encoded. If you're using one of Slack's [developer tools](/tools/), this is handled automatically, and no further action is needed.

The JSON schema is found below:

```
"metadata": {  "entities": [    {      "app_unfurl_url": "https://example.com/document/123?eid=123456&edit=abcxyz", // URL posted by the user in a conversation      "url": "https://example.com/document/123", // URL representing the resource in the third party system      "external_ref": {        "id": "123", // a string ID that uniquely identifies the resource being unfurled        "type": "document" // An optional internal type for entity in the source system. Only needed if the ID is not globally unique or needed when retrieving the item      },      "entity_type": "slack#/entities/file", // entity type      "entity_payload": {}, // entity schema    }  ]}
```

Parameter

Description

`app_unfurl_url`

The URL link posted by the user in a conversation. This is the same URL obtained from the [`link_shared`](/reference/events/link_shared/) event.

`entities`

The array contains the Work Object entities that you want to unfurl in Slack. You can provide multiple entities if the user has provided multiple URLs that need to be unfurled.

`entity_type`

Each entity has a type defined by `entity_type`. The available types are listed in the [supported entity types](#supported-entity-types) section. Each entity also includes a set of properties that are displayed in the Work Object, contained within the `entity_payload` object. Refer to the [entity payload schema](#entity-payload-schema) for details on customizing the displayed information.

`external_ref`

Contains a string ID that uniquely identifies the resource being unfurled. It's strongly recommended to use the same ID your third-party system uses to identify and retrieve the resource via its APIs. Must only be constructed to uniquely identify the Work Object, and must not contain any other information. See [this section](#marketplace-submission-launch-considerations) for more details.

`url`

The URL that directs the user to the desired resource on a third party system. When a user clicks the Work Object link trigger, they'll be directed to this URL.

#### Refreshing unfurls {#refreshing-unfurls}

When an end user hovers over a Work Object unfurl, a refresh button appears in the footer. Clicking this button closely follows the initial unfurl process by triggering a new [`link_shared`](/reference/events/link_shared/) event to your app, allowing it to provide the latest data and update the unfurl using the [`chat.unfurl`](/reference/methods/chat.unfurl/) API method.

![Refreshing unfurls](/assets/images/refreshing-unfurls-b16794ddc774cf0cfe689e990a875e32.png)

#### Automatic refresh {#automatic-refresh}

Unfurls are automatically refreshed when users engage with Work Objects in the following ways:

*   **Flexpane interactions.** When a user opens, edits, or refreshes the flexpane and your app responds using the [entity.presentDetails](/reference/methods/entity.presentdetails) API method, the unfurl will also be updated given the entity metadata that has changed.
*   **Block action clicks.** When a user clicks an action button on an unfurl, a refresh is scheduled to pick up any changes the action may have caused in your external system. This refresh occurs after a short delay to allow time for your system to process the action.

To optimize automatic refresh behavior, you can include the `metadata_last_modified` field in the `attributes` object of the `entity_payload` as in the following example:

```
{  "entity_payload": {    "attributes": {      "title": { "text": "My Document" },      "metadata_last_modified": 1706123456    }  }}
```

This integer timestamp indicates when the entity metadata was last modified. Slack compares this value to the previously stored timestamp, and only triggers a refresh when the new value is greater. If the `metadata_last_modified` field is not provided, Slack will use the `date_updated` field to determine whether the entity metadata has any updates.

### Notifications implementation {#implementation-notifications}

The [`chat.postMessage`](/reference/methods/chat.postMessage/) API method can also be used to post Work Object entities by re-using the existing `metadata` parameter. In this case, no link has been unfurled, so the `app_unfurl_url` property is not required. The JSON schema for passing entity metadata is the same as that for the [`chat.unfurl`](/reference/methods/chat.unfurl/) API method.

### Flexpane implementation {#implementation-flexpane}

The flexpane component requires the Work Object unfurl to be implemented.

The flexpane introduces a new event: [`entity_details_requested`](/reference/events/entity_details_requested) and a new API method: [`entity.presentDetails`](/reference/methods/entity.presentDetails).

To subscribe to the `entity_details_requested` event:

1.  Visit [https://api.slack.com/apps](https://api.slack.com/apps) and select your app.
2.  Navigate to the **Events & Subscriptions** section in the sidebar.
3.  Click the **Subscribe to bot events** section.
4.  Add the `entity_details_requested` event.

When a user clicks an unfurl, an `entity_details_requested` event is sent to your app. This event contains information about the user requesting access to the flexpane. Your app can then use the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method to populate the flexpane with content.

Additionally, your app can require user authentication with a third-party service before granting access to the flexpane. If the user is not authenticated, your app can use the `user_auth_required` parameter to prompt authentication. You can specify a `user_auth_url` to redirect users to an authentication page.

The `metadata` schema for the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method is nearly identical to that of the [`chat.unfurl`](/reference/methods/chat.unfurl) API method, except:

*   the `entities` array is removed.
*   the `app_unfurl_url` parameter is not included in the `entity` object.

```
"metadata": {  "entity_type": "slack#/entities/file", // entity type  "entity_payload": {}, // entity schema}
```

If your app does not implement the flexpane, the content displayed in the unfurl will be shown in the flexpane as a placeholder.

## Entity payload schema {#entity-payload-schema}

The entity payload contains information that will populate the unfurl or the flexpane. The schema is as follows:

```
{  "entity_payload": {    "attributes": {},    "fields": {},     "custom_fields": [], // optional    "display_order": [] // optional  }}
```

info

It is strongly recommended to adhere to our recommended field names, as the Work Object schemas are used to power downstream features. Validation will not fail, but the downstream features will not work as intended For example, don't send a `creator` field instead of the `created_by` field.

### The attributes property {#entity-payload-schema-attributes}

The `attributes` property contains fields that help Slack identify the resource and generate its Work Object header.

```
{  "attributes": {    // Required fields     "title": {      "text": "Document 123" // title of the Work Object entity    },        // Optional fields    "display_id": "123", // user-friendly string ID to display on the entity    "display_type": "Document", // string that represents the resource being unfurled. Default is "File" for a file entity or "Task" for a task entity.    "product_name": "Slack", // name of the product that will be displayed in the Work Objects header. Default is the app name.    "product_icon": {       // A product icon to display in the Work Object header. Default is the app icon. If you choose to provide a custom icon, use a different image than your app icon to avoid      // displaying duplicate icons in the UI. Must be a publicly-accessible URL      // or a `slack_file` object (https://docs.slack.dev/reference/block-kit/composition-objects/slack-file-object/).      "alt_text": "Image of Document app icon",      // this      "url": "https://example.com/icon", // publicly-accessible URL to an image      // OR      "slack_file": { // provide either file ID or the url; only one is required.        "id": "F0123456",         "url": "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"      }    },    "full_size_preview": {      "is_supported": true, // required      "preview_url": "https://example.com/document-123-image.png?res=2000x2000", // publicly-accessible URL to an image      "mime_type": "image/png" // Mime type for the preview (only PDF and images types are currently supported)    },    // This field indicates when the metadata about this item was last    // modified. We use this to determine whether we should request new unfurl    // metadata via the `link_shared` event. This will often be the same value as    // `fields.date_updated`, but can be controlled independently to offer less/more    // frequent requests to update unfurl metadata.    "metadata_last_modified": 1741164235 // value in UNIX timestamp  }}
```

### The full_size_preview property {#full-size-previews}

If your entity supports a visual preview within Slack, you can provide a thumbnail image in the unfurl card and a full size image or PDF preview to be displayed in the full size preview modal. Below are examples of how to define the schema for each scenario.

**Unfurl card**

```
{  "metadata": {    "entities": [      {        "app_unfurl_url": "https://example.com/document/123",        "entity_type": "slack#/entities/file",        "entity_payload": {          "attributes": {            "full_size_preview": {               // `is_supported` lets Slack know that a full preview is supported              "is_supported": true, // required              "preview_url": "https://example.com/document/123/preview_123.png", // required if the full preview is supported              "mime_type": "application/pdf", // required if the full preview is supported              "error": {                "code": "file_not_supported", // "file_not_supported", "file_size_exceeded", or "custom"                "message": "Detailed error message"              } // error message to display if the full-size preview is not available            }          },          "fields":{            "preview": {              // this is the thumbnail that is displayed in the unfurl card              "image_url": "https://example.com/document/123/preview_123.png",              "alt_text": "Preview"            }          }        }      }    ]  } }
```

The `File` and `Content Item` entity types define a `preview` field that can be used to display the thumbnail in the unfurl. If desired for other entity types, a custom field can be used to display an image in the unfurl.

The `full_size_preview` object provided in the unfurl metadata must include the `is_supported` attribute to enable the full size preview. Currently, only images and PDFs are supported for the preview.

**Flexpane window**

```
{  "metadata": {    {      "entity_type": "slack#/entities/file",      "entity_payload": {        "attributes": {          "full_size_preview": {             // `is_supported` lets Slack know that a full preview is going to be rendered            "is_supported": true, // required            "preview_url": "https://example.com/document/123.pdf", // required if the full preview is supported            "mime_type": "application/pdf", // required if the full preview is supported            "error": {                "code": "file_not_supported", // "file_not_supported", "file_size_exceeded", or "custom"                "message": "Detailed error message"            } // error message to display if the full-size preview is not available          }        },        "fields": {...}      }    }  }}
```

The `full_size_preview` object includes three required properties to display a preview: `is_supported`, `preview_url`, and `mime_type`. The `preview_url` contains publicly accessible URLs for PDFs, images, or PDF versions of other supported documents. For security reasons, these public URLs must include the CORS response header set to `access-control-allow-origin:https://app.slack.com`. The `mime_type` property is needed to render the preview modal for the correct media type.

You may provide the minimal `{'is_supported': true}` value for the `full_size_preview` field of an unfurl to enable generation of URLs that are only accessible for a limited duration.

It is not recommended to include the `preview` field when providing entity details for the full size preview modal.

### Automatic file shares {#automatic-file-shares}

When your app includes a `slack_file` object in image fields within the unfurl or flexpane metadata, Slack automatically creates a file share to the conversation.

Using `slack_file` objects instead of publicly-accessible URLs offers several benefits:

*   **Enhanced security**: Images are hosted within Slack rather than exposed on the public internet, keeping sensitive content protected.
*   **Unified file management**: Files are managed through Slack's file system, making them accessible in the unified files browser.

With automatic file shares, your integration is simplified further—no need to include a separate file block in your unfurl payload or call the [`files.remote.share`](/reference/methods/files.remote.share/) API method.

Your app still needs to create the file first using one of these approaches:

*   [Adding remote files](/messaging/working-with-files#adding): Use [`files.remote.add`](/reference/methods/files.remote.add/) for files hosted on external systems
*   [Uploading files](/messaging/working-with-files#uploading_files): Use [`files.getUploadURLExternal`](/reference/methods/files.getUploadURLExternal/) and [`files.completeUploadExternal`](/reference/methods/files.completeUploadExternal/) to upload files directly to Slack

Once the file is created, include its ID in a `slack_file` object within your Work Object metadata, and Slack will handle sharing it to the conversation automatically.

The following fields support automatic file share creation:

Field

Location

`slack_file`

`entity_payload.slack_file` (File entity type)

`product_icon`

`entity_payload.attributes.product_icon`

Image/file fields

`entity_payload.fields` (e.g., `preview` and other image/file fields)

Custom image/file fields

`entity_payload.custom_fields` (when type is `slack#/types/image` or `slack#/types/file`)

**Example**

After creating a file and obtaining its file ID, include it in the `preview` field:

```
{  "fields": {    "preview": {      "type": "slack#/types/image",      "alt_text": "Document preview",      "slack_file": {        "id": "F0123456"      }    }  }}
```

Slack will automatically and silently share the file (`F0123456`) to the conversation where the unfurl appears. You no longer need to call `files.remote.share` or include a file block separately.

**Note**: This automatic behavior only applies to `slack_file` images or file types. When using publicly-accessible URLs via `image_url`, no file share is created since the image is hosted externally.

### The fields property {#entity-payload-schema-fields}

The `fields` properties are optional (but recommended) properties displayed in the Work Object unfurl below the header. The properties within the `fields` object vary by entity type. For a list of supported entity types and their recommended `fields` properties, refer to the [supported entity types](#supported-entity-types) section.

### The custom_fields property {#entity-payload-schema-custom-fields}

The `custom_fields` property is similar to the `fields` property but allows your app to define fully custom properties. This parameter is optional. See the [supported properties for a field](#supported-properties-for-a-field) section for a list of supported properties.

```
{  "custom_fields": [     {      "key": "ticket_type", // key that will be used to reference this property      "label": "Ticket Type", // property label that will be displayed in the Work Object body      "value": "Epic", // property value that will be shown in the Work Object body      "type": "string" // Slack data type    }  ]}
```

### The display_order property {#entity-payload-schema-display-order}

The `display_order` property determines the order in which properties from `fields` and `custom_fields` are displayed in the Work Object body. If `display_order` is not set, the properties will appear in the order defined by the entity type's `fields` schema and the `custom_fields` will be appended at the end.

```
{  "display_order": ["ticket_type", "created_by", "preview"]}
```

## Editing Work Object fields {#editing}

Apps can designate fields as _editable_ by a user in the Work Object flexpane. If supported by the app, users will see a pencil icon in the flexpane header that they can click to modify the editable fields. Once the edits are complete, the user can click `Save`, which will send a [`view_submission`](/reference/interaction-payloads/view-interactions-payload/#view_submission) payload to your app with the updated information.

![Flexpane editing](/assets/images/flexpane-editing-b4cd9bf73fbbf731942179d727b56064.png)

### Designating a field as editable {#editing-designate-field}

Your app can designate a field as editable by adding the `edit` property to a field and setting the value to `true` as shown below:

```
{  "fields": {    "description": {      "value": "We need to implement a login page using [...]",      "format": "markdown",      "edit": {        "enabled": true      }    },    {...} // other fields  }}
```

### The edit property {#editing-edit-property}

The `edit` property contains the following attributes that can help further customize the experience:

Property

Type

Description

`enabled`

boolean

Toggle to enable edit mode on this field.

`placeholder`

object

Placeholder text shown on empty `text` and `number` inputs.

`hint`

object

Hint text is displayed below the input on supported input blocks.

`optional`

boolean

Whether this field can be left blank.

`select`

object

Options relevant to `select` and `multi-select` inputs.

`number`

object

Additional properties relevant to `number` type fields.

`text`

object

Additional properties relevant to `text` type fields.

`boolean`

object

Additional properties relevant to `boolean` type fields.

The `placeholder` and `hint` properties have the following properties:

Property

Type

Description

`type`

string

Set `type: "plain_text"`.

`text`

string

Text to be displayed.

`emoji`

boolean

Whether or not Slack-style emojis should be recognized within the string. _This is only supported for the hint and not the placeholder._

The `number` property has the following properties:

Property

Type

Description

`min_value`

number

Minimum allowed value.

`max_value`

number

Maximum allowed value.

The `text` property has the following properties:

Property

Type

Description

`min_length`

number

Minimum string length. Cannot be lower than 0 or greater than 3000.

`max_length`

number

Maximum string length. Cannot be lower than 0 or greater than 3000.

The `boolean` property has the following properties:

Property

Type

Description

`input_type`

string

The type of boolean input to render when editing. Must be one of: `"checkbox"`, `"radio"`, or `"select"`. You can use different input types for view and edit modes. For example, use `text` in view mode with `select` or `radio` in edit mode, or use `checkbox` in view mode with `checkbox` in edit mode. **Note:** If `input_type` is not provided, the default is `"select"` unless view mode `boolean.type` is `checkbox`, in which case the default is `"checkbox"`.

The `select` property has the following properties:

Property

Type

Description

`current_value`

string

The current value of the select input.

`current_values`

array of strings

If multi-select, then the current values of the multi-select input. Should be in the same order as the human readable form of the values.

`static_options`

array of objects

If present on a valid field, then these values will appear on the fields as static select options.

`fetch_options_dynamically`

boolean

When set to true, Slack will dynamically fetch the select options as the user types. Default is false.

The `static_options` property above has the following properties:

Property

Required

Type

Description

`value`

Yes

string

The value that will be sent to your application when the user submits the form. Max length: 150 characters.

`text`

Yes

object

Human-readable text that will be displayed in the select menu. The object schema can be found [here](/reference/block-kit/composition-objects/#text). Max length: 75 characters.

`description`

No

Object

A descriptive text that will be shown below the text property. The object schema can be found [here](/reference/block-kit/composition-objects/#text). Max length: 75 characters.

### Field mapping {#editing-field-mapping}

When a field is made editable, Slack will map the field's type to the most appropriate Block Kit input. For example, a `description` field will become a Block Kit [Plain-Text input](/reference/block-kit/block-elements/#input), and a `due_date` field will become a [Date picker input](/reference/block-kit/block-elements/#datepicker) when the `slack#/types/date` type is used. The full list of supported Block Kit inputs can be found below:

Block Kit input type

Supported

Restrictions

[`Checkboxes`](/reference/block-kit/block-elements/#checkboxes)

Yes

Default input for Work Object boolean fields when `input_type` is `"checkbox"`. This is limited to a single checkbox for boolean types.

[`Date picker`](/reference/block-kit/block-elements/#datepicker)

Yes

Default input for Work Object date fields

[`Datetime picker`](/reference/block-kit/block-elements/#datetimepicker)

Yes

Default input for Work Object datetime fields

[`Email`](/reference/block-kit/block-elements/#email)

Yes

Default input for Work Object email fields

[`File`](/reference/block-kit/block-elements/#checkboxes)

No

[`Multi-select`](/reference/block-kit/block-elements/#multi-select)

Yes

This is supported on array types using the same criteria outlined below for Select. For example, an array with `slack/#types/channel_id` items will become a multi-conversations select.

[`Number`](/reference/block-kit/block-elements/#number)

Yes

Min/max and whether decimals are allowed can be configured via field edit metadata

[`Plain-text`](/reference/block-kit/block-elements/#input)

Yes

Maximum of 3000 characters allowed. Edit will be disabled for any field with a value larger than this

[`Radio button group`](/reference/block-kit/block-elements/#radio)

No

Use selects instead.

[`Rich text`](/reference/block-kit/block-elements/#rich_text_input)

No

Rich text editing is not currently supported. As an alternative, raw markdown can be used in a standard text input.

[`Select`](/reference/block-kit/block-elements/#select)

Yes

For static or external selects, you'll need to set up appropriate configuration in the fields [`edit.select`](#editing-edit-property) section. Fields of type `slack#/types/user` or `slack/#types/channel_id` will automatically become [users select](/reference/block-kit/block-elements/select-menu-element/#users_select) or [conversations select](/reference/block-kit/block-elements/select-menu-element/#conversations_select) (respectively).

[`Time picker`](/reference/block-kit/block-elements/#timepicker)

Yes

[`URL`](/reference/block-kit/block-elements/#url)

Yes

Default input for Work Object link fields

Apart from the `external_select` input, all changes to any of the input fields are packaged in a [`view_submission`](/reference/interaction-payloads/view-interactions-payload/#view_submission) payload and sent to your app when the user clicks **Save**.

Here is an example of a metadata payload for a `task` entity that contains several editable fields:

```
{  "entity_type": "slack#/entities/task",  "entity_payload": {    "attributes": {      "title": {        "text": "Some task",        "edit": {          // This would cause the title element to transition into a           // to-be-determined edit surface. This would likely not be          // a native Block Kit element, but should have similar properties.          "enabled": true,          "text": {            "max_length": 50          }        }      },    },    "fields": {      "status": {        "value": "Blocked",        "edit": {          // Providing select options here turns this field into a select during          // edit mode.  Without this, the field would become a text input.          "enabled": true,          "select": {            "static_options": [              {                "value": "123",                "text": {                  "text": "In progress"                }              },              {                "value": "456",                "text": {                  "text": "Done"                }              }            ]          }        }      },      "due_date": {        "value": "2026-06-06",        "type": "slack#/types/date", // This value can be `slack#/types/timestamp`         // or `slack#/types/date`        "edit": {          // This would become a datetime or date picker element based on the          // fields type in the schema.          "enabled": true        }      },      "assignee": {        "type": "slack#/types/user",        // You can identify a user in one of two ways:        // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known.        // - Use "text" with the user's display name if the Slack user ID is not available.        "user": {          "text": "Joan Smith",          "email": "joan.smith@example.com",        },        "edit": {          // External select supported by setting the          // `fetch_options_dynamically` field to true.          "enabled": true,          "select": {            "fetch_options_dynamically": true          }        }      },      "completed": {        "type": "boolean",        // In this example, view mode uses `text` type with custom labels, displaying "Nope" when false.        // Edit mode uses `select` input type, showing a dropdown with "Totally!" and "Nope" as options.        "value": false,        "boolean": {          "type": "text",          "true_text": "Totally!",          "false_text": "Nope"        },        "edit": {          "enabled": true,          "optional": true,          "boolean": {            "input_type": "select"          }        }      }    }  }}
```

## Handling view_submission requests {#editing-view-submission}

When the user clicks **Save**, a [`view_submission`](/reference/interaction-payloads/view-interactions-payload/#view_submission) payload will be sent to your app. Here is an example:

```
{  "type": "view_submission",  "team": {    "id": "T123ABC456",    "domain": "slack-domain-12343",    "enterprise_id": "E1234",    "enterprise_name": "Acme Corp"  },  "user": {    "id": "U1234",    "username": "jennifer_hynes",    "name": "jennifer_hynes",    "team_id": "T123ABC456"  },  "api_app_id": "A123ABC456",  "token": "vrv7tNLHMRT8hdqLZjuM10St",  "trigger_id": "1234567890123.1234567890123.abcdef01234567890abcdef012345689",  "view": {    "id": "V08UHA2RFFF",    "team_id": "E123ABC456",    "type": "entity_detail",    "blocks": [],    "private_metadata": "",    "callback_id": "",    "state": {      "values": {        "description": {           "description.input": {            "type": "plain_text_input",            "value": "We need to implement a login page using **Capybara** for our testing framework. This page will be used for testing user authentication and login functionality within the application. hello\\n\\n### Requirements:\\n- Create a simple login page with fields for:\\n  - **Username**\\n  - **Password**\\n  - **Login button**\\n- Implement basic form validation to ensure both fields are populated before submitting.\\n- Ensure the page is responsive and works well on both desktop and mobile views.\\n- Use **Capybara** to automate the interaction with the login form for testing purposes.\\n  - Automate filling out the username and password fields.\\n  - Simulate clicking the login button and validating the redirect or success message.\\n\\n![Image](https://github.com/user-attachments/assets/f94f0a80-993d-46c5-be4c-1d3f3cd8312d)"          }        }      }    },    "hash": "1748539925.7JuMmoCH",    "external_ref": {      "id": "139"    },    "entity_url": "https://github.com/repos/{user}/{repo}/issues/139",    "message_ts": "1758902242.754879",    "thread_ts": "1758901978.959789",    "channel": "C123ABC456",    "app_unfurl_url": "https://github.com/repos/{user}/{repo}/issues/139?myquery=param",    "app_id": "A123ABC456",    "external_id": "",    "app_installed_team_id": "E123ABC456",    "bot_id": "B0123456"  },  "response_urls": [],  "is_enterprise_install": false,  "enterprise": {    "id": "E1234",    "name": "Acme Corp"  }}
```

The payload contains new properties relevant to Work Objects, such as the `entity_url` and `external_ref` properties. You can use both to identify the Work Object that was edited. Additionally, the `view.type` property of the interactivity event will be set to `entity_detail` for these types of requests specifically. The values that have been updated in the flexpane will be provided in the `view.state.values` property.

If the user has submitted an edit that has incorrect or invalid information, there are multiple ways to provide feedback on this to the user using error handling.

Once your app has finished processing the changes submitted by the user, you should make a request to the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method with the updated state of the Work Object using the `trigger_id` that was provided in the `view_submission` payload.

### Dynamic External Select {#editing-dynamic-external-select}

Dynamic External Select allows the app to generate options for single or multi-select inputs dynamically as the user types in the input box.

When `edit.select.fetch_options_dynamically` is set under a select field, Slack will dispatch a [`block_suggestion`](/reference/block-kit/block-elements/#external_select) request when the user begins to modify the field. In the payload, the `block_id` and `action_id` properties are mapped from the name of the field provided in the schema.

```
{   "type": "block_suggestions",   "block_id": "assignee", // comes from the name of the field in the schema   "action_id": "assignee.input",   "value": "jo",   ...}
```

Your app should respond with the options of the select, such as in the example below:

```
{  "options": [    {      "text": {        "type": "plain_text",        "text": "joe.bob@example.com"      },      "value": "U123"    },    {      "text": {        "type": "plain_text",        "text": "joan.rivers@example.com"      },      "value": "U456"    },    {      "text": {        "type": "plain_text",        "text": "jonny.appleseed@example.com"      },      "value": "U789"    }  ]}
```

### Editing validations {#editing-error-handling}

There are three levels of validations to consider when it comes to updating a Work Object in Slack:

1.  Client-side _field level_ validation within Slack via `edit` properties.
2.  Server-side _field level_ validation via response to `view_submission`.
3.  Server-side _form level_ validation via the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method.

**Client-side _field level_ validation**

This type of validation prevents the user from submitting the form until the issue is resolved. These types of validations are configured by the contents of the `edit` block in a given field. For example, an entity with the following metadata will result in the validation errors shown in the subsequent image:

```
{  "entity_type": "slack#/entities/task",  "entity_payload": {    "attributes": {      "title": {        "text": "Update links in login page",        "edit": {          "enabled": true,          // The title is always required (i.e., optional: false)        }      },    },    "fields": {      "description": {        "value": "We need to update the links in the login page to use our new branding",        "edit": {          "enabled": true,          "text": {            "min_length": 15,          }        }      }    },    "custom_fields": [      {        "key": "story_points",        "label": "Story points",        "type": "integer",        "edit": {          "enabled": true,          "number": {            "max_value": 10,          }        }      },    ]  }}
```

![Client-side errors](/assets/images/client-side-errors-759cdee2a888fddb3c58caa4c308dadd.png)

**Server-side _field level_ validation**

These types of errors are documented in more detail [here](/surfaces/modals/#displaying_errors), but you'll want to respond to the `view_submission` event with an object instead of an empty `ack()`. Note that because this is using the `ack` function, you'll need to respond within 3 seconds to prevent a timeout. Here is an example:

```
{  "response_action": "errors",  "errors": {    "due_date": "You cannot select a date in the past"  }}
```

When this happens, we'll display the error in-line and disable the **Submit** button until that field is changed.

![Server-side field errors](/assets/images/server-side-field-errors-c9d8fbb46d7886549bfe2d3a23799dec.png)

**Server-side _form level_ validation**

The last type of error handling is to be used when there isn't anything wrong with a specific field, but instead, something went wrong at a higher level. Examples of these kinds of errors could include rate limit errors, consistency mismatches, or an uncaught exception when processing the save.

These errors should be sent by calling the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method with an `edit_error` `error` payload instead of any entity metadata. For example:

```
{  "trigger_id": "1234567890123.1234567890123.abcdef01234567890abcdef012345689",  "error": {    "status": "edit_error",    "custom_message": "Something went wrong but we're not sure what. Try again later",  }}
```

![Server-side form errors](/assets/images/server-side-form-errors-6b908bdc93d8f9992732ffc18f1cc26b.png)

## Adding actions to Work Objects {#actions}

Block Kit actions, such as buttons, can be added to either (or both) the unfurl card and the flexpane view footer. Up to two primary actions can be defined. These will always appear in the footer of the unfurl card or the flexpane window.

![Actions](/assets/images/actions-33dcc7225ca39054764647a5cc7630b4.png)

Additionally, up to five actions can be defined in the overflow menu. This can be accessed by clicking **More actions** in the overflow menu.

![Actions unfurl overflow](/assets/images/actions-unfurl-overflow-cbad554a3a0618a3920b5cffbf3ce7f8.png)

The actions defined in the unfurl card can be different from the ones defined in the flexpane window. Finally, some default actions may appear in the overflow menu, such as:

*   Share \[Object\] (e.g., Share Issue)
*   Copy link to \[Object\] (e.g., Copy link to Issue)
*   Add to To-do
*   View in App

### Defining actions in the metadata payload {#actions-metadata}

A new `actions` field is used to define what actions will appear in the unfurl or flexpane. Both `primary_actions` and `overflow_actions` are optional properties.

```
{  "actions": {     "primary_actions": [], // up to two actions here    "overflow_actions": [] // up to five actions here  }}
```

Each `action` is defined by the following properties:

Property

Required

Type

Description

`text`

Yes

string

Human readable text that will be displayed in the button.

`action_id`

Yes

string

An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](/interactivity/handling-user-interaction/#payloads). Max length: 255 characters.

`value`

No

string

The value to send along with the [interaction payload](/interactivity/handling-user-interaction/#payloads). Maximum length is 2000 characters.

`style`

No

string

Decorates the button with either a green or red background. Use `style: primary` for green and `style: danger` for red.

`url`

No

string

Clicking the button will open the URL in the user's browser. Max length: 3000 characters.

`accessibility_label`

No

string

A label for longer descriptive text about a button element. This label will be read out by screen readers instead of the button's text parameter. Maximum length: 75 characters.

Example:

```
{  "actions": {     "primary_actions": [ // up to two actions here      {        "text": "Summarize issue with AI",        "action_id": "github_wo_button_summarize_issue",        "style": "primary",        "value": "user"      },      {        "text": "Close issue",        "action_id": "github_wo_button_close_issue",        "style": "danger",        "value": "user"      }    ],    "overflow_actions": [ // up to five actions here      {        "text": "Pin issue",        "action_id": "github_wo_button_pin_issue",        "style": "primary",        "value": "user"      },      {        "text": "Assign to me",        "action_id": "github_wo_button_assign_issue",        "style": "primary",        "value": "user"      }    ]  }}
```

The `actions` field is part of the `entity_payload` of each Work Object:

```
{  "entities": [    {      "app_unfurl_url": "https://github.com/issues",      "entity_type": "slack#/entities/task",      "entity_payload": {        "attributes": {},        "fields": {},        "actions": {          "primary_actions": [ // up to two actions here            {              "text": "Summarize issue with AI",              "action_id": "github_wo_button_summarize_issue",              "style": "primary",              "value": "user"            },            {              "text": "Close issue",              "action_id": "github_wo_button_close_issue",              "style": "danger",              "value": "user"            }          ],          "overflow_actions": [ // up to five actions here            {              "text": "Pin issue",              "action_id": "github_wo_button_pin_issue",              "style": "primary",              "value": "user"            },            {              "text": "Assign to me",              "action_id": "github_wo_button_assign_issue",              "style": "primary",              "value": "user"            }          ]        },        "custom_fields": [],        "display_order": []      }    }  ]}
```

When a user clicks a button, a [`block_actions`](/reference/interaction-payloads/block_actions-payload/) interactivity request is sent to your app.

### Handling block_actions events {#actions-handling-block-actions}

Your app can [handle](/interactivity/handling-user-interaction#payloads) `block_actions` events exactly like you'd respond to button action payloads from anywhere else in Slack.

The event payload looks slightly different when it's coming from an action on the unfurl vs. an action on the flexpane, but the properties in the container related to Work Objects are the same. This includes `entity_url`, `external_ref`, `app_unfurl_url`, `message_ts`, `thread_ts` and `channel_id`.

Below is an example payload when an action button on the unfurl is clicked:

```
{  "type": "block_actions",  "user": {    "id": "U123ABC456",    "username": "jennifer_hynes",    "name": "jennifer_hynes",    "team_id": "T123ABC456"  },  "api_app_id": "A123ABC456",  "token": "abc123",  "container": {    "type": "message_attachment",    "message_ts": "1753813500.959789",    "thread_ts": "1753813200.519449",    "channel_id": "C123ABC456",    "is_ephemeral": false,    "attachment_id": 1,    "is_app_unfurl": true,    "app_unfurl_url": "https://github.com/issues/139#comment123",    "entity_url": "https://github.com/issues/139",    "external_ref": {      "id": "139"    }  },  "trigger_id": "1234567890123.1234567890123.abcdef01234567890abcdef012345689",  "team": {    "id": "T123ABC456",    "domain": "team-domain",    "enterprise_id": "E123ABC456",    "enterprise_name": "Acme Corp"  },  "enterprise": {    "id": "E123ABC456",    "name": "Acme Corp"  },  "is_enterprise_install": false,  "channel": {    "id": "C123ABC456",    "name": "jennifer-test"  },  "app_unfurl": {    "id": 1,    "bot_id": "B123ABC456",    "bot_team_id": "T123ABC456",    "app_unfurl_url": "https://github.com/KrishnaPatel1/github-function-test/issues/139",    "is_app_unfurl": true,    "fallback": "Create Capybara login page\n Issue in GitHub",    "text": "Issue in GitHub",    "title": "Create Capybara login page",    "title_link": "https://github.com/issues/139",    "service_name": "Work Objects Demo App",    "fields": [      {        "value": "open",        "title": "Status",        "short": true      },      {        "value": "KrishnaPatel1",        "title": "Assignee",        "short": true      },      {        "value": "FY26 Q2",        "title": "Milestone",        "short": true      }    ]  },  "response_url": "https://hooks.slack.com/actions/T123/123/abc123",  "actions": [    {      "type": "button",      "text": {        "type": "plain_text",        "text": "Summarize issue with AI",        "emoji": true      },      "action_id": "github_wo_button_summarize_issue",      "block_id": "TPdc",      "style": "primary",      "value": "user",      "action_ts": "1748809126.803329"    }  ]}
```

Note that `container.type` will be `message_attachment` when the event is coming from an action on the unfurl, and will be `entity_detail` when the event is coming from an action on the flexpane.

### Handling authentication {#actions-request-authentication}

You can enforce authentication when a user clicks a button. If the user is not authenticated to perform the action, then your app can make a request to the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method with `user_auth_required=true` and a valid `user_auth_url`. This will open the flexpane with an appropriate treatment that encourages the user to complete the authentication flow by following `user_auth_url`. Other error types will not auto-open the flexpane. For non-authentication related errors, it’s best to send the user a DM for now.

**Other ways to handle the request**

*   [Open a modal](/interactivity/handling-user-interaction/#modal_responses) to collect more information from the user.
*   Post a message to the thread where the unfurl message is posted.
*   Send a message to the user's DM if the action has failed.
*   If the action is successful in the unfurl card, then refresh the unfurl by making a request to the `chat.unfurl` API method and by passing the new `metadata`.
*   If the action is successful in the flexpane, then refresh the flexpane by making a request to the `entity.presentDetails` API method with the new `metadata`. This way, the user will not have to manually click the refresh icon.

## Supported entity types {#supported-entity-types}

Type

`entity_type`

Description

`File`

`slack#/entities/file`

This can represent a document, a spreadsheet, an image, etc.

`Task`

`slack#/entities/task`

This can represent a ticket, a to-do, etc.

`Incident`

`slack#/entities/incident`

This can represent an incident, a service interruption, etc.

`Content Item`

`slack#/entities/content_item`

This can represent a content page, an article page, etc.

`Item`

`slack#/entities/item`

A general-purpose entity that can represent anything.

### File {#file}

![File](/assets/images/file-1d1abaabf876abbb9aa3e4f40b9b2cd9.png)

If your app is providing remote files, you'll want to use the same value for the the `remote_file.external_id` property and the Work Object's `external_ref.id`. This will allow us to provide the same `external_ref` back to your app in the `entity_details_requested` event triggered by a user opening the flexpane or preview from the files browser.

When you include a `slack_file` object in the `preview` field or at the entity level (`slack_file`), Slack will automatically create a file share to the conversation. See [Automatic file shares](#automatic-file-shares) for more details.

**Supported fields**

```
{  "fields": {    "preview": {      "type": "slack#/types/image",      "alt_text": "Document 123 image",      "image_url": "https://example.com/document-123-image.png" // must be a publicly-accessible URL or a `slack_file` URL for an image (https://docs.slack.dev/reference/block-kit/composition-objects/#slack_file)    },    "created_by": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "user_id": "U123ABC456",       },      "type": "slack#/types/user"    },    "date_created": {      "value": 1741164235 // value in UNIX timestamp    },    "date_updated": {       "value": 1741164235 // value in UNIX timestamp    },    "last_modified_by": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "user_id": "U123ABC456",       },      "type": "slack#/types/user"    },    "file_size": {      "value": "256MB"     },    "mime_type": {      "value": "image/gif"    }  },  "slack_file": {    // App's providing remote files as well as Work Objects should provide the     // file ID to ensure compatibility with Slack's unified files browser. File shares    // will be managed automatically    "id": "F123ABC456",        // The file's extension can optionally be specified here to create an icon for the file using    // built-in file icons like https://a.slack-edge.com/470bf9a/img/wo-file-icons/icon_image.png    "type": "gif"  }}
```

### Task {#task}

![Task](/assets/images/task-f0bf9f5098bc5062069c8408590efaba.png)

**Supported fields**

```
{  "fields": {    "description": {      "value": "task description here",      "format": "markdown" // optional    },    "created_by": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "user_id": "U0123456",      },      "type": "slack#/types/user"    },    "date_created": {      "value": 1741164235 // value in UNIX timestamp    },    "date_updated": {       "value": 1741164235 // value in UNIX timestamp    },    "assignee": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "text": "John Smith",        "email" "johnsmith@example.com"      },      "type": "slack#/types/user"    },    "status": {      "value": "open", // the status of the task      "tag_color": "blue", // used to provide a colored "chip" around the text      "link": "https://example.com/tasks?status=open"    },    "due_date": {      "value": "2025-06-10", // date in the format 'YYYY-MM-DD', or an integer unix timestamp if the type is "slack#/types/timestamp"      "type": "slack#/types/date" // this can also be type "slack#/types/timestamp"    },    "priority": {      "value": "high", // the priority level of the task      "icon": {        // the icon will be rendered to the left of the text        "alt_text": "Icon to indicate a high priority item",        "url": "https://example.com/icon/high-priority.png"      },      "link": "https://example.com/tasks?priority=high"    }  }}
```

### Incident {#incident}

![Incident](/assets/images/incident-9df4da8ee830be16790f1f87cbc75c00.png)

**Supported fields**

```
{  "fields": {    "status": {      "value": "open" // the status of the incident     },    "severity": {      "value": "high" // severity level of the incident    },    "created_by": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "user_id": "U0123456",      },      "type": "slack#/types/user"    },    "assigned_to": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "text": "John Smith",        "email" "johnsmith@example.com"      },      "type": "slack#/types/user"    },    "date_created": {      "value": 1741164235 // value in UNIX timestamp    },    "date_updated": {       "value": 1741164235 // value in UNIX timestamp    },    "description": {      "value": "incident description here",    },    "service": {      "value": "backend" // the service that is affected by the incident    }  }}
```

### Content Item {#content}

![Incident](/assets/images/content-item-9d4e994f7873e12ce28db2d1be132bdc.png)

**Supported Fields**

```
{  "fields": {    "preview": {      "type": "slack#/types/image",      "alt_text": "Page 123 review",      "image_url": "https://example.com/page-123-image.png" // must be a publicly-accessible URL or a `slack_file` URL for an image (https://docs.slack.dev/reference/block-kit/composition-objects/#slack_file)    },    "description": {      "value": "content description here",    },    "created_by": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "user_id": "U0123456",      },      "type": "slack#/types/user"    },    "date_created": {      "value": 1741164235 // value in UNIX timestamp    },    "date_updated": {       "value": 1741164235 // value in UNIX timestamp    },    "last_modified_by": {      // You can identify a user in one of two ways:      // - Use "user_id" with a Slack user ID (e.g., "U123ABC456") if known      // - Use "text" with the user's display name if the Slack user ID is not available      "user": {        "user_id": "U0123456",      },      "type": "slack#/types/user"    }  }}
```

### Item {#item}

The `item` entity does not contain a `fields` object. It is a general-purpose entity in which all of the properties must be specified in the `custom_fields` object.

Here is an example for a social media post item:

```
{  "custom_fields": [    {      "key": "saves",       "label": "Saves",      "value": 12,      "type": "integer"    },    {      "key": "likes",       "label": "Likes",      "value": 25,      "type": "integer"    },    {      "key": "username",       "label": "Username",      "value": "Slack Platform",      "type": "string"    },    {      "key": "caption",       "label": "Caption",      "value": "Check out my brand new Work Object app!",      "type": "string"    }  ]}
```

## Supported properties for a field {#supported-properties-for-a-field}

For `fields` and `custom_fields`, here are the properties that may be supported depending on field `type`:

Property

Required/Optional

Description

`value`

required

The value of the property. Not required for image properties such as `preview`.

`type`

varies

Required in `custom_fields` and in certain some entity fields. See the entity's `fields` schema for guidance on where this is optional. See the section below for acceptable values.

`icon`

optional

Can only be set when the `type` is `string`. This icon will be displayed next to field's text value. Not compatible with `tag_color`. More details available [here](#icon-properties).

`link`

optional

Can only be set when the `type` is `string`, `date`, or `timestamp`. The field's content will be hyperlinked with the URL specified here.

`tag_color`

optional

Can only be set when the `type` is `string`. Allows the string to be highlighted in of one of the following colors: `red`, `yellow`, `green`, `gray`, `blue`. e.g., `tag_color: "red"`.

`format`

optional

Can only be set when the `type` is `string`. Allows the string to be formatted in `markdown`. Incompatible with the `icon` or `link` properties. Set `format: "markdown"`.

`item_type`

optional

Required when the field's `type` is `array`. Value should be set to one of the valid array types. See valid array types in the next section.

`image_url`

optional

Used when the field's `type` is `slack#/types/image`.

`long`

optional

Can only be set when the `type` is `string`. Expands the field across a wider area in the unfurl card. Set `long: true`.

`slack_file`

optional

Used when the field's `type` is `slack#/types/image`. The object schema can be found [here](/reference/block-kit/composition-objects/slack-file-object/).

`alt_text`

optional

Used when the field's `type` is `slack#/types/image`.

`user`

optional

Used when the field's `type` is `slack#/types/user`. See [supported properties for user type](#user-properties).

`boolean`

optional

Used to represent a boolean option such as checkbox, radio or select option. Used when the field’s `type` is `boolean` . See [supported properties for boolean options](#boolean-properties).

`entity_ref`

optional

Used to represent relationships between multiple Work Object entities. Use this when the field’s `type` is `slack#/types/entity_ref`. This field not editable. See [supported properties for entity reference type](#entity-reference-properties).

For `custom_fields`, the `key` and `label` properties are required in addition to the `value` and `type`.

Property

Required/Optional

Description

`key`

required

Key that Slack will be use to reference this property.

`label`

required

Label that will be displayed in the Work Object body.

### Data types {#supported-property-data-types}

Here are the acceptable values for `type`:

Type

Description

`string`

A string value.

`integer`

An integer value.

`boolean`

A boolean value.

`array`

An array of items of a single type.

`slack#/types/user`

A user value. You can represent a user by providing either `user_id` (when the Slack user ID is known e.g., U1234567) or `text` (when only the user's name is available e.g., John Smith).

`slack#/types/channel_id`

A Slack conversation ID (e.g., C1234567).

`slack#/types/timestamp`

A UNIX timestamp (e.g., 1741164235).

`slack#/types/date`

A date in the format `YYYY-MM-DD`.

`slack#/types/image`

An image. Provide either the URL of a publicly hosted image (`image_url`) or a `slack_file` with a preview image. When using `slack_file`, a file share is automatically created. See [Automatic file shares](#automatic-file-shares).

`slack#/types/entity_ref`

The entity reference value. This type enables representation of relationships between multiple Work Object entities within the **same app**. For example, when implementing a task entity type with multiple subtasks, the entity reference type can be utilized to establish relationships with other sub-task Work Object entities.

`slack#/types/link`

A URL link. The value should be a valid URL string.

`slack#/types/email`

An email address. The value should be a valid email string.

For arrays, the supported data types are:

*   `string`
*   `integer`
*   `slack#/types/channel_id`
*   `slack#/types/user`
*   `slack#/types/entity_ref`

Here is an example of a custom field with the `array` type:

```
{  "type": "array",  "key": "array-of-strings",  "label": "Array of Strings",  "item_type": "string",  "value": [    {      "value": "A"    },    {      "value": "B"    }  ]}
```

### Boolean types {#boolean-properties}

The `boolean` field supports two rendering modes for view display: checkbox or custom text labels. With the checkbox configuration, a single checkbox option is shown. With the text configuration, two options are shown with custom labels (e.g., "Public" / "Private").

**Note:** Boolean fields can be made editable by adding the `edit` property with `enabled: true`. When editing is enabled, you can specify the `input_type` (checkbox, radio, or select) in the `edit.boolean` property. See [the `boolean` property](#editing-edit-property) for more details.

#### Checkbox schema {#checkbox-schema}

Property

Required/Optional

Type

Description

`type`

required

`string`

Must be `"checkbox"`.

`text`

required

`string`

Label text displayed next to the checkbox.

`description`

optional

`string`

Optional description text.

Here is an example of a boolean field with a checkbox schema and editing enabled:

```
{   "type": "boolean",   "key": "notifications",   "label": "Notifications",   "value": false,   "boolean": {    "type": "checkbox",    "text": "Enable email notifications",    "description": "Receive alerts when updates are made"    },   "edit": {     "enabled": true,     "optional": true,     "boolean": {       "input_type": "checkbox"     }   }}
```

#### Text schema {#text-schema}

Property

Required/Optional

Type

Description

`type`

required

`string`

Must be `"text"`.

`true_text`

required

`string`

Label shown when the value is `true`. Defaults to `Yes` if not provided.

`false_text`

required

`string`

Label shown when the value is `false`. Defaults to `No` if not provided.

`true_description`

optional

`string`

Optional description for the true state.

`false_description`

optional

`string`

Optional description for the false state.

Here is an example of a boolean field with a text schema and editing enabled.

```
{  "type": "boolean",  "key": "bool-key",  "label": "Optional Select",  "value": true,  "boolean": {    "type": "text",    "true_text": "Public",    "false_text": "Private",    "true_description": "Visible to all team members",    "false_description": "Only visible to project owners"    },  "edit": {    "enabled": true,    "optional": true,    "boolean": {      "input_type": "radio"    }  }}
```

### User types {#user-properties}

Here are acceptable properties for a user type:

Property

Required/Optional

Type

Description

`user_id`

optional

`string`

A slack `user_id`. Don't provide `text` when `user_id` is provided.

`text`

optional

`string`

The full name of the user. Don't provide `user_id` when `text` is provided.

`url`

optional

`string`

A link to an external profile for the user.

`email`

optional

`string`

The email of the user. When the email provided matches an valid Slack user, we will display the Slack user.

`icon`

optional

`icon`

An avatar for the user. Schema is described [here](#icon-properties).

### Icon properties {#icon-properties}

Properties such as the `attributes.product_icon` property and the `icon` property in `string` fields take a common structure that looks like this:

```
{   "alt_text": "Summary of image's content",  "url": "https://example.com/icon", // publicly-accessible URL to an image  // OR  "slack_file": { // provide either file ID or the url. Only one is required    "id": "F0123456",     "url": "https://files.slack.com/files-pri/T0123456-F0123456/xyz.png"  }}
```

### Entity reference types {#entity-reference-properties}

Here are acceptable properties for the entity reference type:

Property

Required/Optional

Type

Description

`entity_url`

required

`string`

The URL for the entity. Must be the canonical URL, and must not include any query or tracking parameters.

`external_ref`

required

`external_ref`

Reference used to identify an entity within the external system. Schema is described [here](#external-ref-properties).

`title`

optional

`required`

The title of the entity.

`display_type`

optional

`string`

The type to display on the Work Object entity header.

`icon`

optional

`icon`

An avatar for the entity. Schema is described [here](#icon-properties).

### External ref properties {#external-ref-properties}

Here is the schema for the `external_ref` property.

Property

Required/Optional

Type

Description

`id`

required

`string`

The `ID` of the entity within the external system

`type`

optional

`string`

An internal type for the entity in the external system, only needed if the ID is not globally unique

## The entity_details_requested event {#entity-details-requested-event}

This event is sent to your app when a user clicks a Work Objects unfurl or refreshes the flexpane.

```
{  "type": "entity_details_requested",  "user": "U0123456", // user who opened the flexpane  "external_ref": {    // `external_ref` that was set in the `metadata` of `chat.unfurl`.    // This is not guaranteed to be set in all cases. For example,    // when a work object is opened from an Enterprise Search result    // provided by a Slack-developed search provider, we cannot provide    // an `external_ref`.    "id": "123",    "type": "my-type" // optional  },  // This is the URL that identifies the entity in the developer's system. In the entity metadata, this property is called `url`.  "entity_url": "https://example.com/document/123",  "link": {    "url": "https://example.com/document/123",    "domain": "example.com" // domain of the URL  },  // This is the exact URL that was unfurled in the Slack message. It could be the same as `entity_url`, or different.  "app_unfurl_url": "https://example.com/document/123?myquery=param",  "event_ts": "123456789.1234566", // event timestamp  "trigger_id": "1234567890123.1234567890123.abcdef01234567890abcdef012345689", // event trigger ID  "user_locale": "en-US",  // These fields will not be provided when the entity details are opened  // from outside of a message context (i.e., Enterprise Search)   "channel": "C123ABC456", // ID of the channel where the source message was posted   "message_ts": "1755035323.759739", // timestamp of the source message  "thread_ts": "1755035323.759739", // timestamp of the root message, if the source message is part of a thread}
```

**The `user_locale` property**

When building the entity details you'll be passing to the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method, you'll want to make sure any strings for labels, statuses, select options, and so on are mapped to the user's locale in Slack. To help facilitate this, we provide an [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) (i.e., `en-US`, `en-GB`, `fr-FR`, etc.) in both the `link_shared` and `entity_details_requested` events. The full list of languages supported by Slack can be found [here](https://slack.com/help/articles/215058658-Manage-your-language-preferences).

### Flexpane content refresh {#flexpane-content-refresh}

The `entity_details_requested` event is always sent to your app in the following scenarios:

*   When a user opens a Work Object Unfurl for the first time.
*   When a user clicks on the on the refresh button in the flexpane.

![Flexpane refresh button](/assets/images/flexpane-refresh-button-25841b1adced04577a96273f4624a88e.png)

Assuming a Work Object flexpane was previously opened by a user, the content has a 10 minute refresh timer (TTL) before another event is sent to your app. After the 10 minutes has elapsed, the `entity_details_requested` event will be sent to your app in the following scenarios:

*   A user opens the Work Object flexpane for the 2nd, 3rd, or Xth time.
*   A user has the flexpane open and switches between the `Details` and `Conversations` tabs of the flexpane.
*   A user clicks on the flexpane refresh button.

Additionally, if a user has the flexpane open in their client, the refresh button will have a small red dot indicating that the data may be stale.

![Flexpane refresh button stale](/assets/images/flexpane-refresh-button-stale-7a93ed9db2617eef9a25d6630a5eea78.png)

If the 10 minute refresh timer has not elapsed, the `entity_details_requested` event will not be sent unless the user explicitly clicks the refresh button. The following scenarios do not trigger the event:

*   A user closing and re-opening the flexpane.
*   A user switching between the `Details` and `Conversations` tabs of the flexpane.
*   A user interacting with any other elements within the flexpane or Work Object.

## The entity.presentDetails API method {#entity-present-details-method}

For details, please refer to the [`entity.presentDetails`](/reference/methods/entity.presentDetails) API method.

For actions in the error object, see the action button [schema](#actions).

### Errors with partial views {#entity-details-error}

Some errors should be expected as part of standard authentication and access request flows. Slack will do this by default when you respond with `user_auth_required=true` or `error_status=restricted`. If you would like to do the same for a custom error, you can use the `custom_partial_view` error status.

```
{  "trigger_id": "1234567890123.1234567890123.abcdef01234567890abcdef012345689",  "error": {    "status": "custom_partial_view",    "custom_title": "Ruh roh",    "custom_message": ":hand: This item is *restricted* per our [company policy](https://example.com). Don't worry though, you can request access using the button below.",    "message_format": "markdown",    "actions": [      {        "text": "Request access",        "action_id": "request_access",        "value": "some_val",        "processing_state": {          "enabled": true // This can be enabled to disable the button and show a loading state for up to 30 seconds or until your app responds with another call to the `entity.presentDetails` API method.        }      }    ]  }}
```

![Custom partial access request](/assets/images/custom-partial-access-request-4d1570cf4bc480a75b83e09ec2bec029.png)

If you implement this with an action button, you can present a new error screen in response to the button using a payload as follows:

```
{  "trigger_id": "1234567890123.1234567890123.abcdef01234567890abcdef012345689",  "error": {    "status": "custom_partial_view",    "custom_title": "Access requested",    "custom_message": ":hourglass_flowing_sand: The team is reviewing your request. For urgent needs, see [this runbook](https://example.com).",    "message_format": "markdown"  }}
```

![Custom partial access request updated](/assets/images/custom-partial-access-request-2-2f71ae0449b01691719034f0b6d6532e.png)