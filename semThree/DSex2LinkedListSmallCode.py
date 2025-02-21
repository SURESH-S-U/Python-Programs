head = None

def add_passenger(name, seat_number, head):
    return (name, seat_number, head)

def remove_passenger(seat_number, head):
    # Case 1: The list is empty
    if not head:
        print("No passengers to remove.")
        return head

    # Case 2: The head node itself needs to be removed
    if head[1] == seat_number:
        print(f"Removing passenger with seat number {seat_number}")
        return head[2]  # Return the next node, effectively removing the head

    # Case 3: Removing a non-head node
    current = head
    while current[2]:
        if current[2][1] == seat_number:  # Check if the next node matches
            print(f"Removing passenger with seat number {seat_number}")
            current = (current[0], current[1], current[2][2])  # Remove the node
            break
        current = current[2]  # Move to the next node

    return head

def show_passengers(head):
    if not head:
        print("No passengers in the list.")
        return

    current = head
    while current:
        print(f"Name: {current[0]}, Seat Number: {current[1]}")
        current = current[2]

# Main loop for user interaction
while True:
    print("\n1. Add Passenger")
    print("2. Remove Passenger")
    print("3. Show Passengers")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter passenger name: ")
        seat_number = int(input("Enter seat number: "))
        head = add_passenger(name, seat_number, head)
    elif choice == 2:
        seat_number = int(input("Enter seat number to remove: "))
        head = remove_passenger(seat_number, head)
    elif choice == 3:
        show_passengers(head)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
