import tkinter as tk
from tkinter import messagebox
import csv
import os

# Define global variables
expenses = []
budget = 0

# Function to load data from file
def load_data():
    global expenses, budget
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r") as f:
            reader = csv.DictReader(f)
            expenses = list(reader)
            for expense in expenses:
                expense['amount'] = float(expense['amount'])  # Convert amount back to float
    update_listbox()
    update_total()

# Function to save data to file
def save_data():
    with open("expenses.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)
    messagebox.showinfo("Success", "Expenses saved successfully!")

# Function to add an expense
def add_expense():
    date = entry_date.get()
    category = category_var.get()
    try:
        amount = float(entry_amount.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        return
    description = entry_description.get()
    
    expense = {'date': date, 'category': category, 'amount': amount, 'description': description}
    expenses.append(expense)
    update_listbox()
    update_total()
    entry_date.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_description.delete(0, tk.END)
    messagebox.showinfo("Success", "Expense added successfully!")

# Function to update the listbox
def update_listbox():
      # Check if listbox exists
        #listbox_expenses.delete(0, tk.END)
        for expense in expenses:
            listbox_expenses.insert(tk.END, f"{expense['date']} - {expense['category']} - {expense['description']}: ${expense['amount']:.2f}")

# Function to update the total expense
def update_total():
    total = sum(expense['amount'] for expense in expenses)
    if root.winfo_exists():  # Check if root exists
        label_total.config(text=f"Total: ${total:.2f}")

# Function to set the budget
def set_budget():
    global budget
    try:
        budget = float(entry_budget.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")
        return
    messagebox.showinfo("Success", f"Monthly budget set to ${budget:.2f}")
    update_budget()

# Function to track budget
def update_budget():
    total_expense = sum(expense['amount'] for expense in expenses)
    if total_expense > budget:
        label_budget.config(text=f"Warning: You have exceeded your budget by ${total_expense - budget:.2f}!")
    else:
        remaining_balance = budget - total_expense
        label_budget.config(text=f"You have ${remaining_balance:.2f} left for the month.")

# Initialize main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Load data
load_data()

# Create UI elements
label_date = tk.Label(root, text="Date (YYYY-MM-DD):")
label_date.grid(row=0, column=0, padx=5, pady=5)

entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=5, pady=5)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=1, column=0, padx=5, pady=5)

category_var = tk.StringVar(value="Food")
category_menu = tk.OptionMenu(root, category_var, "Food", "Transport", "Entertainment", "Other")
category_menu.grid(row=1, column=1, padx=5, pady=5)

label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=2, column=0, padx=5, pady=5)

entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1, padx=5, pady=5)

label_description = tk.Label(root, text="Description:")
label_description.grid(row=3, column=0, padx=5, pady=5)

entry_description = tk.Entry(root)
entry_description.grid(row=3, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Expense", command=add_expense)
button_add.grid(row=4, column=0, columnspan=2, pady=5)

listbox_expenses = tk.Listbox(root, width=50)
listbox_expenses.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

label_total = tk.Label(root, text="Total: $0.00")
label_total.grid(row=6, column=0, columnspan=2, pady=5)

label_budget = tk.Label(root, text="Monthly Budget: $0.00")
label_budget.grid(row=7, column=0, columnspan=2, pady=5)

label_set_budget = tk.Label(root, text="Set Monthly Budget:")
label_set_budget.grid(row=8, column=0, padx=5, pady=5)

entry_budget = tk.Entry(root)
entry_budget.grid(row=8, column=1, padx=5, pady=5)

button_set_budget = tk.Button(root, text="Set Budget", command=set_budget)
button_set_budget.grid(row=9, column=0, columnspan=2, pady=5)

button_save = tk.Button(root, text="Save Expenses", command=save_data)
button_save.grid(row=10, column=0, columnspan=2, pady=5)

# Run the main event loop
root.mainloop()
