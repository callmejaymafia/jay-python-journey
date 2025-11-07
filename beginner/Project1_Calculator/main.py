from operators import add, subtract, multiply, divide
from utils import get_number, display_menu


def main():
    while True:
        display_menu()
        choice = input("Choose operation (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            elif choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            elif choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            elif choice == "4":
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
