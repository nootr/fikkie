import pytest


def test_notify(mock_smtp_server, email_notifier):
    email_notifier.notify("Lorem ipsum.")

    mock_smtp_server.login.assert_called()
    mock_smtp_server.sendmail.assert_called()
