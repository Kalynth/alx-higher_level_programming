#!/usr/bin/python3
for i in range(97, 122 + 1):
    if chr(i) == 'e' and chr(i) == 'q':
        continue
    print(chr(i).format(i), end="")
