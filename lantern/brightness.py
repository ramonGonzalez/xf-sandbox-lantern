"""Brightness display helpers."""


def display_lumens(raw: int) -> int:
    """Return the lumens value shown in the UI, rounded down to the nearest 10."""
    return (raw // 10) * 10
