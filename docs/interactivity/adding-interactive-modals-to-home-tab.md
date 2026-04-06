Source: https://docs.slack.dev/interactivity/adding-interactive-modals-to-home-tab

# Adding interactive modals to the Home tab

To demonstrate what you can do with App Home, we'll take a look at an app called _Stickies_, which allows users to store short, private notes within the App Home. The user and app flows are described below.

The _Stickies_ app is no longer maintained.

We've kept this page up as it maintains useful instruction and code snippets!

## User flow {#user_flow}

1.  A user clicks the name of the app under **Apps** within their Slack client (the Home tab should be opened by default).
2.  The user can add a new note by clicking the button in the pane.
3.  The user fills out the form in a modal window, then clicks **Create**.
4.  The Home tab is automatically updated with the new note entry.

## App flow {#app_home}

1.  When a user opens the App Home, the `app_home_opened` event gets triggered and sent to the app server.
2.  The app uses the user ID from the event payload to display the initial view with a button using the [`views.publish`](/reference/methods/views.publish) API method.
3.  When the user clicks **Add a Stickie**, an interaction is triggered.
4.  The app opens a modal with form inputs using the [`views.open`](/reference/methods/views.open) API method.
5.  Once the user submits the form, another interaction is triggered with a type of `view_submission`.
6.  The App Home is updated using the [`views.publish`](/reference/methods/views.publish) API method.

![Diagram](/assets/images/app_diagram-9b3d376ea4d9227237eb453fe102a5fe.png)

