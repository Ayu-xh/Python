# Let us first import the Expense class from the expense.py file.
from expense import Expense
import datetime as dt

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

    # Deleting the expense method.
    def delete_expense(self, expense_id):
        if expense_id not in self.expenses:
            raise ValueError('Expense ID not found.')
        self.expenses.pop(expense_id)
        
    # Modifying the expense method.
    def modify_expense(self, expense_id, name=None, price=None, date=None, category=None):
        
        if expense_id not in self.expenses:
            raise ValueError('Expense ID not found.')

        # Since, we will be using the expense object multiple times, it is better to store it in a local variable.
        expense = self.expenses[expense_id] 

        if name is not None:
            expense.name = name  

        if price is not None:
            expense.price = price

        if date is not None:
            expense.date = dt.datetime.strptime(date, "%Y-%m-%d").date()

        if category is not None:
            expense.category = category  

    # Viewing the expenses.
    def list_expenses(self):
        if not self.expenses:
            print('No expenses found')
            return
        for expense in self.expenses.values():
            print(expense)
        
    # Creating the summary dictionary.
    def summary_by_category(self):
        summary_dict = {}
        for expense in self.expenses.values():
            current_category_value = summary_dict.get(expense.category, 0)
            summary_dict[expense.category] = current_category_value + expense.price

        return summary_dict
            
        



