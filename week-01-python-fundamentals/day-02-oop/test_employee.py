"""Tests for the employee models."""

import unittest

from employee import Employee


class EmployeeTests(unittest.TestCase):
    def test_salary_must_be_nonnegative(self):
        with self.assertRaises(ValueError):
            Employee(1, "Amit", -1, "Engineering")

    def test_salary_must_be_numeric_and_not_boolean(self):
        employee = Employee(1, "Amit", 50000, "Engineering")

        for invalid_salary in ("50000", True):
            with self.subTest(salary=invalid_salary):
                with self.assertRaises(TypeError):
                    employee.salary = invalid_salary

    def test_increase_salary(self):
        employee = Employee(1, "Amit", 50000, "Engineering")

        self.assertEqual(employee.increase_salary(0.10), 55000)

    def test_from_string(self):
        employee = Employee.from_string("103, Navneet, 75000, Product Development")

        self.assertEqual(employee.emp_id, 103)
        self.assertEqual(employee.name, "Navneet")
        self.assertEqual(employee.salary, 75000)
        self.assertEqual(employee.department, "Product Development")

    def test_from_string_requires_four_fields(self):
        with self.assertRaises(ValueError):
            Employee.from_string("103, Navneet, 75000")


if __name__ == "__main__":
    unittest.main()
