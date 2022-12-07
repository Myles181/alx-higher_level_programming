#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_t = []
    if value in a_dictionary.values():
        for key, item in a_dictionary.items():
            if item == value:
                list_t.append(key)

    for i in list_t:
        del a_dictionary[i]

    return a_dictionary
