def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def display_menu():
    print(
        """
+---------------------------+
|                           |
|   ===== Calculator =====  |
|                           |
+---------------------------+
"""
    )

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
