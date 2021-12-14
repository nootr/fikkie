# Fikkie 🔥

A simple watchdog which monitors servers over SSH.

Simply specify which commands should be run on which servers and what output is
expected, and fikkie will let you know when something's wrong.

Notifiers are written as modules, so adding a new notifier is easy! Currently,
fikkie only supports notifying using a Telegram bot, but adding more options
(i.e. e-mail, Slack, Discord) should be added before version 1.0.

## Installation

Installing fikkie is easy, just clone this repository and run pip:

```bash
pip install .
```

## Configuration

The first time you run `fikkie`, a configuration template is placed in
`~/.fikkie/config.yaml`. Edit this file to specify the servers you want to
monitor and which notifyers should be used.

For more info about setting up `fikkie`, see the [documentation](https://nootr.github.io/fikkie).
