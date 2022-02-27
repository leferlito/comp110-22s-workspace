"""Test functions for invert, favorite_color, and count."""

__author__ = "730483024"


from exercises.ex06.dictionary import invert, count, favorite_colors


def test_invert_edgecase() -> None: 
    """Edge case test to see if a given empty dictionary results in a empty dictionary with the invert function."""
    a_dict: dict[str, str] = {}
    assert invert(a_dict) == {}


def test_invert_first() -> None: 
    """Correctly inverts the keys and values of a dictionary comprised of single characters."""
    a_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(a_dict) == {"z": "a", "y": "b", "x": "c"}


def test_invert_second() -> None: 
    """Correctly inverts the keys and values of a dictionary comprised of words."""
    a_dict: dict[str, str] = {"UNC": "blue", "NCSU": "red", "UNCC": "green", "ECU": "yellow"}
    assert invert(a_dict) == {"blue": "UNC", "red": "NCSU", "green": "UNCC", "yellow": "ECU"}


def test_favorite_color_edgecase() -> None: 
    """Edge case test to see if a given empty dictionary results in a empty dictionary with the favorite_colors function."""
    a_dict: dict[str, str] = {}
    assert favorite_colors(a_dict) == ""


def test_favorite_color_first() -> None: 
    """Test to see if the color that is most commonly the favorite (the value in the given dictionary) is returned in a string."""
    a_dict: dict[str, str] = {"Meghan": "blue", "Lauren": "pink", "Morgan": "pink"}
    assert favorite_colors(a_dict) == "pink"


def test_favorite_color_second() -> None: 
    """Test to see if the color that is most commonly the favorite (the value in the given dictionary) is returned in a string."""
    a_dict: dict[str, str] = {"Mark": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_colors(a_dict) == "blue"


def test_count_edgecase() -> None: 
    """Edge case test to see if a given empty dictionary results in a empty dictionary with the count function."""
    a_list: list[str] = []
    assert count(a_list) == {}


def test_count_first() -> None:  # Not working
    """Tests that the returned dictionary shows each original value from the given list as a key and its values is the number of times it was repeated."""
    a_list: list[str] = ["Carly", "Carly", "Sam", "Sam"]
    assert count(a_list) == {"Carly": 2, "Sam": 2}


def test_count_second() -> None:  # Not working
    """Tests that the returned dictionary shows each original value from the given list as a key and its values is the number of times it was repeated."""
    a_list: list[str] = ["blue", "pink", "green", "pink", "blue"]
    assert count(a_list) == {"blue": 2, "pink": 2, "green": 1}