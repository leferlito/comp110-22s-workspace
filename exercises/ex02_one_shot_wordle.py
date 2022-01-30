"""EX02 One Shot Wordle"""

__author__ = "730483024"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
ANSWER: str = ""
while len(guess) != len(secret):
    guess: str = input("That was not 6 letters! Try again: ")
while i < len(secret):
    alternate_indices: int = 0
    exist_elsewhere: bool = False
    if guess[i] == secret[i]:
        ANSWER = ANSWER + GREEN_BOX
    if guess[i] != secret[i] and i < len(secret):
        while alternate_indices < len(secret) and not exist_elsewhere:
            if guess[i] == secret[alternate_indices]:
                exist_elsewhere = True
            else:
                alternate_indices += 1
        if exist_elsewhere:
            ANSWER = ANSWER + YELLOW_BOX
        if not exist_elsewhere:
            ANSWER = ANSWER + WHITE_BOX
    i = i + 1
print(ANSWER)
if guess != secret:
    print("Not quite. Play again soon! ")
if guess == secret:
    print("Woo! You got it! ")
exit()
