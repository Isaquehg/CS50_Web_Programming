import sys

try:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
except ValueError:
    print("Invalid input!")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Cannot divide by zero!")
    sys.exit(1)
print(f"The result of {x} / {y} is {result}")