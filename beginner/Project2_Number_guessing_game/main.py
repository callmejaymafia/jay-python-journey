from utils import (
    display_message,
    invalid_input_message,
    too_low_message,
    too_high_message,
    congrats_message,
    ask_play_again,
)
from game_logics import generate_number, check_guess

MIN_VALUE = 1
MAX_VALUE = 50


def play_round(name: str):
    target = generate_number(MIN_VALUE, MAX_VALUE)
    attempts = 0

    while True:
        raw = input(f"Enter your guess ({MIN_VALUE}-{MAX_VALUE}): ").strip()
        try:
            guess = int(raw)
        except ValueError:
            invalid_input_message()
            continue

        if guess < MIN_VALUE or guess > MAX_VALUE:
            invalid_input_message()
            continue

        attempts += 1
        result = check_guess(guess, target)

        if result == "low":
            too_low_message()
        elif result == "high":
            too_high_message()
        else:  # correct
            congrats_message(name, target, attempts)
            break


def main():
    name = display_message()
    while True:
        play_round(name)
        if not ask_play_again():
            print("\nThanks for playing — goodbye!\n")
            break


if __name__ == "__main__":
    main()
