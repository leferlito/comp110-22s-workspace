"""EX01_Chardle- A cute step toward Wordle."""

__author___ = "730483024"

instances = 0
word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)
if word[0] == character:
    print(character + " found at index 0")
    instances = instances + 1
if word[1] == character:
    print(character + " found at index 1")
    instances = instances + 1
if word[2] == character:
    print(character + " found at index 2")
    instances = instances + 1
if word[3] == character:
    print(character + " found at index 3")
    instances = instances + 1
if word[4] == character:
    print(character + " found at index 4")
    instances = instances + 1
if instances == 0:
    print("No instances of " + character + " found in " + word)
if instances == 1:
    print(str(instances) + " instance of " + character + " found in " + word)
if instances >= 2:  
    print(str(instances) + " instances of " + character + " found in " + word)