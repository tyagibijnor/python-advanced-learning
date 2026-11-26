# Week 02 – Day 01: Closures and Decorators

## Overview

This module explores advanced Python concepts, including closures, decorators, function metadata preservation, application logging, exception handling, and input validation.

The practical exercises demonstrate how to build reusable functions and decorators using clean, maintainable Python code.

## Learning Objectives

- Understand closures and lexical scoping.
- Use the `nonlocal` keyword to maintain state.
- Implement reusable decorators.
- Understand `*args` and `**kwargs` in decorators.
- Preserve function metadata using `functools.wraps`.
- Implement structured logging using Python's `logging` module.
- Handle exceptions and preserve original error propagation.
- Validate numeric inputs and boundary conditions.
- Write automated unit tests using `unittest` and `assertLogs`.

## Project Structure

```text
day-01-closures-decorators/
├── closures.py
├── demo_closures.py
├── decorators.py
├── run_logging_demo.py
├── test_closures.py
├── test_decorators.py
├── demo_exception_logging.py
├── notes.md
└── README.md
```

Generated files such as `application.log` and `__pycache__/` are excluded from version control.

## Concepts Covered

### 1. Closures

Implemented:
- `make_multiplier(factor)`
- `make_counter()`

Key concepts:
- Nested functions
- Lexical scoping
- Enclosing function variables
- `nonlocal`
- Independent closure state

### 2. Decorators

Implemented a reusable `logging_decorator()` using:

- Nested wrapper functions
- `*args` and `**kwargs`
- `functools.wraps`
- Function execution logging
- Exception logging and propagation

### 3. Business Functions

Implemented:
- `calculate_bonus(salary, percentage=10)`
- `employee_salary(salary, bonus=5000)`

Validation includes:
- Negative salary and bonus rejection
- Invalid data type rejection
- Boolean rejection
- NaN and infinity rejection
- Bonus percentage boundaries (0–100)

### 4. Application Logging

Explored:
- `logging.getLogger()`
- `logging.info()`
- `logging.exception()`
- `logging.basicConfig()`
- File-based logging
- Timestamps, severity levels, filenames, function names and line numbers

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| `functools` | Function metadata preservation |
| `logging` | Application logging |
| `math` | Numeric validation |
| `unittest` | Automated testing |
| Black | Code formatting |

## Running the Examples

Activate your virtual environment and navigate to this directory.

Run closure demonstrations:

```bash
python demo_closures.py
```

Run decorator and logging demonstrations:

```bash
python run_logging_demo.py
```

Run the standalone exception logging exercise:

```bash
python demo_exception_logging.py
```

## Running Unit Tests

Run all tests:

```bash
python -m unittest discover -v
```

Run closure tests:

```bash
python -m unittest -v test_closures
```

Run decorator tests:

```bash
python -m unittest -v test_decorators
```

## Code Quality Checks

Format the code:

```bash
black .
```

Compile Python files:

```bash
python -m compileall .
```

Force recompilation:

```bash
python -m compileall -f .
```

Check Git whitespace errors:

```bash
git diff --check
```

## Test Results

**Latest verified result: 20 tests passed.**

| Test module | Tests |
|---|---:|
| `test_closures.py` | 4 |
| `test_decorators.py` | 16 |
| **Total** | **20** |

## Engineering Practices

This exercise emphasizes:

- Separation of reusable functions and demonstration scripts.
- Input validation before business calculations.
- Separation of business logic and cross-cutting logging concerns.
- Exception logging without suppressing original exceptions.
- Automated regression testing.
- Consistent code formatting.

**Production consideration:** Avoid logging sensitive function arguments or credentials. For long-running applications, consider rotating file handlers and centralized log management.

## Learning Outcome

By completing this module, the learner can implement closures, build reusable decorators, instrument Python functions with logging, validate business inputs, and verify application behaviour through automated tests.

---

## Author

**Navneet Tyagi**

Software Development | Python | Generative AI

*Learning, building, and sharing practical software engineering projects.*
