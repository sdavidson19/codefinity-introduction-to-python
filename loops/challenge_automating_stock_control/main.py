# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

print("Processing started")

for item in inventory:
    print(f"Processing {item}")
    current_stock, min_stock, restock_amount, on_sale = inventory[item]
    while current_stock < min_stock:
        current_stock +=restock_amount
        #print(current_stock, min_stock, restock_amount, on_sale)
    inventory[item][0] = current_stock
    discount_threshold = 100
    if current_stock > discount_threshold and on_sale == False:
        inventory[item][3] = True
    
print("Processing completed")