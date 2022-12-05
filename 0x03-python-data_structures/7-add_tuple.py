#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def check_tup(tup):
        if len(tup) == 1:
            tup = (tup[0], 0)
            return tup

        elif len(tup) == 0:
            tup = (0, 0)
            return tup

        else:
            return tup

    temp_1, temp_2 = check_tup(tuple_a), check_tup(tuple_b)
    sum_1 = temp_1[0] + temp_2[0]
    sum_2 = temp_1[1] + temp_2[1]
    new_tuple = (sum_1, sum_2)
    return new_tuple
