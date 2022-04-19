from __future__ import annotations

from typing import Optional  # Allows base case to be written more simply


class Node: 
    data: int 
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]): 
        """Construct an object of type Node."""
        self.data = data
        self.next = next
    
    def __str__(self) -> str: 
        """Print string representation of recursive method."""
        if self.next is None:
            return f"{self.data} -> None"
        else: 
            return f"{self.data} -> {self.next}"

# Procedural Recursion... (Ex. add up the data). 
# Define a function in terms of it self. 
# Begin with simplest case possible - the base case (don't need to look at other Nodes to find out)


def sum(node: Optional[Node]) -> int: 
    """Return the sum of the data in all Nodes."""
    # double equal sign works instead of 'is' too
    if node is None:  # BASE CASE (NEED AT LEAST 1)
        return 0
    else: 
        return node.data + sum(node.next)  # RECURSIVE CASE (NEED AT LEAST 1)


def count(node: Optional[Node], current_count: int = 0) -> int: 
    """Count the number of Node items."""
    # double equal sign works instead of 'is' too
    if node is None: 
        return current_count  # base case 
    else: 
        return count(node.next, current_count + 1)

# Structural recursion means we have Nodes that refer to Nodes of the same kind. Can be in one or 2 directions.
# build up lists from back to front. 
# This example is in one direction


head: Node = Node(3, None)
head = Node(2, head)
head = Node(1, head)
print(sum(head))
print(count(head))
print(head)  # calls magic __str__ method