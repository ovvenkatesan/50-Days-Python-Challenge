# NumberComparison.py

def compare_numbers(num1, num2):
    """Compares two numbers and returns a string indicating their relationship."""
    if num1 > num2:
        return f"{num1} is greater than {num2}."
    elif num1 < num2:
        return f"{num1} is less than {num2}."
    else:
        return f"{num1} is equal to {num2}."

def main():
    print("Number Comparison Tool")
    print("----------------------")

    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            break # Exit loop if inputs are valid
        except ValueError:
            print("Invalid input. Please enter valid numbers only.")

    result = compare_numbers(number1, number2)
    print(result)
    print("----------------------")
    print("Comparison complete.")

if __name__ == "__main__":
    main()
