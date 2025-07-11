def count_numbers(numbers):
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    return positive_count, negative_count, zero_count

if __name__ == "__main__":
    # Example usage:
    my_list = [1, -2, 0, 5, -10, 0, 7, -3]
    pos, neg, zero = count_numbers(my_list)

    print(f"List: {my_list}")
    print(f"Positive numbers: {pos}")
    print(f"Negative numbers: {neg}")
    print(f"Zero numbers: {zero}")

    my_list_2 = [-1, -2, -3, 0, 0, 0, 1, 2, 3]
    pos_2, neg_2, zero_2 = count_numbers(my_list_2)

    print(f"\nList: {my_list_2}")
    print(f"Positive numbers: {pos_2}")
    print(f"Negative numbers: {neg_2}")
    print(f"Zero numbers: {zero_2}")