
from functools import reduce

employees = [
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 65000},
    {"name": "Neha", "salary": 80000},
    {"name": "Priya", "salary": 55000}
]

MIN_SALARY = 60000
INCREMENT_RATE = 0.15

# 1. Filter high earners
high_earners = list(
    filter(
        lambda emp: emp["salary"] > MIN_SALARY,
        employees
    )
)

# 2. Calculate revised salaries
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

# 3. Calculate total salary
total_salary = reduce(
    lambda acc, emp: acc + emp["salary"],
    incremented_salaries,
    0
)

# 4. Find highest-paid employee
highest_paid = max(
    incremented_salaries,
    key=lambda emp: emp["salary"]
)

# 5. Calculate average salary
average_salary = (
    total_salary / len(incremented_salaries)
    if incremented_salaries else 0
)

# 6. Display results
print("Incremented Employees:")
for emp in incremented_salaries:
    print(f'{emp["name"]}: {emp["salary"]}')

print(f"\nTotal Salary: {total_salary}")
print(f"Highest Paid: {highest_paid['name']} - {highest_paid['salary']}")
print(f"Average Salary: {average_salary}")
