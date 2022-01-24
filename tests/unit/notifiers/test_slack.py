import pytest


def test_notify(slack_notifier, mock_bot):
    text = "Lorem ipsum."

    slack_notifier.notify(text)

    mock_bot.chat_postMessage.assert_called_with(
        channel=slack_notifier._channel_id, text=text
    )
