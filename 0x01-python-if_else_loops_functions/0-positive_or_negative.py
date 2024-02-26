#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print("{0} is positive".format(number))

elif number == 0:
    print("{1} is 0".format(number))

else:
    print("{2} is negative".format(number))
