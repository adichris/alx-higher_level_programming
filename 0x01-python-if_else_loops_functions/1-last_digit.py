#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = number < 0
n = int(str(number)[-1])
if neg:
    n = 0 - n
if n == 0:
    print(f"Last digit of {number} is {n} and is 0")
elif n  < 6:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {n} and is greater than 5")
