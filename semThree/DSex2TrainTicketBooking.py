def node(name,seat):
    return [name,seat,None] 
def add_passenger(head,name,seat):
    new_node=node(name,seat) 
    if not head:
        return new_node
    current=head
    while current[2]:
        current = current[2]
    current[2] = new_node
    return head
def remove_passenger(head,name):
    if not head:
        print("No passenger")
        return head
    if head[0] == name:
        return head[2]  
    current = head
    while current[2] and current[2][0] != name:
        current = current[2]
    if current[2] and current[2][0] == name:
        current[2] = current[2][2]
    else:
        print("The passenger was not found")
    return head
def print_passengers(head):
    current = head
    while current:
        print(f"Name: {current[0]}, Seat: {current[1]}", end=" -> ")
        current = current[2]
    print("None")

passenger = None
while True:
    print("\n1. Add passenger")
    print("2. Display passengers")
    print("3. Remove passenger")
    print("4. End task")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter passenger name: ")
        seat = input("Enter seat number: ")
        passenger = add_passenger(passenger, name, seat)
    elif choice == 2:
        print("Passengers in the list:")
        print_passengers(passenger)
    elif choice == 3:
        del_name = input("Enter passenger name to remove: ")
        passenger = remove_passenger(passenger, del_name)
    elif choice == 4:
        print("Thank you")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")