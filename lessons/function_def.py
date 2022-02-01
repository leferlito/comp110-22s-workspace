"""An example function definition."""


def my_max(a: int, b: int) -> int: 
    """Returns the largest argument."""
    if a >= b: 
        return a

    return b 


x: int = 6
y: int = 5 + 2
z: int = my_max(y, x)
print(z)