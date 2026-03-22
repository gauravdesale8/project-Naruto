from expense import Expense

def load_expenses(filename = "expenses.txt"):
    expenses = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                date, amount, category , description = line.strip().split('|')
                expense = Expense(date, amount, category, description)
                expenses.append(expense)

    except FileNotFoundError:
        pass

    return expenses


def save_expenses(expenses, filename = "expenses.txt"):
    with open(filename, 'w') as file:
        for e in expenses:
            file.write(f"{e.date} | {e.amount} | {e.category} | {e.description}\n")
