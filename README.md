# 🔥 Fikkie

> A simple lightweight watchdog which monitors external services over SSH.

[![CI/CD](https://github.com/nootr/fikkie/actions/workflows/main.yml/badge.svg)](https://github.com/nootr/fikkie/actions)
[![Coverage Status](https://coveralls.io/repos/github/nootr/fikkie/badge.svg?branch=main)](https://coveralls.io/github/nootr/fikkie?branch=main)
[![PyPI license](https://img.shields.io/pypi/l/fikkie.svg)](https://github.com/nootr/fikkie/blob/main/LICENSE.md)
[![PyPi version](https://badgen.net/pypi/v/fikkie/)](https://pypi.org/project/fikkie)
[![Downloads](https://pepy.tech/badge/fikkie)](https://pepy.tech/project/fikkie)
[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python versions](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://pypi.python.org/pypi/fikkie/)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


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
* Fikkie is *flexible* and could be used to monitor any service
* Fikkie notifies you using your *favorite messaging service* (i.e. e-mail or Telegram)

Simply specify which commands should be run on which servers and what output is
expected, and fikkie will let you know when something's wrong.

## Installation

Install fikkie using pip and initialize fikkie:

```bash
pip install fikkie
fikkie init
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

notifiers:
  - type: telegram
    token: '1234:abcd'
    chat_id: 1234
```

## Contributing

Contributions to fikkie are more than welcome!

Please visit the
[contribution guidelines](https://github.com/nootr/fikkie/blob/main/CONTRIBUTING.md)
for more info.
