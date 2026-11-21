"""Tests for department composition and employee subclasses."""

import unittest

from department import Department
from developer import Developer
from employee import Employee
from manager import Manager


class DepartmentTests(unittest.TestCase):
    def test_department_totals_employee_and_subclass_salaries(self):
        department = Department("Engineering")
        department.add_employee(Employee(1, "Amit", 50000, "Engineering"))
        department.add_employee(
            Manager(2, "Navneet", 100000, "Engineering", team_size=5)
        )
        department.add_employee(
            Developer(3, "Rahul", 80000, "Engineering", "Python")
        )

        self.assertEqual(department.calculate_total_salary(), 230000)

    def test_department_rejects_non_employee_objects(self):
        department = Department("Engineering")

        with self.assertRaises(TypeError):
            department.add_employee("Amit")


class EmployeeRoleTests(unittest.TestCase):
    def test_manager_bonus_rate(self):
        manager = Manager(2, "Navneet", 100000, "Engineering", team_size=5)

        self.assertEqual(manager.calculate_bonus(), 15000)

    def test_developer_bonus_rate(self):
        developer = Developer(3, "Rahul", 100000, "Engineering", "Python")

        self.assertEqual(developer.calculate_bonus(), 12000)


if __name__ == "__main__":
    unittest.main()
