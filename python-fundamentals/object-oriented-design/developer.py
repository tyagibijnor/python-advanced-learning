"""Developer employee model."""

from employee import Employee


class Developer(Employee):
    def __init__(
        self, emp_id, name, salary, department, programming_language
    ):
        super().__init__(emp_id, name, salary, department)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.12
