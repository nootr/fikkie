import pytest


def test_notify(telegram_notifier, mock_bot):
    telegram_notifier.notify("Lorem ipsum.")

    mock_bot.sendMessage.assert_called()
