a = {1,2,3,4}
b = {3,4,5,6}
''' 
if 5 in a:
    print("2 is in set a")
else:
    print("5 is not in set a")
'''

fruits = {"apple","strawberry","cherry"}
print("apple" in fruits)
print("pomelo" in fruits)

#example 1

no_fly_list ={"Joe","Jame","Alex","Evonne"}
passenger = input("Enter passenger name: ")
if passenger in no_fly_list:
    print("Access denied. This person is on the barred list")
else:
    print("Access granted.")