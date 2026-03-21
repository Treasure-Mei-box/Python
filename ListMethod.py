#append() -> add at the back of array


fruits = ["banana","apple","mango","durian","durian","mango","papaya","pear"]
#fruits.append("cherry")
''' 
fruits.append(5)
print(fruits)

fruits.append(["kiwi","lemon",8]) # this multi data input will create nested list rather than single element - another list in the existing list
print(fruits)
#['banana', 'apple', 'mango', 'durian', 'cherry', 5, ['kiwi', 'lemon', 8]]
'''

#extend() 
more_fruits = ["pear","melon","papaya"]
#fruits.extend(more_fruits)
# print(fruits) 
#['banana', 'apple', 'mango', 'durian', 'cherry', 'pear', 'melon', 'papaya']

#insert()
''' 
fruits.insert(3,"grape")
fruits.insert(-1,"berry")
print(fruits)

'''

#remove()
""" 
fruits.remove("apple")
print(fruits)

#pop()
more_fruits.pop(2)
print(more_fruits)

#clear() -> remove all items

fruits.clear()
print(fruits)

"""

#index() -> listname.index(element,start,end)
i = fruits.index("durian")
#print(i)

#count()
#print(fruits.count("durian"))

#sort() -> sorting in order from desc - asec
mylist = [4,2,6,1,8,9,10,12,16]
mylist.sort()
#print(mylist) 
#print(mylist)

mylist.sort(reverse=True)   #from asec - desc
#same with mylist.reverse() , reverse() method
#print(mylist)

fruits.sort() #string sorting a - z
#rint(fruits) 

fruits.sort(reverse=True) #string sorting z - a
#print(fruits)

#copy()

origin = [1,2,3]
copy = more_fruits.copy()
print(copy)