import csv
import os

expenses = []
budget = 0

def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (Food, Travel, etc.): ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
        return
    description = input("Enter a brief description: ")
    
    expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        if all(key in expense for key in ['date', 'category', 'amount', 'description']):
            print(f"Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
        else:
            print("Incomplete expense entry found.")
            
def set_budget():
    global budget
    try:
        budget = float(input("Enter your monthly budget: "))
    except ValueError:
        print("Invalid budget. Please enter a valid number.")
        return
    print(f"Monthly budget set to ${budget:.2f}")

def track_budget():
    total_expense = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses so far: ${total_expense:.2f}")
    
    if total_expense > budget:
        print("Warning: You have exceeded your budget!")
    else:
        remaining_balance = budget - total_expense
        print(f"You have ${remaining_balance:.2f} left for the month.")
        
def save_expenses():
    with open("expenses.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved successfully!")

def load_expenses():
    global expenses
    if not os.path.exists("expenses.csv"):
        return

    with open("expenses.csv", "r") as f:
        reader = csv.DictReader(f)
        expenses = list(reader)
        for expense in expenses:
            expense['amount'] = float(expense['amount'])  # Convert amount back to float
    
    print("Expenses loaded successfully!")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_expenses()
        elif choice == 3:
            set_budget()
            track_budget()
        elif choice == 4:
            save_expenses()
        elif choice == 5:
            save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    load_expenses()
    menu()
