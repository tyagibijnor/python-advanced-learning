
from functools import reduce

employees = [
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 65000},
    {"name": "Neha", "salary": 80000},
    {"name": "Priya", "salary": 55000}
]

MIN_SALARY = 60000
INCREMENT_RATE = 0.10

# 1. Filter high earners
high_earners = list(
    filter(lambda emp: emp["salary"] > MIN_SALARY, employees)
)

# 2. Calculate updated salaries
updated_salaries = list(
    map(
        lambda emp: {
            "name": emp["name"],
            "salary": round(emp["salary"] * (1 + INCREMENT_RATE), 2)
        },
        employees
    )
)

# 3. Display results
print("Employees earning above threshold:")
for emp in high_earners:
    print(f'{emp["name"]} - {emp["salary"]}')

print("\nUpdated employee salaries:")
for emp in updated_salaries:
    print(f'{emp["name"]} - {emp["salary"]}')
