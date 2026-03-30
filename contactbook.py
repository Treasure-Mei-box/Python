contacts = {}
while True:
    print("\n ========= Menu For Contact book ========")
    print("1. Add new contact.")
    print("2. Search contact.")
    print("3. Delete contact.")
    print("4. Display all contact.")
    print("5. Exit.")
    
    choice = input("Enter your choice(1-5): ")
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        
        contacts [name] = number
        print(f"Contact '{name}' is added successfully.")
    elif choice == "2":
        name = input("Enter the name to search: ").lower()
        ''' 
        for contact in contacts:
            if search in contacts:
                if search == contact[name]:
                    print(f"{search}'s phone number is {number}")   
            else:    
                print(f"'{search}' is not in the contacts.")
        '''
        if name in contacts:
            print(f"{name}'s phone number is {number}") 
        else:    
                print(f"'{name}' is not in the contacts.")
            
    elif choice =="3":
        name = input("Enter name to delete: ").lower()
        if name in contacts:
            del contacts[name]
            print(f"{name} has been successfully deleted from the contacts.")
        else:
            print("{name} is not found in your contact.")
    elif choice == "4":
        if not contacts:
            print("Contact book is empty.")
        else:
            print("\n All Contacts: ")
            for name,phone in contacts.items():
                print(f"{name} - {phone}")
    elif choice == "5":
        print("You have ended the session.")
        break
    else:
        print("Invalid choice. Try again! ")
        