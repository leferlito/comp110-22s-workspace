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


def column_values(table: list[dict[str, str]], column: str) -> list[str]: 
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table: 
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]: 
    """Transform table from row-oriented to column-oriented."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row: 
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]: 
    """Return the column-based table with only the n rows of data for each column."""
    result: dict[str, list[str]] = {}
    for item in table: 
        store_n_values: list[str] = []
        i: int = 0 
        while i < n: 
            store_n_values.append(table[item][i])
            i += 1
        result[item] = store_n_values    
    return result


def select(table: dict[str, list[str]], columns_list: list[str]) -> dict[str, list[str]]: 
    """Return a new column-based table with a specific subset of the original colimns."""
    result: dict[str, list[str]] = {}
    for item in columns_list: 
        if item in table: 
            result[item] = table[item]
    return result 


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for key in one: 
        result[key] = one[key]
    for key in two: 
        if key in result: 
            for item in two[key]:
                result[key].append(item)
        else: 
            result[key] = two[key]
    return result


def count(a_list: list[str]) -> dict[str, int]: 
    """Count the number of times a value appears in the input list."""
    result: dict[str, int] = {}
    for item in a_list: 
        if item in result: 
            result[item] += 1
        else: 
            result[item] = 1
    return result 