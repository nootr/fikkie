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


@pytest.fixture
def mock_no_config(mocker):
    yield mocker.patch("os.path.isdir", return_value=False)


@pytest.fixture
def mock_os_mkdir(mocker):
    yield mocker.patch("os.mkdir")


@pytest.fixture
def mock_file(mocker):
    yield mocker.Mock()


@pytest.fixture
def mock_open(mocker, mock_file):
    _mock_open = mocker.MagicMock()
    _mock_open.__enter__.return_value = mock_file
    yield mocker.patch("builtins.open", return_value=_mock_open)
