## a generator that produces numbers from 1 to 10.
def gen_number():
    for i in range(1, 11):
        yield i


## a generator function that generates even numbers between 1 and 50.

def even_number():
    for i in range(1, 51):
        if i % 2 == 0:
            yield i

'''
Create employee_generator().
Use yield to return one employee at a time.
Iterate through all employees.
Print employee ID and name.
'''

def employee_generator(employees):
    for employee in employees:
        if employee["id"] > 101:
            yield (employee["id"], employee["name"])