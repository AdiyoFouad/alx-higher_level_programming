#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    n = -int(str(number)[-1])

else:
    n = int(str(number)[-1])

if n > 5:
    print("Last digit of", number, "is", n, "and is greater than 5")

if n == 0:
    print("Last digit of", number, "is", n, "and is", n)

if n < 6 and n != 0:
    print("Last digit of", number, "is", n, "and is less than 6 and not 0")
