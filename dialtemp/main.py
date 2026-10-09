import sys
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def main():
    print("Welcome to DialTemp Console App")
    while True:
        print("\nMenu:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        try:
            choice = input("Enter your choice (1-3): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)

        if choice == '1':
            try:
                val_str = input("Enter temperature in Celsius: ").strip()
                res = celsius_to_fahrenheit(val_str)
                print(f"{val_str} C = {res} F")
            except ValueError as e:
                print(f"Error: {e}")
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled.")
        elif choice == '2':
            try:
                val_str = input("Enter temperature in Fahrenheit: ").strip()
                res = fahrenheit_to_celsius(val_str)
                print(f"{val_str} F = {res} C")
            except ValueError as e:
                print(f"Error: {e}")
            except (KeyboardInterrupt, EOFError):
                print("\nOperation cancelled.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
