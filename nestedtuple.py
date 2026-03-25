tuple = (1,2,3,4)
nested_tuple = (1,(2,3,4),5,6,(7,8),9)
#print(nested_tuple)
#print(nested_tuple[0])
#print(nested_tuple[1])

nested = (1,(2,3),(4,5,6),7,8)
print(nested[1:3])

for i in nested:
    print(i)
    
for i in nested:
    if isinstance(i,tuple):
        for j in i:
            print(j)
        else:
            print(i)