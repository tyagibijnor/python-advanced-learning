"""Employee bonus calculation using variable-length keyword arguments."""

INCREMENT_RATE = 0.10


def calculate_bonus(**kwargs):
    """Return each employee's bonus and the total bonus payout."""
    if not kwargs:
        raise ValueError("At least one employee is required")

    if any(
        isinstance(salary, bool) or not isinstance(salary, (int, float))
        for salary in kwargs.values()
    ):
        raise TypeError("Salary must be numeric")

    if any(salary < 0 for salary in kwargs.values()):
        raise ValueError("Salary cannot be negative")

    bonuses = {
        employee: round(salary * INCREMENT_RATE, 2)
        for employee, salary in kwargs.items()
    }

    return {
        "bonuses": bonuses,
        "total_bonus": sum(bonuses.values()),
    }
