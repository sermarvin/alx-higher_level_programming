#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = int(str(number)[-1])
if l_digit > 5 and number > 0:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")
elif number < 0:
    print(f"Last digit of {number} is -{l_digit} and is less that 6 and not 0")
else:
    print(f"Last digit of {number} is {l_digit} and is less that 6 and not 0")
