#!/usr//bin/python3
# prompt user input
num1, operator, num2 = input('Enter the calculation: ').split()
# convert strings to integers
num1 = int(num1)
num2 = int(num2)
# parse inputs for calculations
if operator == "+":
    print("{} + {} = {}". format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}". format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}". format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}". format(num1, num2, num1 / num2))
else:
    print("Please enter a  mathematical  operation")
