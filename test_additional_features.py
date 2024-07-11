import pytest
from starter import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_add_expense(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    expenses = tracker.list_expenses()
    assert len(expenses) == 1
    assert expenses[0].amount == 100
    assert expenses[0].category == "Food"
    assert expenses[0].description == "Lunch"

def test_edit_expense(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.edit_expense(0, 150, "Food", "Dinner")
    expenses = tracker.list_expenses()
    assert expenses[0].amount == 150
    assert expenses[0].description == "Dinner"

def test_delete_expense(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.delete_expense(0)
    expenses = tracker.list_expenses()
    assert len(expenses) == 0

def test_sort_expenses_by_amount(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transportation", "Bus fare")
    tracker.sort_expenses_by_amount()
    expenses = tracker.list_expenses()
    print("Sorted Expenses by Amount:")
    for expense in expenses:
        print(f"{expense.amount} - {expense.category} - {expense.description}")
    assert expenses[0].amount == 50


def test_generate_expense_report(tracker):
    tracker.add_expense(100, "Food", "Lunch")
    tracker.add_expense(50, "Transportation", "Bus fare")
    report = tracker.generate_expense_report()
    assert "Total Expenses: 2" in report
    assert "Total Amount: $150" in report
    assert "Amount: $100 | Category: Food | Description: Lunch | Date:" in report
    assert "Amount: $50 | Category: Transportation | Description: Bus fare | Date:" in report

if __name__ == "__main__":
    pytest.main()
