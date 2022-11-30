#!/usr/bin/python3
for i in range(97, 123):
    j = chr(i)
    if j == 'e' or j == 'q':
        j = ''
    else:
        print("{}".format(j), end='')
