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
        new_expense = Expense(amount, category, description)
        self.expenses.append(new_expense)
        print(f"Added expense: {amount} - {category} - {description}")
        pass
      
    def edit_expense(self, index, amount, category, description):
        """Edit an existing expense"""
        if 0 <= index < len(self.expenses):
            self.expenses[index].amount = amount
            self.expenses[index].category = category
            self.expenses[index].description = description
            print(f"Edited expense at index {index}: {amount} - {category} - {description}")
        else:
            print(f"Invalid index {index}. Cannot edit expense.")
        pass
      
    def delete_expense(self, index):
        """Delete an expense by index"""
        if 0 <= index < len(self.expenses):
            deleted_expense = self.expenses.pop(index)
            print(f"Deleted expense at index {index}: {deleted_expense.amount} - {deleted_expense.category} - {deleted_expense.description}")
        else:
            print(f"Invalid index {index}. Cannot delete expense.")    
        pass
      
    def list_expenses(self):
        """List all expenses"""
        return self.expenses
            
      
    def save_to_file(self, filename):
        """Save expenses to a JSON file"""
        with open(filename, 'w') as f:
            json.dump([vars(expense) for expense in self.expenses], f, indent=4)
        print(f"Expenses saved to {filename}.")
        pass
      
    def load_from_file(self, filename):
        """Load expenses from a JSON file"""
        try:
            with open(filename, 'r') as f:
                expenses_data = json.load(f)
                self.expenses = [Expense(**expense) for expense in expenses_data]
            print(f"Expenses loaded from {filename}.")
        except FileNotFoundError:
            print(f"File {filename} not found. No expenses loaded.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from {filename}. No expenses loaded.")
        pass
    def sort_expenses_by_amount(self):
        """Sort expenses by amount."""
        self.expenses.sort(key=lambda x: x.amount)

    def sort_expenses_by_category(self):
        """Sort expenses by category."""
        self.expenses.sort(key=lambda x: x.category)

    def sort_expenses_by_date(self):
        """Sort expenses by date."""
        self.expenses.sort(key=lambda x: x.date)

    def generate_expense_report(self):
        """Generate a simple expense report."""
        report = ""
        total_expenses = len(self.expenses)
        total_amount = sum(expense.amount for expense in self.expenses)

        report += f"Total Expenses: {total_expenses}\n"
        report += f"Total Amount: ${total_amount}\n\n"

        report += "Expense Details:\n"
        for idx, expense in enumerate(self.expenses, start=1):
            report += f"{idx}. Amount: ${expense.amount} | Category: {expense.category} | Description: {expense.description} | Date: {expense.date}\n"

        return report


if __name__ == "__main__":
    tracker = ExpenseTracker()
    # You can add some code here to interact with the ExpenseTracker
    tracker.add_expense(100, "Food", "Lunch at a restaurant")
    tracker.add_expense(50, "Transportation", "Metro fare")
    tracker.add_expense(200, "Shopping", "New headphones")

    tracker.list_expenses()

    tracker.edit_expense(1, 60, "Transportation", "Taxi fare")

    tracker.list_expenses()

    tracker.delete_expense(2)

    tracker.list_expenses()

    tracker.save_to_file("expenses.json")

    tracker.load_from_file("expenses.json")

    tracker.list_expenses()
