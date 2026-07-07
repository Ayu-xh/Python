# Let us first import the Expense class from the expense.py file.
from expense import Expense

# This expsense tracker class is required to store multiple expense objects.
class ExpenseTracker:
    def __init__(self):
        self.expenses = {} # This represents the empty dictionary where all the expenses will be added.
        self.next_expense_id = 1

    
    # Adding the add expense method.
    def add_expense(self, name, price, date, category):
        expense = Expense(self.next_expense_id, name, price, date, category)
        self.expenses[self.next_expense_id] = expense
        self.next_expense_id += 1


