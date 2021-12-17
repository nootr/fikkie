#!/usr/bin/env python

import atexit
import logging
import os
import pprint
import signal
import sys

from fikkie.config import BASE_DIR, BROKER_DIR, CONFIG_FILE, LOG_FILE, PID_FILE
from fikkie.main import app
from fikkie.watchdog import WatchDog


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
    @staticmethod
    def init():
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
    def run():
        """Start fikkie."""
        app.worker_main(["worker", "-B", "-l", "info"])

    @staticmethod
    def start():
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

        app.worker_main(["worker", "-B", "-l", "info"])

    @staticmethod
    def stop():
        """Stop the fikkie daemon."""
        try:
            with open(PID_FILE, "r") as pid_file:
                pid = int(pid_file.read().strip())
        except FileNotFoundError:
            logging.error("Could not find PID file. Is fikkie running?")
            exit(1)

        os.kill(pid, signal.SIGTERM)
        logging.info("Stopped the fikkie daemon.")

    @staticmethod
    def status(output_format="JSON-PRETTY"):
        """Get status from all servers."""

        def _dump(check):
            try:
                return check.dump()
            except ValueError:
                return check.dump(short=True)

        watchdog = WatchDog()

        if output_format == "JSON-PRETTY":
            data = {
                "Daemon running": os.path.isfile(PID_FILE),
                "checks": [_dump(check) for check in watchdog.checks],
            }
            pprint.pprint(data)
            return

        logging.error(f"Unknown output format: {output_format}")
        exit(1)
