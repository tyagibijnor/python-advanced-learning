# *args: multiple positional arguments
def calculate_total(*args):
    total = sum(args)
    return total


print(calculate_total(45000, 55000, 65000))


# **kwargs: multiple keyword arguments
def display_employee_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_employee_info(
    empId=123,
    name="Navneet",
    salary=70000,
    department="Product Development",
)


# Generator functions yield values one at a time.
def get_numbers():
    for number in range(1, 6):
        yield number


numbers = get_numbers()

for number in numbers:
    print(number)


# A closure is an inner function that can access its enclosing function's
# variables.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function


add_five = outer_function(5)
print(add_five(10))  # Output: 15


# Decorators modify the behavior of other functions.
def log_execution(func):
    def wrapper():
        print("Function started")
        func()
        print("Function completed")
    return wrapper


@log_execution
def process_employee():
    print("Processing employee data")


process_employee()

