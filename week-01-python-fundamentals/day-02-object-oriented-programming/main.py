"""Demonstrate the employee and department classes."""

from department import Department
from developer import Developer
from employee import Employee
from manager import Manager


def main():
    department = Department("Engineering")
    department.add_employee(Employee(101, "Amit", 65000, "Engineering"))
    department.add_employee(
        Manager(201, "Navneet", 200000, "Engineering", team_size=6)
    )
    department.add_employee(
        Developer(301, "Rahul", 80000, "Engineering", "Python")
    )

    department.display_employees()
    print(f"Total Salary: ₹{department.calculate_total_salary():,.2f}")


if __name__ == "__main__":
    main()
