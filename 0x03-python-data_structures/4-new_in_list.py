#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    new_list = []
    if idx < 0 or idx > len(my_list):
        return None

    for e in my_list:
        if i is idx:
            e = element
        else:
            i += 1
        new_list.append(e)

    return new_list
