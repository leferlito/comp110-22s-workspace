"""Contains unit test functions for only_evens, sub, concat."""

__author__ = "730483024"

# One edge case and two use cases
# descriptive docstring of what is being tested

from exercises.ex05.utils import only_evens


def test_only_evens_endcase() -> None:
    """Edge case test for only_evens function."""
    a_list: list[int] = []
    assert only_evens(a_list) == []


def test_only_evens_first() -> None: 
    """Test."""
    a_list: list[int] = [1, 2, 3]
    assert only_evens(a_list) == [2]


def test_only_evens_second() -> None:
    """Test."""
    a_list: list[int] = [4, 4, 4]
    assert only_evens(a_list) == [4, 4, 4]


from exercises.ex05.utils import sub


def test_sub_endcase() -> None: 
    """Edge case test for sub function."""
    a_list: list[int] = []


def test_sub_first() -> None: 
    """Test."""
    
