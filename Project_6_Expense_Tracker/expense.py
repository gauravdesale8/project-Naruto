class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = float(amount)
        self.category = category
        self.description = description