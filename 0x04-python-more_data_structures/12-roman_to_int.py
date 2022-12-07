#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0

    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0

    for i in roman_string:
        if i == 'I':
            number += 1
        elif i == 'V':
            number += 5
        elif i == 'X':
            number += 10
        elif i == 'L':
            number += 50
        elif i == 'C':
            number += 100
        elif i == 'D':
            number += 500
        elif i == 'M':
            number += 1000
        else:
            return 0

    number -= 2 * roman_string.count('IV')
    number -= 2 * roman_string.count('IX')
    number -= 20 * roman_string.count('XL')
    number -= 20 * roman_string.count('XC')
    number -= 200 * roman_string.count('CD')
    number -= 200 * roman_string.count('CM')
    return number
