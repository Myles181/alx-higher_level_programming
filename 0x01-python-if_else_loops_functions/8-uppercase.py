#cse(str):

    for i in str:

        if ord(i) >= ord('a') and ord(i) <= ord('z'):

            item = chr(ord(i) - (ord('a') - ord('A')))

        else:































































#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            item = chr(ord(i) - (ord('a') - ord('A')))

        else:
            item = i
        print("{}".format(item), end='')
    print()













































































            item = i
        print("{}".format(item), end='')
    print()
