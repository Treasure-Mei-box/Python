#TODO-LIST , add, view, delete, exit

list = []

while True:
    print("=======TO-DO LIST=======")
    print("1.Add a task.")
    print("2.View tasks.")
    print("3.Delete Task.")
    print("4.Exit")
    choice = input("Enter a choice: ")
    if choice == "1":
        add = input("Enter task: ")
        list.append(add)
        print("Task added successfully.")
    elif choice == "2":
        for task in range(len(list)):
            print(str(task+1),".",list[task])
    elif choice == "3":
        if list == 0:
            print("No task to delete.")
        else:
            print("Select task number to delete - ")
            for task in range(len(list)):
                print(str(task+1),".",list[task])
            i = int(input("Enter your option: ")) - 1
            if (i >= 0 and i < len(list)):
                delete =list.pop(i)
                print(f"Deleted '{delete}' successfully.")
            else:
                print("Invalid choice.")
    elif choice == "4":
        print("All Done. Have a good day.")
        break
    else:
        print("Invalid Input. Try Again!")