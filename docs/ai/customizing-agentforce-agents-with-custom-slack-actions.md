Source: https://docs.slack.dev/ai/customizing-agentforce-agents-with-custom-slack-actions

# Customizing Agentforce agents with Slack actions

This guide will help you customize your Agentforce agent with custom Slack actions. Implementing custom Slack actions in your agent allows it to carry out certain tasks in Slack via the [Slack Web API](/apis/web-api), such as sending a message to a channel or creating a canvas with content from the agent's response. To use standard Slack actions in your agent, refer to the [Slack Agent Actions](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&type=5) documentation.

Prerequisites

This guide assumes you have a connected Salesforce org and Slack org, as well as an Agentforce agent that can be modified. If you don't, use the [Connect Salesforce and Slack guide](https://slack.com/help/articles/30754346665747-Connect-Salesforce-and-Slack) and the Salesforce [Create Agents](https://help.salesforce.com/s/articleView?id=ai.agent_setup_enable_default.htm&type=5) guide to get set up.

## Step 1: Set up your Slack app {#slack-app-setup}

In order to use the [Slack Web API](/apis/web-api) in custom actions in Agentforce, you first need to set up a way for your agents to get proper Slack credentials. You do this by creating a Slack app and using an `Auth. Provider` in the Salesforce Platform to manage the authentication flow between your Slack app and Salesforce users.

