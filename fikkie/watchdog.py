import logging

from .config import CONFIG
from .notifiers.telegram import TelegramNotifier


__all__ = ['WatchDog']


class WatchDog:
    """
    Executes commands over SSH and notifies when the output is unexpected.

    Will keep track of the state to avoid excessive notification spamming.
    """
    DEFAULT_SSH_USER = "fikkie"

    def __init__(self):
        ssh_config = CONFIG.get('ssh', {"username": self.DEFAULT_SSH_USER})

        self.user: str = ssh_config.get('username', self.DEFAULT_SSH_USER)
        self._checks: dict[str, list[str]] = CONFIG.get('servers', {})

    def tick(self):
        """Perform checks."""
        for hostname, checks in self._checks.items():
            for check in checks:
                logging.debug(f"Executing '{check['command']}' on {hostname}")
                logging.debug(f"Expected: '{check['expected']}'")
