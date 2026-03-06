
"""

import getpass
user =input("Enter your name: ")
balance = 5000
if (user == "admin" ):
    password = getpass.getpass ("Enter your password:")
    if(password == "1234" ):
        choice = input("Enter menu (1-Deposit, 2-Withdrawl,3-check balance, q-exit :)")
        if(choice == str(1)):
            deposit = int(input("Enter your deposit amount: "))
            while (deposit < 0 ):
                print(f"Invalid deposit amount. Retry! ")
                deposit = int(input("Enter your deposit amount: "))
            balance += deposit 
            print(f"Cash deposit success. \nYour balance is {balance} RM now.")  
             
        elif (choice == str(2)):
            withdrawl = int(input("Enter your withdrawl amount: "))
            while withdrawl > balance :
                print(f"Insufficient funds. Retry.")
                withdrawl = int(input("Enter your withdrawl amount: "))
            balance -= withdrawl
            print(f"Your balance is {balance}RM now.")
            
        elif (choice == str(3)):
            print(f"Your balance is {balance}RM now.")
        else:
            print("Thank you for using our service.")
        
    else:
        print("Incorrect password.Retry!")
else:
    print("Unauthorized Log in.")
    
"""

import getpass
user =input("Enter your name: ")
balance = 5000
attempt = 3
if (user == "admin"):
    
    while attempt > 0:
        password = getpass.getpass ("Enter your password:")
        
        if (password == "1234"):
            while True:
                choice = input("Enter menu (1-Deposit, 2-Withdrawl,3-check balance, q-exit :)")
                if(choice == str(1)):
                    deposit = int(input("Enter your deposit amount: "))
                    
                    while (deposit < 0 ):
                        print(f"Invalid deposit amount. Retry! ")
                        deposit = int(input("Enter your deposit amount: "))
                    balance += deposit 
                    print(f"Cash deposit success. \nYour balance is {balance} RM now.")  
                    
                elif (choice == str(2)):
                    withdrawl = int(input("Enter your withdrawl amount: "))
                    while withdrawl > balance :
                        print(f"Insufficient funds. Retry.")
                        withdrawl = int(input("Enter your withdrawl amount: "))
                    balance -= withdrawl
                    print(f"Your balance is {balance}RM now.")
            
                elif (choice == str(3)):
                    print(f"Your balance is {balance}RM now.")
                else:
                    print("Thank you for using our service.")
                    break
            break
        
        else:
            attempt -= 1
            print(f"Incorrect Password. You have {attempt} attempts left.")    
    else:
        print("Account is Locked.")   
else:
    print("Unauthorized Log in.")
