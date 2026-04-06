Source: https://docs.slack.dev/slack-marketplace/marketplace-terms-conditions/slack-security-review

# Slack Security Review

Slack wants to help you (our developers) create secure applications and integrations. To help with this, we created an advanced Security Review program that may be performed on published Slack Marketplace applications. If you're submitting your app to the Slack Marketplace, read on to learn more about the process. If you’re a Slack workplace administrator, we recommend reviewing our [Security recommendations for approving apps](https://slack.com/intl/en-ca/help/articles/360001670528-Security-recommendations-for-approving-apps).

### Your Application can be composed of multiple components: {#your-application-can-be-composed-of-multiple-components}

*   A web server that Slack reaches out to
*   A service that reaches out to Slack
*   Mobile applications that your application offers
*   Servers that access Slack and process data

As part of our security review process, we will assess the security of all parts of your infrastructure that are required to make the core functionality of your offering work in its intended manner (both the Slack parts, and yours). If a customer using your app can type something in your systems, and it can end up in Slack, or vice-versa, we need to take a look at your offering.

### We reserve the right to perform the following on the applicable parts of your application: {#we-reserve-the-right-to-perform-the-following-on-the-applicable-parts-of-your-application}

*   Automated web application security scanning
*   Automated network security scanning
*   Manual verification of proper authentication scope requests to ensure least-privilege design
*   Manual testing of functionality for security vulnerabilities and misuse
*   Manual architecture review of your application
*   Ask you follow-up questions about functionality

### Things to consider while building your application: {#things-to-consider-while-building-your-application}

*   Please review our [Best practices for security](/security) documentation
*   Be mindful of the [OWASP Top 10 Vulnerabilities](https://www.owasp.org/index.php/Top_10-2017_Top_10) when creating your web application
*   New to web application security? Get a copy of [The Web Application Hacker's Handbook](http://www.amazon.com/The-Web-Application-Hackers-Handbook/dp/1118026470)
*   Use encryption! Test out your TLS security at [https://www.ssllabs.com/ssltest/](https://www.ssllabs.com/ssltest/)
*   Do you use Ruby on Rails? Check out [Brakeman](http://brakemanscanner.org/) static analysis

### What we need from you: {#what-we-need-from-you}

*   While not necessary, a basic architecture diagram for your application helps expedite our review process. This includes any services that you operate that interact with Slack, including servers, databases, and third-party integrations that are required for your offering to function.
*   Your application must be "feature-complete" and function as your final product will function on the Slack Marketplace. If your application materially changes, we reserve the right to re-review your application and delist it if it does not pass another security review.
*   Security Review Contact
    *   If we need to contact you during a test, we need a reliable email address and phone number.
*   A sample use case of your application functioning correctly
    *   If you have lots of buttons and options, please tell us how to click them correctly, so we can focus on testing your application! Screenshots are especially helpful.
*   If you have a web application component (something that Slack reaches out to, or a customer goes to, in order to operate the Slack integration)
    *   Testing Account(s), with login information
        *   If your application has a permissions model (admin, non-admin, etc...), we will need a testing account for each.
    *   Test environment populated with some test data
        *   In order to get back to you as quickly as possible, please provide some test data (enough to demonstrate core functionality of your application) so our testers can spend more time assessing your application, and less time making up funny test names.
    *   We can provide your team with our testing IP addresses if your application is only available to certain IP addresses, or if you'd like to monitor our testing.

### Review Notes {#review-notes}

The Slack Application Security Review is not a certification, or proof of a secure application. Additional vulnerabilities may exist after a review, and we may revisit your application in the future to re-evaluate the security of your offering.

We will provide you with a report along with our reasoning for issues, reproduction steps, and links to additional resources to help you remediate the issues.

Due to the nature of testing multiple applications simultaneously, we cannot inform you of when we will be testing your application.

Please note: correspondence regarding an upcoming security review will come from [appdirectory-security@slack-corp.com](mailto:appdirectory-security@slack-corp.com).