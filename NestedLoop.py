'''
i = 0
while i <= 9: #outer loop
    j = 1 #initial condition
    while j<= i: #inner loop
        print(f"{j}" , end=" ")
        j += 1
    print()
    i += 1
    
'''
    
#break and continue 

'''
i = 0
while i < 5:
    i += 1
    if i == 3:
        #break
        continue
    print(i)
'''
    
''' 
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j , end=" ")
        j+= 1
    print()
    i += 1
'''

countL = 0
#nLine = 10
print('This is a break and continue example.')
while countL < 10 :
    countL += 1
    if (countL % 3) == 0:
        break
    print("Statement # : " + str(countL) + '.' )
print("This is the last statement.")
