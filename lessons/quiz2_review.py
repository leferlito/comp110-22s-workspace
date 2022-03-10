"""Quiz 2 Review Code Writing."""


def vowels_and_threes(string: str) -> str: 
    """Docstring."""
    vowels_list: list[str] = ["a", "e", "i", "o", "u"]
    result: str = ""
    i: int = 0 
    while i < len(string): 
        for char in vowels_list: 
            if char == string[i] and i % 3 != 0: 
                result += string[i]
            if char != string[i] and i % 3 == 0: 
                result += string[i]
        i += 1
    return result 


string = "comp110"
print(vowels_and_threes(string))
