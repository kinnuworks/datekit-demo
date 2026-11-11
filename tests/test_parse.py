from datetime import date

from datekit import add_months, days_in_month, parse_iso


def test_parse_iso():
    assert parse_iso("2026-11-11") == date(2026, 11, 11)


def test_parse_iso_strips_spaces():
    assert parse_iso(" 2026-01-02 ") == date(2026, 1, 2)


def test_days_in_month_leap():
    assert days_in_month(2024, 2) == 29


def test_add_months_simple():
    assert add_months(date(2026, 1, 15), 1) == date(2026, 2, 15)


def test_add_months_clamps_to_month_end():
    assert add_months(date(2026, 1, 31), 1) == date(2026, 2, 28)


def test_add_months_across_year():
    assert add_months(date(2026, 11, 30), 3) == date(2027, 2, 28)


def test_add_months_negative():
    assert add_months(date(2026, 3, 31), -1) == date(2026, 2, 28)
