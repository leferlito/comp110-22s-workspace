"""EX02 One Shot Wordle"""

__author__ = "730483024"

secret: str = "python"
the_guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
answer: str = ""

while len(the_guess) != len(secret):
    the_guess: str = input(f"That was not {len(secret)} letters! Try again: ")

while i < len(secret):
    alternate_indices: int = 0
    exist_elsewhere: bool = False
    if the_guess[i] == secret[i]:
        answer = answer + GREEN_BOX
    if the_guess[i] != secret[i] and i < len(secret):
        while alternate_indices < len(secret) and not exist_elsewhere:
            if the_guess[i] == secret[alternate_indices]:
                exist_elsewhere = True
            else:
                alternate_indices += 1
        if exist_elsewhere:
            answer = answer + YELLOW_BOX
        if not exist_elsewhere:
            answer = answer + WHITE_BOX
    i = i + 1

if the_guess != secret:
    print(f"{answer} \nNot quite. Play again soon! ")
if the_guess == secret:
    print(f"{answer} \nWoo! You got it! ")
