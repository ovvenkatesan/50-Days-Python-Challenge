# ShoppingBill.py

# Function to calculate total cost including tax
def calculate_total_cost(prices, tax_percentage):
    subtotal = sum(prices)
    tax_amount = subtotal * (tax_percentage / 100)
    total_cost = subtotal + tax_amount
    return total_cost

if __name__ == "__main__":
    # Prices of 3 items in INR
    item_prices = []
    for i in range(1, 4):
        price = float(input(f"Enter price of item {i} in INR: "))
        item_prices.append(price)

    # GST percentage (example: 18%)
    gst_percentage = float(input("Enter GST percentage: "))

    total = calculate_total_cost(item_prices, gst_percentage)
    print(f"Total cost including {gst_percentage}% GST: INR {total:.2f}")
