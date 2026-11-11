from datetime import date

_DAYS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


def parse_iso(s: str) -> date:
    """Parse YYYY-MM-DD."""
    year, month, day = s.strip().split("-")
    return date(int(year), int(month), int(day))


def days_in_month(year: int, month: int) -> int:
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return 29
    return _DAYS[month - 1]


def add_months(d: date, n: int) -> date:
    """Add n months, clamping the day to the end of the target month."""
    total = d.year * 12 + (d.month - 1) + n
    year, month = divmod(total, 12)
    month += 1
    return d.replace(year=year, month=month, day=min(d.day, days_in_month(year, month)))
