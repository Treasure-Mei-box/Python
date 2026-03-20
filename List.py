#Python has array, list and dictionary data structure. But List is more useful than array.
# ARRAY allows to keep same data type only. Not common in Python
''' 
arr = [10,20,30,40,50,60]

print(arr[1])

#Adding data at specific array's room
arr[1] =25
print(arr)

#adding more data, this will add at the back of orriginal array
arr.append(70)
print(arr)

#removing data
arr.remove(30)
print(arr)


for i in arr:
    print(i, end=" ")
    
'''

''' 

#importing array using ARRAY library file
import array

arr = array.array('i',[1,2,3,4,5]) # 'i' means int. 'f'-> float , 'd'-> double
for i in arr:
    print(i)
    
arr.append(60)
for i in arr:
    print(i)
    
'''

#LIST , allow to have multi data type while ARRAY not support.

''' 
mylist = []  #empty list 
nlist = [-5,-3,-1,0,1,2,3,4,5] #int list
flist = [1.1,2.2,3.3,4.4,5.5] #float list
str = ['car','house','knife','bowl','fork']

mixed_list = ["hi", 10, 3.4 , True ]
for i in mixed_list:
    print(i)
    
for i in range (len(mixed_list)):
    print(mixed_list[i], end = " ")
    
'''

#LIST Updating using assignment operator =

''' 
list = ['a',1,'b',2,'c',3,'d',4,'e',5,'f',6,'g',7]
list[2] = 'B'
print(list)

#update using slicing
list[6:8] = ["D",8]
print(list)

#Update using append() -> add one value at one time 
clist = [0,2,4,6]
clist.append(8)
print(clist)

clist.append(10)
print(clist)

#extend() -> can add several values rather than one
clist.extend([12,14,16])
print(clist)

'''


#List delete -> del / pop(), remove()
''' 
list = ['e','x','a','m','p','l','e','s']
print(list)

del list[7] # specific index
print(list)

del list[2:4] # slicing
print(list)


#pop() method
list.pop(3)  # list.pop(index number)
#print(list)

#remove() method
list.remove('a') # list.remove(character want to remove)
print(list) 

'''

mylist = [3,4,5,6]
flist = [1.1,2.2,3.3,4.4,5.5]
mixed_list = ["Hi",6.6,10,False]

#Negative indexing
alist = [13,5,7,9,11]
print(alist[-1]) # [-1] -> point the last index.

blist = ['a',1,'b',2,'c',3,'d',4,'e',5,'f',6,'g',7]
print(blist[::2]) # if using slicing operator, can mention print(blist[start:end:interval])
print(blist[1:8:2])
print(blist[1::3])
print(blist[1:4:])

