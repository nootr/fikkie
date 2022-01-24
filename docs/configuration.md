# Configuration

* * *

## User's guide

* [About fikkie](./index)
* [Installation](./installation)
* [Configuration](#)
  * [Setting up SSH](#setting-up-ssh)
  * [(Optional) Adding user](#adding-user)
  * [Setting up fikkie](#setting-up-fikkie)
  * [Running fikkie as a daemon](#running-fikkie-as-a-daemon)
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


* * *

## Configuration

### Setting up SSH

Fikkie authenticates with SSH using a key (without password), so make sure you
generate a key using `ssh-keygen` and copy the public key to
`~/.ssh/authorized_keys` on the target host(s) if you haven't already.

### Adding user

This step is optional. However, it might be a good idea to create a separate
user for fikkie on the target host(s) with limited sudo permissions.

Open the sudoers file with `sudo visudo` and add the following line:

```
fikkie ALL=(ALL) NOPASSWD: /path/to/command1, /path/to/command2
```

### Setting up fikkie

When you run `fikkie init`, a configuration template is placed in
`~/.fikkie/config.yaml`. Edit this file to specify the servers you want to
monitor and which notifiers should be used. Go to the
[API Reference](#api-reference) for more info.

To test the configuration, start fikkie by executing:

```bash
fikkie run
```

When everything works, you can [start a fikkie daemon](#running-fikkie-as-a-daemon).


### Running fikkie as a daemon

When you've configured fikkie and everything works as expected, start a fikkie daemon as
follows:

```bash
fikkie start
```

Stopping the daemon is just as easy:

```bash
fikkie stop
```

The fikkie daemon saves its logs in `~/.fikkie/fikkie.log`.
