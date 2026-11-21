"""Functional-style analysis of employee salaries."""

from functools import reduce


EMPLOYEES = [
    {"name": "Rahul", "salary": 45000, "performance_rating": 3.5},
    {"name": "Amit", "salary": 65000, "performance_rating": 4.0},
    {"name": "Neha", "salary": 80000, "performance_rating": 4.5},
    {"name": "Priya", "salary": 55000, "performance_rating": 3.0},
    {"name": "Kuhu", "salary": 80000, "performance_rating": 4.0},
]

MIN_RATING = 4.0
INCREMENT_RATE = 0.20


def analyze_salaries(employees, min_rating=MIN_RATING, increment_rate=INCREMENT_RATE):
    """Return a report for eligible employees without modifying the input."""
    eligible_employees = list(
        filter(
            lambda employee: employee["performance_rating"] >= min_rating,
            employees,
        )
    )
    revised_employees = list(
        map(
            lambda employee: {
                **employee,
                "salary": round(employee["salary"] * (1 + increment_rate), 2),
            },
            eligible_employees,
        )
    )

    total_salary = reduce(
        lambda total, employee: total + employee["salary"],
        revised_employees,
        0,
    )
    highest_salary = max(
        (employee["salary"] for employee in revised_employees),
        default=None,
    )

    return {
        "employees": revised_employees,
        "total_salary": total_salary,
        "average_salary": (
            total_salary / len(revised_employees) if revised_employees else 0
        ),
        "unique_salaries": sorted(
            {employee["salary"] for employee in revised_employees}
        ),
        "highest_paid_employees": [
            employee
            for employee in revised_employees
            if employee["salary"] == highest_salary
        ],
    }


def main():
    report = analyze_salaries(EMPLOYEES)

    print("HR PERFORMANCE & SALARY REPORT")
    print("-" * 40)
    for employee in report["employees"]:
        print(
            f"{employee['name']}: ₹{employee['salary']:,.2f} "
            f"(Rating: {employee['performance_rating']})"
        )

    print("-" * 40)
    print(f"Total Revised Salary: ₹{report['total_salary']:,.2f}")
    print(f"Average Salary: ₹{report['average_salary']:,.2f}")
    print(f"Unique Salaries: {report['unique_salaries']}")
    for employee in report["highest_paid_employees"]:
        print(f"Highest Paid: {employee['name']} - ₹{employee['salary']:,.2f}")


if __name__ == "__main__":
    main()
