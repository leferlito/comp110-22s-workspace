"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None: 
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float: 
    """Raise x to the power of n."""
    return x ** n


# print("helpers.py was evaluated.")
# prints first when we run this module in imports.py

# idiom for making a module able to run as a program 
# of have its global definitions imported elsewhere.
if __name__ == "__main__": 
    main()
else: 
    # this is not idiomatic to have an else branch
    print(f"helpers.py was imported: {__name__}")