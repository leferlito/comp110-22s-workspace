"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "YOUR PID HERE"


class Simpy:
    """Utility class for working with a column of numerical values. Simplified version of NumPy."""
    
    values: list[float] = []

    def __init__(self, values: list[float]): 
        """Constructor definition for initializetion of attributes."""
        self.values = values

    def __str__(self) -> str: 
        """Convert Simpy object into a str representation."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, number_of_values: int) -> None: 
        """..."""
        i: int = 0
        while i < number_of_values: 
            self.values.append(float_value)
            i += 1
        # problems, all are adding together in the same self object. will not reset.

    def arange(self, start: float, stop: float, step: float = 1.0) -> None: 
        """..."""
        assert step != 0.0
        i: float = start
        if start < stop: 
            while i < stop: 
                self.values.append(i)
                i += step
        # problems here with neg numbers. 
        # are my if and while conditons redundant?
        # when I use a for-in loop, I get an empty list at least
        else: 
            while i > stop: 
                self.values.append(i)
                i -= step

    # problems again adding onto self object. How do I reset?

    def sum(self) -> float: 
        """..."""
        total: float = 0.0
        i: int = 0
        while i <= len(self.values): 
            total += self.values[i]
            i += 1
        for number in range(self.values): # for the sum 1-10 one...
        return total
    # problems

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy: 
        """Vectorized concatination operator."""
        result: list[str] = []
        if isinstance(rhs, float): 
            for item in self.values:
                result.append(item + rhs)
        else: 
            assert len(self) == len(rhs.values)
            for i in range(0, len(self.values)): 
                result.append(self.values[i] + rhs.values[i])

        return Simpy(result) 
    # why does self.values not work?

    def __pow__(self, rhs: Union[float, Simpy) -> Simpy: 
        """..."""
        result: list[str] = []
        if isinstance(rhs, float): 
            for item in self.values:
                result.append(item ** rhs)
        else: 
            assert len(self) == len(rhs.values)
            for i in range(0, len(self.values)): 
                result.append(self.values[i] ** rhs.values[i])

        return Simpy(result) 

    