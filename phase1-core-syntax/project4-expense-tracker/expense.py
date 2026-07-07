# Let us first begin by creating the expenses file.
# Since, we are going to be working with datetime, let us begin by importing it.
import datetime as dt

class Expense:
    def __init__(self, expense_id, name, price, date, category):
        self.expense_id = expense_id
        self.name = name
        if price < 0:
            raise ValueError(f"Price cannot be negative. Received: {price}")
        self.price = price
        self.date = dt.datetime.strptime(date, "%Y-%m-%d").date()
        self.category = category


# We will also be using the 'str' dunder method to get a clean, human-readable string as well.
    def __str__(self):
        return f"ID: {self.expense_id}\nExpense Name: {self.name}\nPrice: ₹{self.price}\nPurchased on: {self.date}\nExpense Category: {self.category}."
