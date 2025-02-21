contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key,value in contact.items():
        print(f"{key}\t\t{value}")

while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact\n 4. Delete contact\n 5. Exit\n Enter your choice: "))
   
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        contact[name] = phone
   
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "'s contact number is", contact[search_name])
        else:
            print("Name is not found in contact book")
   
    elif choice == 3:
        if len(contact) == 0:
            print("Empty contact book")
            
        else:
            display_contact()
   
    elif choice == 4:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact (y/n)? ")
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                display_contact()
        else:
            print("Name is not found in contact book")
   
    elif choice == 5:
        break
   
    else:
        print("Invalid choice, please try again.")
