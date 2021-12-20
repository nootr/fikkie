# 🔥 Fikkie

Welcome to the fikkie documentation!

Fikkie is a simple lightweight watchdog which monitors external services over
SSH.

Simply specify which commands should be run on which servers and what output is
expected, and fikkie will let you know when something's wrong.


## User's guide

* [Installation](#installation)
* [Configuration](#configuration)
  * [Setting up SSH](#setting-up-ssh)
  * [(Optional) Adding user](#adding-user)
  * [Setting up fikkie](#setting-up-fikkie)
* [Setting up a notifier](#setting-up-a-notifier)
  * [E-mail notifier](#e-mail-notifier)
  * [Telegram notifier](#telegram-notifier)
* [Running fikkie as a daemon](#running-fikkie-as-a-daemon)


## API Reference

* [API Reference](#api-reference-1)
  * [CLI flags](#cli-flags)
  * [Environment variables](#environment-variables)
  * [Configuration options](#configuration-options)


## Installation

Installing fikkie is easy!

```bash
pip install fikkie
fikkie init
```


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

## Setting up a notifier

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


## Running fikkie as a daemon

When you've configured fikkie and everything works as expected, start a fikkie daemon as
follows:

```bash
fikkie start
```

Stopping the daemon is just as easy:

```bash
fikkie stop
```


## API reference

### CLI flags

* **fikkie init**: Set up the ~/.fikkie directory.
* **fikkie run**: Start fikkie.
* **fikkie start**: Start a fikkie daemon.
* **fikkie stop**: Stop the fikkie daemon.
* **fikkie status [--format {YAML,JSON,JSON-PRETTY}]**: Get status from all servers.
* **fikkie -h/--help**: Show the help/usage text.

### Environment variables

* **FIKKIE_BASE_DIR** *(default: "~/.fikkie")*: Fikkie's working directory.
* **FIKKIE_CONFIG** *(default: "~/.fikkie/config.yaml")*: The configuration
file.
* **FIKKIE_BROKER_DIR** *(default: "~/.fikkie/broker")*: A directory containing
the celery broker data.
* **FIKKIE_DB_FILENAME** *(default: "~/.fikkie/db.json")*: The database file.
* **FIKKIE_LOG_FILE** *(default: "~/.fikkie/fikkie.log")*: The daemon log file.
* **FIKKIE_PID_FILE** *(default: "~/.fikkie/fikkie.pid")*: The PID file.


### Configuration options

* **ssh.username** *(default: "fikkie")*: The SSH username which fikkie uses.

Example:

```yaml
ssh:
  username: fikkie
```

* **servers.HOSTNAME.description**: A human-readable description of the test.
* **servers.HOSTNAME.command**: The command to execute.
* **servers.HOSTNAME.expected**: The expected stdout output.

Example:

```yaml
servers:
  primary.foo.com:
    - description: 'MariaDB'
      command: 'sudo systemctl status mariadb | grep "Active: active" -c'
      expected: '1'
    - description: 'HTTP code foo.com'
      command: 'curl -s -o /dev/null -w "%{http_code}" foo.com'
      expected: '200'
```

* **notifiers**: A list of notifier objects. Parameters may differ per
notifier.

Example:

```yaml
notifiers:
  - type: telegram
    token: '1234:abcd'
    chat_id: 1234
```

For **notifiers.type** = `email`
* **notifiers.recipient**: The e-mail address to which notifications are sent.
* **notifiers.email**: The e-mail address which Fikkie uses to sent.
* **notifiers.password**: The password needed to login to the SMTP server.
* **notifiers.smtp_server**: The SMTP server.
* **notifiers.smtp_port** *(default: 465)*: The port on which the SMTP server listens.

For **notifiers.type** = `telegram`
* **notifiers.token**: The Telegram bot token.
* **notifiers.chat_id**: The chat ID that Fikkie sends its notifications to.
