from .email import EmailNotifier
from .telegram import TelegramNotifier


class Notifier:
    """
    A notifier factory which chooses the notifier based on the "type" param.
    """

    NOTIFIERS = [EmailNotifier, TelegramNotifier]

    def __new__(cls, type: str, *args, **kwargs):
        for notifier in cls.NOTIFIERS:
            if type == notifier.TYPE:
                return notifier(*args, **kwargs)
        raise ValueError(f"Unknown notifier type: {type}")
