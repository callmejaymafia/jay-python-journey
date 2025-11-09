def display_message() -> str:
    """Show welcome banner and ask for player's name. Return the name."""
    print(
        """
+-----------------------------------------------------+
|                                                     |
|   ===== Welcome to the Number Guessing Game =====   |
|                                                     |
+-----------------------------------------------------+
        """
    )

    name = input("What's your name? ").strip()
    if not name:
        name = "Player"
    print(f"\nHello {name}....!")
    print("I'm thinking of a number between 1 and 50.")
    print("Can you guess what it is?")
    print("Let's find out!\n")
    return name


def invalid_input_message():
    print("Invalid input. Please enter an integer between 1 and 50.\n")


def too_low_message():
    print("Too low! Try again.\n")


def too_high_message():
    print("Too high! Try again.\n")


def congrats_message(name: str, target: int, attempts: int):
    print(
        f"\n Congratulations {name}! You've guessed the number {target} "
        f"in {attempts} attempts.\n"
    )


def ask_play_again() -> bool:
    answer = input("Would you like to play again? (y/n): ").strip().lower()
    return answer.startswith("y")
