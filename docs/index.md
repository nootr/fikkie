Welcome to the fikkie documentation!

Fikkie is a simple lightweight watchdog which monitors external services over
SSH.

Simply specify which commands should be run on which servers and what output is
expected, and fikkie will let you know when something's wrong.

For more information, check out the [GitHub repository](https://github.com/nootr/fikkie)
or the [PyPi page](https://pypi.org/project/fikkie).


* * *

## User's guide

* [Installation](./installation)
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


## API Reference

* [API Reference](./api)
  * [CLI flags](./api#cli-flags)
  * [Environment variables](./api#environment-variables)
  * [Configuration options](./api#configuration-options)
