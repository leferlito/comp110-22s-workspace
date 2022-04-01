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
        return f"{self.values}"
        # Not printing ones

    def __fill__(self, float_value: float, number_of_values: int) -> None: 
        """..."""
        i: float = 0.0
        while i <= number_of_values: 
            self.values.append(float_value)
            i += 1.0

    def __arrange__(self, start: float, stop: float, step: float) -> None: 
        """..."""
        assert step != 0.0
        i: float = start
        self.values.append(start)
        while i <= stop: 
            i += step
            self.values.append(i)

    # def __sum__(self, rhs: float) -> float: 
    #     total: float
    #     total = self + rhs
    #     return total

    def __add__(self, lhs: Union[float, Simpy]) -> Simpy: 
        """Vectorized concatination operator."""
        result: list[str] = []

        if isinstance(lhs, float): 
            for item in self.values:
                result.append(lhs + item)
        
        else: 
            assert len(self.values) == len(lhs.values)
            for i in range(0, len(self.values)): 
                result.append(self.values[i] + lhs.values[i])

        return Simpy(result) 

    