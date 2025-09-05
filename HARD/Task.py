# List of available items with their details
items = [
    {"name": "Coke", "price": 40, "stock": 10},
    {"name": "Chips", "price": 20, "stock": 5},
    {"name": "Water", "price": 20, "stock": 8},
    {"name": "Candy", "price": 10, "stock": 20}
]

cart = []
total_cost = 0.0
money_inserted = 0.0


def show_items():
    print("\nAvailable Items:")
    for item in items:
        print(f"{item['name']} - {item['price']:.2f} ({item['stock']} in stock)")


def add_to_cart():
    global total_cost
    show_items()
    choice = input("Enter the name of the item to add: ")

    # Find the item by name
    for item in items:
        if item['name'].lower() == choice.lower():
            if item['stock'] == 0:
                print("Sorry, this item is out of stock.")
                return
            try:
                qty = int(input(f"Enter quantity of {item['name']}: "))
                if qty <= 0:
                    print("Quantity must be positive.")
                    return
                if qty > item['stock']:
                    print(f"Not enough stock. Available: {item['stock']}")
                    return
                # Add to cart
                cart.append({"item": item, "quantity": qty})
                item['stock'] -= qty
                total_cost += item['price'] * qty
                print(f"Added {qty} x {item['name']} to cart. Total: {total_cost:.2f}")
                return
            except ValueError:
                print("Please enter a valid number.")
                return
    print("Item not found.")


def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("\nYour Cart:")
    for entry in cart:
        item = entry['item']
        qty = entry['quantity']
        print(f"{qty} x {item['name']} at {item['price']:.2f} each")
    print(f"Total cost: {total_cost:.2f}")


def insert_money():
    global money_inserted
    try:
        amount = float(input("Insert money (e.g., 50): "))
        if amount <= 0:
            print("Cannot insert negative or zero amount.")
        else:
            money_inserted += amount
            print(f"Total inserted: {money_inserted:.2f}")
    except ValueError:
        print("Please enter a valid amount.")


def checkout():
    global money_inserted, total_cost, cart
    if not cart:
        print("Your cart is empty.")
        return
    if money_inserted < total_cost:
        print(f"Insufficient funds. Please insert at least {total_cost - money_inserted:.2f}")
        return

    change = money_inserted - total_cost
    print("\nDispensing items:")
    for entry in cart:
        print(f"{entry['quantity']} x {entry['item']['name']}")
    print(f"Total cost: {total_cost:.2f}")
    print(f"Money inserted: {money_inserted:.2f}")
    print(f"Change: {change:.2f}")

    # Reset for next customer
    cart.clear()
    total_cost = 0.0
    money_inserted = 0.0
    print("Thank you for your purchase!")


# Main loop
while True:
    print("\n--- Vending Machine ---")
    print("1. View Items")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Insert Money")
    print("5. Checkout")
    print("6. Exit")

    choice = input("Choose an option: ")
    if choice == '1':
        show_items()
    elif choice == '2':
        add_to_cart()
    elif choice == '3':
        view_cart()
    elif choice == '4':
        insert_money()
    elif choice == '5':
        checkout()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
