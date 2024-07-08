import json
from datetime import datetime


class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        """Add a new expense"""
        pass
      
    def edit_expense(self, index, amount, category, description):
        """Edit an existing expense"""
        pass
      
    def delete_expense(self, index):
        """Delete an expense by index"""
        pass
      
    def list_expenses(self):
        """List all expenses"""
        pass
      
    def save_to_file(self, filename):
        """Save expenses to a JSON file"""
        pass
      
    def load_from_file(self, filename):
        """Load expenses from a JSON file"""
        pass


if __name__ == "__main__":
    tracker = ExpenseTracker()
    # You can add some code here to interact with the ExpenseTracker
