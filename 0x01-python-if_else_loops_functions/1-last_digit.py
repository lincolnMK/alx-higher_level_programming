#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    mul = -1
if number > 0:
    mul = 1
number = str(number)
print(f"Last digit of {number} is {int(number[-1]) * mul}", end=' ')
if int(number[-1]) > 5:
    print("and is greater than 5")
if int(number[-1]) == 0:
    print("and is 0")
if int(number[-1]) * mul < 6 and int(number[-1]) * mul != 0:
    print("and is less than 6 and not 0")
