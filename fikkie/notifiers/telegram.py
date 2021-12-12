from telegram import Bot


class TelegramNotifier:
    TYPE = "telegram"

    def __init__(self, token: str, chat_id: str):
        self._bot = Bot(token=token)
        self._chat_id = chat_id

    def send(self, text: str) -> None:
        "Sends a message."""
        self._bot.sendMessage(chat_id=self._chat_id, text=text)
