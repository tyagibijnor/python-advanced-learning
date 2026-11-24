"""Standalone JSON and exception-handling exercises."""

import json
from pathlib import Path

employee = {
    "name": "Rahul Sharma",
    "role": "Software Developer",
    "skills": ["Python", "SQL", "AI"],
}

employee_file = Path("employee.json")
with employee_file.open("w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

with employee_file.open("r", encoding="utf-8") as file:
    data = json.load(file)

print(data["name"])

try:
    number = int(input("Enter number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Program execution completed.")
