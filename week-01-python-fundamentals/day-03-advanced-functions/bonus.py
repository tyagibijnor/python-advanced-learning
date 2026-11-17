def calculate_bonus(**kwargs):

    INCREMENT_RATE = 0.10

    if not kwargs:
        raise ValueError("At least one employee is required")

    if any(isinstance(s, bool) or not isinstance(s, (int, float))
           for s in kwargs.values()):
        raise TypeError("Salary must be numeric")

    if any(s < 0 for s in kwargs.values()):
        raise ValueError("Salary cannot be negative")

    bonuses = {}

    for employee, salary in kwargs.items():
        bonuses[employee] = round(salary * INCREMENT_RATE, 2)

    return {
        "bonuses": bonuses,
        "total_bonus": sum(bonuses.values())
    }
