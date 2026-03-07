#for loop , sequence -> list, tuple , string
# for variable in sequence : \n code block

# if want to extect data from list, tuple, dictionary, use for. no need to tell where to start and end like WHILE       
# while loop cannot use

''' 
mylist = ['me', 'u' , 'we' , 'i']
mylist1 = "i me my mine"
numlist = [1, 3, 5, 7]
print (mylist)
print(numlist)

for var in mylist:
    print(var , end= " ")
    
for num in numlist:
    print(num, end=" ")
    
for char in mylist1:
    print(char, end= " ")
    
'''

'''
#range(start, stop, stepsize)
print(range(10))
print(list(range(10)))
print(list(range(2,6)))
print(list(range(1,100,10)))

#for num in list(range(3,16,3)): #start from 3 , stop at 16, with size up/down 3(+/- 3)
for num in range(3,16,3):
    print(num , end=" ")
    print(f"{num}* 5 = {num * 5}")
    
print(list(range(3,16,3)))
'''
'''
print(range(10))
print(list(range(10)))
print(list(range(2,10)))
print(list(range(0, 100, 10)))
list1 = range(0,100,10)

#for num in list(range(0,100,10)):
for num in list1:
    print(num , end = " ")
    print(f"{num}* 2 = {num*2}")

'''

#nested loop example 1

myNested = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
'''
for i in range(len(myNested)): #outer loop , i=0 till i =3
    for j in range(len(myNested[i])): # inner loop , j=0 till j=2
        print(myNested[i][j], end =" ")
    print()
    
'''

'''
for i in myNested: #outer loop 
    for j in i: #inner loop 
        print((j), end=" * ")
    print()
'''

#Exercise 1
'''
for i in range(1,11):
    for j in range(1,11):
        print(f"{i*j : 5}" , end=" ")
    print()
'''

#Exercise 2
'''
name_list = ["Peter", "Tommy", "George", "Sanchaz","Geo"]
for name in name_list:
    if name[1] == "e" and len(name) >= 4:
        print(name)
        
'''

#Exercise 3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    a,b = b,a
for num in range(a,b+1):
    if str(num)[-1] in['3','7']: #replace with * if the num ending in 3 or 7
        print("*" , end =" ")
    else:
        print(num, end=" ")