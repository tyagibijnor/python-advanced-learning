# Day 5 Notes – File Handling and Exception Handling

## 1. File handling

**Definition:** File handling is the process of creating, reading, writing, appending,
and managing files using a programming language.

### Why do we need file handling?

- Store application data permanently.
- Read configuration files.
- Save application logs.
- Process CSV and JSON datasets.
- Store inputs and outputs for data and AI applications.

### Prefer context managers

Basic file handling requires closing the file manually:

```python
file = open("example.txt", "r", encoding="utf-8")
content = file.read()
file.close()
```

Prefer `with`, which closes the file automatically, including when an exception occurs:

```python
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

## 2. File modes

| Mode | Meaning |
|---|---|
| `r` | Read an existing file |
| `w` | Write; truncate existing content |
| `a` | Append to a file |
| `x` | Create a new file; fail if it exists |
| `r+` | Read and write |
| `rb` | Read binary data |
| `wb` | Write binary data |

**Important:** Opening a file in `w` mode truncates existing content immediately.

## 3. Common file methods

```python
file.read()          # Read all remaining content
file.readline()      # Read one line
file.readlines()     # Read remaining lines into a list
file.write("Hello")  # Write text
file.seek(0)          # Move the file cursor
file.tell()           # Get the current cursor position
```

## 4. JSON

JSON is a text format commonly used to exchange and persist structured data.

```python
import json

employee = {"id": 1, "name": "Rahul", "salary": 50000}

with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

with open("employee.json", "r", encoding="utf-8") as file:
    data = json.load(file)
```

- `json.dump()` writes a Python object to a file.
- `json.load()` reads JSON from a file and returns a Python object.
- `json.dumps()` converts a Python object to a JSON string.
- `json.loads()` parses a JSON string.

## 5. Exceptions

**Definition:** An exception is an event during program execution that interrupts the normal
flow unless it is handled.

| Keyword | Purpose |
|---|---|
| `try` | Wrap code that may raise an exception |
| `except` | Handle a matching exception |
| `else` | Run when the `try` block succeeds |
| `finally` | Run whether an exception occurs or not |
| `raise` | Raise an exception explicitly |

Example:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")
```

## 6. Custom exceptions

A custom exception communicates a domain-specific error:

```python
class InvalidEmployeeError(Exception):
    """Raised when employee information is invalid."""
```

Use it when input violates employee rules, rather than exposing unrelated low-level errors.

## 7. Employee validation lessons

- Validate the outer collection before iterating over it.
- Validate each record's type before accessing its keys.
- Check required fields before reading their values.
- Reject `bool` explicitly when an integer or float is expected because `bool`
  is a subclass of `int` in Python.
- Use `str.strip()` to detect names containing only whitespace.
- Use `math.isfinite()` to reject NaN and infinity.
- Consider numeric conversion edge cases such as extremely large integers.

## 8. Atomic file saving

A direct write with `"w"` truncates the destination before the new content is fully written.
If writing fails, the previous data may be lost.

A safer pattern is:

1. Validate all records.
2. Create a temporary file in the destination directory.
3. Serialize the new JSON into the temporary file.
4. Flush and sync the temporary file.
5. Replace the destination using `os.replace()`.
6. Remove the temporary file if the operation fails.

`os.replace()` provides atomic replacement when supported by the filesystem and when both
paths are on the same filesystem. Atomic replacement prevents readers from seeing a
partially written destination file. It is not a universal guarantee of survival after every
possible power loss or hardware failure.

## 9. Testing

Run:

```bash
python -m py_compile employee_manager.py test_employee_manager.py
python -m unittest -v test_employee_manager.py
black .
```

Negative tests should cover invalid types, missing fields, invalid numbers, malformed JSON,
encoding problems, and failed writes.

## 10. Interview revision

**Q: Why use `with` when opening files?**
A: It ensures the file is closed automatically when the block exits, including when an exception
occurs.

**Q: What is a custom exception?**
A: An application-defined exception used to represent a specific error in the program's domain.

**Q: What is atomic file replacement?**
A: Writing new content separately and replacing the destination only after the new file is ready,
so the destination is not exposed in a partially written state.

**Q: Why reject Boolean values in employee IDs and salaries?**
A: Because `bool` is a subclass of `int`, so `isinstance(True, int)` returns `True`.

**Q: What is negative testing?**
A: Testing invalid inputs and failure conditions to verify that the application handles them
correctly.

## 11. English practice

Write a short explanation using these terms:

- input validation
- custom exception
- temporary file
- atomic replacement
- data integrity

Suggested sentence starter:

"I validate employee records before saving them because ..."
