'''
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))

if (num1<= num2 <=num3) or (num3<= num2 <=num1):
    print(f"Middle number is {num2}.")
elif (num2<= num1 <=num3) or (num3 <=num1 <= num2):
    print(f"Middle number is {num1}.")
else:
    print("Middle number is", num3,".")

'''

'''
number = input("Enter 3 digits number: ")

if len(number) == 3 and number.isdigit():
    left_most_digit = int(number[0])
    if left_most_digit % 2 == 0:
        print("Your number is start with even number.")
    else:
        print("Your number is start with odd number.")
else:
    print("Invalid Number. Try again.")

'''

'''
heroName = ("Superman")
myname = input("Enter your name: ")

if (len(myname) > len(heroName)):
    print("You are stronger than Superman.")
else:
    print("You are weaker than an ant.")
    
'''

#Assignment 1
'''
height = int(input("Enter your height(cm): "))

if(height > 0):
    if(height < 80 ):
        print(f"Your height is {height}cm and you are too short for this ride.")
    elif (80 <= height <=180 ):
        print(f"Your height is OK for this ride.")
    else:
        print(f"Your height is {height}cm is too tall for this ride.")
else:
    print(f"Height should not be a negative number. Try again.")
    
'''

#Assignment 2

'''
eunit = input("Enter your total electric usage(units): ")

if eunit.isdigit():
    eunit = int(eunit) 
    if eunit > 0:
        if(eunit <= 100):
            print(f"Electric bill is FREE!")
        elif(100<eunit<=300):
            print(f"Total cost of electric bill is {(100*0) + (200*50)} MMK.")
        else:
            print(f"Total cost of electric bill is {(100*0) + (200*50) + ((eunit - 300)* 70)} MMK.")
    else:
        print(f"Total units should be a positive number.Retry!")
else:
    print(f"Invalid Input.")
    
'''

import getpass
name = input("Enter name: ")
email = input("Enter email: ")
password = getpass.getpass("Enter your password: ")

if (name == " "):
    print("Name cannot be empty.")
else: 
    if "@" not in email:
        print("Email is not valid.")
    else:
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        else:
            print("Register successful.")
            