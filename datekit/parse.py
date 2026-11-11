import calendar
from datetime import date


def parse_iso(s: str) -> date:
    """Parse YYYY-MM-DD."""
    year, month, day = s.strip().split("-")
    return date(int(year), int(month), int(day))


def days_in_month(year: int, month: int) -> int:
    return calendar.monthrange(year, month)[1]


def add_months(d: date, n: int) -> date:
    """Add n months, clamping the day to the end of the target month."""
    total = d.year * 12 + (d.month - 1) + n
    year, month = divmod(total, 12)
    month += 1
    return date(year, month, min(d.day, days_in_month(year, month)))
