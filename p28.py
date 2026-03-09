import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "expenses.csv"

# Create file if not exists
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Description"])
    df.to_csv(FILE_NAME, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Shopping/Others): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    new_data = pd.DataFrame([[date, category, amount, description]],
                            columns=["Date", "Category", "Amount", "Description"])

    new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)
    print("Expense added successfully!\n")

def view_report():
    df = pd.read_csv(FILE_NAME)

    if df.empty:
        print("No expenses recorded yet.")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    month = input("Enter month (1-12): ")
    year = input("Enter year (YYYY): ")

    monthly_data = df[(df["Date"].dt.month == int(month)) &
                      (df["Date"].dt.year == int(year))]

    if monthly_data.empty:
        print("No expenses for this month.")
        return

    total = monthly_data["Amount"].sum()
    print(f"\nTotal Expense: ₹{total}")

    category_summary = monthly_data.groupby("Category")["Amount"].sum()
    print("\nCategory-wise Expense:")
    print(category_summary)

    # Bar Chart
    category_summary.plot(kind='bar')
    plt.title("Monthly Expense by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Monthly Report")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

main()