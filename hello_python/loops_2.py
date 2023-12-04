#!/usr/bin/python3
# have user enter investment amount and expected interest
# Each year the inv increases by investment + inv * interest
# Print out earnings after a 10yr period

inv, interest = input("The investment and  exp interest are: ").split()
inv = float(inv)
interest = float(interest) * .01
for i in range(10):
    inv = inv + (inv * interest)

print("Ten years accrued investments is {:.2f}".format(inv))
