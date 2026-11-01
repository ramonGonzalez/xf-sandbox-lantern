"""Brightness display helpers."""


def display_lumens(raw: int) -> int:
    """Return the lumens value shown in the UI."""
    return int(round(raw / 10) * 10)
