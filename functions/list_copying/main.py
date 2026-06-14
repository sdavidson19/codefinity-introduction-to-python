# List of product prices
def apply_discount(prices):
    prices_copy = prices.copy()
    for i in (range(len(prices_copy))):
        if prices_copy[i] > 2.00:
            prices_copy[i] = prices_copy[i] * 0.90
    return prices_copy

product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)
print(f"Updated product prices: ${updated_prices}")