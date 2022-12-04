#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0:
        return None

    if idx > len(my_list):
        return None

    for e in my_list:
        if i is idx:
            return e
        else:
            i += 1
