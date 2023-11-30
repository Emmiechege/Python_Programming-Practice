# ask user to input 2 values and store them in valuables num1 and num2
num1, num2 = input("Enter two numbers: ").split()
# Convert the strings into integers
int(num1)
int(num2)
# Add the values entered and store in sum
add = num1 + num2
# Subtract values and store in difference
diff = num1 - num2
# Multiply values and store in product
product = num1 * num2
# Divide values and store in quotient
quotient = num1 / num2
# Find the Modulus and store in remainder
remainder = num1 % num2
# Print the output
print("{} add {} is {}".format, num1, num2, add)
print("{} subtract {} is {}".format, num1, num2, diff)
print("{} multiply {} is {}".format, num1, num2, product)
print("{} divide {} is {}".format, num1, num2, quotient)
print("{} modulus {} is {}".format, num1, num2, quotient)
