Source: https://docs.slack.dev/reference/objects/file-object

# File object

A file object contains information about a file shared with a workspace.

```
{    "id": "F0A12BCDE",    "created": 1531763342,    "timestamp": 1531763342,    "name": "tedair.gif",    "title": "tedair.gif",    "mimetype": "image/gif",    "filetype": "gif",    "pretty_type": "GIF",    "user": "U012A3BCD",    "editable": false,    "size": 137531,    "mode": "hosted",    "is_external": false,    "external_type": "",    "is_public": true,    "public_url_shared": false,    "display_as_bot": false,    "username": "",    "url_private": "https://.../tedair.gif",    "url_private_download": "https://.../tedair.gif",    "thumb_64": "https://.../tedair_64.png",    "thumb_80": "https://.../tedair_80.png",    "thumb_360": "https://.../tedair_360.png",    "thumb_360_w": 176,    "thumb_360_h": 226,    "thumb_160": "https://.../tedair_=_160.png",    "thumb_360_gif": "https://.../tedair_360.gif",    "image_exif_rotation": 1,    "original_w": 176,    "original_h": 226,    "deanimate_gif": "https://.../tedair_deanimate_gif.png",    "pjpeg": "https://.../tedair_pjpeg.jpg",    "permalink": "https://.../tedair.gif",    "permalink_public": "https://.../...",    "comments_count": 0,    "is_starred": false,    "shares": {        "public": {            "C0A1BC2DE": [                {                    "reply_users": [                        "U012A3BCD"                    ],                    "reply_users_count": 1,                    "reply_count": 1,                    "ts": "1531763348.000001",                    "thread_ts": "1531763273.000015",                    "latest_reply": "1531763348.000001",                    "channel_name": "file-under",                    "team_id": "T012AB3C4"                }            ]        }    },    "channels": [        "C0A1BC2DE"    ],    "groups": [],    "ims": [],    "has_rich_preview": false}
```

## Properties {#fields}

Field

Type

Description

`id`

string

The ID of the file object.

`created`

Unix timestamp

A Unix timestamp representing when the file was created.

`timestamp`

Unix timestamp

A **deprecated** property that is provided only for backwards compatibility with older clients.

`name`

string

Name of the file; may be `null` for unnamed files.

`title`

string

Title of the file.

`mimetype`

string

The file's mimetype.

`filetype`

string

The file's type. Note the `mimetype` and `filetype` properties do not have a 1-to-1 mapping, as multiple different files types ('html', 'js', etc.) share the same mime type.

`pretty_type`

string

A human-readable version of the type.

`user`

string

The ID of the user who created the object.

`editable`

boolean

Indicates whether files are stored in editable mode.

`size`

integer

The filesize in bytes. Snippets are limited to a maximum file size of 1 megabyte.

`mode`

string

One of the following: `hosted`, `external`, `snippet` or `post`.

`is_external`

boolean

Indicates whether or not the master copy of a file is stored within the system. If `is_external` is true, the `url` property will point to the externally-hosted master file.

`external_type`

string

Indicates what kind of external file it is, e.g., `dropbox` or `gdoc`.

`is_public`

boolean

Will be `true` if the file is public.

`public_url_shared`

boolean

Will be `true` if the file's public URL has been shared.

`updated`

Unix timestamp

For Post filetypes only; a Unix timestamp of when the Post was last edited.

`channels`

array

Contains the IDs of any channels with which the file is currently shared.

`groups`

array

Contains the IDs of any private groups with which the file is currently shared. Groups are only returned if the caller is a member of that group.

`ims`

array

Contains the IDs of any direct message channels with which the file is currently shared. Messages are only returned if the caller is a member of that channel.

`num_stars`

integer

Contains the number of users who have starred this file. Will not be present if no users have starred it.

`is_starred`

boolean

Will be `true` if the calling user has starred the file, else it will be omitted.

`pinned_to`

array

Contains the IDs of any channels in which the file is currently pinned.

