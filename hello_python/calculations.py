#!/usr/bin/python3
# ask user to input 2 values and store them in valuables num1 and num2
num1, num2 = input("Enter two numbers: ").split()
# Convert the strings into integers
num1_str = int(num1)
num2_str = int(num2)
# Add the values entered and store in sum
add = num1_str + num2_str
# Subtract values and store in difference
difference = num1_str - num2_str
# Multiply values and store in product
product = num1_str * num2_str
# Divide values and store in quotient
quotient = num1_str / num2_str
# Find the Modulus and store in remainder
remainder = num1_str % num2_str
# Print the output
print("{} add {} is {}".format(num1_str, num2_str, add))
print("{} subtract {} is {}".format(num1_str, num2_str, difference))
print("{} multiply {} is {}".format(num1_str, num2_str, product))
print("{} divide {} is {}".format( num1_str, num2_str, quotient))
print("{} modulus {} is {}".format(num1_str, num2_str, quotient))
