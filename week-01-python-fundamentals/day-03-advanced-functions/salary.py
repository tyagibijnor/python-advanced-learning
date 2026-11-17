"""Salary reporting utilities using variable-length positional arguments."""


def salary_report(*args):
    """Return total, average, and highest salary from the supplied values."""
    if not args:
        raise ValueError("At least one salary is required")

    if any(
        isinstance(salary, bool) or not isinstance(salary, (int, float))
        for salary in args
    ):
        raise TypeError("Salary must be numeric")

    if any(salary < 0 for salary in args):
        raise ValueError("Salary cannot be negative")

    total_salary = sum(args)

    return {
        "total_salary": total_salary,
        "average_salary": total_salary / len(args),
        "highest_salary": max(args),
    }
