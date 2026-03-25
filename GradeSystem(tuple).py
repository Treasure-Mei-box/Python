#Allow  add(name/ sub/ grade) / view/ find grade/ display highest grade/ exit

students = []

while True:
    print("------ Student Grade System ------")
    print("1. Add data.")
    print("2. View data.")
    print("3. Find the grade.")
    print("4. Display the highest grade achieved.")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        sub = input("Enter subject: ")
        grade = input("Enter grade achieved: ")
        student = (name,sub,grade)
        students.append(student)
        print("Data added successfully.")
        print()
    elif choice == "2":
        if not students:
            print("No data to show.")
        else:
            for s,student in enumerate(students,1):
                print(f"{s}. Name: {student[0]} | Subject: {student[1]} | Grade: {student[2]}")
    elif choice == "3":
        name_input = input("Enter student name: ")
        found = False
        print(f"Student: {name_input}'s Grades are as follow.")
        
        for record in students:
            if record[0].lower() == name_input.lower():
                print(f"Subject: {record[1]} | Grade Achieved: {record[2]}")
                found = True
                
        if not found: 
            print("No record found for Student: ",name_input,".")
            
    elif choice == "4":
        if not students:
            print("No record found.")
        else:
            highest = students[0]
            for record in students:
                if record[2] > highest[2]:
                    highest = record 
            print(f"Highest scored achieved \n Student: {record[0]} | Subject: {record[1]} | Grade: {record[2]}")  
            print()      
    elif choice == "5":
        print("Thank you for using the system.")
        break
    else:
        print("Invalid input. Try Again.")