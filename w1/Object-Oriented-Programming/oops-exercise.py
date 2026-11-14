
class Employee:
    def __init__(self, emp_id, name, salary, department):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.salary:,.2f}")
        print(f"Department: {self.department}")

    def increase_salary(self, rate):
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


employee1 = Employee(101, "Amit", 65000, "Engineering")
employee2 = Employee(102, "Vinit", 50000, "Operations")
manager = Manager(201, "Navneet", 200000, "Product Development", 6)

for person in [employee1, employee2, manager]:
    person.display_details()
    print(f"Bonus: ₹{person.calculate_bonus():,.2f}")
    print("-" * 40)
