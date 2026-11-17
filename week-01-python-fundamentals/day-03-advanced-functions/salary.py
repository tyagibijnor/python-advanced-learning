def salary_report(*args):

    if not args:
        raise ValueError("At least one salary is required")

    if any(isinstance(s, bool) or not isinstance(s, (int, float))
           for s in args):
        raise TypeError("Salary must be numeric")

    if any(s < 0 for s in args):
        raise ValueError("Salary cannot be negative")

    total_salary = sum(args)
    average_salary = total_salary / len(args)
    highest_salary = max(args)

    report = {
        "total_salary": total_salary,
        "average_salary": average_salary,
        "highest_salary": highest_salary
    }

    return report