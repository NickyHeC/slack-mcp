Source: https://docs.slack.dev/messaging/working-with-files

# Working with files

Working with files may seem daunting, but we're here to help! Think of files as [messages](/messaging) but with extra information included. Since files can represent information that is quite complex, an app that uses files well can communicate more precisely. In the following sections, we'll explore the two ways of working with files and their distinct differences.

[Uploading files](#upload) allows you to:

*   treat files like messages, and
*   upload files directly to and host files within Slack.

[Adding remote files](#remote) allows you to:

*   keep your files hosted wherever you please,
*   reference and unfurl files remotely, and
*   harness the power of the Remote Files API.

## Uploading files {#upload}

When you upload a file to Slack, Slack becomes the host for your file. Uploading files is the easiest way to manage files in Slack.

### App setup {#setup_file_uploads}

In order to upload a file to Slack, there are some [scopes](/reference/scopes) your app should have, as well as some [events](/reference/events) you may want your app to subscribe to.

### Scopes {#upload_scopes}

Within the **Apps** page, select **OAuth & Permissions** to choose your scopes:

*   The [`files:read`](/reference/scopes/files.read) scope allows access to API methods that read files: [`files.info`](/reference/methods/files.info) and [`files.list`](/reference/methods/files.list).
*   The [`files:write`](/reference/scopes/files.write) scope allows your app to upload files. It also allows your app to [remove](/reference/methods/files.remote.remove) files.

### Events {#upload_events}

To subscribe to file events, navigate to the **Event Subscriptions** tab within your **Apps** page. The file events you may subscribe to are as follows:

*   [`file_change`](/reference/events/file_change): A file was changed.
*   [`file_created`](/reference/events/file_created): A file was created.
*   [`file_deleted`](/reference/events/file_deleted): A file was deleted.
*   [`file_public`](/reference/events/file_public): A file was made public.
*   [`file_shared`](/reference/events/file_shared): A file was shared.
*   [`file_unshared`](/reference/events/file_unshared): A file was unshared.

### Steps for uploading files {#uploading_files}

When a user uploads a file, Slack will scan the file for malware before making it available in the workspace. This means the bigger the file, the longer the scan may take. As such, we've broken down the uploading process into the following steps.

### Call the files.getUploadURLExternal API method {#upload-step-1}

The response will contain a URL to which you can then post the contents of your file.

An example request can look like this:

```
curl --location 'https://slack.com/api/files.getUploadURLExternal' \--header 'Authorization: Bearer {token}' \--form 'filename="hello.txt"' \--form 'length="12"'
```

Required parameters are as follows:

*   `filename`: the name of the file being uploaded
*   `length`: the size (in bytes) of the file being uploaded

An example response can look like this:

```
{    "ok": true,    "upload_url": "https://files.slack.com/upload/v1/abcdefghi",    "file_id": "F012AB3CDE4"}
```

### Post the contents of your file to the URL returned by the files.getUploadURLExternal API method {#upload-step-2}

An example request can look like this:

```
curl --location 'https://files.slack.com/upload/v1/abcdefghi' \--header 'Content-Type: application/octet-stream' \--data-binary '@postman-cloud:///1f0a8ecf-f6c9-4620-9684-b3b7d0cb0ff0'
```

Check the HTTP status code to verify the file’s successful upload. An example response can look like this:

```
OK - 12
```

### Call the files.completeUploadExternal API method {#upload-step-3}

An example request can look like this:

```
curl --location 'https://slack.com/api/files.completeUploadExternal' \--header 'Authorization: Bearer {token}' \--form 'files="[{\"title\":\"Hello file\", \"id\":\"F012AB3CDE4\"}]"' \--form 'channel_id="C0123AB4CDE"' \--form 'initial_comment="Hello file"'
```

Required parameters are as follows:

*   `files`: an array of file IDs and their corresponding (optional) titles.
*   For posting the file:
    *   `channel_id`: the channel ID where the file will be shared. If not specified, the file will only be uploaded, i.e., hosted in Slack - the file will therefore be private, as it is not actually shared anywhere.
    *   `channels`: whether the file has to be shared in multiple channels (comma-separated string of channel IDs).
    *   `initial_comment`: the message text introducing the file in a specified channel.

Once your upload succeeds, you'll see an HTTP response from Slack containing an `"ok": true` field, plus a `files` array containing [`file` objects](/reference/objects/file-object). For more detail on file objects and the fields contained inside, refer to the [file object](/reference/objects/file-object) page.

An example response can look like this:

```
{    "ok": true,    "files": [        {            "id": "F012AB3CDE4",            "created": 1760688042,            "timestamp": 1760688042,            "name": "hello.txt",            "title": "Hello file",            "mimetype": "text/plain",            "filetype": "text",            "pretty_type": "Plain Text",            "user": "U012A3456BC",            "user_team": "E0123ABCDEF",            "editable": true,            "size": 12,            "mode": "snippet",            "is_external": false,            "external_type": "",            "is_public": true,            "public_url_shared": false,            "display_as_bot": false,            "username": "",            "url_private": "https://files.slack.com/files-pri/T0123ABCD4E-FF012AB3CDE4/hello.txt",            "url_private_download": "https://files.slack.com/files-pri/T0123ABCD4E-F012AB3CDE4/download/hello.txt",            "permalink": "https://aretia.enterprise.dev.slack.com/files/U012R6127MZ/F012AB3CDE4/hello.txt",            "permalink_public": "https://slack-files.com/T0123ABCD4E-F012AB3CDE4-8627274cfa",            "edit_link": "https://aretia.enterprise.slack.com/files/U012R6127MZ/F012AB3CDE4/hello.txt/edit",            "preview": "Hello txt",            "preview_highlight": "<div class=\"CodeMirror cm-s-default CodeMirrorServer\">\n<div class=\"CodeMirror-code\">\n<div><pre>Hello txt</pre></div>\n</div>\n</div>\n",            "lines": 1,            "lines_more": 0,            "preview_is_truncated": false,            "comments_count": 0,            "is_starred": false,            "shares": {                "public": {                    "C0123AB4CDE": [                        {                            "reply_users": [],                            "reply_users_count": 0,                            "reply_count": 0,                            "ts": "1760688662.900279",                            "channel_name": "general",                            "team_id": "T0123ABCD4E",                            "share_user_id": "U012A3456BC",                            "source": "UNKNOWN",                            "is_silent_share": false                        }                    ]                }            },            "channels": [                "C0123AB4CDE"            ],            "groups": [],            "ims": [],            "has_more_shares": false,            "has_rich_preview": false,            "file_access": "visible"        }    ]}
```

* * *

### Slack SDKs {#sdks}

Life is easier with a [Slack SDK](/tools). In particular, there are helpful `uploadV2` methods available in our node.js, Python, and Java SDKs that wrap the above steps into a single method. You can also use the `Slack file object` to host files in Slack using [Block Kit](/block-kit/). Refer to the [Slack file object](/reference/block-kit/composition-objects/slack-file-object) section for more details.

* * *

## Other API methods for working with files {#other_methods}

Slack provides some other API methods for working with files:

*   [`files.delete`](/reference/methods/files.delete): delete a file.
*   [`files.info`](/reference/methods/files.info): get information on a file.
*   [`files.list`](/reference/methods/files.list): list visible files.
*   [`files.revokePublicURL`](/reference/methods/files.revokePublicURL): disable a file for public sharing.
*   [`files.sharedPublicURL`](/reference/methods/files.sharedPublicURL): enable a file for public sharing.

* * *

## Responding to files {#responding_to_files}

Slack also sends [events](/apis/events-api/) when files are uploaded or changed in your workspace. Here are some of the relevant events:

*   [`file_change`](/reference/events/file_change): A file was changed.
*   [`file_created`](/reference/events/file_created): A file was created.
*   [`file_deleted`](/reference/events/file_deleted): A file was deleted.
*   [`file_public`](/reference/events/file_public): A file was made public.
*   [`file_shared`](/reference/events/file_shared): A file was shared.
*   [`file_unshared`](/reference/events/file_unshared): A file was unshared.

* * *

## Adding remote files {#remote}

Remote files are files _not_ hosted inside Slack. Think of a remote file as a pointer, a forwarding address, or a reference to a file that lives elsewhere.

**For most apps, uploading files directly to Slack is preferred over adding remote files**. Adding remote files involves extra steps that may not be necessary for your use case.

### Why use remote files? {#why}

There are a few benefits to adding and sharing remote files to Slack:

*   If your file can't be hosted in Slack for property rights reasons, remote files are here to save the day.
*   If you wish to provide a rich, custom unfurl experience for your files when their links are shared, remote files bring forth fantastical unfurls for the low low price of a JSON object.
*   If you want to control the way your file appears in Slack searches so that others can find it later, remote files allow for customized `indexable content`. That way, you can ensure your file appears when users search for certain terms.

Terminology

Remote files are "added" to Slack, not "uploaded." Adding a remote file to Slack makes Slack aware of its existence. Once that's done, "sharing" a remote file, like sharing a direct upload file, brings the file into a conversation. So a remote file must be "added" before it is "shared".

You can [add](/reference/methods/files.remote.add), [update](/reference/methods/files.remote.update), [remove](/reference/methods/files.remote.remove), [share](/reference/methods/files.remote.share), and [unfurl](/reference/methods/chat.unfurl) remote files in Slack.

### App setup {#setup_remote_files}

In order to add a remote file to Slack, there are a couple of scopes your app should have. There are also some events you may want your app to subscribe to.

### Scopes {#remote_files_scopes}

Working with remote files requires a distinct set of scopes from those involved in direct upload. Again, under the **Apps** page of your app, choose the **OAuth & Permissions** sidebar to select scopes.

*   [`remote_files:read`](/reference/scopes/remote_files.read) allows your app to read information about remote files visible to the user associated with your user token.
*   [`remote_files:share`](/reference/scopes/remote_files.share) allows your app to share remote files visible to the user associated with your user token.
*   [`remote_files:write`](/reference/scopes/remote_files.write) allows your app to add, edit, or delete remote files on a user's behalf.
*   [`chat:write`](/reference/scopes/chat.write) allows your app to post messages in approved channels & conversations. This is especially useful for an app that provides a custom unfurl for remote files.
*   [`links:read`](/reference/scopes/links.read) allows your app to view and subscribe to events about links that have been shared in conversation. Again, this is useful for knowing when a link to your remote file has been shared, so that you can unfurl it.
*   [`links:write`](/reference/scopes/links.write) allows your app to unfurl links (like to remote files) using the [`chat.unfurl`](/reference/methods/chat.unfurl) API method.

Once you've obtained the necessary scopes, you can [add](/reference/methods/files.remote.add), [update](/reference/methods/files.remote.update), [remove](/reference/methods/files.remote.remove), [share](/reference/methods/files.remote.share), and [unfurl](/reference/methods/chat.unfurl) remote files in Slack.

### Events {#remote_files_events}

To subscribe to any file events, use the **Event Subscriptions** tab under your **Apps** page. One event that can be especially useful to apps that work with remote files is the [`link_shared`](/reference/events/link_shared) event, which notifies your app when a link has been shared so that you can unfurl it. Add any App Unfurl Domains that relate to your file service under that same tab in the **Apps** page.

Once you've obtained the necessary scopes and subscribed to any desired events, you can [add](/reference/methods/files.remote.add), [update](/reference/methods/files.remote.update), [remove](/reference/methods/files.remote.remove), [share](/reference/methods/files.remote.share), and [unfurl](/reference/methods/chat.unfurl) remote files in Slack.

### Steps for adding remote files {#adding}

To add a remote file, use the [`files.remote.add`](/reference/methods/files.remote.add) API method.

Remote files exist across the whole workspace (or organization, for Enterprise organizations).

Here's a sample call:

```
curl -F token=<token> \    -F external_id=ABCD1 \    -F external_url=https://mydocuments.com/document/d/1TA9fIaph4eSz2fC_1JGMuYaYUc4IvieIop0WqfCXw5Y/edit?usp=sharing \    -F title=LeadvilleAndBackAgain \    -F preview_image=@cycling.jpg  \    -F indexable_file_contents=search_terms.txt    https://slack.com/api/files.remote.add
```

Pay particular attention to the `preview_image` parameter. `preview_image` should be a binary image file, and it will be stored in Slack. That's going to allow a more beautiful unfurl in the next step, when the app actually shares the remote file.

`indexable_file_contents` also deserves a mention. Use this parameter to specify a file containing the search terms that correspond to this remote file. When a user searches in Slack, their query will be compared against the contents of this text file for matching.

Think of this text file like the `alt` parameter on an HTML `<img>` tag — a textual representation of a non-textual object. The text file can contain a description of the remote file, or it can contain search keywords, or anything else text-based.

Once your upload succeeds, you'll see an HTTP response from Slack containing an `"ok": true` field, plus a [`file` object](/reference/objects/file-object). For more detail on file objects and the fields contained inside, a look at the [file object documentation](/reference/objects/file-object) is highly recommended.

You'll see the `external_id` returned to you on the `file` object in the Slack response, as well as a `file_id`. Either of these ids can be stored and used to query the [`files.remote.info`](/reference/methods/files.remote.info) API method to access other information about the file.

### Sharing remote files {#sharing}

Adding is nice, but sharing is caring.

In other words, adding a remote file _does not_, by itself, share the file to a conversation. Without sharing the file, it remains an orphan inside Slack - you can view information on it via [`files.remote.info`](/reference/methods/files.remote.info) API method, but it won't actually be visible anywhere. Let's make it visible with a call to the [`files.remote.share`](/reference/methods/files.remote.share) API method.

```
curl -F token=<token> \    -F external_id=ABCD1 \    -F channels=C12345 \    https://slack.com/api/files.remote.share
```

Now we get a lovely message in channel that shows off the remote file as it should be seen.

Now we have a custom `preview_image`, which we specified during the [`add`](#adding) step, instead of the ugly raw URL and a small picture of text.

A word about tokens: the [`files.remote.share`](/reference/methods/files.remote.share) API method may be called with _either_ a [bot](/authentication/tokens#bot) or a [user](/authentication/tokens#user) token. The bot token shares the file from your app, while the user token shares the file from the user associated with your user token. Use the bot token to share to channels that the bot has access to; use the user token to share to channels that the user has access to.

### Unfurling remote files {#unfurling}

We've already mentioned how to [add a custom `preview_image`](#adding) that makes our remote files appear nicer when they're shared. But what about when someone else shares our remote file as a link?

There are a few ways to do this. First, you can provide a rich, interactive unfurl experience by implementing [Work Objects](/messaging/work-objects-overview) within your app.

You can also provide unfurls with the [`link_shared`](/reference/events/link_shared) event. When the `link_shared` event fires, you'll receive its payload, including the `message_ts` of the message that triggered it, as well as the `channel` of that message. Then you can make an HTTP request to the [chat.unfurl](/reference/methods/chat.unfurl) API method. To do this, set up the `unfurls` object using a [block](/messaging#complex_layouts):

```
unfurls: {        'https://mydocuments.com/document/d/1TA9fIaph4eSz2fC_1JGMuYaYUc4IvieIop0WqfCXw5Y/edit?usp=sharing': {          hide_color: true,          blocks: [{            type: 'file',            external_id: 'ABCD1',            source: 'remote',          }]        }      }
```

For use specifically with a file unfurl, you can set the `hide_color` field to `true` to remove the color bar from a message. This property works only with a file block; if this property is included along with other blocks (for example, a section block), the [`chat.unfurl`](/reference/methods/chat.unfurl) API method will throw an error. Then, call the [`chat.unfurl`](/reference/methods/chat.unfurl) API method with the `channel` from the `link_shared` event, and set the `ts` equal to the `message_ts` from the event:

```
curl -F token=<user_token> \    -F ts=123456789.9875 \    -F unfurls=<unfurls json from above> \    -F channel=C12345 \    -F user_auth_required=false \    https://slack.com/api/chat.unfurl
```

### Updating remote files {#updating}

Your remote file's contents may change. When that happens, call the [`files.remote.update`](/reference/methods/files.remote.update) API method to update your remote file:

```
curl -F token=<token> \    -F tile=ACyclistTale \    -F external_id=ABCD1 \    https://slack.com/api/files.remote.update
```

You _cannot_ update the `external_id` or `file_id` of a remote file. If you need to change those fields, your best bet is to [remove](#removing) and then [add](#adding) the file.

One other piece of pleasant news: [adding](#adding) a remote file is actually an "upsert" operation, meaning that if you add a file that has been added before, the existing file will be updated.

### Removing remote files {#removing}

Removing a remote file follows the same pattern as [adding](#adding) and [updating](#updating). Use the [`files.remote.remove`](/reference/methods/files.remote.remove) API method to remove a remote file from Slack.

This API method does _not_ delete the remote file from where it's externally hosted; it only removes the remote file from Slack.

```
    curl -F token=<bot_token> \    -F external_id=ABCD1 \    https://slack.com/api/files.remote.remove
```

After removal, any place that used to display the file will show a tombstone message containing the text "This file was deleted." instead.