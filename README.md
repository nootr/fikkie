# 🔥 Fikkie

> The easiest tool for lightweight monitoring over SSH, compatible with all your
> favorite messengers!

[![CI/CD](https://github.com/nootr/fikkie/actions/workflows/main.yml/badge.svg)](https://github.com/nootr/fikkie/actions)
[![Coverage Status](https://coveralls.io/repos/github/nootr/fikkie/badge.svg?branch=main)](https://coveralls.io/github/nootr/fikkie?branch=main)
[![PyPI license](https://img.shields.io/pypi/l/fikkie.svg)](https://github.com/nootr/fikkie/blob/main/LICENSE.md)
[![PyPi version](https://badgen.net/pypi/v/fikkie/)](https://pypi.org/project/fikkie)
[![Downloads](https://pepy.tech/badge/fikkie)](https://pepy.tech/project/fikkie)
[![Docker pulls](https://img.shields.io/docker/pulls/nootr/fikkie)](https://hub.docker.com/r/nootr/fikkie)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python versions](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://pypi.python.org/pypi/fikkie/)
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
* Fikkie notifies you using your *favorite messaging service* (e.g. e-mail, Discord or
Telegram)

You just need one single YAML file to configure fikkie, so simply specify which commands
should be run on which servers and what output is expected, and fikkie will let you know
when something's wrong.


## Installation

Install fikkie using pip and initialize fikkie:

```bash
pip install fikkie
fikkie init
```

Or use Docker!

```bash
docker run \
  --mount type=bind,source=${PWD}/config.yaml,target=/root/.fikkie/config.yaml \
  nootr/fikkie
```


## Config example

The fikkie configuration file is placed at `~/.fikkie/config.yaml` by default
and could look something like this:

```yaml
servers:
  primary.foo.com:
    - description: 'MariaDB status'
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

Contributions to fikkie are more than welcome! :heart:

Please visit the
[contribution guidelines](https://github.com/nootr/fikkie/blob/main/CONTRIBUTING.md)
for more info. Also, the [Developer's guide](https://nootr.github.io/fikkie/development)
might be useful if you want to contribute code.
