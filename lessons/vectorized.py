from __future__ import annotations 
from typing import Union


class StrArray: 
    items: list[str]

    def __init__(self, items: list[str]): 
        """"""
        self.items = items 
    
    def __repr__(self) -> str: 
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray: 
        """Vectorized concatination operator."""
        result: list[str] = []

        if isinstance(rhs, str): 
            for item in self.items:
                result.append(item + rhs)
        
        else: 
            assert len(self.items) == len(rhs.items)
            # Build up the result list by concatonating each item in self.items with corresponding item in rhs.items 
            for i in range(0, len(self.items)): 
                result.append(self.items[i] + rhs.items[i])

        return StrArray(result)  # Type change from str -> StrArray return type


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + last)
print(first + " " + last)
print(last + "," + first + "!")