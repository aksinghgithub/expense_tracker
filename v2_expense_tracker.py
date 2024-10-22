## CEP01 Expense Tracker project - Python Basics - ##

import json

# ================================#
# File Handling Functions         #
# ================================#
def save_expenses(filename, expenses):
    """Save expenses to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(expenses, f)

def load_expenses(filename):
    """Load expenses from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

# ================================#
# Expense Management Functions    #
# ================================#
def log_expense(expenses):
    """Log a new expense."""
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter expense description: ")

    # Create a new expense with an id #
    expense_id = len(expenses) + 1  # Simple indexing based on the current length #
    expenses.append({
        "id": expense_id,  # Assign a unique id to each expense #
        "amount": amount,
        "category": category,
        "date": date,
        "description": description
    })
    print("Expense logged successfully!")

def view_expenses(expenses):
    """View all logged expenses."""
    if not expenses:
        print("No expenses logged yet.")
        return
    
    print("\nLogged Expenses:")
    for expense in expenses:
        print(f"[ID: {expense['id']}] {expense['date']}: {expense['amount']} in {expense['category']} - {expense['description']}")
    print("\n")

# ================================#
# Budget Management Functions     #
# ================================#
def set_budget():
    """Set a monthly budget."""
    budget = float(input("Enter your monthly budget: "))
    return budget

def track_budget(expenses, budget):
    """Track expenses against the budget."""
    total_spent = sum(expense['amount'] for expense in expenses)
    print(f"Total spent: {total_spent}, Monthly budget: {budget}")
    
    if total_spent > budget:
        print("Warning: You have exceeded your budget!")
    else:
        print("You are within your budget.")

# ================================#
# Main Functionality              #
# ================================#
def main():
    expenses = load_expenses("expenses.json")
    monthly_budget = 0

    while True:
        print("\nPersonal Expense Tracker")
        print("1. Log Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. Track Budget")
        print("5. Save Expenses")
        print("6. Load Expenses")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            log_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            monthly_budget = set_budget()
        elif choice == '4':
            track_budget(expenses, monthly_budget)
        elif choice == '5':
            save_expenses("expenses.json", expenses)
            print("Expenses saved successfully!")
        elif choice == '6':
            expenses = load_expenses("expenses.json")
            print("Expenses loaded successfully!")
        elif choice == '7':
            print("Exiting the tracker. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

# ================================#
# Entry Point                     #
# ================================#
if __name__ == "__main__":
    main()
