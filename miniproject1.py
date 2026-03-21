#add , edit, remove functions

tasks = []
while True:
    print("========To Do List========")
    print("1.Add Tasks.")
    print("2.View Tasks.")
    print("3.Remove Tasks.")
    print("4.Exit.")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task Added.")
    elif choice == "2":
        if len(tasks) == 0:
            print("No task found.")
        else:
            print("Your tasks:")
            for i in range (len(tasks)):
                print(str(i+1)+"."+ tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("No task to remove.")
        else:
            print("Select task number to remove: ")
            for i in range(len(tasks)):
                print(str(i+1)+"."+tasks[i])
            index = int(input("Enter task number to remove: "))-1
            if (index >= 0 and index < len(tasks)):
                remove = tasks.pop(index)
                print("Remove task: ",remove)
            else:
                print("Invalid task  number.")
    elif choice == "4":
        print("Thank you for using TO DO LIST.")
        break
    else:
        print("Invalid input. Try again")