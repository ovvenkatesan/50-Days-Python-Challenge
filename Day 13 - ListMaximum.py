# ListMaximum.py
# Find the largest number in a list without using the built-in max() function.

def find_largest(numbers):
    """Return the largest value in a non-empty list."""
    if not numbers:
        raise ValueError("List is empty.")

    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

def main():
    # Example usage (you can modify the list or take user input instead)
    data = [14, 27, 3, 56, 9, 42]
    print("List:", data)
    print("Largest number:", find_largest(data))

if __name__ == "__main__":
    main()