`reactions`

object

Contains any reactions that have been added to the file. Gives information about the type of reaction, the total number of users who added that reaction, and a (possibly incomplete) list of users who have added that reaction to the file. The users array in the `reactions` property may not always contain all users that have reacted (we limit it to X users, and X might change); however, `count` will always represent the count of all users who made that reaction (i.e., it may be greater than `users.length`). If the authenticated user has a given reaction then they are guaranteed to appear in the `users` array regardless of whether `count` is greater than `users.length` or not.

`initial_comment`

string

A comment from the file uploader. Will only be set when the uploader commented on the file at the time of upload. Clients can use this to display the comment with the file when announcing new file uploads. Use `comments_count` to determine how many comments are attached to a file.

Depending on the file's `type`, you may encounter different fields relevant to that type. For instance, you may encounter fields such as `image_exif_rotation`, `original_w`, and `original_h` for images, but will not find those fields for HTML documents.

### Lists-related properties {#list_fields}

When the file is a List (meaning that the `filetype` has a value of `list`), there will be additional fields in the response for this API.

```
{    ...    "filetype": "list",    "list_metadata": {        "icon": "",        "description": "",        "description_blocks": [            {                "type": "rich_text",                "block_id": "k\/5jH",                "elements": [                    {                        "type": "rich_text_section",                        "elements": [                            {                                "type": "text",                                "text": "My list description"                            }                        ]                    }                ]            }        ],        "creation_source": {            "type": "blank"        },        "is_trial": false,        "schema": [            {                "id": "Col0181CWE8KC",                "name": "Task",                "key": "name",                "type": "text",                "is_primary_column": true,                "options": {                    "format": "text"                }            },            {                "id": "Col00",                "name": "Completed",                "key": "todo_completed",                "type": "todo_completed",                "is_primary_column": false            },            {                "id": "Col01",                "name": "Assignee",                "key": "todo_assignee",                "type": "todo_assignee",                "is_primary_column": false            },            {                "id": "Col02",                "name": "Due Date",                "key": "todo_due_date",                "type": "todo_due_date",                "is_primary_column": false            },            {                "id": "Col01831YFLG3",                "name": "Notes",                "key": "Col01831YFLFM",                "type": "text",                "is_primary_column": false,                "options": {                    "format": "text"                }            }        ],        "subtask_schema": [            {                "id": "Col0181CWE8KC",                "name": "Task",                "key": "name",                "type": "text",                "is_primary_column": true,                "options": {                    "format": "text"                }            },            {                "id": "Col00",                "name": "Completed",                "key": "todo_completed",                "type": "todo_completed",                "is_primary_column": false            },            {                "id": "Col01",                "name": "Assignee",                "key": "todo_assignee",                "type": "todo_assignee",                "is_primary_column": false,                "options": {                    "format": "multi_entity",                    "default_value": null,                    "show_member_name": true                }            },            {                "id": "Col02",                "name": "Due Date",                "key": "todo_due_date",                "type": "todo_due_date",                "is_primary_column": false            }        ],        "views": [            {                "id": "View0181CWE8KU",                "name": "All items",                "type": "table",                "is_locked": false,                "position": "1731452687",                "columns": [                    {                        "visible": true,                        "key": "name",                        "id": "Col0181CWE8KC",                        "position": "5000000000"                    },                    {                        "visible": true,                        "key": "todo_completed",                        "id": "Col00",                        "position": "5000000001"                    },                    {                        "visible": true,                        "key": "todo_assignee",                        "id": "Col01",                        "position": "5000000002"                    },                    {                        "visible": true,                        "key": "todo_due_date",                        "id": "Col02",                        "position": "5000000003"                    },                    {                        "visible": true,                        "key": "Col01831YFLFM",                        "id": "Col01831YFLG3",                        "position": "5000000006"                    }                ],                "date_created": 1753729952,                "created_by": "U02178QA5BA",                "stick_column_left": false,                "is_all_items_view": true,                "default_view_key": "all_items",                "show_completed_items": true            }        ],        "integrations": [],        "todo_mode": true,        "default_view": "View0181CWE8KU"    },    "list_limits": {        "over_row_maximum": false,        "row_count_limit": 1000,        "row_count": 455,        "archived_row_count": 75,        "over_column_maximum": false,        "column_count": 2,        "column_count_limit": 30,        "over_view_maximum": false,        "view_count": 1,        "view_count_limit": 50,        "max_attachments_per_cell": 10    }}
```

