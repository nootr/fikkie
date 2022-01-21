import pytest


def test_dump_long(check):
    expected_dump = {
        "command": "echo foo",
        "description": "Lorem ipsum.",
        "expected": "foo",
        "host": "foo.bar",
        "status": "foo",
        "stdout": "bar",
        "stderr": "baz",
    }

    assert check.dump() == expected_dump


def test_dump_short(check):
    expected_dump = {
        "command": "echo foo",
        "description": "Lorem ipsum.",
        "expected": "foo",
        "host": "foo.bar",
    }

    assert check.dump(short=True) == expected_dump


def test_run(check):
    stdout_changed, is_expected, stdout, stderr = check.run()

    assert stdout_changed
    assert not is_expected
    assert stdout == "foo_stdout"
    assert stderr == "bar_stderr"
