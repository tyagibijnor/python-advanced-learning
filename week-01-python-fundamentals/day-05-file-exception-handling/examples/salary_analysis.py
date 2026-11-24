
"""Load employee JSON and print basic salary statistics."""

import json
import math
from pathlib import Path


def is_valid_salary(salary: object) -> bool:
    """Return True for positive, finite numeric salaries."""
    if isinstance(salary, bool):
        return False

    if isinstance(salary, int):
        return salary > 0

    if isinstance(salary, float):
        return math.isfinite(salary) and salary > 0

    return False


def salary_analysis(json_file: str | Path) -> None:
    """Calculate and print salary statistics from employee JSON."""
    try:
        with Path(json_file).open("r", encoding="utf-8") as file:
            employees = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError("Employee JSON contains invalid data.") from error

    if not isinstance(employees, list):
        raise ValueError("Employee JSON must contain a list.")

    salaries = [
        employee["salary"]
        for employee in employees
        if isinstance(employee, dict)
        and is_valid_salary(employee.get("salary"))
    ]

    if not salaries:
        print("No valid salary records found.")
        return

    total_salary = sum(salaries)

    print(f"Employee records with salaries: {len(salaries)}")
    print(f"Total salary: {total_salary:,.2f}")
    print(f"Average salary: {total_salary / len(salaries):,.2f}")
    print(f"Highest salary: {max(salaries):,.2f}")
    print(f"Lowest salary: {min(salaries):,.2f}")


if __name__ == "__main__":
    sample_file = Path(__file__).resolve().parent.parent / "employees.json"
    salary_analysis(sample_file)
