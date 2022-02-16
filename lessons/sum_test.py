"""Tests for the sum function."""
# must end title with _test.py

from lessons.sum import sum 


def test_sum_empty() -> None: 
    xs: list[float] = []
    assert sum(xs) == 0.0  # With an empty list sum should be 0.0


def test_sum_single_item() -> None: 
    xs: list[float] = [110.0]
    assert sum(xs) == 110

# python -m pytest lessons/sum_test.py
# will not work


def test_sum_many_items() -> None: 
    xs: list[float] = [1.0, 2.0, 3.0]
    assert sum(xs) == 6.0