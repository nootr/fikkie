# Setting up a notifier

* * *

## User's guide

* [About fikkie](./index)
* [Installation](./installation)
* [Configuration](./configuration)
  * [Setting up SSH](./configuration#setting-up-ssh)
  * [(Optional) Adding user](./configuration#adding-user)
  * [Setting up fikkie](./configuration#setting-up-fikkie)
  * [Running fikkie as a daemon](./configuration#running-fikkie-as-a-daemon)
* [Setting up a notifier](#)
  * [Discord notifier](#discord-notifier)
  * [E-mail notifier](#e-mail-notifier)
  * [Slack notifier](#slack-notifier)
  * [Telegram notifier](#telegram-notifier)


## API Reference

* [API Reference](./api)
  * [CLI flags](./api#cli-flags)
  * [Environment variables](./api#environment-variables)
  * [Configuration options](./api#configuration-options)


* * *

## Setting up a notifier

### Discord notifier

Creating a Discord bot as a notifier is pretty straightforward:

* Log into the Discord Developer Portal and create a new Application.
* Navigate to the "Bot" settings and add a new bot.
* Copy the token.
* Disable the "Public bot" switch.
* Navigate to the "OAuth2" settings and click on "URL generator".
* Enable the "Bot" scope and "Send messages" permissions.
* Visit the generated URL.
* Select the server on which you want to add the bot.

Now add the following lines to your fikkie configuration:

```yaml
notifiers:
  - type: discord
    token: 'foobarbaz'
    channel_id: 1234
```

The Discord notifier uses the `hikari` package as a dependency, so make sure you install
that as well.

### E-mail notifier

The e-mail notifier needs to login on an SMTP server. In this example, GMail's SMTP
server is used to mail to a hotmail recipient.

```yaml
notifiers:
  - type: email
    recipient: 'foo@hotmail.com'
    email: 'foo@gmail.com'
    password: 'abcdefghijkl'
    smtp_server: 'smtp.gmail.com'
    smtp_port: 465  # This is the default port, you can remove this line
```

Note that for this to work with GMail, you would first need to create an App Password.

### Slack notifier

Create a Slack bot by following these steps:

* Visit [the Slack Apps page](https://api.slack.com/apps).
* Create a new App and select the "From scratch" option.
* Name the App and pick the workspace in which the bot must send notifications.
* Go to "OAuth & Permissions".
* Scroll down to the "Scopes" section and add a `chat:write` OAuth Scope for bots.
* Now scroll up and click on "Install to Workspace".
* After allowing the permissions, copy the token under "Bot User OAuth Token".
* Finally, return to Slack, select the newly added App and click on the name of the Bot.
* Click on "Add this Bot to a channel" to, well, add it to a channel!

Now add the following lines to your fikkie configuration:

```yaml
notifiers:
  - type: slack
    token: 'xoxb-foobarbaz'
    channel_id: 'C0******'
```

The Slack notifier uses the `slack_sdk` package as a dependency, so make sure you
install that as well.

### Telegram notifier

Talk to @BotFather to create a bot and add the following lines to your fikkie
configuration:

```yaml
notifiers:
  - type: telegram
    token: '1234:abcd'
    chat_id: 1234
```

The Telegram notifier uses the `python-telegram-bot` package as a dependency,
so make sure you install that as well.
