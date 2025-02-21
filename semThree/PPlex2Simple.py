cart = {}

def display():
    print("Item\t\tQuantity")
    for key in cart:
        print("{}\t\t{}".format(key,cart.get(key)))

while True:
    print("1.Add item")
    print("2.Buy item")
    print("3.Updaty item")
    print("4.display item")
    print("exit.")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        item = input("Enter trhe item :")
        quantity = int(input("Enter the number of items :"))
        cart[item] = quantity
    
    if choice == 2:
        item = input("Enter the item to remove :")
        quantity = int(input("Enter the number of items :"))
        cart[item] -= quantity
        display()

    if choice == 3:
        item = input("Enter the item to update :")
        quantity = int(input("Enter the number of items :"))
        cart[item] += quantity
    
    if choice == 4:
        display()

    if choice == 5:
        break


