

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

## kwargs – Multiple keyword arguments


def calculate_bonus(**kwargs):

    INCREMENT_RATE = 0.10
    total_bonus = 0

    if not kwargs:
        raise ValueError("At least one employee is required")

    if any(isinstance(s, bool) or not isinstance(s, (int, float))
           for s in kwargs.values()):
        raise TypeError("Salary must be numeric")

    if any(s < 0 for s in kwargs.values()):
        raise ValueError("Salary cannot be negative")

    for employee, salary in kwargs.items():

        bonus = round(salary * INCREMENT_RATE, 2)

        print(
            f"{employee} - Salary: {salary} - Bonus: {bonus}"
        )

        total_bonus += bonus

    print(f"\nTotal Bonus Payout: {total_bonus}")

    return total_bonus


## args test
print("--" * 10)
print("TEST FOR ARGRS")
result = salary_report(45000, 65000, 80000, 55000)
print(result)


## kwargs test
print("--" * 10)
print("TEST FOR KWARGS")
result = calculate_bonus(
    Amit=50000,
    Rahul=60000,
    Neha=80000
)
