"""Small demonstrations of args, kwargs, generators, closures, and decorators."""


def calculate_total(*args):
    """Return the sum of positional arguments."""
    return sum(args)


def display_employee_info(**kwargs):
    """Print employee information supplied as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def get_numbers():
    """Yield numbers one at a time."""
    yield from range(1, 6)


def outer_function(x):
    """Return a closure that adds x to its argument."""

    def inner_function(y):
        return x + y

    return inner_function


def log_execution(func):
    """Print messages immediately before and after calling a function."""

    def wrapper():
        print("Function started")
        func()
        print("Function completed")

    return wrapper


@log_execution
def process_employee():
    """Example function wrapped by the log_execution decorator."""
    print("Processing employee data")


def main():
    print(calculate_total(45000, 55000, 65000))

    display_employee_info(
        emp_id=123,
        name="Navneet",
        salary=70000,
        department="Product Development",
    )

    for number in get_numbers():
        print(number)

    add_five = outer_function(5)
    print(add_five(10))

    process_employee()


if __name__ == "__main__":
    main()
