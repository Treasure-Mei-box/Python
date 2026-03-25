#(key-value) pair -> key is unique and no duplicate accepted
#dictionary -> unordered but ordered after python version 3.7+ 
#mutable -> changable
#indexable -> by key

mylist = []
list1 = [2,4,6,8]

my_tuple = ()
tuple1 = (1,2,3,4)

my_set = set()
set1 = {1,2,3,4,}

#dictionary

empty_dict = {}
dict1 = {"name":"Alice","Age":25,"City":"New York"} #{key:value , key:value , key:value}

#using dict() constructor
dict2 = dict(name= "Bob", age = 30, City = "Los Angeles")

person = {"name":"John" , "Age": 30 ,"City":"London"}
print(person)

#   accessing dictionary values using key
print(person["name"])
print(person["Age"])
print(person["City"])

#accessing dictionary using .get() method => safe method as if the "KEY" not exist -> return NONE instead of key error if use normal method

print(person.get("Name")) 
print(person.get("name"))

#Modifying dictionary, Add/ Update can only modified VALUE

person["email"] = "John@gmail.com"
print(person.get("email"))

person["Age"] = 35
print(person.get("Age"))

# 1. Removing item using del
#del person["City"]
print(person)

# 2. Removing item using pop
#email = person.pop("email")
print(person)
#print("Removed email: ", email)

## 3. Removing item using popitem() -> remove the last item automatically and return
last_item = person.popitem()
print(person)
print("Item Removed:", last_item)

myitem = person.popitem()
print(person)
print("Item Removed: ", myitem)
