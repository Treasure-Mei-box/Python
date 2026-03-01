'''
p = 5
count = 0
sum = 0
while p > 0:
    num = int(input("Enter a number: "))
    sum += num
    count += 1
    p -= 1
average = sum/count
print(f"Average number is {average}")

'''

'''
attempt = 0
success = True
while success:
    pin = input("Enter your PIN: ")
    if pin == "1234":
        print("Correct PIN entered.")
        break
    else:
        print("Incorrect PIN entered. Try Again!")
        attempt += 1
        if attempt == 3:
            success = False
else:
    print("Your account is locked. Please contact bank. ")
        
'''

#Random Number guess 
'''
import random 
MAX = int(input("Enter a value to set: "))
secret = 1 + random.randint(1,MAX)
guess = 0
num_guess = 0
while guess != secret:
    guess = int(input("Enter your guess number: "))
    if guess == secret:
        print("You Won!")
    elif guess < secret:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
num_guess += 1

'''

#MINI Project

PIN = "4567"
balance = 10000
attempts = 3

while attempts > 0:
    user = input("Enter your PIN: ")
    if user == PIN:
        choice = (input("Correct Pin entered.('Enter q to exit.')\
                           Choose an option: 1 to deposit , 2 to withdrawl ."))
        
        if choice == "1":
            deposit_amt = int(input("Enter an amount to deposit: "))
            balance += deposit_amt
            print(f"Your total amount is {balance} baht.")
            break
        
        elif choice == "2":
            withdrawl_amt = int(input("Enter an amount to withdrawl: "))
            if balance > withdrawl_amt:
                balance -= withdrawl_amt
                print(f"Your Balance is {balance} baht.") 
            else:
                print("You don't have enough funds. \
                      Thank you for using our service.")
            break  
        else:
            print("Thank you for using our service.")
            
    else:
        attempts -= 1
        print(f"Incorrect pin entered. You have {attempts} left.")
        if attempts == 0:
            print("You have exceeded attempts and card is blocked. Contact the bank.")
    