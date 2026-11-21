# Build an Employee Data Manager

import json
from pathlib import Path


class InvalidEmployeeError(Exception):
    """Raised when employee information is invalid."""
    pass


class EmployeeManager:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def validate_employee(self, employee):
        required_fields = ["id", "name", "salary"]

        for field in required_fields:
            if field not in employee:
                raise InvalidEmployeeError(
                    f"Missing required field: {field}"
                )

        if not isinstance(employee["name"], str) or not employee["name"].strip():
            raise InvalidEmployeeError("Employee name cannot be empty.")

        if not isinstance(employee["salary"], (int, float)) or isinstance(employee["salary"], bool) or employee["salary"] <= 0:
            raise InvalidEmployeeError("Salary must be a positive number.")

    def save_employees(self, employees):
        try:
            for employee in employees:
                self.validate_employee(employee)

            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(employees, file, indent=4)

        except (OSError, TypeError) as error:
            raise RuntimeError("Unable to save employee data.") from error

    def load_employees(self):
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                employees = json.load(file)

            if not isinstance(employees, list):
                raise InvalidEmployeeError(
                    "Employee data must be a list."
                )

            for employee in employees:
                if not isinstance(employee, dict):
                    raise InvalidEmployeeError(
                        "Each employee must be a dictionary."
                    )
                self.validate_employee(employee)

            return employees

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            raise InvalidEmployeeError(
                "Employee file contains invalid JSON."
            ) from error
