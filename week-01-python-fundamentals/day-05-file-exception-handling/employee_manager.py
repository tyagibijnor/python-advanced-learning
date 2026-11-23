"""Build an Employee Data Manager."""

import json
import math
import os
import tempfile
from pathlib import Path
from typing import Any


class InvalidEmployeeError(Exception):
    """Raised when employee information is invalid."""


class EmployeeManager:
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def validate_employee(self, employee: object) -> None:
        if not isinstance(employee, dict):
            raise InvalidEmployeeError("Each employee must be a dictionary.")

        required_fields = ("id", "name", "salary")
        for field in required_fields:
            if field not in employee:
                raise InvalidEmployeeError(f"Missing required field: {field}")

        employee_id = employee["id"]
        if (
            not isinstance(employee_id, int)
            or isinstance(employee_id, bool)
            or employee_id <= 0
        ):
            raise InvalidEmployeeError("Employee ID must be a positive integer.")

        name = employee["name"]
        if not isinstance(name, str) or not name.strip():
            raise InvalidEmployeeError("Employee name cannot be empty.")

        salary = employee["salary"]
        if isinstance(salary, bool) or not isinstance(salary, (int, float)):
            raise InvalidEmployeeError("Salary must be a positive finite number.")

        # math.isfinite() converts integers to float internally. Very large
        # integers can therefore raise OverflowError; treat those as invalid
        # salaries under this application's numeric range.
        try:
            salary_is_finite = math.isfinite(salary)
        except OverflowError:
            salary_is_finite = False

        if not salary_is_finite or salary <= 0:
            raise InvalidEmployeeError("Salary must be a positive finite number.")

    def save_employees(self, employees: list[dict[str, Any]]) -> None:
        if not isinstance(employees, list):
            raise InvalidEmployeeError("Employee data must be a list.")

        for employee in employees:
            self.validate_employee(employee)

        temporary_path: Path | None = None

        try:
            # Create the temporary file beside the destination so os.replace()
            # operates on the same filesystem.
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=self.file_path.parent,
                prefix=f".{self.file_path.name}.",
                suffix=".tmp",
                delete=False,
            ) as temporary_file:
                temporary_path = Path(temporary_file.name)
                json.dump(employees, temporary_file, indent=4, allow_nan=False)
                temporary_file.flush()
                os.fsync(temporary_file.fileno())

            os.replace(temporary_path, self.file_path)
            temporary_path = None

        except (OSError, TypeError, ValueError, OverflowError) as error:
            raise RuntimeError("Unable to save employee data.") from error

        finally:
            # Remove an incomplete temporary file if writing/replacement failed.
            if temporary_path is not None:
                try:
                    temporary_path.unlink(missing_ok=True)
                except OSError:
                    pass

    def load_employees(self) -> list[dict[str, Any]]:
        try:
            with self.file_path.open("r", encoding="utf-8") as file:
                employees = json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError as error:
            raise InvalidEmployeeError(
                "Employee file contains invalid JSON."
            ) from error

        except UnicodeDecodeError as error:
            raise InvalidEmployeeError(
                "Employee file must contain valid UTF-8 text."
            ) from error

        except OSError as error:
            raise RuntimeError("Unable to load employee data.") from error

        if not isinstance(employees, list):
            raise InvalidEmployeeError("Employee data must be a list.")

        for employee in employees:
            self.validate_employee(employee)

        return employees
