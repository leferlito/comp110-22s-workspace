"""Examples of importing in python."""


from lessons import helpers
from lessons import helpers as hp
# helpers is now synonimous to "hp"

# import names defined globally
# alias a module / imported name as another name 
from lessons.helpers import powerful, THE_ANSWER


def main() -> None: 
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    # need module name.function to call in diff module
    print(f"The answer: {hp.THE_ANSWER}")
    print(powerful(4, 2))
    print(THE_ANSWER)


if __name__ == "__main__": 
    main()