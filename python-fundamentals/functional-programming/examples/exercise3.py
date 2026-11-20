"""Practice sorting, finding the second-highest salary, and aggregating raises."""

employees = [
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 65000},
    {"name": "Neha", "salary": 80000},
    {"name": "Priya", "salary": 55000},
]

MIN_SALARY = 60000
INCREMENT_RATE = 0.15


def main():
    high_earners = [
        employee
        for employee in employees
        if employee["salary"] > MIN_SALARY
    ]

    incremented_salaries = [
        {
            "name": employee["name"],
            "salary": round(employee["salary"] * (1 + INCREMENT_RATE), 2),
        }
        for employee in high_earners
    ]

    sorted_salaries = sorted(
        incremented_salaries,
        key=lambda employee: employee["salary"],
        reverse=True,
    )
    second_highest_salary = (
        sorted_salaries[1]["salary"] if len(sorted_salaries) > 1 else None
    )

    increment_count = len(incremented_salaries)
    total_increment_amount = sum(
        employee["salary"] * INCREMENT_RATE for employee in high_earners
    )

    print(f"Second Highest Salary: {second_highest_salary}")
    print(f"Number of Employees Receiving Increments: {increment_count}")
    print(f"Total Increment Amount: {total_increment_amount:.2f}")


if __name__ == "__main__":
    main()
