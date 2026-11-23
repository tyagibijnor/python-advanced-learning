# Build an Employee Data Manager

import json
import math
from pathlib import Path
from typing import Any


class InvalidEmployeeError(Exception):
    """Raised when employee information is invalid."""

    pass


class EmployeeManager:

    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def validate_employee(self, employee: object) -> None:
        if not isinstance(employee, dict):
            raise InvalidEmployeeError("Each employee must be a dictionary.")

        required_fields = ["id", "name", "salary"]

        for field in required_fields:
            if field not in employee:
                raise InvalidEmployeeError(f"Missing required field: {field}")

        if (
            not isinstance(employee["id"], int)
            or isinstance(employee["id"], bool)
            or employee["id"] <= 0
        ):
            raise InvalidEmployeeError("Employee ID must be a positive integer.")

        if not isinstance(employee["name"], str) or not employee["name"].strip():
            raise InvalidEmployeeError("Employee name cannot be empty.")

        if (
            not isinstance(employee["salary"], (int, float))
            or isinstance(employee["salary"], bool)
            or not math.isfinite(employee["salary"])
            or employee["salary"] <= 0
        ):
            raise InvalidEmployeeError("Salary must be a positive finite number.")

    def save_employees(self, employees: list[dict[str, Any]]) -> None:
        if not isinstance(employees, list):
            raise InvalidEmployeeError("Employee data must be a list.")

        try:
            for employee in employees:
                self.validate_employee(employee)

            with self.file_path.open("w", encoding="utf-8") as file:
                json.dump(employees, file, indent=4)

        except (OSError, TypeError) as error:
            raise RuntimeError("Unable to save employee data.") from error

    def load_employees(self) -> list[dict[str, Any]]:
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                employees = json.load(file)

            if not isinstance(employees, list):
                raise InvalidEmployeeError("Employee data must be a list.")

            for employee in employees:
                if not isinstance(employee, dict):
                    raise InvalidEmployeeError("Each employee must be a dictionary.")
                self.validate_employee(employee)

            return employees

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            raise InvalidEmployeeError(
                "Employee file contains invalid JSON."
            ) from error
