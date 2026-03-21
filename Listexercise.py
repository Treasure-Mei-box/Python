#Exercise 1
''' 
mylist = [10,20,30,40,50]
#total = sum(mylist)
#print(total)
total = 0
for i in mylist:
    total += i
    print(total)
    
'''

#Exercise 2

''' 

num = [1,2,3,4,5]
product = 1
for i in num:
    product *= i
    print(product)
    
'''
#Exercise 3

''' 

numlist = [10,25,3,99,56,72]
largest = numlist[0]
for i in numlist:
    if i > largest:
        largest = i
    print(largest)
    
'''

#Exercise 4

''' 

numlist = [10,25,3,99,56,72]
smallest = numlist[0]
for i in numlist:
    if i < smallest:
        smallest = i
print(smallest)

'''

#Exercise 5

'''
words = ["abc","xyz","aba" ,"aa","1221"]
count = 0
for word in words:
    if len(word) >= 2 and word[0]==word[-1]:
        count += 1
print("Total: ",count)
        
'''

#Exercise 6

''' 

list = [10,20,30]
single_int =int("".join(str(num) for num in list))
print("Single Integer: ", single_int)

'''

#Exercise 7

''' 

sentence = input("Enter string separated by spaces: ").split()
count = 0
for word in sentence:
    if len(word) >= 5:
        first_two = word[:2].lower()
        last_two_reversed = word[-1:-3:-1].lower()
        print(last_two_reversed)
        if first_two != last_two_reversed:
            count += 1
    print("Number of words that meet requirement is ", count)
    
'''

#Exercise 7

''' '''

input = input("Enter word: ")
char = [char for char in input]
same = []
result = []
for i in char:
    if i in same:
        result.append("*")
    else:
        same.append(i)
        result.append(i)
    print("Input: ", input)
    print("Output: ", result)
        
""" 
Input:  hello
Output:  ['h']
Input:  hello
Output:  ['h', 'e']
Input:  hello
Output:  ['h', 'e', 'l']
Input:  hello 
Output:  ['h', 'e', 'l', '*']
Input:  hello
Output:  ['h', 'e', 'l', '*', 'o']

"""      
     