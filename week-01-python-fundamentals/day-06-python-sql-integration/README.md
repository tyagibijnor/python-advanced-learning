# Day 06 – Python + MySQL Integration

## Overview

This project demonstrates integration between Python and MySQL using `mysql-connector-python`.

It implements CRUD (Create, Read, Update, Delete) operations with parameterized SQL queries, transaction management, environment-based configuration, and automated integration testing.

## Learning Objectives

- Connect Python applications to MySQL.
- Manage database connections and cursors.
- Perform CRUD operations.
- Use parameterized SQL queries.
- Handle database transactions using commit and rollback.
- Manage configuration through environment variables.
- Write integration tests using Python unittest.
- Maintain secure database credentials.

## Project Structure

```text
day-06-python-sql-integration/
├── database.py
├── test_database.py
├── .env.example
├── README.md
└── requirements.txt
```

## Technology Stack

- Python
- MySQL
- mysql-connector-python
- python-dotenv
- unittest
- Black

## Database Configuration

Create a local `.env` file using `.env.example` as a reference.

Required environment variables:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=employee_db
```

Never commit `.env` or expose database credentials.

## Implemented Database Operations

| Function | Description |
|---|---|
| `get_db_connection()` | Establishes MySQL connection |
| `create_employee()` | Inserts a new employee |
| `get_employee_by_id()` | Retrieves employee by ID |
| `get_all_employees()` | Retrieves all employees |
| `update_employee()` | Updates department and salary |
| `delete_employee()` | Deletes employee by ID |

## Installation

Activate your virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Running Integration Tests

Execute:

```bash
python -m unittest -v test_database.py
```

The tests cover:

- Database connection
- Employee creation
- Employee retrieval
- Retrieving all employees
- Employee updates
- Successful employee deletion
- Deletion of a non-existing employee

### Latest Test Results

```text
Ran 7 tests

OK
```

All seven integration tests passed.

## Code Quality Checks

Format the code:

```bash
black database.py test_database.py
```

Compile-check:

```bash
python -m py_compile database.py test_database.py
```

## Security Practices

- Credentials are stored in environment variables.
- SQL statements use parameterized queries.
- Database connections and cursors are closed after operations.
- Transactions use commit and rollback.
- Test records are cleaned up automatically.
- Production credentials must never be committed to GitHub.

## Learning Outcomes

By completing this project, I practiced:

1. Python and MySQL integration.
2. Database connection management.
3. CRUD operations.
4. SQL parameterization.
5. Transaction handling.
6. Automated integration testing.
7. Test data cleanup and repeatability.
8. Environment-based configuration.

## Learning Method

Understand → Execute → Verify → Document → Commit

**Learning Path:** Python Advanced Learning – Week 01, Day 06

**Repository:** https://github.com/tyagibijnor/python-advanced-learning
