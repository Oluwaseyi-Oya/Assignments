# Description: Simulate a shopping cart for an online store where users can add items, view the cart, and calculate the total cost.
# Nested Structure: List of dictionaries, where each dictionary holds item details like name, price, and quantity.
# Features:
# Add items to the cart.
# Remove items from the cart.
# Calculate the total price.
# Display the cart contents.
# from itertools import product

inventory = {"Tomato": {"price": 200, "available": 350},
             "Garden egg": {"price": 50, "available": 1000},
             "Onions": {"price": 30, "available": 500},
             "Habanero": {"price": 15, "available": 100},
             "Dish soap": {"price": 20, "available": 30}}

cart = {}

# Add items to the cart
def add_item(product, quantity):
    #first check if quantity is available in inventory
    curr_inventory = inventory[product]["available"]
    if quantity > curr_inventory:
        print (f"Sorry, we have only {curr_inventory} {product} in stock!")
    else:
        print (f"{quantity} {product} has been added to cart successfully!")
    #check if item is already in cart
    if product in cart:
        previous_quantity = cart[product]
        cart[product] = quantity + previous_quantity
        curr_cart = cart[product]
    else:
        cart[product] = quantity
    store_curr_inventory = curr_inventory - quantity
    inventory[product]["available"] = store_curr_inventory


def remove_item(product, quantity):
    if product in cart:
        previous_quantity = cart[product]
        new_quantity = previous_quantity - quantity
        if quantity < 1:
            del cart[product]
            print(f"Successfully removed {previous_quantity} amount of {product} from cart")
        else:
            cart[product] = new_quantity
            print(f"Successfully removed {quantity} amount of {product} from cart")
    else:
        print(f"{product} not in cart!")

def cart_total_price():
    total_amount = 0
    for product in cart:
        user_quantity = cart[product]
        unit_price = inventory[product]["price"]
        sub_total = user_quantity * unit_price
        total_amount = total_amount + sub_total
        print(
            f"{product} unit cost is {unit_price}, {user_quantity} unit(s) costs {sub_total}, total now {total_amount}")
        print("======================================================")
        print(f"Grand total is {total_amount}")
        print("======================================================")


# print(inventory)
add_item("Tomato", 36)
add_item("Garden egg", 12)
add_item("Onions", 59)
add_item("Habanero", 24)
remove_item("Tomato", 5)
remove_item("Habanero", 5)
add_item("Tomato", 5)
add_item("Dish soap", 10)
add_item("Tomato", 12)
print (f"Cart is {cart}")
cart_total_price()