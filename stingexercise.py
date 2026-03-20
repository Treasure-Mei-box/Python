#SLICING the sentence equally
'''
sentence = input("Write a sentence: ")
length = len(sentence)

mid = (length + 1)//2
first_half = sentence[:mid]
second_half = sentence[mid:]

print(f"First half is {first_half}. \nSecond half id {second_half}.")
'''

#REVERSE string slicing 
''' 
text = input("Write a sentence: ")
reverse = text[::-1]
print(F"Reverse string of {text} is {reverse}")

'''

#REVERSE string without slicing 
''' 
string = input("Enter a string: ")
reverse = " "
for char in string:
    reverse = char + reverse
print(reverse)
'''

#REPLACE method

''' 
orgstr = input("Write a sentence: ") # orgstr = "You are my sunshine. You are my everything."
repstr = orgstr.replace(input("Write smth to replace: "),"are") # repstr = orgstr.replace("are","were",1)
print(repstr)

''' 

''' 
original = input("Enter a string: ")
old = "are"
new = "were"
parts = original.split(old)
result = new.join(parts)
print("Oiginal string: ", original)
print("Update string: ", result)

'''

#ASSIGNMENT 

sentence = input("Enter string(use # to separate substring.): ") # #newhouse_#newcar_#newwife

if sentence.count("#") <= 1:
    print("No largest substring here.")
else:
    substrings = sentence.split("#") # newhouse , newcar , newwife
    largest = " "
    for s in substrings: # s means each newhouse / new car and newwife
        if len(s) > len(largest): #newhouse > 0 / newcar < newhouse / newwife < newhouse
            largest = s # newhouse 
    print(f"The largest string is '{largest}' with the length of '{len(largest)}'.")