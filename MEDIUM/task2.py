# Personal Expense Tracker

expenses = []  # List to store expenses as dictionaries


def add_expense():
    """Add a new expense with amount and category"""
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        expenses.append({"amount": amount, "category": category})
        print(f"Added expense: ${amount:.2f} in category '{category}'.\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")


def view_total():
    """View total of all expenses"""
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal expenses: ${total:.2f}\n")


def view_category_breakdown():
    """View total expenses grouped by category"""
    category_totals = {}
    for expense in expenses:
        cat = expense['category']
        category_totals[cat] = category_totals.get(cat, 0) + expense['amount']

    print("\nExpenses by category:")
    for cat, total in category_totals.items():
        print(f"  {cat}: ${total:.2f}")
    print()


def main():
    """Main menu loop"""
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Total Spent")
        print("3. View Expenses by Category")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_total()
        elif choice == "3":
            view_category_breakdown()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")
