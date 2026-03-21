nlist = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] # -> nested list
''' 
print(nlist)
print(nlist[0])
for each in nlist:
    print(each)
    
for each in range(len(nlist)):
    print(nlist[each])

''' 

''' 
1  2  3
4  5  6
7  8  9
10 11 12

'''

''' 
print(nlist[1][2]) #print(nlist[rol][col])
nlist[2][0] *= 2
nlist[2][1] *= 3
nlist[2][2] *= 4
print(nlist[2])

exlist = []
exlist.append([2,4,6])
print(exlist)
exlist.append([8,10,12])
exlist.append([14,16,18])
print(exlist)

for i in range(len(exlist)):
    for j in range(len(exlist[i])):
        print(exlist[i][j])
    print()
    
'''

#Nested list in python is similar to Matrix
A = [[1,2] , [5,6]]
B = [[0.5,1.6,7.9],[2.2,4.0,5.6],[3.5,9.8,2.9],[9.5,11.2,5.7]]
'''' 

0.5     1.6     7.9
2.2     4.0     5.6
3.5     9.8     2.9
9.5     11.2    5.7

'''

'''' 
nRow = len(B)
print(nRow)
nCol = len(B[0])
print(nCol)

for row in range(nRow):
    for col in range(nCol):
        print(B[row][col], end = " ")
    print()
    
'''

#Exercise 1
''' 
With any two lists of integer values where the first list is always smaller than the second list, if the short list is a subset of a long list, the code
prints “Yes”. Otherwise, the code prints “No.”
For examples
List_1 = [3, 4]
List_2 = [3,6,7,4]
Output is: “Yes”.
List_1 = [6,7,0]
List_2 = [3,5,7,8,9,0]
Output is: “No”.
'''
""" 
list1 = [3,4]
list2 = [3,6,7,4]
is_sub = True

for char in list1:
    if char not in list2:
        is_sub = False
        break

if is_sub:
    print("Yes")
else:
    print("No subset")
    
"""

#Exercise 2
""" 
numlist = [1,4.9,4,5,6.5,"hi","hola"]
str_list = []
flist = []
intlist = []
for item in numlist:
    if type(item) == int:
        intlist.append(item)
    elif type(item) == float:
        flist.append(item)
    elif type(item) == str:
        str_list.append(item)
print("String list:" , str_list)
print("Integer List:", intlist)
print("Float List: ", flist)

"""

#Exercise 3

''''''
nlist =[[2,5,99],[-3,8,9,10],[1,7,100]]
max = nlist[0][0]
min = nlist[0][0]

for sublist in nlist:
    for i in sublist:
        if i > max:
            max = i
        if i < min:
            min = i
print("Maximum value is ", max)
print("Minimum value is ", min)