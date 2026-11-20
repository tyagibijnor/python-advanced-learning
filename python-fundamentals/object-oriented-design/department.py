"""Department model for grouping employees."""

from employee import Employee


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
