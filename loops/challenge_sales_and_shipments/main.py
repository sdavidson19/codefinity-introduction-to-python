# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

for i in range(len(products)):
    product_in_stock = products[i]
    product_sold = units_sold[i]

    products[i][1] = product_in_stock[1] - product_sold[1]
    print(products)

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for i in range(len(products)):
    product_in_stock = products[i]
    product_update = shipment_received[i]
    products[i][1] = product_in_stock[1] + product_update[1]

print("Final stock levels for all products:", products)