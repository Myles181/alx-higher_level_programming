#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if j > i:
            if i == 8 and j == 9:
                print('{0}{1}'.format(i, j))
                break
            print("{0}{1}".format(i, j), end=', ')
