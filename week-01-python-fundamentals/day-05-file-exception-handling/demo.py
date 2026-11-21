from employee_manager import EmployeeManager

manager = EmployeeManager("employees.json")

employees = [
    {"id": 101, "name": "Rahul", "salary": 50000},
    {"id": 102, "name": "Amit", "salary": 60000}
]

manager.save_employees(employees)

data = manager.load_employees()

print(data)