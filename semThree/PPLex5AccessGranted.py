credentials = {'123':'456', '324':'342', '799':'007'}

def checkAccess(id, password):
    if id in credentials:
        if password == credentials[id]:
            print('Access granted')
        else:
            print('Incorrect password')
    else:
        print('Access denied')

def register():
    id = input("Enter your ID: ")
    password = input("Enter your password: ")

    credentials[id] = password

def main():
    print('1. Register')
    print('2. Check Access')
    print('3. Exit')
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            register()
        elif choice == 2:
            id = input("Enter your ID: ")
            password = input("Enter your password: ")
            checkAccess(id, password)
        elif choice == 3:
            break
        else:
            print("invalid choice")

if __name__ == '__main__':
    main()