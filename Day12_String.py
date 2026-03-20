# + -> string concatenation
''' 
print("Hello " + "World " + "and " + "Python")

# * -> multi print
print("Programming" * 5 ,end=" ")

'''

'''
str1 = input("Enter sentence: ")
str2 = input("Enter search word: ")
# if in -> if wat to check 
if str2 in str1:
    print("Yes. " + "str2 is in str1")
else:
    print("Oh No.")
'''

'''
#name = "Trudy"
name = input("Enter your name:")
if name not in "Alice, BOB":
    print("Access denied.")
else:
    print("Access granted.")
    
'''

''' 
#message = "abcdefghigklmnopqrstuvwxyz"
message = input("Enter a sentence: ")
for c in message:
    if c not in "aeiou":
        print(c , end= "")
    else:
        print("*" , end="")
'''

name = "zoom"
print(name[3])

name1 = "Yadanar Theint"
print(name1[7])
print(name1[0:6])
print(name1[8:14])