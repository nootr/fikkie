import pytest


def test_notify(telegram_notifier, mock_bot):
    text = "Lorem ipsum."

    telegram_notifier.notify(text)

    mock_bot.sendMessage.assert_called_with(
        chat_id=telegram_notifier._chat_id, text=text
    )
