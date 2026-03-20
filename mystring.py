''' 
print("Hello")
print('Hello')

x = "Hello World"
print(x[0:5])
print(x[5:11])

print(len(x))

print("alice".capitalize())
print("Alice".upper())
print("ALICE".lower())

'''

'''
print ("Alice".isupper())
print("alice".islower())


print("Alice".find("ice")) #.find() method give the location of array where it starts to find the keyword that is want to be found.
print('Alice'.find("li"))

print("Alice".replace("ice","ex"))

print("Alice,Bob".split(","))
print(",".join(["Alice","Bob"]))

'''

''' 
i = 5
print(str(i))

f = 3.14
print(int(f))

x = 3.13
if type(x) is int:
    print("x is integer")
else:
    print("It's not")
    
'''
    
#instance of -> checking whether a variable is an integer or not. | .isinstance()
''' 
x = 3.14
if isinstance(x,float):
    print("X is a float")
else:
    print("X is not.")
    
'''

#Exercise 1

sentence = "My friend and I want to go shopping and dining."
#print(sentence.upper())

#Exercise 2
''' 
message = input("Enter a sentence: ")
keyword = input("Enter a character: ")
if len(keyword) != 1:
    print("Enter only one character.")
else:
    count = sentence.count(keyword)
    print(f"The character '{keyword}' appears {count} times.")

'''

#Exercise 3
'''
while message >= "0":
    message = input("Enter a sentence: ")
    keyword = input("Enter a character: ")
    keyword1 = message.count(keyword)
    print(f"Total no. of Character {keyword} in this sentence = {keyword1}")
'''

''' 
message = input("Enter a sentence: ")
while True:
    keyword = input("Enter character to count: ")
    if keyword == '0':
        print("Exit from the program.")
        break
    elif len(keyword) != 1:
        print("Enter only one character.")
    else:
        count = message.count(keyword)
        print(f"The character '{keyword}' appears {count} times.")
'''

#Exercise 4

'''' 
sentence = input("Enter a setence: ")
filtered = ''.join(char for char in sentence if char.isalpha() or char.isspace())
print(f"Filter sentence is '{filtered}'")

'''


#Exercise 5

''' 
sentence = input("Enter a setence: ")
alphabets = 0
uppercase = 0
lowercase = 0
numeric = 0
others = 0
for char in sentence:
    if char.isalpha():
        alphabets += 1
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
    elif char.isdigit():
        numeric += 1
    else:
        others += 1 #other is including of white spaces.
print("Total alphabets: ", alphabets)
print("Total uppercase is: ",uppercase)
print("Total lowercase is: ",lowercase)
print("Total number is ",numeric)
print("Total other character is ", others)

'''