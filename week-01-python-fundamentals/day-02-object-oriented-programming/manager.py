"""Manager employee model."""

from employee import Employee


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department, team_size):
        super().__init__(emp_id, name, salary, department)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")

    def calculate_bonus(self):
        return self.salary * 0.15
