## import json
import json

employee = {
    "name": "Navneet",
    "role": "Software Development Manager",
    "skills": ["Python", "SQL", "AI"]
}

## write JSON
with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)

## read JSON
with open("employee.json", "r") as file:
    data = json.load(file)

print(data["name"])


## error handling
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