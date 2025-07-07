# PersonalGreeting.py

def main():
    print("Welcome to the Personal Greeter!")
    print("--------------------------------")

    # Ask for name
    name = input("What is your name? ")

    # Ask for age with input validation
    while True:
        try:
            age = int(input("How old are you? "))
            if age <= 0:
                print("Age must be a positive number. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number for your age.")

    # Ask for favorite color
    favorite_color = input("What is your favorite color? ")

    # Create personalized message
    message = f"\nHello, {name}! "
    message += f"It's wonderful to know that you are {age} years old. "
    message += f"Your favorite color, {favorite_color}, is a lovely choice! "
    message += "May your day be as vibrant as your favorite color!"

    # Display the personalized message
    print(message)
    print("--------------------------------")
    print("Thank you for using the Personal Greeter!")

if __name__ == "__main__":
    main()
