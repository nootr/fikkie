from enum import Enum
from typing import Literal


__all__ = ["BaseNotifier", "Encoding"]


class Encoding(Enum):
    ASCII = 1
    UTF8 = 2


class BaseNotifier:  # pragma: no cover - base-class for typing purposes
    """A base-class for notifiers to allow typing."""

    TYPE: str = "UNKNOWN"
    ENCODING: Encoding = Encoding.UTF8

    def notify(self, text: str) -> None:
        """Sends a message."""
        raise NotImplementedError()
