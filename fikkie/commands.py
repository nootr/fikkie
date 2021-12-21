#!/usr/bin/env python

import atexit
import json
import logging
import os
import pprint
import signal
import sys
import yaml

from fikkie.config import BASE_DIR, BROKER_DIR, CONFIG_FILE, LOG_FILE, PID_FILE
from fikkie.main import app
from fikkie.watchdog import WatchDog

try:
    # Python 3.8+
    from typing import Literal
except ImportError:
    # Python 3.7
    from typing_extensions import Literal  # type: ignore


CONFIG_TEMPLATE = """---
## SSH config
# Fikkie needs to know which user to use to login into the servers. This will
# default to "fikkie".
#
# Example:
#
# ssh:
#   username: fikkie

## Servers
# This is where you specify the commands fikkie needs to execute over SSH to
# test them.
#
# Example:
#
# servers:
#   primary.foo.com:
#     - description: 'MariaDB'
#       command: 'sudo systemctl status mariadb | grep "Active: active" -c'
#       expected: '1'
#     - description: 'HTTP code foo.com'
#       command: 'curl -s -o /dev/null -w "%{http_code}" foo.com'
#       expected: '200'

## Notifiers
# If you want fikkie to notify state changes/problems, you'll need to specify
# the notifiers here.
#
# Example:
#
# notifiers:
#   - type: telegram
#     token: '1234:abcd'
#     chat_id: 1234
"""


class Commands:
    FORMAT_OPTIONS = ["YAML", "JSON", "JSON-PRETTY"]

    @staticmethod
    def init(*args, **kwargs):
        """Initialize fikkie's workspace."""
        if os.path.isdir(BASE_DIR):
            logging.warning("Fikkie has already been initialized!")
            exit(1)

        directories = [
            BASE_DIR,
            BROKER_DIR,
            os.path.join(BROKER_DIR, "out"),
            os.path.join(BROKER_DIR, "processed"),
        ]
        for directory in directories:
            os.mkdir(directory)

        with open(CONFIG_FILE, "x") as f:
            f.write(CONFIG_TEMPLATE)

    @staticmethod
    def run(loglevel, *args, **kwargs):
        """Start fikkie."""
        app.worker_main(["worker", "-B", "-l", loglevel])

    @staticmethod
    def start(loglevel, *args, **kwargs):
        """
        Start a fikkie daemon.

        It creates the daemon by forking two times, ensuring we can't get a controlling
        TTY. It also changes the directory to BASE_DIR to have a gaurenteed working
        directory. Finally, it redirects stdout and stderr to the log file and writes
        its PID to the PID_FILE.
        """
        if os.path.isfile(PID_FILE):
            logging.warning("PID file exists, is fikkie already running?")
            exit(1)

        if os.fork():
            logging.info("Starting a fikkie daemon.")
            sys.exit()

        os.chdir(BASE_DIR)

        if os.fork():
            sys.exit()

        sys.stderr.flush()
        sys.stdout.flush()
        with open(LOG_FILE, "a+b", 0) as log_file:
            os.dup2(log_file.fileno(), sys.stderr.fileno())
            os.dup2(log_file.fileno(), sys.stdout.fileno())

        def _delete_pid_file():
            os.remove(PID_FILE)

        atexit.register(_delete_pid_file)
        with open(PID_FILE, "w+") as pid_file:
            pid_file.write(f"{os.getpid()}")

        app.worker_main(["worker", "-B", "-l", loglevel])

    @staticmethod
    def stop(*args, **kwargs):
        """Stop the fikkie daemon."""
        try:
            with open(PID_FILE, "r") as pid_file:
                pid = int(pid_file.read().strip())
        except FileNotFoundError:
            logging.error("Could not find PID file. Is fikkie running?")
            exit(1)

        try:
            os.kill(pid, signal.SIGTERM)
            logging.info("Stopped the fikkie daemon.")
        except ProcessLookupError:
            os.remove(PID_FILE)
            logging.warning("The fikkie daemon had already stopped.")

    @staticmethod
    def status(output_format: Literal["YAML", "JSON", "JSON-PRETTY"], *args, **kwargs):
        """Get status from all servers."""

        def _dump(check):
            try:
                return check.dump()
            except ValueError:
                return check.dump(short=True)

        watchdog = WatchDog()
        data = {
            "Daemon running": os.path.isfile(PID_FILE),
            "checks": [_dump(check) for check in watchdog.checks],
        }

        if output_format.upper() == "YAML":
            print(yaml.safe_dump(data))
        elif output_format.upper() == "JSON":
            print(json.dumps(data))
        elif output_format.upper() == "JSON-PRETTY":
            pprint.pprint(data)
        else:
            logging.error(f"Unknown output format: {output_format}")
            exit(1)
