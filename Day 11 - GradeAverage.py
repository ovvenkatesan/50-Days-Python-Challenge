# GradeAverage.py
# Calculates the average of 5 test scores and determines pass/fail.

def get_score(prompt):
    """Read a single test score and validate it."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a numeric value.")

def main():
    print("=== Grade Average Calculator ===")
    scores = [get_score(f"Enter score {i+1}: ") for i in range(5)]

    average = sum(scores) / 5
    print(f"\nAverage score: {average:.2f}")

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

if __name__ == "__main__":
    main()