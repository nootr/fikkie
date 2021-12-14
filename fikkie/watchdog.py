import logging

from .config import CONFIG
from .notifiers.telegram import Notifier, TelegramNotifier


__all__ = ['WatchDog']


class WatchDog:
    """
    Executes commands over SSH and notifies when the output is unexpected.

    Will keep track of the state to avoid excessive notification spamming.
    """
    DEFAULT_SSH_USER = "fikkie"
    NOTIFIERS = [TelegramNotifier]

    def __init__(self):
        ssh_config = CONFIG.get('ssh', {"username": self.DEFAULT_SSH_USER})

        self.user: str = ssh_config.get('username', self.DEFAULT_SSH_USER)
        self._checks: dict[str, list[str]] = CONFIG.get('servers', {})
        self._notifiers: list[Notifier] = [
            self._get_notifier(**n) for n in CONFIG.get('notifiers', [])
        ]

    def _get_notifier(self, type: str, **kwargs) -> Notifier:
        """Returns a notifier."""
        for notifier in self.NOTIFIERS:
            if notifier.TYPE == type:
                return notifier(**kwargs)
        raise ValueError(f"Unknown notifier type: {type}")

    def notify(self, msg: str) -> None:
        """Sends a notification using all available notifiers."""
        for notifier in self._notifiers:
            notifier.notify(msg)

    def tick(self) -> None:
        """Perform checks."""
        for hostname, checks in self._checks.items():
            for check in checks:
                logging.debug(f"Executing '{check['command']}' on {hostname}")
                logging.debug(f"Expected: '{check['expected']}'")
                self.notify(f"{hostname}: {check['expected']} OK")
