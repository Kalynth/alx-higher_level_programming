#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1, -1):
        if i % 2 != 0:
            print(i, end="")
        else:
            i = i - 32
            print(i, end="")
