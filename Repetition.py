''' 
countS = 0
Total = 10 
while countS < Total:
    print ("*", end= " ")
    countS += 1

'''
'''
evennum = 0
nTime = 5
while nTime > 0:
    print(evennum)
    evennum += 2
    nTime -= 1
    
'''

'''
num = int(input("Enter a positive number: "))
binOutput = " "

while num > 0:
    binDigit = num % 2
    binOutput = str(binDigit) + binOutput
    num = int(num/2)
    print(binOutput)

'''

'''
firstInt = int(input("Enter number 1: "))
SecondInt = int(input("Enter number 2: "))

if firstInt <= SecondInt:
    current = firstInt
    while current <= SecondInt:
        print(current, end=" ")
        current += 1
else:
    current = firstInt
    while current >= SecondInt:
        print(current, end=" ")
        current -= 1
'''

'''
num = int(input("Enter a number: "))

if num > 0 :
    current = 0
    total = 0
    while current <= num :
        total += current
        print(current, end=" ")
        #print("+", end=" ")
        
        if current < num:
            print("+" , end= " ")
        else:
            print("=" , end=" ")
            print(total)
        current += 1
else:
    print("Number should be positive. Retry!")

'''
#Assignment 1 Day 9
'''
num = int(input("Enter a number(0 - 99): "))
if 0<= num <= 99:
    if num > 0:
        while num <= 99:
            print(num)
            num += 1
    else:
        while num > 0:
            print(num)
            num -= 1
            
else:
    print("Number should be from 0 to 99 only.")

'''

''''''
left = 1
right = 100 - left
while left <= 99 and right >= 1:
        print(left, "------" , right)
        left += 1
        right -= 1
else: 
        print("Numbers only from 0 - 99 is accepted.")
        

#Assignment 2 Day 9

number = int(input("Enter a number: "))
test = number
total = 0

if test > 0:
    while test > 0:
        digit = test % 10
        if digit % 2 == 0:
            total += digit
        test = test // 10
    print(f"Sum of even number from {number} = {total}")  
else:
       print("Invalid Number. Retry!.")