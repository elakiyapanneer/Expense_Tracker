import csv
from datetime import datetime

FILE_NAME = "data.csv"

# Initialize CSV file with headers
def init_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "category", "type", "amount", "description"])
    except FileExistsError:
        pass

# Add a new transaction
def add_transaction():
    print("\nAdd a new transaction")

    t_type = input("Type (income/expense): ").strip().lower()
    if t_type not in ["income", "expense"]:
        print("Invalid type! Must be 'income' or 'expense'.")
        return

    category = input("Category: ").strip()
    description = input("Description: ").strip()

    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, t_type, f"{amount:.2f}", description])

    print("Transaction added ")

# View all transactions
def view_transactions():
    print("\nAll Transactions")
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header
            rows = list(reader)
            if not rows:
                print("No transactions yet!")
                return
            print("Date|Category|Type|Amount|Description")
            print("-"*50)
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
    except FileNotFoundError:
        print("No transactions yet!")

# Show summary
def view_summary():
    income = 0
    expense = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                amt = float(row["amount"])
                if row["type"].lower() == "income":
                    income += amt
                else:
                    expense += amt
    except FileNotFoundError:
        print("No transactions yet!")
        return

    print("\nSummary")
    print(f"Total Income : {income:.2f}")
    print(f"Total Expense: {expense:.2f}")
    print(f"Balance      : {income - expense:.2f}")

# Search by category
def search_category():
    keyword = input("\nEnter category to search: ").strip().lower()
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            print("Date|Category|Type|Amount|Description")
            print("-"*50)
            for row in reader:
                if row["category"].lower() == keyword:
                    print(f"{row['date']} | {row['category']} | {row['type']} | {row['amount']} | {row['description']}")
                    found = True
    except FileNotFoundError:
        print("No transactions yet!")
        return
    if not found:
        print("No transactions found for this category.")

# Main menu
def main():
    init_file()
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add transaction")
        print("2. View all transactions")
        print("3. View summary")
        print("4. Search by category")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            search_category()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()