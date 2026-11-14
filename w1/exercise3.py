
employees = [
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 65000},
    {"name": "Neha", "salary": 80000},
    {"name": "Priya", "salary": 55000}
]

MIN_SALARY = 60000
INCREMENT_RATE = 0.15

# Filter high earners
high_earners = list(
    filter(
        lambda emp: emp["salary"] > MIN_SALARY,
        employees
    )
)

# Calculate revised salaries
incremented_salaries = list(
    map(
        lambda emp: {
            "name": emp["name"],
            "salary": round(
                emp["salary"] * (1 + INCREMENT_RATE), 2
            )
        },
        high_earners
    )
)

# Find the second-highest salary after increment
sorted_salaries = sorted(
    incremented_salaries,
    key=lambda emp: emp["salary"],
    reverse=True
)
second_highest_salary = (
    sorted_salaries[1]["salary"]
    if len(sorted_salaries) > 1 else None
)
print(f"Second Highest Salary: {second_highest_salary}")

# Count the number of employees receiving increments
increment_count = len(incremented_salaries)
print(f"Number of Employees Receiving Increments: {increment_count}")

# Calculate the total increment amount (not total revised salary)
total_increment_amount = sum(
    emp["salary"] - next((
        original_emp["salary"]
        for original_emp in employees
        if original_emp["name"] == emp["name"]
    ))
    for emp in incremented_salaries
)
print(f"Total Increment Amount: {total_increment_amount}")
