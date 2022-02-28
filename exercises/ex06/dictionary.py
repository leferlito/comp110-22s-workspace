"""Three dictionary functions: invert, favorite_color, and count."""

__author__ = "730483024"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of the given dictionary."""
    result: dict[str, str] = {}
    for x in a:
        if a[x] in result: 
            raise KeyError("KeyError: Duplicate Keys") 
        result[a[x]] = x
    return result


def favorite_colors(a: dict[str, str]) -> str: 
    """Returns a string of which color appeared most frequently.""" 
    result: dict[str, int] = {}
    for x in a: 
        if a[x] in result: 
            result[a[x]] += 1
        else: 
            result[a[x]] = 1
    max: int = 0 
    answer: str = ""
    for key in result: 
        if result[key] > max: 
            max = result[key]
            answer = key 
    return answer


def count(a: list[str]) -> dict[str, int]:
    """Each key is a unique value in the given list and each value associated with the key is the count of the number of times it appeared in the given list."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(a): 
        if a[i] in result: 
            result[a[i]] += 1
        else: 
            result[a[i]] = 1
        i += 1
    return result