# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    result = []
    for price, quantity in zip(prices, quantities_sold): 
        result.append(price * quantity)
        print(result)
        
    return result
 
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
revenue_per_product.sort()

def formatted_output(revenue):
    
# Example of expected output line (do not remove):
    for product, revenue in revenue_per_product:
        print(f"{product} has total revenue of ${revenue}")
    return revenue_per_product

revenue_per_product = formatted_output(revenue)


