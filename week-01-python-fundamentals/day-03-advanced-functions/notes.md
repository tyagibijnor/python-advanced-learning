## Generators

A **generator** is a function that returns values one at a time using `yield`.
Generator functions return a generator object and execute only when `next()` is
called or when the object is iterated.

Key generator features:

- `yield` pauses the function and saves its state.
- Calling `next()` resumes execution from the saved state.
- A generator ends when execution reaches the end of the function.
- `StopIteration` is raised automatically when a generator is exhausted.
- Generators use lazy evaluation, so values are produced as needed.

### Generator functions in `generators.py`

#### `gen_number()`

Produces integer values from 1 through 10.

```python
def gen_number():
    for i in range(1, 11):
        yield i
```

Usage:

```python
numbers = gen_number()

for number in numbers:
    print(number)
```

#### `even_number()`

Produces only even integers from 1 through 50.

```python
def even_number():
    for i in range(1, 51):
        if i % 2 == 0:
            yield i
```

#### `employee_generator(employees)`

Iterates through employee dictionaries and yields each employee whose ID is
greater than 101 as an `(id, name)` tuple.

```python
def employee_generator(employees):
    for employee in employees:
        if employee["id"] > 101:
            yield (employee["id"], employee["name"])
```

Usage:

```python
employees = [
    {"id": 101, "name": "Amit"},
    {"id": 102, "name": "Rahul"},
]

for employee in employee_generator(employees):
    print(employee)
```

## Iterators

An **iterator** is an object that tracks the next value in a sequence. It
implements the iterator protocol through `iter()` and `next()`.

- `iter(sequence)` creates an iterator from an iterable.
- `next(iterator)` returns the next value.
- `StopIteration` means no more values remain.

### `basic_iter(emp)` in `iterators.py`

`basic_iter()` creates an iterator from the supplied sequence and prints each
value until `StopIteration` is caught.

```python
def basic_iter(emp):
    emp = iter(emp)
    while True:
        try:
            print(next(emp))
        except StopIteration:
            break
```

Usage:

```python
employee_names = ["Navneet", "Amit", "Neha", "Kuhu"]
basic_iter(employee_names)
```

## Generators versus iterators

- All generators are iterators, but not all iterators are generators.
- Generators are created with `yield` and require less setup.
- Iterators use `iter()` and `next()` to retrieve values sequentially.
- `StopIteration` is handled explicitly when using manual `next()` calls or
  custom iterator loops.

## Unit tests

- `test_generators.py` tests number, even-number, employee, and empty-list
  generator behavior.
- `test_iterators.py` tests printed output for populated and empty sequences.
