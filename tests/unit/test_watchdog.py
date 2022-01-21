import pytest

from fikkie.watchdog import WatchDog


def test_watchdog_load_config(watchdog):
    assert len(watchdog.checks) == 1
    assert len(watchdog._notifiers) == 1


def test_watchdog_notify_no_icon(watchdog, mock_notifier):
    message = "Lorem ipsum"
    watchdog.notify(message)

    mock_notifier.notify.assert_called_with(message)


def test_watchdog_notify_utf8(watchdog, mock_notifier):
    mock_notifier.ENCODING = "UTF-8"

    message = "Lorem ipsum"
    icon = "!"
    watchdog.notify(message, icon)

    mock_notifier.notify.assert_called_with(f"{icon} {message}")


def test_watchdog_notify_ascii(watchdog, mock_notifier):
    mock_notifier.ENCODING = "ASCII"

    message = "Lorem ipsum"
    icon = "!"
    watchdog.notify(message, icon)

    mock_notifier.notify.assert_called_with(message)


@pytest.mark.parametrize("changed", (True, False))
@pytest.mark.parametrize("expected", (True, False))
def test_watchdog_tick(mocker, watchdog, mock_notifier, changed, expected):
    check = mocker.Mock()
    check.run.return_value = (changed, expected, "foo", "bar")
    watchdog.checks = [check]

    watchdog.tick()

    check.run.assert_called()

    if changed and expected:
        mock_notifier.notify.assert_called()
    elif changed and not expected:
        mock_notifier.notify.assert_called()
    elif not changed and expected:
        mock_notifier.notify.assert_not_called()
    elif not changed and not expected:
        mock_notifier.notify.assert_not_called()
