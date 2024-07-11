# test_starter.py

import pytest
import os
from starter import ExpenseTracker, Expense

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_add_expense(tracker):
    tracker.add_expense(100, 'Food', 'Lunch')
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 100
    assert tracker.expenses[0].category == 'Food'
    assert tracker.expenses[0].description == 'Lunch'

def test_edit_expense(tracker):
    tracker.add_expense(100, 'Food', 'Lunch')
    tracker.edit_expense(0, 150, 'Food', 'Dinner')
    assert len(tracker.expenses) == 1
    assert tracker.expenses[0].amount == 150
    assert tracker.expenses[0].description == 'Dinner'

def test_delete_expense(tracker):
    tracker.add_expense(100, 'Food', 'Lunch')
    tracker.delete_expense(0)
    assert len(tracker.expenses) == 0

def test_list_expenses(tracker):
    tracker.add_expense(100, 'Food', 'Lunch')
    tracker.add_expense(50, 'Transport', 'Bus fare')
    expenses = tracker.list_expenses()
    assert len(expenses) == 2
    assert expenses[0].amount == 100
    assert expenses[1].category == 'Transport'

def test_save_and_load_from_file(tracker):
    filename = 'test_expenses.json'
    tracker.add_expense(100, 'Food', 'Lunch')
    tracker.add_expense(50, 'Transport', 'Bus fare')

    tracker.save_to_file(filename)
    assert os.path.exists(filename)

    tracker2 = ExpenseTracker()
    tracker2.load_from_file(filename)
    assert len(tracker2.expenses) == 2
    assert tracker2.expenses[0].description == 'Lunch'
    assert tracker2.expenses[1].amount == 50

    # Clean up test file
    os.remove(filename)
