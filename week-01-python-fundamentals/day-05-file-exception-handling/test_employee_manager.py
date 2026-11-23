import json
import tempfile
import unittest

from pathlib import Path
from employee_manager import EmployeeManager, InvalidEmployeeError


class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = Path(self.temp_dir.name) / "employees.json"
        self.manager = EmployeeManager(self.file_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_load_employees(self):
        employees = [{"id": 1, "name": "Navneet", "salary": 50000}]

        self.manager.save_employees(employees)

        self.assertEqual(self.manager.load_employees(), employees)

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(self.manager.load_employees(), [])

    def test_invalid_salary_raises_exception(self):
        employee = [{"id": 1, "name": "Navneet", "salary": -100}]

        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_missing_employee_name(self):
        employee = [{"id": 1, "salary": 50000}]

        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_missing_employee_salary(self):
        employee = [{"id": 1, "name": "Navneet"}]

        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_missing_employee_id(self):
        employee = [{"name": "Navneet", "salary": 50000}]

        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_invalid_employee_id(self):
        invalid_ids = [0, -1, "1", True]

        for invalid_id in invalid_ids:
            with self.subTest(invalid_id=invalid_id):
                employee = [{"id": invalid_id, "name": "Navneet", "salary": 50000}]

                with self.assertRaises(InvalidEmployeeError):
                    self.manager.save_employees(employee)

    def test_invalid_json_file(self):
        self.file_path.write_text("{invalid json", encoding="utf-8")

        with self.assertRaises(InvalidEmployeeError):
            self.manager.load_employees()

    def test_json_must_contain_a_list(self):
        self.file_path.write_text(json.dumps({"id": 1}), encoding="utf-8")

        with self.assertRaises(InvalidEmployeeError):
            self.manager.load_employees()

    def test_save_requires_a_list(self):
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees({"id": 1})

    def test_employee_must_be_a_dictionary(self):
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(["Navneet"])

    def test_nan_salary_raises_exception(self):
        employee = [{"id": 1, "name": "Navneet", "salary": float("nan")}]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_infinite_salary_raises_exception(self):
        employee = [{"id": 1, "name": "Navneet", "salary": float("inf")}]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

    def test_employee_string_input_raises_exception(self):
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(["Navneet"])

    def test_employee_list_input_raises_exception(self):
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees([["Navneet"]])

    def test_employee_none_input_raises_exception(self):
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees([None])
    
    def test_employee_name_whitespace_input_raises_exception(self):
        employee = [{"id": 1, "name": " ", "salary": 10000 }]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)
    
    def test_employee_id_decimal_input_raises_exception(self):
        employee = [{"id": 1.5, "name": "Navneet", "salary": 10000 }]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)
    
    def test_employee_salary_boolean_input_raises_exception(self):
        employee = [{"id": 1, "name": "Navneet", "salary": True }]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)
    
    def test_negative_infinite_salary_raises_exception(self):
        employee = [{"id": 1, "name": "Navneet", "salary": float("-inf")}]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)
    
    def test_large_integer_salary_raises_exception(self):
        employee = [{"id": 1, "name": "Navneet", "salary": 10**1000}]
        with self.assertRaises(InvalidEmployeeError):
            self.manager.save_employees(employee)

if __name__ == "__main__":
    unittest.main()
