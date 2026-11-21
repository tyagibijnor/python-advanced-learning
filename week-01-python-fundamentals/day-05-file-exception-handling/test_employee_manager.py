
import json
import tempfile
import unittest

from pathlib import Path
from employee_manager import (
    EmployeeManager,
    InvalidEmployeeError
)


class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "employees.json"
        self.manager = EmployeeManager(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_load_employees(self):
        employees = [
            {"id": 1, "name": "Rahul", "salary": 50000}
        ]

        self.manager.save_employees(employees)

        self.assertEqual(
            self.manager.load_employees(),
            employees
        )

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(
            self.manager.load_employees(),
            []
        )

    def test_invalid_salary_raises_exception(self):
        employee = [
            {"id": 1, "name": "Rahul", "salary": -100}
        ]

        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_missing_employee_name(self):
        employee = [
            {"id": 1, "salary": 50000}
        ]

        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_invalid_json_file(self):
        self.file_path.write_text(
            "{invalid json",
            encoding="utf-8"
        )

        with self.assertRaises(InvalidEmployeeError):
            self.manager.load_employees()

    def test_json_must_contain_a_list(self):
        self.file_path.write_text(
            json.dumps({"id": 1}),
            encoding="utf-8"
        )

        with self.assertRaises(InvalidEmployeeError):
            self.manager.load_employees()


if __name__ == "__main__":
    unittest.main()
