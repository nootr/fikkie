# 🔥 Fikkie

> A simple lightweight watchdog which monitors external services over SSH.

![CI/CD](https://github.com/nootr/fikkie/actions/workflows/main.yml/badge.svg)

## Quick links

* [Installation](#installation)
* [Config example](#config-example)
* [Documentation](https://nootr.github.io/fikkie/)
* [Contributing](#contributing)

## Introduction

Why use fikkie?

* Fikkie is *easy* to set up
* Fikkie is *lightweight*
* Fikkie is *flexible* enough to be used for any service

Simply specify which commands should be run on which servers and what output is
expected, and fikkie will let you know when something's wrong.

## Installation

Install fikkie using pip:

```bash
pip install fikkie
```

## Config example

The fikkie configuration file is placed at `~/.fikkie/config.yaml` by default
and could look something like this:

```yaml
---
ssh:
  username: fikkie

servers:
  primary.foo.com:
    - description: 'MariaDB'
      command: 'sudo systemctl status mariadb | grep "Active: active" -c'
      expected: '1'
    - description: 'HTTP code foo.com'
      command: 'curl -s -o /dev/null -w "%{http_code}" foo.com'
      expected: '200'

notifier:
  - type: telegram
    token: '1234:abcd'
    chat_id: 1234
```

## Contributing

Contributions to fikkie are welcome!

1. Fork this repository and create a new branch for your feature or bugfix.
2. Make your changes.
3. Make sure to add the necessary tests.
4. Send a pull request!
