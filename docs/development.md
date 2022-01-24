# Development

* * *

## User's guide

* [About fikkie](./index)
* [Installation](#)
* [Configuration](./configuration)
  * [Setting up SSH](./configuration#setting-up-ssh)
  * [(Optional) Adding user](./configuration#adding-user)
  * [Setting up fikkie](./configuration#setting-up-fikkie)
  * [Running fikkie as a daemon](./configuration#running-fikkie-as-a-daemon)
* [Setting up a notifier](./notifiers)
  * [Discord notifier](./notifiers#discord-notifier)
  * [E-mail notifier](./notifiers#e-mail-notifier)
  * [Slack notifier](./notifiers#slack-notifier)
  * [Telegram notifier](./notifiers#telegram-notifier)


## Developer's guide

* [Setting up a development environment](#setting-up-a-development-environment)
* [Useful commands](#useful-commands)


## API Reference

* [API Reference](./api)
  * [CLI flags](./api#cli-flags)
  * [Environment variables](./api#environment-variables)
  * [Configuration options](./api#configuration-options)


* * *

## Setting up a development environment

So you want to write a patch, fix a bug or implement a new feature? You're awesome,
thanks!

Start off by forking the fikkie GitHub repository and clone the fork.

```bash
git clone https://github.com/YOUR_USERNAME/fikkie
cd fikkie
```

Now create a virtual environment to prevent a dependency hell on your system.

```bash
python3 -m venv venv
source venv/bin/activate
```

Now that you're inside the virtual environment, install the dependencies:

```bash
pip install -r requirements.txt
pip install -r test-requirements.txt
```

Finally, fikkie will need a configuration file to send notifications. Create a file at
`~/.fikkie/config.yaml` with the following contents:

```yaml
---
heartbeat:
  schedule:
    minute: '*'
    hour: '*'
```

This will make sure fikkie sends a heartbeat notification every minute.

The celery output will contain logs of the heartbeat notifications, but please check out
[Setting up a notifier](./notifiers) to configure a notifier.


## Useful commands

The project contains a Makefile to make your life a tiny bit easier. The most important
make commands are the following three:

```bash
make unit  # Run the unit tests
make lint  # Run the linter (black)
make dev   # Run fikkie with loglevel set to DEBUG
```
