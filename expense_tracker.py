class Expense:
    def __init__(self,amount,category,description):
        self.amount = amount
        self.category = category
        self.description = description

    def display(self):
        print("=====Expense Details=====")
        print("Amount:",self.amount)
        print("Category: ",self.category)
        print("Description: ",self.description)

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def save_to_file(self):
        file = open("expense.txt","w")
        for items in self.expenses:
            data = f"{items.amount},{items.category},{items.description}\n"
            file.write(data)
        file.close()
        print("Expense saved successfuly")

    def load_from_file(self):
        self.expenses = []

        try:
            file = open ("expense.txt","r")

            for line in file:
                data = line.strip().split(",")

                amount = int(data[0]) 
                category = (data[1])
                description = (data[2])     

                expense = Expense(amount,category,description)
                self.expenses.append(expense)

            file.close()
            print("Data loaded successfuly")

        except FileNotFoundError:
            print("No expenses found")

    def add_expense(self,new_expense):
        self.expenses.append(new_expense)
        print("Expense added successfuly")

    def view_expense(self):
        if not self.expenses:
            print("No expenses found")
            return 
        for items in self.expenses:  
                items.display()

    def search_category(self,name):
        for expense in self.expenses:
            if expense.category.lower() == name.lower():
                expense.display()
                return
        print("Expense not found of this category")

    def remove_expense(self,expense_category):
        for expense in self.expenses:
            if expense.category.lower() == expense_category.lower():
                self.expenses.remove(expense)
                print("Expense of given category is removed successfuly")
                return

        else:
            print("Not found")

    def chek_expense(self,name):
        for items in self.expenses:
            if items.category.lower() == name.lower():
                return True
        return False
        
expenses = ExpenseTracker()
expenses.load_from_file()
while True:
    print("=====Expense Tracker=====")
    print("1.Add Expense")
    print("2.View Expense")
    print("3.Search Expense")
    print("4.Remove Expnese")
    print("5.Save Expense")
    print("6.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        new_expense = Expense(amount,category,description)
        expenses.add_expense(new_expense)
    
    elif choice == 2:
        expenses.view_expense()

    elif choice==3:
        category = input("Enter category to search: ")
        expenses.search_category(category)

    elif choice == 4:
        expense_category = input("Enter category: ")
        expenses.remove_expense(expense_category)

    elif choice == 5:
        expenses.save_to_file()

    elif choice == 6:
        expenses.save_to_file()
        print("GoodBye!")
        break
    else:
        print("------Invalid choice------")