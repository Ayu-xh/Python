# Let us first begin by creating the expenses file.
# Since, we are going to be working with datetime, let us begin by importing it.
import datetime

class Expense:
    def __init__(self, id, name, price, date, type):
        self.id = id
        self.name = name
        self.price = price
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.type = type


        
