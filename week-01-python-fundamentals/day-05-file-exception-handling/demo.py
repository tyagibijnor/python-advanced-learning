"""Run a small EmployeeManager demonstration."""

from employee_manager import EmployeeManager


def main() -> None:
    manager = EmployeeManager("employees-demo.json")
    employees = [
        {"id": 101, "name": "Rahul", "salary": 50000},
        {"id": 102, "name": "Amit", "salary": 60000},
    ]
    manager.save_employees(employees)
    print(manager.load_employees())


if __name__ == "__main__":
    main()
