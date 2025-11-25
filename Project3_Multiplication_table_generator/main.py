# Entry point – controls flow
from table_generator.logic import generate_multiplication_table
from utils.input_handler import get_user_inputs, validate_inputs
from utils.output_handler import display_table, save_table_to_file


def main():
    print("Welcome to the Multiplication Table Generator!")
    try:
        n, start, end = get_user_inputs()
        validate_inputs(n, start, end)
    except ValueError as e:
        print(f"Input Error: {e}")
        return

    table = generate_multiplication_table(n, start, end)
    display_table(table)

    save_option = (
        input("Do you want to save the table to a file? (y/n): ").strip().lower()
    )
    if save_option == "y":
        filename = input("Enter the filename to save the table: ").strip()
        save_table_to_file(table, filename)
        print(f"Table saved to {filename}")

    print("Thank you for using the Multiplication Table Generator!")


if __name__ == "__main__":
    main()
