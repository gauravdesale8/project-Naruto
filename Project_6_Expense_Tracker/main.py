from expense import Expense
from data_handler import load_expenses, save_expenses

def show_total_expenses(expenses):
    total = 0

    for e in expenses:
        total += e.amount

    print("\nTotal Spending:", total)


def show_category_totals(expenses):
    category_totals = {}

    for e in expenses:
        if e.category not in category_totals:
            category_totals[e.category] = 0

        category_totals[e.category] += e.amount

    print("\n---- Category Total ----")

    for category, total in category_totals.items():
        print(category, ":",total)


def filter_by_category(expenses):
    user_category = input("Enter category: ").strip()

    print("\n---- Filter Expenses ----")

    found = False

    for e in expenses:
        if e.category.lower() == user_category.lower():
            print(e.date, '|',e.amount, '|',e.category, '|', e.description)
            found = True

    if not found:
        print("No expenses found for this category.")


def main():
    expenses = load_expenses()

    while True:
        print("\n---Expenses Tracker---")
        print("1.Add Expenses")
        print("2.View Expenses")
        print("3. Total Spending")
        print("4. Category Totals")
        print("5. Filter by Category")
        print("6. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            amount = input("Amount: ").strip()
            category = input("Category: ").strip()
            description = input("Description: ").strip()

            expense = Expense(date,amount,category, description)
            expenses.append(expense)

        elif choice == "2":
            print("\n--- All expenses ---")
            for e in expenses:
                print(e.date,"|",e.amount,"|",e.category,"|",e.description)

        elif choice == "3":
            show_total_expenses(expenses)

        elif choice == "4":
            show_category_totals(expenses)

        elif choice == "5":
            filter_by_category(expenses)

        elif choice == "6":
            save_expenses(expenses)
            print("Expenses saved. GoodBye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()