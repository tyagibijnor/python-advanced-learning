print("TEST FOR ARGRS")

def salary_report(*args):
    total_salary = sum(args)
    average_salary = total_salary / len(args) if args else 0
    highest_salary = max(args) if args else 0
    print("--" * 10)
    print(f"Total Salary: {total_salary}")
    print(f"Average Salary: {average_salary}")
    print(f"Highest Salary: {highest_salary}")

salary_report(45000, 65000, 80000, 55000)