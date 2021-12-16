import pytest

from fikkie.commands import Commands


def test_scripts_init(mock_os_mkdir, mock_open, mock_file, mock_no_config):
    Commands.init()

    assert mock_os_mkdir.call_count == 4
    mock_file.write.assert_called()


def test_scripts_status(watchdog, capsys):
    Commands.status()

    output = capsys.readouterr().out

    assert "'Daemon running':" in output
    assert "'checks':" in output
