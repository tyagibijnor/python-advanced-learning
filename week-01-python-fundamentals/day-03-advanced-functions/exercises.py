from generators import *
from iterators import *
even_num = even_number()
while True:
    try:
        print(next(even_num))
    except StopIteration:
        break
       

numbers = gen_number()
while True:
    try:
        print(next(numbers))
    except StopIteration:
        break    

employee_name = ["Navneet", "Amit", "Neha", "Kuhu"]
basic_iter(employee_name)

## Real-world Employee Generator
employees = [
    {"id": 101, "name": "Amit"},
    {"id": 102, "name": "Rahul"},
    {"id": 103, "name": "Neha"}
]

## using loop
for emp in employee_generator(employees):
    print(emp)

## using next
employee = employee_generator(employees)
print(next(employee))