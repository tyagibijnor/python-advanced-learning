class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₹{self.salary}")
        print(f"Department: {self.department}")

    def increase_salary(self, rate):
        increment = self.salary * rate
        self.salary += increment
        return self.salary

    def calculated_bonus(self):
        return 6500

class Manager(Employee):
    def __init__(self, emp_id, name, salary, department, team_size):
        super().__init__(emp_id, name, salary, department)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size: {self.team_size}")

    def calculated_bonus(self):
        return 30000

employee1 = Employee(101, "Amit", 65000, "Engineering")
employee2 = Employee(102, "Vinit", 50000, "Operations")
manager = Manager(201, "Navneet", 200000, "Product Development", 6)

employee1.display_details()
print(f"Bonus: ₹{employee1.calculated_bonus()}")
print()
employee2.display_details()
print(f"Bonus: ₹{employee2.calculated_bonus()}")
print()
manager.display_details()
print(f"Bonus: ₹{manager.calculated_bonus()}")
