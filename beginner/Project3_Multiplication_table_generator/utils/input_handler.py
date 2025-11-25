# Handles all user inputs and validations
def get_user_inputs():
    n = int(input("Enter a number to generate its multiplication table: "))
    start = int(input("Enter the starting multiplier: "))
    end = int(input("Enter the ending multiplier: "))
    return n, start, end


def validate_inputs(n, start, end):
    if start > end:
        raise ValueError(
            "Starting multiplier must be less than or equal to ending multiplier."
        )
    if n < 0 or start < 0 or end < 0:
        raise ValueError("Inputs must be non-negative integers.")
    return True
