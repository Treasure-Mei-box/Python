""" 

person = {"Name":"John", "Age":30, "City":"London"}
print(person.keys())
print(person.values())

print(person.items())

#print(person.clear()) # RETURN NONE

#COPY dictionary
original = {"a":1,"b":2,"c":3}
copy = original.copy()
print(copy)

copy ["a"] = 10
print(copy)

#Iteration
for key in person:
    print(key)
    
for value in person.values():
    print(value)
for key,value in person.items():
    print(key,value)
    
"""

#Nested Dictionary

company = {"Name":"Introspect Myanmar","employee":
           {"employee1" : {"name":"Treasure","role":"Co-Founder"},
            "employee2" : {"name":"Kaung","role":"Co-Founder"},
            "employee3" : {"name":"May","role":"CEO"}}
            }

#print(company)

#Access nested dictionary
'''
print(company["employee"]) 
print(company["employee"]["employee1"])
print(company["employee"]["employee1"]["role"])

'''

student = {"101":{"name":"Joe","age":20,"major":"CS"},
           "102":{"name":"Evonne","age":21,"major":"Data"},
           "202":{"name":"Elvin","age":20,"major":"Cloud"}}

print(student)
print(student["101"])
print(student["101"]["major"])