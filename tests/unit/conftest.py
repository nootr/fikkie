import pytest
import sys

from fikkie.check import Check
from fikkie.notifiers.discord import DiscordNotifier
from fikkie.notifiers.email import EmailNotifier
from fikkie.notifiers.slack import SlackNotifier
from fikkie.notifiers.telegram import TelegramNotifier
from fikkie.watchdog import WatchDog


# Imports


@pytest.fixture
def mock_slack_sdk_import(mocker):
    sys.modules["slack_sdk"] = mocker.Mock()


@pytest.fixture
def mock_telegram_import(mocker):
    sys.modules["telegram"] = mocker.Mock()


@pytest.fixture
def mock_hikari_import(mocker):
    sys.modules["hikari"] = mocker.Mock()


# Data


@pytest.fixture
def mock_config_data():
    yield {
        "heartbeat": {"schedule": {"hour": 13, "minute": 37}},
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
def mock_config_no_heartbeat_data(mock_config_data):
    config = mock_config_data
    config["heartbeat"] = {"enable": False}
    yield config


@pytest.fixture
def mock_check_status():
    yield ("foo", "bar", "baz")


@pytest.fixture
def mock_ssh_output():
    yield ("foo_stdout", "bar_stderr")


# Mocks


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
def mock_file(mocker):
    yield mocker.Mock()


@pytest.fixture
def mock_hikari_rest_app_client(mocker, awaitable_magicmock):
    yield mocker.MagicMock()


@pytest.fixture
def mock_hikari_rest_app(mocker, mock_hikari_rest_app_client):
    mock_acquired = mocker.MagicMock()
    mock_acquired.__aenter__.return_value = mock_hikari_rest_app_client
    rest_app = mocker.Mock()
    rest_app.acquire.return_value = mock_acquired
    yield rest_app


# Classes with mocked environment


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
    mocker.patch("fikkie.watchdog.Notifier", return_value=mock_notifier)
    mocker.patch("fikkie.watchdog.Check", return_value=check)
    yield WatchDog()


@pytest.fixture
def discord_notifier(mocker, mock_hikari_rest_app, mock_hikari_import):
    mocker.patch("hikari.RESTApp", return_value=mock_hikari_rest_app)
    yield DiscordNotifier(token="foo", channel_id=1234)


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
def slack_notifier(mocker, mock_bot, mock_slack_sdk_import):
    mocker.patch("slack_sdk.WebClient", return_value=mock_bot)
    yield SlackNotifier(token="foo", channel_id="bar")


@pytest.fixture
def telegram_notifier(mocker, mock_bot, mock_telegram_import):
    mocker.patch("telegram.Bot", return_value=mock_bot)
    yield TelegramNotifier(token="foo", chat_id="bar")


# Patches


@pytest.fixture
def mock_no_config(mocker):
    yield mocker.patch("os.path.isdir", return_value=False)


@pytest.fixture
def mock_os_mkdir(mocker):
    yield mocker.patch("os.mkdir")


@pytest.fixture
def mock_open(mocker, mock_file):
    _mock_open = mocker.MagicMock()
    _mock_open.__enter__.return_value = mock_file
    yield mocker.patch("builtins.open", return_value=_mock_open)


@pytest.fixture
def awaitable_magicmock(mocker):
    async def _async_method():
        pass

    mocker.MagicMock.__await__ = lambda x: _async_method().__await__()


@pytest.fixture
def mock_config(mocker, mock_config_data):
    mocker.patch("fikkie.config.load_config", return_value=mock_config_data)
    mocker.patch("fikkie.watchdog.load_config", return_value=mock_config_data)


@pytest.fixture
def mock_config_no_heartbeat(mocker, mock_config_no_heartbeat_data):
    mocker.patch(
        "fikkie.config.load_config", return_value=mock_config_no_heartbeat_data
    )