1.  Start by logging into your Slack org and create [a new app](https://api.slack.com/apps?new_app=1). In the **Create an app** modal, select **From a manifest**, then select a workspace in which to develop your app and click **Next**.
    
2.  Highlight the contents of the placeholder JSON and replace it with this:
    
    App manifest code
    
    ```
    {    "display_information": {        "name": "Agentforce Custom Actions"    },    "features": {        "bot_user": {            "display_name": "Agentforce Custom Actions",            "always_online": false        }    },    "oauth_config": {        "scopes": {            "bot": [                "chat:write",                "chat:write.public",                "mpim:read",                "reactions:write",                "channels:history",                "canvases:write",                "channels:join",                "channels:read",                "team:read"            ]        }    },    "settings": {        "org_deploy_enabled": true,        "socket_mode_enabled": false,        "token_rotation_enabled": false    }}
    ```
    
3.  Click **Next** then **Create**.
    
4.  Select **Install App** in the sidebar. Click **Install to Organization**. Allow the app access to the org.
    
5.  Select **Basic Information** in the sidebar. Copy down your Client ID and Client Secret; we'll use these later.
    

## Step 2: Create an Auth Provider {#auth}

To use your Slack app credentials in your agent, you need to first create an auth provider, allowing you to complete the authentication flow needed for the Salesforce Platform to get the proper credentials.

1.  Log into your Salesforce org and open `Setup` from the gear icon in the upper right. Use the Quick Find to search for `Auth. Providers`, click on it, then click the `New` button above the list of existing providers to create a new provider. Enter the values for the fields listed below.
    
    Field
    
    Value
    
    `Provider Type`
    
    `Open ID Connect`
    
    `Name`
    
    `Slack`
    
    `URL Suffix`
    
    Leave the value created by entering a `Name`
    
    `Consumer Key`
    
    `Client ID` of your Slack app
    
    `Consumer Secret`
    
    `Client Secret` of your Slack app
    
    `Authorize Endpoint URL`
    
    [https://slack.com/oauth/v2/authorize](https://slack.com/oauth/v2/authorize)
    
    `Token Endpoint URL`
    
    [https://slack.com/api/oauth.v2.access](https://slack.com/api/oauth.v2.access)
    
2.  Click **Save**.
    
3.  Scroll down the page and copy the `Callback URL`.
    
4.  Navigate back to your Slack app settings and add the callback URL to your app in the **OAuth & Permissions** settings page.
    
    *   In the **Redirect URLs** section, click **Add New Redirect URL**.
    *   Enter the callback URL from the auth provider, then click **Add**.
    *   Click **Save URLs**.

## Step 3: Create an External Credential {#external-credential}

Once you have an auth provider, it’s time to set up an external credential. External credentials are the actual record of credentials for external services. This is what stores your tokens and connects them to a Principal for use in permission sets or user profiles.

1.  Within your Salesforce org setup, search for and click on `Named Credentials`; then within the settings click the `External Credentials` tab, then click the `New` button located above the list of external credentials. Enter the following values for the fields listed below:
    
    Field
    
    Value
    
    `Label`
    
    `Slack`
    
    `Name`
    
    `Slack`
    
    `Authentication Protocol`
    
    `OAuth 2.0`
    
    `Authentication Flow Type`
    
    `Browser Flow`
    
    `Scope`
    
    Leave blank
    
    `Identity Provider`
    
    Select `Authentication Provider` as the type and select the auth provider you created in the previous step
    
2.  Save the external credential.
    
3.  In the settings for the external credential you created, under `Principals`, click `New`. Enter the following values for the fields listed below:
    
    Field
    
    Value
    
    `Parameter Name`
    
    Enter your Slack app name (`Agentforce Custom Actions`)
    
    `Sequence Number`
    
    `1`
    
    `Identity Type`
    
    `Named Principal`
    
    `Scope`
    
    `chat:write`, `chat:write.public`, `mpim:read`, `reactions:write`, `channels:history`, `canvases:write`, `channels:join`, `channels:read`, `team:read`
    

Note on Named Principal

We want to use a `Named Principal` when we want to share credentials (i.e. agent actions on the agent's behalf) and a `User Principal` when we want to keep credentials scoped to a user (i.e. agent takes actions on your behalf).

4.  Save your changes.
5.  Click the drop-down toggle in the `Actions` section for your new Principal.
6.  Click `Authenticate` to start the browser authentication flow with your Slack app. When the Slack authentication browser page opens, be sure to use the workspace picker in the header to switch to installation at the org level. Problems can occur authenticating if the browser is used to log in to any other Salesforce or Slack orgs, so it's safest to create a separate browser profile or use an incognito browser if you run into issues.
    *   Once you’ve switched the install destination to your org, click **Allow**.
    *   On the Salesforce auth page, click **Confirm**.
    *   You’re credentials are now configured for use!
7.  Now we can enable external credentials for the `Einstein Agent User` and `System Administrator` profiles.
    *   From Setup, in the Quick Find box, enter `Profiles`, then select it from the options.
    *   Find the `Einstein Agent User` profile and select it. In the `Apps` section, select `External Credentials Principal Access`.
        *   In the `Enable External Credential Principal Access` section, click `Edit`.
        *   Select the checkbox for the external credentials principal that you created.
        *   Save your changes.
    *   Repeat for the `System Administrator` profile.

## Step 4: Create a Named Credential {#named-credential}

Now that you have an external credential to allow proper access to your Slack app, you’ll need a `Named Credential` to finalize your API configuration with the proper base URL and any custom headers you may want to include. This is what will be used in [Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_intro_what_is_apex.htm) classes for interacting with the [Slack Web API](/apis/web-api).

1.  Search again for `Named Credentials` in Salesforce Setup.
2.  From the `Named Credentials` tab, click `New`.
    *   For label enter `Slack API`.
    *   For name enter `Slack_API`.
    *   For the URL, enter `https://slack.com/api`.
    *   For external credentials, select `Slack` from the drop-down.
    *   Save your changes.

## Step 5: Set up your Salesforce Platform developer environment {#dev-environment}

There are two methods of developing with [Apex](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_intro_what_is_apex.htm): using the `Code Builder` developer environment within the Salesforce Platform or using VSCode with the proper Salesforce extensions installed. This guide focuses on using VSCode as your developer environment.

1.  Install the Salesforce CLI.
    *   Navigate to this [instruction page](https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm) and install the CLI for your given environment.
    *   Confirm your installation by running `sf --version` in the terminal of your choice.
2.  Set up VSCode for Salesforce Platform development.
    *   Open VSCode and navigate to the extensions tab.
    *   Search for and install the following extensions:
        *   `Salesforce Extension Pack`—You can install the extended pack for Salesforce extensions which has all these packages included (and a few others that aren’t needed for this guide).
        *   `Prettier`
        *   `ESLint`
        *   `XML`
    *   Reload the window to activate the new extensions.
3.  Set up a Salesforce development project.
    *   From the VSCode command palette (`Cmd/Ctrl + Shift + P`), search for `SFDX:Create Project` and select it from the list of options.
        
    *   For the template type, leave `Standard` selected and press `Enter`.
        
    *   Give your project a name like `Custom Slack Actions` and press `Enter`.
        
    *   Choose a destination on your computer for the project and click `Create Project`. If you see an error about Apex not being able to find a Java runtime, then you’ll need to install OpenJDK version 21 (if not already installed) and set the path in your workspace settings. See **Install JDK** below.
        
        Install JDK
        
        If you see an error about Apex not being able to find the Java runtime, follow these steps:
        
        1.  Navigate to this [install page](https://www.azul.com/downloads/?version=java-21-lts&package=jdk#zulu) and select the options for your specific OS and architecture. Then download the `.dmg` (for macOS) or `.msi` (for Windows) for the latest version for your set up.
        2.  Install the `.dmg` or `.msi`, leaving all defaults as is.
        3.  Open VSCode settings and search for `java: home`.
        4.  For the `Salesforcedx-vscode-apex › Java: Home` property, enter `/Library/Java/JavaVirtualMachines/zulu-21.jdk/Contents/Home` for macOS or `C:\Program-Files\Zulu\zulu-21\` for Windows.
        5.  Reload the workspace (`Cmd/Ctrl + Shift + P`, search for and select `Developer: Reload Window`).
        
    *   From the VSCode command palette, search for `SFDX: Authorize an Org` and select it from the list of options.
        
        *   Leave `Project Default` selected for login URL source and press `Enter`.
        *   Set an org alias like `customActionsOrg` or leave the default and press `Enter`.
        *   On the Salesforce login page, enter your `Username` and `Password` and click `Log In`.
        *   Allow access for the Salesforce CLI to act on your behalf by clicking `Allow`.
        *   You will get a notification in VSCode if authentication was successful.

Now that your credentials and developer environment are ready, we move on to the real fun—creating custom actions.

## Step 6: Create custom Agentforce actions with Apex {#custom-actions}

Apex actions use the `Invocable Method` [annotation syntax](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm) to define how the class can be used in platform features that support actions, like Flow and Agentforce. You'll use invocable methods that call out to the Slack API using the named credentials you created to authenticate. For this guide, you'll create two actions:

*   `GetSlackChannelAction` (from the [`auth.teams.list`](/reference/methods/auth.teams.list) and [`conversations.list`](/reference/methods/conversations.list) methods) to look up channels by name and workspace.
*   `SendSlackMessageAction` (from the [`chat.postMessage`](/reference/methods/chat.postMessage) method) to allow the agent to send messages to a given channel.

Here is an example request with a named credential:

```
request.setEndpoint('callout:Slack_API/chat.postMessage');
```

Why do I need two actions to send a message?

Technically you don't. You could have one action take the channel name, the org, and the message content to complete the task. However, it's useful to think of actions as composable steps.

Looking up a channel by it's name is useful in a lot of use cases so it makes sense to be it's own action! Then we can rely on the [instructions in our topics](#agent-builder) to inform how the agent uses these actions together, in this case allowing users to provide channel names when sending messages, and the agent can use the get channel action to get the proper data needed to send the message in Slack.

1.  Create your first custom action Apex class.
    *   From the VSCode command palette, search for `SFDX: Create Apex Class` and select it from the list of options.
    *   Name your class `GetSlackChannelAction` and press `Enter`.
    *   Leave the default path for the destination and press `Enter`.
    *   Replace the contents of the file with the code shown here, then save the file.

View file code

```
/*** GetSlackChannelAction* * This class provides a Flow-invocable action to search for a Slack channel by name within a specific workspace* in a Slack Enterprise org environment. It handles the pagination of results and provides detailed channel information.* * The process:* 1. Takes a workspace name and channel name as input* 2. Queries auth.teams.list to find the workspace ID from the name* 3. Uses the workspace ID to search for the channel using conversations.list* 4. Returns channel details if found*/public class GetSlackChannelAction {        /**    * Input class for the Flow action    * Requires both workspace name and channel name to perform the search    */    public class ChannelSearchInput {        @InvocableVariable(required=true description='Name of the channel to search for')        public String channel_name;                @InvocableVariable(required=true description='Name of the Slack workspace')        public String workspace_name;    }        /**    * Output class containing channel details or error information    * Returns basic channel information including ID, name, member count, and topic    */    public class ChannelSearchOutput {        @InvocableVariable(description='Channel ID')        public String channel_id;                @InvocableVariable(description='Channel Name')        public String channel_name;                @InvocableVariable(description='Number of members in the channel')        public Integer num_members;                @InvocableVariable(description='Channel topic')        public String topic;                @InvocableVariable(description='Error message if search failed')        public String error_message;    }        // ------------------------    // API Response Structures    // ------------------------        /**    * Response structure for auth.teams.list endpoint    * Used to find workspace/team ID from workspace name    */    private class TeamsListResponse {        public Boolean ok;        public List<Team> teams;        public ResponseMetadata response_metadata;        public String error;    }        /**    * Structure representing a Slack workspace/team    */    private class Team {        public String id;        public String name;    }        /**    * Response structure for conversations.list endpoint    * Contains list of channels and pagination metadata    */    private class SlackResponse {        public Boolean ok;        public List<Channel> channels;        public ResponseMetadata response_metadata;        public String error;    }        /**    * Metadata structure containing pagination information    */    private class ResponseMetadata {        public String next_cursor;    }        /**    * Structure representing a Slack channel    * Contains only the fields we need for our output    */    private class Channel {        public String id;        public String name;        public Integer num_members;        public Topic topic;    }        /**    * Structure representing a channel's topic    */    private class Topic {        public String value;    }        /**    * Main invocable method for the Flow action    * Processes a list of inputs (bulk processing support) and returns corresponding outputs    */    @InvocableMethod(label='Get Slack Channel'                     description='Searches for a Slack channel by name in specified workspace and returns its details')    public static List<ChannelSearchOutput> searchChannel(List<ChannelSearchInput> inputs) {        List<ChannelSearchOutput> outputs = new List<ChannelSearchOutput>();                // Process each input in the list (supporting bulk operations)        for(ChannelSearchInput input : inputs) {            ChannelSearchOutput output = new ChannelSearchOutput();                        try {                // Step 1: Get the workspace ID from the workspace name                String teamId = getWorkspaceId(input.workspace_name);                                if (teamId == null) {                    output.error_message = 'Workspace "' + input.workspace_name + '" not found';                    outputs.add(output);                    continue;                }                                // Step 2: Search for the channel in the identified workspace                Channel foundChannel = searchAllChannels(input.channel_name, teamId);                                // Step 3: Process results                if (foundChannel != null) {                    // Channel found - populate output with channel details                    output.channel_id = foundChannel.id;                    output.channel_name = foundChannel.name;                    output.num_members = foundChannel.num_members;                                        if (foundChannel.topic != null) {                        output.topic = foundChannel.topic.value;                    }                } else {                    // Channel not found                    output.error_message = 'Channel not found';                }                            } catch(Exception e) {                // Handle any errors that occur during processing                output.error_message = 'Error: ' + e.getMessage();                System.debug('Error details: ' + e.getStackTraceString());            }                        outputs.add(output);        }                return outputs;    }        /**    * Gets the workspace ID for a given workspace name using auth.teams.list    * This method handles the Enterprise org workspace lookup    *     * @param workspaceName The name of the workspace to find    * @return The workspace ID if found, null if not found    */    private static String getWorkspaceId(String workspaceName) {        // Initialize HTTP request        Http http = new Http();        HttpRequest request = new HttpRequest();        request.setEndpoint('callout:Slack_API/auth.teams.list');        request.setMethod('GET');                // Make the API call        HttpResponse response = http.send(request);                // Check for successful response        if (response.getStatusCode() != 200) {            throw new CalloutException('Teams list failed with status code: ' + response.getStatusCode());        }                // Parse the response        TeamsListResponse teamsResponse = (TeamsListResponse)JSON.deserialize(            response.getBody(),             TeamsListResponse.class        );                if (!teamsResponse.ok) {            throw new CalloutException('Teams list not OK: ' + teamsResponse.error);        }                // Search for matching workspace name        for (Team team : teamsResponse.teams) {            if (team.name.equalsIgnoreCase(workspaceName)) {                return team.id;            }        }                // No matching workspace found        return null;    }        /**    * Searches for a channel by name within a specific workspace    * Handles pagination to search through all available channels    *     * @param channelName The name of the channel to find    * @param teamId The ID of the workspace to search in    * @return Channel object if found, null if not found    */    private static Channel searchAllChannels(String channelName, String teamId) {        String cursor = null;                do {            // Construct endpoint URL with team_id and pagination cursor            String endpoint = 'callout:Slack_API/conversations.list?team_id=' + teamId;            if (String.isNotBlank(cursor)) {                endpoint += '&cursor=' + EncodingUtil.urlEncode(cursor, 'UTF-8');            }                        // Initialize HTTP request            Http http = new Http();            HttpRequest request = new HttpRequest();            request.setEndpoint(endpoint);            request.setMethod('GET');                        // Make the API call            HttpResponse response = http.send(request);                        // Check for successful response            if (response.getStatusCode() != 200) {                throw new CalloutException('Failed with status code: ' + response.getStatusCode());            }                        // Parse the response            SlackResponse slackResponse = (SlackResponse)JSON.deserialize(                response.getBody(),                 SlackResponse.class            );                        if (!slackResponse.ok) {                throw new CalloutException('Slack API response not OK: ' + slackResponse.error);            }                        // Search through current page of channels            for (Channel channel : slackResponse.channels) {                if (channel.name.equalsIgnoreCase(channelName)) {                    return channel;                }            }                        // Get cursor for next page of results            cursor = (slackResponse.response_metadata != null) ?                     slackResponse.response_metadata.next_cursor : null;                            } while (String.isNotBlank(cursor)); // Continue while there are more pages                // Channel not found after searching all pages        return null;    }}
```

*   Deploy the class to your org by running the following command in the VSCode command palette: `SFDX: Deploy This Source to Org`. You can also access this command by right-clicking in the file and selecting the option from the menu.

2.  Test your custom action.
    *   From the VSCode file explorer, navigate to `scripts/apex/hello.apex`.
        
    *   Replace the contents of the file with this testing script. Be sure to change `workspaceName` and `channelName` to yours.
        
        View test script code
        
        ```
            GetSlackChannelAction.ChannelSearchInput input = new GetSlackChannelAction.ChannelSearchInput();    input.workspaceName = 'SDO';  // Change this to match your workspace    input.channelName = 'general'; // Change this to match your channel    List<GetSlackChannelAction.ChannelSearchInput> inputs = new List<GetSlackChannelAction.ChannelSearchInput>();    inputs.add(input);    List<GetSlackChannelAction.ChannelSearchOutput> results = GetSlackChannelAction.searchChannel(inputs);    // Print results    GetSlackChannelAction.ChannelSearchOutput result = results[0];    if(String.isNotBlank(result.errorMessage)) {    System.debug('Error: ' + result.errorMessage);    } else {        System.debug('Success! Channel found:');        System.debug('Channel ID: ' + result.channelId);        System.debug('Channel Name: ' + result.channelName);        System.debug('Members: ' + result.numMembers);        System.debug('Topic: ' + result.topic);    }
        ```
        
    *   From the VSCode command palette (`Cmd/Ctrl + Shift + P`), search for and select `SFDX: Execute Anonymous Apex with Editor Contents` to execute the script.
        
    *   In VSCode’s `OUTPUT` tab, check to ensure you were successfully able to look up a channel by name.
        
3.  Now we'll do the same for the `SendSlackMessageAction`.
    *   From the VSCode command palette, search for `SFDX: Create Apex Class` and select it from the list of options.
        
    *   Name your class `SendSlackMessageAction` and press `Enter`.
        
    *   Leave the default path for the destination and press `Enter`.
        
    *   Replace the contents of the file with the code shown here, then save the file.
        
        View file code
        
        ```
        /*** SendSlackMessageAction* * Invocable Apex action that sends a message to a Slack channel.* Requires direct Channel ID and Workspace ID rather than names.* Uses Named Credential 'Slack_API' for authentication.*/public class SendSlackMessageAction {        /**    * Invocable method input class    */    public class MessageInput {                @InvocableVariable(required=true description='ID of the channel to send to')        public String channel_id;        @InvocableVariable(required=true description='ID of the workspace to send to')        public String workspace_id;                @InvocableVariable(required=true description='Message text to send')        public String text;    }        /**    * Invocable method output class returned to Flow/Process Builder    * Provides message send status, timestamp for reference, and any error details    * Message timestamp (ts) can be used as a message identifier for later updates/deletion    */    public class MessageOutput {        @InvocableVariable(description='True if message was sent successfully')        public Boolean is_success;                @InvocableVariable(description='Timestamp of sent message')        public String message_ts;                @InvocableVariable(description='Error message if send failed')        public String error_message;    }        /**    * Main invocable method to send a message to Slack    * Handles a list of inputs for bulk processing but typically receives one input    * Returns a corresponding list of outputs with success/failure details    *     * @param inputs List of MessageInput objects containing message details    * @return List<MessageOutput> Results of the message send operation(s)    */    @InvocableMethod(label='Send Slack Message To Channel')    public static List<MessageOutput> sendMessage(List<MessageInput> inputs) {        List<MessageOutput> outputs = new List<MessageOutput>();                // Process each input (usually just one)        for(MessageInput input : inputs) {            MessageOutput output = new MessageOutput();            output.is_success = false; // Default to false until success confirmed                        try {                // Setup HTTP request to Slack API                Http http = new Http();                HttpRequest request = new HttpRequest();                request.setEndpoint('callout:Slack_API/chat.postMessage');                request.setMethod('POST');                request.setHeader('Content-Type', 'application/json');                                // Construct message payload                Map<String, String> body = new Map<String, String>{                    'channel' => input.channel_id,                    'text' => input.text,                    'team_id' => input.workspace_id                };                                request.setBody(JSON.serialize(body));                                // Send message to Slack                HttpResponse response = http.send(request);                                // Parse the JSON response                Map<String, Object> responseBody = (Map<String, Object>)JSON.deserializeUntyped(response.getBody());                                // Check for success and process results                if(response.getStatusCode() == 200 && responseBody.get('ok') == true) {                    output.is_success = true;                    output.message_ts = (String)responseBody.get('ts');                } else {                    // Capture API error message if present                    output.error_message = 'API Error: ' + responseBody.get('error');                }                            } catch(Exception e) {                // Handle any exceptions (callout errors, parsing errors, etc)                output.error_message = 'Error: ' + e.getMessage();                System.debug('Error details: ' + e.getStackTraceString());            }                        outputs.add(output);        }                return outputs;    }}
        ```
        
    *   Deploy the class to your org by running the following command in the VSCode command palette: `SFDX: Deploy This Source to Org`. You can also access this command by right-clicking in the file and selecting the option from the menu.
        
4.  Test your custom action.
    *   From the VSCode file explorer, navigate to `scripts/apex/hello.apex`.
    *   Replace the contents of the file with this testing script. Be sure to change `workspaceName` and `channelName` to yours.

View test script code

```
SendSlackMessageAction.MessageInput input = new SendSlackMessageAction.MessageInput();input.workspace_id = 'T06HLNFMU22';  // Replace with your workspace IDinput.channel_id = 'C06HT8GNC03'; // Replace with your channel IDinput.text = 'Test message from Salesforce ' + Datetime.now();List<SendSlackMessageAction.MessageInput> inputs = new List<SendSlackMessageAction.MessageInput>();inputs.add(input);List<SendSlackMessageAction.MessageOutput> results = SendSlackMessageAction.sendMessage(inputs);// Print resultsSendSlackMessageAction.MessageOutput result = results[0];if(result.is_success) {    System.debug('Message sent successfully!');    System.debug('Message Timestamp: ' + result.message_ts);} else {    System.debug('Failed to send message');    System.debug('Error: ' + result.error_message);}
```

*   From the VSCode command palette (`Cmd/Ctrl + Shift + P`), search for and select `SFDX: Execute Anonymous Apex with Editor Contents` to execute the script.
*   In VSCode’s `OUTPUT` tab, check to ensure you were successfully able to look up a channel by name.

## Step 7: Make your custom actions available in Agent Builder {#agent-builder}

Now that you have your Apex classes deployed to the org, it’s time to create the custom actions for use in Agent Builder.

### Assign permissions for the Einstein Agent User to use your Apex classes {#assign-permissions-for-the-einstein-agent-user-to-use-your-apex-classes}

*   Navigate back to your Salesforce org setup. Search for `Profiles` in `Search Setup` and select it from the list of options.
*   Select `Einstein Agent User` from the list of profiles.
*   In the `Apps` section, select `Apex Class Access`.
*   In the `Apex Class Access` section, select `Edit`.
*   Find the two new Apex classes you deployed to your org and select them. Click `Save`. You need to save per page of classes, and your classes may appear on different pages.

### Create custom actions from your Apex classes {#create-custom-actions-from-your-apex-classes}

*   In the Quick Find search in Setup, search for `Agentforce Assets` and select the setting. Navigate to the `Actions` tab.
*   In the top-right, click `+ New Agent Action`.
    *   For `Reference Action Type` select `Apex`.
    *   For `Reference Action Category` select `Invocable Methods`.
    *   For `Reference Action`, search for `Get Slack Channel`. It may take a few moments for this option to show up; give it a moment!
    *   For `Agent Action Label` and `Agent Action API Name` leave the default values.
    *   Click `Next`.
*   In the `Agent Action Configuration` form:
    *   Enter `Searches for a Slack channel by name in specified workspace and returns its details` under `Agent Action Instructions`. Leave the default values for the `Inputs` and `Outputs` instructions.
    *   For each parameter in `Outputs`, check the `Show in conversation` checkbox.
    *   Click `Finish`.
*   Now repeat for the `Send Slack Message` Apex class you created. In the Quick Find search in Setup, search for `Agentforce Assets` and select the setting. Navigate to the `Actions` tab.
*   In the top-right, click `+ New Agent Action`.
    *   For `Reference Action Type` select `Apex`.
    *   For `Reference Action Category` select `Invocable Methods`.
    *   For `Reference Action`, search for `Send Slack Message`.
    *   For `Agent Action Label` and `Agent Action API Name` leave the default values.
    *   Click `Next`.
*   In the `Agent Action Configuration` form:
    *   Enter `Sends a Slack message to the provided channel` under `Agent Action Instructions`. Leave the default values for the `Inputs` and `Outputs` instructions.
    *   For each parameter in `Outputs`, check the `Show in conversation` checkbox.
    *   Click `Finish`.

### Add your actions to a Topic {#add-your-actions-to-a-topic}

*   From the `Agentforce Agents` settings in Setup, click on the agent of your choice and select `Open in Builder`.
*   From the `Topics` tab in the left sidebar, click the `New` button and select `New Topic`:
    *   When prompted, `What do you want this topic to do?`, enter `Help the user send messages in Slack to specific channels. Also, look up a Slack channel by name and workspace to assist in sending messages.` Click `Next`.
    *   Note the generated fields. Adjust as you see fit. Here are some helpful instructions to add to help the agent understand how to best use the actions within the given topic:
        *   `If a user asks you to send a message to a channel and provides the channel name instead of an ID, use the Get Slack Channel action to look up the appropriate channel ID.`
        *   `When users provide channel names, remove the ‘#’ at the beginning if they include one.`
    *   Click `Next`.
    *   Search for the Slack actions you created and add them to the Topic.
    *   Click `Finish`.

### Test your agent in Agent Builder {#test-your-agent-in-agent-builder}

*   Click the refresh icon in the `Conversation Preview` sidebar to refresh your agent.
*   Click the `Activate` button to start the agent.
*   Test the agent by asking it to send a Slack message to the #general channel for you, then confirm the message was posted in your Slack workspace.

Look at that; you built an agent that works with Slack! Let's deploy it there next.

## Step 8: Deploy your agent to Slack {#deploy}

Follow these steps to deploy your agent to Slack.

1.  First, we'll add a connection to Slack for our agent.
    *   Download the [Slack Platform Connector](https://login.salesforce.com/packaging/installPackage.apexp?p0=04tKX000000cHXG) and select `Install for All Users`
    *   Navigate back to the Salesforce Setup Quick Find and search for `Einstein Bots`. Select `Einstein Bots` under `Einstein Platform`, then switch the toggle in the upper right to `On`.
    *   There are two ways to add the connection to your agent.

Method 1: Agent Builder

*   If your agent is still open in Agent Builder, click on the `Connections` tab in the sidebar nav; it looks like a stack of squares. Under `Connections`, click `Add`.
*   Select `API` and give it a descriptive name in the `Integration Name` field. This must be distinct from other agent connections you've created.
*   Search for "Slack" in the `Connected App` field. Click on "Slack" as it appears in the autocomplete.
*   `Save` the connection.
*   Make sure your agent is `Active` before moving on to the next steps.

Method 2: Agent settings

*   In the Quick Find, search for and select `Agents` under `Agent Studio`. Find your desired agent in the list of agents and click the arrow button on the far right, then select `Edit`.
*   On the `Connections` tab, under `Connections`, click the `Add` button.
*   Select `API` and give it a descriptive name in the `Integration Name` field. This must be distinct from other agent connections you've created.
*   Search for "Slack" in the `Connected App` field. Click on "Slack" as it appears in the autocomplete.
*   `Save` the connection.
*   Make sure your agent is `Active` before moving on to the next steps.

2.  Install your agent in Slack
    *   In your Slack org settings navigate to `Salesforce` > `Agentforce`
    *   Under `Requested Agents` find the agent you added your Slack actions to and click `Review Agent`. Only agents with the word `Agent` in their label will show up in your Slack org for review and installation.
    *   Review the agent's information and click `Install Agent`
    *   Next, click `Choose Workspaces` and add to any workspaces you want the agent in, click `Next`, then `Next` again
    *   For `Who can use this agent?`, select `Everyone`
    *   Agree to terms and click `Add Agent`
    *   Save
3.  Test your agent in Slack
    *   Navigate to the `Agentforce` tab in your Slack workspace.

If Agentforce tab is not present, follow these instructions

*   In Slack, click on the workspace name, then select `Preferences`.
*   Under `Navigation`, select the checkboxes for `Show app agents` and the name of your agent.
*   Close `Preferences` and reload Slack. You should now see `Agentforce` in the side nav. Click on it.

*   Select the agent you installed to start a conversation with it
*   Ask the agent to send a message for you
*   Verify the message was sent to the proper channel

## Next steps {#next-steps}

While this guide explored just two Slack Web API methods for [getting a channel](/reference/methods/conversations.list) and [sending a message](/reference/methods/chat.postMessage), there are a wealth of methods available to customize your agent's capabilities even more. Check out the full scope of the Slack API [here](/reference/methods), create Apex actions for them as outlined in this guide, and use the created actions as topics in your agent!

Looking to customize your agent without the code? Explore the available standard Slack actions [here](https://help.salesforce.com/s/articleView?id=ai.copilot_actions_ref.htm&type=5).