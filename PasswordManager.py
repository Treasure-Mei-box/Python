#Display menu first
import random
import string

entries = [ ] #list

while True: 
    print("========Simple Password Manager========")
    print("Menu: ")
    print("1.Add new entry ")
    print("2.Show all entries")
    print("3.Search by website")
    print("4.Generate random password")
    print("5.Check Password strength")
    print("6.Exit")
    choice = input("Enter your choice(1 - 6): ")
    if choice == "1":
        website = input("Enter website: ")
        username = input("Enter username or email: ")
        password = input("Enter password(Leave blank to auto generate): ")
        if password == "":
            #char = string.ascii_letters+string.digits+string.punctuation
            char = string.ascii_letters+string.digits+string.punctuation
            password ="".join(random.choice(char) for _ in range(12))
            print(f"Generated password: {password}")
            entries.append([website,username,password])
            print("Entry successfully added.")
    elif choice == "2":
        if len(entries) == 0:
            print("No entry yet.")
        else:
            print(f"======Saved entries=====")
            for entry in entries:
                print(f"Website: {entry[0]} | Username: {entry[1]} | Password: {entry[2]} ")
                
    elif choice == "3":
        search = input("Enter a website to search: ").lower()
        found = False
        for entry in entries:
            if search in entry[0].lower():
                print("Wesbite found")
                print(f"Website: {entry[0]} | Username: {entry[1]} | Password: {entry[2]} ")
                found = True
            if not found:
                print("No matching entry found.")
        
    elif choice == "4":
        length = input("Enter desire password length(default-12): ")
        if not length.isdigit():
            length = 12
        else:
            length = int(length)
            chars = string.ascii_letters+string.digits+string.punctuation
            password = "".join(random.choice(chars) for _ in range(length))
            print("Generated pasword: " , password)
    elif choice == "5":
        password = input("Enter password to check: ")
        has_upper = any(char.isupper() for char in password)
        has_lower = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        has_special = any(not char.isalnum() for char in password)
        score = has_upper+has_lower+has_digit+has_special
        print("Score: " , score)
        if len(password) >= 12 and score == 4:
            print("Strength: Strong")
        elif len(password) >= 8 and score >= 3:
            print("Strength : Moderate")
        else:
            print("Strength: Weak")
    elif choice == "6":
        print("Thank you for using our service.")
        break
    else:
        print("Invalid Choice.")