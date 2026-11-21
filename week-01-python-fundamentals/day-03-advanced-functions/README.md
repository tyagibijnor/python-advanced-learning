# Day 3 – Advanced Python Functions

## Learning covered

### Variable-length arguments

- `*args` – Accept multiple positional arguments.
- `**kwargs` – Accept multiple keyword arguments.
- Dictionary iteration using `.items()`.

### Practical exercises

- `salary.py` – Calculate total, average, and highest salary using `*args`.
- `bonus.py` – Calculate individual and total employee bonuses using `**kwargs`.
- Both functions validate empty input, numeric types, booleans, and negative values.

### Unit testing

- `test_salary.py` – Salary calculation and input validation tests.
- `test_bonus.py` – Bonus calculation and input validation tests.
- Tests use Python's built-in `unittest` framework.

### Additional concept demonstrations

`function_concepts_demo.py` preserves the original introductory examples for
generators (`yield`), closures, and decorators. These are demonstration
snippets, not a claim that the detailed lessons have been completed.

## Run the examples

```bash
python function_concepts_demo.py
```

## Run all tests

```bash
python -m unittest -v
```

## Key learning outcomes

- Reusable functions and variable-length arguments
- Input validation and exception handling
- Separating business logic from printed output
- Returning structured dictionaries
- Automated tests for normal and invalid input
