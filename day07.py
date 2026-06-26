#This is a simple food ordering system that allows users to select items from a menu, add them to their cart, and calculate the total cost of their order.


menu = {"Pizza":  250,
        "Burger":  150,
        "Pasta":  200,
        "Popcorn":  80,
        "Salad":  100,
        "Soda":  50,
        "Ice Cream":  120,
        "Coffee":  90,
        "Tea":  60,
        "Sandwich":  180}

cart = []
total = 0

print("---Welcome to the Food Ordering System!---")
for key, value in menu.items():
    print(f"{key:10}: Rs {value}")
print("--------------------------------")


while True:
    food = input("Please select an item (X to exit): ").strip()
    if food.upper() == "X":
        break

    food_name = food.title()
    if food_name in menu:
        cart.append(food_name)
    else:
        print("Item not found. Please choose a valid menu item.")


if cart:
    print("------Your Order------")
    for food in cart:
        total += menu[food]
        print(f"- {food}: Rs {menu[food]}")
    print(f"Total is: Rs {total}")
else:
    print("No items ordered.")