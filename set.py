# set -> no duplicate elements allowed, unordered, mutable like list (can be changed)
"""
mylist = [2,2,4,5]
list1 = []

my_tuple = (1,23,4)
tuple1 = ()

empty_set = set() # {} -> this only not empty set 
my_set = {1,2,3,4}

fruits = {"apple","orange","pomelo","cherry"}
print(fruits)

mixed_set = {1,"python",4.2}
print(mixed_set)

duplicate_set = {1,2,3,4,1,4}
print(duplicate_set)

#set methods
#add to set single item / append in list 
s = {1,2}
s.add(3)
print(s)

#update() -> add mutiple item
s.update([5,6,7])
print(s)

#remove
#if not existing element to delete -> will give key error(value error)
s.remove(2)
print(s)

#discard -> same like Remove 
#if not existing element to delete -> print the current set
s.discard(3)
print(s)

s.discard(8)
print(s)

#pop() -> remove and return a random element usually the first element
item = s.pop()
print(s)
print(item)

#clear
s.clear()
print(s)

""" 
#--------------------------------------------------------------------------------------#

#SET OPERATION (Union, intersection,difference,symmetric difference)

#UNION symbol: | , .union()
a = {1,2,3,4}
b = {3,4,5,6}

print(a | b)
print(a.union(b))

#intersection symbol: & , .intersection()
print(a & b)
print(a.intersection(b))

#difference symbol: .difference() , - 

print(a-b)
print(a.difference(b))

##symmetric difference symbol:  ^ , .symmetric_difference()
print(a^b)
print(a.symmetric_difference(b))