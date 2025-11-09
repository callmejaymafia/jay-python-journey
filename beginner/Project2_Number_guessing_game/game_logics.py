import random


def generate_number(min_val: int = 1, max_val: int = 50) -> int:
    """Return a random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)


def check_guess(guess: int, target: int) -> str:
    """Return 'low', 'high', or 'correct' depending on the guess."""
    if guess < target:
        return "low"
    if guess > target:
        return "high"
    return "correct"
