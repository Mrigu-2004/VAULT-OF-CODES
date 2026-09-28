import json # Import json module to handle saving and loading expense data
import os # Import os module to check for file existence
from datetime import datetime # Import datetime for handling and formatting dates

# File to store expenses
FILE_NAME = "expenses.json" # Define the filename for storing expenses

# Load data from file (if exists)
def load_expenses():
    if os.path.exists(FILE_NAME): # Check if the file exists
        with open(FILE_NAME, "r") as file: # Open the file in read mode
            return json.load(file) # Load and return JSON data as a list of expenses
    return [] # Return an empty list if the file does not exist

# Save data to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file: # Open the file in write mode
        json.dump(expenses, file, indent=4) # Save the expenses list as JSON with indentation for readability

# Display all expenses
def display_expenses(expenses):
    if not expenses: # Check if there are no expenses
        print("No expenses recorded yet.") # Print message if no expenses are found
    else:
        print("\nCurrent Expenses:") # Print header for expenses
        for expense in expenses: # Loop through each expense in the list
            print(f"Amount: Rs.{expense['amount']}, Category: {expense['category']}, Date: {expense['date']}") # Print expense details
        print("\n") # Add a newline for spacing

# Add an expense
def add_expense(expenses):
    amount = float(input("Enter the amount: ")) # Prompt user to input the expense amount and convert to float
    category = input("Enter the category (e.g., Food, Transport): ") # Prompt user to input the expense category
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ") # Prompt user to input the expense date
    if not date: # If no date is entered, use today's date
        date = datetime.today().strftime('%Y-%m-%d') # Format today's date as 'YYYY-MM-DD'
    
    # Create expense dictionary
    expense = {
        "amount": amount, # Set the amount
        "category": category, # Set the category
        "date": date # Set the date
    }
    
    expenses.append(expense) # Add the new expense to the list
    save_expenses(expenses) # Save the updated list to the file
    print(f"Expense of {amount} in {category} added!") # Confirm addition to the user

def view_summary(expenses):
    # Print options for summary
    print("\n1. Total spending by category") # Option 1 for category-based spending
    print("2. Total overall spending") # Option 2 for total spending
    print("3. Spending over time") # Option 3 for time-based spending
    choice = input("Choose an option: ") # Prompt the user to choose an option
    
    # Option 1: Calculate total spending by category
    if choice == "1":
        category = input("Enter the category: ") # Ask for the specific category
        # Sum up expenses that match the given category (case-insensitive)
        total = sum(expense['amount'] for expense in expenses if expense['category'].lower() == category.lower())
        print(f"Total spending on {category}: Rs.{total}") # Output the total
    
    # Option 2: Calculate the total spending across all expenses
    elif choice == "2":
        total = sum(expense['amount'] for expense in expenses) # Sum up all expenses
        print(f"Total overall spending: Rs.{total}") # Output the total
    
    # Option 3: Provide time-based spending summary (daily, weekly, or monthly)
    elif choice == "3":
        print("\nChoose time period:")
        print("1. Daily")   # Option for daily summary
        print("2. Weekly")  # Option for weekly summary
        print("3. Monthly") # Option for monthly summary
        time_choice = input("Enter your choice: ") # Prompt the user for time period
        
        # Daily summary of expenses
        if time_choice == "1":
            daily_summary = {} # Initialize dictionary for storing daily totals
            for expense in expenses:
                date = expense['date'] # Use the full date as the key
                if date in daily_summary:
                    daily_summary[date] += expense['amount'] # Add amount if date exists
                else:
                    daily_summary[date] = expense['amount'] # Create new entry if date is new
            
            print("\nDaily Spending Summary:")
            for date, total in daily_summary.items(): # Output daily spending totals
                print(f"{date}: Rs.{total}")
        
        # Weekly summary of expenses
        elif time_choice == "2":
            weekly_summary = {} # Initialize dictionary for weekly totals
            for expense in expenses:
                date = datetime.strptime(expense['date'], '%Y-%m-%d') # Parse the date
                week = date.strftime('%Y-W%U') # Format as year-week string
                if week in weekly_summary:
                    weekly_summary[week] += expense['amount'] # Add amount if week exists
                else:
                    weekly_summary[week] = expense['amount'] # Create new entry if week is new
            
            print("\nWeekly Spending Summary:")
            for week, total in weekly_summary.items(): # Output weekly spending totals
                print(f"{week}: Rs.{total}")
        
        # Monthly summary of expenses
        elif time_choice == "3":
            monthly_summary = {} # Initialize dictionary for monthly totals
            for expense in expenses:
                month = expense['date'][:7] # Extract "YYYY-MM" for month
                if month in monthly_summary:
                    monthly_summary[month] += expense['amount'] # Add amount if month exists
                else:
                    monthly_summary[month] = expense['amount'] # Create new entry if month is new
            
            print("\nMonthly Spending Summary:")
            for month, total in monthly_summary.items(): # Output monthly spending totals
                print(f"{month}: Rs.{total}")
        
        else:
            print("Invalid choice. Please choose again.") # Handle invalid time period choice


# Menu for the user
def main_menu():
    expenses = load_expenses() # Load expenses from file
    
    # Display expenses at the start
    display_expenses(expenses) # Show all existing expenses to the user
    
    while True: # Start an infinite loop for the main menu
        print("\nPersonal Expense Tracker") # Print application title
        print("1. Add Expense") # Print option 1 for adding an expense
        print("2. View Summary") # Print option 2 for viewing summary
        print("3. Exit") # Print option 3 for exiting the application
        
        choice = input("Enter your choice: ") # Prompt user for menu choice
        
        if choice == "1": # If user chooses to add an expense
            add_expense(expenses) # Call add_expense function
        elif choice == "2": # If user chooses to view summary
            view_summary(expenses) # Call view_summary function
        elif choice == "3": # If user chooses to exit
            print("Exiting program...") # Print exit message
            break # Exit the loop and end the program
        else:
            print("Invalid choice. Please choose again.") # Prompt for valid input if choice is invalid

if __name__ == "__main__":
    main_menu() # Run the main_menu function to start the application

