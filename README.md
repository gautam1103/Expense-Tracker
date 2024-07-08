# Online Technical Assessment: Expense Tracker

Welcome! Thank you for applying for the QA Engineer role at Cloud Code AI. As part of the technical assessment, we require you to complete the following task. Good luck!

## Instructions:
- You have up to 4 days to complete this assessment (Please submit by July 12, 2024 - 12 PM EST). Please manage your time effectively.
- Fork the provided repository and create a private repository.
- Add [shreyashkgupta](https://github.com/shreyashkgupta) and [sauravpanda](https://github.com/sauravpanda) as collaborators to your private repository.
- Upload all your code, test results, and supporting files to this private repository.
- Provide a brief document explaining your approach within the repository.
- Feel free to use any resources, but ensure that the work you submit is your own.

## Overview:
You will complete and test a simple Expense Tracker application. The provided starter code includes function definitions and basic structure. Your task is to implement the functionality, write a comprehensive suite of automated tests for it, and add any additional features or functionality that you believe would enhance the application.

## Task Details

### Part 1: Implement Functionality
Implement the following methods in the `ExpenseTracker` class:
- `add_expense(amount, category, description)`: Adds a new expense to the tracker.
- `edit_expense(index, amount, category, description)`: Edits an existing expense at the specified index.
- `delete_expense(index)`: Deletes an expense at the specified index.
- `list_expenses()`: Lists all expenses, displaying amount, category, description, and date.
- `save_to_file(filename)`: Saves all expenses to a JSON file.
- `load_from_file(filename)`: Loads expenses from a JSON file.

### Part 2: Automated Testing
Write a suite of automated tests for the Expense Tracker application using `pytest`.

#### Unit Tests:
- Test each method individually to ensure they work as expected.
- Include tests for edge cases.

#### Integration Tests:
- Test interactions between different methods.
- Ensure expenses can be saved to and loaded from a file correctly.

#### Additional Testing (Optional):
- Implement additional testing strategies.

### Part 3: Additional Features/Functionality (Optional)
Implement any additional features or functionality that you believe would enhance the Expense Tracker application. This is an opportunity to showcase your creativity and technical skills.

## Submission Requirements

### Code:
- Submit the complete code for the Expense Tracker application with the implemented methods and any additional features.
- Ensure the code is well-documented and follows best practices for readability and maintainability.

### Test Suite:
- Submit all test cases written using `pytest`.
- Include instructions on how to run the tests.

### Approach Document:
- Provide a brief document (1-2 pages) explaining your approach to the assignment.
- Discuss your testing strategy, any challenges you faced, and how you addressed them.
- Explain any assumptions you made while implementing the application and tests.
- Highlight any additional features you implemented and why you chose them.

## Evaluation Criteria

### Functionality:
- The Expense Tracker application should meet all the specified requirements and run correctly.

### Code Quality:
- Code should be clean, well-structured, and follow best practices.
- Proper use of comments and documentation.

### Testing Coverage:
- Comprehensive unit and integration tests covering various scenarios and edge cases.
- Use of `pytest` for test automation.

### Problem-Solving Skills:
- Effective and efficient implementation of the application and tests.
- Innovative solutions and clear explanation of the approach.

### Documentation:
- Clear and concise explanation of the approach and testing strategy.
- Ability to articulate challenges faced and solutions implemented.

### Additional Features:
- Implementation of additional features that enha
