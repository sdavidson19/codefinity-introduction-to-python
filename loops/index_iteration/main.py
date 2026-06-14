prices = [29.99, 45.50, 12.75, 38.20]

discounts = [0.1, 0.20, 0.15, 0.05]


for i in range(len(prices)):
    original_price = prices[i]
    rate = discounts[i]
    
    new_price = original_price * (1 - rate)
    prices[i] = new_price
    print(f"Updated price for item {i}: ${new_price:.2f}")