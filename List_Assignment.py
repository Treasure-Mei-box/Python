#Write Python code to create a list (and print all elements in the list as an output) by
#concatenating each individual string (a single character) input with the number of
#stars based on the input number. For the output, a character must be capitalized.
#TestRun-01
#Input: a b c
#Enter a value for n: 3
#Output:A* A** A*** B* B** B*** C* C** C***
#TestRun-02
#Input: a b c
#Enter a value for n: 4
#Output:A* A** A*** A**** B* B** B*** B**** C* C** C***

words = input("Enter words: ")
stars = int(input("Enter a value for stars: "))

#char = list(words)
result = []
for c in words:
    c = c.upper()
    for s in range(1,stars+1):
        result.append(c + "*"*s)
print(" ".join(result))


