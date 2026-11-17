# Day 3 – Advanced Python Functions

## Topics Covered

### 1. Variable-Length Arguments

- `*args` – Accept multiple positional arguments.
- `**kwargs` – Accept multiple keyword arguments.
- Dictionary iteration using `.items()`.

### 2. Practical Exercises

**Exercise 1 – Employee Salary Report (`salary.py`)**

- Calculate total salary.
- Calculate average salary.
- Find highest salary.
- Validate salary inputs.

**Exercise 2 – Employee Bonus Calculator (`bonus.py`)**

- Calculate employee bonuses using a 10% rate.
- Calculate total bonus payout.
- Validate input data.
- Return structured results.

### 3. Unit Testing

Using Python's built-in `unittest` framework:

- `test_salary.py`
- `test_bonus.py`

Test scenarios:
- Valid calculations.
- Empty input.
- Negative salary.
- Expected exceptions.

## How to Run

Run the tests from this directory:

```bash
python -m unittest -v
```

Run individual test files:

```bash
python -m unittest -v test_salary.py
python -m unittest -v test_bonus.py
```

## Key Learnings

- Writing reusable functions.
- Handling variable-length arguments.
- Input validation and exception handling.
- Separating business logic from presentation.
- Automated unit testing.

## Next Topics

- Generators and `yield`
- Iterators
- Closures
- Decorators