Field

Type

Description

`list_metadata`

object

This field contains List information such as List schema, which includes all columns with header names of the List. This field also has List view information (all existing views for the given List) and subtasks schema (column information for subtasks). The header name for columns will be present in the `schema[].name` field, and List view names will be present in the `views[].name` field.

`list_limits`

object

The List count of the current amount of rows/items, columns, views, and archived items. It also has the limits for each entity, including the maximum amount of items a List can have. Task tracking field columns (`todo_completed`, `todo_due_date`, and `todo_assignee` type columns) don't count towards the `column_count` limit.

## Authentication {#authentication}

Authentication is required to retrieve file URLs.

The `url_private` property points to a URL with the file contents. Editable-mode files will also have a `url_private_download` parameter, which includes headers to force a browser download. Both `url_private` and `url_private_download` require an authorization header of the form:

Authorization: Bearer A\_VALID\_TOKEN

In this case, `A_VALID_TOKEN` is representative of a real OAuth token, bearing at least the `files:read` scope. [Learn more about OAuth Scopes](/authentication/installing-with-oauth).

Fields providing URLs that require this form of authentication include:

*   `url_private`
*   `url_private_download`
*   `thumb_64`
*   `thumb_80`
*   `thumb_160`
*   `thumb_360`
*   `thumb_480`
*   `thumb_720`
*   `thumb_960`
*   `thumb_1024`

The `url` and `url_download` parameters have been deprecated.

Please use `url_private` and `url_private_download` instead.

## Thumbnails {#thumbnails}

If a thumbnail is available for the file, the URL to a 64x64 pixel thumbnail will be returned as the `thumb_64` property.

The `thumb_80` property, when present, contains the URL of an 80x80 pixel thumbnail. Unlike the 64px thumbnail, this size is guaranteed to be 80x80, even when the source image was smaller (it is padded with transparent pixels).

A variable-sized thumbnail will be returned as `thumb_360`, with its longest size no bigger than 360 pixels(although it may be smaller depending on the source size). Dimensions for this thumb are returned in `thumb_360_w` and `thumb_360_h`. In the case where the original image was an animated gif with dimensions greater than 360 pixels, an animated thumbnail is also created and passed as `thumb_360_gif`.

Depending on the original file's size, you may even find a `thumb_480`, `thumb_720`, `thumb_960`, or `thumb_1024` property.

