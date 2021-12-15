import pytest

from fikkie.watchdog import WatchDog


@pytest.fixture
def mock_config():
    yield {
        "servers": {
            "foo.bar": [
                {
                    "description": "foo",
                    "command": "echo foo",
                    "expected": "foo",
                }
            ]
        },
        "notifiers": [
            {
                "type": "telegram",
                "token": "1234:abcd",
                "chat_id": 1234,
            }
        ],
    }


@pytest.fixture
def mock_notifier(mocker):
    yield mocker.Mock()


@pytest.fixture
def mock_check(mocker):
    yield mocker.Mock()


@pytest.fixture
def watchdog(mocker, mock_config, mock_notifier, mock_check):
    mocker.patch("fikkie.watchdog.CONFIG", mock_config)
    mocker.patch("fikkie.watchdog.Notifier", return_value=mock_notifier)
    mocker.patch("fikkie.watchdog.Check", return_value=mock_check)
    yield WatchDog()


def test_watchdog_load_config(watchdog):
    assert len(watchdog._checks) == 1
    assert len(watchdog._notifiers) == 1


def test_watchdog_notify(watchdog, mock_notifier):
    message = "Lorem ipsum"
    watchdog.notify(message)

    mock_notifier.notify.assert_called_with(message)


@pytest.mark.parametrize("changed", (True, False))
@pytest.mark.parametrize("expected", (True, False))
def test_watchdog_tick(watchdog, mock_check, mock_notifier, changed, expected):
    mock_check.run.return_value = (changed, expected, "foo", "bar")

    watchdog.tick()

    mock_check.run.assert_called()

    if changed and expected:
        mock_notifier.notify.assert_called()
    elif changed and not expected:
        mock_notifier.notify.assert_called()
    elif not changed and expected:
        mock_notifier.notify.assert_not_called()
    elif not changed and not expected:
        mock_notifier.notify.assert_not_called()
