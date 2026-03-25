students = (
    ("Jo",20,("English","Math","Science"),(90,77,80)),
    ("Sui",19,("English","Math","Science"),(78,80,92)),
    ("Charles",19,("English","Math","Science"),(90,85,95)))

while True:
    print("\n======= Student Menu =======")
    print("1.View all students")
    print("2.Total and Average of given students")
    print("3.Find Top student in a given subject")
    print("4.Add New student")
    print("5.Exit")

    choice = input("Enter your choice(1-5): ")
    if choice == "1":
        for student in students:
            print(f"Name: {student[0]} | Age: {student[1]} | Subjects: {student[2]} | Marks: {student[3]}")
    elif choice == "2":
        name = input("Enter student's name: ")
        for student in students:
            if student[0].lower() == name.lower():  
                total = sum(student[3])
                average = total/len(student[3])
                print(f"{name.title()}'s Total Marks: {total}")
                print(f"{name.title()}'s Average Marks: {average}")
                
    elif choice == "3":
        subject = input("Enter subject name: ")
        top_student = ""
        highest = -1
        for student in students:
            if subject in student[2]:
                index = student[2].index(subject) 
                if student[3][index] > highest:
                    highest = student[3][index]
                    top_student = student[0]
        if top_student:
            print(f"Top Scorer in {subject} : {top_student} with {highest} Marks.")
                
    elif choice == "4":
        new_student = ("Treasure",27,("English","Math","Science"),(78,92,87))
        students = students + (new_student,) #adding as tuple style with comma(,) separated (--,)
        print("Successfully added new student.")
    elif choice == "5":
        print("Exit from the studebt record system.")
        break
    else:
        print("Invalid Input. Try Again.")