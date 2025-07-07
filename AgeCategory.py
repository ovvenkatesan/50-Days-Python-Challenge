# AgeCategory.py

def determine_age_category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

if __name__ == "__main__":
    age = int(input("Enter age: "))
    category = determine_age_category(age)
    print(f"Age category: {category}")
