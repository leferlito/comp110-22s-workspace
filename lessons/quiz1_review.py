"""Quiz 1 Review"""
"""What would it look like for you if you write a funuction to remove white space"""

def main(): 
    """Starting point of program"""
    print(remove_ws())

def remove_ws(word:str) -> str: 
    """removes whitespace"""
    new_word: str = ""
    i: int = 0
    while i < len(word): 
        if word[i] != " ":
            new_word += word[i]
        i += 1
    return new_word


if __name__ == main 
