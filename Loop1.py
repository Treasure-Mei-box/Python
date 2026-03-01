#Loop exercise 1
''' 
num = int(input("Enter number : "))

if (num > 0):
    print("The number is positive.")
### elif (num == 0):
###    print("The number is Zero.")
    
else:
    if(num < 0):
        print("The number is Negative.")
    else:
        print("The number is Zero.")

'''
    
#Loop exercise 2
''' 
age = int(input("Enter your age : "))

if (age >= 60):
    print("You are a senior citizen.")
elif (age >= 25):
    print("You are an adult.")

elif (age >= 10 ):
    print("You are a teenager.")
    
else:
    if (age >= 0):
        print("You are a child.")
    else:
        print("Your input is invalid.")
        
'''

#Loop exercise 3 - Odd/Even
''' 
num = int(input("Enter your number: "))

if num > 0:
    if (num % 2 == 0 ):
        print("The number is positive even number.")
    else:
        if(num % 2 != 0):
            print("The number is positive odd number.")
else:
        print("The number is not positive.")

'''

#Loop exercise 4 - user/password

import getpass
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

if username == "admin" :
    if password == "password":
        print("Log in Successful.")
    elif password == "12345":
        print("Weak password. Reset!")
    else:
        print("Incorrect Password.")
    
elif username == "guest":
    if password == "guest":
        print("Welcome Guest.")
    else:
        print("Incorrect password.") 
else:
    print("Unknown Login and password.")