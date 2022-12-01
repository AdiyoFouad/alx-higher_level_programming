#!/usr/bin/python3
n = 0
while n < 26:
    if n != 4 and n != 16:
        print('{:c}'.format(n + 97), end='')
    n += 1
