import time
import pytest
from starter import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_add_expense_performance(tracker):
    start_time = time.time()
    for i in range(1000):  # Add 1000 expenses
        tracker.add_expense(i, "Category", f"Expense {i}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken to add 1000 expenses: {execution_time:.4f} seconds")
    # Assert that adding expenses should take less than 1 second
    assert execution_time < 1.0

def test_edit_expense_performance(tracker):
    # Add initial expenses for testing
    for i in range(100):
        tracker.add_expense(i, "Category", f"Expense {i}")
    
    start_time = time.time()
    tracker.edit_expense(50, 999, "Updated Category", "Updated Expense")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken to edit an expense: {execution_time:.4f} seconds")
    # Assert that editing an expense should take less than 0.01 seconds
    assert execution_time < 0.01

def test_delete_expense_performance(tracker):
    # Add initial expenses for testing
    for i in range(100):
        tracker.add_expense(i, "Category", f"Expense {i}")
    
    start_time = time.time()
    tracker.delete_expense(50)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Time taken to delete an expense: {execution_time:.4f} seconds")
    # Assert that deleting an expense should take less than 0.01 seconds
    assert execution_time < 0.01