All thumbnails require an authorization header as described [above](#authentication).

## Permalinks {#permalinks}

The `permalink` URL points to a single page for the file containing details, comments, and a download link. If the file is available to the public, a `permalink_public` URL points to the public file itself.

The `edit_link` is only present for posts and snippets, and is the page at which the file can be edited.

## Previews {#previews}

For posts, a short plain-text `preview` is also included than can be shown in place of a thumbnail.

For snippets, a `preview` of the contents is included (a few truncated lines of plaintext), as well as a more complex syntax-highlighted preview (`preview_highlight`) in HTML. The total count of lines in the snippet is returned in `lines`, while `lines_more` contains a count of lines not shown in the preview.

## Slack Connect files {#slack_connect_files}

When a file is uploaded to a Slack Connect channel, [file object](/reference/objects/file-object) properties are not immediately accessible to apps listening via the Events API or the legacy RTM API. Instead, the payload will contain a file object with the key-value pair `"file_access": "check_file_info"` meaning that further action is required from your app in order to view an uploaded file's metadata.

```
{    ...    "files": [        {          "id": "F12345678",          "mode": "file_access",          "file_access": "check_file_info",          "created": 0,          "timestamp": 0,          "user": ""        }      ]    ...}
```

See the [Slack Connect](https://docs.slack.dev/apis/slack-connect/#check_file_info) overview page for more details on how to handle this scenario.

## File types {#types}

Possible `filetype` values include, but are not limited to, the following:

Type

Description

`auto`

Auto Detect Type

`text`

Plain Text

`ai`

Illustrator File

`apk`

APK

`applescript`

AppleScript

`binary`

Binary

`bmp`

Bitmap

`boxnote`

BoxNote

`c`

C

`csharp`

C#

`cpp`

C++

`css`

CSS

`csv`

CSV

`clojure`

Clojure

`coffeescript`

CoffeeScript

`cfm`

ColdFusion

`d`

D

`dart`

Dart

`diff`

Diff

`doc`

Word Document

`docx`

Word document

`dockerfile`

Docker

`dotx`

Word template

`eml`

Email

`eps`

EPS

`epub`

EPUB

`erlang`

Erlang

`fla`

Flash FLA

`flv`

Flash video

`fsharp`

F#

`fortran`

Fortran

`gdoc`

GDocs Document

`gdraw`

GDocs Drawing

`gif`

GIF

`go`

Go

`gpres`

GDocs Presentation

`groovy`

Groovy

`gsheet`

GDocs Spreadsheet

`gzip`

Gzip

`html`

HTML

`handlebars`

Handlebars

`haskell`

Haskell

`haxe`

Haxe

`indd`

InDesign Document

`java`

Java

`javascript`

JavaScript

`jpg`

JPEG

`json`

JSON

`keynote`

Keynote Document

`kotlin`

Kotlin

`latex`

LaTeX/sTeX

`lisp`

Lisp

`lua`

Lua

`m4a`

MPEG 4 audio

`markdown`

Markdown (raw)

`matlab`

MATLAB

`mhtml`

MHTML

`mkv`

Matroska video

`mov`

QuickTime video

`mp3`

mp4

`mp4`

MPEG 4 video

`mpg`

MPEG video

`mumps`

MUMPS

`numbers`

Numbers Document

`nzb`

NZB

`objc`

Objective-C

`ocaml`

OCaml

`odg`

OpenDocument Drawing

`odi`

OpenDocument Image

`odp`

OpenDocument Presentation

`ods`

OpenDocument Spreadsheet

`odt`

OpenDocument Text

`ogg`

Ogg Vorbis

`ogv`

Ogg video

`pages`

Pages Document

`pascal`

Pascal

`pdf`

PDF

`perl`

Perl

`php`

PHP

`pig`

Pig

`png`

PNG

`post`

Slack Post

`powershell`

PowerShell

`ppt`

PowerPoint presentation

`pptx`

PowerPoint presentation

`psd`

Photoshop Document

`puppet`

Puppet

`python`

Python

`qtz`

Quartz Composer Composition

`r`

R

`rtf`

Rich Text File

`ruby`

Ruby

`rust`

Rust

`sql`

SQL

`sass`

Sass

`scala`

Scala

`scheme`

Scheme

`sketch`

Sketch File

`shell`

Shell

`smalltalk`

Smalltalk

`svg`

SVG

`swf`

Flash SWF

`swift`

Swift

`tar`

Tarball

`tiff`

TIFF

`tsv`

TSV

`vb`

VB.NET

`vbscript`

VBScript

`vcard`

vCard

`velocity`

Velocity

`verilog`

Verilog

`wav`

Waveform audio

`webm`

WebM

`wmv`

Windows Media Video

`xls`

Excel spreadsheet

`xlsx`

Excel spreadsheet

`xlsb`

Excel Spreadsheet (Binary, Macro Enabled)

`xlsm`

Excel Spreadsheet (Macro Enabled)

`xltx`

Excel template

`xml`

XML

`yaml`

YAML

`zip`

Zip