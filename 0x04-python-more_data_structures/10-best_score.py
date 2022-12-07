#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    count = 0
    for student, score in a_dictionary.items():
        if count != 0:
            if max_val < score:
                name = student
                max_val = score
        else:
            name = student
            max_val = score
        count += 1
    return name
