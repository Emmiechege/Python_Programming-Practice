#!/usr/bin/python3
# 1 - 18 important age
# 21, 50, > 65 important age
# All others, not important
# Receive age and store in age
age = eval(input("Enter age: "))
# if age is 1 to 18, its important
if (age == 1) and (age >= 18):
    print("Important birthday")
elif (age == 21) or (age == 50):
    print("Somehow important birthday")
elif (age >= 65):
    print("Very Important")
else:
    print("Sorry, not important")
