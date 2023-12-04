#!/usr/bin/python3
# if age is 5 go to kindergatten
# ages 6 to 17, go to elementary
# Above age 17 go to college
# Else, not in school
# Use less than 10 lines to complete
age = eval(input("Enter the age: "))
if (age <= 5):
    print("Go to kindergatten")
elif (age >= 6) and (age <= 17):
    print("Go to elementary")
elif not (age > 17) or (age <= 25):
    print("Go to college")
else:
    print("Not in school")
