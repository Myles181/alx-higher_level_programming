#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

numb = abs(number) % 10
if number < 0:
    numb = (abs(number) % 10) * -1

print("Last digit of {} is {}".format(number, numb, end=' ')

if numb == 0:
    print("and is 0")

elif numb > 5:
    print("and is greater than 5")

elif (numb < 6) and (numb != 0):
    print("and is less than 6 and not 0")
