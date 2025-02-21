inventory = {}

def add_product(product_name, quantity):
    if product_name in inventory:
        print(f"{product_name} already exists in the inventory. Use update_product to change the quantity.")
    else:
        inventory[product_name] = quantity
        print(f"{product_name} added with quantity {quantity}.")

def update_product(product_name, quantity):
    if product_name in inventory:
        inventory[product_name] += quantity
        print(f"{product_name} updated. New quantity: {inventory[product_name]}")
    else:
        print(f"{product_name} does not exist in the inventory. Use add_product to add the product.")

def delete_product(product_name):
    if product_name in inventory:
        del inventory[product_name]
        print(f"{product_name} removed from the inventory.")
    else:
        print(f"{product_name} does not exist in the inventory.")

def display_inventory():
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Current Inventory:")
        for product_name, quantity in inventory.items():
            print(f"{product_name}: {quantity}")

def menu():
    while True:
        print("\n1. Add Product")
        print("2. Update Product Quantity")
        print("3. Delete Product")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            add_product(product_name, quantity)

        elif choice == '2':
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity to update (use negative values to reduce quantity): "))
            update_product(product_name, quantity)

        elif choice == '3':
            product_name = input("Enter product name to delete: ")
            delete_product(product_name)

        elif choice == '4':
            display_inventory()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

menu()
