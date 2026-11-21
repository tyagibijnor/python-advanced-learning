"""Base employee model."""


class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
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

    @classmethod
    def from_string(cls, employee_data):
        if not isinstance(employee_data, str):
            raise TypeError("Employee data must be a string")

        fields = [field.strip() for field in employee_data.split(",")]
        if len(fields) != 4:
            raise ValueError("Expected 4 employee fields")

        emp_id, name, salary, department = fields
        return cls(int(emp_id), name, float(salary), department)

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
