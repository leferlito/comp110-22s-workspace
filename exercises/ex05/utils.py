"""Where functions: only_evens, sub, and concat are defined."""

__author__ = "730483024"


def only_evens(a_list: list[int]) -> list[int]: 
    """Returns a list with only the even intergers in the given list."""
    answer: list[int] = list()
    for i in a_list:
        if i % 2 == 0:
            answer.append(i) 
    return answer


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """Return a list, which is subset of the given list, between the start (inclusive) and end index (non-inclusive)."""
    answer: list[int] = list()
    # If the length of the list is 0, start > len of the list or end <= 0, return the empty list.
    if a < 0: 
        a = 0 
    if b > len(a_list) - 1: 
        b = len(a_list) - 1
    i: int = a
    while i < b:
        answer.append(a_list[i]) 
        i += 1
    return answer


def concat(a_list: list[int], b_list: list[int]) -> list[int]: 
    """Combines two given lists together in order of which list was given first."""
    answer: list[int] = list()
    i: int = 0
    while i < len(a_list): 
        answer.append(a_list[i])
        i += 1
    i = 0
    while i < len(b_list): 
        answer.append(b_list[i])  
        i += 1
    return answer