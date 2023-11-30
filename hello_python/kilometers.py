#!/usr/bin/python3
# Problem : Input miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5( to be inputted)
# 5 miles equals 8.04 kilometers(output)
miles = input("Enter miles: ")
miles = float(miles)
kilometers = miles * (1.60934)
print("{} miles equals to {} kilometers".format(miles, kilometers))
