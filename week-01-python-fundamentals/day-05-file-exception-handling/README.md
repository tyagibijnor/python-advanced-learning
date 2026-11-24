# Day 5 – File Handling and Exception Handling

## Overview

This folder contains the Week 1, Day 5 Python exercises. The main project is an
`EmployeeManager` that validates employee records and stores them as JSON.

## Project structure

```text
day-05-file-exception-handling/
├── employee_manager.py          # Employee validation and JSON persistence
├── test_employee_manager.py     # Unit tests for validation and file operations
├── demo.py                      # Runnable EmployeeManager demonstration
├── exercises.py                 # Standalone JSON and exception-handling exercises
├── employees.json               # Sample employee data
├── employees.txt                # Sample text file for reading exercises
├── README.md                    # Project overview and run instructions
├── NOTES.md                     # Notebook-ready learning notes
└── examples/
    ├── division_calculator.py   # try/except/else/finally example
    ├── file_reading.py          # Generator-based line reading
    ├── file_writing.py          # Appending text to a file
    └── salary_analysis.py       # Calculate basic salary statistics from sample JSON
```

## Employee record format

Each employee must be a dictionary containing:

```python
{"id": 101, "name": "Rahul", "salary": 50000}
```

Validation rules:

- The collection passed to `save_employees()` must be a list.
- Every employee record must be a dictionary.
- `id` must be a positive integer; Boolean values are rejected.
- `name` must be a non-empty string after whitespace is stripped.
- `salary` must be a positive, finite integer or float. Boolean values, NaN,
  positive/negative infinity, and integers outside the supported float range are rejected.

## Features

- Custom `InvalidEmployeeError` for invalid employee data.
- JSON serialization and deserialization.
- A missing JSON file returns an empty list.
- Invalid JSON and invalid UTF-8 are reported as invalid employee-file errors.
- Atomic save strategy: write a temporary file in the destination directory,
  flush it, and replace the destination using `os.replace()`.
- Temporary files are cleaned up when a save fails.

**Atomicity note:** `os.replace()` provides atomic replacement on supported filesystems
when source and destination are on the same filesystem. The implementation calls
`fsync()` on the temporary file, but does not claim full crash durability of directory
metadata on every operating system/filesystem.

## Run the tests

Run these commands from this directory with your project virtual environment activated:

```bash
python -m py_compile employee_manager.py test_employee_manager.py
python -m unittest -v test_employee_manager.py
```

Format the project:

```bash
black .
```

Run the demonstration:

```bash
python demo.py
```

The demo writes to `employees-demo.json`, so it does not overwrite the checked-in
`employees.json` sample.

## Learning objectives

- Validate untrusted input before using it.
- Raise and test custom exceptions.
- Use context managers for file operations.
- Read and write JSON data.
- Understand temporary files and atomic replacement.
- Test failure paths, not only successful execution.
