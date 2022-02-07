"""EXO3 Structured Wordle."""

__author__ = "730483024"


def contains_char(search_string: str, character: str) -> bool:
    """Determines if a character in a string."""
    assert len(character) == 1
    i: int = 0
    in_string: bool = False
    while i < len(search_string):
        if character == search_string[i]:
            in_string = True
        i += 1
    return in_string
# Assert is a built-in that helps us assert an assumption. In this case, it makes sure that the character being searched's length is only 1.


secret: str = "codes"
guess: str = "" 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Will return yellow or white box depending on if characters from guess are in secret."""
    assert len(guess) == len(secret)
    i: int = 0
    answer: str = ""
    while i < len(secret):
        if contains_char(guess[i], secret[i]):
            answer += GREEN_BOX
            i += 1
        elif contains_char(secret, guess[i]):
            answer += YELLOW_BOX
            i += 1
        else:
            answer += WHITE_BOX
            i += 1
    return answer 
# Must always be using something to iterate in a while look to avoid infinite loops. Ex. i += 1.


def input_guess(a: int) -> str: 
    """Will prompt the player to keep guessing if the guess length is not the same as the secret."""
    error_message: str = input(f"Enter a {a} char word: ")
    while len(secret) != len(error_message):
        error_message: str = input(f"That wasn't {a} chars! Try again: ")
    return error_message


def main() -> None: 
    """The main entrypoint of the program and main game loop."""
    turn: int = 1
    player_guess: str = ""
    while turn <= 6 and player_guess != secret:
        print(f"=== Turn {turn}/6 ===") 
        player_guess = input_guess(len(secret))
        print(emojified(player_guess, secret))
        if player_guess == secret: 
            print(f"You won in {turn} turns! ")
        turn += 1
    if turn > 6: 
        print("X/6 - Sorry, try again tomorrow! ")
       
# Defining codes always moves down. This is the funtion that makes the game run how it is supposed to, but note that it is defined last, since the previously defined funtions are in main's definition.


# What is below helps you run the programs not only in the repl, but as a module.
if __name__ == "__main__":
    main()