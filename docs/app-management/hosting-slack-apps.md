Source: https://docs.slack.dev/app-management/hosting-slack-apps

# Hosting Slack apps

If you have chosen to self-host your Slack app, you'll need a cloud provider to do so. Below are some common ones as well as some resources to help you get started.

## Common cloud providers {#cloud-providers}

### Vercel {#vercel}

[Vercel](https://vercel.com/docs) is a platform for building AI-powered apps. Vercel provides tools and infrastructure needed to build and deploy robust, secure, and performant AI applications.

Slack Agent Template

To jumpstart your development, use Vercel's [Slack Agent Template](https://vercel.com/templates/ai/slack-agent-template) built with [Bolt for JavaScript](/tools/bolt-js) and Nitro.

Use this button to deploy a new project through the Vercel project creation flow while cloning the Slack Agent Template.

[Deploy with Vercel](https://vercel.com/new/clone?demo-description=This+is+a+Slack+Agent+template+built+with+Bolt+for+JavaScript+%28TypeScript%29+and+the+Nitro+server+framework.&demo-image=%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FSs9t7RkKlPtProrbDhZFM%2F0d11b9095ecf84c87a68fbdef6f12ad1%2FFrame__1_.png&demo-title=Slack+Agent+Template&demo-url=https%3A%2F%2Fgithub.com%2Fvercel-partner-solutions%2Fslack-agent-template&env=SLACK_SIGNING_SECRET%2CSLACK_BOT_TOKEN&envDescription=These+environment+variables+are+required+to+deploy+your+Slack+app+to+Vercel&envLink=https%3A%2F%2Fapi.slack.com%2Fapps&from=templates&project-name=Slack+Agent+Template&project-names=Comma+separated+list+of+project+names%2Cto+match+the+root-directories&repository-name=slack-agent-template&repository-url=https%3A%2F%2Fgithub.com%2Fvercel-partner-solutions%2Fslack-agent-template&root-directories=List+of+directory+paths+for+the+directories+to+clone+into+projects&skippable-integrations=1&teamSlug=vercel-partner-demo)

### Heroku {#heroku}

[Heroku](https://www.heroku.com/home) is a platform as a service based on a managed container system, with integrated data services and a powerful ecosystem, for deploying and running Slack apps.

✨ Follow our step-by-step guide on [deploying to Heroku](/tools/bolt-js/deployments/heroku) using [Bolt for JavaScript](/tools/bolt-js).

### AWS Lambda {#aws}

[AWS Lambda](https://aws.amazon.com/lambda/) is a compute service that runs your code in response to events and automatically manages the compute resources, making it the fastest way to turn an idea into a modern, production, serverless application. Check out their repository for [running a Slackbot on AWS using coldbrew-cli](https://github.com/coldbrewcloud/tutorial-echo-slack-bot/blob/master/README.md).

✨ You can also follow our step-by-step guide on [deploying to AWS Lambda](/tools/bolt-js/deployments/aws-lambda) using [Bolt for JavaScript](/tools/bolt-js).

### Google Cloud Platform {#google-cloud-platform}

[Google Cloud Platform](https://cloud.google.com/why-google-cloud) lets you build, deploy, and scale applications, websites, and services on the same infrastructure as Google. Check out their guide on [three ways to build Slack integrations on Google Cloud Platform](https://cloud.google.com/blog/products/gcp/three-ways-to-build-slack-integrations-on-google-cloud-platform/) and their repository for [sending connection notifications to Slack from Google Computer Engine](https://github.com/GoogleCloudPlatform/community/blob/master/archived/send-connect-notification-to-slack-from-google-compute-engine.md).

### Microsoft Azure {#ms-azure}

[Microsoft Azure](https://azure.microsoft.com/) allows you to build, run, and manage applications across multiple clouds, on-premises, and at the edge, with the tools and frameworks of your choice.

### IBM Cloud {#ibm-cloud}

[IBM Cloud](https://www.ibm.com/cloud) is an enterprise cloud platform that is AI-ready. Check out their guide on how to [build a database-driven Slackbot](https://cloud.ibm.com/docs/solution-tutorials?topic=solution-tutorials-slack-chatbot-database-watson#slack-chatbot-database-watson).

## Next steps {#next-steps}

▶️ **To list your app in the Slack Marketplace**, refer to our [Slack Marketplace review guide](/slack-marketplace/slack-marketplace-review-guide).

▶️ **To learn more about Slack app development**, check out [designing Slack apps](/surfaces/app-design).