def sum_calculator(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    return total_sum

if __name__ == "__main__":
    # Example usage:
    num = 10
    result = sum_calculator(num)
    print(f"The sum of numbers from 1 to {num} is: {result}")

    num_2 = 100
    result_2 = sum_calculator(num_2)
    print(f"The sum of numbers from 1 to {num_2} is: {result_2}")