## Employee Generator – Advanced Filtering
'''
Create a generator function employee_generator().
Filter employees belonging to the IT department.
Salary must be greater than ₹50,000.
Return only id, name, and salary.
Use yield.
print records one at a time.
'''
MIN_SALARY = 50000
def employee_generator(employees):
    for employee in employees:
        if employee["department"] == "IT" and employee["salary"] > MIN_SALARY:
            yield {
                "id": employee["id"],
                "name": employee["name"],
                "salary": employee["salary"]
            }

## test method
employees = [
    {"id": 101, "name": "Amit", "department": "IT", "salary": 60000},
    {"id": 102, "name": "Rahul", "department": "HR", "salary": 70000},
    {"id": 103, "name": "Neha", "department": "IT", "salary": 45000},
    {"id": 104, "name": "Priya", "department": "IT", "salary": 80000}
]

for employee in employee_generator(employees):
    print(employee)
    
