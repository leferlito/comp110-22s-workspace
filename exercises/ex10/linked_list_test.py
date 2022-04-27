"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, max, linkify, is_equal, scale

__author__ = "730483024"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None: 
    """Value of an empty list should raise an IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 4) 


def test_value_at_non_empty() -> None: 
    """Value of a non-empty list should return its value at a given index."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert value_at(linked_list, 1) == 20


def test_max_empty() -> None:
    """Max of an empty list should raise an ValueError."""
    with pytest.raises(ValueError): 
        max(None)


def test_max_not_empty() -> None: 
    """Max of a non-empty llist should return the largest data value."""
    linked_list = Node(10, Node(30, Node(20, None)))
    assert max(linked_list) == 30


def test_linkify_empty() -> None: 
    """Linkify of an empty list should return None."""
    items: list[int] = []
    assert linkify(items) is None


def test_linkify_not_empty() -> None: 
    """Linkify of a non-empty list should return inked list of Nodes with the same values, in the same order, as the input list."""
    items: list[int] = [10, 20, 30, 40]
    assert is_equal(Node(10, Node(20, Node(30, Node(40, None)))), linkify(items))


def test_scale_empty() -> None: 
    """Scale for an empty list shoulf return None."""
    assert scale(None, 4) is None


def test_scale_not_empty() -> None: 
    """Scale for a non-empty list should return a linked list of Nodes each multiplied by a factor."""
    head: Node = Node(10, Node(20, Node(30, Node(40, None))))
    assert is_equal(Node(20, Node(40, Node(60, Node(80, None)))), scale(head, 2))