This guide uses `Node.js` with [Express](https://expressjs.com/) as the web server. All API calls are made with straightforward HTTP requests and responses. Hopefully, the code is readily comprehensible for any language you use.

## Triggering the app_home_opened event {#triggering_app_home}

Use an HTTP POST method route to create an endpoint to receive the event payload. This is where Slack API server sends you a JSON payload when an event is fired. Once you receive the data, check whether the event type is `app_home_opened`, then prepare to display the App Home view.

![Slack diagram](/assets/images/app_diagram_app_home_opend-5023353c351a66deb0a78755fd29282b.png)

Here is the code snippet from `index.js`:

```
app.post('/slack/events', async(req, res) => {  switch (req.body.type) {    case 'url_verification': {      // verify Events API endpoint by returning challenge if present      res.send({ challenge: req.body.challenge });      break;    }    case 'event_callback': {      // Verify the signing secret      if (!signature.isVerified(req)) {        res.sendStatus(404);        return;      }       // Request is verified --      else {        const {type, user, channel, tab, text, subtype} = req.body.event;        // Triggered when the App Home is opened by a user        if(type === 'app_home_opened') {          // Display App Home          appHome.displayHome(user);        }
```

Let’s display a rich content in App Home view with rich message layout, [Block Kit](/block-kit):

```
const displayHome = async(user, data) => {  const args = {    token: process.env.SLACK_BOT_TOKEN,    user_id: user,    view: await updateView(user)  };  const result = await axios.post('/views.publish', qs.stringify(args));};
```

To display content in the App Home, call the `view.publish` API method. In this example, we'll use the `axios` module to handle the API calls via HTTP POST.

## Constructing the view with Block Kit {#view_construction}

We'll call another function to create JSON to construct the view to be displayed. This function can be reused when you update the view when new content is added later. This code snippet shows how to build and display the initial view:

```
const updateView = async(user) => {    let blocks = [     {      // Section with text and a button      type: "section",      text: {        type: "mrkdwn",        text: "*Welcome!* \nThis is a home for Stickers app. You can add small notes here!"      },      accessory: {        type: "button",        action_id: "add_note",         text: {          type: "plain_text",          text: "Add a Stickie"        }      }    },    // Horizontal divider line     {      type: "divider"    }  ];  let view = {    type: 'home',    title: {      type: 'plain_text',      text: 'Keep notes!'    },    blocks: blocks  }  return JSON.stringify(view);};
```

The `blocks` array defined in the code snippet above is [prototyped with Block Kit Builder](https://api.slack.com/tools/block-kit-builder?mode=appHome&view=%7B%22type%22%3A%22home%22%2C%22blocks%22%3A%5B%7B%22type%22%3A%22section%22%2C%22text%22%3A%7B%22type%22%3A%22mrkdwn%22%2C%22text%22%3A%22*Welcome!*%20%5CnThis%20is%20a%20home%20for%20Stickers%20app.%20You%20can%20add%20small%20notes%20here!%22%7D%2C%22accessory%22%3A%7B%22type%22%3A%22button%22%2C%22action_id%22%3A%22add_note%22%2C%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Add%20a%20Stickie%22%7D%7D%7D%2C%7B%22type%22%3A%22divider%22%7D%5D%7D).

In the actual source code, the function is dynamic, and it takes additional content from the interactive button and modal.

## Handling user interaction {#button_clicks}

Once a user clicks the button, a modal opens.

![Slack diagram](/assets/images/app_diagram_button_click-f99caa1e336fb9c6070e280a697384ab.png)

Notice that the `action_id` is specified in the message building block. Use the identifier to retrieve the data we need. Once a user clicks the button, the API server sends your Request URL a payload for the user action, which contains a `trigger_id`. You'll need this to open a modal.

```
app.post('/slack/actions', async(req, res) => {  const { token, trigger_id, user, actions, type } = JSON.parse(req.body.payload);  if(actions && actions[0].action_id.match(/add_/)) {    openModal(trigger_id);  } });
```

## Opening a modal {#opening_modal}

This is how you create form elements (input box and a drop-down menu with a submit button) in a modal view. For this example, we'll make a form with a multi-line text input and a pick-a-color dropdown.

To open the modal, call the `views.open` API method:

```
const openModal = async(trigger_id) => {  const modal = {    type: 'modal',    title: {      type: 'plain_text',      text: 'Create a stickie note'    },    submit: {      type: 'plain_text',      text: 'Create'    },    blocks: [      // Text input      {        "type": "input",        "block_id": "note01",        "label": {          "type": "plain_text",          "text": "Note"        },        "element": {          "action_id": "content",          "type": "plain_text_input",          "placeholder": {            "type": "plain_text",            "text": "Take a note... "          },          "multiline": true        }      },      // Drop-down menu      {        "type": "input",        "block_id": "note02",        "label": {          "type": "plain_text",          "text": "Color",        },        "element": {          "type": "static_select",          "action_id": "color",          "options": [            {              "text": {                "type": "plain_text",                "text": "yellow"              },              "value": "yellow"            },            {              "text": {                "type": "plain_text",                "text": "blue"              },              "value": "blue"            }          ]        }      }    ]  };  const args = {    token: process.env.SLACK_BOT_TOKEN,    trigger_id: trigger_id,    view: JSON.stringify(modal)  };    const result = await axios.post('https://slack.com/api/views.open', qs.stringify(args));};
```

The code snippet seems long, but as you can see, it's mostly just constructing a JSON for the form UI. See how it's built on [Block Kit Builder](https://api.slack.com/tools/block-kit-builder?mode=modal&view=%7B%22type%22%3A%22modal%22%2C%22title%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Create%20a%20stickie%20note%22%2C%22emoji%22%3Atrue%7D%2C%22submit%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Create%22%2C%22emoji%22%3Atrue%7D%2C%22blocks%22%3A%5B%7B%22type%22%3A%22input%22%2C%22block_id%22%3A%22note01%22%2C%22element%22%3A%7B%22type%22%3A%22plain_text_input%22%2C%22placeholder%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Take%20a%20note...%20%22%7D%2C%22multiline%22%3Atrue%7D%2C%22label%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Note%22%7D%7D%2C%7B%22type%22%3A%22input%22%2C%22element%22%3A%7B%22type%22%3A%22static_select%22%2C%22action_id%22%3A%22color%22%2C%22options%22%3A%5B%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22yellow%22%7D%2C%22value%22%3A%22yellow%22%7D%2C%7B%22text%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22blue%22%7D%2C%22value%22%3A%22blue%22%7D%5D%7D%2C%22label%22%3A%7B%22type%22%3A%22plain_text%22%2C%22text%22%3A%22Color%22%7D%7D%5D%7D).

## Handling the form submission {#handling_submission}

The submission from a user is handled in the same way the button click from the Home tab was handled.

![Slack diagram](/assets/images/app_diagram_modal_submit-9be5e6bd757b2da8bcc0fddf2b006eda.png)

When the form in the modal is submitted, a payload is sent to the same endpoint of the action. You can differentiate the submission by checking the `type` in the payload data. The full code snippet from the `index.js` file is below:

```
app.post('/slack/actions', async(req, res) => {  //console.log(JSON.parse(req.body.payload));  const { token, trigger_id, user, actions, type } = JSON.parse(req.body.payload);  // Button with "add_" action_id clicked --  if(actions && actions[0].action_id.match(/add_/)) {    // Open a modal window with forms to be submitted by a user    appHome.openModal(trigger_id);  }   // Modal forms submitted --  else if(type === 'view_submission') {    res.send(''); // Make sure to respond to the server to avoid an error    const ts = new Date();    const { user, view } = JSON.parse(req.body.payload);    const data = {      timestamp: ts.toLocaleString(),      note: view.state.values.note01.content.value,      color: view.state.values.note02.color.selected_option.value    }    appHome.displayHome(user.id, data);  }});
```

## Updating the App Home view {#updating_app_home}

Append the newly acquired data from the user to the current view block, and re-render the Home tab view using the [`views.publish`](/reference/methods/views.publish) API method.

In this example, we're using a persistent database with the [`node-json-db`](https://www.npmjs.com/package/node-json-db) module. Each time a user adds a new note, the data is pushed to the data array. We'll create a new data block in JSON, then append it to the existing JSON, and finally display the new view by calling the `views.publish` API method.

You can see the source code in the `appHome.js` file below:

```
const updateView = async(user) => {  // Intro message -   let blocks = [     {      type: "section",      text: {        type: "mrkdwn",        text: "Hello! Make a note of things you don't want to forget."      },      accessory: {        type: "button",        action_id: "add_note",         text: {          type: "plain_text",          text: "Add sticky note",          emoji: true        }      }    },    {      type: "divider"    }  ];  // Append new data blocks after the intro -   let newData = [];  try {    const rawData = db.getData(`/${user}/data/`);    newData = rawData.slice().reverse(); // Reverse to make the latest first    newData = newData.slice(0, 50); // Just display 20. Block Kit display has some limit.  } catch(error) {    //console.error(error);   };  if(newData) {    let noteBlocks = [];    for (const o of newData) {      const color = (o.color) ? o.color : 'yellow';      let note = o.note;      if (note.length > 3000) {        note = note.substr(0, 2980) + '... _(truncated)_'        console.log(note.length);      }      noteBlocks = [        {          type: "section",          text: {            type: "mrkdwn",            text: note          },          accessory: {            type: "image",            image_url: `https://example.com/example.png`,            alt_text: "stickie note"          }        },        {          "type": "context",          "elements": [            {              "type": "mrkdwn",              "text": o.timestamp            }          ]        },        {          type: "divider"        }      ];      blocks = blocks.concat(noteBlocks);    }  }  // The final view -  let view = {    type: 'home',    title: {      type: 'plain_text',      text: 'Keep notes!'    },    blocks: blocks  }  return JSON.stringify(view);};/* Display App Home */const displayHome = async(user, data) => {  if(data) {         // Store in a local DB    db.push(`/${user}/data[]`, data, true);     }  const args = {    token: process.env.SLACK_BOT_TOKEN,    user_id: user,    view: await updateView(user)  };  const result = await axios.post(`${apiUrl}/views.publish`, qs.stringify(args));  try {    if(result.data.error) {      console.log(result.data.error);    }  } catch(e) {    console.log(e);  }};
```