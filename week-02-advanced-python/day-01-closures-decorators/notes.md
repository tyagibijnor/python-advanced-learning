
# Week 02 – Day 01: Closures & Decorators

## 1. Closures

A closure is a function that remembers variables from its enclosing scope,
even after the outer function has finished executing.

### Example

```python
def make_multiplier(factor):
    def multiply(value):
        return factor * value

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))  # 20
print(triple(10))  # 30
```

### Key concepts

- Inner functions can access variables from outer functions.
- The returned function retains access to those variables.
- Each closure maintains its own independent state.
- Closures are useful for function factories and state management.

## 2. The nonlocal Keyword

`nonlocal` allows an inner function to modify a variable defined in
its nearest enclosing function scope.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

Without `nonlocal`, assigning to `count` inside `increment()` would
create a local variable and could result in `UnboundLocalError`.

## 3. Decorators

A decorator is a function that takes another function, extends its
behaviour, and returns a modified or wrapped function.

### Basic example

```python
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


@my_decorator
def greet():
    print("Hello!")


greet()
```

The following syntax:

```python
@my_decorator
def greet():
    pass
```

is equivalent to:

```python
def greet():
    pass

greet = my_decorator(greet)
```

## 4. *args and **kwargs

Decorators should support functions with different arguments.

- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.

```python
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function:", func.__name__)
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        return func(*args, **kwargs)

    return wrapper
```

## 5. functools.wraps

Use `@wraps(func)` to preserve the original function's metadata.

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Without `@wraps`, attributes such as `__name__` and `__doc__`
may refer to the wrapper instead of the original function.

## 6. Python Logging

Logging records application events with different severity levels.

| Level | Purpose |
|---|---|
| DEBUG | Detailed diagnostic information |
| INFO | Normal application events |
| WARNING | Unexpected situations |
| ERROR | Operation failures |
| CRITICAL | Serious application failures |

### Module-level logger

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Application started")
logger.warning("Unexpected input")
logger.error("Operation failed")
```

### Logging an exception

```python
try:
    raise ValueError("Invalid payment")

except ValueError:
    logger.exception("Payment processing failed")
```

`logger.exception()` records the error message and traceback.
It should normally be called inside an exception handler.

## 7. Input Validation

Validate function arguments before performing business calculations.

Important checks used in this exercise:

- Reject Boolean values when a numeric value is required.
- Validate numeric types.
- Use `math.isfinite()` to reject NaN and infinity.
- Reject negative salary and bonus values.
- Validate percentage ranges.

Example:

```python
import math

def validate_salary(salary):
    if isinstance(salary, bool) or not isinstance(salary, (int, float)):
        raise TypeError("Salary must be a number")

    if not math.isfinite(salary):
        raise ValueError("Salary must be finite")

    if salary < 0:
        raise ValueError("Salary cannot be negative")
```

Remember: `bool` is a subclass of `int` in Python.
That is why explicit Boolean validation is useful.

## 8. Exception Handling in Decorators

A logging decorator can log exceptions and re-raise them.

```python
try:
    result = func(*args, **kwargs)
    logger.info("Function completed successfully")
    return result

except Exception:
    logger.exception("Function execution failed")
    raise
```

A bare `raise` inside an exception handler re-raises the original
exception without suppressing it.

## 9. Unit Testing

Use `unittest` to verify expected behaviour.

Important testing concepts:

- `assertEqual()` checks expected results.
- `assertRaises()` checks expected exceptions.
- `assertLogs()` verifies logging output.
- `assertIs()` can check object identity.
- Test normal inputs, invalid inputs and edge cases.

Run tests:

```bash
python -m unittest discover -s week-02-advanced-python/day-01-closures-decorators -v
```

Current Day 01 result: 20 tests passed.

## 10. Important Commands

```bash
black .
python -m compileall -f .
python -m unittest discover -v
git diff --check
git status --short
git diff --cached --check
```

For focused formatting, prefer:

```bash
black week-02-advanced-python/day-01-closures-decorators/
```

## 11. Interview Questions

1. What is a closure in Python?
2. What is the difference between `nonlocal` and `global`?
3. What is a decorator?
4. Why do decorators use `*args` and `**kwargs`?
5. What is the purpose of `functools.wraps`?
6. What is the difference between `logger.error()` and `logger.exception()`?
7. Why should exceptions sometimes be logged and re-raised?
8. Why is `bool` explicitly checked during numeric validation?
9. What is the purpose of `math.isfinite()`?
10. How would you test a decorator?

## 12. Day 01 Learning Outcome

Completed:

- Closures and function factories.
- Independent closure state.
- The `nonlocal` keyword.
- Function decorators.
- `*args` and `**kwargs`.
- `functools.wraps`.
- Application logging.
- Exception logging and propagation.
- Input validation.
- Unit testing and edge-case testing.

**Test status:** 20/20 tests passing.
**Formatting status:** Black check passed.

---

## Author

**Navneet Tyagi**

Python | Software Engineering | Generative AI
