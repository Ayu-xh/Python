# This file is responsible for saving all the objects (like a receipt).

# First, we design the save to CSV function.
def save_to_csv(expenses, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        