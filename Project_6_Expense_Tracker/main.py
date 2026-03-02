from expense import Expense

def main():
    expenses = []

    while True:
        print("\n---Expenses Tracker---")
        print("1.Add Expenses")
        print("2.View Expenses")
        print("3.Exit")

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
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()