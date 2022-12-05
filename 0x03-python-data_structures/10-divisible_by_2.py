#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list()
    i = 0

    for i in range(0, len(my_list)):
        if int(my_list[i]) % 2 == 0:
            new_list.append(my_list[i])

    return new_list
