"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730483024"


class Simpy:
    """Utility class for working with a column of numerical values. Simplified version of NumPy."""
    
    values: list[float] = []

    def __init__(self, values: list[float]): 
        """Constructor definition for initialization of attributes for Simpy class."""
        self.values = values

    def __str__(self) -> str: 
        """Convert Simpy object into a str representation."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, number_of_values: int) -> None: 
        """Fill Simpy's values with a specific number of repeating values."""
        a_list: list[float] = []
        i: int = 0
        while i < number_of_values: 
            a_list.append(float_value)
            i += 1
        self.values = a_list

    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        """Fill in the values attribute with a range of values, from start to the integer before stop."""
        a_list: list[float] = []
        assert step != 0.0
        i: float = start
        if start < stop: 
            while i < stop: 
                a_list.append(i)
                i += step
        else: 
            while i > stop: 
                a_list.append(i)
                i += step
        self.values = a_list

    def sum(self) -> float: 
        """Compute and return the sum of all items in the values attribute."""
        total: float = 0.0
        i: int = 0
        while i < len(self.values): 
            total += self.values[i]
            i += 1
    
        return total

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy: 
        """Overload the addition operator so that + can be used between two Simpy object and a Simpy and float."""
        result: list[float] = []
        if isinstance(rhs, float): 
            for item in self.values:
                result.append(item + rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)): 
                result.append(self.values[i] + rhs.values[i])
        return Simpy(result) 

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy: 
        """Overload the exponentiation operator so that ** can be used between two Simpy object and a Simpy and float."""
        result: list[float] = []
        if isinstance(rhs, float): 
            for item in self.values:
                result.append(item ** rhs)
        else: 
            assert len(self.values) == len(rhs.values)
            for i in range(0, len(self.values)): 
                result.append(self.values[i] ** rhs.values[i])
        return Simpy(result) 

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]: 
        """Overload the == operator so that it can be used between two Simpy object and a Simpy and float and create a mask."""
        mask: list[bool] = []
        if isinstance(rhs, float): 
            for item in self.values: 
                if item == rhs: 
                    mask.append(True)
                else: 
                    mask.append(False)
        else: 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    mask.append(True)
                else: 
                    mask.append(False)
                i += 1
        return mask

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]: 
        """Overload the greater than operator so that > can be used between two Simpy object and a Simpy and float and create a mask."""
        mask: list[bool] = []
        if isinstance(rhs, float): 
            for item in self.values: 
                if item > rhs: 
                    mask.append(True)
                else: 
                    mask.append(False)
        else: 
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):  
                if self.values[i] > rhs.values[i]:
                    mask.append(True)
                else: 
                    mask.append(False)
                i += 1
        return mask
    
    # def __getitem__(self, rhs: int) -> float: 
    #     """Overload the subscription notation operator for class Simpy."""
    #     index_value: float = 0.0
    #     i: int = rhs
    #     if i < len(self.values):
    #         index_value = self.values[i]
    #     else: 
    #         raise IndexError
    #     return index_value

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """..."""
        if isinstance(rhs, int): 
            index_value: float = 0.0
            i: int = rhs
            if i < len(self.values):
                index_value = self.values[i]
            else: 
                raise IndexError
            return index_value   
        # problems after here     
        else:
            mask: Union[float, Simpy]
            for item in self. values: 
                if rhs: 
                    mask[item] = True
                else: 
                    mask[item] = False
            return mask