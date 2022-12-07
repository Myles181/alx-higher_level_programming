#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0

    for i, j in dict(my_list).items():
        numerator += (i * j)

    for num in dict(my_list).values():
        denominator += num
    return numerator / denominator
