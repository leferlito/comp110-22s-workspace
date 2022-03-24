"""An example of Union types."""

from typing import Union


def log(info: Union[int, str]) -> None: 
    """Log is a function that can be called with _either_ an int or str argument."""
    if isinstance(info, str): 
        print(f"str: {info}")
    else: 
        print(f"int: {info}")


log("Hello, World")  # print function is a union function of all types
log(110)