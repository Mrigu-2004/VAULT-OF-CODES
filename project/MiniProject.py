import json
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.json"

# Load data from file (if exists)
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Display all expenses
def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nCurrent Expenses:")
        for expense in expenses:
            print(f"Amount: ${expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")
        print("\n")

# Add an expense
def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Transport): ")
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    # Create expense dictionary
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense of {amount} in {category} added!")

# View summary
def view_summary(expenses):
    print("\n1. Total spending by category")
    print("2. Total overall spending")
    print("3. Spending over time (monthly)")
    choice = input("Choose an option: ")
    
    if choice == "1":
        category = input("Enter the category: ")
        total = sum(expense['amount'] for expense in expenses if expense['category'].lower() == category.lower())
        print(f"Total spending on {category}: ${total}")
    
    elif choice == "2":
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total overall spending: ${total}")
    
    elif choice == "3":
        summary = {}
        for expense in expenses:
            month = expense['date'][:7]  # Extract "YYYY-MM" for monthly summary
            if month in summary:
                summary[month] += expense['amount']
            else:
                summary[month] = expense['amount']
        
        for month, total in summary.items():
            print(f"{month}: ${total}")

# Menu for the user
def main_menu():
    expenses = load_expenses()
    
    # Display expenses at the start
    display_expenses(expenses)
    
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main_menu()