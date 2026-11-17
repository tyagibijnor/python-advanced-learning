# Day 1 – Functional Programming

## Learning covered

- Lambda expressions
- `map()` and `filter()`
- `functools.reduce()`
- Filtering and transforming employee records
- Salary aggregation, sorting, and reporting
- Working with lists, dictionaries, and comprehensions

## Main practical example

`employee_salary_analytics.py` contains the consolidated employee salary
analytics exercise. It filters eligible employees, calculates revised
salaries, aggregates totals, and identifies the highest-paid employees.

Run it:

```bash
python employee_salary_analytics.py
```

## Additional practice

The `examples/` folder preserves the original exercises and focused examples:

- `exercise1.py`, `exercise2.py`, `exercise3.py`
- `lambda_functions.py`
- `map_filter.py`
- `reduce_examples.py`

Run an example from this folder:

```bash
python examples/exercise1.py
```

## Tests

Run the automated tests from this directory:

```bash
python -m unittest -v
```

The tests verify report calculations, custom thresholds, empty input, and
that the original employee data is not modified.
