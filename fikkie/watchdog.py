import logging
import os
import subprocess

from .config import CONFIG
from .notifiers import Notifier


__all__ = ['WatchDog']


class WatchDog:
    """
    Executes commands over SSH and notifies when the output is unexpected.

    Will keep track of the state to avoid excessive notification spamming.
    """
    def __init__(self):
        self._ssh_config: dict[str, str] = CONFIG.get('ssh', {})
        self._checks: dict[str, list[str]] = CONFIG.get('servers', {})
        self._notifiers: list[Notifier] = [
            Notifier(**n) for n in CONFIG.get('notifiers', [])
        ]

    def notify(self, msg: str) -> None:
        """Sends a notification using all available notifiers."""
        for notifier in self._notifiers:
            notifier.notify(msg)

    def _execute_ssh_command(self, host: str, command: str) -> str:
        """Executes an SSH command and returns stdout and stderr."""
        username = self._ssh_config.get("username", "fikkie")

        result = subprocess.run(
            [
                "ssh",
                "-l",
                username,
                host,
                "--",
                command,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        def _decode(b):
            return b.decode("utf-8").strip() if b else ""

        return _decode(result.stdout), _decode(result.stderr)

    def tick(self) -> None:
        """Perform checks."""
        for hostname, checks in self._checks.items():
            for check in checks:
                logging.debug(f"{hostname}: {check['command']}")
                stdout, stderr = self._execute_ssh_command(
                    hostname, check['command']
                )
                logging.debug(f"Expected: '{check['expected']}'")
                logging.debug(f"Result: '{stdout}'")
                logging.debug(f"stderr: '{stderr}'")

                if stdout == check["expected"]:
                    self.notify(f"[OK] {hostname}: {stdout}")
                else:
                    self.notify(f"[NOK] {hostname}: {stdout} ({stderr})")
