categories = {"Food","Utilities","Entertainment","Transportation","Donation","Beauty"}

expenses = {category:0 for category in categories}

while True:
    print("\n -------- Personal Finance Tracker --------")
    print("1.Add expense.")
    print("2.Show expense")
    print("3.Exit")
    choice = input("Enter your option(1-3): ").strip()
    
    if choice == "1":
        category_input = input("Enter the category: ").strip().capitalize()
        print("Available categories: ",",".join(categories).capitalize())
        
        if  category_input not in categories:
            print("Invalid Category.")
            continue
        amount = float(input(f"Enter amount spent on {category_input}: "))
        expenses[category_input] += amount
        print(f"{amount}RM added to {category_input}")

    elif choice == "2":
        print("Show Expense")
        total = sum(expenses.values())
        print("Total expense: ", total)
        print("Breakdown by category: ")
        for category, amount in expenses.items():
            print(f"-{category}: {amount}")
    elif choice == "3":
        print("Stay smart with Personal Finance Tracker.")
        break
    else:
        print("Invalid option. Onmly 1 - 3 allowed.")