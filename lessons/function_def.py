"""An example function definition."""


def my_max(a: int, b: int) -> int: 
    """Returns the largest argument."""
    if a >= b: 
        return a
    else: 
        return b 


print(my_max(10 + 1, 10))
result: int = my_max(-50, 100)
print(result)