# Handle ValueError and ZeroDivisionError using try/except/else/finally.

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