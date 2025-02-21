cart = {}

def display_item(total):
    print("Item\t\tPrice")
    for key,value in cart.items():
        print(f"{key}\t\t{value}")
    print("Total amount is :",total)

    
total = 0

while True:
    print("1.Add product")
    print("2.Remove product")
    print("3.Display products")
    print("4.exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        item = input("Enter item : ")
        price = int(input("Enter price amount : "))

        cart[item] = price
        total = total + price
    
    elif choice == 2:
        item_remove = input("Enter the item to remove :")
        total = total - cart[item_remove]
        cart.pop(item_remove)
    
    elif choice == 3:
        display_item(total)
    
    elif choice == 4:
        break
        
    else:
        print("Invalid input ")