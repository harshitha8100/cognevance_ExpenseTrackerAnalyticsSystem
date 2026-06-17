import sqlite3
import matplotlib.pyplot as plt

# Database Connection
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    date TEXT
)
""")
conn.commit()

# Add Expense
def add_expense():
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date (YYYY-MM-DD): ")

    cursor.execute(
        "INSERT INTO expenses(category, amount, date) VALUES (?, ?, ?)",
        (category, amount, date)
    )
    conn.commit()
    print("Expense Added Successfully!")

# View Expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    print("\nExpenses:")
    for row in data:
        print(row)

# Update Expense
def update_expense():
    expense_id = int(input("Enter Expense ID to Update: "))
    new_amount = float(input("Enter New Amount: "))

    cursor.execute(
        "UPDATE expenses SET amount=? WHERE id=?",
        (new_amount, expense_id)
    )
    conn.commit()
    print("Expense Updated!")

# Delete Expense
def delete_expense():
    expense_id = int(input("Enter Expense ID to Delete: "))

    cursor.execute(
        "DELETE FROM expenses WHERE id=?",
        (expense_id,)
    )
    conn.commit()
    print("Expense Deleted!")

# Generate Report
def report():
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    data = cursor.fetchall()

    print("\nExpense Report")
    for row in data:
        print(row[0], ":", row[1])

# Chart
def chart():
    cursor.execute("""
    SELECT category, SUM(amount)
    FROM expenses
    GROUP BY category
    """)

    data = cursor.fetchall()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.pie(amounts, labels=categories, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()

# Main Menu
while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Generate Report")
    print("6. Show Chart")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        report()

    elif choice == "6":
        chart()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")