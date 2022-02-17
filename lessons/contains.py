"""Example of a function that searches through a list."""

# Define a function that contains 
# Two parameters: 
# 1. needle - the string that we are searching for 
# 2. haystack - the list we are searching through 
# Algorithm:


def main() -> None: 
    print(contains("Kevin Bacon", ["Kanye West", "Pete Davidson"]))


def contains(needle: str, haystack: list[str]) -> bool:
    # For each item in the haystack
    #     Test if it is equal to the needle 
    #           If so, return True
    for item in haystack: 
        if item == needle: 
            return True
    #     After testing all items, return False, because not found
    # Returns True if needle is in haystack, False if otherwise
    return False


if __name__ == "__main__":
    main()
# else: 
#     print(__name__)