# Expense Tracker Application

## Overview

This Expense Tracker application allows users to manage their expenses efficiently. It includes functionalities to add, edit, delete expenses, list all expenses, and save/load expenses from a JSON file.

## Features Implemented

- **ExpenseTracker Class:** Manages the core functionalities of the expense tracking system.
- **Expense Class:** Represents individual expenses with attributes such as amount, category, description, and date.
- **Methods Implemented:**
  - `add_expense(amount, category, description)`: Adds a new expense to the tracker.
  - `edit_expense(index, amount, category, description)`: Edits an existing expense at the specified index.
  - `delete_expense(index)`: Deletes an expense at the specified index.
  - `list_expenses()`: Lists all expenses with details.
  - `save_to_file(filename)`: Saves all expenses to a JSON file.
  - `load_from_file(filename)`: Loads expenses from a JSON file.

## Additional Features

- **Sorting Expenses:** Implemented methods to sort expenses by amount, category, and date.
- **Performance Testing:** Implemented performance tests to ensure the application handles a large number of expenses efficiently.

## Testing Strategy

- **Unit Tests:** Comprehensive unit tests using `pytest` to validate each method's functionality.
- **Integration Tests:** Tests to ensure interactions between different methods work correctly, especially focusing on saving to and loading from a file.
- **Performance Tests:** Tests to verify the application's performance under load, ensuring it remains responsive with a large dataset.

## Challenges Faced

- Ensuring proper error handling and edge case coverage in tests.
- Implementing sorting methods efficiently without impacting performance.

## Assumptions

- JSON file format assumed to be consistent and valid during load operations.
- No specific user authentication or access control implemented.

## How to Run

1. **Clone Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install Dependencies:**
   Ensure Python 3.12.2 is installed and dependencies are installed using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Tests:**
   Execute `pytest` to run all tests:
   ```bash
   pytest
   ```

4. **Execute Application:**
   Modify `main.py` or use the existing `starter.py` to interact with the Expense Tracker application.

## Future Enhancements

- Implement filtering and reporting functionalities.
- Enhance user interface for better user experience.
