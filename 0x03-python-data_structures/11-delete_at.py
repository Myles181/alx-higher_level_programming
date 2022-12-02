#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    xx = len(my_list)
    count = 0
    if idx > xx:
        return my_list
    if idx < 0:
        return my_list

    for i in range(0, len(my_list)):
        if i == idx:
            del(my_list[idx])
    return my_list
