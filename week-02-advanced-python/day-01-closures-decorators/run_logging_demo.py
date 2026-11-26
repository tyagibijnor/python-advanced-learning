import logging

from decorators import calculate_bonus, employee_salary

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

print("Bonus:", calculate_bonus(50000, percentage=15))

print("Employee salary:", employee_salary(50000))

print("Employee salary:", employee_salary(60000, bonus=10000))
