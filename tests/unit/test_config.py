import pytest

from fikkie.config import get_schedule


def test_schedule(mock_config):
    schedule, timezone = get_schedule()

    assert schedule["tick"]["schedule"] == 60
    assert schedule["heartbeat"]["schedule"].minute == {37}
    assert schedule["heartbeat"]["schedule"].hour == {13}
    assert schedule["heartbeat"]["schedule"].day_of_week == set(range(7))
    assert schedule["heartbeat"]["schedule"].day_of_month == set(range(1, 32))
    assert timezone == "UTC"


def test_default_schedule_no_config(mock_no_config):
    schedule, timezone = get_schedule()

    assert schedule["tick"]["schedule"] == 60
    assert schedule["heartbeat"]["schedule"].minute == {0}
    assert schedule["heartbeat"]["schedule"].hour == {12}
    assert schedule["heartbeat"]["schedule"].day_of_week == set(range(7))
    assert schedule["heartbeat"]["schedule"].day_of_month == set(range(1, 32))
    assert timezone == "UTC"


def test_disable_heartbeat(mock_config_no_heartbeat):
    schedule, _ = get_schedule()

    assert "tick" in schedule
    assert "heartbeat" not in schedule
