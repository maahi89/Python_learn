import os
from datetime import datetime
from utils import validate_date

# File path for storing expenses
EXPENSE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "expenses", "expenses.txt")

def add_expense():
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    elif not validate_date(date_str):
        print("Invalid date format! Use YYYY-MM-DD")
        return

    category = input("Enter category (Food, Transport, etc.): ").strip()
    amount = input("Enter amount: ").strip()
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount!")
        return

    os.makedirs(os.path.join(os.path.dirname(EXPENSE_FILE)), exist_ok=True)
    with open(EXPENSE_FILE, "a") as f:
        f.write(f"{date_str},{category},{amount}\n")

    print("Expense added ✅")

def view_expenses():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.")
        return

    print("\nDate\t\tCategory\tAmount")
    print("-"*40)
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            date, category, amount = line.strip().split(",")
            print(f"{date}\t{category}\t{amount}")

def monthly_summary():
    if not os.path.exists(EXPENSE_FILE):
        print("No expenses recorded yet.")
        return

    summary = {}
    with open(EXPENSE_FILE, "r") as f:
        for line in f:
            date, category, amount = line.strip().split(",")
            month = date[:7]  # YYYY-MM
            amount = float(amount)
            summary[month] = summary.get(month, 0) + amount

    print("\nMonth\t\tTotal Spent")
    print("-"*30)
    for month, total in summary.items():
        print(f"{month}\t{total}")
