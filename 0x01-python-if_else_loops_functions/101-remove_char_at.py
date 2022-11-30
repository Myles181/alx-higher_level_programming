#!/usr/bin/python3

def remove_char_at(str, n):
    count = 0
    string = ''
    for i in str:
        if count != n:
            string += i
        count += 1
    return string
