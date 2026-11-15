
class Employee:
    def __init__(self, emp_id, name, salary, department):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.emp_id = emp_id
        self.name = name
        #self.salary = salary
        self.__salary = salary
        self.department = department

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Salary must be a number")
            
        if value < 0:
            raise ValueError("Salary cannot be negative")

        self.__salary = value

    @staticmethod
    def is_valid_salary(salary):
        return (
            isinstance(salary, (int, float))
            and not isinstance(salary, bool)
            and salary >= 0
        )
    
    ## using classmethod

    @classmethod
    def from_string(cls, employee_data):

        ## adding a check to ensure that the input is a string
        fields = [
        field.strip()
        for field in employee_data.split(",")
    ]
        ## added a check to ensure that the input string has exactly 4 fields
        if len(fields) != 4:
            raise ValueError("Expected 4 employee fields")
        emp_id, name, salary, department = fields
        
        return cls(
        int(emp_id),
        name,
        float(salary),
        department
    )

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.salary:,.2f}")
        print(f"Department: {self.department}")

    def increase_salary(self, rate):
        if not isinstance(rate, (int, float)) or isinstance(rate, bool):
            raise TypeError("Increment rate must be numeric")
        if rate < 0:
            raise ValueError("Increment rate cannot be negative")
        self.salary += self.salary * rate
        return self.salary

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department, team_size):
        super().__init__(emp_id, name, salary, department)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")

    def calculate_bonus(self):
        return self.salary * 0.15

class Developer(Employee):
    def __init__(self, emp_id, name, salary, department, programming_language):
        super().__init__(emp_id, name, salary, department)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.12


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added")
        self.employees.append(employee)

    def display_employees(self):
        print(f"Employees in {self.name}:")
        for employee in self.employees:
            employee.display_details()

    def calculate_total_salary(self):
        return sum(employee.salary for employee in self.employees)



employee1 = Employee(101, "Amit", 65000, "Engineering")
employee2 = Employee(102, "Vinit", 50000, "Operations")
manager = Manager(201, "Navneet", 200000, "Product Development", 6)

for person in [employee1, employee2, manager]:
    person.display_details()
    print(f"Bonus: ₹{person.calculate_bonus():,.2f}")
    print("-" * 40)


emp = Employee(101, "Amit", 65000, "Engineering")

print(emp.salary)

emp.salary = 70000
print(emp.salary)

## tested and commented out the below line to avoid ValueError
## emp.salary = -5000  # Should raise ValueError

## usig class method to create an employee from a string
employee_data = "103, Navneet, 75000, Product Development"
new_employee = Employee.from_string(employee_data)
new_employee.display_details()


## test case

# Test 1: Valid salary
emp = Employee(105, "Rahul", 80000, "IT")
print(emp.salary)

# Test 2: Invalid data type
## commented out the below line to avoid TypeError
##emp.salary = "90000"

# Test 3: Boolean salary
## commented out the below line to avoid TypeError
## emp.salary = True

# Test 4: Invalid employee string
## commented out the below line to avoid ValueError
## Employee.from_string("105,Rahul,80000")

# Test 5: Valid salary increment
emp.increase_salary(0.15)
print(emp.salary)


## testing for developer class

developer = Developer(
    301,
    "Rahul",
    80000,
    "Engineering",
    "Python"
)

developer.display_details()
print(f"Bonus: ₹{developer.calculate_bonus():,.2f}")

## add example for Department class
department = Department("Engineering")
department.add_employee(employee1)
department.add_employee(developer)
department.display_employees()
print(f"Total Salary: ₹{department.calculate_total_salary():,.2f}")

