import pytest
import sys

from fikkie.check import Check
from fikkie.watchdog import WatchDog
from fikkie.notifiers.email import EmailNotifier
from fikkie.notifiers.telegram import TelegramNotifier


@pytest.fixture
def mock_telegram_import(mocker):
    sys.modules["telegram"] = mocker.Mock()


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
def mock_smtp_server(mocker):
    yield mocker.Mock()


@pytest.fixture
def mock_bot(mocker):
    yield mocker.Mock()


@pytest.fixture
def mock_check_status():
    yield ("foo", "bar", "baz")


@pytest.fixture
def mock_ssh_output():
    yield ("foo_stdout", "bar_stderr")


@pytest.fixture
def check(mocker, mock_check_status, mock_ssh_output):
    mocker.patch("fikkie.check.Check._get_status", return_value=mock_check_status)
    mocker.patch("fikkie.check.Check._set_status")
    mocker.patch(
        "fikkie.check.Check._execute_ssh_command", return_value=mock_ssh_output
    )
    yield Check(
        host="foo.bar",
        username="baz",
        command="echo foo",
        expected="foo",
        description="Lorem ipsum.",
    )


@pytest.fixture
def watchdog(mocker, mock_config, mock_notifier, check):
    mocker.patch("fikkie.watchdog.load_config", return_value=mock_config)
    mocker.patch("fikkie.watchdog.Notifier", return_value=mock_notifier)
    mocker.patch("fikkie.watchdog.Check", return_value=check)
    yield WatchDog()


@pytest.fixture
def email_notifier(mocker, mock_smtp_server):
    _mock_server = mocker.MagicMock()
    _mock_server.__enter__.return_value = mock_smtp_server
    mocker.patch("smtplib.SMTP_SSL", return_value=_mock_server)

    yield EmailNotifier(
        recipient="foo",
        email="bar@baz.qwerty",
        password="v3rys3cr3t",
        smtp_server="foo.bar",
        smtp_port=1337,
    )


@pytest.fixture
def telegram_notifier(mocker, mock_bot, mock_telegram_import):
    mocker.patch("telegram.Bot", return_value=mock_bot)
    yield TelegramNotifier(token="foo", chat_id="bar")


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
