
employees = [
    {"name": "Rahul", "salary": 45000, "performance_rating": 3.5},
    {"name": "Amit", "salary": 65000, "performance_rating": 4.0},
    {"name": "Neha", "salary": 80000, "performance_rating": 4.5},
    {"name": "Priya", "salary": 55000, "performance_rating": 3.0},
    {"name": "Kuhu", "salary": 80000, "performance_rating": 4.0}
]

MIN_RATING = 4.0
INCREMENT_RATE = 0.20

# 1. Filter eligible employees
high_performance_employees = list(
    filter(
        lambda emp: emp["performance_rating"] >= MIN_RATING,
        employees
    )
)

# 2. Calculate revised salaries
incremented_salaries = list(
    map(
        lambda emp: {
            **emp,
            "salary": round(
                emp["salary"] * (1 + INCREMENT_RATE), 2
            )
        },
        high_performance_employees
    )
)

# 3. Calculate total and average
total_salary = sum(
    emp["salary"] for emp in incremented_salaries
)

average_salary = (
    total_salary / len(incremented_salaries)
    if incremented_salaries else 0
)

# 4. Find unique salaries
unique_salaries = sorted(
    {emp["salary"] for emp in incremented_salaries}
)

# 5. Find all highest-paid employees
highest_paid_employees = []

if incremented_salaries:
    highest_salary = max(
        emp["salary"] for emp in incremented_salaries
    )

    highest_paid_employees = [
        emp for emp in incremented_salaries
        if emp["salary"] == highest_salary
    ]

# 6. Count eligible employees
incremented_count = len(incremented_salaries)

# 7. Display report
print("HR PERFORMANCE & SALARY REPORT")
print("-" * 40)

for emp in incremented_salaries:
    print(
        f"{emp['name']}: "
        f"₹{emp['salary']:,.2f} "
        f"(Rating: {emp['performance_rating']})"
    )

print("-" * 40)
print(f"Total Revised Salary: ₹{total_salary:,.2f}")
print(f"Average Salary: ₹{average_salary:,.2f}")
print(f"Unique Salaries: {unique_salaries}")
print(f"Incremented Employees: {incremented_count}")

for emp in highest_paid_employees:
    print(
        f"Highest Paid: {emp['name']} "
        f"- ₹{emp['salary']:,.2f}"
    )
