# 🔥 Fikkie

> A simple lightweight watchdog which monitors external services over SSH.

![CI/CD](https://github.com/nootr/fikkie/actions/workflows/main.yml/badge.svg)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![PyPi version](https://badgen.net/pypi/v/fikkie/)](https://pypi.org/project/fikkie)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)

## Quick links

* [Installation](#installation)
* [Config example](#config-example)
* [Documentation](https://nootr.github.io/fikkie/)
* [Contributing](#contributing)
* [Changelog](https://github.com/nootr/fikkie/blob/main/CHANGELOG.md)

## Introduction

Why use fikkie?

* Fikkie is *easy* to set up
* Fikkie is *lightweight*
* Fikkie is *flexible* enough to be used for any service

Simply specify which commands should be run on which servers and what output is
expected, and fikkie will let you know when something's wrong.

## Installation

Install fikkie using pip and initialize fikkie:

```bash
pip install fikkie
fikkie --init
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
