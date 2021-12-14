import os

from .check import Check
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

        servers = CONFIG.get('servers', {})
        self._checks: list[Check] = [
            Check(h, self._ssh_config.get('username', 'fikkie'), **c)
            for h, cs in CONFIG.get('servers', {}).items() for c in cs
        ]

        self._notifiers: list[Notifier] = [
            Notifier(**n) for n in CONFIG.get('notifiers', [])
        ]

    def notify(self, msg: str) -> None:
        """Sends a notification using all available notifiers."""
        for notifier in self._notifiers:
            notifier.notify(msg)

    def tick(self) -> None:
        """Perform checks."""
        for check in self._checks:
            stdout_changed, stdout_expected, stdout, stderr = check.run()

            if stdout_changed:
                if stdout_expected:
                    self.notify(f"[OK] {check.host}: {check.description}")
                else:
                    self.notify(
                        f"[NOK] {check.host}: {check.description}\n{stdout} (stderr: {stderr})"
                    )
