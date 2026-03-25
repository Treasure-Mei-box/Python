# TUPLE -> ordered(order of elements is preserved) , immutable, once created data cannot be changed,removed or update
#Allow duplicate , Heterogenous -> can store different data types.

#Tuple -> suitable to use where the data wanted to be remaine the same throughout the project.
#LIST -> represented by [] 

mylist = []

#tuple creation with parenthes ()

empty_tuple = ()
int_tuple = (1,2,3,4,5)

'''
mix_tuple = ("hi",1,2,4.5,False) #heterogenous type
print(int_tuple[0])

#tuple creation without parenthes ()

packed_tuple = 1,2,3,4
print(type(packed_tuple))

name = "susu","alex","Rio"
print(type(name))

#tuple creation using tuple constructor

tuple_from_list = tuple([1,2,3,4,5]) #. <- tuple constructor - same with class name
print(type(tuple_from_list))

tuple_string = tuple("hello")
print(type(tuple_string))
print(tuple_string)

 '''
#indexing 
print(int_tuple[3])

#negative indexing
print(int_tuple[-1])

#slicing 
print(int_tuple[1:3])

#Tuple operation , concatenation (+)

a = (1,2)
b = (3,4)
print(a+b)

#repetition (*)
print(a*3)

#membership test (in) -> boolean return
print(9 in a) 

#count() 
t = (1,2,3,4,5,2,1,2,3,2)
print(t.count(2))

print(t.index(2))


person = ("Treasure","27","DataEngineer")
name,age,profession = person
print(name)
print(age)
print(profession)