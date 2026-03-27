from expense_manager import add_expense, view_expenses, get_total
from ai_insights import analyze_expenses

def menu():
    print("\n===== Student Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. AI Insights")
    print("5. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == '1':
        category = input("Enter category (Food/Travel/Study/etc): ")
        amount = float(input("Enter amount: "))
        add_expense(category, amount)
        print("✅ Expense added!")

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        total = get_total()
        print(f"💰 Total Spending: ₹{total}")

    elif choice == '4':
        analyze_expenses()

    elif choice == '5':
        print("Exiting... Goodbye!")
        break

    else:
        print("❌ Invalid choice! Try again.")