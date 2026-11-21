# Day 2 – Object-Oriented Programming

## Learning covered

- Classes and objects
- Constructors and instance attributes
- Encapsulation using a property and setter
- Instance methods, static methods, and class methods
- Inheritance and `super()`
- Method overriding and polymorphism
- Composition through a `Department` containing employees
- Input validation and custom exceptions

## Project files

- `employee.py` – Base employee model and salary validation
- `manager.py` – Manager subclass with an overridden bonus calculation
- `developer.py` – Developer subclass with an overridden bonus calculation
- `department.py` – Department composition and salary aggregation
- `main.py` – Demonstration of the employee hierarchy
- `test_employee.py` – Employee model tests
- `test_department.py` – Department, Manager, and Developer tests

The JPG files are retained as learning diagrams.

## Run the demonstration

```bash
python main.py
```

## Run all tests

```bash
python -m unittest -v
```
