#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    if idx < 0 or idx > len(my_list):
        return None

    for e in my_list:
        if i is idx:
            my_list[idx] = element
    return my_list
