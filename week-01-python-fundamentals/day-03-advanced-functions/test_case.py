## *args – Multiple positional arguments
def calculate_total(*args):
    total = sum(args)
    return total

## test the function
print(calculate_total(45000, 55000, 65000))

## **kwargs – Multiple keyword arguments
def display_employee_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

## test the function
display_employee_info(empId=123, name="Navneet", salary=70000, department="Product Development")

## Generator functions – Functions that yield values one at a time
def get_numbers():
    for i in range(1, 6):
        yield i

numbers = get_numbers()

for num in numbers:
    print(num)

## closure – A function defined inside another function that has access to the outer function’s variables
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

## test the closure
add_five = outer_function(5)
print(add_five(10))  # Output: 15

## decorators – Functions that modify the behavior of other functions
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
print()
print("==" * 10)
print("TEST FOR ARGRS")

def salary_report(*args):
    total_salary = sum(args)
    average_salary = total_salary / len(args) if args else 0
    highest_salary = max(args) if args else 0
    print("--" * 10)
    print(f"Total Salary: {total_salary}")
    print(f"Average Salary: {average_salary}")
    print(f"Highest Salary: {highest_salary}")

salary_report(45000, 65000, 80000, 55000)



