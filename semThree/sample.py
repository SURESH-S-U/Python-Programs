contact = {}

def display(contact):
    print("name\t\tnumber")
    for key,value in contact.items():
        print(f"{key}\t\t{value}")

def add(contact):
    name = input()
    num = input()
    contact[name]= num

def rem(contact):
    remove = input()
    if remove in contact:
        contact.pop(remove)

def search(contact):
    ser = input()
    if ser in contact:
        print(f"number : {contact[ser]}")


while True:
    choice = int(input())

    if choice == 1:
        add(contact)
    
    elif choice== 2:
        rem(contact)
    elif choice == 3:
        search(contact)
    else:
        display(contact)