#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > len(my_list):
        return None

    for e in my_list:
        if i is idx:
            e = element
        new_list.append(e)

    return new_list
