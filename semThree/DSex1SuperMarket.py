from collections import deque

basket = deque()
checkout = []

def add(basket):
    num_items = int(input("Enter the number of items : "))

    for i in range (num_items):
        item  = input(f"Enter the item {i+1}: ")
        basket.append(item)
    print("All items are added.")

def remove(basket):
    item  = input("Enter the item to remove : ")
    basket.remove(item)
    print(f"Item {item} removed.")

def check_basket_item(basket,checkout):
    i = 0
    while basket:
        item = basket.popleft()
        print(f"{i+1}.{item}")
        checkout.append(item)

def checkout_item(checkout):
    while checkout:
        item = checkout.pop()
        print(f"Checked out {item}.")

def main():
    while True:
        print("1.Add")
        print("2.Remove item")
        print("3.Check Basket")
        print("4.Checkout")
        print("5.Exit")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            add(basket)
        elif choice == 2:
            remove(basket)
        elif choice == 3:
            check_basket_item(basket,checkout)
        elif choice == 4:
            checkout_item(checkout)
        else:
            break

if __name__ == "__main__":
    main()