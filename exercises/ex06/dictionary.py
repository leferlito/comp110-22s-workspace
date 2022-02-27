"""Three dictionary functions: invert, favorite_color and count."""

__author__ = "730483024"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of the given dictionary."""
    result: dict[str, str] = {}
    for x in a:
        result[a[x]] = x
        if result[x] == a[x]: 
            raise KeyError("KeyError: Duplicate Keys") 
    return result


def favorite_color(a: dict[str, str]) -> str: 
    """Returns a string of which color appeared most frequently.""" 
    # There is a tie, print which color came in the list first.
    result: str = ""
    for x in a: 
        if a[x] in result: 

        else: 
            a[x] = result[]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(a): 
        if a[i] in result: 
            result[a[i]] += 1
        else: 
            result[a[i]] = 1
    return result