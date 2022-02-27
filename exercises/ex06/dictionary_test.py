""""""

__author__ = "730483024"

from exercises.ex06.dictionary import invert   # , count, favorite_colors
from pytest import pytest  # doing this wrong?


def test_invert_edgecase() -> None: 
    """Edge case test to see if a given empty dictionary results in a empty dictionary with the invert function."""
    a_dict: dict[str, str] = {}
    assert invert(a_dict) == {}


def test_invert_keyerror() -> None:
    with pytest.raises(KeyError): 
        a_dict = {"Kris": "Jordan", "Michael": "Jordan"}
        invert(a_dict)


def test_invert_first() -> None: 
    """Correctly inverts the keys and values of a dictionary comprised of single characters."""
    a_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(a_dict) == {"z": "a", "y": "b", "x": "c"}


def test_ivert_second() -> None: 
    """Correctly inverts the keys and values of a dictionary comprised of words."""
    a_dict: dict[str, str] = {"UNC": "blue", "NCSU": "red", "UNCC": "green", "ECU": "yellow"}
    assert invert(a_dict) == {"blue": "UNC", "red": "NCSU", "green": "UNCC", "yellow": "ECU"}