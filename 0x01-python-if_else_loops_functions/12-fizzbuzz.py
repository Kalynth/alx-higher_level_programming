#!/usr/bin/python3
def fizzbuzz(limit):
    for i in range(1, 100 + 1):
        if i % 3 == 0 and 1 % 5 == 0:
            print("FizzBuzz", end='')
        elif i % 3 == 0:
            print("Fizz", end='')
        elif i % 5 == 0:
            print("Buzz", end="")
        else:
            print(i, end="")

