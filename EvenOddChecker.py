# EvenOddChecker.py

# Function to check if a single number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Function to check a list of numbers and return their even/odd status
def check_list_even_odd(numbers):
    return [(num, check_even_odd(num)) for num in numbers]

if __name__ == "__main__":
    # Check a single number
    single_number = int(input("Enter a number to check if it is Even or Odd: "))
    result = check_even_odd(single_number)
    print(f"{single_number} is {result}.")

    # Check a list of numbers
    numbers_input = input("Enter a list of numbers separated by spaces: ")
    number_list = [int(num) for num in numbers_input.strip().split()]
    list_results = check_list_even_odd(number_list)
    for num, status in list_results:
        print(f"{num} is {status}.")
