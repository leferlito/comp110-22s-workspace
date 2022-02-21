"""Contains unit test functions for only_evens, sub, concat."""

__author__ = "730483024"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_endcase() -> None:
    """Edge case test where if the given list is empty, the result is an empty list."""
    a_list: list[int] = []
    assert only_evens(a_list) == []


def test_only_evens_first() -> None: 
    """Test to see that in a simple string with one even number that only the even number is returned."""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


def test_only_evens_second() -> None:
    """Test to see that the even number is repeated many times if it is given in a list multiple times."""
    a_list: list[int] = [4, 4, 4]
    assert only_evens(a_list) == [4, 4, 4]


def test_sub_endcase() -> None: 
    """Test that the result is an empty list when the length of the list is 0, a > len of the list or b <= 0, return the empty list."""
    a_list: list[int] = []
    assert sub(a_list, -1, -2) == []


def test_sub_first() -> None: 
    """Test that a is the index where the sub-list begins and b-1 is the index where the sub-list ends."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_second() -> None: 
    """Test that when a < 0, that the function starts at the first index of the list and if b > length of the list, the function ends at the end of the list."""
    a_list: list[int] = [25, 30, 35, 40, 45, 50, 55]
    assert sub(a_list, -1, 8) == [25, 30, 35, 40, 45, 50, 55] 


def test_concat_endcase() -> None: 
    """End case test for concat function. Two empty lists concatinated should  result in an empty list."""
    a_list: list[int] = []
    b_list: list[int] = []
    assert concat(a_list, b_list) == []


def test_concat_first() -> None: 
    """Test that the two string are appended to a new string in the order they were given."""
    a_list: list[int] = [1, 2, 3]
    b_list: list[int] = [4, 5, 6]
    assert concat(a_list, b_list) == [1, 2, 3, 4, 5, 6]


def test_concat_second() -> None: 
    """Test that the two string are appended to a new string in the order they were given."""
    a_list: list[int] = [5, 10]
    b_list: list[int] = [15, 20, 25]
    assert concat(a_list, b_list) == [5, 10, 15, 20, 25]