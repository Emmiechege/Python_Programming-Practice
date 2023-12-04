#!/usr/bin/python3
num = input("Enter a number ")
num = int(num)
if (num == 0):
    print("Number is zero")
elif (num < 0):
    print("Number is negative")
elif (num > 0):
    print("Number is positive")
else:
    print("Please input a valid number")

