#!/usr/bin/env python3

number = __import__('random').randint(-10000, 10000)
last = number % 10

if number < 0 and digit !=0:
    digit -= 10

if last == 0:
    print(f"Last digit of {number} is {last} and is 0")

elif last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")

else:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
