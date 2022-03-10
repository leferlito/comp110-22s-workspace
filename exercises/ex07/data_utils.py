"""Dictionary related utility functions."""

__author__ = "730483024"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]: 
    """Read the rows of a CSV into a 'table"."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result
